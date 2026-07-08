"""Generate Technical Brief PDF — Analisi Tecnico-Normativa per i Regolatori"""
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
                      "Technical_Brief_Sovranita_Digitale_PA.pdf")

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
        "Osservatorio Nazionale Sovranità Digitale — Technical Brief — CC BY-SA 4.0"
    )
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"pag. {doc.page}")
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
        "Analisi Tecnico-Normativa della Dipendenza<br/>"
        "Digitale nella Pubblica Amministrazione Italiana",
        s_title
    ))
    story.append(Paragraph(
        "Per AgID, ACN, Garante per la Protezione dei Dati Personali — "
        "Osservatorio Nazionale Sovranità Digitale — Giugno 2025",
        s_subtitle
    ))
    story.append(HRFlowable(
        width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2
    ))

    # Executive Summary
    story.append(Paragraph("Executive Summary", s_h1))
    story.append(Paragraph(
        "Il presente documento analizza la dipendenza della Pubblica Amministrazione "
        "italiana da infrastrutture di comunicazione digitale gestite da soggetti "
        "extra-europei. L'analisi si basa sui dati raccolti dal progetto MxMap.it, "
        "che ha mappato i record MX (Mail Exchange) di tutti i domini istituzionali "
        "registrati nell'Indice delle Pubbliche Amministrazioni (IndicePA).",
        s_body
    ))
    story.append(Paragraph(
        "I risultati evidenziano una significativa esposizione delle comunicazioni "
        "istituzionali a giurisdizioni terze, con implicazioni dirette su: protezione "
        "dei dati personali (GDPR, Schrems II), sicurezza nazionale (NIS2, Perimetro "
        "di Sicurezza Nazionale Cibernetica), autonomia strategica e conformità alle "
        "linee guida AgID e alla Strategia Cloud Italia.",
        s_body
    ))

    # Key findings box
    story.append(Spacer(1, 2 * mm))
    story.append(gray_box([
        Paragraph("Risultati chiave", s_box_title),
        Paragraph("•  La PA italiana comprende circa 23.000 enti con domini email istituzionali", s_bullet_small),
        Paragraph("•  Una quota significativa di questi enti utilizza provider email soggetti a giurisdizione extra-UE", s_bullet_small),
        Paragraph("•  I provider statunitensi sono soggetti al CLOUD Act (18 U.S.C. § 2713, 2018)", s_bullet_small),
        Paragraph("•  Le comunicazioni istituzionali contengono regolarmente dati personali ex art. 4 GDPR", s_bullet_small),
        Paragraph("•  La dipendenza è trasversale: Comuni, ASL, Università, Ministeri", s_bullet_small),
        Paragraph("•  Non esiste attualmente un obbligo di disclosure del provider email nel catalogo IndicePA", s_bullet_small),
    ]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Destinatari", s_h2))
    dest_data = [
        [Paragraph("Ente", s_th), Paragraph("Competenza", s_th), Paragraph("Azione attesa", s_th)],
        [Paragraph("AgID", s_tc_bold),
         Paragraph("Linee guida, qualificazione cloud, IndicePA", s_tc),
         Paragraph("Aggiornamento linee guida e catalogo IndicePA", s_tc)],
        [Paragraph("ACN", s_tc_bold),
         Paragraph("Cybersecurity, Perimetro Sicurezza, NIS2", s_tc),
         Paragraph("Valutazione rischio, requisiti sicurezza", s_tc)],
        [Paragraph("Garante Privacy", s_tc_bold),
         Paragraph("Protezione dati, trasferimenti extra-UE", s_tc),
         Paragraph("Verifica conformità, provvedimenti", s_tc)],
        [Paragraph("ANAC", s_tc_bold),
         Paragraph("Trasparenza, procurement pubblico", s_tc),
         Paragraph("Requisiti sovranità in gare d'appalto", s_tc)],
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
    # PAGE 2 — Metodologia e Quadro Tecnico
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("1. Metodologia di raccolta dati", s_h1))
    story.append(Paragraph(
        "La metodologia adottata si articola in quattro fasi sequenziali, "
        "ciascuna automatizzata e documentata per garantire riproducibilità e verificabilità.",
        s_body
    ))

    story.append(Paragraph("1.1 Acquisizione dell'elenco enti", s_h2))
    story.append(Paragraph(
        "L'elenco degli enti e dei relativi domini istituzionali viene estratto "
        "dall'IndicePA attraverso l'API CKAN JSON. L'IndicePA, gestito da AgID ai "
        "sensi dell'art. 6-ter del CAD (D.Lgs. 82/2005), è la fonte autoritativa "
        "per l'identificazione di tutte le PA italiane. Vengono estratti: codice "
        "IPA (cod_amm), denominazione, dominio email, tipologia ente e regione.",
        s_body
    ))

    story.append(Paragraph("1.2 Risoluzione DNS dei record MX", s_h2))
    story.append(Paragraph(
        "Per ciascun dominio istituzionale viene effettuata una query DNS di tipo MX "
        "(RFC 7208). I record MX indicano i server designati a ricevere la posta "
        "elettronica per quel dominio. La risoluzione avviene tramite resolver "
        "pubblici per garantire risultati non influenzati da configurazioni locali.",
        s_body
    ))

    story.append(Paragraph("1.3 Identificazione del provider", s_h2))
    story.append(Paragraph(
        "I record MX vengono confrontati con un database di pattern noti per "
        "identificare il provider email. Il database contiene oltre 200 pattern "
        "di provider, mantenuto e aggiornato nel repository open source MxMap.it. "
        "La classificazione assegna a ogni provider:",
        s_body
    ))
    story.append(Paragraph("•  <b>Nome commerciale</b> del provider (es. Google Workspace, Microsoft 365)", s_bullet))
    story.append(Paragraph("•  <b>Paese di sede legale</b> dell'operatore (codice ISO 3166-1)", s_bullet))
    story.append(Paragraph("•  <b>Classificazione di sovranità</b>: IT (italiano), EU (europeo), EXTRA_EU (extra-europeo)", s_bullet))

    story.append(Paragraph("1.4 Validazione e pubblicazione", s_h2))
    story.append(Paragraph(
        "I dati aggregati vengono sottoposti a controlli di qualità automatici "
        "(coerenza dei codici IPA, validità dei domini, completezza dei record) "
        "e pubblicati in formato CSV e JSON sotto licenza CC BY-SA 4.0. L'intero "
        "processo è ripetibile e il codice sorgente è pubblicamente disponibile.",
        s_body
    ))

    # Schema dati
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Schema dati del dataset", s_h2))
    schema_data = [
        [Paragraph("Campo", s_th), Paragraph("Tipo", s_th), Paragraph("Descrizione", s_th), Paragraph("Fonte", s_th)],
        [Paragraph("cod_amm", s_tc_bold), Paragraph("string", s_tc), Paragraph("Codice IPA dell'ente", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("des_amm", s_tc_bold), Paragraph("string", s_tc), Paragraph("Denominazione ufficiale", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("dominio", s_tc_bold), Paragraph("string", s_tc), Paragraph("Dominio email istituzionale", s_tc), Paragraph("IndicePA", s_tc)],
        [Paragraph("mx_records", s_tc_bold), Paragraph("string[]", s_tc), Paragraph("Record MX rilevati", s_tc), Paragraph("DNS query", s_tc)],
        [Paragraph("provider", s_tc_bold), Paragraph("string", s_tc), Paragraph("Provider identificato", s_tc), Paragraph("MxMap.it", s_tc)],
        [Paragraph("provider_country", s_tc_bold), Paragraph("ISO 3166", s_tc), Paragraph("Sede legale del provider", s_tc), Paragraph("MxMap.it", s_tc)],
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
    # PAGE 3 — Quadro Normativo Dettagliato
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("2. Quadro normativo di riferimento", s_h1))
    story.append(Paragraph(
        "La dipendenza da provider extra-UE per le comunicazioni istituzionali "
        "interseca molteplici profili normativi, ciascuno con implicazioni "
        "specifiche per gli enti e per i regolatori.",
        s_body
    ))

    # 2.1 GDPR
    story.append(Paragraph("2.1 Regolamento Generale sulla Protezione dei Dati (GDPR)", s_h2))
    story.append(Paragraph(
        "Il GDPR (Reg. UE 2016/679) disciplina il trattamento e il trasferimento "
        "dei dati personali. La posta elettronica istituzionale costituisce "
        "trattamento di dati personali ai sensi dell'art. 4, in quanto le "
        "comunicazioni contengono regolarmente: nomi, indirizzi, codici fiscali, "
        "dati sanitari, informazioni giudiziarie e altri dati sensibili.",
        s_body
    ))
    story.append(Paragraph(
        "Il Capo V del GDPR (artt. 44-49) subordina i trasferimenti verso paesi "
        "terzi a garanzie specifiche. L'utilizzo di un provider soggetto al CLOUD "
        "Act configura un potenziale trasferimento extra-UE indipendentemente dalla "
        "localizzazione fisica dei server, poiché l'autorità giudiziaria statunitense "
        "può imporre la disclosure dei dati al provider.",
        s_body
    ))

    # Schrems box
    story.append(Spacer(1, 1 * mm))
    story.append(colored_box([
        Paragraph("Sentenze Schrems I e II — Implicazioni", s_box_title),
        Paragraph(
            "<b>Schrems I</b> (C-362/14, 2015): La CGUE ha invalidato il Safe Harbor "
            "per insufficienza di garanzie contro la sorveglianza di massa USA.",
            s_box_body
        ),
        Paragraph(
            "<b>Schrems II</b> (C-311/18, 2020): La CGUE ha invalidato il Privacy Shield "
            "e richiesto una valutazione caso per caso delle clausole contrattuali standard (SCC). "
            "Le SCC sono insufficienti quando il diritto del paese terzo impone obblighi di "
            "disclosure incompatibili con le garanzie europee.",
            s_box_body
        ),
        Paragraph(
            "<b>Data Privacy Framework</b> (2023): Decisione di adeguatezza CE per gli USA, "
            "ma applicabile solo alle organizzazioni auto-certificate DPF. Non risolve il "
            "conflitto strutturale CLOUD Act / GDPR e potrebbe essere invalidata (\"Schrems III\").",
            s_box_body
        ),
    ], AMBER_LIGHT, AMBER_BORDER))

    # 2.2 CLOUD Act
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2.2 CLOUD Act (Clarifying Lawful Overseas Use of Data Act)", s_h2))
    story.append(Paragraph(
        "Il CLOUD Act (18 U.S.C. § 2713, 2018) consente alle autorità giudiziarie "
        "statunitensi di richiedere a qualsiasi provider soggetto a giurisdizione USA "
        "la produzione di dati in loro possesso, custodia o controllo, "
        "<b>indipendentemente dalla localizzazione fisica dei dati</b>.",
        s_body
    ))
    story.append(Paragraph(
        "Questo significa che un ente PA che utilizza Google Workspace o Microsoft 365 "
        "per la posta elettronica espone le proprie comunicazioni istituzionali alla "
        "potenziale disclosure verso le autorità USA, anche se i server sono fisicamente "
        "situati in Europa (regioni UE dei cloud provider).",
        s_body
    ))

    # Risk box
    story.append(colored_box([
        Paragraph("Conflitto giuridico strutturale", s_box_title),
        Paragraph(
            "Il CLOUD Act crea un conflitto diretto con il GDPR: il provider è "
            "obbligato a produrre i dati dal diritto USA, ma è vietato dal farlo "
            "dal diritto UE. Questo conflitto non è risolvibile attraverso misure "
            "contrattuali o tecniche, poiché l'obbligo di disclosure del CLOUD Act "
            "prevale sugli accordi contrattuali del provider.",
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
        Paragraph("L'AMMISSIONE DI MICROSOFT", s_quote_eyebrow),
        Paragraph("«No, non posso garantirlo.»", s_quote_big),
        Paragraph(
            "Il Direttore degli Affari Pubblici e Legali di Microsoft France, "
            "richiesto in audizione se potesse garantire che i dati dei cittadini "
            "europei non venissero trasferiti al governo statunitense in virtù di "
            "un ordine emesso ai sensi del CLOUD Act — senza l'accordo delle "
            "autorità nazionali. È Microsoft stessa ad ammettere di non poter "
            "escludere il trasferimento dei dati europei alle autorità USA.",
            s_quote_context
        ),
        Paragraph(
            "Anton Carniaux, Direttore Affari Pubblici e Legali, Microsoft France "
            "— Audizione, Commissione d'inchiesta del Senato francese, "
            "10 giugno 2025. Fonti: Senato francese (senat.fr) · heise.de",
            s_quote_attr
        ),
    ], GRAY_BG, RED_BORDER))

    # 2.3 Strategia Cloud Italia e ACN
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("2.3 Strategia Cloud Italia e qualificazione ACN", s_h2))
    story.append(Paragraph(
        "La Strategia Cloud Italia (2021) classifica i dati della PA in tre livelli: "
        "ordinari, critici e strategici. Per i dati critici e strategici è prevista "
        "la migrazione verso il Polo Strategico Nazionale (PSN) o verso infrastrutture "
        "qualificate da ACN (Agenzia per la Cybersicurezza Nazionale).",
        s_body
    ))
    story.append(Paragraph(
        "Il Regolamento ACN per la qualificazione dei servizi cloud per la PA "
        "(Determinazione n. 307/2022 e successive modifiche) definisce requisiti "
        "specifici per la localizzazione dei dati e il controllo giurisdizionale. "
        "I servizi qualificati al livello QC3 (strategico) e QC2 (critico) devono "
        "garantire che i dati non siano accessibili da giurisdizioni extra-UE.",
        s_body
    ))

    # 2.4 NIS2
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("2.4 Direttiva NIS2 e D.Lgs. 138/2024", s_h2))
    story.append(Paragraph(
        "La Direttiva NIS2 (2022/2555), recepita con D.Lgs. 138/2024, impone "
        "alle PA obblighi di gestione del rischio cybersecurity, inclusa la "
        "valutazione dei rischi della supply chain. La dipendenza da provider "
        "email extra-UE configura un rischio di supply chain che deve essere "
        "valutato e gestito nell'ambito delle misure di sicurezza previste dall'art. 21.",
        s_body
    ))

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 4 — Analisi dei Rischi
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("3. Analisi dei rischi", s_h1))
    story.append(Paragraph(
        "La dipendenza da provider extra-UE genera rischi su quattro dimensioni "
        "interconnesse, ciascuna rilevante per diversi profili regolatori.",
        s_body
    ))

    # Risk matrix
    risk_data = [
        [Paragraph("Dimensione", s_th), Paragraph("Rischio", s_th),
         Paragraph("Impatto", s_th), Paragraph("Regolatore", s_th)],
        [Paragraph("Giurisdizionale", s_tc_bold),
         Paragraph("Accesso ai dati PA da parte di autorità extra-UE "
                    "tramite CLOUD Act o normativa equivalente", s_tc),
         Paragraph("ALTO", ParagraphStyle("R", parent=s_tc_bold, textColor=RED_BORDER)),
         Paragraph("Garante, ACN", s_tc)],
        [Paragraph("Protezione dati", s_tc_bold),
         Paragraph("Non conformità ai requisiti GDPR per i trasferimenti "
                    "extra-UE (Capo V); potenziale violazione Schrems II", s_tc),
         Paragraph("ALTO", ParagraphStyle("R2", parent=s_tc_bold, textColor=RED_BORDER)),
         Paragraph("Garante", s_tc)],
        [Paragraph("Continuità operativa", s_tc_bold),
         Paragraph("Interruzione del servizio per decisioni unilaterali "
                    "del provider, sanzioni, conflitti geopolitici", s_tc),
         Paragraph("MEDIO", ParagraphStyle("A", parent=s_tc_bold, textColor=AMBER_BORDER)),
         Paragraph("AgID, ACN", s_tc)],
        [Paragraph("Strategico", s_tc_bold),
         Paragraph("Lock-in tecnologico, perdita di competenze nazionali, "
                    "dipendenza strutturale da ecosistemi proprietari", s_tc),
         Paragraph("MEDIO", ParagraphStyle("A2", parent=s_tc_bold, textColor=AMBER_BORDER)),
         Paragraph("AgID, ANAC", s_tc)],
        [Paragraph("Economico", s_tc_bold),
         Paragraph("Flussi finanziari verso operatori esteri, mancato "
                    "sviluppo dell'industria IT nazionale ed europea", s_tc),
         Paragraph("MEDIO", ParagraphStyle("A3", parent=s_tc_bold, textColor=AMBER_BORDER)),
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
    story.append(Paragraph("3.1 Scenario: richiesta CLOUD Act", s_h2))
    story.append(Paragraph(
        "Si consideri lo scenario in cui un'autorità giudiziaria USA emette un "
        "ordine di produzione (warrant o subpoena) verso un provider che gestisce "
        "la posta di enti PA italiani:",
        s_body
    ))
    story.append(Paragraph("1.  Il provider è legalmente obbligato a produrre i dati (18 U.S.C. § 2713)", s_bullet))
    story.append(Paragraph("2.  Il provider può contestare l'ordine solo se viola un trattato internazionale — "
                           "attualmente non esiste un executive agreement UE-USA", s_bullet))
    story.append(Paragraph("3.  L'ente PA non viene necessariamente informato della disclosure", s_bullet))
    story.append(Paragraph("4.  I dati possono includere: comunicazioni interne, dati dei cittadini, "
                           "informazioni sensibili, atti amministrativi", s_bullet))
    story.append(Paragraph("5.  La disclosure viola potenzialmente gli artt. 44-49 GDPR e configura un "
                           "data breach ai sensi dell'art. 33", s_bullet))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("3.2 Rischio per tipologia di ente", s_h2))
    story.append(Paragraph(
        "L'impatto della dipendenza varia per tipologia di ente in funzione "
        "della sensibilità dei dati trattati:",
        s_body
    ))

    tipo_data = [
        [Paragraph("Tipologia", s_th), Paragraph("Dati sensibili tipici", s_th),
         Paragraph("Rischio", s_th)],
        [Paragraph("ASL / Ospedali", s_tc_bold),
         Paragraph("Dati sanitari, referti, comunicazioni medico-paziente", s_tc),
         Paragraph("CRITICO", ParagraphStyle("C", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Comuni", s_tc_bold),
         Paragraph("Anagrafe, stato civile, servizi sociali, tributi", s_tc),
         Paragraph("ALTO", ParagraphStyle("A4", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Forze dell'ordine", s_tc_bold),
         Paragraph("Indagini, segnalazioni, dati giudiziari", s_tc),
         Paragraph("CRITICO", ParagraphStyle("C2", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Università", s_tc_bold),
         Paragraph("Dati studenti, ricerca, proprietà intellettuale", s_tc),
         Paragraph("MEDIO", ParagraphStyle("M", parent=s_tc_bold, textColor=AMBER_BORDER))],
        [Paragraph("Ministeri", s_tc_bold),
         Paragraph("Policy, comunicazioni inter-istituzionali, dati classificati", s_tc),
         Paragraph("CRITICO", ParagraphStyle("C3", parent=s_tc_bold, textColor=RED_BORDER))],
        [Paragraph("Autorità indipendenti", s_tc_bold),
         Paragraph("Segnalazioni, procedimenti, dati riservati", s_tc),
         Paragraph("CRITICO", ParagraphStyle("C4", parent=s_tc_bold, textColor=RED_BORDER))],
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
    # PAGE 5 — Raccomandazioni per i Regolatori
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("4. Raccomandazioni per i regolatori", s_h1))

    # AgID
    story.append(Paragraph("4.1 Raccomandazioni per AgID", s_h2))
    story.append(colored_box([
        Paragraph("R1 — Estendere l'IndicePA con informazioni sul provider email", s_box_title),
        Paragraph(
            "Inserire nell'IndicePA un campo obbligatorio per il provider email "
            "e la relativa classificazione di sovranità. Questo consentirebbe un "
            "monitoraggio istituzionale continuo e renderebbe l'informazione pubblica "
            "e accessibile a tutti gli stakeholder.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R2 — Aggiornare le linee guida sui servizi email", s_box_title),
        Paragraph(
            "Aggiornare le Linee Guida sulla formazione, gestione e conservazione "
            "dei documenti informatici per includere requisiti espliciti di sovranità "
            "giurisdizionale per i servizi di posta elettronica istituzionale. "
            "Prevedere un periodo di adeguamento proporzionato alla dimensione dell'ente.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R3 — Definire criteri di qualificazione per i servizi email PA", s_box_title),
        Paragraph(
            "Analogamente alla qualificazione cloud, definire criteri specifici per "
            "i servizi email della PA, includendo: giurisdizione del provider, "
            "localizzazione dei dati, assenza di obblighi di disclosure verso autorità "
            "extra-UE, conformità GDPR certificata.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ACN
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("4.2 Raccomandazioni per ACN", s_h2))
    story.append(colored_box([
        Paragraph("R4 — Includere la dipendenza email nella valutazione del rischio NIS2", s_box_title),
        Paragraph(
            "Nelle linee guida per l'attuazione della NIS2, includere esplicitamente "
            "la dipendenza da provider email extra-UE come fattore di rischio nella "
            "valutazione della supply chain. Richiedere ai soggetti essenziali e importanti "
            "una dichiarazione del provider email utilizzato.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R5 — Estendere il Perimetro di Sicurezza Nazionale Cibernetica", s_box_title),
        Paragraph(
            "Valutare l'inclusione dei servizi di posta elettronica degli enti del "
            "Perimetro tra i beni ICT soggetti a notifica e a misure di sicurezza "
            "rafforzate, con particolare attenzione alla giurisdizione del provider.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # Garante
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("4.3 Raccomandazioni per il Garante Privacy", s_h2))
    story.append(colored_box([
        Paragraph("R6 — Provvedimento generale sull'uso di servizi email extra-UE nella PA", s_box_title),
        Paragraph(
            "Adottare un provvedimento generale, analogo a quello sui cookie (n. 231/2021) "
            "o su Google Analytics (n. 224/2022), che chiarisca le condizioni di liceità "
            "dell'utilizzo di servizi email gestiti da provider soggetti al CLOUD Act "
            "per le comunicazioni istituzionali della PA.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))
    story.append(Spacer(1, 2 * mm))
    story.append(colored_box([
        Paragraph("R7 — DPIA obbligatoria per servizi email PA con provider extra-UE", s_box_title),
        Paragraph(
            "Richiedere una Valutazione d'Impatto (DPIA, art. 35 GDPR) obbligatoria "
            "per gli enti PA che utilizzano servizi email gestiti da provider soggetti "
            "a giurisdizioni extra-UE, includendo la valutazione del rischio di "
            "disclosure ai sensi del CLOUD Act.",
            s_box_body
        ),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ═══════════════════════════════════════════════════════════════════
    # PAGE 6 — Roadmap e Riferimenti
    # ═══════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("5. Roadmap proposta", s_h1))
    story.append(Paragraph(
        "Si propone un percorso graduale di adeguamento, articolato in tre fasi, "
        "che tenga conto delle diverse dimensioni e capacità degli enti.",
        s_body
    ))

    road_data = [
        [Paragraph("Fase", s_th), Paragraph("Orizzonte", s_th),
         Paragraph("Azione", s_th), Paragraph("Responsabile", s_th)],
        [Paragraph("1. Trasparenza", s_tc_bold),
         Paragraph("0-6 mesi", s_tc),
         Paragraph("Censimento obbligatorio provider email in IndicePA; "
                    "pubblicazione dashboard pubblica", s_tc),
         Paragraph("AgID", s_tc)],
        [Paragraph("2. Regolazione", s_tc_bold),
         Paragraph("6-18 mesi", s_tc),
         Paragraph("Aggiornamento linee guida; provvedimento Garante; "
                    "criteri NIS2; qualificazione email", s_tc),
         Paragraph("AgID, ACN, Garante", s_tc)],
        [Paragraph("3. Migrazione", s_tc_bold),
         Paragraph("18-36 mesi", s_tc),
         Paragraph("Piano nazionale migrazione con fondi dedicati; "
                    "priorità per enti con dati critici/strategici", s_tc),
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

    # Priorità migrazione
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("5.1 Criteri di priorità per la migrazione", s_h2))
    story.append(Paragraph(
        "La migrazione dovrebbe essere prioritizzata in base alla sensibilità "
        "dei dati trattati e al profilo di rischio dell'ente:",
        s_body
    ))
    story.append(Paragraph("•  <b>Priorità 1 (immediata):</b> Enti del Perimetro Sicurezza Nazionale, "
                           "Forze dell'ordine, Servizi di intelligence, Ministeri", s_bullet))
    story.append(Paragraph("•  <b>Priorità 2 (entro 12 mesi):</b> ASL/Ospedali, Autorità indipendenti, "
                           "Regioni, Grandi Comuni", s_bullet))
    story.append(Paragraph("•  <b>Priorità 3 (entro 24 mesi):</b> Università, Enti di ricerca, "
                           "Province, Comuni medi", s_bullet))
    story.append(Paragraph("•  <b>Priorità 4 (entro 36 mesi):</b> Piccoli Comuni, Enti strumentali, "
                           "altre PA", s_bullet))

    # Conclusioni
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("6. Conclusioni", s_h1))
    story.append(Paragraph(
        "L'analisi dei dati MxMap.it evidenzia una dipendenza strutturale della PA "
        "italiana da provider email soggetti a giurisdizioni extra-europee. Questa "
        "dipendenza non è un problema teorico: il CLOUD Act crea un conflitto "
        "giuridico concreto con il GDPR, le sentenze Schrems e la Strategia Cloud Italia.",
        s_body
    ))
    story.append(Paragraph(
        "La soluzione richiede un approccio coordinato tra AgID, ACN e Garante Privacy, "
        "con azioni concrete su tre fronti: trasparenza (rendere visibile il problema), "
        "regolazione (definire requisiti chiari) e migrazione (supportare gli enti "
        "nel percorso di adeguamento).",
        s_body
    ))
    story.append(Paragraph(
        "L'Osservatorio Nazionale Sovranità Digitale mette a disposizione dati aperti, "
        "metodologia documentata e strumenti replicabili per supportare questo percorso. "
        "Il monitoraggio civico è al servizio delle istituzioni e dei cittadini.",
        s_body
    ))

    # Riferimenti
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph("Riferimenti normativi e fonti", s_h2))
    refs = [
        "GDPR — Regolamento (UE) 2016/679 del Parlamento Europeo e del Consiglio",
        "CLOUD Act — Clarifying Lawful Overseas Use of Data Act (18 U.S.C. § 2713, 2018)",
        "Schrems I — CGUE, C-362/14 (6 ottobre 2015)",
        "Schrems II — CGUE, C-311/18 (16 luglio 2020)",
        "Data Privacy Framework — Decisione di adeguatezza CE (10 luglio 2023)",
        "Direttiva NIS2 — Direttiva (UE) 2022/2555; D.Lgs. 138/2024",
        "Strategia Cloud Italia — Dipartimento per la trasformazione digitale (2021)",
        "CAD — D.Lgs. 82/2005, art. 6-ter (IndicePA)",
        "Regolamento ACN — Determinazione n. 307/2022 (qualificazione cloud PA)",
        "Perimetro di Sicurezza Nazionale Cibernetica — D.L. 105/2019, conv. L. 133/2019",
        "MxMap.it — https://mxmap.it/",
        "IndicePA — https://indicepa.gov.it",
        "Osservatorio Nazionale Sovranità Digitale — "
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
        "Questo documento è rilasciato sotto licenza CC BY-SA 4.0. "
        "Contatti: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale",
        s_small
    ))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
