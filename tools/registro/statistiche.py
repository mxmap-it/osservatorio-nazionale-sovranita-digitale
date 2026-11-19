#!/usr/bin/env python3
"""Statistiche di accesso ai siti dell'Osservatorio: pubblicazione sul sito e su Telegram.

Il contatore è GoatCounter, installato su questo server (stats.mxmap.it, servizio
`goatcounter`): niente cookie, nessun IP salvato, nessuna visita singola conservata.
GoatCounter tiene solo conteggi aggregati per pagina e per ora/giorno; questo script li
legge (copia del database, in sola lettura), li aggrega ancora e pubblica soltanto:

  - visite per sito e per giorno;
  - pagine, fonti, paesi, regioni, dispositivi degli ultimi 30 giorni, con SOGLIA:
    una voce con meno di 5 visite non compare (finisce in «altro»);
  - per mxmap.it, le pagine per ente GEORIFERITE: ogni /ente/<sigla>/<nome>/ è
    ricondotto all'ente IndicePA (stessa funzione che genera gli URL in mxmap.it,
    `mail_sovereignty.pages.assign_entity_paths`), quindi a regione, provincia,
    comune, categoria e classe di sovranità del suo provider di posta.

  statistiche.py mappa            scarica data.json di mxmap.it e ricostruisce path → ente
  statistiche.py pubblica         scrive data/statistiche/statistiche.json
  statistiche.py settimana [--prova] [--settimana AAAA-Www]   post Telegram + grafico
  statistiche.py grafico [FILE]

Variabili: OSSERVATORIO_BOT_DATA, GOATCOUNTER_DB (default /var/lib/goatcounter/goatcounter.sqlite3),
TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID.
"""
import argparse
import datetime as dt
import json
import os
import sqlite3
import subprocess
import sys
import urllib.request
from collections import Counter, defaultdict
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import registro as R  # noqa: E402

DATA = os.environ.get("OSSERVATORIO_BOT_DATA", os.path.expanduser("~/.local/share/osservatorio-bot"))
GC_DB = os.environ.get("GOATCOUNTER_DB", "/var/lib/goatcounter/goatcounter.sqlite3")
COPIA = os.path.join(DATA, "statistiche", "goatcounter-copia.sqlite3")
MAPPA = os.path.join(DATA, "statistiche", "mxmap-enti-mappa.json")
MXMAP_SRC = os.path.join(DATA, "mxmap-src")
USCITA = os.path.join(R.ROOT, "data", "statistiche", "statistiche.json")
ROMA = ZoneInfo("Europe/Rome")
SOGLIA = 5          # sotto questa soglia una voce non si pubblica
FINESTRA = 30       # giorni delle distribuzioni (pagine, fonti, luoghi, enti)

SITI = [  # ordine fisso: decide anche l'ordine dei pannelli e dei colori
    {"host": "mxmap.it", "nome": "MxMap.it", "nome_en": "MxMap.it", "descr": {"it": "mappa e pagine per ente", "en": "map and per-entity pages"}},
    {"host": "osservatorio.mxmap.it", "nome": "Osservatorio", "nome_en": "Observatory", "descr": {"it": "sito dell'Osservatorio", "en": "Observatory site"}},
    {"host": "analisi-spesa-ict.mxmap.it", "nome": "Spesa ICT", "nome_en": "ICT spending", "descr": {"it": "analisi della spesa ICT", "en": "ICT spending analysis"}},
]
HOSTS = {s["host"] for s in SITI}
SOV4 = {"it": ("Italiano", "Italian"), "eu_non_it": ("UE non italiano", "EU, non-Italian"),
        "extra_eu": ("Extra-UE", "Non-EU"), "unknown": ("Non determinato", "Undetermined")}
