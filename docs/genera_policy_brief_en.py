"""Generate Policy Brief PDF — Digital Sovereignty in the Italian Public Administration (EN)"""
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
                      "Policy_Brief_Sovranita_Digitale_PA_EN.pdf")

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
        "National Digital Sovereignty Observatory — CC BY-SA 4.0 — "
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
        "Digital Sovereignty in the Italian<br/>Public Administration",
        style_title
    ))
    story.append(Paragraph(
        "National Digital Sovereignty Observatory — June 2025",
        style_subtitle
    ))
    story.append(HRFlowable(
        width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2
    ))

    # The problem
    story.append(Paragraph("The problem", style_h2))
    story.append(Paragraph(
        "The Italian Public Administration depends to a significant extent "
        "on digital infrastructure operated by providers subject to non-European "
        "jurisdictions. This dependence exposes institutional communications "
        "and citizens' data to concrete risks of access by foreign authorities, "
        "in particular through the United States <b>CLOUD Act</b> (2018), "
        "and stands in potential conflict with the <b>GDPR</b> and the rulings of the "
        "Court of Justice of the EU (<b>Schrems I</b> and <b>II</b>). In particular, "
        "<b>arts. 48 and 115 of the GDPR</b> prohibit giving effect to orders from "
        "non-EU authorities not grounded in international agreements: jurisdiction is "
        "determined by the <b>provider's nationality</b>, not the physical location of the data.",
        style_body
    ))

    # The numbers (gray box)
    box_content = [
        Paragraph("The numbers", style_box_title),
        Paragraph("•  ~23,000 PA bodies monitored (source: IndicePA)", style_bullet),
        Paragraph("•  Email services are the first area analysed", style_bullet),
        Paragraph("•  The mapping covers all registered institutional domains", style_bullet),
        Paragraph("•  Data is collected and updated through automated analysis of MX records", style_bullet),
        Paragraph("•  The dataset is open, verifiable and released under the CC BY-SA 4.0 licence", style_bullet),
    ]
    story.append(Spacer(1, 2 * mm))
    story.append(gray_box(box_content))

    # Regulatory context
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("The regulatory context", style_h2))
    story.append(Paragraph(
        "The European and Italian regulatory framework imposes precise obligations "
        "on the localisation and protection of PA data:",
        style_body
    ))

    # Table
    table_data = [
        [Paragraph("Rule", style_table_header),
         Paragraph("Relevance", style_table_header)],
        [Paragraph("GDPR (EU Reg. 2016/679)", style_table_cell_bold),
         Paragraph("Prohibits data transfers to third countries without adequate safeguards", style_table_cell)],
        [Paragraph("Schrems II (CJEU, 2020)", style_table_cell_bold),
         Paragraph("Invalidated the EU-US Privacy Shield", style_table_cell)],
        [Paragraph("CLOUD Act (USA, 2018)", style_table_cell_bold),
         Paragraph("Allows US access to data held by American providers even within the EU", style_table_cell)],
        [Paragraph("Italy's Cloud Strategy (2021)", style_table_cell_bold),
         Paragraph("Classifies PA data and provides for migration to qualified infrastructure", style_table_cell)],
        [Paragraph("NIS2 (EU Dir. 2022/2555)", style_table_cell_bold),
         Paragraph("Cybersecurity requirements for the PA and essential entities", style_table_cell)],
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

    # Recommendations
    story.append(Paragraph("Recommendations", style_h2))

    recs = [
        ("1. Mandatory census of the PA's digital services",
         "Make it mandatory for every body to declare the digital services it uses "
         "and their jurisdiction. Integrate this information into IndicePA to make it "
         "public and monitorable."),
        ("2. Sovereignty requirements in Consip framework agreements",
         "Introduce digital sovereignty criteria (data jurisdiction, server "
         "localisation, absence of obligations towards non-EU authorities) into "
         "framework agreements for email and cloud services."),
        ("3. National migration plan",
         "Define a plan with progressive deadlines for migrating the PA's email "
         "services to compliant providers. Provide dedicated funding from the PNRR "
         "or from cybersecurity budgets."),
        ("4. Continuous and transparent monitoring",
         "Institutionalise the monitoring of the PA's digital sovereignty with "
         "public data updated periodically."),
        ("5. Promotion of the model at European level",
         "Propose, in European fora, the adoption of a common framework for "
         "monitoring the digital sovereignty of public administrations across all "
         "member states."),
    ]

    for title, body in recs:
        story.append(Paragraph(title, style_rec_title))
        story.append(Paragraph(body, style_rec_body))

    # What you can do (gray box)
    story.append(Spacer(1, 2 * mm))
    box2 = [
        Paragraph("What you can do", style_box_title),
        Paragraph(
            "<b>If you are a member of parliament:</b> Table a parliamentary "
            "question citing the Observatory's data. Propose the inclusion of "
            "sovereignty requirements in legislation.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>If you are a PA manager:</b> Check your body's position "
            "and launch an internal assessment on migration.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>If you are a regulator:</b> Use the data to update the "
            "guidelines and introduce requirements into framework agreements.",
            style_body_box
        ),
    ]
    story.append(gray_box(box2))

    # Sources and references
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph("Sources and references", style_h2))
    refs = [
        "National Digital Sovereignty Observatory: "
        "https://osservatorio.mxmap.it/",
        "MxMap.it — Mapping of PA email providers: https://mxmap.it/",
        "IndicePA — Index of Public Administrations: https://indicepa.gov.it",
        "GDPR: EU Regulation 2016/679",
        "Schrems II ruling: CJEU C-311/18",
    ]
    for ref in refs:
        story.append(Paragraph(f"•  {ref}", style_ref))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=HexColor("#DEE2E6"),
        spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph(
        "This document is released under the CC BY-SA 4.0 licence. "
        "Contact: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale",
        style_small
    ))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
