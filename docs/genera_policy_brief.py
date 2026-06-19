"""Generate Policy Brief PDF — Sovranità Digitale nella PA Italiana"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__),
                      "Policy_Brief_Sovranita_Digitale_PA.pdf")

# Colors
BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
LIGHT_BLUE = HexColor("#E8F0FE")

# Register fonts
pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))

# Styles
style_label = ParagraphStyle(
    "Label", fontName="Arial-Bold", fontSize=11, textColor=BLUE,
    spaceAfter=2, spaceBefore=0, leading=13,
    letterSpacing=2
)
style_title = ParagraphStyle(
    "Title", fontName="Arial-Bold", fontSize=18, textColor=DARK,
    spaceAfter=4, spaceBefore=0, leading=22
)
style_subtitle = ParagraphStyle(
    "Subtitle", fontName="Arial", fontSize=10, textColor=GRAY_TEXT,
    spaceAfter=8, spaceBefore=0, leading=13
)
style_h2 = ParagraphStyle(
    "H2", fontName="Arial-Bold", fontSize=12, textColor=BLUE,
    spaceAfter=6, spaceBefore=10, leading=15
)
style_body = ParagraphStyle(
    "Body", fontName="Arial", fontSize=9.5, textColor=DARK,
    spaceAfter=6, spaceBefore=0, leading=13, alignment=TA_JUSTIFY
)
style_body_box = ParagraphStyle(
    "BodyBox", fontName="Arial", fontSize=9, textColor=DARK,
    spaceAfter=3, spaceBefore=0, leading=12, alignment=TA_LEFT
)
style_bullet = ParagraphStyle(
    "Bullet", fontName="Arial", fontSize=9, textColor=DARK,
    spaceAfter=2, spaceBefore=0, leading=12, leftIndent=12, bulletIndent=0,
    bulletFontName="Arial", bulletFontSize=9
)
style_rec_title = ParagraphStyle(
    "RecTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE,
    spaceAfter=2, spaceBefore=0, leading=12
)
style_rec_body = ParagraphStyle(
    "RecBody", fontName="Arial", fontSize=9, textColor=DARK,
    spaceAfter=6, spaceBefore=0, leading=12, alignment=TA_JUSTIFY
)
style_table_header = ParagraphStyle(
    "TH", fontName="Arial-Bold", fontSize=8.5, textColor=WHITE,
    leading=11
)
style_table_cell = ParagraphStyle(
    "TC", fontName="Arial", fontSize=8.5, textColor=DARK,
    leading=11
)
style_table_cell_bold = ParagraphStyle(
    "TCB", fontName="Arial-Bold", fontSize=8.5, textColor=DARK,
    leading=11
)
style_small = ParagraphStyle(
    "Small", fontName="Arial", fontSize=8, textColor=GRAY_TEXT,
    spaceAfter=4, spaceBefore=0, leading=10
)
style_footer_text = ParagraphStyle(
    "Footer", fontName="Arial-Italic", fontSize=7, textColor=GRAY_TEXT,
    leading=9, alignment=TA_CENTER
)
style_ref = ParagraphStyle(
    "Ref", fontName="Arial", fontSize=8, textColor=DARK,
    spaceAfter=2, spaceBefore=0, leading=10, leftIndent=8
)
style_box_title = ParagraphStyle(
    "BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE,
    spaceAfter=4, spaceBefore=0, leading=12
)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(
        A4[0] / 2, 10 * mm,
        "Osservatorio Nazionale Sovranità Digitale — CC BY-SA 4.0 — "
        "osservatorio-nazionale-sovranita-digitale"
    )
    canvas.restoreState()


def gray_box(content_elements):
    """Wrap content in a gray background table cell."""
    inner = []
    for el in content_elements:
        inner.append(el)
    t = Table([[inner]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return t


def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=18 * mm, bottomMargin=22 * mm
    )

    story = []

    # ── PAGE 1 ──

    # Title block
    story.append(Paragraph("POLICY BRIEF", style_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Sovranità Digitale nella Pubblica<br/>Amministrazione Italiana",
        style_title
    ))
    story.append(Paragraph(
        "Osservatorio Nazionale Sovranità Digitale — Giugno 2025",
        style_subtitle
    ))
    story.append(HRFlowable(
        width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2
    ))

    # Il problema
    story.append(Paragraph("Il problema", style_h2))
    story.append(Paragraph(
        "La Pubblica Amministrazione italiana dipende in misura significativa "
        "da infrastrutture digitali gestite da provider soggetti a giurisdizioni "
        "extra-europee. Questa dipendenza espone le comunicazioni istituzionali "
        "e i dati dei cittadini a rischi concreti di accesso da parte di autorità "
        "straniere, in particolare attraverso il <b>CLOUD Act</b> statunitense (2018), "
        "e si pone in potenziale contrasto con il <b>GDPR</b> e le sentenze della "
        "Corte di Giustizia dell’UE (<b>Schrems I</b> e <b>II</b>). In particolare, gli "
        "<b>artt. 48 e 115 del GDPR</b> vietano di dare seguito a ordini di autorità "
        "extra-UE non fondati su accordi internazionali: a determinare la giurisdizione "
        "è la <b>nazionalità del fornitore</b>, non la sede fisica del dato.",
        style_body
    ))

    # I numeri (gray box)
    box_content = [
        Paragraph("I numeri", style_box_title),
        Paragraph("•  ~23.000 enti PA monitorati (fonte IndicePA)", style_bullet),
        Paragraph("•  I servizi email sono il primo ambito analizzato", style_bullet),
        Paragraph("•  La mappatura copre tutti i domini istituzionali registrati", style_bullet),
        Paragraph("•  I dati sono raccolti e aggiornati tramite analisi automatica dei record MX", style_bullet),
        Paragraph("•  Il dataset è aperto, verificabile e rilasciato sotto licenza CC BY-SA 4.0", style_bullet),
    ]
    story.append(Spacer(1, 2 * mm))
    story.append(gray_box(box_content))

    # Contesto normativo
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Il contesto normativo", style_h2))
    story.append(Paragraph(
        "Il quadro normativo europeo e italiano impone obblighi precisi sulla "
        "localizzazione e protezione dei dati della PA:",
        style_body
    ))

    # Table
    table_data = [
        [Paragraph("Norma", style_table_header),
         Paragraph("Rilevanza", style_table_header)],
        [Paragraph("GDPR (Reg. UE 2016/679)", style_table_cell_bold),
         Paragraph("Vieta trasferimenti dati verso paesi terzi senza garanzie adeguate", style_table_cell)],
        [Paragraph("Schrems II (CGUE, 2020)", style_table_cell_bold),
         Paragraph("Ha invalidato il Privacy Shield UE-USA", style_table_cell)],
        [Paragraph("CLOUD Act (USA, 2018)", style_table_cell_bold),
         Paragraph("Consente accesso USA a dati di provider americani anche in UE", style_table_cell)],
        [Paragraph("Strategia Cloud Italia (2021)", style_table_cell_bold),
         Paragraph("Classifica i dati PA e prevede migrazione verso infrastrutture qualificate", style_table_cell)],
        [Paragraph("NIS2 (Dir. UE 2022/2555)", style_table_cell_bold),
         Paragraph("Requisiti cybersecurity per PA e soggetti essenziali", style_table_cell)],
    ]

    t = Table(table_data, colWidths=[55 * mm, 115 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 1), (-1, -1), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # ── PAGE 2 ──
    story.append(PageBreak())

    # Raccomandazioni
    story.append(Paragraph("Raccomandazioni", style_h2))

    recs = [
        ("1. Censimento obbligatorio dei servizi digitali della PA",
         "Rendere obbligatoria la dichiarazione dei servizi digitali utilizzati "
         "da ogni ente e della relativa giurisdizione. Integrare questa informazione "
         "nell’IndicePA per renderla pubblica e monitorabile."),
        ("2. Requisiti di sovranità nelle convenzioni Consip",
         "Inserire criteri di sovranità digitale (giurisdizione dati, localizzazione "
         "server, assenza obblighi verso autorità extra-UE) nelle convenzioni per "
         "servizi email e cloud."),
        ("3. Piano nazionale di migrazione",
         "Definire un piano con scadenze progressive per la migrazione dei servizi "
         "email della PA verso provider conformi. Prevedere fondi dedicati dal PNRR "
         "o dalla cybersecurity."),
        ("4. Monitoraggio continuo e trasparente",
         "Istituzionalizzare il monitoraggio della sovranità digitale della PA "
         "con dati pubblici e aggiornati periodicamente."),
        ("5. Promozione del modello a livello europeo",
         "Proporre nelle sedi europee l’adozione di un framework comune per il "
         "monitoraggio della sovranità digitale delle PA in tutti gli stati membri."),
    ]

    for title, body in recs:
        story.append(Paragraph(title, style_rec_title))
        story.append(Paragraph(body, style_rec_body))

    # Cosa puoi fare (gray box)
    story.append(Spacer(1, 2 * mm))
    box2 = [
        Paragraph("Cosa puoi fare", style_box_title),
        Paragraph(
            "<b>Se sei un parlamentare:</b> Presenta un’interrogazione citando "
            "i dati dell’Osservatorio. Proponi l’inserimento di requisiti di "
            "sovranità nella normativa.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>Se sei un dirigente PA:</b> Verifica la posizione del tuo ente "
            "e avvia una valutazione interna sulla migrazione.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>Se sei un regolatore:</b> Utilizza i dati per aggiornare le linee "
            "guida e inserire requisiti nelle convenzioni.",
            style_body_box
        ),
    ]
    story.append(gray_box(box2))

    # Fonti e riferimenti
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph("Fonti e riferimenti", style_h2))
    refs = [
        "Osservatorio Nazionale Sovranità Digitale: "
        "https://osservatorio.mxmap.it/",
        "MxMap.it — Mappatura provider email PA: https://mxmap.it/",
        "IndicePA — Indice delle Pubbliche Amministrazioni: https://indicepa.gov.it",
        "GDPR: Regolamento UE 2016/679",
        "Sentenza Schrems II: CGUE C-311/18",
    ]
    for ref in refs:
        story.append(Paragraph(f"•  {ref}", style_ref))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=HexColor("#DEE2E6"),
        spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph(
        "Questo documento è rilasciato sotto licenza CC BY-SA 4.0. "
        "Contatti: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale",
        style_small
    ))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
