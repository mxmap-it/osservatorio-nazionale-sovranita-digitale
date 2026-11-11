#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepara il deck per SFSCon 2026 partendo da quello di RomHack.

NON rigenera nulla: apre il deck definitivo rivisto a mano (39 slide, con gli
screenshot), ne aggiorna copertina e numeri preservando formattazione e
immagini, e aggiunge la sezione sull'analisi della spesa ICT.

  Talk: «MXMap Italia: Observatory of Digital Sovereignty of Italian Public
  Agencies» — SFSCon 2026, sabato 14 novembre, 14:20, Auditorium (A2), 35'.

Numeri da mxmap.it/kpi.json del 2026-11-09; spesa ICT dallo STATE.md del
progetto analisi-spesa-ict al 2026-11-06. Ciò che è misurato da noi e ciò che
è riferito da terzi resta distinto, come nel resto del progetto.

Uso:  python tools/aggiorna-slide-sfscon.py
"""
import copy
import os
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORGENTE = os.path.join(ROOT, "static", "slide", "romhack-2026-mxmap-italia.pptx")
USCITA = os.path.join(ROOT, "static", "slide", "sfscon-2026-mxmap-italia.pptx")

ASSET = os.path.join(ROOT, "static", "slide", "_assets")
MARCHIO_EUCN = os.path.join(ASSET, "eu-china-commons-mark.png")
QR_EUCN = os.path.join(ASSET, "eu-china-commons-qr.png")

NAVY, NAVY_SCURO = RGBColor(0x17, 0x32, 0x4D), RGBColor(0x0E, 0x20, 0x33)
BLU, BIANCO, GRIGIO = RGBColor(0x6D, 0xB3, 0xFF), RGBColor(0xFF, 0xFF, 0xFF), RGBColor(0x9E, 0xB2, 0xC6)
ROSSO, VERDE = RGBColor(0xFF, 0x6B, 0x74), RGBColor(0x5C, 0xB8, 0x8A)
W, H = Inches(13.333), Inches(7.5)

# ---------------------------------------------------------------- sostituzioni
# (testo esatto da cercare, testo nuovo). Si applicano run per run, così i
# caratteri e i colori restano quelli scelti a mano.
SOSTITUZIONI = [
    # copertina
    ("Fabio Pietrosanti (naif)  ·  RomHack Camp 2026  ·  2 October, STAGE 2",
     "Fabio Pietrosanti (naif)  ·  SFSCon 2026  ·  14 November, Auditorium A2"),
    # sezione risultati
    ("22,987 Italian public bodies, 97% coverage",
     "22,922 Italian public bodies, 94% coverage"),
    # pannelli dei numeri (slide 11 e 12, identiche)
    ("46.1%", "43.3%"),
    ("10.586 bodies", "9,915 bodies"),
    ("51.2%", "50.5%"),
    ("11.772 bodies", "11,581 bodies"),
    ("0.0%", "0.5%"),
    ("0 bodies", "123 bodies"),
    ("2.7%", "5.7%"),
    ("629 bodies", "1,303 bodies"),
    ("Source: mxmap.it on IndicePA data · 22987 bodies, 97.26% coverage · snapshot 2026-06-14 · CC BY-SA 4.0",
     "Source: mxmap.it on IndicePA data · 22,922 bodies, 94.32% coverage · snapshot 2026-11-09 · CC BY-SA 4.0"),
    # provider
    ("Google Workspace — 27.7% of public bodies (6.374)",
     "Google Workspace — 26.9% of public bodies (6,157)"),
    ("Microsoft 365 — 18.3% (4.203)", "Microsoft 365 — 16.4% (3,751)"),
    ("Italian providers — 33.6%   ·   self-run infrastructure — 13.5%   ·   Italian cloud — 4.2%",
     "Italian providers — 42.9%   ·   Italian cloud — 4.0%   ·   self-run — 3.6%   ·   European (non-Italian) — 0.5%"),
    # cybersecurity
    ("Two vendors carry 46% of Italian public email.",
     "Two vendors carry 43% of Italian public email."),
]


def sostituisci(prs):
    """Sostituisce il testo dentro i run, per non perdere la formattazione."""
    fatte = {}
    for s in prs.slides:
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            for par in sh.text_frame.paragraphs:
                # un run alla volta: se la stringa e' spezzata fra run, si
                # ricompone il paragrafo mantenendo il formato del primo run
                intero = "".join(r.text for r in par.runs)
                nuovo = intero
                for vecchio, sost in SOSTITUZIONI:
                    if vecchio in nuovo:
                        nuovo = nuovo.replace(vecchio, sost)
                        fatte[vecchio] = fatte.get(vecchio, 0) + 1
                if nuovo != intero and par.runs:
                    par.runs[0].text = nuovo
                    for r in par.runs[1:]:
                        r.text = ""
    return fatte


def rendi_grassetto(prs):
    """Trasforma i **così** rimasti a video in vero grassetto.

    Nel deck di RomHack i marcatori Markdown erano finiti stampati sulle slide.
    Qui il paragrafo viene ricomposto: il primo run fa da modello per font,
    corpo e colore, e i pezzi fra i doppi asterischi diventano run in grassetto.
    """
    cambiati = 0
    for s in prs.slides:
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            for par in sh.text_frame.paragraphs:
                intero = "".join(r.text for r in par.runs)
                if "**" not in intero or not par.runs:
                    continue
                modello = par.runs[0]
                formato = (modello.font.size, modello.font.color,
                           modello.font.name, modello.font.underline)
                pezzi = [p for p in intero.split("**") if p != ""]
                grassetto_primo = intero.startswith("**")
                # si riusa il primo run e si aggiungono gli altri in coda
                for r in par.runs[1:]:
                    r._r.getparent().remove(r._r)
                for n, pezzo in enumerate(pezzi):
                    r = modello if n == 0 else par.add_run()
                    r.text = pezzo
                    if n > 0:
                        r.font.size = formato[0]
                        r.font.name = formato[2]
                        r.font.underline = formato[3]
                        if formato[1].type is not None:
                            try:
                                r.font.color.rgb = formato[1].rgb
                            except AttributeError:
                                pass
                    r.font.bold = (n % 2 == 0) if grassetto_primo else (n % 2 == 1)
                cambiati += 1
    return cambiati


# ---------------------------------------------------------------- nuove slide
def _txt(s, testo, x, y, w, h, size=18, bold=False, colore=BIANCO,
         align=PP_ALIGN.LEFT, interlinea=1.25, spazio=9):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, riga in enumerate(testo if isinstance(testo, list) else [testo]):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.alignment = align
        par.line_spacing = interlinea
        par.space_after = Pt(spazio)
        # il grassetto si marca con **così**, anche a metà riga: si spezza sui
        # delimitatori e i pezzi dispari diventano run in grassetto
        pezzi = riga.split("**")
        for n, pezzo in enumerate(pezzi):
            if pezzo == "":
                continue
            r = par.add_run()
            r.text = pezzo
            r.font.size, r.font.bold = Pt(size), bold or (n % 2 == 1)
            r.font.color.rgb = colore
            r.font.name = "Segoe UI"
    return tb


def _fondo(s, colore):
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = colore


def _barra(s, colore=BLU):
    sh = s.shapes.add_shape(1, 0, 0, W, Inches(0.09))
    sh.fill.solid(); sh.fill.fore_color.rgb = colore
    sh.line.fill.background(); sh.shadow.inherit = False


def nuova(prs, vuota):
    return prs.slides.add_slide(vuota)


def costruisci_sezione_spesa(prs, vuota):
    """Quattro slide sull'analisi della spesa ICT."""
    nuove = []

    # --- divisore di sezione
    s = nuova(prs, vuota); _fondo(s, NAVY_SCURO); _barra(s)
    _txt(s, "02 · continues", Inches(0.9), Inches(2.4), Inches(5), Inches(0.8), size=20, bold=True, colore=BLU)
    _txt(s, "Following the money", Inches(0.9), Inches(3.2), Inches(11.5), Inches(1.6), size=34, bold=True)
    _txt(s, "The same question asked of the contracts, not of the DNS",
         Inches(0.95), Inches(4.7), Inches(11), Inches(1), size=17, colore=GRIGIO)
    nuove.append(s)

    # --- cosa abbiamo misurato
    s = nuova(prs, vuota); _fondo(s, NAVY); _barra(s)
    _txt(s, "What we actually did", Inches(0.75), Inches(0.55), Inches(11.9), Inches(1), size=29, bold=True)
    _txt(s, "Every public contract in Italy since 2024", Inches(0.78), Inches(1.5), Inches(11.8), Inches(0.6),
         size=15, colore=BLU)
    _txt(s, [
        "**3,745,883 contract notices (CIG)** pulled from the national public-contracts database, "
        "then filtered down in stages — each stage published, each stage reproducible.",
        "**85.9% excluded with certainty**: not ICT at all. What survives is the part that needs judgement.",
        "**Certain cloud spending: 4,537 contracts, €1.21bn.** Plus €0.72bn awarded in-house.",
        "**The hard part is not the sum. It is the ceiling.** Framework agreements and concessions publish "
        "a maximum, not what was spent. We separated the two: €58.2bn in scope, of which €14.4bn still "
        "uncertain — and we say which 79 contracts they are.",
    ], Inches(0.78), Inches(2.15), Inches(11.8), Inches(4.3), size=16)
    _txt(s, "Method, code and intermediate files are public. The uncertain stays labelled uncertain.",
         Inches(0.78), H - Inches(1.2), Inches(11.2), Inches(0.7), size=12, colore=GRIGIO)
    nuove.append(s)

    # --- la convergenza
    s = nuova(prs, vuota); _fondo(s, NAVY); _barra(s)
    _txt(s, "Two instruments, two methods, one answer", Inches(0.75), Inches(0.55), Inches(11.9), Inches(1),
         size=29, bold=True)
    _txt(s, "The result that matters", Inches(0.78), Inches(1.5), Inches(11.8), Inches(0.6), size=15, colore=BLU)
    _txt(s, "43.3%", Inches(1.1), Inches(2.5), Inches(4.5), Inches(1.4), size=58, bold=True, colore=ROSSO)
    _txt(s, ["**who operates the email**",
             "of 22,922 public bodies,",
             "read from public DNS records"],
         Inches(1.15), Inches(4.0), Inches(4.5), Inches(1.8), size=15, colore=GRIGIO, interlinea=1.2, spazio=2)
    _txt(s, "45%", Inches(7.3), Inches(2.5), Inches(4.5), Inches(1.4), size=58, bold=True, colore=ROSSO)
    _txt(s, ["**where the cloud money goes**",
             "of €1.21bn in certain cloud contracts,",
             "read from awarded public contracts"],
         Inches(7.35), Inches(4.0), Inches(4.5), Inches(1.8), size=15, colore=GRIGIO, interlinea=1.2, spazio=2)
    _txt(s, "Different sources, different methods, independently built — and they land in the same place. "
            "Neither confirms the other; together they make the number hard to dismiss.",
         Inches(0.78), Inches(5.9), Inches(11.8), Inches(1), size=16, bold=True)
    nuove.append(s)

    # --- cosa impedisce di contare
    s = nuova(prs, vuota); _fondo(s, NAVY); _barra(s, ROSSO)
    _txt(s, "What stops anyone from counting", Inches(0.75), Inches(0.55), Inches(11.9), Inches(1),
         size=29, bold=True)
    _txt(s, "Eighteen defects found, seventeen written up for the authority",
         Inches(0.78), Inches(1.5), Inches(11.8), Inches(0.6), size=15, colore=BLU)
    _txt(s, [
        "**1,282 placeholder tax codes** in the contracting-authority register: bodies recorded as "
        "«CFAVCP-…» instead of an identifier. You cannot aggregate what you cannot name.",
        "**20 public bodies out of 617** have published the procurement-plan data they are required to publish.",
        "**The ceiling problem, quantified**: framework agreements and concessions publish a maximum. Read "
        "naively, Italian public ICT looks like €113bn. Read with the ceilings separated, €58.2bn.",
        "**National cloud programme**: €4.38bn committed in the public database — against €0.79bn of revenue "
        "reported for 2023-25 in the company's own accounts. We report both and label which is which.",
    ], Inches(0.78), Inches(2.15), Inches(11.8), Inches(4.3), size=15)
    _txt(s, "Each defect is written as a problem with a proposed remedy. None of it requires new law — only "
            "that existing obligations be met.",
         Inches(0.78), H - Inches(1.2), Inches(11.2), Inches(0.7), size=12, colore=GRIGIO)
    nuove.append(s)
    return nuove


