"""Generate Researchers Factsheet PDF (2 pages) — guide for researchers and analysts"""
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

OUTPUT = os.path.join(os.path.dirname(__file__), "Scheda_Ricercatori_Sovranita_Digitale_EN.pdf")

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
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "National Digital Sovereignty Observatory — Researchers Factsheet — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"p. {doc.page}")
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

    story.append(Paragraph("RESEARCHERS FACTSHEET", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Using the Observatory Data<br/>for Research", s_title))
    story.append(Paragraph("For researchers, academics, students and analysts — "
                           "National Digital Sovereignty Observatory", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("Open and reproducible data", s_h1))
    story.append(Paragraph(
        "The Observatory dataset is released under the CC BY-SA 4.0 licence, the collection pipeline "
        "is open source and the methodology is documented. Every result is verifiable and every "
        "analysis is replicable.", s_body))

    story.append(Paragraph("Data dictionary", s_h2))
    schema = [
        [Paragraph("Field", s_th), Paragraph("Type", s_th), Paragraph("Description", s_th)],
        [Paragraph("cod_amm", s_tc_b), Paragraph("string", s_tc), Paragraph("IPA code of the public body", s_tc)],
        [Paragraph("des_amm", s_tc_b), Paragraph("string", s_tc), Paragraph("Official name of the public body", s_tc)],
        [Paragraph("dominio", s_tc_b), Paragraph("string", s_tc), Paragraph("Institutional email domain", s_tc)],
        [Paragraph("mx_records", s_tc_b), Paragraph("string[]", s_tc), Paragraph("MX records detected for the domain", s_tc)],
        [Paragraph("provider", s_tc_b), Paragraph("string", s_tc), Paragraph("Identified email provider", s_tc)],
        [Paragraph("provider_country", s_tc_b), Paragraph("ISO 3166", s_tc), Paragraph("Country of the provider's registered office", s_tc)],
        [Paragraph("sovereignty", s_tc_b), Paragraph("enum", s_tc), Paragraph("IT / EU / EXTRA_EU", s_tc)],
        [Paragraph("categoria_ente", s_tc_b), Paragraph("string", s_tc), Paragraph("Type (Municipality, Local Health Authority, University, ...)", s_tc)],
        [Paragraph("regione", s_tc_b), Paragraph("string", s_tc), Paragraph("Region of belonging", s_tc)],
    ]
    story.append(grid_table(schema, [32 * mm, 24 * mm, 114 * mm]))
    story.append(Paragraph("The schema may vary between versions: refer to the header of the downloaded file.", s_small))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("Suggested research questions", s_h1))
    rq = [
        [Paragraph("Area", s_th), Paragraph("Question", s_th)],
        [Paragraph("Geography", s_tc_b), Paragraph("Territorial distribution of dependence on non-EU providers", s_tc)],
        [Paragraph("Body size", s_tc_b), Paragraph("Correlation between the body's size/resources and provider choice", s_tc)],
        [Paragraph("Type", s_tc_b), Paragraph("Comparison across categories (Municipalities, Local Health Authorities, Universities, Ministries)", s_tc)],
        [Paragraph("Policy", s_tc_b), Paragraph("Impact of AgID guidelines on technology choices over time", s_tc)],
        [Paragraph("Economics", s_tc_b), Paragraph("Estimate of public spending towards foreign vs domestic providers", s_tc)],
        [Paragraph("EU comparison", s_tc_b), Paragraph("Replication of the methodology on other Member States", s_tc)],
    ]
    story.append(grid_table(rq, [40 * mm, 130 * mm]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("How to cite", s_h1))
    cite = ("Pietrosanti, F. (2025). National Digital Sovereignty Observatory:\n"
            "State of digital sovereignty in the Italian public administration.\n"
            "MxMap.it data on IndicePA. CC BY-SA 4.0.\n"
            "https://osservatorio.mxmap.it/")
    story.append(box([Preformatted(cite, s_mono)]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Resources", s_h1))
    story.append(Paragraph("•  <b>Dataset</b> (CSV/JSON) and data dictionary — Open Data section of the website", s_bullet))
    story.append(Paragraph("•  <b>Full methodology</b> — Methodology section of the website", s_bullet))
    story.append(Paragraph("•  <b>Source code</b> and pipeline — the project's GitHub repository", s_bullet))
    story.append(Paragraph("•  <b>Detailed data by public body</b> — MxMap.it", s_bullet))

    story.append(Spacer(1, 2 * mm))
    story.append(box([
        Paragraph("Collaborations", s_box_title),
        Paragraph("Are you conducting research, a thesis or a publication on the Observatory data? "
                  "Contact us via GitHub: we are interested in giving visibility to independent studies "
                  "that use our data.", ParagraphStyle("bb", fontName="Arial", fontSize=8.5, textColor=DARK, leading=11)),
    ]))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("National Digital Sovereignty Observatory — "
                           "https://osservatorio.mxmap.it/ — "
                           "CC BY-SA 4.0 document.", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
