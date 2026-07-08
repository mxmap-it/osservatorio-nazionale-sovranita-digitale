"""Generate the Report PDF (DRAFT) — concise snapshot from data/kpi.json.
Equivalent to mxmap.it/report.html: summary, sovereignty (donut), providers, sectors.
'DRAFT' is drawn on every page."""
import os, json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.piecharts import Pie
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(__file__)
KPI = os.path.join(HERE, "..", "data", "kpi.json")
OUTPUT = os.path.join(HERE, "Report_Sovranita_Digitale_PA_EN.pdf")

BLUE = HexColor("#0066CC")
INK = HexColor("#17324D")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
AMBER = HexColor("#E8A33D")
RED = HexColor("#D9364F")
GREEN = HexColor("#1D9E75")
GRAY = HexColor("#9AA6B2")

SOV = {"extra_eu": RED, "it": BLUE, "eu_non_it": GREEN, "unknown": GRAY}

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))

s_label = ParagraphStyle("L", fontName="Arial-Bold", fontSize=10, textColor=BLUE, leading=12, letterSpacing=2, spaceAfter=2)
s_title = ParagraphStyle("T", fontName="Arial-Bold", fontSize=18, textColor=INK, leading=22, spaceAfter=2)
s_sub = ParagraphStyle("S", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT, leading=12, spaceAfter=6)
s_h2 = ParagraphStyle("H2", fontName="Arial-Bold", fontSize=12, textColor=BLUE, leading=15, spaceBefore=10, spaceAfter=5)
s_body = ParagraphStyle("B", fontName="Arial", fontSize=9.5, textColor=DARK, leading=13, alignment=TA_JUSTIFY, spaceAfter=5)
s_small = ParagraphStyle("Sm", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT, leading=10, spaceAfter=3)
s_leg = ParagraphStyle("Leg", fontName="Arial", fontSize=9, textColor=DARK, leading=14)
s_leg_b = ParagraphStyle("LegB", fontName="Arial-Bold", fontSize=9, textColor=DARK, leading=14)
s_bar_l = ParagraphStyle("BarL", fontName="Arial", fontSize=8.5, textColor=DARK, leading=10)
s_bar_lb = ParagraphStyle("BarLB", fontName="Arial-Bold", fontSize=8.5, textColor=DARK, leading=10)
s_q_eyebrow = ParagraphStyle("QE", fontName="Arial-Bold", fontSize=8.5, textColor=RED, leading=11, spaceAfter=4)
s_q_big = ParagraphStyle("QB", fontName="Arial-Italic", fontSize=15, textColor=INK, leading=19, spaceAfter=5)
s_q_ctx = ParagraphStyle("QC", fontName="Arial", fontSize=9, textColor=DARK, leading=12.5, alignment=TA_JUSTIFY, spaceAfter=5)
s_q_attr = ParagraphStyle("QA", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT, leading=10)