CATEGORIE_EN = {  # chiavi di mail_sovereignty.stats.CLUSTERS
    "territorial": "Local authorities (municipalities, provinces, regions)", "education": "Education (schools, universities)",
    "healthcare": "Healthcare (local health authorities, hospitals)", "central": "Central government, ministries and authorities",
    "orders": "Professional orders, chambers of commerce, ACI", "consortia": "Consortia, unions of municipalities",
    "soe": "Publicly owned companies and foundations", "welfare": "Welfare and social housing",
    "environment": "Environment, parks and river basins", "agencies": "Regional agencies", "procurement": "Contracting authorities",
    "pension": "Pension and social security funds", "culture": "Culture (theatres, foundations)", "research": "Research",
    "transport": "Transport and ports", "altri": "Other bodies"}
REGIONI_ISO = {  # ISO 3166-2:IT → nome (uguale nelle due lingue: nomi propri)
    "21": "Piemonte", "23": "Valle d'Aosta", "25": "Lombardia", "32": "Trentino-Alto Adige", "34": "Veneto",
    "36": "Friuli-Venezia Giulia", "42": "Liguria", "45": "Emilia-Romagna", "52": "Toscana", "55": "Umbria",
    "57": "Marche", "62": "Lazio", "65": "Abruzzo", "67": "Molise", "72": "Campania", "75": "Puglia",
    "77": "Basilicata", "78": "Calabria", "82": "Sicilia", "88": "Sardegna"}
PAESI_IT = {  # i nomi di GoatCounter sono in inglese
    "Italy": "Italia", "Switzerland": "Svizzera", "Germany": "Germania", "France": "Francia", "Spain": "Spagna",
    "United States": "Stati Uniti", "United Kingdom": "Regno Unito", "Netherlands": "Paesi Bassi", "Belgium": "Belgio",
    "Austria": "Austria", "Ireland": "Irlanda", "Sweden": "Svezia", "Norway": "Norvegia", "Denmark": "Danimarca",
    "Finland": "Finlandia", "Poland": "Polonia", "Portugal": "Portogallo", "Greece": "Grecia", "Romania": "Romania",
    "Czechia": "Cechia", "Hungary": "Ungheria", "Luxembourg": "Lussemburgo", "Slovenia": "Slovenia", "Croatia": "Croazia",
    "Estonia": "Estonia", "Latvia": "Lettonia", "Lithuania": "Lituania", "Malta": "Malta", "San Marino": "San Marino",
    "Vatican City": "Città del Vaticano", "Canada": "Canada", "Brazil": "Brasile", "China": "Cina", "Japan": "Giappone",
    "India": "India", "Russia": "Russia", "Ukraine": "Ucraina", "Albania": "Albania", "Israel": "Israele",
    "Singapore": "Singapore", "Australia": "Australia", "Argentina": "Argentina", "Turkey": "Turchia", "Türkiye": "Turchia",
    "non determinato": "non determinato"}
DISP_EN = {"telefono": "phone", "tablet": "tablet", "computer": "computer"}


# ───────────────────────────── lettura di GoatCounter ─────────────────────────────

def copia_db():
    """Copia coerente del database (backup SQLite, fatto dall'utente del servizio)."""
    os.makedirs(os.path.dirname(COPIA), exist_ok=True)
    tmp = "/var/lib/goatcounter/.copia-export.sqlite3"
    subprocess.run(["sudo", "-n", "-u", "goatcounter", "sqlite3", GC_DB, f".backup '{tmp}'"], check=True)
    with open(COPIA, "wb") as f:
        subprocess.run(["sudo", "-n", "cat", tmp], check=True, stdout=f)
    subprocess.run(["sudo", "-n", "rm", "-f", tmp], check=True)
    os.chmod(COPIA, 0o600)
    return sqlite3.connect(COPIA)


def separa(path):
    """'/mxmap.it/ente/rm/x' → ('mxmap.it', '/ente/rm/x'). Gli host ignoti finiscono in 'altri'."""
    p = path.lstrip("/")
    host, _, resto = p.partition("/")
    if host.startswith("www."):
        host = host[4:]
    return (host if host in HOSTS else "altri"), "/" + resto


def giorno_roma(ora_utc):
    t = dt.datetime.fromisoformat(ora_utc.replace(" ", "T")).replace(tzinfo=dt.timezone.utc)
    return t.astimezone(ROMA).date().isoformat()