def costruisci_eu_china(prs, vuota):
    """Slide sull'Europe–China Digital Commons Observatory.

    Numeri dallo STATE.md del progetto eu-china-digital-commons all'11/11/2026.
    Sito, repo e casella verificati vivi lo stesso giorno (HTTP 200 su
    eu-china-commons.eu e sul repo; MX del dominio su smtp.google.com).
    """
    s = nuova(prs, vuota); _fondo(s, NAVY); _barra(s)

    if os.path.exists(MARCHIO_EUCN):
        s.shapes.add_picture(MARCHIO_EUCN, Inches(9.35), Inches(1.35),
                             width=Inches(3.45))
        zh = _txt(s, "中欧数字公地观察站", Inches(9.35), Inches(3.75), Inches(3.45),
                  Inches(0.6), size=19, bold=True, colore=BIANCO, align=PP_ALIGN.CENTER)
        # Segoe UI non ha i glifi cinesi: il font va detto, non lasciato al ripiego
        for par in zh.text_frame.paragraphs:
            for r in par.runs:
                r.font.name = "Microsoft YaHei"
        _txt(s, ["Europe–China Digital", "Commons Observatory"], Inches(9.35),
             Inches(4.35), Inches(3.45), Inches(0.9), size=13, colore=GRIGIO,
             align=PP_ALIGN.CENTER, interlinea=1.15, spazio=0)

    _txt(s, "The same method, pointed somewhere else",
         Inches(0.75), Inches(0.55), Inches(8.4), Inches(1.1), size=28, bold=True)
    _txt(s, "Europe–China Digital Commons Observatory — research in progress",
         Inches(0.78), Inches(1.62), Inches(8.4), Inches(0.6), size=15, colore=BLU)
    _txt(s, [
        "**Who funds, builds and reuses open source** in Europe and in China — "
        "read from public sources on both sides, in English and in Chinese, "
        "rather than from press releases.",
        "**62 initiatives** in a four-level registry, 66% of them on primary sources · "
        "**13 verified public-sector reuse cases** (EU 8, China 5) · **40 papers** in a "
        "systematic review · every source archived with its SHA-256.",
        "**A finding, not a gap:** documented open-source deployments inside Chinese "
        "public administrations are scarce — and the scarcity is itself the result.",
    ], Inches(0.78), Inches(2.3), Inches(8.3), Inches(3.4), size=15)

    if os.path.exists(QR_EUCN):
        s.shapes.add_picture(QR_EUCN, Inches(0.78), Inches(5.55), height=Inches(1.3))
    _txt(s, ["**eu-china-commons.eu**",
             "contact@eu-china-commons.eu",
             "github.com/fpietrosanti/eu-china-commons  ·  data CC BY 4.0"],
         Inches(2.3), Inches(5.65), Inches(7), Inches(1.3), size=14,
         colore=GRIGIO, interlinea=1.15, spazio=2)
    return [s]


