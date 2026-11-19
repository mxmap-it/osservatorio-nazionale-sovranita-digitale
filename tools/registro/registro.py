#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Registro attività dell'Osservatorio — raccolta, sintesi e bot Telegram.

Una sola sorgente: i commit dei repository di ciascun «contesto»
(data/registro/contesti.json). Da lì:

  raccogli    scarica i commit (API GitHub) nella cache locale .registro-cache/
              (NON in git: contiene anche i messaggi dei repo privati) e, per
              MxMap, i KPI della scansione notturna di ogni giorno;
  sintetizza  per ogni (giorno, contesto) nuovo o cambiato chiede a Claude una
              sintesi IT+EN e la scrive in data/registro/giorni/AAAA-MM-GG.json;
  settimana   sintesi settimanale in data/registro/settimane/AAAA-Www.json;
  telegram    posta sul canale: «live» (voci rilevanti appena sintetizzate),
              «giornaliero» (ieri, alle 8:30) e «settimanale» (lunedì 8:30);
  ciclo       quello che fa il workflow ogni ora: raccogli + sintetizza +
              live + (se è l'ora) riepilogo delle 8:30.

I link ai commit e alle issue sono costruiti dal codice, mai dal modello: il
modello sceglie solo fra identificativi che gli diamo. Per i contesti con
"pubblico": false non si pubblicano link ai commit né alle issue.

Motori di sintesi:
  --motore api  SDK Anthropic (ANTHROPIC_API_KEY) — il workflow GitHub;
  --motore cli  Claude Code headless (`claude -p`) — usato per lo storico.

Uso tipico:
  python tools/registro/registro.py ciclo                       # come l'Action
  python tools/registro/registro.py raccogli --dal 2026-05-01
  python tools/registro/registro.py sintetizza --dal 2026-05-01 --al 2026-11-18 --motore cli
  python tools/registro/registro.py settimana --tutte --motore cli
  python tools/registro/registro.py telegram giornaliero --prova   # stampa, non posta
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATI = os.path.join(ROOT, "data", "registro")
GIORNI = os.path.join(DATI, "giorni")
SETTIMANE = os.path.join(DATI, "settimane")
CACHE = os.path.join(ROOT, ".registro-cache")
STATO = os.path.join(ROOT, "tools", "registro", "stato-telegram.json")
ROMA = ZoneInfo("Europe/Rome")
SITO = "https://osservatorio.mxmap.it"
MODELLO = os.environ.get("REGISTRO_MODELLO", "claude-opus-5-5")
INIZIO = "2026-05-02"  # primo commit di MxMap Italia

TIPI = ["pubblicazione", "dati", "analisi", "sviluppo", "bugfix", "metodo", "infrastruttura", "documentazione"]
TIPI_LABEL = {
    "pubblicazione": ("Pubblicazione", "Publication"), "dati": ("Dati", "Data"),
    "analisi": ("Analisi", "Analysis"), "sviluppo": ("Sviluppo", "Development"),
    "bugfix": ("Correzione", "Fix"), "metodo": ("Metodo", "Method"),
    "infrastruttura": ("Infrastruttura", "Infrastructure"), "documentazione": ("Documentazione", "Documentation"),
}


# ───────────────────────────── utilità ─────────────────────────────

def log(*a):
    print(*a, file=sys.stderr, flush=True)


def leggi_json(p, default=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def scrivi_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")
    os.replace(tmp, p)


def contesti():
    return leggi_json(os.path.join(DATI, "contesti.json"))


def oggi_roma():
    return dt.datetime.now(ROMA).date()


def giorno_roma(iso_utc):
    return dt.datetime.fromisoformat(iso_utc.replace("Z", "+00:00")).astimezone(ROMA).date().isoformat()


def settimana_di(giorno):
    y, w, _ = dt.date.fromisoformat(giorno).isocalendar()
    return f"{y}-W{w:02d}"


def giorni_settimana(sett):
    y, w = sett.split("-W")
    lun = dt.date.fromisocalendar(int(y), int(w), 1)
    return [(lun + dt.timedelta(days=i)).isoformat() for i in range(7)]


def intervallo(dal, al):
    d, a = dt.date.fromisoformat(dal), dt.date.fromisoformat(al)
    while d <= a:
        yield d.isoformat()
        d += dt.timedelta(days=1)


# ───────────────────────────── GitHub ─────────────────────────────

def gh_token():
    for k in ("REGISTRO_GH_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(k):
            return os.environ[k]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def gh_get(path, params=None):
    url = "https://api.github.com/" + path.lstrip("/")
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json", "User-Agent": "osservatorio-registro",
        **({"Authorization": "Bearer " + gh_token()} if gh_token() else {})})
    for tentativo in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 502, 503) and tentativo < 3:
                time.sleep(10 * (tentativo + 1))
                continue
            if e.code in (404, 409):  # repo inaccessibile o vuoto
                log(f"  GitHub {e.code} su {path}")
                return None
            raise


