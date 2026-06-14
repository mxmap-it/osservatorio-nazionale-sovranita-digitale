"""
Genera il PDF: Visione Strategica dell'Osservatorio Nazionale Sovranità Digitale
"""
from fpdf import FPDF
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "Visione_Strategica_Osservatorio.pdf")


class VisionePDF(FPDF):
    BLUE = (0, 102, 178)
    DARK = (33, 37, 41)
    GRAY = (108, 117, 125)
    LIGHT_BG = (240, 243, 246)
    WHITE = (255, 255, 255)
    ACCENT = (0, 128, 83)  # verde Italia
    WARN = (204, 102, 0)

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=25)
        self.add_font("DejaVu", "", r"C:\Windows\Fonts\arial.ttf")
        self.add_font("DejaVu", "B", r"C:\Windows\Fonts\arialbd.ttf")
        self.add_font("DejaVu", "I", r"C:\Windows\Fonts\ariali.ttf")

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(*self.GRAY)
        self.cell(0, 6, "Osservatorio Nazionale Sovranità Digitale — Visione Strategica", align="L")
        self.cell(0, 6, f"Pagina {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.BLUE)
        self.line(10, 14, 200, 14)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 7)
        self.set_text_color(*self.GRAY)
        self.cell(0, 10, "Documento strategico interno — Giugno 2025 — CC BY-SA 4.0", align="C")

    def cover_page(self):
        self.add_page()
        self.ln(50)
        self.set_font("DejaVu", "B", 28)
        self.set_text_color(*self.BLUE)
        self.multi_cell(0, 14, "Osservatorio Nazionale\nSovranità Digitale", align="C")
        self.ln(8)
        self.set_draw_color(*self.BLUE)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(10)
        self.set_font("DejaVu", "", 16)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 9, "Visione Strategica, Stakeholder\ne Piano di Comunicazione", align="C")
        self.ln(30)
        self.set_font("DejaVu", "", 11)
        self.set_text_color(*self.GRAY)
        self.cell(0, 8, "Versione 1.0 — Giugno 2025", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "A cura di Fabio Pietrosanti", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "https://fpietrosanti.github.io/osservatorio-nazionale-sovranita-digitale/", align="C", new_x="LMARGIN", new_y="NEXT")

    def section_title(self, n, title):
        self.add_page()
        self.ln(5)
        self.set_font("DejaVu", "B", 20)
        self.set_text_color(*self.BLUE)
        self.cell(0, 12, f"{n}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.BLUE)
        self.line(10, self.get_y() + 1, 200, self.get_y() + 1)
        self.ln(6)

    def sub_title(self, title):
        self.ln(3)
        self.set_font("DejaVu", "B", 13)
        self.set_text_color(*self.DARK)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def sub2_title(self, title):
        self.ln(2)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body(self, text):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def body_bold(self, text):
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*self.DARK)
        x0 = self.get_x()
        self.cell(6, 5.5, "•")
        w = self.w - self.r_margin - self.get_x()
        self.multi_cell(w, 5.5, text)
        self.set_x(x0)

    def numbered(self, n, text):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*self.DARK)
        x0 = self.get_x()
        self.cell(8, 5.5, f"{n}.")
        w = self.w - self.r_margin - self.get_x()
        self.multi_cell(w, 5.5, text)
        self.set_x(x0)

    def info_box(self, title, text):
        self.ln(2)
        y0 = self.get_y()
        self.set_fill_color(*self.LIGHT_BG)
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(*self.BLUE)
        self.cell(0, 7, f"  {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {text}", fill=True)
        self.ln(3)

    def stakeholder_card(self, name, who, why, actions, how):
        self.ln(3)
        self.set_fill_color(*self.LIGHT_BG)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*self.BLUE)
        self.cell(0, 8, f"  {name}", fill=True, new_x="LMARGIN", new_y="NEXT")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 6, "  CHI:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {who}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 6, "  PERCHÉ GLI INTERESSA:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {why}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 6, "  COSA POSSONO FARE:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {actions}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.WARN)
        self.cell(0, 6, "  COME PARLARGLI:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {how}")
        self.ln(2)

    def table_row(self, cols, widths, bold=False, fill=False):
        self.set_font("DejaVu", "B" if bold else "", 9)
        if fill:
            self.set_fill_color(*self.LIGHT_BG)
        h = 6
        x0 = self.get_x()
        max_h = h
        # Calculate multi-cell heights
        cell_texts = []
        for i, (col, w) in enumerate(zip(cols, widths)):
            cell_texts.append(col)
        y0 = self.get_y()
        heights = []
        for i, (col, w) in enumerate(zip(cols, widths)):
            self.set_xy(x0 + sum(widths[:i]), y0)
            ncell = self.multi_cell(w, h, col, border=1, fill=fill, split_only=True)
            heights.append(len(ncell) * h)
        max_h = max(heights) if heights else h

        for i, (col, w) in enumerate(zip(cols, widths)):
            self.set_xy(x0 + sum(widths[:i]), y0)
            self.multi_cell(w, h, col, border=1, fill=fill, max_line_height=h)
            # Fill remaining space if shorter
        self.set_xy(x0, y0 + max_h)