def leggi(c):
    """Tutto ciò che serve, già aggregato: nessuna riga per visitatore esiste nel database."""
    paths = {pid: (path, titolo) for pid, path, titolo in c.execute("SELECT path_id, path, title FROM paths")}
    visite = defaultdict(int)          # (giorno, path_id) → visite (ore UTC convertite in giorni di Roma)
    for pid, ora, n in c.execute("SELECT path_id, hour, total FROM hit_counts"):
        visite[(giorno_roma(ora), pid)] += n
    refs = {rid: (ref, schema) for rid, ref, schema in c.execute("SELECT ref_id, ref, ref_scheme FROM refs")}
    fonti = defaultdict(int)
    for pid, rid, ora, n in c.execute("SELECT path_id, ref_id, hour, total FROM ref_counts"):
        fonti[(giorno_roma(ora), pid, rid)] += n
    luoghi_nomi = {}
    for codice, paese, regione, nome_paese, nome_regione in c.execute(
            "SELECT iso_3166_2, country, region, country_name, region_name FROM locations"):
        luoghi_nomi[codice] = (paese, nome_paese, nome_regione)
    luoghi = [(g, pid, loc, n) for pid, g, loc, n in c.execute("SELECT path_id, day, location, count FROM location_stats")]
    larghezze = [(g, pid, w, n) for pid, g, w, n in c.execute("SELECT path_id, day, width, count FROM size_stats")]
    browser_n = {i: n for i, n in c.execute("SELECT browser_id, name FROM browsers")}
    browser = [(g, pid, browser_n.get(b, "?"), n) for pid, g, b, n in c.execute("SELECT path_id, day, browser_id, count FROM browser_stats")]
    sistemi_n = {i: n for i, n in c.execute("SELECT system_id, name FROM systems")}
    sistemi = [(g, pid, sistemi_n.get(s, "?"), n) for pid, g, s, n in c.execute("SELECT path_id, day, system_id, count FROM system_stats")]
    return {"paths": paths, "visite": visite, "refs": refs, "fonti": fonti, "luoghi": luoghi,
            "luoghi_nomi": luoghi_nomi, "larghezze": larghezze, "browser": browser, "sistemi": sistemi}


# ───────────────────────────── mappa pagina → ente (mxmap.it) ─────────────────────────────

def mappa(forza=False):
    """path normalizzato (senza / finale) → ente. Si rifà una volta al giorno."""
    if not forza and os.path.exists(MAPPA) and (dt.datetime.now().timestamp() - os.path.getmtime(MAPPA)) < 20 * 3600:
        return R.leggi_json(MAPPA, {})
    if os.path.isdir(os.path.join(MXMAP_SRC, ".git")):
        subprocess.run(["git", "-C", MXMAP_SRC, "pull", "-q", "--ff-only"], check=False)
    else:
        subprocess.run(["git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse",
                        "https://github.com/mxmap-it/mxmap.it.git", MXMAP_SRC], check=True)
        subprocess.run(["git", "-C", MXMAP_SRC, "sparse-checkout", "set", "src"], check=True)
    sys.path.insert(0, os.path.join(MXMAP_SRC, "src"))
    from mail_sovereignty import pages, kpi  # funzioni canoniche di mxmap.it: niente slug rifatti qui

    with urllib.request.urlopen("https://mxmap.it/data.json", timeout=180) as r:
        dati = json.load(r)
    ents = [e for e in (dati.get("municipalities") or {}).values() if str(e.get("bfs", "")).startswith("IT-")]
    percorsi = pages.assign_entity_paths(ents)
    out = {}
    for e in ents:
        p = percorsi[e["bfs"]].rstrip("/")
        out[p] = {"bfs": e["bfs"], "nome": e.get("name"), "regione": e.get("regione"), "provincia": e.get("provincia"),
                  "comune": e.get("comune"), "cat": pages.cluster_of(e["bfs"])[0], "categoria": pages.cluster_of(e["bfs"])[1],
                  "sov": kpi.provider_to_sov4(e.get("provider") or "")}
    R.scrivi_json(MAPPA, out)
    R.log(f"mappa enti mxmap: {len(out)} pagine")
    return out


