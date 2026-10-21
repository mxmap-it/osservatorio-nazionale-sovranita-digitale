#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dice in pochi secondi se questo computer può costruire il progetto.

Pensato per il primo avvio dopo un «git clone»: invece di scoprire un pezzo
mancante al terzo comando, lo si sa subito e con l'istruzione per rimediare.

    python tools/verifica-ambiente.py

Uscita 0 se tutto l'essenziale c'è, 1 altrimenti.
"""
import importlib
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OK, KO, NOTA = "  ok  ", " MANCA", " nota "
problemi = []


def riga(stato, voce, dettaglio=""):
    print("[%s] %-34s %s" % (stato, voce, dettaglio))


print("Verifica ambiente — Osservatorio Nazionale Sovranità Digitale")
print("=" * 74)

# ---------------------------------------------------------------- il sito
print("\nSITO (necessario)")
hugo = shutil.which("hugo")
if hugo:
    try:
        v = subprocess.run([hugo, "version"], capture_output=True, text=True, timeout=30).stdout.strip()
        esteso = "extended" in v
        riga(OK if esteso else KO, "Hugo", v.split("+")[0].replace("hugo ", ""))
        if not esteso:
            problemi.append("Serve Hugo **Extended**: questa è la versione normale. "
                            "https://github.com/gohugoio/hugo/releases")
    except Exception as e:
        riga(KO, "Hugo", str(e)[:40]); problemi.append("Hugo non eseguibile")
else:
    riga(KO, "Hugo", "non trovato nel PATH")
    problemi.append("Installare Hugo Extended ≥ 0.163: https://gohugo.io/installation/")

dati = os.path.join(ROOT, "data", "kpi.json")
riga(OK if os.path.exists(dati) else KO, "data/kpi.json",
     "%d byte" % os.path.getsize(dati) if os.path.exists(dati) else "assente")
if not os.path.exists(dati):
    problemi.append("data/kpi.json manca: il sito costruisce ma senza i numeri in home")

# ---------------------------------------------------------------- generatori
print("\nGENERATORI DI PDF E SLIDE (facoltativi: gli artefatti sono già in git)")
moduli = [("reportlab", "reportlab"), ("fpdf", "fpdf2"), ("pptx", "python-pptx"),
          ("PIL", "pillow"), ("pypdf", "pypdf"), ("bs4", "beautifulsoup4"),
          ("lxml", "lxml"), ("segno", "segno")]
mancanti = []
for modulo, pacchetto in moduli:
    try:
        importlib.import_module(modulo)
        riga(OK, pacchetto)
    except ImportError:
        riga(NOTA, pacchetto, "non installato")
        mancanti.append(pacchetto)
if mancanti:
    problemi.append("Per rigenerare gli artefatti: python -m pip install -r requirements.txt")

# ---------------------------------------------------------------- font
print("\nFONT")
sys.path.insert(0, os.path.join(ROOT, "docs"))
try:
    from _font import registra_famiglia, percorso_sans
    try:
        fam = registra_famiglia()
        riga(OK if fam == "Arial" else NOTA, "famiglia per i PDF", fam)
        if fam != "Arial":
            print("        I PDF rigenerati avranno un font diverso da quelli pubblicati.")
            print("        Non è un problema: gli artefatti vanno ripristinati da git.")
        riga(OK, "font per le immagini", os.path.basename(percorso_sans("regular")))
    except RuntimeError as e:
        riga(KO, "font", str(e).split("\n")[0])
        problemi.append(str(e))
except ImportError:
    riga(NOTA, "font", "reportlab non installato, controllo saltato")

# ---------------------------------------------------------------- artefatti
print("\nARTEFATTI PUBBLICATI (devono stare in git, non si rigenerano)")
for p, atteso in [("static/pdf", 20), ("static/slide", 1), ("static/brand", 10)]:
    d = os.path.join(ROOT, p)
    n = len([f for f in os.listdir(d)
             if os.path.isfile(os.path.join(d, f))]) if os.path.isdir(d) else 0
    riga(OK if n >= atteso else KO, p, "%d file" % n)
    if n < atteso:
        problemi.append("%s ha %d file, attesi almeno %d: clone incompleto?" % (p, n, atteso))

# ---------------------------------------------------------------- esito
print("\n" + "=" * 74)
if problemi:
    print("DA SISTEMARE:\n")
    for i, p in enumerate(problemi, 1):
        print("  %d. %s" % (i, p))
    sys.exit(1)
print("Tutto a posto. Per costruire il sito:  hugo --quiet --gc")
sys.exit(0)
