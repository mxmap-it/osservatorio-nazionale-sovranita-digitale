# Analisi europee della dipendenza tecnologica/cloud basate su spesa pubblica e procurement

Note di ricerca, 2026-10-27. Legenda: **[V]** = verificato sulla fonte primaria; **[S]** = di seconda mano (stampa, sintesi, comunicato); **[N]** = cercato, non trovato.
Budget di ricerca limitato (~15 chiamate). Molte domande restano aperte; vedi i Gaps.

## 1. Catalogo degli studi basati su spesa e procurement

### Takeaway
Non abbiamo trovato in Europa nessuno studio pubblico che attribuisca la giurisdizione al PRODOTTO letto nella descrizione della gara. Tutti gli studi trovati attribuiscono la nazionalità al vincitore (sede legale) oppure contano le menzioni di vendor nei testi. È proprio il punto debole che il nostro approccio "prodotto, non fornitore" corregge. Lo studio più vicino per metodo è quello del Parlamento europeo (Visionary Analytics, 2025): dati TED, filtro per parole chiave, dizionario delle aziende, ChatGPT e revisione manuale. Però classifica il vincitore, e il suo campione è minuscolo (315 avvisi).

### Cited Findings
**European Parliament / ITRE, "European Software and Cyber Dependencies" (PE 778.576, 2025; autori Visionary Analytics secondo la sintesi ATAG) [V, annesso 1 letto sul PDF]**
- Dati: estratto TED 2020–mid 2025 della sezione "contracts awarded by EU institutions", 13.238 avvisi. Titoli tradotti in inglese con Google Translate. Quindi riguarda solo le istituzioni UE, NON le PA nazionali, anche se il testo parla di "EU public sector". — [EP study PDF, Annex 1](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- Identificazione ICT: niente CPV. Parole chiave sul titolo ("SaaS", "Cloud computing", "Licensed software", "ERP system" ecc.), più un match dei vincitori su una lista curata dei "top 100 global IT and software companies" con nomi normalizzati (minuscole, senza suffissi legali), più una classificazione di pertinenza via ChatGPT API (yes/no/uncertain) con revisione manuale. Risultato: circa 315 avvisi. — [ibid.](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- Multi-aggiudicatario: il 41,5% (162 avvisi) ha più vincitori. Le righe sono state esplose a 778 righe vincitore, duplicando il valore della gara su ogni riga (rischio di doppio conteggio del valore). — [ibid.](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- Giurisdizione: sede (HQ) del vincitore, ricavata dal dizionario delle grandi aziende (che riporta le filiali alla sede della capogruppo) e da ChatGPT per i nomi restanti. Nessun uso di GLEIF/Orbis. — [ibid.](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- Risultati: solo il 59% dei vincitori ha sede nell'UE. Circa l'88% del valore va a consorzi con almeno un'azienda non UE. I vincitori più frequenti sono integratori (Accenture, Deloitte, NTT Data, Atos, PwC), "rather than software vendors". Lo studio stesso nota quindi che il vincitore non è il vendor. — [ibid.](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- Limite dichiarato (sulla parte quote di mercato): i ricavi non separano prezzo e volume, cosa che pesa dove compete il software libero. — [ibid.](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)

**Compass Lexecon per Open Cloud Coalition, "Quantifying EU Public Sector Dependence on Productivity Software" (2025) [S]**
- Fonti: TED, Statista, ecosistema dei partner. Approfondimenti su FR, DE, IT, ES, PL. La "incidence share" di Microsoft nelle menzioni TED è 72–91% nel 2023 e 89–100% nel 2024. La quota di mercato nella produttività per la PA è 73–80% a livello UE. — [OCC press release](https://opencloudcoalition.com/microsoft-dominates-80-of-public-sector-productivity-software-market-in-eu-raising-competition-concerns-according-to-new-report/); [ComputerWeekly](https://www.computerweekly.com/news/366628053/Europe-sleepwalking-into-deeper-dependency-on-Microsoft-cloud-technologies-claims-OCC)
- È basata sulle menzioni del vendor nel testo, non sul vincitore. Per metodo è quindi la più vicina al nostro "prodotto", ma conta citazioni (anche nelle specifiche di compatibilità), non valori. — [Digital Samba blog](https://www.digitalsamba.com/blog/europes-dependency-on-microsoft-a-threat-to-its-digital-sovereignty)
- Conflitto di interessi: OCC è nata con Google tra i membri. Microsoft sostiene che sia finanziata da Google. — [TechCrunch](https://techcrunch.com/2024/10/28/google-backed-open-cloud-coalition-launches-to-lobby-european-lawmakers)
- La definizione di incidence share, la gestione dei reseller e i CPV usati non sono stati verificati: il report primario non è stato trovato **[N]**.

**Tussell (UK) [S]**
- "Tech Titans" (2022, aggiornato 2026): top 150 fornitori tech della PA UK, ricavi, quota e routes-to-market. Metodologia dietro form di download, non letta. — [Tussell](https://www.tussell.com/tech-titans-report)
- "Public Sector Cloud Market Snapshot 2026": Microsoft, AWS e Google, con strategie go-to-market. Contenuti gated. — [Tussell](https://www.tussell.com/public-sector-cloud-market-snapshot-2026)
- La vendita diretta di AWS alla PA UK è stata di £253m nel FY2022/23 (dati Tussell). — [The Register](https://www.theregister.com/2024/02/26/uk_gov_cloud_services/)
- Tussell ha pubblicato anche un report sui fornitori esteri ("Overseas suppliers", 2021), utile come precedente sulla nazionalità del fornitore. — [Tussell](https://tussell.com/overseas-suppliers-report-2021)

**Dati di spesa G-Cloud (CCS, UK) [S]**
- Nel 2021–22 AWS ha incassato £147,8m via G-Cloud, contro £32m di Microsoft in diretta. Molti SI però "funnel" i carichi su Azure/O365: è un esempio esplicito della sottostima dovuta ai reseller. — [The Stack](https://thestack.technology/uk-government-cloud-spend-digital-suppliers)
- La spesa G-Cloud è stata di £2,92bn nei 12 mesi a marzo 2026 (−2,2%). AWS supera di oltre 4x il secondo fornitore. Cresce la spesa verso i value-added reseller. — [TechMarketView](https://www.techmarketview.com/news/archive/2026/09/10/new-research-g-cloud-framework-spending-review-202526)

**Germania: risposte parlamentari (dati di spesa del Bund) [S]**
- La spesa del Bund per Microsoft è passata da €74m (2017) a €198m (2023), oltre metà in licenze. Oracle vale €4,8bn di volume contrattuale, di cui un framework da €4,6bn per maggio 2023–2030. I framework Microsoft valgono €1,3bn. Sono valori massimali (ceiling), non pagato: sono proprio il caso di pitfall. — [Computerwoche](https://www.computerwoche.de/a/bundesregierung-zahlt-milliarden-an-oracle-und-microsoft,3698126); [BT-Drs. 21/5413](https://dserver.bundestag.de/btd/21/054/2105413.pdf); [vergabeblog 2026](https://vergabeblog.de/2026-04-29/bundesverwaltung-details-zu-ausgaben-fuer-softwarelizenzen-im-jahr-2025/)

**Paesi Bassi [S]**
- Un'inchiesta di Binnenlands Bestuur/AD stima in circa €185m la spesa Microsoft dei comuni nel 2025. Il governo dichiara di non poter dare un totale perché la spesa è sparsa su più bilanci. L'analisi NOS sulla dipendenza cloud si basa sui siti web, non su dati di acquisto. — [Binnenlands Bestuur](https://www.binnenlandsbestuur.nl/digitaal/vng-gemeenten-moeten-grote-techleveranciers-afbouwen); [NOS](https://nos.nl/l/2569392)

**Francia [S]**
- Esistono i DECP (dati essenziali della commanda pubblica, consolidati su data.gouv). Un contratto può comparire su più righe (più titolari o modifiche), e ci sono buchi o duplicati in alcuni periodi. — [data.gouv DECP](https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire/informations)
- Solo usi giornalistici puntuali, per esempio €11,8m dei ministeri sociali a Microsoft Ireland. Nessuna analisi sistematica trovata. — [next.ink](https://next.ink/17888/95562-les-ministeres-sociaux-ont-eux-aussi-leur-contrat-open-bar-avec-microsoft/)

**Asterès per Cigref (aprile 2025): solo come riferimento di metodo, NON basato su procurement [S]**
- Stima €264bn l'anno di spesa UE in cloud e software verso gli USA. Il metodo si basa su interviste a 6 CIO: spesa cloud/software pari a ~2,2% del fatturato, 83% verso aziende USA, 80% del valore creato negli USA. I dati di commercio sono scartati per il peso dell'Irlanda. È criticato per la base ristretta. — [Asterès PDF](https://asteres.fr/site/wp-content/uploads/2025/05/Etude-Asteres-La-dependance-technologique-aux-services-de-cloud-et-logiciels-americains-avril-2025.pdf); [Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-le-cigref-evalue-la-dependance-economique-aux-clouds-americains-96746.html)
- Il punto metodologico utile per noi: l'Irlanda è la sede di fatturazione di Microsoft, Google e AWS. Una nazionalità per sede del contraente (per esempio "Microsoft Ireland") classificherebbe il fornitore come UE.

**Menzioni di brand nei bandi (OpenForum Europe 2008–2011, Polonia) [S]**
- OFE 2011: il 13% di un campione di gare IT sulla GUUE cita marchi. Nel 2010, su oltre 400 avvisi IT, la gran parte dei marchi citati è Microsoft. Uno studio della Commissione su 3.616 gare: il 36% di quelle che nominano un produttore nomina Microsoft. — [NetworkWorld](https://www.networkworld.com/article/693058/data-center-governments-illegally-specify-brands-in-it-tenders-study.html); [Computing](https://www.computing.co.uk/news/2077519/source-vendors-unfairly-excluded-government-contracts)
- Polonia: un'analisi di 72 procedure conclude che il 99% esclude di fatto alternative a Microsoft (autore e data non verificati). — [xyz.pl](https://xyz.pl/?p=150073)
- Sono il precedente diretto del riconoscimento del prodotto tramite dizionario di brand nel testo della gara.

**Lock-in accademico [S]**
- Tesi della Charles University (Vozková, 2017) sul lock-in nelle gare ICT ceche: più offerte nel contratto originario sono associate a più lock-in successivo. Campione piccolo. — [dspace.cuni.cz](https://dspace.cuni.cz/handle/20.500.11956/85874)
- DIGIWHIST/opentender.eu (Fazekas, GTI): dati a livello di transazione per 35 giurisdizioni, 2009–2017, con indicatori red-flag. Non abbiamo trovato un'analisi specifica su cloud o vendor lock-in. — [Nottingham PPRG](https://www.nottingham.ac.uk/pprg/events/2018/big-data-in-law-and-economics.aspx); [European Data Portal](https://www.europeandataportal.eu/da/news/new-eu-public-procurement-data-portal)

### Inferences
- Il campo si divide in tre famiglie: (a) nazionalità del vincitore (EP 2025, Tussell); (b) menzioni di vendor o brand nel testo (OCC/Compass Lexecon, OFE); (c) spesa o contratti per vendor da risposte parlamentari (DE, NL). Nessuna combina prodotto → giurisdizione → valore, che è la nostra proposta. Per essere compatibili conviene pubblicare entrambe le viste, per fornitore (come EP/Tussell) e per prodotto, con la matrice di riconciliazione tra le due.
- Il dato EP "59% vincitori UE" e quello OCC "incidence share" non sono confrontabili tra loro né con i nostri. Va detto esplicitamente nel disegno metodologico.

### Gaps
- Testi primari di Tussell (metodologia sui reseller), OCC/Compass Lexecon, Spend Network/Open Opps ([report 2025](https://openopps.com/research/global-digital-tech-procurement-trends-2025/), non letto) e OCP: non letti, o gated.
- Non abbiamo trovato studi su PLACSP (Spagna), UK spend-over-£25k, FSFE "Public Money Public Code" con dati di spesa, EuroStack/Bertelsmann, CISPE, né lavori di UvA, TU Delft, OII o Hertie basati su procurement. Restano da cercare.
- Non abbiamo trovato studi che usino GLEIF o Orbis per le catene di controllo dei fornitori ICT.

## 2. Tassonomie e codici CPV usati per definire ICT e cloud

### Takeaway
Nelle fonti verificate nessuno studio dichiara una lista di CPV: lo studio EP usa solo parole chiave sul titolo. Non abbiamo una lista CPV "di riferimento" da citare. Conviene pubblicare la nostra lista (72xxxxxx, 48xxxxxx, 72317000, 72400000, 30200000 ecc.) con un test di sensibilità.

### Cited Findings
- EP 2025: filtro per parole chiave sul titolo, nessun CPV citato nell'annesso. — [EP study](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)

### Inferences
- Il CPV da solo non distingue il cloud: non esiste un codice SaaS specifico, e 72400000 "servizi Internet" o 48000000 "pacchetti software" mescolano licenze on-prem e cloud. È un argomento a favore della classificazione testuale.

### Gaps
- Le liste CPV di OCC, Tussell e OCP non sono state verificate.

## 3. Mappatura prodotto → vendor tramite descrizioni

### Takeaway
Ci sono solo precedenti parziali: il dizionario di aziende applicato ai nomi dei vincitori (EP 2025) e il conteggio delle menzioni di brand (OFE, OCC). Nessuno pubblica un dizionario prodotto→giurisdizione riutilizzabile. Qui il nostro progetto può contribuire.

### Cited Findings
- EP 2025: dizionario "top 100" più normalizzazione dei nomi e ChatGPT per la sede; risultato rivisto a mano. — [EP study](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- OCC: menzioni del vendor nei testi TED (anche nelle specifiche di compatibilità, quindi non sono vittorie). — [Digital Samba](https://www.digitalsamba.com/blog/europes-dependency-on-microsoft-a-threat-to-its-digital-sovereignty)

### Gaps
- Non abbiamo trovato codice o dataset pubblici per nessuno dei due studi.

## 4. Errori noti (pitfall)

### Takeaway
Le fonti confermano quattro pitfall: (1) i reseller e gli SI nascondono il vendor; (2) i massimali dei framework gonfiano i valori rispetto al pagato; (3) il valore duplicato sui multi-aggiudicatari o sui lotti; (4) le filiali irlandesi rendono "UE" i fornitori USA.

### Cited Findings
- I reseller e gli SI portano i carichi su Azure/O365, quindi la spesa diretta verso Microsoft sottostima la dipendenza. — [The Stack](https://thestack.technology/uk-government-cloud-spend-digital-suppliers)
- Ceiling contro pagato: il framework Oracle del Bund da €4,6bn è un valore di volume contrattuale, mentre la spesa Microsoft effettiva è nell'ordine di €198m l'anno. — [Computerwoche](https://www.computerwoche.de/a/bundesregierung-zahlt-milliarden-an-oracle-und-microsoft,3698126)
- Multi-aggiudicatario: nello studio EP il valore viene ripetuto su ogni riga vincitore. — [EP study](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU(2025)778576_EN.pdf)
- DECP: righe multiple per contratto (titolari, modifiche), buchi e duplicati. — [data.gouv](https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire/informations)
- Irlanda: Asterès scarta i dati di commercio per la distorsione irlandese. Contratti intestati a "Microsoft Ireland". — [Asterès](https://asteres.fr/site/wp-content/uploads/2025/05/Etude-Asteres-La-dependance-technologique-aux-services-de-cloud-et-logiciels-americains-avril-2025.pdf); [next.ink](https://next.ink/17888/95562-les-ministeres-sociaux-ont-eux-aussi-leur-contrat-open-bar-avec-microsoft/)

### Inferences
- Per il nostro disegno conviene: attribuire la giurisdizione all'ultima capogruppo e al prodotto, non al contraente; tenere separate le serie "aggiudicato" (BDNCP) e "pagato" (SIOPE); deduplicare lotti e adesioni ai framework (accordo quadro contro contratto attuativo); mai ripartire il valore in parti uguali tra i vincitori senza dichiararlo.

### Gaps
- Non abbiamo trovato studi che quantifichino lo scarto tra massimale e pagato nell'ICT.