def tipo_pagina_mxmap(p):
    for pref, tipo in (("/ente/", "ente"), ("/aree/", "aree"), ("/categoria/", "categoria"), ("/dominio/", "ente")):
        if p.startswith(pref):
            return tipo
    return "mappa" if p in ("/", "/index.html", "") else "altre"


# ───────────────────────────── aggregazione ─────────────────────────────

def con_soglia(conteggio, n_max=None, chiave="nome"):
    """Lista ordinata delle voci ≥ SOGLIA; il resto sommato in «altro»."""
    tot = sum(conteggio.values())
    righe = [{chiave: k, "n": v} for k, v in conteggio.most_common() if v >= SOGLIA and k not in (None, "", "?")]
    if n_max:
        righe = righe[:n_max]
    resto = tot - sum(r["n"] for r in righe)
    return righe, resto


def nome_fonte(ref, schema):
    if schema == "o" or not ref:
        return "diretto"          # nessun referrer: link digitato, app, segnalibro
    if schema == "c":
        return "campagna"
    ref = ref.split("/")[0]
    return ref[4:] if ref.startswith("www.") else ref


def dispositivo(w):
    return "telefono" if w and w < 768 else ("tablet" if w and w < 1100 else ("computer" if w else None))


def calcola(d, mp, dal, al):
    """Distribuzioni sul periodo [dal, al] (date ISO). Restituisce contatori grezzi (prima della soglia)."""
    nel = lambda g: dal <= g <= al  # noqa: E731
    per_sito, per_pagina, titoli = Counter(), defaultdict(Counter), {}
    enti, regioni_enti, prov_enti, cat_enti, sov_enti, tipi = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
    enti_per_regione = defaultdict(set)
    for (g, pid), n in d["visite"].items():
        if not nel(g):
            continue
        host, p = separa(d["paths"][pid][0])
        per_sito[host] += n
        per_pagina[host][p] += n
        titoli[(host, p)] = d["paths"][pid][1]
        if host == "mxmap.it":
            tipi[tipo_pagina_mxmap(p)] += n
            e = mp.get(p.rstrip("/"))
            if e:
                enti[p.rstrip("/")] += n
                regioni_enti[e["regione"] or "—"] += n
                prov_enti[e["provincia"] or "—"] += n
                cat_enti[(e.get("cat", "altri"), e["categoria"])] += n
                sov_enti[e["sov"]] += n
                enti_per_regione[e["regione"] or "—"].add(e["bfs"])
    fonti = Counter()
    for (g, pid, rid), n in d["fonti"].items():
        if nel(g):
            fonti[nome_fonte(*d["refs"].get(rid, ("", "o")))] += n
    paesi, regioni_vis = Counter(), Counter()
    for g, pid, loc, n in d["luoghi"]:
        if not nel(g):
            continue
        paese, nome_paese, nome_regione = d["luoghi_nomi"].get(loc, ("", "", ""))
        paesi[nome_paese or "non determinato"] += n  # in inglese: tradotti in pubblica()
        if paese == "IT" and "-" in (loc or ""):
            regioni_vis[REGIONI_ISO.get(loc.split("-", 1)[1], nome_regione or loc)] += n
    disp = Counter()
    for g, pid, w, n in d["larghezze"]:
        if nel(g) and dispositivo(w):
            disp[dispositivo(w)] += n
    browser = Counter({})
    for g, pid, b, n in d["browser"]:
        if nel(g):
            browser[b] += n
    sistemi = Counter()
    for g, pid, s, n in d["sistemi"]:
        if nel(g):
            sistemi[s] += n
    return {"per_sito": per_sito, "per_pagina": per_pagina, "titoli": titoli, "enti": enti,
            "regioni_enti": regioni_enti, "prov_enti": prov_enti, "cat_enti": cat_enti, "sov_enti": sov_enti,
            "enti_per_regione": enti_per_regione, "tipi": tipi, "fonti": fonti, "paesi": paesi,
            "regioni_vis": regioni_vis, "disp": disp, "browser": browser, "sistemi": sistemi}


