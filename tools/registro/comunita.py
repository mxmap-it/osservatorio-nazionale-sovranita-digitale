#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comunità Telegram dell'Osservatorio — misura e sintesi delle conversazioni.

Il bot del Registro legge il gruppo della comunità (TELEGRAM_COMMUNITY_ID) e:
  - conserva i messaggi in un database SQLite PRIVATO sul server
    ($OSSERVATORIO_BOT_DATA/comunita.db, permessi 600, mai in git);
  - le persone sono pseudonimizzate (hash con sale segreto): nessun nome,
    nessuno username viene salvato;
  - misura ogni giorno quante persone sono nel gruppo, quanti messaggi e quante
    persone diverse hanno scritto;
  - produce con Claude la sintesi delle discussioni e dei link/documenti
    condivisi (giornaliera e settimanale), senza nomi e senza citazioni;
  - disegna il grafico dell'andamento (membri, messaggi, persone attive).

Chi non vuole esserci scrive /escludimi al bot: i suoi messaggi vengono
cancellati dal database e ignorati da allora in poi (/includimi per tornare).

LIMITE DELLE API TELEGRAM: un bot non può leggere i messaggi precedenti al suo
ingresso. Lo storico si importa dall'esportazione JSON di Telegram Desktop
(Chat > ⋮ > Esporta cronologia chat > formato JSON, senza media):
  python tools/registro/comunita.py importa /percorso/result.json