def build():
    pdf = VisionePDF()

    # ── COVER ──
    pdf.cover_page()

    # ── 1. MISSIONE ──
    pdf.section_title(1, "Missione e Visione")

    pdf.sub_title("Missione")
    pdf.body(
        "L'Osservatorio Nazionale Sovranità Digitale è un progetto di monitoraggio civico "
        "che misura e monitora lo stato della sovranità digitale nella Pubblica Amministrazione "
        "italiana, secondo criteri tecnici e analitici, con dati aperti e metodologia trasparente."
    )
    pdf.body(
        "Il progetto è al servizio di tutti gli stakeholder: istituzioni, politica, industria, "
        "ricerca, società civile e cittadini. Il monitoraggio civico è uno strumento di democrazia "
        "partecipativa che rende visibile ciò che altrimenti resterebbe opaco."
    )

    pdf.sub_title("Obiettivi strategici")
    pdf.numbered(1, "MISURARE — Quantificare la dipendenza della PA italiana da infrastrutture digitali extra-UE, partendo dai servizi email e estendendo progressivamente ad altri servizi critici.")
    pdf.numbered(2, "RENDERE CONSAPEVOLI — Diffondere i risultati a tutti gli stakeholder: istituzioni, decisori politici, PA, industria, ricerca, società civile. Ogni soggetto deve comprendere il problema nella propria lingua e per i propri obiettivi.")
    pdf.numbered(3, "STIMOLARE IL CAMBIAMENTO — Fornire dati oggettivi che supportino decisioni informate verso una maggiore sovranità digitale, senza ideologia ma con rigore analitico.")
    pdf.numbered(4, "COSTRUIRE COMUNITÀ — Creare una comunità aperta di contributori (tecnici, ricercatori, attivisti, PA) che alimenti e arricchisca il monitoraggio nel tempo.")
    pdf.numbered(5, "REPLICARE IL MODELLO — Rendere la metodologia e gli strumenti disponibili affinché altri paesi possano condurre analisi analoghe (dimensione europea).")

    pdf.sub_title("Principi fondanti")
    pdf.bullet("Trasparenza: dati aperti, metodologia documentata, codice open source")
    pdf.bullet("Rigore: approccio tecnico-analitico, verificabile e replicabile")
    pdf.bullet("Indipendenza: nessun legame con vendor o fornitori")
    pdf.bullet("Inclusività: accessibile a tecnici e non tecnici, in tutte le lingue UE")
    pdf.bullet("Azione: orientato al cambiamento, non alla sola osservazione")

    # ── 2. STAKEHOLDER ──
    pdf.section_title(2, "Mappa degli Stakeholder")

    pdf.body(
        "L'Osservatorio serve una pluralità di soggetti, ciascuno con motivazioni, "
        "linguaggi e capacità di azione diverse. La comunicazione deve essere modulata "
        "per parlare a ciascuno nella propria lingua e per i propri obiettivi."
    )

    pdf.stakeholder_card(
        "A. Decisori politici nazionali",
        "Parlamentari (Comm. Trasporti/TLC, Difesa, Affari Costituzionali), Sottosegretari con delega innovazione, Presidenza del Consiglio (Dip. Trasformazione Digitale).",
        "La sovranità digitale è tema di sicurezza nazionale. Un parlamentare che presenta un'interrogazione o un emendamento ha bisogno di dati concreti e verificabili, non di opinioni. \"Il 73% delle PA usa provider email extra-UE\" è una frase che si cita in aula.",
        "Interrogazioni parlamentari, proposte di legge, emendamenti, audizioni in commissione citando i dati dell'Osservatorio.",
        "Sintesi esecutiva di 1 pagina con 3-5 numeri chiave e una raccomandazione di policy. Non serve il dataset — serve la frase da dire in commissione."
    )

    pdf.stakeholder_card(
        "B. Autorità e regolatori",
        "AgID, ACN (Agenzia Cybersicurezza Nazionale), Garante Privacy, ANAC, Consip.",
        "AgID definisce le linee guida IT per la PA — l'Osservatorio misura l'efficacia delle loro policy. ACN ha mandato sulla sicurezza delle infrastrutture digitali (CLOUD Act, rischio giurisdizionale). Il Garante monitora i trasferimenti dati extra-UE (post Schrems II). Consip gestisce le convenzioni di acquisto IT.",
        "Emanare raccomandazioni, aggiornare linee guida, inserire requisiti di sovranità nelle convenzioni Consip, avviare verifiche di conformità GDPR.",
        "Report tecnico dettagliato con metodologia rigorosa. Queste organizzazioni hanno uffici studi interni — vogliono poter verificare i dati. La credibilità metodologica è fondamentale."
    )

    pdf.stakeholder_card(
        "C. Dirigenti e responsabili IT della PA",
        "CIO / Responsabili Sistemi Informativi di Comuni, Regioni, ASL, Università, Ministeri, Enti previdenziali (~23.000 enti nel perimetro IndicePA).",
        "Sono quelli che hanno scelto (o ereditato) il provider email. Molti non sanno di essere su un provider extra-UE perché il contratto passa attraverso un rivenditore italiano. L'Osservatorio fornisce uno specchio: \"Il tuo ente usa Google Workspace — ecco cosa significa in termini di giurisdizione sui dati.\"",
        "Avviare migrazione verso provider sovrani, richiedere fondi per la transizione, giustificare investimenti IT citando il posizionamento nel report.",
        "Dashboard consultabile per singolo ente (\"cerca il tuo ente\"). Motivazione difensiva: se esce un articolo sulla PA che usa Gmail, l'assessore chiederà conto. Devono potersi posizionare e confrontare con enti simili."
    )

    pdf.stakeholder_card(
        "D. Provider italiani ed europei",
        "Aruba, Register.it, Infocert, TIM, OVHcloud, Ionos, Proton, Infomaniak, e altri fornitori europei di email/cloud.",
        "L'Osservatorio quantifica il mercato potenziale della migrazione. Se il 60% delle PA usa provider extra-UE, è un mercato indirizzabile enorme. I dati dimostrano che esiste un problema — e loro sono la soluzione.",
        "Citare i dati nelle proposte commerciali alla PA, sponsorizzare o supportare il progetto, sviluppare offerte specifiche per la migrazione, lobby informata con dati concreti.",
        "Dati di mercato: quanti enti, di che dimensione, su quale provider attuale. Non la retorica della sovranità — i numeri del business opportunity."
    )

    pdf.stakeholder_card(
        "E. Giornalisti e media",
        "Giornalisti cybersecurity (Cybersecurity360, CorCom, Agenda Digitale, Key4biz) e generalisti (Sole 24 Ore, Repubblica, Wired Italia, RAI).",
        "I dati generano titoli. \"Il 73% dei Comuni italiani affida le email a Big Tech USA\" si scrive da solo. Il giornalista ha bisogno di numeri verificabili e di una fonte citabile.",
        "Articoli, inchieste, servizi TV. Ogni pubblicazione amplifica il progetto e mette pressione sui decisori.",
        "Press kit con infografiche pronte all'uso, 3 numeri chiave, citazione dell'autore disponibile. Il giornalista ha 2 ore per scrivere — se gli dai tutto pronto, lo scrive."
    )

    pdf.stakeholder_card(
        "F. Mondo accademico e ricerca",
        "Docenti e ricercatori di diritto dell'informatica, cybersecurity, scienze politiche, pubblica amministrazione. Studenti di dottorato e tesi di laurea.",
        "Dataset aperto, metodologia documentata, tema attuale. Per un ricercatore è oro: dati reali, aggiornati, con cui pubblicare paper. Per uno studente è una tesi pronta.",
        "Pubblicazioni accademiche che danno autorevolezza al progetto, analisi approfondite su sottoinsiemi, modelli predittivi, confronti internazionali.",
        "API o dataset scaricabile, documentazione metodologica dettagliata, licenza aperta. Citare \"dati utilizzabili per ricerca accademica\"."
    )

    pdf.stakeholder_card(
        "G. Società civile e attivismo digitale",
        "Hermes Center, Transparency International Italia, Italian Linux Society, reti civiche digitali, attivisti open source e privacy.",
        "La sovranità digitale è un tema di diritti fondamentali. L'Osservatorio trasforma un tema astratto (\"dipendenza tecnologica\") in dati concreti utili per campagne di advocacy.",
        "Campagne pubbliche, petizioni informate, partecipazione a consultazioni pubbliche citando i dati, pressione su amministratori locali.",
        "Messaggi forti e condivisibili, infografiche per social media, kit per attivisti locali (\"porta questi dati al tuo consiglio comunale\")."
    )

    pdf.stakeholder_card(
        "H. Istituzioni europee",
        "Commissione Europea (DG CONNECT, DG DIGIT), ENISA, Parlamento Europeo (Comm. ITRE), EU Cybersecurity Competence Centre.",
        "L'Italia sarebbe il primo paese a misurare sistematicamente la sovranità digitale della PA in modo aperto. Il modello è replicabile in ogni stato membro. La Commissione spinge su sovranità digitale (Chips Act, Data Act, EUCS) ma manca di dati granulari.",
        "Citare l'Italia come caso studio, finanziare l'estensione ad altri paesi, includere metriche simili nei criteri di valutazione.",
        "In inglese, con framing europeo (\"EU digital sovereignty assessment model\"). Posizionato come best practice replicabile — motivo per cui il sito è multilingue."
    )

    pdf.stakeholder_card(
        "I. Amministratori locali",
        "Sindaci, Assessori all'innovazione, Presidenti di Regione, Direttori generali enti locali.",
        "Se il loro Comune è in fondo alla classifica di sovranità digitale, qualcuno glielo farà notare. Se è in cima, è un merito da comunicare. La competizione tra enti è una leva potentissima.",
        "Delibere comunali per la migrazione, stanziamento fondi locali, adesione a convenzioni Consip per servizi sovrani, comunicazione politica locale.",
        "Ranking per territorio (regione, provincia), confronto con enti omologhi. \"Il tuo Comune è 847° su 7.904 per sovranità digitale\" è un messaggio che muove un assessore."
    )

    # ── 3. ARCHITETTURA DEL SITO ──
    pdf.section_title(3, "Architettura del Sito Web")

    pdf.body(
        "Il sito deve parlare a tutti gli stakeholder identificati, con contenuti modulati "
        "per profilo. L'architettura prevede sezioni trasversali e sezioni dedicate."
    )

    pdf.sub_title("Sezioni esistenti (già implementate)")
    pdf.bullet("Home — Hero, ultimi report, ultime news, collegamento MxMap.it")
    pdf.bullet("Report — Elenco report con download PDF")
    pdf.bullet("News — Aggiornamenti e comunicati")
    pdf.bullet("Presentazioni — Slide e materiali presentati a conferenze")
    pdf.bullet("Metodologia — Descrizione approccio tecnico e fonti dati")
    pdf.bullet("FAQ — Domande frequenti con accordion Bootstrap Italia")
    pdf.bullet("Partecipa — 7 modalità di contribuzione + canale Telegram")
    pdf.bullet("Chi Siamo — Informazioni sul team e sul progetto")

    pdf.sub_title("Nuove sezioni da implementare")

    pdf.sub2_title("3.1 Per i Decisori (nuova sezione)")
    pdf.body(
        "Pagina dedicata ai decision maker istituzionali e politici. Contiene:"
    )
    pdf.bullet("Executive summary con 5 numeri chiave visualizzati con card grandi")
    pdf.bullet("Raccomandazioni di policy numerate e concrete")
    pdf.bullet("Sezione \"Cosa puoi fare\" differenziata per ruolo (parlamentare, dirigente PA, regolatore)")
    pdf.bullet("Download del Policy Brief in PDF (2 pagine)")
    pdf.bullet("Riferimenti normativi (GDPR, Schrems II, CLOUD Act, Strategia Cloud Italia)")

    pdf.sub2_title("3.2 Dati Aperti (nuova sezione)")
    pdf.body(
        "Pagina per ricercatori e analisti con accesso ai dati grezzi:"
    )
    pdf.bullet("Dataset scaricabile in formato CSV/JSON")
    pdf.bullet("Documentazione API (quando disponibile)")
    pdf.bullet("Dizionario dati con descrizione di ogni campo")
    pdf.bullet("Esempi di utilizzo e citazione accademica suggerita")
    pdf.bullet("Licenza esplicita per riuso accademico e commerciale (CC BY-SA 4.0)")

    pdf.sub2_title("3.3 Press Kit (nuova sezione)")
    pdf.body(
        "Pagina per giornalisti e comunicatori:"
    )
    pdf.bullet("3-5 numeri chiave in formato citabile")
    pdf.bullet("Infografiche scaricabili (PNG alta risoluzione + SVG)")
    pdf.bullet("Comunicati stampa")
    pdf.bullet("Bio e foto dell'autore / portavoce")
    pdf.bullet("Contatto stampa dedicato")

    pdf.sub2_title("3.4 Cerca il tuo Ente (nuova sezione / integrazione MxMap)")
    pdf.body(
        "Funzionalità di ricerca per singolo ente PA:"
    )
    pdf.bullet("Ricerca per nome ente, codice IPA, comune, regione")
    pdf.bullet("Scheda ente con provider email attuale, classificazione sovranità")
    pdf.bullet("Posizionamento rispetto a enti omologhi (benchmark)")
    pdf.bullet("Evoluzione temporale (quando disponibili dati storici)")
    pdf.body("Nota: questa funzionalità richiede integrazione con i dati MxMap.it e potrebbe necessitare di un componente dinamico (API o pre-rendering statico per ogni ente).")

    pdf.sub2_title("3.5 Stakeholder e Impatto (nuova sezione)")
    pdf.body(
        "Pagina che esplicita la missione di diffusione a tutti gli stakeholder:"
    )
    pdf.bullet("Mappa visiva degli stakeholder e del loro ruolo")
    pdf.bullet("Per ciascuno: perché il progetto è rilevante e cosa possono fare")
    pdf.bullet("Testimonianze e endorsement (quando disponibili)")
    pdf.bullet("Impatto misurato: citazioni, articoli, interrogazioni, migrazioni avviate")

    pdf.sub2_title("3.6 Espansione sezioni esistenti")
    pdf.bullet("Chi Siamo — Aggiungere missione di diffusione a tutti gli stakeholder, visione di monitoraggio civico come servizio pubblico")
    pdf.bullet("Metodologia — Aggiungere sezione sulla replicabilità internazionale del modello")
    pdf.bullet("FAQ — Aggiungere domande per stakeholder non tecnici (\"Perché dovrebbe interessarmi?\", \"Cosa posso fare come cittadino?\")")
    pdf.bullet("Partecipa — Aggiungere call-to-action specifiche per tipo di stakeholder")

    # ── 4. DOCUMENTI ──
    pdf.section_title(4, "Documenti da Produrre")

    pdf.body(
        "Ogni documento è pensato per uno o più stakeholder specifici. "
        "Tutti i documenti saranno prodotti in bozza per revisione prima della pubblicazione."
    )

    pdf.sub_title("4.1 Policy Brief (2 pagine)")
    pdf.info_box("Destinatari: Parlamentari, dirigenti ministeriali, regolatori",
                 "Sintesi esecutiva con 5 numeri chiave, contesto normativo (GDPR, Schrems II, CLOUD Act, Strategia Cloud Italia), 3 raccomandazioni di policy concrete e attuabili. Formato: PDF A4, stampabile, con grafica istituzionale.")

    pdf.sub_title("4.2 Technical Brief (4-6 pagine)")
    pdf.info_box("Destinatari: AgID, ACN, Garante Privacy, uffici studi",
                 "Metodologia dettagliata, fonti dati (IndicePA, DNS, MX records), criteri di classificazione dei provider, limiti dell'analisi, confronto con standard internazionali. Rigore metodologico è la priorità.")

    pdf.sub_title("4.3 Business Case per la Migrazione (2-3 pagine)")
    pdf.info_box("Destinatari: Provider italiani/europei, Consip, CIO della PA",
                 "Dimensione del mercato (n. enti su provider extra-UE per tipologia), costi stimati della migrazione, benefici (compliance, sicurezza, economia locale), roadmap tipo per la migrazione di un ente medio.")

    pdf.sub_title("4.4 Press Kit")
    pdf.info_box("Destinatari: Giornalisti, media, comunicatori",
                 "Scheda progetto (1 pagina), 3-5 numeri chiave con fonte, 2-3 infografiche in alta risoluzione (PNG + SVG), comunicato stampa di lancio, bio e contatti portavoce, FAQ per giornalisti.")

    pdf.sub_title("4.5 Kit per Attivisti e Società Civile")
    pdf.info_box("Destinatari: Associazioni, attivisti, reti civiche",
                 "Guida \"Porta questi dati al tuo Consiglio Comunale\" (come usare i dati per interpellanze locali), template di lettera all'assessore, infografiche social-ready (formato Instagram/Twitter), talking points per eventi pubblici.")

    pdf.sub_title("4.6 Scheda per Ricercatori")
    pdf.info_box("Destinatari: Accademici, dottorandi, studenti",
                 "Descrizione dataset, dizionario dati, citazione BibTeX suggerita, esempi di domande di ricerca, link a pubblicazioni che usano i dati, contatto per collaborazioni accademiche.")

    pdf.sub_title("4.7 EU Briefing (in inglese)")
    pdf.info_box("Destinatari: Commissione Europea, ENISA, Parlamento Europeo",
                 "Posizionamento come \"first EU-wide replicable model for PA digital sovereignty assessment\". Metriche chiave italiane come caso studio, proposta di estensione ad altri stati membri, allineamento con EU Digital Decade targets.")

    pdf.sub_title("4.8 Presentazione Slide Deck")
    pdf.info_box("Destinatari: Conferenze (Forum PA, ITASEC, Cybertech), audizioni",
                 "15-20 slide con: problema, dati chiave, metodologia, risultati principali, raccomandazioni, call to action. Versione IT e EN. Formato utilizzabile sia in presenza che da remoto.")

    # ── 5. PIANO DI DIFFUSIONE ──
    pdf.section_title(5, "Piano di Diffusione")

    pdf.sub_title("5.1 Canali di comunicazione")

    pdf.sub2_title("Canali digitali")
    pdf.bullet("Sito web (hub centrale di tutti i contenuti)")
    pdf.bullet("Canale Telegram (aggiornamenti in tempo reale, community)")
    pdf.bullet("GitHub (codice, dati, issue tracking, contribuzioni)")
    pdf.bullet("Social media: LinkedIn (decisori, professionisti), Twitter/X (community tech, giornalisti)")
    pdf.bullet("Newsletter periodica (per chi vuole aggiornamenti senza social)")
    pdf.bullet("RSS Feed (già implementato)")

    pdf.sub2_title("Canali istituzionali")
    pdf.bullet("Forum PA (conferenza annuale — presentazione dati)")
    pdf.bullet("ITASEC (conferenza italiana cybersecurity)")
    pdf.bullet("Cybertech Europe (Roma — platea internazionale)")
    pdf.bullet("Audizioni parlamentari (su invito, supportate dal Policy Brief)")
    pdf.bullet("Consultazioni pubbliche AgID/ACN (partecipazione con dati)")
    pdf.bullet("Convegni accademici (paper peer-reviewed)")

    pdf.sub2_title("Media outreach")
    pdf.bullet("Distribuzione Press Kit a giornalisti di settore (Cybersecurity360, CorCom, Key4biz, Agenda Digitale)")
    pdf.bullet("Op-ed / articoli di opinione su testate generaliste (Sole 24 Ore, Domani, Wired)")
    pdf.bullet("Interviste radio/TV (RAI Radio1 / TG Leonardo su temi tech)")

    pdf.sub_title("5.2 Strategia per stakeholder")

    pdf.body("Ogni stakeholder viene raggiunto con il contenuto giusto, nel formato giusto, nel canale giusto:")
    pdf.ln(2)

    # Simple text-based table
    rows = [
        ("Stakeholder", "Documento chiave", "Canale principale", "Frequenza"),
        ("Parlamentari", "Policy Brief", "Audizioni, email diretta", "Ad ogni report"),
        ("AgID / ACN", "Technical Brief", "Consultazioni, meeting", "Semestrale"),
        ("Garante Privacy", "Technical Brief", "Segnalazioni formali", "Ad hoc"),
        ("CIO della PA", "Cerca il tuo Ente", "Sito web, LinkedIn", "Continuo"),
        ("Provider IT/EU", "Business Case", "Conferenze, LinkedIn", "Annuale"),
        ("Giornalisti", "Press Kit", "Email, conferenze stampa", "Ad ogni report"),
        ("Accademici", "Dataset + Scheda", "Sito web, convegni", "Continuo"),
        ("Società civile", "Kit Attivisti", "Telegram, social, eventi", "Continuo"),
        ("Istituzioni EU", "EU Briefing (EN)", "Conferenze EU, email", "Annuale"),
        ("Amm. locali", "Cerca il tuo Ente", "LinkedIn, stampa locale", "Ad ogni report"),
    ]

    for i, row in enumerate(rows):
        if i == 0:
            pdf.set_font("DejaVu", "B", 8)
            pdf.set_fill_color(*pdf.BLUE)
            pdf.set_text_color(*pdf.WHITE)
        else:
            pdf.set_font("DejaVu", "", 8)
            pdf.set_text_color(*pdf.DARK)
            if i % 2 == 0:
                pdf.set_fill_color(*pdf.LIGHT_BG)
            else:
                pdf.set_fill_color(*pdf.WHITE)

        w = [42, 38, 55, 55]
        y0 = pdf.get_y()
        x0 = pdf.get_x()
        for j, (col, cw) in enumerate(zip(row, w)):
            pdf.set_xy(x0 + sum(w[:j]), y0)
            pdf.cell(cw, 7, f" {col}", border=1, fill=True)
        pdf.set_xy(x0, y0 + 7)

    pdf.set_text_color(*pdf.DARK)

    # ── 6. ROADMAP ──
    pdf.section_title(6, "Roadmap Implementativa")

    pdf.sub_title("Fase 1 — Fondamenta (completata)")
    pdf.bullet("Sito web con Hugo + Bootstrap Italia + GitHub Pages")
    pdf.bullet("Sezioni base: Home, Report, News, Presentazioni, Metodologia, FAQ, Partecipa, Chi Siamo")
    pdf.bullet("Infrastruttura multilingue (24 lingue UE)")
    pdf.bullet("CI/CD con GitHub Actions")
    pdf.bullet("Integrazione dati MxMap.it")

    pdf.sub_title("Fase 2 — Contenuti strategici (in corso)")
    pdf.bullet("Nuove sezioni sito: Per i Decisori, Dati Aperti, Press Kit, Stakeholder e Impatto")
    pdf.bullet("Produzione documenti: Policy Brief, Technical Brief, Press Kit")
    pdf.bullet("Espansione Chi Siamo con missione di diffusione")
    pdf.bullet("FAQ ampliate per stakeholder non tecnici")

    pdf.sub_title("Fase 3 — Diffusione")
    pdf.bullet("Lancio press kit e outreach media")
    pdf.bullet("Presentazione a Forum PA / ITASEC")
    pdf.bullet("Contatto diretto con AgID, ACN")
    pdf.bullet("Pubblicazione EU Briefing in inglese")
    pdf.bullet("Apertura canali social (LinkedIn, Twitter/X)")

    pdf.sub_title("Fase 4 — Scala")
    pdf.bullet("Funzionalità \"Cerca il tuo Ente\" (richiede integrazione dati)")
    pdf.bullet("Dashboard interattiva con visualizzazioni dati")
    pdf.bullet("Traduzioni contenuti principali in inglese")
    pdf.bullet("Primo paper accademico peer-reviewed")
    pdf.bullet("Proposta di replica del modello in altri paesi EU")

    # ── 7. TODO LIST ──
    pdf.section_title(7, "Todo List — Documenti in Bozza")

    pdf.body(
        "Elenco dei deliverable da produrre in bozza. Ogni documento sarà sottoposto "
        "a revisione prima della pubblicazione. La priorità indica l'ordine di produzione suggerito."
    )
    pdf.ln(2)

    todos = [
        ("P1", "Policy Brief (IT)", "2 pag. PDF", "Parlamentari, dirigenti", "Da produrre"),
        ("P1", "Sezione 'Per i Decisori'", "Pagina web", "Decision maker", "Da produrre"),
        ("P1", "Sezione 'Stakeholder e Impatto'", "Pagina web", "Tutti", "Da produrre"),
        ("P1", "Espansione 'Chi Siamo'", "Pagina web", "Tutti", "Da produrre"),
        ("P1", "Press Kit base", "Web + PDF", "Giornalisti", "Da produrre"),
        ("P2", "Technical Brief", "4-6 pag. PDF", "AgID, ACN, Garante", "Da produrre"),
        ("P2", "Sezione 'Dati Aperti'", "Pagina web", "Ricercatori", "Da produrre"),
        ("P2", "Sezione 'Press Kit'", "Pagina web", "Media", "Da produrre"),
        ("P2", "FAQ ampliate", "Pagina web", "Non tecnici", "Da produrre"),
        ("P2", "Business Case migrazione", "2-3 pag. PDF", "Provider, Consip", "Da produrre"),
        ("P3", "Kit Attivisti", "Web + PDF", "Società civile", "Da produrre"),
        ("P3", "Scheda Ricercatori", "Web + PDF", "Accademici", "Da produrre"),
        ("P3", "EU Briefing (EN)", "2 pag. PDF", "Istituzioni EU", "Da produrre"),
        ("P3", "Slide Deck", "15-20 slide", "Conferenze", "Da produrre"),
        ("P3", "Partecipa ampliata", "Pagina web", "Per stakeholder", "Da produrre"),
    ]

    # Header
    pdf.set_font("DejaVu", "B", 8)
    pdf.set_fill_color(*pdf.BLUE)
    pdf.set_text_color(*pdf.WHITE)
    hw = [12, 52, 28, 48, 25]
    hdr = ("Prior.", "Documento", "Formato", "Destinatari", "Stato")
    y0 = pdf.get_y()
    x0 = pdf.get_x()
    for j, (col, cw) in enumerate(zip(hdr, hw)):
        pdf.set_xy(x0 + sum(hw[:j]), y0)
        pdf.cell(cw, 7, f" {col}", border=1, fill=True)
    pdf.set_xy(x0, y0 + 7)

    for i, row in enumerate(todos):
        pdf.set_font("DejaVu", "", 7)
        pdf.set_text_color(*pdf.DARK)
        if i % 2 == 0:
            pdf.set_fill_color(*pdf.LIGHT_BG)
        else:
            pdf.set_fill_color(*pdf.WHITE)
        y0 = pdf.get_y()
        x0 = pdf.get_x()
        for j, (col, cw) in enumerate(zip(row, hw)):
            pdf.set_xy(x0 + sum(hw[:j]), y0)
            pdf.cell(cw, 6, f" {col}", border=1, fill=True)
        pdf.set_xy(x0, y0 + 6)

    pdf.set_text_color(*pdf.DARK)
    pdf.ln(8)
    pdf.set_font("DejaVu", "I", 9)
    pdf.set_text_color(*pdf.GRAY)
    pdf.multi_cell(0, 5, "P1 = Priorità alta (produrre subito)  |  P2 = Priorità media  |  P3 = Priorità successiva")

    pdf.output(OUTPUT)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
