"""Generate Business Case PDF — Migrazione verso provider sovrani (per provider IT/EU e Consip)"""
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
                      "Business_Case_Migrazione_Sovranita_PA.pdf")

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
                             "Osservatorio Nazionale Sovranità Digitale — Business Case — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"pag. {doc.page}")
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
    story.append(Paragraph("La Migrazione verso Provider Sovrani:<br/>Un'Opportunità di Mercato", s_title))
    story.append(Paragraph("Per provider IT italiani ed europei, Consip e centrali di committenza — "
                           "Osservatorio Nazionale Sovranità Digitale — Giugno 2025", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("In sintesi", s_h1))
    story.append(Paragraph(
        "La Pubblica Amministrazione italiana — circa 23.000 enti — dipende oggi in misura "
        "rilevante da provider di posta elettronica soggetti a giurisdizione extra-UE. "
        "L'evoluzione normativa (GDPR, Schrems II, Strategia Cloud Italia, NIS2) e la crescente "
        "attenzione politica spingono verso la migrazione su infrastrutture sovrane. Questo "
        "rappresenta una <b>significativa opportunità di mercato</b> per i provider italiani ed europei "
        "e una <b>leva strategica</b> per le centrali di committenza pubblica.", s_body))

    # KPI cards row
    story.append(Spacer(1, 2 * mm))
    kpi_row = [[
        Table([[Paragraph("~23.000", s_kpi_num)], [Paragraph("enti PA potenziali clienti", s_kpi_lbl)]]),
        Table([[Paragraph("—%", s_kpi_num)], [Paragraph("oggi su provider extra-UE", s_kpi_lbl)]]),
        Table([[Paragraph("—%", s_kpi_num)], [Paragraph("quota di mercato contendibile", s_kpi_lbl)]]),
    ]]
    kt = Table(kpi_row, colWidths=[56 * mm, 56 * mm, 56 * mm])
    kt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY_BG),
        ("BOX", (0, 0), (0, 0), 0.5, WHITE), ("BOX", (1, 0), (1, 0), 0.5, WHITE),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("INNERGRID", (0, 0), (-1, -1), 2, WHITE),
    ]))
    story.append(kt)
    story.append(Paragraph("I valori percentuali saranno aggiornati con i dati del prossimo report "
                           "(fonte: MxMap.it su IndicePA).", s_small))

    story.append(Paragraph("Il contesto: una domanda in formazione", s_h1))
    story.append(Paragraph(
        "Tre forze convergenti stanno trasformando la sovranità digitale da tema di nicchia a "
        "requisito di acquisto della PA:", s_body))
    story.append(Paragraph("•  <b>Spinta normativa</b> — GDPR e Schrems II rendono giuridicamente fragile "
                           "l'uso di provider soggetti al CLOUD Act; la Strategia Cloud Italia impone la "
                           "qualificazione delle infrastrutture.", s_bullet))
    story.append(Paragraph("•  <b>Spinta politica</b> — la sovranità digitale è entrata nell'agenda "
                           "istituzionale italiana ed europea, con crescente domanda di alternative nazionali.", s_bullet))
    story.append(Paragraph("•  <b>Spinta reputazionale</b> — gli enti sono sempre più consapevoli del "
                           "rischio giurisdizionale e cercano soluzioni che li mettano al riparo.", s_bullet))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Perché ora", s_box_title),
        Paragraph("La finestra di mercato si apre quando il quadro normativo si fa stringente ma "
                  "l'offerta sovrana è ancora poco strutturata. È il momento in cui un provider può "
                  "posizionarsi come riferimento prima che il mercato si consolidi.", s_box_body),
    ], AMBER_LIGHT, AMBER_BORDER))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("1. Il mercato potenziale", s_h1))
    story.append(Paragraph(
        "Il bacino è l'intera PA italiana censita nell'IndicePA. La segmentazione per tipologia "
        "di ente consente di individuare i target a più alta priorità e propensione alla migrazione.", s_body))

    seg = [
        [Paragraph("Segmento", s_th), Paragraph("Enti (ordine di grandezza)", s_th),
         Paragraph("Priorità migrazione", s_th), Paragraph("Sensibilità dati", s_th)],
        [Paragraph("Comuni", s_tc_bold), Paragraph("~7.900", s_tc), Paragraph("Alta", s_tc), Paragraph("Anagrafe, tributi", s_tc)],
        [Paragraph("ASL / Sanità", s_tc_bold), Paragraph("Centinaia", s_tc), Paragraph("Critica", s_tc), Paragraph("Dati sanitari", s_tc)],
        [Paragraph("Scuole / Università", s_tc_bold), Paragraph("Migliaia", s_tc), Paragraph("Media", s_tc), Paragraph("Dati studenti", s_tc)],
        [Paragraph("PA centrale / Ministeri", s_tc_bold), Paragraph("Decine", s_tc), Paragraph("Critica", s_tc), Paragraph("Atti, policy", s_tc)],
        [Paragraph("Regioni / Province", s_tc_bold), Paragraph("~120", s_tc), Paragraph("Alta", s_tc), Paragraph("Servizi, sanità", s_tc)],
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
    story.append(Paragraph("Le numerosità sono ordini di grandezza indicativi dall'IndicePA; i dati "
                           "puntuali per segmento saranno pubblicati nel report.", s_small))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2. La proposta di valore del provider sovrano", s_h1))
    story.append(Paragraph(
        "Un provider che voglia conquistare questo mercato deve costruire un'offerta intorno a "
        "elementi che i grandi operatori extra-UE non possono garantire per costruzione:", s_body))
    story.append(Paragraph("•  <b>Giurisdizione UE/IT garantita</b> — assenza di obblighi di disclosure "
                           "verso autorità extra-europee (no CLOUD Act).", s_bullet))
    story.append(Paragraph("•  <b>Conformità documentata</b> — GDPR by design, qualificazione ACN, "
                           "localizzazione dei dati certificata.", s_bullet))
    story.append(Paragraph("•  <b>Continuità e indipendenza</b> — nessun rischio di interruzione per "
                           "decisioni unilaterali estere o tensioni geopolitiche.", s_bullet))
    story.append(Paragraph("•  <b>Supporto e prossimità</b> — assistenza in lingua, SLA su fuso e "
                           "normativa nazionale, radicamento sul territorio.", s_bullet))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Differenziazione, non competizione di prezzo", s_box_title),
        Paragraph("Il provider sovrano non deve battere i grandi operatori sul prezzo per terabyte, "
                  "ma sul valore: conformità, riduzione del rischio giuridico e autonomia. È una vendita "
                  "di risk management, non di commodity.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ── PAGE 3 ──
    story.append(PageBreak())
    story.append(Paragraph("3. La leva del procurement pubblico", s_h1))
    story.append(Paragraph(
        "Consip e le centrali di committenza hanno un ruolo determinante: i criteri delle convenzioni "
        "e degli accordi quadro orientano di fatto le scelte tecnologiche di migliaia di enti. "
        "Inserire requisiti di sovranità nei bandi crea simultaneamente domanda qualificata e "
        "un campo di gioco equo per i provider conformi.", s_body))

    story.append(Paragraph("3.1 Requisiti di sovranità inseribili nelle gare", s_h2))
    proc = [
        [Paragraph("Requisito", s_th), Paragraph("Effetto", s_th)],
        [Paragraph("Giurisdizione esclusiva UE sui dati", s_tc_bold),
         Paragraph("Esclude provider soggetti a normative extra-UE di disclosure", s_tc)],
        [Paragraph("Localizzazione dei data center in UE/IT", s_tc_bold),
         Paragraph("Garantisce controllo fisico e tracciabilità", s_tc)],
        [Paragraph("Qualificazione ACN del servizio", s_tc_bold),
         Paragraph("Allinea l'acquisto alla Strategia Cloud Italia", s_tc)],
        [Paragraph("Reversibilità e portabilità dei dati", s_tc_bold),
         Paragraph("Evita il lock-in e abilita la concorrenza futura", s_tc)],
        [Paragraph("Trasparenza su subfornitori e MX", s_tc_bold),
         Paragraph("Rende verificabile la catena di sovranità", s_tc)],
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
    story.append(Paragraph("3.2 Benefici per le centrali di committenza", s_h2))
    story.append(Paragraph("•  <b>Riduzione del rischio aggregato</b> — un parco fornitori conforme "
                           "abbassa l'esposizione giuridica dell'intera PA.", s_bullet))
    story.append(Paragraph("•  <b>Stimolo all'industria nazionale</b> — la domanda pubblica qualificata "
                           "fa crescere un ecosistema IT europeo competitivo.", s_bullet))
    story.append(Paragraph("•  <b>Coerenza con gli obiettivi strategici</b> — l'acquisto diventa "
                           "strumento di politica industriale e di autonomia.", s_bullet))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("4. Percorso e ostacoli", s_h1))
    story.append(Paragraph(
        "La migrazione non è priva di attriti. Riconoscerli è parte del business case: chi offre "
        "un percorso di migrazione gestito, e non solo un prodotto, vince.", s_body))
    obs = [
        [Paragraph("Ostacolo", s_th), Paragraph("Mitigazione lato offerta", s_th)],
        [Paragraph("Costi e tempi di migrazione", s_tc_bold),
         Paragraph("Servizi di migrazione chiavi in mano, strumenti di import, affiancamento", s_tc)],
        [Paragraph("Abitudine agli strumenti diffusi", s_tc_bold),
         Paragraph("Interoperabilità, formazione, interfacce familiari", s_tc)],
        [Paragraph("Percezione di minore affidabilità", s_tc_bold),
         Paragraph("SLA solidi, referenze pubbliche, certificazioni", s_tc)],
        [Paragraph("Frammentazione degli enti", s_tc_bold),
         Paragraph("Convenzioni quadro e offerte aggregate via Consip", s_tc)],
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
        Paragraph("Per i provider IT italiani ed europei", s_box_title),
        Paragraph("Costruite un'offerta esplicita di sovranità: comunicate giurisdizione, conformità e "
                  "percorso di migrazione. Usate i dati pubblici dell'Osservatorio per dimensionare il "
                  "mercato e individuare i segmenti prioritari.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(box([
        Paragraph("Per Consip e le centrali di committenza", s_box_title),
        Paragraph("Inserite requisiti di sovranità nelle convenzioni per posta e cloud. Trasformate "
                  "la spesa pubblica in leva di autonomia strategica e crescita industriale.", s_box_body),
    ], GREEN_LIGHT, GREEN_BORDER))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2))
    story.append(Paragraph("Fonti", s_h2))
    for ref in [
        "Osservatorio Nazionale Sovranità Digitale — https://fpietrosanti.github.io/osservatorio-nazionale-sovranita-digitale/",
        "MxMap.it — Mappatura provider email PA — https://fpietrosanti.github.io/mxmap.it/",
        "IndicePA — https://indicepa.gov.it",
        "Strategia Cloud Italia (2021); Regolamento ACN n. 307/2022",
        "GDPR (Reg. UE 2016/679); Schrems II (CGUE C-311/18)",
    ]:
        story.append(Paragraph(f"•  {ref}", s_ref))
    story.append(Spacer(1, 3 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("Documento rilasciato sotto licenza CC BY-SA 4.0. "
                           "Contatti: github.com/fpietrosanti/osservatorio-nazionale-sovranita-digitale", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