Comandi:
  poll              legge i nuovi aggiornamenti dal bot (cron ogni 5 minuti)
  chat              elenca le chat in cui il bot ha visto messaggi (per l'ID)
  importa FILE      importa un export JSON di Telegram Desktop
  statistiche       stampa la serie giornaliera
  grafico [FILE]    disegna il PNG dell'andamento
  sintesi GIORNO|SETTIMANA [--prova]   sintesi (non posta; --prova stampa)
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import registro as R  # noqa: E402

DATA = os.environ.get("OSSERVATORIO_BOT_DATA", os.path.expanduser("~/.local/share/osservatorio-bot"))
DB = os.path.join(DATA, "comunita.db")
URL_RE = re.compile(r"https?://[^\s<>\"']+")
MIN_MESSAGGI_SINTESI = 5


def comunita_ids():
    return [x.strip() for x in os.environ.get("TELEGRAM_COMMUNITY_ID", "").split(",") if x.strip()]


def db():
    os.makedirs(DATA, exist_ok=True)
    nuovo = not os.path.exists(DB)
    c = sqlite3.connect(DB)
    if nuovo:
        os.chmod(DB, 0o600)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS messaggi(chat TEXT, id INTEGER, data TEXT, persona TEXT, testo TEXT,
        url TEXT, documento TEXT, PRIMARY KEY(chat, id));
    CREATE TABLE IF NOT EXISTS eventi(chat TEXT, data TEXT, persona TEXT, delta INTEGER, fonte TEXT,
        UNIQUE(chat, data, persona, delta));
    CREATE TABLE IF NOT EXISTS membri(chat TEXT, giorno TEXT, numero INTEGER, PRIMARY KEY(chat, giorno));
    CREATE TABLE IF NOT EXISTS esclusi(persona TEXT PRIMARY KEY);
    CREATE TABLE IF NOT EXISTS kv(k TEXT PRIMARY KEY, v TEXT);
    """)
    return c


def kv(c, k, v=None):
    if v is None:
        r = c.execute("SELECT v FROM kv WHERE k=?", (k,)).fetchone()
        return r[0] if r else None
    c.execute("INSERT OR REPLACE INTO kv VALUES(?,?)", (k, str(v)))


def persona(user_id):
    sale = os.environ.get("COMUNITA_SALT")
    if not sale:
        raise SystemExit("COMUNITA_SALT non impostato (vedi tools/registro/server.sh)")
    return hashlib.sha256(f"{sale}:{user_id}".encode()).hexdigest()[:16]


def giorno(iso_utc):
    return R.giorno_roma(iso_utc)


# ───────────────────────────── Bot API ─────────────────────────────

def api(metodo, **parametri):
    tok = os.environ["TELEGRAM_BOT_TOKEN"]
    data = urllib.parse.urlencode({k: (json.dumps(v) if isinstance(v, (list, dict)) else v)
                                   for k, v in parametri.items()}).encode()
    with urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/{metodo}", data=data, timeout=70) as r:
        d = json.load(r)
    if not d.get("ok"):
        raise RuntimeError(f"Telegram {metodo}: {d}")
    return d["result"]


def invia_foto(percorso, didascalia, prova=False, canale="principale"):
    tok, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get(R.CANALI[canale])
    if prova or not (tok and chat):
        print(f"— FOTO {percorso} —\n{didascalia}\n")
        return prova
    confine = uuid.uuid4().hex
    corpo = b""
    for k, v in (("chat_id", chat), ("caption", didascalia[:1024]), ("parse_mode", "HTML")):
        corpo += f"--{confine}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    with open(percorso, "rb") as f:
        corpo += (f"--{confine}\r\nContent-Disposition: form-data; name=\"photo\"; filename=\"comunita.png\"\r\n"
                  f"Content-Type: image/png\r\n\r\n").encode() + f.read() + f"\r\n--{confine}--\r\n".encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendPhoto", data=corpo,
                                 headers={"Content-Type": f"multipart/form-data; boundary={confine}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r).get("ok", False)


def rispondi(chat, testo, a=None):
    try:
        api("sendMessage", chat_id=chat, text=testo, **({"reply_to_message_id": a} if a else {}))
    except Exception as e:
        R.log(f"risposta non inviata: {e}")


TESTO_INFO = ("Sono il bot del Registro attività dell'Osservatorio (osservatorio.mxmap.it/registro/).\n\n"
              "In questo gruppo misuro la comunità: quante persone ci sono, quanti messaggi e quante persone "
              "scrivono, e preparo una sintesi delle discussioni e dei link condivisi. Non salvo nomi né "
              "username (solo uno pseudonimo cifrato per contare le persone diverse), le sintesi non citano "
              "nessuno e i messaggi restano su un server del progetto, non in pubblico.\n\n"
              "Non vuoi esserci? Scrivi /escludimi: cancello i tuoi messaggi e da allora ti ignoro. "
              "/includimi per tornare.")


def salva_messaggio(c, chat, m, p):
    testo = m.get("text") or m.get("caption") or ""
    urls = URL_RE.findall(testo)
    for e in (m.get("entities") or []) + (m.get("caption_entities") or []):
        if e.get("type") == "text_link" and e.get("url"):
            urls.append(e["url"])
    doc = (m.get("document") or {}).get("file_name") or ("[foto]" if m.get("photo") else None)
    data = dt.datetime.fromtimestamp(m["date"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    c.execute("INSERT OR IGNORE INTO messaggi VALUES(?,?,?,?,?,?,?)",
              (chat, m["message_id"], data, p, testo[:4000], json.dumps(sorted(set(urls))), doc))


def poll():
    """Legge gli aggiornamenti (Telegram li conserva 24 ore: basta un cron ogni pochi minuti)."""
    c = db()
    offset = int(kv(c, "offset") or 0)
    ammessi = set(comunita_ids())
    visti = json.loads(kv(c, "chat_viste") or "{}")
    esclusi = {r[0] for r in c.execute("SELECT persona FROM esclusi")}
    if not ammessi:
        # Gruppo non ancora configurato: si guardano le chat senza consumare gli
        # aggiornamenti, così a configurazione fatta si leggono anche questi
        # (presentazione all'ingresso compresa). Telegram li tiene 24 ore.
        for u in api("getUpdates", offset=offset, timeout=0, limit=100) or []:
            for k in ("message", "channel_post", "edited_message", "my_chat_member", "chat_member"):
                ch = (u.get(k) or {}).get("chat")
                if ch:
                    visti[str(ch["id"])] = {"tipo": ch.get("type"), "titolo": ch.get("title")}
        kv(c, "chat_viste", json.dumps(visti, ensure_ascii=False))
        c.commit()
        return
    n = 0
    while True:
        lot = api("getUpdates", offset=offset, timeout=0, limit=100,
                  allowed_updates=["message", "edited_message", "channel_post", "chat_member", "my_chat_member"])
        if not lot:
            break
        for u in lot:
            offset = u["update_id"] + 1
            m = u.get("message") or u.get("channel_post") or u.get("edited_message")
            cm = u.get("chat_member") or u.get("my_chat_member")
            chat_obj = (m or cm or {}).get("chat") or {}
            chat = str(chat_obj.get("id", ""))
            if chat:
                visti[chat] = {"tipo": chat_obj.get("type"), "titolo": chat_obj.get("title")}
            if u.get("my_chat_member") and chat in ammessi:
                if cm["new_chat_member"]["status"] in ("member", "administrator"):
                    rispondi(chat, TESTO_INFO)  # presentazione all'ingresso: trasparenza
            if chat not in ammessi:
                continue
            if cm and u.get("chat_member"):
                prima, dopo = cm["old_chat_member"]["status"], cm["new_chat_member"]["status"]
                dentro = {"member", "administrator", "creator", "restricted"}
                delta = (dopo in dentro) - (prima in dentro)
                if delta:
                    data = dt.datetime.fromtimestamp(cm["date"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    c.execute("INSERT OR IGNORE INTO eventi VALUES(?,?,?,?,?)",
                              (chat, data, persona(cm["new_chat_member"]["user"]["id"]), delta, "bot"))
                continue
            if not m:
                continue
            autore = (m.get("from") or {}).get("id") or (m.get("sender_chat") or {}).get("id")
            p = persona(autore) if autore else "canale"
            testo = (m.get("text") or "").strip()
            comando = testo.split("@")[0].split()[0].lower() if testo.startswith("/") else ""
            if comando == "/escludimi":
                c.execute("INSERT OR IGNORE INTO esclusi VALUES(?)", (p,))
                c.execute("DELETE FROM messaggi WHERE persona=?", (p,))
                esclusi.add(p)
                rispondi(chat, "Fatto: ho cancellato i tuoi messaggi dal registro della comunità e da ora non li leggo più.", m["message_id"])
                continue
            if comando == "/includimi":
                c.execute("DELETE FROM esclusi WHERE persona=?", (p,))
                esclusi.discard(p)
                rispondi(chat, "Fatto: da ora i tuoi messaggi rientrano nelle statistiche e nelle sintesi.", m["message_id"])
                continue
            if comando in ("/info", "/start", "/registro"):
                rispondi(chat, TESTO_INFO, m["message_id"])
                continue
            for nuovo in m.get("new_chat_members") or []:
                c.execute("INSERT OR IGNORE INTO eventi VALUES(?,?,?,?,?)", (chat, dt.datetime.fromtimestamp(m["date"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), persona(nuovo["id"]), 1, "servizio"))
            if m.get("left_chat_member"):
                c.execute("INSERT OR IGNORE INTO eventi VALUES(?,?,?,?,?)", (chat, dt.datetime.fromtimestamp(m["date"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), persona(m["left_chat_member"]["id"]), -1, "servizio"))
            if p in esclusi or m.get("new_chat_members") or m.get("left_chat_member"):
                continue
            salva_messaggio(c, chat, m, p)
            n += 1
        kv(c, "offset", offset)
        c.commit()
    kv(c, "chat_viste", json.dumps(visti, ensure_ascii=False))
    # conteggio dei membri: una fotografia al giorno
    oggi = R.oggi_roma().isoformat()
    for chat in ammessi:
        if not c.execute("SELECT 1 FROM membri WHERE chat=? AND giorno=?", (chat, oggi)).fetchone():
            try:
                c.execute("INSERT INTO membri VALUES(?,?,?)", (chat, oggi, api("getChatMemberCount", chat_id=chat)))
            except Exception as e:
                R.log(f"getChatMemberCount {chat}: {e}")
    c.commit()
    if n:
        R.log(f"comunità: {n} nuovi messaggi")


# ───────────────────────────── import storico ─────────────────────────────

def testo_export(t):
    if isinstance(t, str):
        return t, []
    parti, urls = [], []
    for x in t:
        if isinstance(x, str):
            parti.append(x)
        else:
            parti.append(x.get("text", ""))
            if x.get("type") == "text_link" and x.get("href"):
                urls.append(x["href"])
    return "".join(parti), urls


def importa(percorso, chat=None):
    with open(percorso, encoding="utf-8") as f:
        ex = json.load(f)
    chat = chat or (comunita_ids() or [None])[0]
    if not chat:
        raise SystemExit("serve TELEGRAM_COMMUNITY_ID o --chat")
    c = db()
    esclusi = {r[0] for r in c.execute("SELECT persona FROM esclusi")}
    n_m = n_e = 0
    for m in ex.get("messages", []):
        data = dt.datetime.fromtimestamp(int(m["date_unixtime"]), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        if m.get("type") == "service":
            azione = m.get("action")
            if azione in ("join_group_by_link", "join_group_by_request", "invite_members", "remove_members", "create_group", "migrate_from_group"):
                delta = -1 if azione == "remove_members" else 1
                if azione == "invite_members" and m.get("members"):
                    chi = m["members"]
                elif azione == "remove_members" and m.get("members"):
                    chi = m["members"]
                else:
                    chi = [m.get("actor_id") or m.get("from_id")]
                for x in chi:
                    c.execute("INSERT OR IGNORE INTO eventi VALUES(?,?,?,?,?)", (chat, data, persona(x), delta, "export"))
                    n_e += 1
            continue
        autore = m.get("from_id") or "anonimo"
        p = persona(re.sub(r"^(user|channel)", "", str(autore)))
        if p in esclusi:
            continue
        testo, urls = testo_export(m.get("text", ""))
        urls += URL_RE.findall(testo)
        doc = m.get("file_name") or ("[foto]" if m.get("photo") else None)
        c.execute("INSERT OR IGNORE INTO messaggi VALUES(?,?,?,?,?,?,?)",
                  (chat, int(m["id"]), data, p, testo[:4000], json.dumps(sorted(set(urls))), doc))
        n_m += 1
    c.commit()
    R.log(f"importati {n_m} messaggi e {n_e} eventi di ingresso/uscita in {chat}")


# ───────────────────────────── statistiche e grafico ─────────────────────────────

def serie(chat=None):
    """Una riga per giorno: membri (fotografia o ricostruzione), messaggi, persone attive."""
    c = db()
    chat = chat or (comunita_ids() or [None])[0]
    msg = {}
    for data, p in c.execute("SELECT data, persona FROM messaggi WHERE chat=?", (chat,)):
        g = giorno(data)
        msg.setdefault(g, []).append(p)
    eventi = c.execute("SELECT data, delta FROM eventi WHERE chat=? ORDER BY data", (chat,)).fetchall()
    foto = dict(c.execute("SELECT giorno, numero FROM membri WHERE chat=?", (chat,)).fetchall())
    giorni = sorted(set(msg) | {giorno(e[0]) for e in eventi} | set(foto))
    if not giorni:
        return []
    cum, ricostr, i = 0, {}, 0
    for g in R.intervallo(giorni[0], max(giorni[-1], R.oggi_roma().isoformat())):
        while i < len(eventi) and giorno(eventi[i][0]) <= g:
            cum += eventi[i][1]
            i += 1
        ricostr[g] = cum
    # gli eventi non coprono chi c'era prima dell'export: si allinea la curva
    # all'ultima fotografia reale del conteggio, che fa fede
    scarto = 0
    if foto:
        ultimo = max(foto)
        scarto = foto[ultimo] - ricostr.get(ultimo, cum)
    out = []
    for g in ricostr:
        out.append({"giorno": g, "membri": foto.get(g, ricostr[g] + scarto if (eventi or g in foto) else None),
                    "membri_misurati": g in foto,
                    "messaggi": len(msg.get(g, [])), "attivi": len(set(msg.get(g, [])))})
    return out


def settimanale(righe):
    w = {}
    for r in righe:
        s = R.settimana_di(r["giorno"])
        x = w.setdefault(s, {"settimana": s, "lunedi": R.giorni_settimana(s)[0], "messaggi": 0, "persone": set(), "membri": None})
        x["messaggi"] += r["messaggi"]
        if r["membri"] is not None:
            x["membri"] = r["membri"]  # fine settimana
    return w


def grafico(uscita=None, chat=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    c = db()
    chat = chat or (comunita_ids() or [None])[0]
    righe = serie(chat)
    if not righe:
        return None
    # persone attive per settimana = persone DIVERSE nella settimana (non somma dei giorni)
    attivi_w = {}
    for data, p in c.execute("SELECT data, persona FROM messaggi WHERE chat=?", (chat,)):
        attivi_w.setdefault(R.settimana_di(giorno(data)), set()).add(p)
    w = settimanale(righe)
    sett = sorted(w)
    x = [dt.date.fromisoformat(w[s]["lunedi"]) for s in sett]
    xg = [dt.date.fromisoformat(r["giorno"]) for r in righe if r["membri"] is not None]
    yg = [r["membri"] for r in righe if r["membri"] is not None]

    SUP, TXT, TXT2, GRID, SERIE = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#2a78d6"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "text.color": TXT,
                         "axes.labelcolor": TXT2, "xtick.color": TXT2, "ytick.color": TXT2})
    pannelli = 3 if yg else 2
    fig, assi = plt.subplots(pannelli, 1, figsize=(10, 2.6 * pannelli + 0.9), sharex=True, facecolor=SUP)
    assi = list(assi)

    def stile(ax, titolo):
        ax.set_facecolor(SUP)
        ax.set_title(titolo, loc="left", fontsize=11, fontweight="bold", color=TXT, pad=6)
        for lato in ("top", "right", "left"):
            ax.spines[lato].set_visible(False)
        ax.spines["bottom"].set_color(GRID)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(length=0)
        ax.set_ylim(bottom=0)

    larg = 5.2  # giorni: barre sottili con spazio fra l'una e l'altra
    if yg:
        ax = assi.pop(0)
        ax.plot(xg, yg, color=SERIE, linewidth=2)
        stile(ax, "Persone nella comunità")
        ax.annotate(f"{yg[-1]:,}".replace(",", "."), (xg[-1], yg[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=10, fontweight="bold", color=TXT)
        ax.set_ylim(0, max(yg) * 1.15 + 1)
    ax = assi.pop(0)
    ax.bar(x, [w[s]["messaggi"] for s in sett], width=larg, color=SERIE, edgecolor=SUP, linewidth=0)
    stile(ax, "Messaggi per settimana")
    ax = assi.pop(0)
    ax.bar(x, [len(attivi_w.get(s, ())) for s in sett], width=larg, color=SERIE, linewidth=0)
    stile(ax, "Persone che hanno scritto, per settimana")
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
    fig.text(0.01, 0.005, "Fonte: bot del Registro attività · osservatorio.mxmap.it/registro · conteggi anonimi"
             + ("" if all(r["membri_misurati"] for r in righe if r["membri"] is not None) else
                " · membri prima della prima misura: ricostruiti dagli ingressi e uscite"),
             fontsize=8, color=TXT2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    uscita = uscita or os.path.join(DATA, "comunita.png")
    fig.savefig(uscita, dpi=150, facecolor=SUP)
    plt.close(fig)
    return uscita


# ───────────────────────────── sintesi ─────────────────────────────

SCHEMA = {
    "type": "object",
    "properties": {
        "sintesi": {"type": "string"},
        "temi": {"type": "array", "items": {"type": "string"}},
        "link": {"type": "array", "items": {"type": "object", "properties": {
            "id": {"type": "string"}, "descrizione": {"type": "string"}},
            "required": ["id", "descrizione"], "additionalProperties": False}},
        "documenti": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["sintesi", "temi", "link", "documenti"], "additionalProperties": False,
}

SISTEMA = """Sei il redattore della sintesi della comunità Telegram dell'Osservatorio Nazionale Sovranità Digitale (osservatorio.mxmap.it), un gruppo di cittadini, tecnici, giuristi e attivisti che discute di sovranità digitale della PA italiana.

Ricevi i messaggi di un periodo, con le persone indicate solo da pseudonimi (P1, P2…), e la lista degli URL condivisi (u1, u2…).

Scrivi in italiano:
- sintesi: 2-5 frasi su di che cosa si è discusso, le posizioni emerse, le domande aperte e le proposte. Tono sobrio e neutrale.
- temi: 2-6 temi in poche parole.
- link: i link utili alla comunità (articoli, documenti, dati, strumenti, normative), scelti SOLO dalla lista u1, u2…, ciascuno con una descrizione di una riga. Escludi link a profili personali, inviti a chat, contenuti privati o irrilevanti.
- documenti: i documenti/file condivisi rilevanti (nome e, se chiaro, di che cosa trattano).

PRIVACY, vincolante: non nominare né identificare nessuno, nemmeno con lo pseudonimo; niente citazioni letterali; niente dati personali (telefoni, email, indirizzi, fatti privati); ignora le conversazioni personali o fuori tema. Scrivi «si è discusso di», «alcuni partecipanti hanno proposto», mai «X ha detto». Non inventare nulla che non sia nei messaggi."""


def messaggi_periodo(c, chat, giorni):
    righe = []
    for data, p, testo, url, doc in c.execute(
            "SELECT data, persona, testo, url, documento FROM messaggi WHERE chat=? ORDER BY data", (chat,)):
        if giorno(data) in giorni:
            righe.append((data, p, testo, json.loads(url or "[]"), doc))
    return righe


def sintesi(periodo, prova=False, motore=None):
    """periodo: 'AAAA-MM-GG' oppure 'AAAA-Www'. Ritorna (dict, statistiche) o None."""
    motore = motore or os.environ.get("REGISTRO_MOTORE", "cli")
    chat = (comunita_ids() or [None])[0]
    if not chat:
        return None
    giorni = R.giorni_settimana(periodo) if "-W" in periodo else [periodo]
    c = db()
    righe = messaggi_periodo(c, chat, set(giorni))
    stat = {"messaggi": len(righe), "persone": len({r[1] for r in righe})}
    if len(righe) < MIN_MESSAGGI_SINTESI:
        return None, stat
    alias, urls, testo = {}, [], []
    for data, p, t, uu, doc in righe:
        a = alias.setdefault(p, f"P{len(alias) + 1}")
        for u in uu:
            if u not in urls:
                urls.append(u)
        testo.append(f"[{giorno(data)} {data[11:16]}] {a}: {t}" + (f" [file: {doc}]" if doc else ""))
    inp = (f"PERIODO: {giorni[0]}" + (f" – {giorni[-1]}" if len(giorni) > 1 else "") +
           f"\nMESSAGGI ({len(righe)}, {stat['persone']} persone):\n" + "\n".join(testo)[:400000] +
           "\n\nURL CONDIVISI:\n" + ("\n".join(f"u{i} {u}" for i, u in enumerate(urls, 1)) or "(nessuno)"))
    out = R.chiama_modello(SISTEMA, inp, SCHEMA, motore)
    out["link"] = [{"url": urls[int(x["id"][1:]) - 1], "descrizione": x["descrizione"]}
                   for x in out["link"] if re.fullmatch(r"u\d+", x["id"]) and 0 < int(x["id"][1:]) <= len(urls)]
    return out, stat


def testo_sintesi(titolo, out, stat, membri=None):
    e = R.esc
    righe = [f"💬 <b>{e(titolo)}</b>",
             f"{stat['messaggi']} messaggi da {stat['persone']} persone" + (f" · {membri:,} nel gruppo".replace(",", ".") if membri else "")]
    if out:
        righe += ["", e(out["sintesi"])]
        if out["temi"]:
            righe.append("<i>Temi:</i> " + e(" · ".join(out["temi"])))
        if out["link"]:
            righe.append("\n🔗 <b>Link condivisi</b>")
            righe += [f'• <a href="{e(x["url"])}">{e(x["descrizione"])}</a>' for x in out["link"][:12]]
        if out["documenti"]:
            righe.append("\n📎 <b>Documenti</b>")
            righe += [f"• {e(d)}" for d in out["documenti"][:8]]
    return "\n".join(righe)


def membri_oggi():
    s = serie()
    return next((r["membri"] for r in reversed(s) if r["membri"] is not None), None) if s else None


def post_giornaliero(g, prova=False):
    if not comunita_ids():
        return
    out, stat = sintesi(g, prova)
    if stat["messaggi"] == 0:
        return
    R.invia(testo_sintesi(f"Dalla comunità — {R.mesi_it(g)}", out, stat, membri_oggi()), prova, "feed")


def post_settimanale(sett, prova=False):
    if not comunita_ids():
        return
    out, stat = sintesi(sett, prova)
    dal, al = R.giorni_settimana(sett)[0], R.giorni_settimana(sett)[-1]
    titolo = f"La comunità nella settimana {dt.date.fromisoformat(dal).day}–{R.mesi_it(al).split(' ', 1)[1]}"
    R.invia(testo_sintesi(titolo, out, stat, membri_oggi()), prova, "feed")
    png = grafico()
    if png:
        invia_foto(png, "📈 <b>Andamento della comunità</b>: persone nel gruppo, messaggi e persone che scrivono, settimana per settimana.", prova, "feed")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("poll")
    sub.add_parser("chat")
    a = sub.add_parser("importa"); a.add_argument("file"); a.add_argument("--chat")
    sub.add_parser("statistiche")
    a = sub.add_parser("grafico"); a.add_argument("file", nargs="?")
    a = sub.add_parser("sintesi"); a.add_argument("periodo"); a.add_argument("--prova", action="store_true")
    x = ap.parse_args()
    if x.cmd == "poll":
        poll()
    elif x.cmd == "chat":
        print(json.dumps(json.loads(kv(db(), "chat_viste") or "{}"), ensure_ascii=False, indent=1))
    elif x.cmd == "importa":
        importa(x.file, x.chat)
    elif x.cmd == "statistiche":
        for r in serie():
            print(r)
    elif x.cmd == "grafico":
        print(grafico(x.file))
    elif x.cmd == "sintesi":
        (post_settimanale if "-W" in x.periodo else post_giornaliero)(x.periodo, x.prova)


if __name__ == "__main__":
    main()