def raw_github(repo, sha, file):
    url = f"https://raw.githubusercontent.com/{repo}/{sha}/{file}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "osservatorio-registro"}), timeout=60) as r:
            return json.load(r)
    except Exception as e:
        log(f"  raw {url}: {e}")
        return None


# ───────────────────────────── raccolta ─────────────────────────────

URL_RE = re.compile(r"https?://[^\s)\]>»\"'`,;]+")
ISSUE_RE = re.compile(r"(?<![\w/])#(\d{1,4})\b")


def cache_repo(repo):
    return os.path.join(CACHE, "commit", repo.replace("/", "__") + ".json")


def mappa_url_osservatorio(file):
    """content/it/news/x.md -> https://osservatorio.mxmap.it/news/x/ (solo pagine)."""
    s = re.match(r"static/((?:pdf|slide)/[^_/][^/]*\.(?:pdf|pptx))$", file)
    if s:
        return f"{SITO}/{s.group(1)}"
    m = re.match(r"content/(it|en)/(.+?)(?:/index|/_index)?\.md$", file)
    if not m:
        return None
    lang, path = m.groups()
    if path in ("_index", "index"):
        path = ""
    base = SITO + ("/en/" if lang == "en" else "/")
    return base + (path.strip("/") + "/" if path else "")


def raccogli(dal, file_osservatorio=True):
    """Scarica nella cache i commit dal giorno `dal` (Europe/Rome) in poi."""
    since = (dt.datetime.combine(dt.date.fromisoformat(dal), dt.time(0), ROMA) - dt.timedelta(hours=1)).astimezone(dt.timezone.utc)
    falliti = []
    for c in contesti():
        for repo in c["repo"]:
            p = cache_repo(repo)
            cache = leggi_json(p, {})
            n_nuovi, pagina = 0, 1
            while True:
                lot = gh_get(f"repos/{repo}/commits", {"since": since.strftime("%Y-%m-%dT%H:%M:%SZ"), "per_page": 100, "page": pagina})
                if lot is None and pagina == 1:
                    falliti.append(repo)  # inaccessibile: il contesto NON va sintetizzato (si azzererebbe)
                if not lot:
                    break
                for x in lot:
                    sha = x["sha"]
                    if sha in cache:
                        continue
                    msg = x["commit"]["message"]
                    titolo, _, corpo = msg.partition("\n")
                    data = x["commit"]["committer"]["date"] or x["commit"]["author"]["date"]
                    rec = {
                        "repo": repo, "sha": sha, "data": data, "giorno": giorno_roma(data),
                        "autore": x["commit"]["author"]["name"],
                        "bot": (x.get("author") or {}).get("type") == "Bot" or "[bot]" in x["commit"]["author"]["name"],
                        "titolo": titolo.strip(), "corpo": corpo.strip()[:2500],
                    }
                    if file_osservatorio and repo.endswith("/osservatorio-nazionale-sovranita-digitale") and not rec["bot"]:
                        det = gh_get(f"repos/{repo}/commits/{sha}") or {}
                        rec["file"] = [f["filename"] for f in det.get("files", [])][:200]
                    cache[sha] = rec
                    n_nuovi += 1
                if len(lot) < 100:
                    break
                pagina += 1
            scrivi_json(p, cache)
            log(f"raccolti {n_nuovi:4d} nuovi commit da {repo} (totale cache {len(cache)})")
    scrivi_json(os.path.join(CACHE, "falliti.json"), falliti)
    if falliti:
        log(f"ATTENZIONE: repo non leggibili, contesti saltati: {falliti}")
    raccogli_kpi(dal)


def raccogli_kpi(dal):
    """KPI dell'ultima scansione notturna di ogni giorno (contesti con "scansioni")."""
    for c in contesti():
        s = c.get("scansioni")
        if not s:
            continue
        p = os.path.join(CACHE, "kpi", c["id"] + ".json")
        kpi = leggi_json(p, {})
        cache = leggi_json(cache_repo(s["repo"]), {})
        ultimi = {}
        for rec in cache.values():
            if rec["giorno"] >= dal and re.search(s["titolo"], rec["titolo"]):
                if rec["giorno"] not in ultimi or rec["data"] > ultimi[rec["giorno"]]["data"]:
                    ultimi[rec["giorno"]] = rec
        for g, rec in sorted(ultimi.items()):
            if g in kpi and kpi[g].get("sha") == rec["sha"]:
                continue
            d = raw_github(s["repo"], rec["sha"], s["file"])
            if not d:
                continue
            sov = d.get("sovereignty", {})
            kpi[g] = {
                "sha": rec["sha"],
                "n_enti": (d.get("totals") or {}).get("n_entities"),
                "copertura": (d.get("totals") or {}).get("coverage_pct"),
                **{k: (sov.get(k) or {}).get("pct") for k in ("extra_eu", "eu_non_it", "it", "unknown")},
            }
        scrivi_json(p, kpi)
        log(f"KPI scansioni {c['id']}: {len(kpi)} giorni in cache")