def quote_box(eyebrow, quote, context, attribution):
    """Highlighted-evidence callout: solid tint background + coloured left border,
    so it stays legible over the diagonal watermark."""
    inner = [
        Paragraph(eyebrow, s_q_eyebrow),
        Paragraph(quote, s_q_big),
        Paragraph(context, s_q_ctx),
        Paragraph(attribution, s_q_attr),
    ]
    t = Table([[inner]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 3, RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 8 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 5 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5 * mm),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def load():
    with open(KPI, encoding="utf-8") as f:
        return json.load(f)


def fmt(n):
    s = f"{int(n):,}"
    return s


def page_deco(canvas, doc):
    canvas.saveState()
    # diagonal DRAFT watermark
    canvas.setFont("Arial-Bold", 100)
    canvas.setFillColor(AMBER)
    try:
        canvas.setFillAlpha(0.10)
    except Exception:
        pass
    canvas.translate(A4[0] / 2, A4[1] / 2)
    canvas.rotate(45)
    canvas.drawCentredString(0, -20, "DRAFT")
    canvas.restoreState()
    # top-right DRAFT badge
    canvas.saveState()
    bw, bh = 26 * mm, 8 * mm
    bx, by = A4[0] - 20 * mm - bw, A4[1] - 16 * mm
    canvas.setFillColor(AMBER)
    canvas.roundRect(bx, by, bw, bh, 2 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Arial-Bold", 11)
    canvas.drawCentredString(bx + bw / 2, by + 2.3 * mm, "DRAFT")
    # footer
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawString(20 * mm, 10 * mm, "draft — preliminary data, not for distribution")
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "National Digital Sovereignty Observatory — CC BY-SA 4.0")
    canvas.drawRightString(A4[0] - 20 * mm, 10 * mm, f"p. {doc.page}")
    canvas.restoreState()


def donut(sov):
    order = ["extra_eu", "it", "eu_non_it", "unknown"]
    vals, cols = [], []
    for k in order:
        v = sov.get(k, {}).get("pct", 0) or 0
        if v > 0:
            vals.append(v)
            cols.append(SOV[k])
    d = Drawing(150, 150)
    pie = Pie()
    pie.x = 25; pie.y = 15; pie.width = 110; pie.height = 110
    pie.data = vals
    pie.labels = [""] * len(vals)
    pie.simpleLabels = 1
    pie.slices.strokeColor = WHITE
    pie.slices.strokeWidth = 1.5
    for i, c in enumerate(cols):
        pie.slices[i].fillColor = c
        pie.slices[i].labelRadius = 0  # hide labels (legend instead)
    pie.sideLabels = 0
    d.add(pie)
    d.add(Circle(80, 70, 30, fillColor=WHITE, strokeColor=WHITE))  # donut hole
    return d


def sov_legend(sov):
    order = ["extra_eu", "it", "eu_non_it", "unknown"]
    rows = []
    for k in order:
        s = sov.get(k, {})
        sw = Table([[""]], colWidths=[5 * mm], rowHeights=[5 * mm])
        sw.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), SOV[k]),
                                ("ROUNDEDCORNERS", [2, 2, 2, 2])]))
        lbl = Paragraph(f"<b>{s.get('label','')}</b>", s_leg)
        val = Paragraph(f"{s.get('pct',0):.1f}% &nbsp;<font color='#6C757D'>({fmt(s.get('count',0))})</font>", s_leg)
        rows.append([sw, lbl, val])
    t = Table(rows, colWidths=[7 * mm, 58 * mm, 33 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


def bar_rows(items, label_w=70 * mm, max_pct=100.0, color_fn=None):
    """items: list of (label, sublabel, pct, color). Returns a flowable Table of bars."""
    rows = []
    for label, sub, pct, color in items:
        head = Table([[Paragraph(f"<b>{label}</b> <font size=7 color='#6C757D'>{sub}</font>", s_bar_l),
                       Paragraph(f"<b>{pct:.1f}%</b>", ParagraphStyle('r', parent=s_bar_lb, alignment=2))]],
                     colWidths=[label_w - 22 * mm, 22 * mm])
        head.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        full = label_w
        fillw = max(0.4 * mm, full * (pct / max_pct))
        bar = Table([[""]], colWidths=[fillw], rowHeights=[3.2 * mm])
        bar.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color), ("ROUNDEDCORNERS", [2, 2, 2, 2])]))
        track = Table([[bar]], colWidths=[full])
        track.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), HexColor("#E9ECEF")),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                   ("ROUNDEDCORNERS", [2, 2, 2, 2])]))
        rows.append([head])
        rows.append([track])
        rows.append([Spacer(1, 2.5 * mm)])
    t = Table(rows, colWidths=[label_w])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t


