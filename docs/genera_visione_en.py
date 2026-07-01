"""
Generate the PDF: Strategic Vision of the National Digital Sovereignty Observatory
"""
from fpdf import FPDF
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "Visione_Strategica_Osservatorio_EN.pdf")


class VisionePDF(FPDF):
    BLUE = (0, 102, 178)
    DARK = (33, 37, 41)
    GRAY = (108, 117, 125)
    LIGHT_BG = (240, 243, 246)
    WHITE = (255, 255, 255)
    ACCENT = (0, 128, 83)  # Italian green
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
        self.cell(0, 6, "National Digital Sovereignty Observatory — Strategic Vision", align="L")
        self.cell(0, 6, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.BLUE)
        self.line(10, 14, 200, 14)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 7)
        self.set_text_color(*self.GRAY)
        self.cell(0, 10, "Internal strategy document — June 2025 — CC BY-SA 4.0", align="C")

    def cover_page(self):
        self.add_page()
        self.ln(50)
        self.set_font("DejaVu", "B", 28)
        self.set_text_color(*self.BLUE)
        self.multi_cell(0, 14, "National Digital\nSovereignty Observatory", align="C")
        self.ln(8)
        self.set_draw_color(*self.BLUE)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(10)
        self.set_font("DejaVu", "", 16)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 9, "Strategic Vision, Stakeholders\nand Communication Plan", align="C")
        self.ln(30)
        self.set_font("DejaVu", "", 11)
        self.set_text_color(*self.GRAY)
        self.cell(0, 8, "Version 1.0 — June 2025", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "Edited by Fabio Pietrosanti", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "https://osservatorio.mxmap.it/", align="C", new_x="LMARGIN", new_y="NEXT")

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
        self.cell(0, 6, "  WHO:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {who}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 6, "  WHY IT MATTERS TO THEM:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {why}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.ACCENT)
        self.cell(0, 6, "  WHAT THEY CAN DO:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5, f"  {actions}")

        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*self.WARN)
        self.cell(0, 6, "  HOW TO SPEAK TO THEM:", new_x="LMARGIN", new_y="NEXT")
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

    # ── 1. MISSION ──
    pdf.section_title(1, "Mission and Vision")

    pdf.sub_title("Mission")
    pdf.body(
        "The National Digital Sovereignty Observatory is a civic monitoring project "
        "that measures and monitors the state of digital sovereignty in the Italian "
        "Public Administration, according to technical and analytical criteria, with open data and a transparent methodology."
    )
    pdf.body(
        "The project is at the service of all stakeholders: institutions, politics, industry, "
        "research, civil society and citizens. Civic monitoring is a tool of participatory "
        "democracy that makes visible what would otherwise remain opaque."
    )

    pdf.sub_title("Strategic objectives")
    pdf.numbered(1, "MEASURE — Quantify the dependence of the Italian PA on non-EU digital infrastructure, starting from email services and progressively extending to other critical services.")
    pdf.numbered(2, "RAISE AWARENESS — Disseminate the results to all stakeholders: institutions, political decision-makers, PA, industry, research, civil society. Each actor must understand the problem in their own language and for their own objectives.")
    pdf.numbered(3, "STIMULATE CHANGE — Provide objective data that support informed decisions towards greater digital sovereignty, without ideology but with analytical rigour.")
    pdf.numbered(4, "BUILD COMMUNITY — Create an open community of contributors (technicians, researchers, activists, PA) that feeds and enriches the monitoring over time.")
    pdf.numbered(5, "REPLICATE THE MODEL — Make the methodology and tools available so that other countries can conduct similar analyses (European dimension).")

    pdf.sub_title("Founding principles")
    pdf.bullet("Transparency: open data, documented methodology, open source code")
    pdf.bullet("Rigour: technical-analytical approach, verifiable and replicable")
    pdf.bullet("Independence: no ties to vendors or suppliers")
    pdf.bullet("Inclusiveness: accessible to technical and non-technical audiences, in all EU languages")
    pdf.bullet("Action: oriented towards change, not observation alone")

    # ── 2. STAKEHOLDERS ──
    pdf.section_title(2, "Stakeholder Map")

    pdf.body(
        "The Observatory serves a plurality of actors, each with different motivations, "
        "languages and capacity for action. Communication must be modulated "
        "to speak to each one in their own language and for their own objectives."
    )

    pdf.stakeholder_card(
        "A. National political decision-makers",
        "Members of Parliament (Transport/Telecoms, Defence, Constitutional Affairs Committees), Under-Secretaries with responsibility for innovation, the Presidency of the Council of Ministers (Dept. for Digital Transformation).",
        "Digital sovereignty is a matter of national security. A member of parliament who tables a question or an amendment needs concrete and verifiable data, not opinions. \"73% of PAs use non-EU email providers\" is a sentence that can be quoted in the chamber.",
        "Parliamentary questions, bills, amendments, committee hearings citing the Observatory's data.",
        "A 1-page executive summary with 3-5 key figures and a policy recommendation. The dataset is not needed — what is needed is the sentence to say in committee."
    )

    pdf.stakeholder_card(
        "B. Authorities and regulators",
        "AgID, ACN (National Cybersecurity Agency), the Data Protection Authority (Garante), ANAC, Consip.",
        "AgID defines the IT guidelines for the PA — the Observatory measures the effectiveness of their policies. ACN has a mandate on the security of digital infrastructure (CLOUD Act, jurisdictional risk). The Garante monitors non-EU data transfers (post Schrems II). Consip manages IT purchasing framework agreements.",
        "Issue recommendations, update guidelines, introduce sovereignty requirements into Consip framework agreements, launch GDPR compliance checks.",
        "A detailed technical report with rigorous methodology. These organisations have internal research offices — they want to be able to verify the data. Methodological credibility is essential."
    )

    pdf.stakeholder_card(
        "C. PA managers and IT officers",
        "CIOs / Heads of Information Systems of Municipalities, Regions, local health authorities, Universities, Ministries, social security bodies (~23,000 bodies within the IndicePA perimeter).",
        "They are the ones who chose (or inherited) the email provider. Many do not know they are on a non-EU provider because the contract goes through an Italian reseller. The Observatory provides a mirror: \"Your body uses Google Workspace — here is what that means in terms of jurisdiction over the data.\"",
        "Launch migration to sovereign providers, request funds for the transition, justify IT investments citing their position in the report.",
        "A dashboard that can be consulted for a single body (\"find your body\"). A defensive motivation: if an article comes out about the PA using Gmail, the councillor will ask for an explanation. They need to be able to position themselves and compare with similar bodies."
    )

    pdf.stakeholder_card(
        "D. Italian and European providers",
        "Aruba, Register.it, Infocert, TIM, OVHcloud, Ionos, Proton, Infomaniak, and other European email/cloud suppliers.",
        "The Observatory quantifies the potential migration market. If 60% of PAs use non-EU providers, it is an enormous addressable market. The data demonstrate that a problem exists — and they are the solution.",
        "Cite the data in commercial proposals to the PA, sponsor or support the project, develop specific offerings for migration, informed lobbying with concrete data.",
        "Market data: how many bodies, of what size, on which current provider. Not the rhetoric of sovereignty — the numbers of the business opportunity."
    )

    pdf.stakeholder_card(
        "E. Journalists and media",
        "Cybersecurity journalists (Cybersecurity360, CorCom, Agenda Digitale, Key4biz) and generalists (Sole 24 Ore, Repubblica, Wired Italia, RAI).",
        "Data generates headlines. \"73% of Italian Municipalities entrust their email to US Big Tech\" writes itself. The journalist needs verifiable figures and a citable source.",
        "Articles, investigations, TV features. Every publication amplifies the project and puts pressure on decision-makers.",
        "A press kit with ready-to-use infographics, 3 key figures, an available author quote. The journalist has 2 hours to write — if you give them everything ready, they write it."
    )

    pdf.stakeholder_card(
        "F. Academia and research",
        "Lecturers and researchers in IT law, cybersecurity, political science, public administration. PhD students and undergraduate dissertations.",
        "Open dataset, documented methodology, topical subject. For a researcher it is gold: real, up-to-date data with which to publish papers. For a student it is a ready-made dissertation.",
        "Academic publications that lend authority to the project, in-depth analyses of subsets, predictive models, international comparisons.",
        "An API or downloadable dataset, detailed methodological documentation, an open licence. Cite \"data usable for academic research\"."
    )

    pdf.stakeholder_card(
        "G. Civil society and digital activism",
        "Hermes Center, Transparency International Italia, Italian Linux Society, digital civic networks, open source and privacy activists.",
        "Digital sovereignty is a matter of fundamental rights. The Observatory transforms an abstract topic (\"technological dependence\") into concrete data useful for advocacy campaigns.",
        "Public campaigns, informed petitions, participation in public consultations citing the data, pressure on local administrators.",
        "Strong, shareable messages, infographics for social media, kits for local activists (\"take this data to your municipal council\")."
    )

    pdf.stakeholder_card(
        "H. European institutions",
        "European Commission (DG CONNECT, DG DIGIT), ENISA, European Parliament (ITRE Committee), EU Cybersecurity Competence Centre.",
        "Italy would be the first country to systematically measure the digital sovereignty of the PA in an open way. The model is replicable in every member state. The Commission is pushing on digital sovereignty (Chips Act, Data Act, EUCS) but lacks granular data.",
        "Cite Italy as a case study, fund the extension to other countries, include similar metrics in evaluation criteria.",
        "In English, with a European framing (\"EU digital sovereignty assessment model\"). Positioned as a replicable best practice — which is why the site is multilingual."
    )

    pdf.stakeholder_card(
        "I. Local administrators",
        "Mayors, Innovation councillors, Regional Presidents, Directors-General of local bodies.",
        "If their Municipality is at the bottom of the digital sovereignty ranking, someone will point it out. If it is at the top, it is a merit to communicate. Competition between bodies is a very powerful lever.",
        "Municipal resolutions for migration, allocation of local funds, adhesion to Consip framework agreements for sovereign services, local political communication.",
        "A ranking by territory (region, province), comparison with comparable bodies. \"Your Municipality is 847th out of 7,904 for digital sovereignty\" is a message that moves a councillor."
    )

    # ── 3. SITE ARCHITECTURE ──
    pdf.section_title(3, "Website Architecture")

    pdf.body(
        "The site must speak to all the identified stakeholders, with content modulated "
        "by profile. The architecture provides for cross-cutting sections and dedicated sections."
    )

    pdf.sub_title("Existing sections (already implemented)")
    pdf.bullet("Home — Hero, latest reports, latest news, link to MxMap.it")
    pdf.bullet("Reports — List of reports with PDF download")
    pdf.bullet("News — Updates and press releases")
    pdf.bullet("Presentations — Slides and materials presented at conferences")
    pdf.bullet("Methodology — Description of the technical approach and data sources")
    pdf.bullet("FAQ — Frequently asked questions with a Bootstrap Italia accordion")
    pdf.bullet("Get Involved — 7 ways to contribute + Telegram channel")
    pdf.bullet("About us — Information on the team and the project")

    pdf.sub_title("New sections to be implemented")

    pdf.sub2_title("3.1 For Decision-makers (new section)")
    pdf.body(
        "A page dedicated to institutional and political decision makers. It contains:"
    )
    pdf.bullet("An executive summary with 5 key figures displayed with large cards")
    pdf.bullet("Numbered and concrete policy recommendations")
    pdf.bullet("A \"What you can do\" section differentiated by role (member of parliament, PA manager, regulator)")
    pdf.bullet("Download of the Policy Brief in PDF (2 pages)")
    pdf.bullet("Regulatory references (GDPR, Schrems II, CLOUD Act, Italy's Cloud Strategy)")

    pdf.sub2_title("3.2 Open Data (new section)")
    pdf.body(
        "A page for researchers and analysts with access to the raw data:"
    )
    pdf.bullet("Downloadable dataset in CSV/JSON format")
    pdf.bullet("API documentation (when available)")
    pdf.bullet("Data dictionary with a description of each field")
    pdf.bullet("Usage examples and a suggested academic citation")
    pdf.bullet("Explicit licence for academic and commercial reuse (CC BY-SA 4.0)")

    pdf.sub2_title("3.3 Press Kit (new section)")
    pdf.body(
        "A page for journalists and communicators:"
    )
    pdf.bullet("3-5 key figures in citable format")
    pdf.bullet("Downloadable infographics (high-resolution PNG + SVG)")
    pdf.bullet("Press releases")
    pdf.bullet("Bio and photo of the author / spokesperson")
    pdf.bullet("Dedicated press contact")

    pdf.sub2_title("3.4 Find your Body (new section / MxMap integration)")
    pdf.body(
        "A search function for a single PA body:"
    )
    pdf.bullet("Search by body name, IPA code, municipality, region")
    pdf.bullet("Body profile with current email provider, sovereignty classification")
    pdf.bullet("Positioning relative to comparable bodies (benchmark)")
    pdf.bullet("Temporal evolution (when historical data is available)")
    pdf.body("Note: this feature requires integration with MxMap.it data and may need a dynamic component (an API or static pre-rendering for each body).")

    pdf.sub2_title("3.5 Stakeholders and Impact (new section)")
    pdf.body(
        "A page that makes explicit the mission of dissemination to all stakeholders:"
    )
    pdf.bullet("A visual map of the stakeholders and their role")
    pdf.bullet("For each one: why the project is relevant and what they can do")
    pdf.bullet("Testimonials and endorsements (when available)")
    pdf.bullet("Measured impact: citations, articles, parliamentary questions, migrations launched")

    pdf.sub2_title("3.6 Expansion of existing sections")
    pdf.bullet("About us — Add the mission of dissemination to all stakeholders, the vision of civic monitoring as a public service")
    pdf.bullet("Methodology — Add a section on the international replicability of the model")
    pdf.bullet("FAQ — Add questions for non-technical stakeholders (\"Why should I care?\", \"What can I do as a citizen?\")")
    pdf.bullet("Get Involved — Add specific calls-to-action for each type of stakeholder")

    # ── 4. DOCUMENTS ──
    pdf.section_title(4, "Documents to be Produced")

    pdf.body(
        "Each document is designed for one or more specific stakeholders. "
        "All documents will be produced in draft for review before publication."
    )

    pdf.sub_title("4.1 Policy Brief (2 pages)")
    pdf.info_box("Recipients: Members of Parliament, ministerial managers, regulators",
                 "Executive summary with 5 key figures, regulatory context (GDPR, Schrems II, CLOUD Act, Italy's Cloud Strategy), 3 concrete and actionable policy recommendations. Format: A4 PDF, printable, with institutional graphics.")

    pdf.sub_title("4.2 Technical Brief (4-6 pages)")
    pdf.info_box("Recipients: AgID, ACN, the Data Protection Authority, research offices",
                 "Detailed methodology, data sources (IndicePA, DNS, MX records), provider classification criteria, limits of the analysis, comparison with international standards. Methodological rigour is the priority.")

    pdf.sub_title("4.3 Business Case for Migration (2-3 pages)")
    pdf.info_box("Recipients: Italian/European providers, Consip, PA CIOs",
                 "Market size (no. of bodies on non-EU providers by type), estimated migration costs, benefits (compliance, security, local economy), a typical roadmap for the migration of an average body.")

    pdf.sub_title("4.4 Press Kit")
    pdf.info_box("Recipients: Journalists, media, communicators",
                 "Project sheet (1 page), 3-5 key figures with source, 2-3 high-resolution infographics (PNG + SVG), launch press release, spokesperson bio and contacts, FAQ for journalists.")

    pdf.sub_title("4.5 Kit for Activists and Civil Society")
    pdf.info_box("Recipients: Associations, activists, civic networks",
                 "A \"Take this data to your Municipal Council\" guide (how to use the data for local interpellations), a template letter to the councillor, social-ready infographics (Instagram/Twitter format), talking points for public events.")

    pdf.sub_title("4.6 Sheet for Researchers")
    pdf.info_box("Recipients: Academics, PhD students, students",
                 "Dataset description, data dictionary, suggested BibTeX citation, examples of research questions, links to publications that use the data, a contact for academic collaborations.")

    pdf.sub_title("4.7 EU Briefing (in English)")
    pdf.info_box("Recipients: European Commission, ENISA, European Parliament",
                 "Positioning as the \"first EU-wide replicable model for PA digital sovereignty assessment\". Key Italian metrics as a case study, a proposal to extend to other member states, alignment with EU Digital Decade targets.")

    pdf.sub_title("4.8 Slide Deck Presentation")
    pdf.info_box("Recipients: Conferences (Forum PA, ITASEC, Cybertech), hearings",
                 "15-20 slides with: the problem, key data, methodology, main results, recommendations, call to action. IT and EN versions. A format usable both in person and remotely.")

    # ── 5. DISSEMINATION PLAN ──
    pdf.section_title(5, "Dissemination Plan")

    pdf.sub_title("5.1 Communication channels")

    pdf.sub2_title("Digital channels")
    pdf.bullet("Website (central hub for all content)")
    pdf.bullet("Telegram channel (real-time updates, community)")
    pdf.bullet("GitHub (code, data, issue tracking, contributions)")
    pdf.bullet("Social media: LinkedIn (decision-makers, professionals), Twitter/X (tech community, journalists)")
    pdf.bullet("Periodic newsletter (for those who want updates without social media)")
    pdf.bullet("RSS Feed (already implemented)")

    pdf.sub2_title("Institutional channels")
    pdf.bullet("Forum PA (annual conference — presentation of data)")
    pdf.bullet("ITASEC (Italian cybersecurity conference)")
    pdf.bullet("Cybertech Europe (Rome — international audience)")
    pdf.bullet("Parliamentary hearings (by invitation, supported by the Policy Brief)")
    pdf.bullet("AgID/ACN public consultations (participation with data)")
    pdf.bullet("Academic conferences (peer-reviewed papers)")

    pdf.sub2_title("Media outreach")
    pdf.bullet("Distribution of the Press Kit to sector journalists (Cybersecurity360, CorCom, Key4biz, Agenda Digitale)")
    pdf.bullet("Op-eds / opinion articles in generalist outlets (Sole 24 Ore, Domani, Wired)")
    pdf.bullet("Radio/TV interviews (RAI Radio1 / TG Leonardo on tech topics)")

    pdf.sub_title("5.2 Strategy by stakeholder")

    pdf.body("Each stakeholder is reached with the right content, in the right format, on the right channel:")
    pdf.ln(2)

    # Simple text-based table
    rows = [
        ("Stakeholder", "Key document", "Main channel", "Frequency"),
        ("Members of Parliament", "Policy Brief", "Hearings, direct email", "With each report"),
        ("AgID / ACN", "Technical Brief", "Consultations, meetings", "Half-yearly"),
        ("Data Protection Authority", "Technical Brief", "Formal reports", "Ad hoc"),
        ("PA CIOs", "Find your Body", "Website, LinkedIn", "Ongoing"),
        ("IT/EU providers", "Business Case", "Conferences, LinkedIn", "Annual"),
        ("Journalists", "Press Kit", "Email, press conferences", "With each report"),
        ("Academics", "Dataset + Sheet", "Website, conferences", "Ongoing"),
        ("Civil society", "Activist Kit", "Telegram, social, events", "Ongoing"),
        ("EU institutions", "EU Briefing (EN)", "EU conferences, email", "Annual"),
        ("Local admins.", "Find your Body", "LinkedIn, local press", "With each report"),
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
    pdf.section_title(6, "Implementation Roadmap")

    pdf.sub_title("Phase 1 — Foundations (completed)")
    pdf.bullet("Website with Hugo + Bootstrap Italia + GitHub Pages")
    pdf.bullet("Base sections: Home, Reports, News, Presentations, Methodology, FAQ, Get Involved, About us")
    pdf.bullet("Multilingual infrastructure (24 EU languages)")
    pdf.bullet("CI/CD with GitHub Actions")
    pdf.bullet("MxMap.it data integration")

    pdf.sub_title("Phase 2 — Strategic content (in progress)")
    pdf.bullet("New site sections: For Decision-makers, Open Data, Press Kit, Stakeholders and Impact")
    pdf.bullet("Document production: Policy Brief, Technical Brief, Press Kit")
    pdf.bullet("Expansion of About us with the dissemination mission")
    pdf.bullet("Expanded FAQ for non-technical stakeholders")

    pdf.sub_title("Phase 3 — Dissemination")
    pdf.bullet("Launch of press kit and media outreach")
    pdf.bullet("Presentation at Forum PA / ITASEC")
    pdf.bullet("Direct contact with AgID, ACN")
    pdf.bullet("Publication of the EU Briefing in English")
    pdf.bullet("Opening of social channels (LinkedIn, Twitter/X)")

    pdf.sub_title("Phase 4 — Scale")
    pdf.bullet("\"Find your Body\" feature (requires data integration)")
    pdf.bullet("Interactive dashboard with data visualisations")
    pdf.bullet("Translation of the main content into English")
    pdf.bullet("First peer-reviewed academic paper")
    pdf.bullet("Proposal to replicate the model in other EU countries")

    # ── 7. TODO LIST ──
    pdf.section_title(7, "Todo List — Documents in Draft")

    pdf.body(
        "List of the deliverables to be produced in draft. Each document will be submitted "
        "for review before publication. The priority indicates the suggested order of production."
    )
    pdf.ln(2)

    todos = [
        ("P1", "Policy Brief (IT)", "2-page PDF", "MPs, managers", "To be produced"),
        ("P1", "'For Decision-makers' section", "Web page", "Decision makers", "To be produced"),
        ("P1", "'Stakeholders and Impact' section", "Web page", "All", "To be produced"),
        ("P1", "Expansion of 'About us'", "Web page", "All", "To be produced"),
        ("P1", "Base Press Kit", "Web + PDF", "Journalists", "To be produced"),
        ("P2", "Technical Brief", "4-6 page PDF", "AgID, ACN, Garante", "To be produced"),
        ("P2", "'Open Data' section", "Web page", "Researchers", "To be produced"),
        ("P2", "'Press Kit' section", "Web page", "Media", "To be produced"),
        ("P2", "Expanded FAQ", "Web page", "Non-technical", "To be produced"),
        ("P2", "Migration Business Case", "2-3 page PDF", "Providers, Consip", "To be produced"),
        ("P3", "Activist Kit", "Web + PDF", "Civil society", "To be produced"),
        ("P3", "Researcher Sheet", "Web + PDF", "Academics", "To be produced"),
        ("P3", "EU Briefing (EN)", "2-page PDF", "EU institutions", "To be produced"),
        ("P3", "Slide Deck", "15-20 slides", "Conferences", "To be produced"),
        ("P3", "Expanded Get Involved", "Web page", "By stakeholder", "To be produced"),
    ]

    # Header
    pdf.set_font("DejaVu", "B", 8)
    pdf.set_fill_color(*pdf.BLUE)
    pdf.set_text_color(*pdf.WHITE)
    hw = [12, 52, 28, 48, 25]
    hdr = ("Prior.", "Document", "Format", "Recipients", "Status")
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
    pdf.multi_cell(0, 5, "P1 = High priority (produce immediately)  |  P2 = Medium priority  |  P3 = Later priority")

    pdf.output(OUTPUT)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