# ───────────────────────────── sintesi ─────────────────────────────

SCHEMA_GIORNO = {
    "type": "object",
    "properties": {"voci": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "tipo": {"type": "string", "enum": TIPI},
            "rilevante": {"type": "boolean"},
            "titolo_it": {"type": "string"}, "titolo_en": {"type": "string"},
            "sintesi_it": {"type": "string"}, "sintesi_en": {"type": "string"},
            "commit": {"type": "array", "items": {"type": "string"}},
            "link": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["tipo", "rilevante", "titolo_it", "titolo_en", "sintesi_it", "sintesi_en", "commit", "link"],
        "additionalProperties": False}}},
    "required": ["voci"], "additionalProperties": False,
}

SISTEMA = """Sei il redattore del «Registro attività» dell'Osservatorio Nazionale Sovranità Digitale (osservatorio.mxmap.it), un progetto civico, open source e multi-stakeholder che misura la dipendenza giurisdizionale della Pubblica Amministrazione italiana da fornitori digitali extra-UE.

Ricevi i commit di UN contesto di lavoro in UN giorno. Scrivi le voci del registro di quel giorno: raggruppa i commit per risultato o tema (una voce = un avanzamento comprensibile, non un commit), di solito 1-4 voci al giorno, di più solo se il lavoro è davvero distinto.

Per ogni voce:
- titolo_it / titolo_en: breve e concreto (max ~90 caratteri), senza punto finale.
- sintesi_it / sintesi_en: 1-3 frasi che dicono CHE COSA è cambiato e PERCHÉ conta, per un lettore informato ma non tecnico (giornalista, decisore, attivista). Riporta i numeri esattamente come nei commit, nel formato della lingua (IT: 22.922 e 43,3%; EN: 22,922 and 43.3%). Se un dato è dichiarato provvisorio, parziale o in corso, dillo.
- tipo: pubblicazione (contenuti/pagine/report/PDF/rendiconti pubblicati), dati (nuovi dati o rilevazioni), analisi (risultati di analisi), sviluppo (funzioni nuove), bugfix, metodo (scelte metodologiche, decisioni), infrastruttura (server, automazioni, deploy), documentazione.
- rilevante: true SOLO per ciò che merita una notifica immediata alla community: nuove pubblicazioni o pagine, risultati o numeri nuovi, release, cambi di metodo che cambiano i numeri. false per manutenzione, refactoring, stato interno, piccoli fix.
- commit: gli identificativi (c1, c2, …) dei commit su cui si basa la voce. Ogni commit al massimo in una voce; puoi ignorare i commit irrilevanti (stato interno, sync, log).
- link: identificativi (u1, u2, …) scelti SOLO dalla lista di URL fornita, i più utili per approfondire (0-3). Non inventare mai URL.

Regole di tono (vincolanti): civico, sobrio, non ideologico, verificabile. Niente enfasi o marketing («rivoluzionario», «importantissimo»). Non attribuire illeciti a aziende o persone. Non inventare nulla che non sia nei commit: se il senso di un commit non è chiaro, descrivilo in modo neutro o tralascialo. Nomi di persone: solo «Fabio» o «il fondatore» se compare una sua decisione; nessun altro nome privato. Non citare Claude, LLM o assistenti come autori del lavoro, salvo quando l'uso di un modello è parte del metodo descritto.
L'inglese è una traduzione fedele dell'italiano, non un testo diverso."""

SISTEMA_PRIVATO = """
ATTENZIONE: questo contesto proviene da un repository PRIVATO. Le voci saranno pubbliche. Riporta solo risultati, avanzamenti e scelte di metodo. OMETTI del tutto: nomi di server, host, IP, tunnel, proxy residenziali, password, credenziali, percorsi interni, cron, cruscotti interni, nomi di file interni, dettagli di sicurezza operativa. Se un giorno contiene solo lavoro interno di questo tipo, restituisci una sola voce sobria (tipo infrastruttura, rilevante false) oppure nessuna voce."""


def commit_del_giorno(c, giorno):
    esc = [re.compile(r) for r in c.get("escludi", [])]
    out = []
    for repo in c["repo"]:
        for rec in leggi_json(cache_repo(repo), {}).values():
            if rec["giorno"] != giorno or rec["bot"] or any(r.search(rec["titolo"]) for r in esc):
                continue
            out.append(rec)
    return sorted(out, key=lambda r: r["data"])