def sposta_dopo(prs, nuove, indice_dopo):
    """Le slide aggiunte finiscono in coda: si spostano dopo `indice_dopo` (0-based)."""
    lst = prs.slides._sldIdLst
    elementi = list(lst)
    coda = elementi[-len(nuove):]
    for el in coda:
        lst.remove(el)
    for off, el in enumerate(coda):
        lst.insert(indice_dopo + 1 + off, el)


def rimuovi_doppioni(prs):
    """Elimina le slide consecutive con lo stesso testo, tenendo la piu' ricca.

    Nel deck di RomHack la slide sui risultati della posta compare due volte,
    identica nei numeri: una delle due ha in piu' la mappa. Si tiene quella
    con piu' immagini. Se non ci sono doppioni non si tocca nulla.
    """
    def firma(s):
        return "\n".join(sh.text_frame.text.strip() for sh in s.shapes
                         if sh.has_text_frame and sh.text_frame.text.strip())

    def immagini(s):
        return sum(1 for sh in s.shapes if sh.shape_type == 13)

    slide = list(prs.slides)
    da_togliere = []
    for i in range(len(slide) - 1):
        a, b = slide[i], slide[i + 1]
        if firma(a) and firma(a) == firma(b):
            # si scarta quella con meno immagini (a parita', la prima)
            scarto = i if immagini(a) <= immagini(b) else i + 1
            da_togliere.append(scarto)

    lst = prs.slides._sldIdLst
    elementi = list(lst)
    for i in sorted(set(da_togliere), reverse=True):
        # va tolta anche la relazione, altrimenti la parte resta nel pacchetto
        # e in salvataggio due slide finiscono sullo stesso nome: file rotto
        prs.part.drop_rel(elementi[i].rId)
        lst.remove(elementi[i])
    return [i + 1 for i in sorted(set(da_togliere))]


