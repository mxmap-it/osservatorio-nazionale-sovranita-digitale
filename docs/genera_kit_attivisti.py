"""Generate Kit Attivisti PDF (2 pages) — practical toolkit for civic activists"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__), "Kit_Attivisti_Sovranita_Digitale.pdf")

BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
GREEN_LIGHT = HexColor("#F0FFF0")
GREEN_BORDER = HexColor("#5CB85C")

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Mono", r"C:\Windows\Fonts\consola.ttf"))

s_label = ParagraphStyle("Label", fontName="Arial-Bold", fontSize=10, textColor=BLUE, spaceAfter=2, leading=12, letterSpacing=2)
s_title = ParagraphStyle("Title", fontName="Arial-Bold", fontSize=18, textColor=DARK, spaceAfter=4, leading=22)
s_subtitle = ParagraphStyle("Subtitle", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT, spaceAfter=6, leading=12)
s_h1 = ParagraphStyle("H1", fontName="Arial-Bold", fontSize=13, textColor=BLUE, spaceAfter=6, spaceBefore=10, leading=16)
s_body = ParagraphStyle("Body", fontName="Arial", fontSize=9.5, textColor=DARK, spaceAfter=6, leading=13, alignment=TA_JUSTIFY)
s_step_t = ParagraphStyle("StepT", fontName="Arial-Bold", fontSize=10, textColor=BLUE, spaceAfter=2, leading=12)
s_step_b = ParagraphStyle("StepB", fontName="Arial", fontSize=9, textColor=DARK, spaceAfter=6, leading=12)
s_bullet = ParagraphStyle("Bullet", fontName="Arial", fontSize=9, textColor=DARK, spaceAfter=3, leading=12, leftIndent=12)
s_mono = ParagraphStyle("MonoP", fontName="Mono", fontSize=8, textColor=DARK, leading=11)
s_small = ParagraphStyle("Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT, spaceAfter=3, leading=9)
s_box_title = ParagraphStyle("BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE, spaceAfter=3, leading=12)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "Osservatorio Nazionale Sovranità Digitale — Kit Attivisti — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"pag. {doc.page}")
    canvas.restoreState()


def box(elements, bg=GRAY_BG, border_color=None):
    style = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 10),
             ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("ROUNDEDCORNERS", [3, 3, 3, 3])]
    if border_color:
        style.append(("LINEBEFORE", (0, 0), (0, -1), 3, border_color))
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle(style))
    return t


def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=22 * mm)
    story = []

    story.append(Paragraph("KIT ATTIVISTI", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Agire sulla Sovranità Digitale<br/>della tua Amministrazione", s_title))
    story.append(Paragraph("Strumenti pratici per cittadini attivi — "
                           "Osservatorio Nazionale Sovranità Digitale", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("Perché il tuo gesto conta", s_h1))
    story.append(Paragraph(
        "Non serve essere esperti di tecnologia. Quando un cittadino chiede al proprio Comune dove "
        "finiscono le sue email, l'amministrazione è costretta a porsi la domanda. La pressione "
        "civica, moltiplicata, diventa consapevolezza istituzionale e poi azione.", s_body))

    story.append(Paragraph("Quattro passi concreti", s_h1))
    for t, b in [
        ("1. Verifica il tuo ente",
         "Cerca il tuo Comune, ASL o scuola nei dati dell'Osservatorio e scopri quale provider gestisce le email e sotto quale giurisdizione."),
        ("2. Fai la domanda giusta",
         "Scrivi all'ente e chiedi quale provider email usa, dove sono archiviati i dati e se è stata fatta una valutazione del rischio giurisdizionale."),
        ("3. Diffondi i dati",
         "Condividi i risultati sui social e con la stampa locale: \"dove finiscono le email del nostro Comune\" è una notizia di forte impatto sul territorio."),
        ("4. Porta il tema in consiglio",
         "Proponi a un consigliere comunale una mozione o un'interrogazione sulla sovranità digitale dell'ente, usando i dati come base."),
    ]:
        story.append(Paragraph(t, s_step_t))
        story.append(Paragraph(b, s_step_b))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Messaggi chiave", s_box_title),
        Paragraph("•  \"I tuoi dati possono finire su server soggetti a leggi straniere.\"", s_bullet),
        Paragraph("•  \"La sovranità digitale è: chi controlla i dati dei cittadini.\"", s_bullet),
        Paragraph("•  \"Non è contro un fornitore: è a favore del controllo pubblico sui dati pubblici.\"", s_bullet),
        Paragraph("•  \"Esistono alternative europee conformi. Serve la volontà di usarle.\"", s_bullet),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("Modello di richiesta di accesso civico", s_h1))
    story.append(Paragraph(
        "Puoi usare l'accesso civico generalizzato (art. 5, c. 2, D.Lgs. 33/2013) per ottenere "
        "informazioni dall'ente. Adatta il testo seguente al tuo caso:", s_body))

    fac = ("Oggetto: Richiesta di accesso civico generalizzato\n"
           "(art. 5, c. 2, D.Lgs. 33/2013)\n\n"
           "Il/la sottoscritto/a [nome], chiede di conoscere:\n\n"
           "1. quale fornitore gestisce il servizio di posta\n"
           "   elettronica dell'ente;\n"
           "2. in quale Paese sono archiviati i dati di posta;\n"
           "3. se il fornitore e' soggetto a normative extra-UE\n"
           "   che ne consentano l'accesso da parte di autorita'\n"
           "   straniere (es. CLOUD Act statunitense);\n"
           "4. se e' stata effettuata una valutazione d'impatto\n"
           "   sulla protezione dei dati (DPIA) per tale servizio.\n\n"
           "Distinti saluti,\n"
           "[nome, luogo, data]")
    story.append(box([Preformatted(fac, s_mono)]))
    story.append(Paragraph("Modello informativo, da adattare al caso concreto. Non costituisce "
                           "consulenza legale.", s_small))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Dove trovare i dati e coordinarti", s_h1))
    story.append(Paragraph("•  <b>Dati e report</b>: il sito dell'Osservatorio e i suoi documenti scaricabili", s_bullet))
    story.append(Paragraph("•  <b>Dati di dettaglio per ente</b>: MxMap.it", s_bullet))
    story.append(Paragraph("•  <b>Coordinamento</b>: canale Telegram dell'Osservatorio", s_bullet))
    story.append(Paragraph("•  <b>Segnalazioni e proposte</b>: GitHub Issues del progetto", s_bullet))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("Osservatorio Nazionale Sovranità Digitale — "
                           "https://fpietrosanti.github.io/osservatorio-nazionale-sovranita-digitale/ — "
                           "Documento CC BY-SA 4.0.", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