def serie_giornaliere(d):
    s = defaultdict(Counter)
    for (g, pid), n in d["visite"].items():
        s[separa(d["paths"][pid][0])[0]][g] += n
    return s


def pubblica():
    c = copia_db()
    d = leggi(c)
    mp = mappa()
    oggi = R.oggi_roma()
    al = (oggi - dt.timedelta(days=1)).isoformat()          # solo giorni conclusi
    dal = (oggi - dt.timedelta(days=FINESTRA)).isoformat()
    x = calcola(d, mp, dal, al)
    serie = serie_giornaliere(d)
    tutti_giorni = sorted({g for s in serie.values() for g in s if g <= al})
    inizio = tutti_giorni[0] if tutti_giorni else al

    def giorni(host):
        g0 = dt.date.fromisoformat(inizio)
        n = (dt.date.fromisoformat(al) - g0).days + 1
        return [[(g0 + dt.timedelta(days=i)).isoformat(), serie[host].get((g0 + dt.timedelta(days=i)).isoformat(), 0)]
                for i in range(max(n, 0))]

    def settimana(host, fine):
        f = dt.date.fromisoformat(fine)
        return sum(serie[host].get((f - dt.timedelta(days=i)).isoformat(), 0) for i in range(7))

    prec = (dt.date.fromisoformat(al) - dt.timedelta(days=7)).isoformat()
    siti = []
    for s in SITI:
        h = s["host"]
        righe, resto = con_soglia(x["per_pagina"][h], 25, "path")
        for r in righe:
            r["titolo"] = (x["titoli"].get((h, r["path"])) or "").strip()
            r["url"] = f"https://{h}{r['path']}"
        siti.append({**s, "url": f"https://{h}/", "giorni": giorni(h),
                     "ultimi_7": settimana(h, al), "precedenti_7": settimana(h, prec),
                     "ultimi_30": x["per_sito"][h], "totale": sum(serie[h].values()),
                     "pagine": righe, "pagine_altro": resto})

    def lista(cnt, n_max=None, chiave="nome"):
        righe, resto = con_soglia(cnt, n_max, chiave)
        return {"voci": righe, "altro": resto, "totale": sum(cnt.values())}

    def tradotta(lst, it_en):
        for r in lst["voci"]:
            r["nome_en"] = it_en(r["nome"])
        return lst

    enti_top, _ = con_soglia(x["enti"], 30, "path")
    for r in enti_top:
        e = mp[r["path"]]
        r.update({"nome": e["nome"], "comune": e["comune"], "provincia": e["provincia"], "regione": e["regione"],
                  "categoria": e["categoria"], "categoria_en": CATEGORIE_EN.get(e.get("cat"), e["categoria"]),
                  "sov": e["sov"], "url": f"https://mxmap.it{r['path']}/"})
    regioni = [{"nome": k, "n": v, "enti": len(x["enti_per_regione"][k])}
               for k, v in x["regioni_enti"].most_common()]  # 20 regioni: aggregato territoriale, niente soglia
    out = {
        "aggiornato": dt.datetime.now(ROMA).strftime("%Y-%m-%dT%H:%M"),
        "dal": inizio, "al": al, "finestra": {"dal": dal, "al": al, "giorni": FINESTRA}, "soglia": SOGLIA,
        "siti": siti,
        "altri_host_30": x["per_sito"].get("altri", 0),
        "fonti": lista(x["fonti"], 20),
        "paesi": tradotta(lista(Counter({PAESI_IT.get(k, k): v for k, v in x["paesi"].items()}), 15),
                          lambda n: next((en for en, it in PAESI_IT.items() if it == n), n)),
        "regioni_visitatori": lista(x["regioni_vis"]),
        "dispositivi": tradotta(lista(x["disp"]), lambda n: DISP_EN.get(n, n)),
        "browser": lista(x["browser"], 8), "sistemi": lista(x["sistemi"], 8),
        "mxmap": {
            "tipi_pagina": dict(x["tipi"]),
            "visite_pagine_ente": sum(x["enti"].values()), "enti_distinti": len(x["enti"]),
            "enti_totali": len(mp),
            "per_regione": regioni,
            "per_provincia": lista(x["prov_enti"], 25),
            "per_categoria": [{"chiave": k, "nome": lab, "nome_en": CATEGORIE_EN.get(k, lab), "n": n}
                              for (k, lab), n in x["cat_enti"].most_common()],
            "per_sovranita": [{"chiave": k, "nome": SOV4[k][0], "nome_en": SOV4[k][1], "n": x["sov_enti"].get(k, 0)} for k in SOV4],
            "enti_top": enti_top,
        },
    }
    R.scrivi_json(USCITA, out)
    R.log(f"statistiche: {sum(x['per_sito'].values())} visite negli ultimi {FINESTRA} giorni → {os.path.relpath(USCITA, R.ROOT)}")
    return out


