# Studi europei su spesa/procurement e contatti verificati (sovranità digitale)

Ricerca del 2026-10-27. Tag: [P] = fonte primaria (sito/documento dell'autore), [S] = fonte secondaria (stampa/aggregatore). "NON VERIFICATO" = non aperto in questa sessione (memoria o snippet di ricerca), da controllare prima di scrivere. Solo canali pubblici e istituzionali.

## Parte A: quali studi basati su spesa/procurement esistono e con che metodo?

### Takeaway
L'unico studio pubblico trovato che misura direttamente la dipendenza della PA UE dai dati di procurement (TED) è quello di Compass Lexecon per l'Open Cloud Coalition (luglio 2025). È metodologicamente debole: incidenza delle menzioni nei bandi, nessun CPV pubblicato, committente legato a Google. Lo studio ITRE del PE (dicembre 2025) è una sintesi di quote di mercato, non un'analisi della spesa. La maggior parte degli altri "indici" (EDRIX, Nextcloud DSI, Bonn DDI) misura infrastruttura o commercio, non la spesa della PA. L'approccio dell'Osservatorio (spesa ANAC/OCDS classificata per giurisdizione del prodotto) sembra quindi non avere un equivalente diretto.

### Cited Findings
**Compass Lexecon / Open Cloud Coalition, "Quantifying EU Public Sector Dependence on Productivity Software" (24/07/2025)**
- Commissionato dall'OCC e redatto da Compass Lexecon, senza autori individuali indicati. Copre l'UE più FR, DE, IT, ES e PL, con dati da TED, Statista e "other public sources". Risultati: quota di Microsoft nella productivity software al 73–80% UE e 77% nei 5 Stati; fino al 92% in collaboration/office suite; quota di incidenza nei bandi TED al 72–91% (2023) e 89–100% (2024). I meccanismi indicati sono acquisti ripetuti, requisiti di compatibilità e bundling. Il comunicato non dice nulla su CPV o parole chiave usate. — [P] [Comunicato OCC](https://opencloudcoalition.com/microsoft-dominates-80-of-public-sector-productivity-software-market-in-eu-raising-competition-concerns-according-to-new-report/); report: https://opencloudcoalition.com/quantifying-eu-public-sector-dependence-on-productivity-software/ (non aperto)
- Il report ha 36 pagine e si basa su 189 bandi TED che menzionano Microsoft. — [S] [Computer Weekly](https://www.computerweekly.com/news/366628053/Europe-sleepwalking-into-deeper-dependency-on-Microsoft-cloud-technologies-claims-OCC)
- Microsoft accusa l'OCC di essere una campagna "astroturf" organizzata da Google. — [S] [TechCrunch](https://techcrunch.com/2024/10/28/microsoft-accuses-google-of-shadow-campaign-to-influence-cloud-regulation-in-europe)
- Il caso UK è documentato: OCC alla CMA nell'indagine SMS su Microsoft business software. — [P] [OCC submission CMA](https://assets.publishing.service.gov.uk/media/6a3a4060e590e5e061c9a485/Open_Cloud_Coalition.pdf)

**Parlamento europeo, ITRE, "European Software and Cyber Dependencies", PE 778.576 (dicembre 2025)**
- Autori: Vaida Gineikyte-Kanclere, Militsa Eggert e Goda Skiotyte (Visionary Analytics). Advisory board: Paul Timmers e Roxana Radu. Amministratrice responsabile: Anne Plöger. Contatto: ecti-poldep-b@europarl.europa.eu. — [P] [PDF PE](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU%282025%29778576_EN.pdf)
- Il metodo è desk research con interviste, senza analisi di dati di procurement. I numeri sono di seconda mano: circa 80% della spesa corporate in cloud e software verso fornitori USA, "digital bill" di 264 mld €/anno (solo imprese), hyperscaler USA al 70% circa. Tra le leve proposte: open standards, multisourcing e clausole "Buy European" negli acquisti IT pubblici. — [P] stesso PDF

**CISPE / Frédéric Jenny (2023)**
- Stima i sovraccosti di licenza Microsoft per chi usa cloud non-Azure in circa 1,01 mld € nel 2022 (SQL Server), più circa 560 mln €/anno con lo stesso metodo applicato a Office 365. Copre settore pubblico e privato, con un metodo basato sui prezzi di licenza, non sul procurement. Dopo il settlement (somme riportate in modo diverso dalle fonti, 20 o 30 mln €) Microsoft è entrata in CISPE. — [S] [itassetmanagement](https://itassetmanagement.net/?p=37690), [The Register](https://www.theregister.com/2025/01/21/microsoft_joins_cispe/)

**IT vendor lock-in nel procurement svizzero (Univ. Berna)**
- 2.754 progetti IT da simap.ch su 7 anni. Il 47,2% sopra soglia WTO è stato assegnato senza gara; gli autori propongono un metodo per misurare il lock-in. — [S/P] [BORIS Bern](https://boris.unibe.ch/114065), [ITU DK](https://pure.itu.dk/en/publications/when-the-exception-becomes-the-norm-direct-awards-to-it-vendors-b/). Autori: NON VERIFICATO (in memoria: Matthias Stürmer et al.).

**Indici non basati sulla spesa (utili per triangolare)**
- EDRIX: punteggio 0–10 su 5 pilastri (policy OSS da OSOR, sviluppatori GitHub e directory EuroStack, quota browser/Linux, sovranità web/mail/DNS di domini privati e di istituzioni chiave). Non tratta di procurement. — [P] [edrix.eu metodologia](https://edrix.eu/en/methodology), [linuxfr](https://linuxfr.org/news/lancement-de-l-edrix-un-indice-pour-mesurer-la-souverainete-numerique-europeenne)
- Nextcloud DSI: conta istanze Shodan di circa 50 tool self-hosted ogni 100k abitanti, normalizzate 0–100. Codice e dati su github.com/nextcloud/Digital-Sovereignty-Index. — [P] [dsi.nextcloud.com](https://dsi.nextcloud.com/)
- Bonn DDI 2.0 (CASSIS e Vodafone Institute): 51 paesi su hardware, software, piattaforme e IP; il DDI 1.0 copriva 23 paesi. Metodologia nel PDF del 2022. — [P] [CASSIS DDI 2.0](https://www.cassis.uni-bonn.de/en/research/interdisciplinary-research-initiatives/politics-and-governance-of-global-infrastructures/research-projects/digital-dependence-index-2.0), [PDF metodo](https://www.cassis.uni-bonn.de/medien/forschungsprojekte/ddi/ddi_methodology.pdf)
- Famiglia MxMap (provider email dei comuni): CH (frozen aprile 2026, successore SecAssure2026 DACH), BE, DE, EU, FR, IT, LV, NL, NO, PT, SE, UK. "CAmap" è **CAmap Nordic & Baltic**, che mappa la sovranità delle certificate authority TLS (koldex.github.io/ca-sovereignty-map, pagina in 404 al momento del controllo); non riguarda il Canada. — [P] [README mxmap](https://github.com/davidhuser/mxmap)

### Inferences
- Il metodo Compass Lexecon (conteggio delle menzioni di marchio nei bandi TED) è il punto di confronto più vicino. Il nostro approccio (importi aggiudicati, prodotto distinto dal fornitore, giurisdizione) è più fine. Conviene chiedere a OCC e Compass Lexecon la lista dei 189 bandi e le query usate.
- Lo studio ITRE non contiene dati di spesa della PA: un nostro dato italiano colmerebbe un vuoto che lo studio stesso segnala.

### Gaps
- PDF Compass Lexecon non aperto: mancano CPV, parole chiave e definizione di "incidence share".
- Non ho trovato in questa sessione studi su tech/cloud procurement di OCP, Spend Network/Open Opps o GTI/opentender: lacuna di ricerca, non prova di assenza.
- Non verificati in questa sessione: FSFE PMPC (publiccode.eu ha restituito una pagina vuota), OpenForum Europe, SWP, Bruegel, CEPS, ECFR, Institut Delors, Asterès (studio Cigref/Asterès sul "coût de la dépendance"), metodo Synergy Research, audit di Algemene Rekenkamer e Cour des comptes.

## Parte B: contatti pubblici verificati

### Takeaway
Ho verificato canali ufficiali per 15 soggetti. Per gli altri riporto solo indicazioni non verificate, oppure nulla.

### Cited Findings
| Soggetto | Canale pubblico | Persona nominata | Stato |
|---|---|---|---|
| Open Contracting Partnership | engage@open-contracting.org; data@ (OCDS); media@ | Georg Neumann, Head of Communications | [P] [contact](https://www.open-contracting.org/contact/) |
| Spend Network / Open Opps | contact@spendnetwork.com (uffici a Sheffield e Tallinn) | non indicata | [P] [contact](https://www.spendnetwork.com/contact) |
| Tussell | contact@tussell.com; press: henry.thompson@tussell.com | Henry Thompson, Press Officer | [P] [contact](https://www.tussell.com/contact) |
| Government Transparency Institute | info@govtransparency.eu | M. Fazekas (direttore, da [RUSI](https://rusi.org/people/fazekas) [S]) | [P] [home](https://www.govtransparency.eu/) |
| OpenForum Europe | info@openforumeurope.org, +32 2 446 21 94 | non indicata | [P] [contact](https://openforumeurope.org/contact/) |
| CISPE | solo moduli: /general-inquiries/, /contact-for-media-inquiries/; pagina /secretariat | non indicata | [P] [general inquiries](https://www.cispe.cloud/general-inquiries/) |
| Interface (ex SNV) | /press-enquires; esperti con email pubblica, es. sherpig@interface-eu.org (Sven Herpig) | nessun lead su procurement/cloud | [P] [home](https://www.interface-eu.org/) |
| Cigref | cigref@cigref.fr, +33 1 56 59 70 00 | non indicata | [P] [contact](https://www.cigref.fr/contact) |
| EFK/CDF (Svizzera) | info@efk.admin.ch; media: kommunikation@efk.admin.ch | non indicata | [P] [contact](https://www.efk.admin.ch/en/contact/) |
| Bertelsmann reframe[Tech] | pagina progetto (nessuna email nella pagina) | Dr. Kirsten Witte (Director); Dr. Felix Sieker e altri PM | [P] [progetto](https://www.bertelsmann-stiftung.de/en/our-projects/reframetech-algorithms-for-the-common-good) |
| EuroStack (eurostack.eu) | solo /join-us/; Bria e Timmers non nominati nella home | non indicata | [P] [eurostack.eu](https://eurostack.eu/) |
| EDRIX | nessuna email; rimanda a eurostack.eu | Stéfane Fermigier (Abilian, CNLL, APELL) | [P] [about](https://edrix.eu/en/about) |
| Nextcloud DSI | modulo "Contribute"; issue su GitHub nextcloud/Digital-Sovereignty-Index | non indicata | [P] [DSI](https://dsi.nextcloud.com/) |
| Univ. Bonn DDI | cassis@uni-bonn.de; maximilian.mayer@uni-bonn.de; yenchilu@uni-bonn.de | Maximilian Mayer, Yen-Chi Lu (+4) | [P] [CASSIS](https://www.cassis.uni-bonn.de/en/research/interdisciplinary-research-initiatives/politics-and-governance-of-global-infrastructures/research-projects/digital-dependence-index-2.0) |
| Studio ITRE PE 778.576 | ecti-poldep-b@europarl.europa.eu | Anne Plöger (admin); autori Visionary Analytics | [P] [PDF](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU%282025%29778576_EN.pdf) |
| David Huser (MxMap) | issue sul repo GitHub davidhuser/mxmap; progetto successore SecAssure2026 | David Huser ([LinkedIn](https://ch.linkedin.com/in/davidhuser) [S]) | [P] [repo](https://github.com/davidhuser/mxmap) |
| Open Cloud Coalition / Compass Lexecon | https://opencloudcoalition.com/contact-us/ | Nicky Stewart, Senior Advisor OCC (citata nel comunicato) | [P] [comunicato](https://opencloudcoalition.com/microsoft-dominates-80-of-public-sector-productivity-software-market-in-eu-raising-competition-concerns-according-to-new-report/) |

### Inferences
- I canali migliori per allineare i metodi su dati di procurement sono OCP (data@ per OCDS), GTI (info@), Spend Network e OCC/Compass Lexecon (per i 189 bandi TED).

### Gaps (NON VERIFICATO: aprire prima di scrivere)
- FSFE: fsfe.org/contact ha risposto 403. In memoria: contact@fsfe.org, NON VERIFICATO.
- SWP, CEPS, Bruegel, ECFR, Institut Delors, Asterès, Algemene Rekenkamer (la pagina tentata era in 404), Cour des comptes: non aperti.
- Francesca Bria e Paul Timmers: nessun contatto pubblico trovato sui siti EuroStack/Bertelsmann. Timmers figura nell'advisory board dello studio ITRE.
- CAmap Nordic & Baltic: autore (account GitHub "koldex") e contatto non verificati, pagina in 404.
- Synergy Research: metodo non verificato.
- Compass Lexecon: nessun autore individuale nominato.