def impronta(commits):
    return hashlib.sha256("|".join(sorted(r["sha"] for r in commits)).encode()).hexdigest()[:16]


def costruisci_input(c, giorno, commits):
    urls, righe = [], []
    def url_id(u):
        u = u.rstrip(".")
        if u not in urls:
            urls.append(u)
    for r in commits:
        for u in URL_RE.findall(r["titolo"] + "\n" + r["corpo"]):
            if c["pubblico"]:
                url_id(u)
        for f in r.get("file", []):
            u = mappa_url_osservatorio(f)
            if u:
                url_id(u)
    if c.get("sito"):
        url_id(c["sito"])
    for i, r in enumerate(commits, 1):
        corpo = ("\n    " + r["corpo"].replace("\n", "\n    ")) if r["corpo"] else ""
        righe.append(f"c{i} [{r['data'][11:16]} UTC, {r['repo'].split('/')[1]}] {r['titolo']}{corpo}")
    testo = (f"CONTESTO: {c['nome']['it']}\nDESCRIZIONE: {c['descrizione']}\nGIORNO: {giorno}\n\n"
             f"COMMIT ({len(commits)}):\n" + "\n".join(righe) +
             "\n\nURL DISPONIBILI PER I LINK:\n" + ("\n".join(f"u{i} {u}" for i, u in enumerate(urls, 1)) or "(nessuno)"))
    return testo, urls