def build():
    k = load()
    tot = k.get("totals", {})
    sov = k.get("sovereignty", {})
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=20 * mm, bottomMargin=20 * mm)
    story = []

    story.append(Paragraph("REPORT", s_label))
    story.append(Paragraph("State of Digital Sovereignty<br/>in the Italian PA", s_title))
    story.append(Paragraph("June 2026 — National Digital Sovereignty Observatory · MxMap.it data on IndicePA", s_sub))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    # Summary
    story.append(Paragraph("In summary", s_h2))
    ee = sov.get("extra_eu", {}).get("pct", 0)
    it = sov.get("it", {}).get("pct", 0)
    eu = sov.get("eu_non_it", {}).get("pct", 0)
    story.append(Paragraph(
        f"We analysed <b>{fmt(tot.get('n_entities',0))}</b> bodies of the Italian Public "
        f"Administration registered in IndicePA. For each one we identified the email "
        f"provider and the <b>jurisdiction</b> to which it is subject. <b><font color='#D9364F'>{ee:.1f}%</font></b> "
        f"of bodies rely on providers subject to <b>non-EU</b> jurisdiction (e.g. the CLOUD Act), against "
        f"<b><font color='#0066CC'>{it:.1f}%</font></b> on Italian providers"
        + (f" and {eu:.1f}% on other EU providers" if eu else "") + ".", s_body))

    # Quote box — Microsoft's own admission
    story.append(Spacer(1, 3 * mm))
    story.append(quote_box(
        "MICROSOFT&#39;S OWN ADMISSION",
        "&ldquo;No, I cannot guarantee it.&rdquo;",
        "Microsoft France&#39;s Director of Public and Legal Affairs, asked at a hearing "
        "whether he could guarantee that European citizens&#39; data would never be "
        "transferred to the US government under a CLOUD Act order &mdash; without the "
        "national authorities&#39; agreement. Microsoft itself admits it cannot rule out "
        "the transfer of European data to US authorities.",
        "Anton Carniaux, Director of Public and Legal Affairs, Microsoft France &mdash; "
        "hearing before the French Senate committee of inquiry, 10 June 2025. "
        "Sources: French Senate (senat.fr) &middot; heise.de"))
    story.append(Spacer(1, 3 * mm))

    # Sovereignty — donut + legend
    story.append(Paragraph("The snapshot: provider sovereignty", s_h2))
    combo = Table([[donut(sov), sov_legend(sov)]], colWidths=[55 * mm, 105 * mm])
    combo.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story.append(combo)

    # Providers
    tps = k.get("top_providers", [])[:6]
    if tps:
        story.append(Paragraph("Most widespread providers", s_h2))
        items = [(p["name"], f"· {fmt(p['count'])} bodies", p.get("pct", 0), SOV.get(p.get("sovereignty"), GRAY)) for p in tps]
        story.append(bar_rows(items, label_w=170 * mm))

    # Sectors
    bc = sorted(k.get("by_cluster", []), key=lambda x: x.get("usa_pct", 0), reverse=True)[:8]
    if bc:
        story.append(PageBreak())
        story.append(Paragraph("By body category", s_h2))
        story.append(Paragraph("Share of bodies on <b>non-EU</b> providers, by category (top 8 by dependency).", s_small))
        items = [(c["cluster"], f"· {fmt(c['n_entities'])} bodies · {c.get('dominant_provider','')}", c.get("usa_pct", 0), RED) for c in bc]
        story.append(bar_rows(items, label_w=170 * mm))

    # Methodology + note
    story.append(Paragraph("Methodology and notes", s_h2))
    story.append(Paragraph(
        "The data derive from the analysis of the DNS records of PA domains (IndicePA): for each body "
        "we identify the email provider and the jurisdiction. Raw data from MxMap.it, open and "
        "reproducible methodology, CC BY-SA 4.0 licence.", s_body))
    gen = k.get("generated_at", "")[:10]
    story.append(Paragraph(
        f"<b>DRAFT.</b> This document is a draft with <b>preliminary</b> data: the first "
        f"official measurement is not yet consolidated. Data last updated: {gen or 'n/a'}"
        + (f" — coverage {tot.get('coverage_pct',0):.0f}%." if tot.get('coverage_pct') else ".")
        + " Do not cite as definitive data.", s_small))

    doc.build(story, onFirstPage=page_deco, onLaterPages=page_deco)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
