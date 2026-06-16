"""Generate Scheda Ricercatori PDF (2 pages) — guide for researchers and analysts"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__), "Scheda_Ricercatori_Sovranita_Digitale.pdf")

BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Mono", r"C:\Windows\Fonts\consola.ttf"))

s_label = ParagraphStyle("Label", fontName="Arial-Bold", fontSize=10, textColor=BLUE, spaceAfter=2, leading=12, letterSpacing=2)
s_title = ParagraphStyle("Title", fontName="Arial-Bold", fontSize=18, textColor=DARK, spaceAfter=4, leading=22)
s_subtitle = ParagraphStyle("Subtitle", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT, spaceAfter=6, leading=12)
s_h1 = ParagraphStyle("H1", fontName="Arial-Bold", fontSize=13, textColor=BLUE, spaceAfter=6, spaceBefore=10, leading=16)
s_h2 = ParagraphStyle("H2", fontName="Arial-Bold", fontSize=11, textColor=BLUE, spaceAfter=5, spaceBefore=8, leading=14)
s_body = ParagraphStyle("Body", fontName="Arial", fontSize=9.5, textColor=DARK, spaceAfter=6, leading=13, alignment=TA_JUSTIFY)
s_bullet = ParagraphStyle("Bullet", fontName="Arial", fontSize=9, textColor=DARK, spaceAfter=3, leading=12, leftIndent=12)
s_th = ParagraphStyle("TH", fontName="Arial-Bold", fontSize=8, textColor=WHITE, leading=10)
s_tc = ParagraphStyle("TC", fontName="Arial", fontSize=8, textColor=DARK, leading=10)
s_tc_b = ParagraphStyle("TCB", fontName="Arial-Bold", fontSize=8, textColor=DARK, leading=10)
s_mono = ParagraphStyle("MonoP", fontName="Mono", fontSize=7.5, textColor=DARK, leading=10)
s_small = ParagraphStyle("Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT, spaceAfter=3, leading=9)
s_box_title = ParagraphStyle("BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE, spaceAfter=3, leading=12)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "Osservatorio Nazionale Sovranità Digitale — Scheda Ricercatori — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"pag. {doc.page}")
    canvas.restoreState()


def box(elements, bg=GRAY_BG):
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 10),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("ROUNDEDCORNERS", [3, 3, 3, 3])]))
    return t


def grid_table(data, widths):
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=22 * mm)
    story = []

    story.append(Paragraph("SCHEDA RICERCATORI", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Usare i Dati dell'Osservatorio<br/>per la Ricerca", s_title))
    story.append(Paragraph("Per ricercatori, accademici, studenti e analisti — "
                           "Osservatorio Nazionale Sovranità Digitale", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("Dati aperti e riproducibili", s_h1))
    story.append(Paragraph(
        "Il dataset dell'Osservatorio è rilasciato sotto licenza CC BY-SA 4.0, la pipeline di "
        "raccolta è open source e la metodologia è documentata. Ogni risultato è verificabile e "
        "ogni analisi è replicabile.", s_body))

    story.append(Paragraph("Dizionario dati", s_h2))
    schema = [
        [Paragraph("Campo", s_th), Paragraph("Tipo", s_th), Paragraph("Descrizione", s_th)],
        [Paragraph("cod_amm", s_tc_b), Paragraph("string", s_tc), Paragraph("Codice IPA dell'ente", s_tc)],
        [Paragraph("des_amm", s_tc_b), Paragraph("string", s_tc), Paragraph("Denominazione ufficiale dell'ente", s_tc)],
        [Paragraph("dominio", s_tc_b), Paragraph("string", s_tc), Paragraph("Dominio email istituzionale", s_tc)],
        [Paragraph("mx_records", s_tc_b), Paragraph("string[]", s_tc), Paragraph("Record MX rilevati per il dominio", s_tc)],
        [Paragraph("provider", s_tc_b), Paragraph("string", s_tc), Paragraph("Provider email identificato", s_tc)],
        [Paragraph("provider_country", s_tc_b), Paragraph("ISO 3166", s_tc), Paragraph("Paese di sede legale del provider", s_tc)],
        [Paragraph("sovereignty", s_tc_b), Paragraph("enum", s_tc), Paragraph("IT / EU / EXTRA_EU", s_tc)],
        [Paragraph("categoria_ente", s_tc_b), Paragraph("string", s_tc), Paragraph("Tipologia (Comune, ASL, Università, ...)", s_tc)],
        [Paragraph("regione", s_tc_b), Paragraph("string", s_tc), Paragraph("Regione di appartenenza", s_tc)],
    ]
    story.append(grid_table(schema, [32 * mm, 24 * mm, 114 * mm]))
    story.append(Paragraph("Lo schema può variare tra versioni: fare riferimento all'header del file scaricato.", s_small))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("Domande di ricerca suggerite", s_h1))
    rq = [
        [Paragraph("Area", s_th), Paragraph("Domanda", s_th)],
        [Paragraph("Geografia", s_tc_b), Paragraph("Distribuzione territoriale della dipendenza da provider extra-UE", s_tc)],
        [Paragraph("Dimensione ente", s_tc_b), Paragraph("Correlazione tra dimensione/risorse dell'ente e scelta del provider", s_tc)],
        [Paragraph("Tipologia", s_tc_b), Paragraph("Confronto tra categorie (Comuni, ASL, Università, Ministeri)", s_tc)],
        [Paragraph("Policy", s_tc_b), Paragraph("Impatto delle linee guida AgID sulle scelte tecnologiche nel tempo", s_tc)],
        [Paragraph("Economia", s_tc_b), Paragraph("Stima della spesa pubblica verso provider esteri vs nazionali", s_tc)],
        [Paragraph("Comparazione UE", s_tc_b), Paragraph("Replica della metodologia su altri Stati membri", s_tc)],
    ]
    story.append(grid_table(rq, [40 * mm, 130 * mm]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Come citare", s_h1))
    cite = ("Pietrosanti, F. (2025). Osservatorio Nazionale Sovranita' Digitale:\n"
            "Stato della sovranita' digitale nella PA italiana.\n"
            "Dati MxMap.it su IndicePA. CC BY-SA 4.0.\n"
            "https://osservatorio.mxmap.it/")
    story.append(box([Preformatted(cite, s_mono)]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Risorse", s_h1))
    story.append(Paragraph("•  <b>Dataset</b> (CSV/JSON) e dizionario dati — sezione Dati Aperti del sito", s_bullet))
    story.append(Paragraph("•  <b>Metodologia</b> completa — sezione Metodologia del sito", s_bullet))
    story.append(Paragraph("•  <b>Codice sorgente</b> e pipeline — repository GitHub del progetto", s_bullet))
    story.append(Paragraph("•  <b>Dati di dettaglio per ente</b> — MxMap.it", s_bullet))

    story.append(Spacer(1, 2 * mm))
    story.append(box([
        Paragraph("Collaborazioni", s_box_title),
        Paragraph("Stai conducendo una ricerca, una tesi o una pubblicazione sui dati dell'Osservatorio? "
                  "Contattaci tramite GitHub: siamo interessati a dare visibilità agli studi indipendenti "
                  "che usano i nostri dati.", ParagraphStyle("bb", fontName="Arial", fontSize=8.5, textColor=DARK, leading=11)),
    ]))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("Osservatorio Nazionale Sovranità Digitale — "
                           "https://osservatorio.mxmap.it/ — "
                           "Documento CC BY-SA 4.0.", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
