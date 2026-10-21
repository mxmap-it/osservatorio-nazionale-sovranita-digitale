#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Risoluzione dei font per i generatori di PDF, indipendente dal sistema.

Perché esiste: i generatori registravano percorsi come C:\\Windows\\Fonts\\arial.ttf.
Su quella macchina funzionava; su qualsiasi altra il clone si fermava al primo
avvio. Qui i font vengono cercati nei posti dove stanno davvero su Windows,
macOS e Linux, e si sceglie la prima famiglia disponibile.

Ordine di preferenza, e perché:
  1. Arial       — è ciò con cui i PDF pubblicati sono stati composti;
                   rigenerandoli su Windows si ottiene lo stesso risultato
  2. Liberation Sans — metricamente compatibile con Arial, diffusa su Linux
  3. DejaVu Sans — quasi sempre presente, copertura Unicode ampia
  4. Helvetica/Arimo — ripieghi su macOS e distribuzioni minimali

I PDF pubblicati sono committati e vanno RIPRISTINATI, non rigenerati: una
differenza di font conta solo per chi li rifà davvero da capo.

Uso:
    from _font import registra_famiglia
    registra_famiglia()       # registra "Arial", "Arial-Bold", "Arial-Italic", ...
"""
import glob
import os
import sys

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# cartelle di sistema dove cercare, per piattaforma
CARTELLE = [
    r"C:\Windows\Fonts",                                   # Windows
    "/System/Library/Fonts", "/Library/Fonts",             # macOS
    os.path.expanduser("~/Library/Fonts"),
    "/usr/share/fonts", "/usr/local/share/fonts",          # Linux
    os.path.expanduser("~/.local/share/fonts"),
    os.path.expanduser("~/.fonts"),
]

# famiglie candidate: (nome, regular, bold, italic, bold-italic)
FAMIGLIE = [
    ("Arial",           "arial.ttf",            "arialbd.ttf",        "ariali.ttf",         "arialbi.ttf"),
    ("Liberation Sans", "LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf",
                        "LiberationSans-Italic.ttf",  "LiberationSans-BoldItalic.ttf"),
    ("DejaVu Sans",     "DejaVuSans.ttf",       "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf",
                        "DejaVuSans-BoldOblique.ttf"),
    ("Arimo",           "Arimo-Regular.ttf",    "Arimo-Bold.ttf",     "Arimo-Italic.ttf",   "Arimo-BoldItalic.ttf"),
    ("Helvetica",       "Helvetica.ttc",        "Helvetica.ttc",      "Helvetica.ttc",      "Helvetica.ttc"),
]

# monospazio, usato da alcuni generatori per i blocchi di codice
MONO = [
    ("Consolas",        "consola.ttf",          "consolab.ttf"),
    ("DejaVu Sans Mono", "DejaVuSansMono.ttf",  "DejaVuSansMono-Bold.ttf"),
    ("Liberation Mono", "LiberationMono-Regular.ttf", "LiberationMono-Bold.ttf"),
    ("Menlo",           "Menlo.ttc",            "Menlo.ttc"),
]

_cache = {}


def trova(nome_file):
    """Percorso del font, cercato ricorsivamente nelle cartelle di sistema."""
    if nome_file in _cache:
        return _cache[nome_file]
    for cartella in CARTELLE:
        if not os.path.isdir(cartella):
            continue
        diretto = os.path.join(cartella, nome_file)
        if os.path.exists(diretto):
            _cache[nome_file] = diretto
            return diretto
        trovati = glob.glob(os.path.join(cartella, "**", nome_file), recursive=True)
        if trovati:
            _cache[nome_file] = trovati[0]
            return trovati[0]
    _cache[nome_file] = None
    return None


def _registra(alias, percorso):
    try:
        pdfmetrics.registerFont(TTFont(alias, percorso))
        return True
    except Exception:
        return False


def registra_famiglia(alias="Arial", mono_alias="Consolas"):
    """Registra la prima famiglia disponibile sotto i nomi attesi dagli script.

    Gli script usano "Arial", "Arial-Bold", "Arial-Italic", "Arial-BoldItalic":
    i nomi restano quelli anche quando il font sottostante è un altro, così non
    c'è nulla da cambiare nel corpo dei generatori.

    Restituisce il nome della famiglia effettivamente usata.
    """
    for nome, reg, bold, ital, bi in FAMIGLIE:
        p_reg = trova(reg)
        if not p_reg:
            continue
        ok = _registra(alias, p_reg)
        if not ok:
            continue
        for suffisso, nf in (("-Bold", bold), ("-Italic", ital), ("-BoldItalic", bi)):
            p = trova(nf)
            if not (p and _registra(alias + suffisso, p)):
                _registra(alias + suffisso, p_reg)   # ripiego sul regular
        # monospazio: facoltativo, alcuni generatori non lo usano
        for nome_m, m_reg, m_bold in MONO:
            p_m = trova(m_reg)
            if p_m and _registra(mono_alias, p_m):
                p_mb = trova(m_bold)
                _registra(mono_alias + "-Bold", p_mb or p_m)
                # quattro generatori usano il nome "Mono"
                _registra("Mono", p_m)
                _registra("Mono-Bold", p_mb or p_m)
                break
        if nome != "Arial":
            sys.stderr.write(
                "[_font] Arial non disponibile: uso «%s». I PDF rigenerati "
                "avranno un font diverso da quelli pubblicati.\n" % nome)
        return nome

    raise RuntimeError(
        "Nessun font utilizzabile trovato.\n"
        "Installare una di queste famiglie e riprovare:\n"
        "  Debian/Ubuntu : sudo apt install fonts-liberation fonts-dejavu\n"
        "  Fedora        : sudo dnf install liberation-fonts dejavu-sans-fonts\n"
        "  macOS         : i font di sistema bastano, verificare i permessi\n"
        "Cartelle esaminate: " + ", ".join(c for c in CARTELLE if os.path.isdir(c))
    )



def percorso_sans(stile="regular", preferisci_segoe=False):
    """Percorso di un font sans-serif utilizzabile, per librerie che vogliono un
    file invece di un nome registrato (PIL, fpdf).

    stile: "regular" | "bold" | "italic"
    """
    base = {
        "regular": ["arial.ttf", "LiberationSans-Regular.ttf", "DejaVuSans.ttf",
                    "Arimo-Regular.ttf", "Helvetica.ttc"],
        "bold":    ["arialbd.ttf", "LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf",
                    "Arimo-Bold.ttf", "Helvetica.ttc"],
        "italic":  ["ariali.ttf", "LiberationSans-Italic.ttf", "DejaVuSans-Oblique.ttf",
                    "Arimo-Italic.ttf", "Helvetica.ttc"],
    }[stile]
    # Segoe UI solo su richiesta: è il font con cui è disegnata la copertina
    # LinkedIn, ma NON quello con cui sono composti i PDF pubblicati. Metterlo
    # per primo ovunque cambierebbe le interruzioni di riga dei PDF.
    if preferisci_segoe:
        segoe = {"regular": "segoeui.ttf", "bold": "segoeuib.ttf",
                 "italic": "segoeuii.ttf"}[stile]
        candidati = [segoe] + base
    else:
        candidati = base

    for nome in candidati:
        p = trova(nome)
        if p:
            return p
    raise RuntimeError(
        "Nessun font sans-serif trovato per lo stile «%s».\n"
        "Debian/Ubuntu: sudo apt install fonts-liberation fonts-dejavu" % stile)

if __name__ == "__main__":
    fam = registra_famiglia()
    print("famiglia registrata: %s" % fam)
    for n in ("Arial", "Arial-Bold", "Arial-Italic", "Arial-BoldItalic", "Consolas"):
        try:
            pdfmetrics.getFont(n)
            print("  %-18s ok" % n)
        except Exception:
            print("  %-18s ASSENTE" % n)
