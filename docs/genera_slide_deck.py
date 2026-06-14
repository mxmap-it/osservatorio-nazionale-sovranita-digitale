"""Generate Slide Deck PDF (landscape, 16:9-ish) — Osservatorio Sovranità Digitale"""
import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as canvas_mod

OUTPUT = os.path.join(os.path.dirname(__file__), "Slide_Deck_Osservatorio_Sovranita_Digitale.pdf")

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
    c.drawString(ML, 12 * mm, "Osservatorio Nazionale Sovranità Digitale")
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
        c.drawString(ML, cy - 8 * mm, "Valori in aggiornamento — fonte: MxMap.it su IndicePA")
    content_slide(c, title, n, total, body)


def build():
    c = canvas_mod.Canvas(OUTPUT, pagesize=PAGE)
    TOTAL = 16
    n = 0

    # 1 — Title
    n += 1
    title_slide(c, "Osservatorio Nazionale",
                "Sovranità Digitale nella PA Italiana",
                "Misurare, rendere consapevoli, stimolare il cambiamento — Giugno 2025",
                n, TOTAL)
    c.showPage()

    # 2 — Cos'è
    n += 1
    content_slide(c, "Cos'è l'Osservatorio", n, TOTAL, lambda c, y: bullets(c, [
        "Progetto indipendente di monitoraggio civico della sovranità digitale nella PA italiana",
        "Misura la dipendenza degli enti pubblici da infrastrutture digitali estere",
        "Parte dalla posta elettronica: il canale di comunicazione più diffuso e più sensibile",
        "Dati aperti, metodologia replicabile, codice open source (CC BY-SA 4.0)",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 3 — Il problema (section)
    n += 1
    section_slide(c, "Il problema: dipendenza giurisdizionale", n, TOTAL)
    c.showPage()

    # 4 — Il problema dettaglio
    n += 1
    content_slide(c, "Perché è un problema", n, TOTAL, lambda c, y: bullets(c, [
        "Le email istituzionali contengono dati personali dei cittadini (art. 4 GDPR)",
        "Molti enti usano provider soggetti a giurisdizione extra-UE",
        "Il CLOUD Act USA consente l'accesso ai dati anche se i server sono in Europa",
        "Conflitto strutturale con GDPR e sentenze Schrems I e II",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 5 — KPI
    n += 1
    kpi_slide(c, "I numeri (in aggiornamento)", [
        ("~23.000", "enti PA monitorati"),
        ("—%", "su provider extra-UE"),
        ("—%", "su provider italiani"),
        ("—%", "su provider UE"),
    ], n, TOTAL)
    c.showPage()

    # 6 — Metodologia (section)
    n += 1
    section_slide(c, "Come lo misuriamo", n, TOTAL)
    c.showPage()

    # 7 — Metodologia steps
    n += 1
    content_slide(c, "La metodologia in 4 passi", n, TOTAL, lambda c, y: bullets(c, [
        "1. Estrazione enti e domini dall'IndicePA (API CKAN JSON)",
        "2. Risoluzione dei record MX (Mail Exchange) via DNS",
        "3. Identificazione del provider e della sua giurisdizione",
        "4. Classificazione di sovranità: Italiano / UE / Extra-UE",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 8 — Rischi (section)
    n += 1
    section_slide(c, "I rischi", n, TOTAL)
    c.showPage()

    # 9 — Rischi dettaglio
    n += 1
    content_slide(c, "Quattro dimensioni di rischio", n, TOTAL, lambda c, y: bullets(c, [
        "Giurisdizionale — accesso ai dati da parte di autorità extra-UE",
        "Protezione dati — non conformità GDPR sui trasferimenti",
        "Continuità operativa — dipendenza da decisioni unilaterali estere",
        "Strategico ed economico — lock-in e mancato sviluppo dell'industria UE",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 10 — A chi serve (section)
    n += 1
    section_slide(c, "A chi serve l'Osservatorio", n, TOTAL)
    c.showPage()

    # 11 — Stakeholder
    n += 1
    content_slide(c, "Il monitoraggio civico al servizio di tutti", n, TOTAL, lambda c, y: bullets(c, [
        "Decisori politici — dati per interrogazioni e proposte normative",
        "Regolatori (AgID, ACN, Garante) — base per linee guida e provvedimenti",
        "Dirigenti PA — confronto e supporto alle scelte di migrazione",
        "Giornalisti, ricercatori, cittadini — trasparenza e consapevolezza",
        "Provider IT e Consip — opportunità di mercato e procurement",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 12 — Cosa proponiamo (section)
    n += 1
    section_slide(c, "Cosa proponiamo", n, TOTAL)
    c.showPage()

    # 13 — Raccomandazioni
    n += 1
    content_slide(c, "Cinque raccomandazioni", n, TOTAL, lambda c, y: bullets(c, [
        "Censimento obbligatorio dei provider nella PA (trasparenza)",
        "Requisiti di sovranità nelle convenzioni Consip",
        "Piano nazionale di migrazione con fondi dedicati",
        "Monitoraggio continuo e pubblico nel tempo",
        "Promozione del modello a livello europeo",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 14 — Documenti
    n += 1
    content_slide(c, "I documenti dell'Osservatorio", n, TOTAL, lambda c, y: bullets(c, [
        "Policy Brief — per i decisori politici (2 pagine)",
        "Technical Brief — per AgID, ACN, Garante (6 pagine)",
        "Business Case — per provider IT e Consip",
        "EU Briefing — per le istituzioni europee (inglese)",
        "Tutti scaricabili dal sito, sotto licenza CC BY-SA 4.0",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 15 — Roadmap
    n += 1
    content_slide(c, "Prossimi passi", n, TOTAL, lambda c, y: bullets(c, [
        "Pubblicazione del report con i dati aggiornati",
        "Presentazione dei risultati alla Camera dei Deputati",
        "Integrazione dei KPI live da MxMap.it, aggiornati quotidianamente",
        "Estensione del monitoraggio ad altri servizi digitali della PA",
    ], ML, y, W - 2 * ML))
    c.showPage()

    # 16 — Chiusura
    n += 1
    title_slide(c, "Partecipa",
                "Il cambiamento parte dalla consapevolezza",
                "osservatorio-nazionale-sovranita-digitale  •  fpietrosanti.github.io/mxmap.it  •  Telegram",
                n, TOTAL)
    c.showPage()

    c.save()
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