def main():
    if not os.path.exists(SORGENTE):
        sys.exit("Manca il deck sorgente: %s" % SORGENTE)
    prs = Presentation(SORGENTE)
    prima = len(prs.slides._sldIdLst)

    fatte = sostituisci(prs)
    print("Sostituzioni applicate:")
    for vecchio, _ in SOSTITUZIONI:
        n = fatte.get(vecchio, 0)
        print("   %-62s %s" % (vecchio[:62], ("%dx" % n) if n else "NON TROVATO"))

    n = rendi_grassetto(prs)
    print("\nParagrafi con **marcatori** convertiti in grassetto vero: %d" % n)

    vuota = prs.slide_layouts[6]
    nuove = costruisci_sezione_spesa(prs, vuota)
    # la sezione va in coda ai risultati sulla posta: si cerca l'ultima slide
    # prima del divisore «03», invece di fidarsi di un indice fisso
    dopo = None
    for i, s in enumerate(prs.slides):
        # la barra in cima ha una cornice di testo vuota: si scartano i vuoti
        testi = [sh.text_frame.text.strip() for sh in s.shapes
                 if sh.has_text_frame and sh.text_frame.text.strip()]
        if testi and testi[0] == "03":
            dopo = i - 1
            break
    if dopo is None:
        sys.exit("Divisore «03» non trovato: collocazione della nuova sezione incerta, mi fermo.")
    sposta_dopo(prs, nuove, dopo)
    print("\nSezione inserita dopo la slide %d (prima del divisore 03)." % (dopo + 1))

    # EU–China: va in fondo, subito prima della slide «Contribute»
    if not os.path.exists(MARCHIO_EUCN):
        sys.exit("Mancano gli asset EU–China: esegui prima "
                 "python tools/genera-asset-eu-china.py")
    eucn = costruisci_eu_china(prs, vuota)
    prima_di = None
    for i, s in enumerate(prs.slides):
        testi = [sh.text_frame.text.strip() for sh in s.shapes
                 if sh.has_text_frame and sh.text_frame.text.strip()]
        if testi and testi[0] == "Contribute":
            prima_di = i
            break
    if prima_di is None:
        sys.exit("Slide «Contribute» non trovata: non so dove mettere EU–China.")
    sposta_dopo(prs, eucn, prima_di - 1)
    print("Slide EU–China inserita alla posizione %d (prima di «Contribute»)." % prima_di)

    # la rimozione va per ultima: se si rimuove prima, add_slide riusa i nomi
    # di parte (slideNN.xml) ancora occupati dalle slide rimaste, e il file esce
    # con due parti sullo stesso nome, cioe' rotto
    togliere = rimuovi_doppioni(prs)
    if togliere:
        print("Slide doppie rimosse: %s" % ", ".join(str(n) for n in togliere))
    else:
        print("Nessuna slide doppia trovata: non rimuovo niente.")

    prs.save(USCITA)
    print("\n%s  |  %d slide (prima %d)  |  %d KB"
          % (os.path.relpath(USCITA, ROOT), len(prs.slides._sldIdLst), prima,
             os.path.getsize(USCITA) // 1024))


if __name__ == "__main__":
    main()
