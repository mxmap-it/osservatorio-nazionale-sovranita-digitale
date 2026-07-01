"""Generate Business Case PDF — Migration to sovereign providers (for IT/EU providers and Consip)"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
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
                      "Business_Case_Migrazione_Sovranita_PA_EN.pdf")

BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
GREEN_LIGHT = HexColor("#F0FFF0")
GREEN_BORDER = HexColor("#5CB85C")
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
s_h2 = ParagraphStyle("H2", fontName="Arial-Bold", fontSize=11, textColor=BLUE,
                      spaceAfter=5, spaceBefore=8, leading=14)
s_body = ParagraphStyle("Body", fontName="Arial", fontSize=9, textColor=DARK,
                        spaceAfter=5, leading=12.5, alignment=TA_JUSTIFY)
s_bullet = ParagraphStyle("Bullet", fontName="Arial", fontSize=9, textColor=DARK,
                          spaceAfter=2, leading=12, leftIndent=14)
s_th = ParagraphStyle("TH", fontName="Arial-Bold", fontSize=8, textColor=WHITE, leading=10)
s_tc = ParagraphStyle("TC", fontName="Arial", fontSize=8, textColor=DARK, leading=10)
s_tc_bold = ParagraphStyle("TCB", fontName="Arial-Bold", fontSize=8, textColor=DARK, leading=10)
s_box_title = ParagraphStyle("BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE,
                             spaceAfter=3, leading=12)
s_box_body = ParagraphStyle("BoxBody", fontName="Arial", fontSize=8.5, textColor=DARK,
                            spaceAfter=2, leading=11)
s_small = ParagraphStyle("Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
                         spaceAfter=3, leading=9)
s_ref = ParagraphStyle("Ref", fontName="Arial", fontSize=7.5, textColor=DARK,
                       spaceAfter=2, leading=9.5, leftIndent=8)
s_kpi_num = ParagraphStyle("KpiNum", fontName="Arial-Bold", fontSize=20, textColor=BLUE,
                           alignment=TA_CENTER, leading=22)
s_kpi_lbl = ParagraphStyle("KpiLbl", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
                           alignment=TA_CENTER, leading=9)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(A4[0] / 2, 10 * mm,
                             "National Digital Sovereignty Observatory — Business Case — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"p. {doc.page}")
    canvas.restoreState()


def box(elements, bg=GRAY_BG, border_color=None):
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
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
    story.append(Paragraph("BUSINESS CASE", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Migration to Sovereign Providers:<br/>A Market Opportunity", s_title))
    story.append(Paragraph("For Italian and European IT providers, Consip and central purchasing bodies — "
                           "National Digital Sovereignty Observatory — June 2025", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("In brief", s_h1))
    story.append(Paragraph(
        "The Italian Public Administration — around 23,000 bodies — today depends to a "
        "significant extent on email providers subject to non-EU jurisdiction. "
        "Regulatory developments (GDPR, Schrems II, Italy's Cloud Strategy, NIS2) and growing "
        "political attention are driving migration to sovereign infrastructure. This "
        "represents a <b>significant market opportunity</b> for Italian and European providers "
        "and a <b>strategic lever</b> for public purchasing bodies.", s_body))

    # KPI cards row
    story.append(Spacer(1, 2 * mm))
    kpi_row = [[
        Table([[Paragraph("~23,000", s_kpi_num)], [Paragraph("PA bodies as potential clients", s_kpi_lbl)]]),
        Table([[Paragraph("—%", s_kpi_num)], [Paragraph("today on non-EU providers", s_kpi_lbl)]]),
        Table([[Paragraph("—%", s_kpi_num)], [Paragraph("contestable market share", s_kpi_lbl)]]),
    ]]
    kt = Table(kpi_row, colWidths=[56 * mm, 56 * mm, 56 * mm])
    kt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY_BG),
        ("BOX", (0, 0), (0, 0), 0.5, WHITE), ("BOX", (1, 0), (1, 0), 0.5, WHITE),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("INNERGRID", (0, 0), (-1, -1), 2, WHITE),
    ]))
    story.append(kt)
    story.append(Paragraph("The percentage values will be updated with the data from the next report "
                           "(source: MxMap.it on IndicePA).", s_small))

    story.append(Paragraph("The context: a demand in the making", s_h1))
    story.append(Paragraph(
        "Three converging forces are transforming digital sovereignty from a niche topic into a "
        "purchasing requirement for the PA:", s_body))
    story.append(Paragraph("•  <b>Regulatory pressure</b> — GDPR and Schrems II make the use of providers "
                           "subject to the CLOUD Act legally fragile; Italy's Cloud Strategy requires the "
                           "qualification of infrastructure.", s_bullet))
    story.append(Paragraph("•  <b>Political pressure</b> — digital sovereignty has entered the Italian and "
                           "European institutional agenda, with growing demand for national alternatives.", s_bullet))
    story.append(Paragraph("•  <b>Reputational pressure</b> — bodies are increasingly aware of the "
                           "jurisdictional risk and are seeking solutions that shield them from it.", s_bullet))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Why now", s_box_title),
        Paragraph("The market window opens when the regulatory framework becomes stringent but "
                  "the sovereign offering is still poorly structured. It is the moment when a provider can "
                  "position itself as a benchmark before the market consolidates.", s_box_body),
    ], AMBER_LIGHT, AMBER_BORDER))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("1. The potential market", s_h1))
    story.append(Paragraph(
        "The pool is the entire Italian PA recorded in IndicePA. Segmentation by type of "
        "body makes it possible to identify the highest-priority targets with the greatest propensity to migrate.", s_body))

    seg = [
        [Paragraph("Segment", s_th), Paragraph("Bodies (order of magnitude)", s_th),
         Paragraph("Migration priority", s_th), Paragraph("Data sensitivity", s_th)],
        [Paragraph("Municipalities", s_tc_bold), Paragraph("~7,900", s_tc), Paragraph("High", s_tc), Paragraph("Registry, taxes", s_tc)],
        [Paragraph("Local health authorities / Healthcare", s_tc_bold), Paragraph("Hundreds", s_tc), Paragraph("Critical", s_tc), Paragraph("Health data", s_tc)],
        [Paragraph("Schools / Universities", s_tc_bold), Paragraph("Thousands", s_tc), Paragraph("Medium", s_tc), Paragraph("Student data", s_tc)],
        [Paragraph("Central PA / Ministries", s_tc_bold), Paragraph("Dozens", s_tc), Paragraph("Critical", s_tc), Paragraph("Acts, policy", s_tc)],
        [Paragraph("Regions / Provinces", s_tc_bold), Paragraph("~120", s_tc), Paragraph("High", s_tc), Paragraph("Services, healthcare", s_tc)],
    ]
    t = Table(seg, colWidths=[45 * mm, 45 * mm, 38 * mm, 42 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)
    story.append(Paragraph("The figures are indicative orders of magnitude from IndicePA; the precise "
                           "data per segment will be published in the report.", s_small))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2. The value proposition of the sovereign provider", s_h1))
    story.append(Paragraph(
        "A provider that wants to win this market must build an offering around "
        "elements that the large non-EU operators cannot guarantee by design:", s_body))
    story.append(Paragraph("•  <b>Guaranteed EU/IT jurisdiction</b> — no disclosure obligations "
                           "towards non-European authorities (no CLOUD Act).", s_bullet))
    story.append(Paragraph("•  <b>Documented compliance</b> — GDPR by design, ACN qualification, "
                           "certified data localisation.", s_bullet))
    story.append(Paragraph("•  <b>Continuity and independence</b> — no risk of disruption from "
                           "unilateral foreign decisions or geopolitical tensions.", s_bullet))
    story.append(Paragraph("•  <b>Support and proximity</b> — native-language assistance, SLAs on national "
                           "time zone and legislation, local roots.", s_bullet))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Differentiation, not price competition", s_box_title),
        Paragraph("The sovereign provider does not need to beat the large operators on price per terabyte, "
                  "but on value: compliance, reduction of legal risk and autonomy. It is a sale "
                  "of risk management, not of a commodity.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ── PAGE 3 ──
    story.append(PageBreak())
    story.append(Paragraph("3. The lever of public procurement", s_h1))
    story.append(Paragraph(
        "Consip and the central purchasing bodies play a decisive role: the criteria of framework agreements "
        "and framework contracts effectively steer the technological choices of thousands of bodies. "
        "Introducing sovereignty requirements into tenders simultaneously creates qualified demand and "
        "a level playing field for compliant providers.", s_body))

    story.append(Paragraph("3.1 Sovereignty requirements that can be included in tenders", s_h2))
    proc = [
        [Paragraph("Requirement", s_th), Paragraph("Effect", s_th)],
        [Paragraph("Exclusive EU jurisdiction over data", s_tc_bold),
         Paragraph("Excludes providers subject to non-EU disclosure legislation", s_tc)],
        [Paragraph("Data centre localisation in EU/IT", s_tc_bold),
         Paragraph("Guarantees physical control and traceability", s_tc)],
        [Paragraph("ACN qualification of the service", s_tc_bold),
         Paragraph("Aligns the purchase with Italy's Cloud Strategy", s_tc)],
        [Paragraph("Data reversibility and portability", s_tc_bold),
         Paragraph("Avoids lock-in and enables future competition", s_tc)],
        [Paragraph("Transparency on subcontractors and MX", s_tc_bold),
         Paragraph("Makes the sovereignty chain verifiable", s_tc)],
    ]
    t = Table(proc, colWidths=[70 * mm, 100 * mm])
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
    story.append(Paragraph("3.2 Benefits for central purchasing bodies", s_h2))
    story.append(Paragraph("•  <b>Reduction of aggregate risk</b> — a compliant supplier base "
                           "lowers the legal exposure of the entire PA.", s_bullet))
    story.append(Paragraph("•  <b>Stimulus to national industry</b> — qualified public demand "
                           "grows a competitive European IT ecosystem.", s_bullet))
    story.append(Paragraph("•  <b>Consistency with strategic objectives</b> — the purchase becomes "
                           "an instrument of industrial policy and autonomy.", s_bullet))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("4. Path and obstacles", s_h1))
    story.append(Paragraph(
        "Migration is not free of friction. Recognising this is part of the business case: whoever offers "
        "a managed migration path, and not just a product, wins.", s_body))
    obs = [
        [Paragraph("Obstacle", s_th), Paragraph("Mitigation on the supply side", s_th)],
        [Paragraph("Migration costs and timescales", s_tc_bold),
         Paragraph("Turnkey migration services, import tools, hands-on support", s_tc)],
        [Paragraph("Habit with widespread tools", s_tc_bold),
         Paragraph("Interoperability, training, familiar interfaces", s_tc)],
        [Paragraph("Perception of lower reliability", s_tc_bold),
         Paragraph("Solid SLAs, public references, certifications", s_tc)],
        [Paragraph("Fragmentation of bodies", s_tc_bold),
         Paragraph("Framework agreements and aggregated offers via Consip", s_tc)],
    ]
    t = Table(obs, colWidths=[70 * mm, 100 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("5. Call to action", s_h1))
    story.append(box([
        Paragraph("For Italian and European IT providers", s_box_title),
        Paragraph("Build an explicit sovereignty offering: communicate jurisdiction, compliance and "
                  "migration path. Use the Observatory's public data to size the "
                  "market and identify the priority segments.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(box([
        Paragraph("For Consip and central purchasing bodies", s_box_title),
        Paragraph("Introduce sovereignty requirements into email and cloud framework agreements. Turn "
                  "public spending into a lever of strategic autonomy and industrial growth.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2))
    story.append(Paragraph("Sources", s_h2))
    for ref in [
        "National Digital Sovereignty Observatory — https://osservatorio.mxmap.it/",
        "MxMap.it — Mapping of PA email providers — https://mxmap.it/",
        "IndicePA — https://indicepa.gov.it",
        "Italy's Cloud Strategy (2021); ACN Regulation no. 307/2022",
        "GDPR (EU Reg. 2016/679); Schrems II (CJEU C-311/18)",
    ]:
        story.append(Paragraph(f"•  {ref}", s_ref))
    story.append(Spacer(1, 3 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("Document released under a CC BY-SA 4.0 licence. "
                           "Contact: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
