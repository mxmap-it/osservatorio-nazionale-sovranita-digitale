"""Generate Slide Deck PDF (landscape, 16:9-ish) — National Digital Sovereignty Observatory (EN)"""
import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as canvas_mod

OUTPUT = os.path.join(os.path.dirname(__file__), "Slide_Deck_Osservatorio_Sovranita_Digitale_EN.pdf")

BLUE = HexColor("#0066B2")
DARK_BLUE = HexColor("#042C53")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
GREEN = HexColor("#1D9E75")
AMBER = HexColor("#BA7517")
RED = HexColor("#A32D2D")

PAGE = landscape(A4)
W, H = PAGE
ML = 28 * mm


def _wrap(c, text, font, size, max_w):
    c.setFont(font, size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def footer(c, n, total):
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(GRAY_TEXT)
    c.drawString(ML, 12 * mm, "National Digital Sovereignty Observatory")
    c.drawRightString(W - ML, 12 * mm, f"{n} / {total}")


def bullets(c, items, x, y, max_w, gap=11 * mm, size=14, color=DARK, marker_color=BLUE):
    for it in items:
        c.setFillColor(marker_color)
        c.setFont("Helvetica-Bold", size)
        c.drawString(x, y, "•")
        c.setFillColor(color)
        lines = _wrap(c, it, "Helvetica", size, max_w - 8 * mm)
        ty = y
        for ln in lines:
            c.setFont("Helvetica", size)
            c.drawString(x + 7 * mm, ty, ln)
            ty -= size + 4
        y = ty - (gap - (size + 4))
    return y


def title_slide(c, kicker, title, subtitle, n, total):
    c.setFillColor(DARK_BLUE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(HexColor("#7FB2E0"))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(ML, H - 55 * mm, kicker.upper())
    c.setFillColor(WHITE)
    y = H - 75 * mm
    for ln in _wrap(c, title, "Helvetica-Bold", 34, W - 2 * ML):
        c.drawString(ML, y, ln)
        y -= 40
    c.setFillColor(HexColor("#C9DEF2"))
    y -= 6
    for ln in _wrap(c, subtitle, "Helvetica", 15, W - 2 * ML):
        c.drawString(ML, y, ln)
        y -= 21
    c.setFillColor(HexColor("#7FB2E0"))
    c.setFont("Helvetica-Oblique", 9)
    c.drawRightString(W - ML, 12 * mm, f"{n} / {total}")


def content_slide(c, title, n, total, draw_body):
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(0, H - 4 * mm, W, 4 * mm, fill=1, stroke=0)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 24)
    tlines = _wrap(c, title, "Helvetica-Bold", 24, W - 2 * ML)
    ty = H - 26 * mm
    for ln in tlines:
        c.drawString(ML, ty, ln)
        ty -= 28
    c.setStrokeColor(BLUE)
    c.setLineWidth(1)
    c.line(ML, ty + 6, ML + 40 * mm, ty + 6)
    draw_body(c, ty - 8 * mm)
    footer(c, n, total)


def section_slide(c, title, n, total):
    c.setFillColor(GRAY_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(0, H / 2 - 1, 18 * mm, 2, fill=1, stroke=0)
    c.setFillColor(DARK_BLUE)
    y = H / 2 + 18
    for ln in _wrap(c, title, "Helvetica-Bold", 30, W - 2 * ML):
        c.drawString(ML, y, ln)
        y -= 36
    footer(c, n, total)


def kpi_slide(c, title, cards, n, total):
    def body(c, y0):
        n_cards = len(cards)
        gap = 8 * mm
        cw = (W - 2 * ML - (n_cards - 1) * gap) / n_cards
        cy = y0 - 40 * mm
        ch = 46 * mm
        for i, (num, lbl) in enumerate(cards):
            cx = ML + i * (cw + gap)
            c.setFillColor(GRAY_BG)
            c.roundRect(cx, cy, cw, ch, 4 * mm, fill=1, stroke=0)
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 40)
            c.drawCentredString(cx + cw / 2, cy + ch - 26 * mm, num)
            c.setFillColor(GRAY_TEXT)
            for j, ln in enumerate(_wrap(c, lbl, "Helvetica", 11, cw - 8 * mm)):
                c.drawCentredString(cx + cw / 2, cy + ch - 33 * mm - j * 13, ln)
        c.setFillColor(GRAY_TEXT)
        c.setFont("Helvetica-Oblique", 9)
        c.drawString(ML, cy - 8 * mm, "Values being updated — source: MxMap.it on IndicePA")
    content_slide(c, title, n, total, body)


def build():
    c = canvas_mod.Canvas(OUTPUT, pagesize=PAGE)
    TOTAL = 16
    n = 0

    # 1 — Title
    n += 1
    title_slide(c, "National Observatory",
                "Digital Sovereignty in the Italian Public Administration",
                "Measuring, raising awareness, driving change — June 2025",
                n, TOTAL)
    c.showPage()

    # 2 — What it is
    n += 1
    content_slide(c, "What the Observatory is", n, TOTAL, lambda c, y: bullets(c, [
        "Independent civic monitoring project on digital sovereignty in the Italian Public Administration",
        "Measures the dependence of public bodies on foreign digital infrastructure",
        "Starts with email: the most widespread and most sensitive communication channel",
        "Open data, replicable methodology, open source code (CC BY-SA 4.0)",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 3 — The problem (section)
    n += 1
    section_slide(c, "The problem: jurisdictional dependence", n, TOTAL)
    c.showPage()

    # 4 — The problem in detail
    n += 1
    content_slide(c, "Why it is a problem", n, TOTAL, lambda c, y: bullets(c, [
        "Institutional emails contain citizens' personal data (art. 4 GDPR)",
        "Many bodies use providers subject to non-EU jurisdiction",
        "The US CLOUD Act allows access to data even if the servers are in Europe",
        "Structural conflict with the GDPR and the Schrems I and II rulings",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 5 — KPI
    n += 1
    kpi_slide(c, "The numbers (being updated)", [
        ("~23,000", "PA bodies monitored"),
        ("—%", "on non-EU providers"),
        ("—%", "on Italian providers"),
        ("—%", "on EU providers"),
    ], n, TOTAL)
    c.showPage()

    # 6 — Methodology (section)
    n += 1
    section_slide(c, "How we measure it", n, TOTAL)
    c.showPage()

    # 7 — Methodology steps
    n += 1
    content_slide(c, "The methodology in 4 steps", n, TOTAL, lambda c, y: bullets(c, [
        "1. Extraction of bodies and domains from IndicePA (CKAN JSON API)",
        "2. Resolution of MX (Mail Exchange) records via DNS",
        "3. Identification of the provider and its jurisdiction",
        "4. Sovereignty classification: Italian / EU / Non-EU",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 8 — Risks (section)
    n += 1
    section_slide(c, "The risks", n, TOTAL)
    c.showPage()

    # 9 — Risks in detail
    n += 1
    content_slide(c, "Four dimensions of risk", n, TOTAL, lambda c, y: bullets(c, [
        "Jurisdictional — access to data by non-EU authorities",
        "Data protection — GDPR non-compliance on transfers",
        "Operational continuity — dependence on unilateral foreign decisions",
        "Strategic and economic — lock-in and lack of development of the EU industry",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 10 — Who it is for (section)
    n += 1
    section_slide(c, "Who the Observatory is for", n, TOTAL)
    c.showPage()

    # 11 — Stakeholders
    n += 1
    content_slide(c, "Civic monitoring at everyone's service", n, TOTAL, lambda c, y: bullets(c, [
        "Policymakers — data for parliamentary questions and legislative proposals",
        "Regulators (AgID, ACN, Garante) — basis for guidelines and measures",
        "PA executives — benchmarking and support for migration choices",
        "Journalists, researchers, citizens — transparency and awareness",
        "IT providers and Consip — market and procurement opportunities",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 12 — What we propose (section)
    n += 1
    section_slide(c, "What we propose", n, TOTAL)
    c.showPage()

    # 13 — Recommendations
    n += 1
    content_slide(c, "Five recommendations", n, TOTAL, lambda c, y: bullets(c, [
        "Mandatory census of providers in the PA (transparency)",
        "Sovereignty requirements in Consip framework agreements",
        "National migration plan with dedicated funding",
        "Continuous and public monitoring over time",
        "Promotion of the model at European level",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 14 — Documents
    n += 1
    content_slide(c, "The Observatory's documents", n, TOTAL, lambda c, y: bullets(c, [
        "Policy Brief — for policymakers (2 pages)",
        "Technical Brief — for AgID, ACN, Garante (6 pages)",
        "Business Case — for IT providers and Consip",
        "EU Briefing — for the European institutions (English)",
        "All downloadable from the site, under CC BY-SA 4.0 licence",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 15 — Roadmap
    n += 1
    content_slide(c, "Next steps", n, TOTAL, lambda c, y: bullets(c, [
        "Publication of the report with updated data",
        "Presentation of the findings to the Chamber of Deputies",
        "Integration of live KPIs from MxMap.it, updated daily",
        "Extension of monitoring to other digital PA services",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 16 — Closing
    n += 1
    title_slide(c, "Get Involved",
                "Change starts with awareness",
                "osservatorio-nazionale-sovranita-digitale  •  mxmap.it  •  Telegram",
                n, TOTAL)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
