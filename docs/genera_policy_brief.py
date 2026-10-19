"""Generate Policy Brief PDF — Sovranità Digitale nella PA Italiana"""
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
                      "Policy_Brief_Sovranita_Digitale_PA.pdf")

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
style_quote_eyebrow = ParagraphStyle(
    "QuoteEyebrow", fontName="Arial-Bold", fontSize=8.5, textColor=BLUE,
    spaceAfter=4, spaceBefore=0, leading=11, letterSpacing=1
)
style_quote = ParagraphStyle(
    "Quote", fontName="Arial-Italic", fontSize=14, textColor=DARK,
    spaceAfter=5, spaceBefore=0, leading=17, alignment=TA_LEFT
)
style_quote_context = ParagraphStyle(
    "QuoteContext", fontName="Arial", fontSize=8.5, textColor=DARK,
    spaceAfter=4, spaceBefore=0, leading=11.5, alignment=TA_LEFT
)
style_quote_attr = ParagraphStyle(
    "QuoteAttr", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT,
    spaceAfter=0, spaceBefore=0, leading=10, alignment=TA_LEFT
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
        "Osservatorio Nazionale Sovranità Digitale — CC BY-SA 4.0 — "
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


def quote_box(eyebrow, quote, context, attribution):
    """Highlighted callout with a tinted background and a coloured left border."""
    inner = [
        Paragraph(eyebrow, style_quote_eyebrow),
        Paragraph(quote, style_quote),
        Paragraph(context, style_quote_context),
        Paragraph(attribution, style_quote_attr),
    ]
    t = Table([[inner]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
        ("LINEBEFORE", (0, 0), (0, -1), 3, BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
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
        "Sovranità Digitale nella Pubblica<br/>Amministrazione Italiana",
        style_title
    ))
    story.append(Paragraph(
        "Osservatorio Nazionale Sovranità Digitale — Giugno 2025",
        style_subtitle
    ))
    story.append(HRFlowable(
        width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2
    ))

    # Il problema
    story.append(Paragraph("Il problema", style_h2))
    story.append(Paragraph(
        "La Pubblica Amministrazione italiana dipende in misura significativa "
        "da infrastrutture digitali gestite da provider soggetti a giurisdizioni "
        "extra-europee. Questa dipendenza espone le comunicazioni istituzionali "
        "e i dati dei cittadini a rischi concreti di accesso da parte di autorità "
        "straniere, in particolare attraverso il <b>CLOUD Act</b> statunitense (2018), "
        "e si pone in potenziale contrasto con il <b>GDPR</b> e le sentenze della "
        "Corte di Giustizia dell’UE (<b>Schrems I</b> e <b>II</b>). In particolare, gli "
        "<b>artt. 48 e 115 del GDPR</b> vietano di dare seguito a ordini di autorità "
        "extra-UE non fondati su accordi internazionali: a determinare la giurisdizione "
        "è la <b>nazionalità del fornitore</b>, non la sede fisica del dato.",
        style_body
    ))

    # Ammissione di Microsoft (quote box)
    story.append(Spacer(1, 2 * mm))
    story.append(quote_box(
        "L'AMMISSIONE DI MICROSOFT",
        "«No, non posso garantirlo.»",
        "Il Direttore degli Affari Pubblici e Legali di Microsoft France, "
        "richiesto in audizione se potesse garantire che i dati dei cittadini "
        "europei non venissero trasferiti al governo statunitense in virtù di un "
        "ordine emesso ai sensi del CLOUD Act — senza l'accordo delle autorità "
        "nazionali. È Microsoft stessa ad ammettere di non poter escludere il "
        "trasferimento dei dati europei alle autorità USA.",
        "Anton Carniaux, Direttore Affari Pubblici e Legali, Microsoft France — "
        "Audizione, Commissione d'inchiesta del Senato francese, 10 giugno 2025. "
        "Fonti: Senato francese (senat.fr) · heise.de"
    ))

    # I numeri (gray box)
    box_content = [
        Paragraph("I numeri", style_box_title),
        Paragraph("•  ~23.000 enti PA monitorati (fonte IndicePA)", style_bullet),
        Paragraph("•  I servizi email sono il primo ambito analizzato", style_bullet),
        Paragraph("•  La mappatura copre tutti i domini istituzionali registrati", style_bullet),
        Paragraph("•  I dati sono raccolti e aggiornati tramite analisi automatica dei record MX", style_bullet),
        Paragraph("•  Il dataset è aperto, verificabile e rilasciato sotto licenza CC BY-SA 4.0", style_bullet),
    ]
    story.append(Spacer(1, 2 * mm))
    story.append(gray_box(box_content))

    # Contesto normativo
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Il contesto normativo", style_h2))
    story.append(Paragraph(
        "Il quadro normativo europeo e italiano impone obblighi precisi sulla "
        "localizzazione e protezione dei dati della PA:",
        style_body
    ))

    # Table
    table_data = [
        [Paragraph("Norma", style_table_header),
         Paragraph("Rilevanza", style_table_header)],
        [Paragraph("GDPR (Reg. UE 2016/679)", style_table_cell_bold),
         Paragraph("Vieta trasferimenti dati verso paesi terzi senza garanzie adeguate", style_table_cell)],
        [Paragraph("Schrems II (CGUE, 2020)", style_table_cell_bold),
         Paragraph("Ha invalidato il Privacy Shield UE-USA", style_table_cell)],
        [Paragraph("CLOUD Act (USA, 2018)", style_table_cell_bold),
         Paragraph("Consente accesso USA a dati di provider americani anche in UE", style_table_cell)],
        [Paragraph("Strategia Cloud Italia (2021)", style_table_cell_bold),
         Paragraph("Classifica i dati PA e prevede migrazione verso infrastrutture qualificate", style_table_cell)],
        [Paragraph("NIS2 (Dir. UE 2022/2555)", style_table_cell_bold),
         Paragraph("Requisiti cybersecurity per PA e soggetti essenziali", style_table_cell)],
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
    # Il costo economico della dipendenza
    story.append(Paragraph("Il costo economico della dipendenza", style_h2))
    story.append(Paragraph(
        "Alla questione giuridica se ne affianca una economica, finora assente "
        "dal dibattito italiano. Due studi della società <b>Asterès</b>, commissionati "
        "dal <b>Cigref</b>, provano a quantificarla a scala europea. Le imprese "
        "dell’Unione acquistano ogni anno <b>264 miliardi di euro</b> di servizi "
        "cloud e software a beneficio dell’economia americana — circa <b>l’1,5% del "
        "PIL dell’Unione</b> e <b>una volta e mezza il bilancio europeo</b>. I fornitori "
        "statunitensi valgono l’<b>83%</b> del mercato europeo del settore. Poiché le "
        "importazioni europee di energia sono valse 360 miliardi nel 2024, la "
        "<b>bolletta digitale dell’Europa è ormai comparabile alla sua bolletta "
        "energetica</b>.",
        style_body
    ))
    story.append(Paragraph(
        "Il secondo studio misura la dinamica dei prezzi: <b>+8,7% annuo</b> negli "
        "ultimi tre anni, <b>+12% atteso</b> nei prossimi cinque, con un aumento "
        "medio del <b>51% al rinnovo di contratto</b> e casi estremi dichiarati fino "
        "al 200-300%. Il sovrapprezzo stimato è di <b>140 miliardi l’anno</b> al 2030, "
        "dei quali <b>93 uscirebbero definitivamente dal continente</b>. Gli aumenti "
        "sono giustificati con funzionalità di intelligenza artificiale <b>imposte "
        "nel 40% dei casi</b>, mentre circa il <b>60%</b> degli intervistati giudica "
        "teorici i relativi guadagni di produttività.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Come vanno letti questi numeri.</b> Non sono misurazioni ma stime "
        "estrapolate da interviste a sei <i>Chief Information Officer</i>, perché i "
        "dati commerciali sono distorti dal peso dell’Irlanda nei flussi; e il "
        "Cigref è parte interessata. Lo studio dichiara metodo e limiti, e vanno "
        "citati per quello che sono. Restano, allo stato, <b>il solo ordine di "
        "grandezza disponibile</b> — e indicano che la dipendenza non è soltanto un "
        "rischio giuridico, ma una <b>voce di spesa crescente e non negoziata</b>.",
        style_body
    ))
    story.append(Spacer(1, 2 * mm))

    story.append(PageBreak())

    # La via d'uscita: certificare l'immunità
    story.append(Paragraph("La via d’uscita: certificare l’immunità", style_h2))
    story.append(Paragraph(
        "La distinzione decisiva è una sola. <b>La residenza del dato e gli impegni "
        "contrattuali non tolgono la giurisdizione</b>: un data center in Italia e "
        "clausole di riservatezza non sottraggono un fornitore statunitense al CLOUD "
        "Act. A determinare la giurisdizione è il <b>controllo societario di chi opera "
        "il servizio</b>. L’unica misura che la rimuove è che il servizio sia operato "
        "da un’entità europea autonoma — e questo è un requisito che si può "
        "<b>certificare</b>.",
        style_body
    ))
    story.append(Paragraph(
        "<b>SecNumCloud 3.2</b> (ANSSI, Francia) è oggi l’unico schema nazionale "
        "europeo che richiede esplicitamente l’<b>immunità dalle legislazioni "
        "extraterritoriali</b> e il <b>controllo europeo del capitale</b>: esclude "
        "quindi in modo strutturale, e non solo contrattuale, l’applicazione del "
        "CLOUD Act. Risultano qualificati <b>OVHcloud</b> e <b>S3NS</b> (Thales, su tecnologia "
        "Google, qualificata il 17 dicembre 2025); <b>Bleu</b> (Orange e Capgemini "
        "su tecnologia Microsoft) è in corso di qualificazione.",
        style_body
    ))
    story.append(Paragraph(
        "La <b>qualificazione italiana</b> dei servizi cloud per la PA <b>non prevede una "
        "clausola equivalente</b>. L’Osservatorio ha esaminato il testo integrale del "
        "<b>Decreto Direttoriale ACN 21007/24</b> — 88 pagine, tutti e quattro gli "
        "allegati: le espressioni «extraterritoriale», «CLOUD Act», «nazionalità», «sede "
        "legale», «capogruppo», «capitale» e «paese terzo» <b>non vi compaiono mai</b>. "
        "Lo schema è costruito su classificazione dei dati, misure di sicurezza e "
        "localizzazione, non sul controllo societario dell’operatore. L’unica "
        "disposizione sul tema, limitata ai dati strategici, impone al fornitore di "
        "<i>segnalare</i> le richieste di accesso provenienti da entità extra-UE: è un "
        "obbligo procedurale che presuppone l’accesso invece di escluderlo, ed è "
        "ineseguibile proprio nel caso per cui è previsto, perché un ordine accompagnato "
        "da <i>gag order</i> vieta al fornitore quella stessa segnalazione.",
        style_body
    ))
    story.append(Paragraph(
        "A livello europeo gli stessi criteri di immunità hanno un nome: <b>«High+»</b>. "
        "Non sono mai stati un livello formale — il Cybersecurity Act ne prevede tre — ma "
        "l’etichetta negoziale dei criteri di immunità, <b>rimossi dallo schema EUCS nel "
        "marzo 2024 e mai reintrodotti</b>. Nel giugno 2026 la Commissione europea "
        "afferma che l’EUCS «non è ancora stato adottato»: nessun atto giuridico, nessun "
        "certificato emesso. La sovranità è riemersa altrove, nei livelli di affidabilità "
        "dell’Unione previsti dalla proposta di <i>Cloud and AI Development Act</i>, il "
        "cui livello più alto riprende in sostanza i requisiti mancati — ma vincola gli "
        "appalti pubblici, non il mercato, ed è ancora una proposta. È uno "
        "schema <b>volontario</b>: non esclude alcun fornitore dal mercato e non impone "
        "nulla agli acquirenti, offre soltanto un’alternativa certificata a chi ne ha "
        "bisogno. L’inclusione dei criteri High+ è stata chiesta da <b>62 "
        "organizzazioni</b>, in un’iniziativa coordinata da Airbus e composta in larga "
        "parte da <b>utenti</b> — banche, assicurazioni, industria della difesa — tra "
        "cui gli italiani <b>Leonardo, Fincantieri, Generali e Telecom Italia</b>. Il "
        "dato rilevante non è un giudizio su quelle imprese: è che <b>la domanda di "
        "immunità esiste e viene dall’industria italiana, mentre manca la risposta "
        "normativa italiana</b>.",
        style_body
    ))
    story.append(Paragraph(
        "Il modello, infine, <b>non richiede di abbandonare i fornitori statunitensi</b> "
        "ed è già realtà. Microsoft opera <i>national cloud</i> separati dove un governo "
        "lo ha preteso: negli Stati Uniti con <b>Microsoft Cloud for US Government</b> e "
        "in Cina, dove la tecnologia è licenziata a <b>21Vianet</b>, che gestisce il "
        "servizio in autonomia — «Microsoft is the technology provider, but Microsoft "
        "doesn’t operate the service». In Francia la stessa impostazione ha prodotto "
        "Bleu e S3NS. Ciò che cambia non è la tecnologia, ma <b>chi opera il servizio</b>.",
        style_body
    ))

    story.append(Spacer(1, 2 * mm))
    box_immunity = [
        Paragraph("Raccomandazioni di policy", style_box_title),
        Paragraph(
            "<b>1.</b>  Introdurre un <b>requisito di immunità dalle legislazioni "
            "extra-UE</b> nello schema di qualificazione italiano dei servizi cloud "
            "per la PA, sul modello di SecNumCloud 3.2.",
            style_bullet
        ),
        Paragraph(
            "<b>2.</b>  Sostenere l’inclusione dei <b>criteri High+ nell’EUCS</b> nelle "
            "sedi europee competenti (ECCG, Commissione europea), esplicitando la "
            "posizione italiana.",
            style_bullet
        ),
        Paragraph(
            "<b>3.</b>  Usare la <b>domanda pubblica come leva</b>: prevedere il "
            "requisito di immunità nelle convenzioni e negli appalti che riguardano "
            "dati critici e strategici.",
            style_bullet
        ),
        Paragraph(
            "<b>4.</b>  <b>Non serve escludere i fornitori statunitensi</b>: serve "
            "richiedere che il servizio sia <b>operato da un’entità europea autonoma</b>.",
            style_bullet
        ),
    ]
    story.append(gray_box(box_immunity))
    story.append(Spacer(1, 3 * mm))

    # Raccomandazioni
    story.append(Paragraph("Raccomandazioni", style_h2))

    recs = [
        ("1. Censimento obbligatorio dei servizi digitali della PA",
         "Rendere obbligatoria la dichiarazione dei servizi digitali utilizzati "
         "da ogni ente e della relativa giurisdizione. Integrare questa informazione "
         "nell’IndicePA per renderla pubblica e monitorabile."),
        ("2. Requisiti di sovranità nelle convenzioni Consip",
         "Inserire criteri di sovranità digitale (giurisdizione dati, localizzazione "
         "server, assenza obblighi verso autorità extra-UE) nelle convenzioni per "
         "servizi email e cloud."),
        ("3. Piano nazionale di migrazione",
         "Definire un piano con scadenze progressive per la migrazione dei servizi "
         "email della PA verso provider conformi. Prevedere fondi dedicati dal PNRR "
         "o dalla cybersecurity."),
        ("4. Monitoraggio continuo e trasparente",
         "Istituzionalizzare il monitoraggio della sovranità digitale della PA "
         "con dati pubblici e aggiornati periodicamente."),
        ("5. Promozione del modello a livello europeo",
         "Proporre nelle sedi europee l’adozione di un framework comune per il "
         "monitoraggio della sovranità digitale delle PA in tutti gli stati membri."),
    ]

    for title, body in recs:
        story.append(Paragraph(title, style_rec_title))
        story.append(Paragraph(body, style_rec_body))

    # Cosa puoi fare (gray box)
    story.append(Spacer(1, 2 * mm))
    box2 = [
        Paragraph("Cosa puoi fare", style_box_title),
        Paragraph(
            "<b>Se sei un parlamentare:</b> Presenta un’interrogazione citando "
            "i dati dell’Osservatorio. Proponi l’inserimento di requisiti di "
            "sovranità nella normativa.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>Se sei un dirigente PA:</b> Verifica la posizione del tuo ente "
            "e avvia una valutazione interna sulla migrazione.",
            style_body_box
        ),
        Spacer(1, 2 * mm),
        Paragraph(
            "<b>Se sei un regolatore:</b> Utilizza i dati per aggiornare le linee "
            "guida e inserire requisiti nelle convenzioni.",
            style_body_box
        ),
    ]
    story.append(gray_box(box2))

    # Fonti e riferimenti
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=BLUE, spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph("Fonti e riferimenti", style_h2))
    refs = [
        "Osservatorio Nazionale Sovranità Digitale: "
        "https://osservatorio.mxmap.it/",
        "MxMap.it — Mappatura provider email PA: https://mxmap.it/",
        "IndicePA — Indice delle Pubbliche Amministrazioni: https://indicepa.gov.it",
        "GDPR: Regolamento UE 2016/679",
        "Sentenza Schrems II: CGUE C-311/18",
    ]
    for ref in refs:
        story.append(Paragraph(f"•  {ref}", style_ref))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.5, color=HexColor("#DEE2E6"),
        spaceAfter=4, spaceBefore=2
    ))
    story.append(Paragraph(
        "Questo documento è rilasciato sotto licenza CC BY-SA 4.0. "
        "Contatti: github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale",
        style_small
    ))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
