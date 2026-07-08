"""Generate Technical Brief PDF — Technical-Regulatory Analysis for Regulators (EN)"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__),
                      "Technical_Brief_Sovranita_Digitale_PA_EN.pdf")

# Colors
BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
RED_LIGHT = HexColor("#FFF3F3")
RED_BORDER = HexColor("#D9534F")
GREEN_LIGHT = HexColor("#F0FFF0")
GREEN_BORDER = HexColor("#5CB85C")
AMBER_LIGHT = HexColor("#FFFBF0")
AMBER_BORDER = HexColor("#F0AD4E")

# Register fonts
pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", r"C:\Windows\Fonts\arialbi.ttf"))

# Styles
s_label = ParagraphStyle(
    "Label", fontName="Arial-Bold", fontSize=10, textColor=BLUE,
    spaceAfter=2, leading=12, letterSpacing=2
)
s_title = ParagraphStyle(
    "Title", fontName="Arial-Bold", fontSize=17, textColor=DARK,
    spaceAfter=4, leading=21
)
s_subtitle = ParagraphStyle(
    "Subtitle", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT,
    spaceAfter=6, leading=12
)
s_h1 = ParagraphStyle(
    "H1", fontName="Arial-Bold", fontSize=13, textColor=BLUE,
    spaceAfter=6, spaceBefore=10, leading=16
)
s_h2 = ParagraphStyle(
    "H2", fontName="Arial-Bold", fontSize=11, textColor=BLUE,
    spaceAfter=5, spaceBefore=8, leading=14
)
s_h3 = ParagraphStyle(
    "H3", fontName="Arial-Bold", fontSize=9.5, textColor=DARK,
    spaceAfter=3, spaceBefore=6, leading=12
)
s_body = ParagraphStyle(
    "Body", fontName="Arial", fontSize=9, textColor=DARK,
    spaceAfter=5, leading=12.5, alignment=TA_JUSTIFY
)
s_body_small = ParagraphStyle(
    "BodySmall", fontName="Arial", fontSize=8.5, textColor=DARK,
    spaceAfter=3, leading=11, alignment=TA_JUSTIFY
)
s_bullet = ParagraphStyle(
    "Bullet", fontName="Arial", fontSize=9, textColor=DARK,
    spaceAfter=2, leading=12, leftIndent=14, bulletIndent=0,
    bulletFontName="Arial", bulletFontSize=9
)
s_bullet_small = ParagraphStyle(
    "BulletSmall", fontName="Arial", fontSize=8.5, textColor=DARK,
    spaceAfter=2, leading=11, leftIndent=14, bulletIndent=0,
    bulletFontName="Arial", bulletFontSize=8.5
)
s_th = ParagraphStyle(
    "TH", fontName="Arial-Bold", fontSize=8, textColor=WHITE, leading=10
)
s_tc = ParagraphStyle(
    "TC", fontName="Arial", fontSize=8, textColor=DARK, leading=10
)
s_tc_bold = ParagraphStyle(
    "TCB", fontName="Arial-Bold", fontSize=8, textColor=DARK, leading=10
)
s_box_title = ParagraphStyle(
    "BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE,
    spaceAfter=3, leading=12
)
s_box_body = ParagraphStyle(
    "BoxBody", fontName="Arial", fontSize=8.5, textColor=DARK,
    spaceAfter=2, leading=11
)
s_footer = ParagraphStyle(
    "Footer", fontName="Arial-Italic", fontSize=7, textColor=GRAY_TEXT,
    leading=9, alignment=TA_CENTER
)
s_small = ParagraphStyle(
    "Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
    spaceAfter=3, leading=9
)
s_ref = ParagraphStyle(
    "Ref", fontName="Arial", fontSize=7.5, textColor=DARK,
    spaceAfter=2, leading=9.5, leftIndent=8
)
s_page_num = ParagraphStyle(
    "PageNum", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
    leading=9, alignment=TA_CENTER
)
s_quote = ParagraphStyle(
    "Quote", fontName="Arial-Italic", fontSize=8.5, textColor=GRAY_TEXT,
    spaceAfter=5, spaceBefore=3, leading=11, leftIndent=12, rightIndent=12,
    alignment=TA_JUSTIFY
)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(
        A4[0] / 2, 10 * mm,
        "National Digital Sovereignty Observatory — Technical Brief — CC BY-SA 4.0"
    )
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"p. {doc.page}")
    canvas.restoreState()


def gray_box(elements, bg=GRAY_BG):
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return t


def colored_box(elements, bg, border_color):
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEBEFOREBORDERRADIUS", (0, 0), (-1, -1), 3),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border_color),
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

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 1 — Cover + Executive Summary
    # ═══════════════════════════════════════════════════════════════════

    story.append(Paragraph("TECHNICAL BRIEF", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Technical-Regulatory Analysis of Digital<br/>"
        "Dependence in the Italian Public Administration",
        s_title
    ))
    story.append(Paragraph(
        "For AgID, ACN, Garante for the Protection of Personal Data — "
        "National Digital Sovereignty Observatory — June 2025",
        s_subtitle
    ))
    story.append(HRFlowable(
        width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2
    ))

    # Executive Summary
    story.append(Paragraph("Executive Summary", s_h1))
    story.append(Paragraph(
        "This document analyses the Italian Public Administration's dependence "
        "on digital communication infrastructure operated by non-European entities. "
        "The analysis is based on data collected by the MxMap.it project, "
        "which has mapped the MX (Mail Exchange) records of all institutional "
        "domains registered in the Index of Public Administrations (IndicePA).",
        s_body
    ))
    story.append(Paragraph(
        "The findings highlight a significant exposure of institutional "
        "communications to third-country jurisdictions, with direct implications for: "
        "personal data protection (GDPR, Schrems II), national security (NIS2, National "
        "Cybersecurity Perimeter), strategic autonomy and compliance with AgID "
        "guidelines and with Italy's Cloud Strategy.",
        s_body
    ))

    # Key findings box
    story.append(Spacer(1, 2 * mm))
    story.append(gray_box([
        Paragraph("Key findings", s_box_title),
        Paragraph("•  The Italian PA comprises around 23,000 bodies with institutional email domains", s_bullet_small),
        Paragraph("•  A significant share of these bodies uses email providers subject to non-EU jurisdiction", s_bullet_small),
        Paragraph("•  US providers are subject to the CLOUD Act (18 U.S.C. § 2713, 2018)", s_bullet_small),
        Paragraph("•  Institutional communications regularly contain personal data under art. 4 GDPR", s_bullet_small),
        Paragraph("•  The dependence is cross-cutting: Municipalities, Local Health Authorities, Universities, Ministries", s_bullet_small),
        Paragraph("•  There is currently no obligation to disclose the email provider in the IndicePA catalogue", s_bullet_small),
    ]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Recipients", s_h2))
    dest_data = [
        [Paragraph("Body", s_th), Paragraph("Remit", s_th), Paragraph("Expected action", s_th)],
        [Paragraph("AgID", s_tc_bold),
         Paragraph("Guidelines, cloud qualification, IndicePA", s_tc),
         Paragraph("Update of guidelines and the IndicePA catalogue", s_tc)],
        [Paragraph("ACN", s_tc_bold),
         Paragraph("Cybersecurity, Security Perimeter, NIS2", s_tc),
         Paragraph("Risk assessment, security requirements", s_tc)],
        [Paragraph("Garante Privacy", s_tc_bold),
         Paragraph("Data protection, non-EU transfers", s_tc),
         Paragraph("Compliance checks, measures", s_tc)],
        [Paragraph("ANAC", s_tc_bold),
         Paragraph("Transparency, public procurement", s_tc),
         Paragraph("Sovereignty requirements in public tenders", s_tc)],
    ]
    t = Table(dest_data, colWidths=[25 * mm, 65 * mm, 80 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 2 — Methodology and Technical Framework
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("1. Data collection methodology", s_h1))
    story.append(Paragraph(
        "The methodology adopted is structured in four sequential phases, "
        "each automated and documented to ensure reproducibility and verifiability.",
        s_body
    ))

    story.append(Paragraph("1.1 Acquisition of the list of bodies", s_h2))
    story.append(Paragraph(
        "The list of bodies and their institutional domains is extracted "
        "from IndicePA through the CKAN JSON API. IndicePA, managed by AgID pursuant "
        "to art. 6-ter of the CAD (Legislative Decree 82/2005), is the authoritative "
        "source for identifying all Italian public administrations. The following are "
        "extracted: IPA code (cod_amm), name, email domain, body type and region.",
        s_body
    ))

    story.append(Paragraph("1.2 DNS resolution of MX records", s_h2))
    story.append(Paragraph(
        "For each institutional domain, a DNS query of type MX is performed "
        "(RFC 7208). MX records indicate the servers designated to receive email "
        "for that domain. Resolution is carried out through public "
        "resolvers to ensure results that are not affected by local configurations.",
        s_body
    ))

    story.append(Paragraph("1.3 Provider identification", s_h2))
    story.append(Paragraph(
        "MX records are matched against a database of known patterns to "
        "identify the email provider. The database contains over 200 provider "
        "patterns, maintained and updated in the open source MxMap.it repository. "
        "The classification assigns to each provider:",
        s_body
    ))
    story.append(Paragraph("•  <b>Commercial name</b> of the provider (e.g. Google Workspace, Microsoft 365)", s_bullet))
    story.append(Paragraph("•  <b>Country of registered office</b> of the operator (ISO 3166-1 code)", s_bullet))
    story.append(Paragraph("•  <b>Sovereignty classification</b>: IT (Italian), EU (European), EXTRA_EU (non-European)", s_bullet))

    story.append(Paragraph("1.4 Validation and publication", s_h2))
    story.append(Paragraph(
        "The aggregated data is subjected to automated quality checks "
        "(consistency of IPA codes, validity of domains, completeness of records) "
        "and published in CSV and JSON format under the CC BY-SA 4.0 licence. The entire "
        "process is repeatable and the source code is publicly available.",
        s_body
    ))

    # Data schema
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Dataset schema", s_h2))
    schema_data = [
        [Paragraph("Field", s_th), Paragraph("Type", s_th), Paragraph("Description", s_th), Paragraph("Source", s_th)],
        [Paragraph("cod_amm", s_tc_bold), Paragraph("string", s_tc), Paragraph("IPA code of the body", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("des_amm", s_tc_bold), Paragraph("string", s_tc), Paragraph("Official name", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("dominio", s_tc_bold), Paragraph("string", s_tc), Paragraph("Institutional email domain", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("mx_records", s_tc_bold), Paragraph("string[]", s_tc), Paragraph("Detected MX records", s_tc), Paragraph("DNS query", s_tc)],
        [Paragraph("provider", s_tc_bold), Paragraph("string", s_tc), Paragraph("Identified provider", s_tc), Paragraph("MxMap.it", s_tc)],
        [Paragraph("provider_country", s_tc_bold), Paragraph("ISO 3166", s_tc), Paragraph("Provider's registered office", s_tc), Paragraph("MxMap.it", s_tc)],
        [Paragraph("sovereignty", s_tc_bold), Paragraph("enum", s_tc), Paragraph("IT / EU / EXTRA_EU", s_tc), Paragraph("MxMap.it", s_tc)],
    ]
    t = Table(schema_data, colWidths=[30 * mm, 20 * mm, 75 * mm, 25 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 3 — Detailed Regulatory Framework
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("2. Applicable regulatory framework", s_h1))
    story.append(Paragraph(
        "Dependence on non-EU providers for institutional communications "
        "intersects with multiple regulatory dimensions, each with specific "
        "implications for bodies and regulators.",
        s_body
    ))

    # 2.1 GDPR
    story.append(Paragraph("2.1 General Data Protection Regulation (GDPR)", s_h2))
    story.append(Paragraph(
        "The GDPR (EU Reg. 2016/679) governs the processing and transfer "
        "of personal data. Institutional email constitutes "
        "processing of personal data within the meaning of art. 4, since "
        "communications regularly contain: names, addresses, tax codes, "
        "health data, judicial information and other sensitive data.",
        s_body
    ))
    story.append(Paragraph(
        "Chapter V of the GDPR (arts. 44-49) makes transfers to third "
        "countries subject to specific safeguards. The use of a provider subject to the CLOUD "
        "Act constitutes a potential non-EU transfer regardless of the physical "
        "location of the servers, since the US judicial authority "
        "can compel the disclosure of data by the provider.",
        s_body
    ))

    # Schrems box
    story.append(Spacer(1, 1 * mm))
    story.append(colored_box([
        Paragraph("Schrems I and II rulings — Implications", s_box_title),
        Paragraph(
            "<b>Schrems I</b> (C-362/14, 2015): The CJEU invalidated Safe Harbor "
            "for insufficient safeguards against US mass surveillance.",
            s_box_body
        ),
        Paragraph(
            "<b>Schrems II</b> (C-311/18, 2020): The CJEU invalidated the Privacy Shield "
            "and required a case-by-case assessment of standard contractual clauses (SCCs). "
            "SCCs are insufficient where the law of the third country imposes disclosure "
            "obligations incompatible with European safeguards.",
            s_box_body
        ),
        Paragraph(
            "<b>Data Privacy Framework</b> (2023): EC adequacy decision for the USA, "
            "but applicable only to DPF self-certified organisations. It does not resolve the "
            "structural CLOUD Act / GDPR conflict and could be invalidated (\"Schrems III\").",
            s_box_body
        ),
    ], AMBER_LIGHT, AMBER_BORDER))

    # 2.2 CLOUD Act
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2.2 CLOUD Act (Clarifying Lawful Overseas Use of Data Act)", s_h2))
    story.append(Paragraph(
        "The CLOUD Act (18 U.S.C. § 2713, 2018) allows US judicial "
        "authorities to require any provider subject to US jurisdiction "
        "to produce data in its possession, custody or control, "
        "<b>regardless of the physical location of the data</b>.",
        s_body
    ))
    story.append(Paragraph(
        "This means that a PA body using Google Workspace or Microsoft 365 "
        "for email exposes its institutional communications to "
        "potential disclosure to US authorities, even if the servers are physically "
        "located in Europe (the cloud providers' EU regions).",
        s_body
    ))

    # Risk box
    story.append(colored_box([
        Paragraph("Structural legal conflict", s_box_title),
        Paragraph(
            "The CLOUD Act creates a direct conflict with the GDPR: the provider is "
            "required to produce the data by US law, but is prohibited from doing so "
            "by EU law. This conflict cannot be resolved through contractual "
            "or technical measures, since the CLOUD Act's disclosure obligation "
            "prevails over the provider's contractual agreements.",
            s_box_body
        ),
    ], RED_LIGHT, RED_BORDER))

    # Microsoft admission quote box
    s_quote_eyebrow = ParagraphStyle(
        "QuoteEyebrow", fontName="Arial-Bold", fontSize=8.5, textColor=RED_BORDER,
        spaceAfter=4, leading=11, letterSpacing=1.5
    )
    s_quote_big = ParagraphStyle(
        "QuoteBig", fontName="Arial-BoldItalic", fontSize=15, textColor=DARK,
        spaceAfter=5, leading=19
    )
    s_quote_context = ParagraphStyle(
        "QuoteContext", fontName="Arial", fontSize=8.5, textColor=DARK,
        spaceAfter=4, leading=11.5, alignment=TA_JUSTIFY
    )
    s_quote_attr = ParagraphStyle(
        "QuoteAttr", fontName="Arial-Italic", fontSize=7.5, textColor=GRAY_TEXT,
        spaceAfter=0, leading=10
    )
    story.append(Spacer(1, 3 * mm))
    story.append(colored_box([
        Paragraph("MICROSOFT'S OWN ADMISSION", s_quote_eyebrow),
        Paragraph("“No, I cannot guarantee it.”", s_quote_big),
        Paragraph(
            "Microsoft France's Director of Public and Legal Affairs, asked at a "
            "hearing whether he could guarantee that European citizens' data would "
            "never be transferred to the US government under a CLOUD Act order "
            "— without the national authorities' agreement. Microsoft itself "
            "admits it cannot rule out the transfer of European data to US authorities.",
            s_quote_context
        ),
        Paragraph(
            "Anton Carniaux, Director of Public and Legal Affairs, Microsoft France "
            "— hearing before the French Senate committee of inquiry, "
            "10 June 2025. Sources: French Senate (senat.fr) · heise.de",
            s_quote_attr
        ),
    ], GRAY_BG, RED_BORDER))

    # 2.3 Italy's Cloud Strategy and ACN
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2.3 Italy's Cloud Strategy and ACN qualification", s_h2))
    story.append(Paragraph(
        "Italy's Cloud Strategy (2021) classifies PA data into three levels: "
        "ordinary, critical and strategic. For critical and strategic data, "
        "migration to the National Strategic Hub (PSN) or to infrastructure "
        "qualified by ACN (National Cybersecurity Agency) is required.",
        s_body
    ))
    story.append(Paragraph(
        "The ACN Regulation for the qualification of cloud services for the PA "
        "(Determination no. 307/2022 and subsequent amendments) defines specific "
        "requirements for data localisation and jurisdictional control. "
        "Services qualified at level QC3 (strategic) and QC2 (critical) must "
        "ensure that data is not accessible from non-EU jurisdictions.",
        s_body
    ))

    # 2.4 NIS2
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("2.4 NIS2 Directive and Legislative Decree 138/2024", s_h2))
    story.append(Paragraph(
        "The NIS2 Directive (2022/2555), transposed by Legislative Decree 138/2024, imposes "
        "on the PA obligations to manage cybersecurity risk, including the "
        "assessment of supply chain risks. Dependence on non-EU email "
        "providers constitutes a supply chain risk that must be "
        "assessed and managed within the security measures required by art. 21.",
        s_body
    ))

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 4 — Risk Analysis
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("3. Risk analysis", s_h1))
    story.append(Paragraph(
        "Dependence on non-EU providers generates risks across four interconnected "
        "dimensions, each relevant to different regulatory profiles.",
        s_body
    ))

    # Risk matrix
    risk_data = [
        [Paragraph("Dimension", s_th), Paragraph("Risk", s_th),
         Paragraph("Impact", s_th), Paragraph("Regulator", s_th)],
        [Paragraph("Jurisdictional", s_tc_bold),
         Paragraph("Access to PA data by non-EU authorities "
                    "through the CLOUD Act or equivalent legislation", s_tc),
         Paragraph("HIGH", ParagraphStyle("R", parent=s_tc_bold, textColor=RED_BORDER)),
         Paragraph("Garante, ACN", s_tc)],
        [Paragraph("Data protection", s_tc_bold),
         Paragraph("Non-compliance with GDPR requirements for non-EU "
                    "transfers (Chapter V); potential breach of Schrems II", s_tc),
         Paragraph("HIGH", ParagraphStyle("R2", parent=s_tc_bold, textColor=RED_BORDER)),
         Paragraph("Garante", s_tc)],
        [Paragraph("Operational continuity", s_tc_bold),
         Paragraph("Service interruption due to unilateral decisions "
                    "by the provider, sanctions, geopolitical conflicts", s_tc),
         Paragraph("MEDIUM", ParagraphStyle("A", parent=s_tc_bold, textColor=AMBER_BORDER)),
         Paragraph("AgID, ACN", s_tc)],
        [Paragraph("Strategic", s_tc_bold),
         Paragraph("Technology lock-in, loss of national skills, "
                    "structural dependence on proprietary ecosystems", s_tc),
         Paragraph("MEDIUM", ParagraphStyle("A2", parent=s_tc_bold, textColor=AMBER_BORDER)),
         Paragraph("AgID, ANAC", s_tc)],
        [Paragraph("Economic", s_tc_bold),
         Paragraph("Financial flows towards foreign operators, failure "
                    "to develop the national and European IT industry", s_tc),
         Paragraph("MEDIUM", ParagraphStyle("A3", parent=s_tc_bold, textColor=AMBER_BORDER)),
         Paragraph("ANAC, Consip", s_tc)],
    ]
    t = Table(risk_data, colWidths=[28 * mm, 72 * mm, 18 * mm, 28 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # Scenario analysis
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("3.1 Scenario: CLOUD Act request", s_h2))
    story.append(Paragraph(
        "Consider the scenario in which a US judicial authority issues a "
        "production order (warrant or subpoena) to a provider that manages "
        "the email of Italian PA bodies:",
        s_body
    ))
    story.append(Paragraph("1.  The provider is legally required to produce the data (18 U.S.C. § 2713)", s_bullet))
    story.append(Paragraph("2.  The provider can challenge the order only if it breaches an international treaty — "
                           "currently there is no EU-US executive agreement", s_bullet))
    story.append(Paragraph("3.  The PA body is not necessarily informed of the disclosure", s_bullet))
    story.append(Paragraph("4.  The data may include: internal communications, citizens' data, "
                           "sensitive information, administrative acts", s_bullet))
    story.append(Paragraph("5.  The disclosure potentially breaches arts. 44-49 GDPR and constitutes a "
                           "data breach within the meaning of art. 33", s_bullet))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("3.2 Risk by type of body", s_h2))
    story.append(Paragraph(
        "The impact of the dependence varies by type of body depending "
        "on the sensitivity of the data processed:",
        s_body
    ))

    tipo_data = [
        [Paragraph("Type", s_th), Paragraph("Typical sensitive data", s_th),
         Paragraph("Risk", s_th)],
        [Paragraph("Local Health Authorities / Hospitals", s_tc_bold),
         Paragraph("Health data, medical reports, doctor-patient communications", s_tc),
         Paragraph("CRITICAL", ParagraphStyle("C", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Municipalities", s_tc_bold),
         Paragraph("Population registry, civil status, social services, taxes", s_tc),
         Paragraph("HIGH", ParagraphStyle("A4", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Law enforcement", s_tc_bold),
         Paragraph("Investigations, reports, judicial data", s_tc),
         Paragraph("CRITICAL", ParagraphStyle("C2", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Universities", s_tc_bold),
         Paragraph("Student data, research, intellectual property", s_tc),
         Paragraph("MEDIUM", ParagraphStyle("M", parent=s_tc_bold, textColor=AMBER_BORDER))],
        [Paragraph("Ministries", s_tc_bold),
         Paragraph("Policy, inter-institutional communications, classified data", s_tc),
         Paragraph("CRITICAL", ParagraphStyle("C3", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Independent authorities", s_tc_bold),
         Paragraph("Reports, proceedings, confidential data", s_tc),
         Paragraph("CRITICAL", ParagraphStyle("C4", parent=s_tc_bold, textColor=RED_BORDER))],
    ]
    t = Table(tipo_data, colWidths=[40 * mm, 90 * mm, 25 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 5 — Recommendations for Regulators
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("4. Recommendations for regulators", s_h1))

    # AgID
    story.append(Paragraph("4.1 Recommendations for AgID", s_h2))
    story.append(colored_box([
        Paragraph("R1 — Extend IndicePA with email provider information", s_box_title),
        Paragraph(
            "Add to IndicePA a mandatory field for the email provider "
            "and its sovereignty classification. This would enable "
            "continuous institutional monitoring and would make the information public "
            "and accessible to all stakeholders.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R2 — Update the guidelines on email services", s_box_title),
        Paragraph(
            "Update the Guidelines on the creation, management and preservation "
            "of electronic documents to include explicit jurisdictional sovereignty "
            "requirements for institutional email services. "
            "Provide a transition period proportionate to the size of the body.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R3 — Define qualification criteria for PA email services", s_box_title),
        Paragraph(
            "By analogy with cloud qualification, define specific criteria for "
            "the PA's email services, including: provider jurisdiction, "
            "data localisation, absence of disclosure obligations towards non-EU "
            "authorities, certified GDPR compliance.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ACN
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("4.2 Recommendations for ACN", s_h2))
    story.append(colored_box([
        Paragraph("R4 — Include email dependence in the NIS2 risk assessment", s_box_title),
        Paragraph(
            "In the guidelines for the implementation of NIS2, explicitly include "
            "dependence on non-EU email providers as a risk factor in the "
            "supply chain assessment. Require essential and important entities "
            "to declare the email provider used.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R5 — Extend the National Cybersecurity Perimeter", s_box_title),
        Paragraph(
            "Assess the inclusion of the email services of Perimeter bodies "
            "among the ICT assets subject to notification and reinforced "
            "security measures, with particular attention to the provider's jurisdiction.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # Garante
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("4.3 Recommendations for the Garante Privacy", s_h2))
    story.append(colored_box([
        Paragraph("R6 — General measure on the use of non-EU email services in the PA", s_box_title),
        Paragraph(
            "Adopt a general measure, similar to the one on cookies (no. 231/2021) "
            "or on Google Analytics (no. 224/2022), clarifying the conditions of lawfulness "
            "for the use of email services managed by providers subject to the CLOUD "
            "Act for the PA's institutional communications.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R7 — Mandatory DPIA for PA email services with non-EU providers", s_box_title),
        Paragraph(
            "Require a mandatory Data Protection Impact Assessment (DPIA, art. 35 GDPR) "
            "for PA bodies that use email services managed by providers subject "
            "to non-EU jurisdictions, including an assessment of the risk of "
            "disclosure under the CLOUD Act.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 6 — Roadmap and References
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("5. Proposed roadmap", s_h1))
    story.append(Paragraph(
        "A gradual adjustment path is proposed, structured in three phases, "
        "taking account of the different sizes and capacities of bodies.",
        s_body
    ))

    road_data = [
        [Paragraph("Phase", s_th), Paragraph("Horizon", s_th),
         Paragraph("Action", s_th), Paragraph("Responsible", s_th)],
        [Paragraph("1. Transparency", s_tc_bold),
         Paragraph("0-6 months", s_tc),
         Paragraph("Mandatory census of email providers in IndicePA; "
                    "publication of a public dashboard", s_tc),
         Paragraph("AgID", s_tc)],
        [Paragraph("2. Regulation", s_tc_bold),
         Paragraph("6-18 months", s_tc),
         Paragraph("Update of guidelines; Garante measure; "
                    "NIS2 criteria; email qualification", s_tc),
         Paragraph("AgID, ACN, Garante", s_tc)],
        [Paragraph("3. Migration", s_tc_bold),
         Paragraph("18-36 months", s_tc),
         Paragraph("National migration plan with dedicated funding; "
                    "priority for bodies with critical/strategic data", s_tc),
         Paragraph("PCM, AgID, ACN", s_tc)],
    ]
    t = Table(road_data, colWidths=[28 * mm, 22 * mm, 80 * mm, 32 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DEE2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)

    # Migration priority
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("5.1 Priority criteria for migration", s_h2))
    story.append(Paragraph(
        "Migration should be prioritised according to the sensitivity "
        "of the data processed and the body's risk profile:",
        s_body
    ))
    story.append(Paragraph("•  <b>Priority 1 (immediate):</b> National Security Perimeter bodies, "
                           "Law enforcement, Intelligence services, Ministries", s_bullet))
    story.append(Paragraph("•  <b>Priority 2 (within 12 months):</b> Local Health Authorities/Hospitals, Independent authorities, "
                           "Regions, Large Municipalities", s_bullet))
    story.append(Paragraph("•  <b>Priority 3 (within 24 months):</b> Universities, Research bodies, "
                           "Provinces, Medium-sized Municipalities", s_bullet))
    story.append(Paragraph("•  <b>Priority 4 (within 36 months):</b> Small Municipalities, ancillary bodies, "
                           "other PA", s_bullet))

    # Conclusions
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("6. Conclusions", s_h1))
    story.append(Paragraph(
        "The analysis of MxMap.it data highlights a structural dependence of the Italian "
        "PA on email providers subject to non-European jurisdictions. This "
        "dependence is not a theoretical problem: the CLOUD Act creates a concrete "
        "legal conflict with the GDPR, the Schrems rulings and Italy's Cloud Strategy.",
        s_body
    ))
    story.append(Paragraph(
        "The solution requires a coordinated approach between AgID, ACN and the Garante Privacy, "
        "with concrete actions on three fronts: transparency (making the problem visible), "
        "regulation (defining clear requirements) and migration (supporting bodies "
        "along the adjustment path).",
        s_body
    ))
    story.append(Paragraph(
        "The National Digital Sovereignty Observatory provides open data, "
        "documented methodology and replicable tools to support this path. "
        "Civic monitoring is at the service of institutions and citizens.",
        s_body
    ))

    # References
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph("Regulatory references and sources", s_h2))
    refs = [
        "GDPR — Regulation (EU) 2016/679 of the European Parliament and of the Council",
        "CLOUD Act — Clarifying Lawful Overseas Use of Data Act (18 U.S.C. § 2713, 2018)",
        "Schrems I — CJEU, C-362/14 (6 October 2015)",
        "Schrems II — CJEU, C-311/18 (16 July 2020)",
        "Data Privacy Framework — EC adequacy decision (10 July 2023)",
        "NIS2 Directive — Directive (EU) 2022/2555; Legislative Decree 138/2024",
        "Italy's Cloud Strategy — Department for Digital Transformation (2021)",
        "CAD — Legislative Decree 82/2005, art. 6-ter (IndicePA)",
        "ACN Regulation — Determination no. 307/2022 (PA cloud qualification)",
        "National Cybersecurity Perimeter — Decree-Law 105/2019, converted into Law 133/2019",
        "MxMap.it — https://mxmap.it/",
        "IndicePA — https://indicepa.gov.it",
        "National Digital Sovereignty Observatory — "
        "https://osservatorio.mxmap.it/",
    ]
    for ref in refs:
        story.append(Paragraph(f"•  {ref}", s_ref))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=HexColor("#DEE2E6"),
        spaceAfter=3, spaceBefore=2
    ))
    story.append(Paragraph(
        "This document is released under the CC BY-SA 4.0 licence. "
        "Contact: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale",
        s_small
    ))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