# ───────────────────────────── Telegram ─────────────────────────────

def grafico(uscita=None, settimane=8):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    st = R.leggi_json(USCITA)
    if not st:
        return None
    SUP, TXT, TXT2, GRID, SERIE = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#2a78d6"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "text.color": TXT,
                         "axes.labelcolor": TXT2, "xtick.color": TXT2, "ytick.color": TXT2})
    siti = st["siti"]
    fig, assi = plt.subplots(len(siti), 1, figsize=(10, 2.3 * len(siti) + 0.8), sharex=True, facecolor=SUP)
    limite = dt.date.fromisoformat(st["al"]) - dt.timedelta(days=7 * settimane - 1)
    for ax, s in zip(assi, siti):
        g = [(dt.date.fromisoformat(a), n) for a, n in s["giorni"] if dt.date.fromisoformat(a) >= limite]
        ax.set_facecolor(SUP)
        if g:
            ax.bar([a for a, _ in g], [n for _, n in g], width=0.72, color=SERIE, linewidth=0)
        ax.set_title(f"{s['nome']} · {s['host']}", loc="left", fontsize=11, fontweight="bold", color=TXT, pad=6)
        ax.text(1, 1.02, f"ultimi 7 giorni: {s['ultimi_7']:,}".replace(",", "."), transform=ax.transAxes,
                ha="right", va="bottom", fontsize=9.5, color=TXT2)
        for lato in ("top", "right", "left"):
            ax.spines[lato].set_visible(False)
        ax.spines["bottom"].set_color(GRID)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(length=0)
        ax.set_ylim(bottom=0)
    assi[-1].xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    assi[-1].xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    fig.text(0.01, 0.005, "Visite al giorno · fonte: stats.mxmap.it (GoatCounter, senza cookie) · osservatorio.mxmap.it/statistiche",
             fontsize=8, color=TXT2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    uscita = uscita or os.path.join(DATA, "statistiche", "siti.png")
    fig.savefig(uscita, dpi=150, facecolor=SUP)
    plt.close(fig)
    return uscita


def num(n):
    return f"{n:,}".replace(",", ".")


def variazione(a, b):
    if not b:
        return ""
    v = round(100 * (a - b) / b)
    return f" ({'+' if v >= 0 else ''}{v}% sulla settimana prima)"


def post_settimanale(sett=None, prova=False):
    """Lunedì: la settimana appena chiusa (lun–dom) sui tre siti, con il grafico."""
    import comunita
    oggi = R.oggi_roma()
    sett = sett or R.settimana_di((oggi - dt.timedelta(days=oggi.weekday() + 1)).isoformat())
    giorni = R.giorni_settimana(sett)
    st = pubblica()
    d = leggi(sqlite3.connect(COPIA))
    mp = mappa()
    x = calcola(d, mp, giorni[0], giorni[-1])
    prima = (dt.date.fromisoformat(giorni[0]) - dt.timedelta(days=7)).isoformat()
    xp = calcola(d, mp, prima, (dt.date.fromisoformat(giorni[0]) - dt.timedelta(days=1)).isoformat())
    if not sum(x["per_sito"].values()):
        R.log(f"statistiche: nessuna visita nella settimana {sett}, niente post")
        return
    E = R.esc
    al = R.mesi_it(giorni[-1]).split(" ", 1)[1]
    t = [f"📊 <b>I siti dell'Osservatorio nella settimana {dt.date.fromisoformat(giorni[0]).day}–{al}</b>", ""]
    for s in SITI:
        n = x["per_sito"][s["host"]]
        t.append(f"• <b>{E(s['nome'])}</b> ({s['host']}): {num(n)} visite{variazione(n, xp['per_sito'][s['host']])}")
    if x["enti"]:
        t += ["", f"🗺️ <b>Enti consultati su MxMap.it</b>: {num(len(x['enti']))} enti diversi, {num(sum(x['enti'].values()))} visite alle loro pagine"]
        reg = [f"{E(k)} {num(v)}" for k, v in x["regioni_enti"].most_common(6)]
        t.append("Per regione dell'ente: " + " · ".join(reg))
        top, _ = con_soglia(x["enti"], 5, "path")
        for r in top:
            e = mp[r["path"]]
            t.append(f"  – <a href=\"https://mxmap.it{r['path']}/\">{E(e['nome'] or '')}</a> ({E(e['provincia'] or '')}): {num(r['n'])}")
    for titolo, cnt, h in (("📄 Pagine più lette dell'Osservatorio", x["per_pagina"]["osservatorio.mxmap.it"], "osservatorio.mxmap.it"),
                           ("📄 Pagine più lette della Spesa ICT", x["per_pagina"]["analisi-spesa-ict.mxmap.it"], "analisi-spesa-ict.mxmap.it")):
        top, _ = con_soglia(cnt, 5, "path")
        if top:
            t += ["", f"<b>{titolo}</b>"]
            for r in top:
                tit = (x["titoli"].get((h, r["path"])) or r["path"]).split(" | ")[0].split(" — ")[0].strip()[:70]
                t.append(f"  – <a href=\"https://{h}{r['path']}\">{E(tit)}</a>: {num(r['n'])}")
    fonti, _ = con_soglia(x["fonti"], 6)
    if fonti:
        t += ["", "↪️ <b>Da dove arrivano</b>: " + " · ".join(f"{E(r['nome'])} {num(r['n'])}" for r in fonti)]
    paesi, _ = con_soglia(Counter({PAESI_IT.get(k, k): v for k, v in x["paesi"].items()}), 5)
    if paesi:
        t.append("🌍 " + " · ".join(f"{E(r['nome'])} {num(r['n'])}" for r in paesi))
    t += ["", f"Senza cookie e senza salvare IP; voci sotto {SOGLIA} visite non mostrate. "
          f"<a href=\"{R.SITO}/statistiche/\">Tutte le statistiche</a> · <a href=\"https://stats.mxmap.it/\">dashboard in tempo reale</a>"]
    R.invia("\n".join(t), prova)
    png = grafico()
    if png:
        comunita.invia_foto(png, "📈 <b>Visite al giorno</b> sui siti dell'Osservatorio, ultime 8 settimane.", prova)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("mappa"); a.add_argument("--forza", action="store_true")
    sub.add_parser("pubblica")
    a = sub.add_parser("settimana"); a.add_argument("--settimana"); a.add_argument("--prova", action="store_true")
    a = sub.add_parser("grafico"); a.add_argument("file", nargs="?")
    x = ap.parse_args()
    if x.cmd == "mappa":
        print(len(mappa(True)), "pagine ente")
    elif x.cmd == "pubblica":
        pubblica()
    elif x.cmd == "settimana":
        post_settimanale(x.settimana, x.prova)
    elif x.cmd == "grafico":
        print(grafico(x.file))


if __name__ == "__main__":
    main()