def chiama_modello(sistema, testo, schema, motore, max_tokens=16000):
    if motore == "cli":
        prompt = sistema + "\n\n────────\n\n" + testo
        cmd = ["claude", "-p", "--output-format", "json", "--json-schema", json.dumps(schema),
               "--model", MODELLO, "--tools", ""]
        for tentativo in range(3):
            r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=900, cwd="/tmp")
            try:
                d = json.loads(r.stdout)
                if not d.get("is_error") and d.get("structured_output") is not None:
                    return d["structured_output"]
                log(f"  cli errore: {d.get('result')!r:.200}")
            except json.JSONDecodeError:
                log(f"  cli output non JSON: {r.stdout[:200]!r} {r.stderr[:200]!r}")
            time.sleep(20 * (tentativo + 1))
        raise RuntimeError("claude -p non ha prodotto una sintesi valida")
    import anthropic  # solo per il motore api
    client = anthropic.Anthropic()
    with client.beta.messages.stream(
        model=MODELLO, max_tokens=max_tokens,
        betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        thinking={"type": "adaptive"}, output_config={"effort": "medium", "format": {"type": "json_schema", "schema": schema}},
        system=sistema, messages=[{"role": "user", "content": testo}],
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason == "refusal":
        raise RuntimeError(f"rifiuto del modello: {msg.stop_details}")
    if msg.stop_reason == "max_tokens":
        raise RuntimeError("sintesi troncata (max_tokens)")
    return json.loads(next(b.text for b in msg.content if b.type == "text"))


def file_giorno(g):
    return os.path.join(GIORNI, g + ".json")


def carica_giorno(g):
    return leggi_json(file_giorno(g)) or {"data": g, "settimana": settimana_di(g), "fonte": {}, "voci": []}


def salva_giorno(d):
    ordine = {c["id"]: i for i, c in enumerate(contesti())}
    d["voci"].sort(key=lambda v: (ordine.get(v["contesto"], 99), not v["rilevante"]))
    if not d["voci"] and not d.get("kpi"):
        if os.path.exists(file_giorno(d["data"])):
            os.remove(file_giorno(d["data"]))
        return
    scrivi_json(file_giorno(d["data"]), d)


def aggiorna_kpi_giorno(d):
    for c in contesti():
        if not c.get("scansioni"):
            continue
        kpi = leggi_json(os.path.join(CACHE, "kpi", c["id"] + ".json"), {})
        g = d["data"]
        if g in kpi:
            prec = max((k for k in kpi if k < g), default=None)
            k = {x: y for x, y in kpi[g].items() if x != "sha"}
            if prec:
                k["delta_extra_eu"] = round((kpi[g].get("extra_eu") or 0) - (kpi[prec].get("extra_eu") or 0), 2)
            d["kpi"] = k


def sintetizza_giorno(g, motore, forza=False):
    d = carica_giorno(g)
    cambiato = False
    falliti = set(leggi_json(os.path.join(CACHE, "falliti.json"), []))
    for c in contesti():
        if falliti & set(c["repo"]):
            continue
        commits = commit_del_giorno(c, g)
        imp = impronta(commits) if commits else ""
        if not forza and d["fonte"].get(c["id"], "") == imp:
            continue
        cambiato = True
        d["voci"] = [v for v in d["voci"] if v["contesto"] != c["id"]]
        d["fonte"][c["id"]] = imp
        if not commits:
            continue
        testo, urls = costruisci_input(c, g, commits)
        log(f"  {g} {c['id']}: {len(commits)} commit → sintesi ({motore})")
        out = chiama_modello(SISTEMA + ("" if c["pubblico"] else SISTEMA_PRIVATO), testo, SCHEMA_GIORNO, motore)
        for n, v in enumerate(out.get("voci", []), 1):
            idx = [int(x[1:]) - 1 for x in v["commit"] if re.fullmatch(r"c\d+", x) and 0 < int(x[1:]) <= len(commits)]
            rif = [commits[i] for i in idx]
            issue = sorted({f"{r['repo']}#{m}" for r in rif for m in ISSUE_RE.findall(r["titolo"] + " " + r["corpo"])},
                           key=lambda s: (s.split("#")[0], int(s.split("#")[1])))
            link = [urls[int(x[1:]) - 1] for x in v["link"] if re.fullmatch(r"u\d+", x) and 0 < int(x[1:]) <= len(urls)]
            d["voci"].append({
                "id": f"{g}-{c['id']}-{n}",
                "contesto": c["id"], "tipo": v["tipo"], "rilevante": bool(v["rilevante"]),
                "titolo": {"it": v["titolo_it"].strip(), "en": v["titolo_en"].strip()},
                "sintesi": {"it": v["sintesi_it"].strip(), "en": v["sintesi_en"].strip()},
                "commit": [f"{r['repo']}@{r['sha'][:10]}" for r in rif] if c["pubblico"] else [],
                "n_commit": len(rif),
                "issue": issue if c["pubblico"] else [],
                "link": link,
            })
    vecchio_kpi = d.get("kpi")
    aggiorna_kpi_giorno(d)
    if cambiato or d.get("kpi") != vecchio_kpi:
        salva_giorno(d)
    return cambiato


def sintetizza(dal, al, motore, forza=False):
    for g in intervallo(dal, al):
        try:
            sintetizza_giorno(g, motore, forza)
        except Exception as e:
            log(f"  ERRORE {g}: {e}")
            if motore == "api":
                raise


# ───────────────────────────── settimana ─────────────────────────────

SCHEMA_SETTIMANA = {
    "type": "object",
    "properties": {
        "titolo_it": {"type": "string"}, "titolo_en": {"type": "string"},
        "sintesi_it": {"type": "string"}, "sintesi_en": {"type": "string"},
        "punti": {"type": "array", "items": {"type": "object", "properties": {
            "contesto": {"type": "string"}, "testo_it": {"type": "string"}, "testo_en": {"type": "string"},
            "voci": {"type": "array", "items": {"type": "string"}}},
            "required": ["contesto", "testo_it", "testo_en", "voci"], "additionalProperties": False}},
    },
    "required": ["titolo_it", "titolo_en", "sintesi_it", "sintesi_en", "punti"], "additionalProperties": False,
}

SISTEMA_SETTIMANA = """Sei il redattore del «Registro attività» dell'Osservatorio Nazionale Sovranità Digitale. Ricevi le voci giornaliere del registro di UNA settimana (già pubbliche) e scrivi il riepilogo settimanale.

- titolo_it / titolo_en: il filo della settimana in una riga (max ~90 caratteri).
- sintesi_it / sintesi_en: 2-4 frasi su che cosa è avanzato davvero nella settimana e perché conta.
- punti: per ogni contesto che ha avuto attività, 1 punto (contesto = id del contesto) con 1-3 frasi (testo_it/testo_en) che riassumono i progressi principali, e in «voci» gli id delle voci giornaliere più importanti (1-4) per approfondire.
Stesse regole di tono: sobrio, civico, verificabile, numeri esatti e nel formato della lingua, niente enfasi, niente di inventato, niente nomi privati. L'inglese traduce fedelmente l'italiano."""


def sintetizza_settimana(sett, motore, forza=False):
    p = os.path.join(SETTIMANE, sett + ".json")
    giorni = [carica_giorno(g) for g in giorni_settimana(sett)]
    voci = [v for d in giorni for v in d["voci"]]
    if not voci:
        return None
    imp = hashlib.sha256(json.dumps([[v["id"], v["titolo"]["it"]] for v in voci]).encode()).hexdigest()[:16]
    vecchio = leggi_json(p)
    if vecchio and vecchio.get("fonte") == imp and not forza:
        return vecchio
    nomi = {c["id"]: c["nome"]["it"] for c in contesti()}
    righe = [f"[{v['id']}] ({nomi.get(v['contesto'])}, {v['tipo']}{', RILEVANTE' if v['rilevante'] else ''}) "
             f"{v['titolo']['it']} — {v['sintesi']['it']}" for v in voci]
    kpi = [f"{d['data']}: {d['kpi']}" for d in giorni if d.get("kpi")]
    testo = (f"SETTIMANA {sett} ({giorni_settimana(sett)[0]} – {giorni_settimana(sett)[-1]})\n\nCONTESTI: "
             + ", ".join(f"{k} = {n}" for k, n in nomi.items()) + "\n\nVOCI:\n" + "\n".join(righe)
             + ("\n\nKPI SCANSIONE NOTTURNA MXMAP (percentuali):\n" + "\n".join(kpi) if kpi else ""))
    log(f"  settimana {sett}: {len(voci)} voci → sintesi ({motore})")
    out = chiama_modello(SISTEMA_SETTIMANA, testo, SCHEMA_SETTIMANA, motore)
    ids = {v["id"] for v in voci}
    d = {
        "settimana": sett, "dal": giorni_settimana(sett)[0], "al": giorni_settimana(sett)[-1], "fonte": imp,
        "titolo": {"it": out["titolo_it"], "en": out["titolo_en"]},
        "sintesi": {"it": out["sintesi_it"], "en": out["sintesi_en"]},
        "punti": [{"contesto": x["contesto"], "testo": {"it": x["testo_it"], "en": x["testo_en"]},
                   "voci": [i for i in x["voci"] if i in ids]} for x in out["punti"] if x["contesto"] in nomi],
        "n_voci": len(voci),
    }
    scrivi_json(p, d)
    return d


# ───────────────────────────── Telegram ─────────────────────────────

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def url_voce(v):
    return f"{SITO}/registro/#{v['id']}"


def link_voce(v, max_link=2):
    out = []
    for u in v["link"][:max_link]:
        etichetta = urllib.parse.urlparse(u).netloc.replace("www.", "")
        out.append(f'<a href="{esc(u)}">{esc(etichetta)}</a>')
    for i in v["issue"][:2]:
        repo, n = i.split("#")
        out.append(f'<a href="https://github.com/{repo}/issues/{n}">#{n}</a>')
    if v["commit"]:
        repo, sha = v["commit"][-1].split("@")
        out.append(f'<a href="https://github.com/{repo}/commit/{sha}">commit</a>')
    return " · ".join(out)


def mesi_it(d):
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    giorni = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
    x = dt.date.fromisoformat(d)
    return f"{giorni[x.weekday()]} {x.day} {mesi[x.month - 1]}"


def pct(x):
    return "—" if x is None else f"{x:.1f}".replace(".", ",") + "%"


def riga_kpi(k):
    delta = k.get("delta_extra_eu")
    d = "" if not delta else f" ({'+' if delta > 0 else '−'}{abs(delta):.1f} punti)".replace(".", ",")
    n = f"{k['n_enti']:,}".replace(",", ".") if k.get("n_enti") else "—"
    return f"🛰️ Scansione notturna: {n} enti · extra-UE {pct(k.get('extra_eu'))}{d} · italiani {pct(k.get('it'))}"


def testo_giornaliero(g):
    d = carica_giorno(g)
    if not d["voci"]:
        return None
    cs = {c["id"]: c for c in contesti()}
    parti = [f"📋 <b>Osservatorio — attività di {mesi_it(g)}</b>"]
    if d.get("kpi"):
        parti.append(riga_kpi(d["kpi"]))
    for cid, c in cs.items():
        vv = [v for v in d["voci"] if v["contesto"] == cid]
        if not vv:
            continue
        blocco = [f"\n{c['emoji']} <b>{esc(c['nome']['it'])}</b>"]
        for v in vv:  # sintesi completa solo per le voci rilevanti, il resto in una riga
            lk = link_voce(v, 1)
            if v["rilevante"]:
                blocco.append(f"• <b>{esc(v['titolo']['it'])}</b> — {esc(v['sintesi']['it'])}" + (f"\n  {lk}" if lk else ""))
            else:
                blocco.append(f'• <a href="{url_voce(v)}">{esc(v["titolo"]["it"])}</a>')
        parti.append("\n".join(blocco))
    parti.append(f'\n📚 <a href="{SITO}/registro/#g-{g}">Registro completo</a>')
    return "\n".join(parti)


def testo_settimanale(sett):
    s = leggi_json(os.path.join(SETTIMANE, sett + ".json"))
    if not s:
        return None
    cs = {c["id"]: c for c in contesti()}
    voci = {v["id"]: v for g in giorni_settimana(sett) for v in carica_giorno(g)["voci"]}
    dal, al = dt.date.fromisoformat(s["dal"]), dt.date.fromisoformat(s["al"])
    mese = lambda g: mesi_it(g).split()[-1]
    periodo = f"{dal.day}" + (f" {mese(s['dal'])}" if dal.month != al.month else "") + f"–{al.day} {mese(s['al'])} {al.year}"
    parti = [f"🗓️ <b>Settimana dell'Osservatorio — {periodo}</b>",
             f"<i>{esc(s['titolo']['it'])}</i>", "", esc(s["sintesi"]["it"])]
    for p in s["punti"]:
        c = cs.get(p["contesto"])
        if not c:
            continue
        righe = [f"\n{c['emoji']} <b>{esc(c['nome']['it'])}</b>", esc(p["testo"]["it"])]
        for vid in p["voci"][:3]:
            v = voci.get(vid)
            if v:
                righe.append(f'• <a href="{url_voce(v)}">{esc(v["titolo"]["it"])}</a>')
        parti.append("\n".join(righe))
    parti.append(f'\n📚 <a href="{SITO}/registro/#s-{sett}">Tutte le voci della settimana</a> · {s["n_voci"]} voci')
    return "\n".join(parti)


def testo_live(v):
    c = {c["id"]: c for c in contesti()}[v["contesto"]]
    lk = link_voce(v, 3)
    return (f"{c['emoji']} <b>{esc(c['breve']['it'])}</b> · {TIPI_LABEL[v['tipo']][0]}\n"
            f"<b>{esc(v['titolo']['it'])}</b>\n{esc(v['sintesi']['it'])}" + (f"\n{lk}" if lk else ""))


def spezza(testo, lim=4000):
    if len(testo) <= lim:
        return [testo]
    pezzi, cur = [], ""
    for blocco in testo.split("\n\n"):
        if len(cur) + len(blocco) + 2 > lim and cur:
            pezzi.append(cur)
            cur = ""
        cur = (cur + "\n\n" + blocco) if cur else blocco
    return pezzi + [cur]


def invia(testo, prova=False):
    tok, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if prova or not (tok and chat):
        print(("— PROVA —\n" if prova else "— TELEGRAM NON CONFIGURATO (manca TELEGRAM_BOT_TOKEN/CHAT_ID) —\n") + testo + "\n")
        return prova  # in prova consideriamo «inviato», senza config no
    for pezzo in spezza(testo):
        data = urllib.parse.urlencode({"chat_id": chat, "text": pezzo, "parse_mode": "HTML",
                                       "link_preview_options": json.dumps({"is_disabled": True})}).encode()
        with urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/sendMessage", data=data, timeout=30) as r:
            if not json.load(r).get("ok"):
                raise RuntimeError("Telegram ha rifiutato il messaggio")
        time.sleep(1)
    return True


def stato():
    return leggi_json(STATO, {"commit_postati": [], "voci_postate": [], "giornaliero": "", "settimanale": ""})


def salva_stato(s):
    s["commit_postati"] = s["commit_postati"][-3000:]
    s["voci_postate"] = s["voci_postate"][-3000:]
    scrivi_json(STATO, s)


def telegram_live(prova=False):
    s = stato()
    gia = set(s["commit_postati"])
    oggi = oggi_roma()
    for g in [(oggi - dt.timedelta(days=1)).isoformat(), oggi.isoformat()]:
        for v in carica_giorno(g)["voci"]:
            if not v["rilevante"] or v["id"] in s["voci_postate"]:
                continue
            chiave = v["commit"] or [v["id"]]
            if v["commit"] and sum(c in gia for c in chiave) * 2 >= len(chiave):
                continue  # già annunciata (la voce è stata solo riscritta)
            if invia(testo_live(v), prova) and not prova:
                s["voci_postate"].append(v["id"])
                s["commit_postati"] += chiave
                gia.update(chiave)
    if not prova:
        salva_stato(s)


def telegram_riepilogo(prova=False, forza=False, motore="api"):
    """Alle 8:30 (Europe/Rome): lunedì il settimanale, gli altri giorni il giornaliero di ieri."""
    ora = dt.datetime.now(ROMA)
    if not forza and not (dt.time(8, 25) <= ora.time() <= dt.time(12, 0)):
        log(f"riepilogo: sono le {ora:%H:%M} a Roma, non è l'ora")
        return
    s = stato()
    oggi = ora.date()
    if oggi.weekday() == 0:
        sett = settimana_di((oggi - dt.timedelta(days=1)).isoformat())
        if s["settimanale"] == sett and not forza:
            return
        sintetizza_settimana(sett, motore)
        t = testo_settimanale(sett)
        if t and invia(t, prova) and not prova:
            s["settimanale"] = sett
        comunita_post("settimanale", sett, prova)
    else:
        ieri = (oggi - dt.timedelta(days=1)).isoformat()
        if s["giornaliero"] == ieri and not forza:
            return
        t = testo_giornaliero(ieri)
        if t is None:
            log(f"riepilogo: nessuna attività il {ieri}, nessun post")
            s["giornaliero"] = ieri
        elif invia(t, prova) and not prova:
            s["giornaliero"] = ieri
        comunita_post("giornaliero", ieri, prova)
    if not prova:
        salva_stato(s)


def comunita_post(modo, periodo, prova=False):
    """Sezione «Dalla comunità»: errori qui non devono bloccare il registro."""
    try:
        import comunita
        (comunita.post_settimanale if modo == "settimanale" else comunita.post_giornaliero)(periodo, prova)
    except Exception as e:
        log(f"comunità: {modo} {periodo} non pubblicato: {e}")


def segna_tutto_postato():
    """Dopo la ricostruzione dello storico: niente raffica di post sul passato."""
    s = stato()
    for p in sorted(os.listdir(GIORNI)):
        for v in leggi_json(os.path.join(GIORNI, p))["voci"]:
            if v["id"] not in s["voci_postate"]:
                s["voci_postate"].append(v["id"])
                s["commit_postati"] += v["commit"]
    oggi = oggi_roma()
    s["giornaliero"] = (oggi - dt.timedelta(days=1)).isoformat()
    s["settimanale"] = settimana_di((oggi - dt.timedelta(days=oggi.weekday() + 1)).isoformat())
    salva_stato(s)


# ───────────────────────────── main ─────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("raccogli"); a.add_argument("--dal", default=(oggi_roma() - dt.timedelta(days=2)).isoformat())
    a = sub.add_parser("sintetizza")
    a.add_argument("--dal", default=(oggi_roma() - dt.timedelta(days=1)).isoformat())
    a.add_argument("--al", default=oggi_roma().isoformat())
    a.add_argument("--motore", choices=["api", "cli"], default=os.environ.get("REGISTRO_MOTORE", "api")); a.add_argument("--forza", action="store_true")
    a = sub.add_parser("settimana"); a.add_argument("settimana", nargs="?")
    a.add_argument("--tutte", action="store_true"); a.add_argument("--motore", choices=["api", "cli"], default=os.environ.get("REGISTRO_MOTORE", "api"))
    a.add_argument("--forza", action="store_true")
    a = sub.add_parser("telegram"); a.add_argument("modo", choices=["live", "giornaliero", "settimanale", "riepilogo", "segna-tutto"])
    a.add_argument("--giorno"); a.add_argument("--prova", action="store_true"); a.add_argument("--forza", action="store_true")
    a.add_argument("--motore", choices=["api", "cli"], default=os.environ.get("REGISTRO_MOTORE", "api"))
    a = sub.add_parser("ciclo"); a.add_argument("--motore", choices=["api", "cli"], default=os.environ.get("REGISTRO_MOTORE", "api"))
    a.add_argument("--prova", action="store_true")
    x = ap.parse_args()

    if x.cmd == "raccogli":
        raccogli(x.dal)
    elif x.cmd == "sintetizza":
        sintetizza(x.dal, x.al, x.motore, x.forza)
    elif x.cmd == "settimana":
        if x.tutte:
            corrente = settimana_di(oggi_roma().isoformat())
            for sett in sorted({settimana_di(p[:10]) for p in os.listdir(GIORNI)}):
                if sett != corrente:
                    try:
                        sintetizza_settimana(sett, x.motore, x.forza)
                    except Exception as e:
                        log(f"  ERRORE {sett}: {e}")
        else:
            sintetizza_settimana(x.settimana or settimana_di((oggi_roma() - dt.timedelta(days=7)).isoformat()), x.motore, x.forza)
    elif x.cmd == "telegram":
        if x.modo == "live":
            telegram_live(x.prova)
        elif x.modo == "riepilogo":
            telegram_riepilogo(x.prova, x.forza, x.motore)
        elif x.modo == "giornaliero":
            g = x.giorno or (oggi_roma() - dt.timedelta(days=1)).isoformat()
            t = testo_giornaliero(g)
            print("(nessuna attività)") if t is None else invia(t, x.prova)
        elif x.modo == "settimanale":
            sett = x.giorno or settimana_di((oggi_roma() - dt.timedelta(days=7)).isoformat())
            t = testo_settimanale(sett)
            print("(nessun riepilogo)") if t is None else invia(t, x.prova)
        elif x.modo == "segna-tutto":
            segna_tutto_postato()
    elif x.cmd == "ciclo":
        oggi = oggi_roma()
        raccogli((oggi - dt.timedelta(days=2)).isoformat())
        if x.motore == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
            log("ANTHROPIC_API_KEY assente: nessuna sintesi, nessun post")
            return
        sintetizza((oggi - dt.timedelta(days=1)).isoformat(), oggi.isoformat(), x.motore)
        telegram_live(x.prova)
        telegram_riepilogo(x.prova, motore=x.motore)


if __name__ == "__main__":
    main()
