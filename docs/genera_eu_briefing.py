"""Generate EU Briefing PDF (English) — Digital Sovereignty in the Italian PA, for EU institutions"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__), "EU_Briefing_Digital_Sovereignty_Italian_PA.pdf")

BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
AMBER_LIGHT = HexColor("#FFFBF0")
AMBER_BORDER = HexColor("#F0AD4E")

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))

s_label = ParagraphStyle("Label", fontName="Arial-Bold", fontSize=10, textColor=BLUE,
                         spaceAfter=2, leading=12, letterSpacing=2)
s_title = ParagraphStyle("Title", fontName="Arial-Bold", fontSize=18, textColor=DARK,
                         spaceAfter=4, leading=22)
s_subtitle = ParagraphStyle("Subtitle", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT,
                            spaceAfter=6, leading=12)
s_h1 = ParagraphStyle("H1", fontName="Arial-Bold", fontSize=13, textColor=BLUE,
                      spaceAfter=6, spaceBefore=10, leading=16)
s_body = ParagraphStyle("Body", fontName="Arial", fontSize=9.5, textColor=DARK,
                        spaceAfter=6, leading=13, alignment=TA_JUSTIFY)
s_bullet = ParagraphStyle("Bullet", fontName="Arial", fontSize=9, textColor=DARK,
                          spaceAfter=2, leading=12, leftIndent=14)
s_th = ParagraphStyle("TH", fontName="Arial-Bold", fontSize=8.5, textColor=WHITE, leading=11)
s_tc = ParagraphStyle("TC", fontName="Arial", fontSize=8.5, textColor=DARK, leading=11)
s_tc_bold = ParagraphStyle("TCB", fontName="Arial-Bold", fontSize=8.5, textColor=DARK, leading=11)
s_box_title = ParagraphStyle("BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE,
                             spaceAfter=3, leading=12)
s_box_body = ParagraphStyle("BoxBody", fontName="Arial", fontSize=9, textColor=DARK,
                            spaceAfter=2, leading=12)
s_small = ParagraphStyle("Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
                         spaceAfter=3, leading=9)
s_ref = ParagraphStyle("Ref", fontName="Arial", fontSize=8, textColor=DARK,
                       spaceAfter=2, leading=10, leftIndent=8)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(A4[0] / 2, 10 * mm,
                             "National Digital Sovereignty Observatory (Italy) — EU Briefing — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"p. {doc.page}")
    canvas.restoreState()


def box(elements, bg=GRAY_BG, border_color=None):
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]
    if border_color:
        style.append(("LINEBEFORE", (0, 0), (0, -1), 3, border_color))
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle(style))
    return t


def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=22 * mm)
    story = []

    # ── PAGE 1 ──
    story.append(Paragraph("EU BRIEFING", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Digital Sovereignty in the Italian<br/>Public Administration", s_title))
    story.append(Paragraph("For EU institutions, policymakers and researchers — "
                           "National Digital Sovereignty Observatory (Italy) — June 2025", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("The issue", s_h1))
    story.append(Paragraph(
        "Italy's Public Administration — around 23,000 entities — relies to a significant extent on "
        "email infrastructure operated by providers subject to non-EU jurisdiction. Because "
        "institutional email routinely carries citizens' personal data, this dependence exposes "
        "public communications to potential access by foreign authorities, most notably under the "
        "United States <b>CLOUD Act</b> (2018), in tension with the <b>GDPR</b> and the Court of "
        "Justice of the EU's <b>Schrems I and II</b> rulings.", s_body))

    story.append(box([
        Paragraph("Key findings", s_box_title),
        Paragraph("•  ~23,000 PA entities with institutional email domains were mapped (source: IndicePA)", s_bullet),
        Paragraph("•  A significant share rely on providers subject to extra-EU jurisdiction", s_bullet),
        Paragraph("•  US providers are subject to the CLOUD Act regardless of physical data location", s_bullet),
        Paragraph("•  The dependence is cross-cutting: municipalities, healthcare, universities, ministries", s_bullet),
        Paragraph("•  The dataset is open, reproducible and released under CC BY-SA 4.0", s_bullet),
    ]))

    story.append(Paragraph("Why it matters for the EU", s_h1))
    story.append(Paragraph(
        "The Italian case is not an isolated one: every Member State faces the same structural "
        "conflict between extra-EU jurisdiction over data and the European legal framework. A "
        "transparent, reproducible monitoring methodology — applied first to Italy — can be "
        "extended across the Union to support evidence-based policy on digital sovereignty.", s_body))
    story.append(Paragraph("•  <b>Data protection</b> — consistency with GDPR Chapter V on international transfers", s_bullet))
    story.append(Paragraph("•  <b>Cybersecurity</b> — supply-chain risk under NIS2 (Dir. EU 2022/2555)", s_bullet))
    story.append(Paragraph("•  <b>Strategic autonomy</b> — the EU's stated goal of digital sovereignty", s_bullet))
    story.append(Paragraph("•  <b>Single market</b> — fair conditions for EU cloud and email providers", s_bullet))

    story.append(box([
        Paragraph("The jurisdictional conflict in one line", s_box_title),
        Paragraph("The CLOUD Act can compel a US-based provider to disclose data even when stored in "
                  "the EU; the GDPR forbids such transfers without adequate safeguards. The conflict is "
                  "structural and cannot be fully resolved by contractual clauses alone.", s_box_body),
    ], AMBER_LIGHT, AMBER_BORDER))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("Methodology", s_h1))
    story.append(Paragraph(
        "The analysis is built on open, verifiable data. For every institutional domain listed in "
        "IndicePA (the authoritative register of Italian public bodies), the MX (Mail Exchange) DNS "
        "records are resolved and matched against a maintained database of provider patterns. Each "
        "entity is then classified by provider and by sovereignty (Italian / EU / extra-EU). The "
        "entire pipeline is open source and reproducible.", s_body))

    story.append(Paragraph("Policy relevance — EU frameworks", s_h1))
    table_data = [
        [Paragraph("Framework", s_th), Paragraph("Relevance to the findings", s_th)],
        [Paragraph("GDPR (Reg. EU 2016/679)", s_tc_bold),
         Paragraph("Chapter V restricts transfers of personal data to third countries", s_tc)],
        [Paragraph("Schrems II (CJEU C-311/18)", s_tc_bold),
         Paragraph("Invalidated Privacy Shield; SCCs insufficient where third-country law compels disclosure", s_tc)],
        [Paragraph("NIS2 (Dir. EU 2022/2555)", s_tc_bold),
         Paragraph("Supply-chain risk management duties for public entities", s_tc)],
        [Paragraph("EU Cloud Rulebook / EUCS", s_tc_bold),
         Paragraph("Sovereignty requirements for cloud services used by the public sector", s_tc)],
        [Paragraph("Digital Decade / strategic autonomy", s_tc_bold),
         Paragraph("Political objective of EU control over critical digital infrastructure", s_tc)],
    ]
    t = Table(table_data, colWidths=[55 * mm, 115 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Recommendations", s_h1))
    story.append(Paragraph("1.  <b>A common monitoring framework</b> — adopt a shared, open methodology "
                           "to measure PA digital sovereignty across Member States.", s_bullet))
    story.append(Paragraph("2.  <b>Transparency by default</b> — make provider and jurisdiction information "
                           "part of public administration registries.", s_bullet))
    story.append(Paragraph("3.  <b>Sovereignty in procurement</b> — embed jurisdiction and data-location "
                           "requirements in public tenders for email and cloud.", s_bullet))
    story.append(Paragraph("4.  <b>Support EU providers</b> — qualified public demand to strengthen a "
                           "competitive European cloud and email ecosystem.", s_bullet))

    story.append(Spacer(1, 3 * mm))
    story.append(box([
        Paragraph("Replicable across the Union", s_box_title),
        Paragraph("The methodology is country-agnostic: any Member State with a public registry of "
                  "institutional domains can be mapped the same way. The Observatory offers the open "
                  "methodology and tools as a basis for an EU-wide effort.", s_box_body),
    ]))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2))
    story.append(Paragraph("Sources and references", s_h1))
    for ref in [
        "National Digital Sovereignty Observatory — https://fpietrosanti.github.io/osservatorio-nazionale-sovranita-digitale/",
        "MxMap.it — Mapping of PA email providers — https://fpietrosanti.github.io/mxmap.it/",
        "IndicePA — Index of Italian Public Administrations — https://indicepa.gov.it",
        "GDPR — Regulation (EU) 2016/679",
        "Schrems II — CJEU, Case C-311/18 (16 July 2020)",
        "NIS2 — Directive (EU) 2022/2555",
    ]:
        story.append(Paragraph(f"•  {ref}", s_ref))
    story.append(Spacer(1, 3 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("Released under CC BY-SA 4.0. "
                           "Contact: github.com/fpietrosanti/osservatorio-nazionale-sovranita-digitale", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
