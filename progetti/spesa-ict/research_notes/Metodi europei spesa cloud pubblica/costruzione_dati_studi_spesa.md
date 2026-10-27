# Come sono stati costruiti i dati degli studi europei sulla spesa pubblica cloud/big tech

Ricerca del 27/10/2026. Integra `reports/Misure europee sovranità digitale.md` senza ripeterlo.

- **[P]** = letto in questa sessione sul documento primario (PDF scaricato e cercato nel testo).
- **[S]** = di seconda mano.
- **N/D** = non disponibile, con il motivo.

## Executive summary

1. **PE 778.576: l'Annex 1 TED esiste [P].** Delle due note in conflitto aveva ragione quella che descriveva l'annesso; quella "solo desk research" era sbagliata. Ci sono però due avvertenze nuove:
   - l'annesso dichiara come fonte la sezione TED dei *contratti aggiudicati dalle istituzioni UE*, mentre il testo principale (p. 60) presenta il risultato come TED delle PA di tutti gli Stati membri. È un'ambiguità interna al documento;
   - l'88% del valore a consorzi con almeno un membro extra-UE si basa su righe in cui il valore della gara è duplicato su ogni vincitore.
2. **Compass Lexecon/OCC: il report integrale è aperto [P].** Conferma che misura le *menzioni* nel CPV 48000000, non la spesa. Per l'Italia i numeri sono minimi: 5 avvisi nel 2024 (100% Microsoft) e 18 nel 2023 (72%). Il "100% Italia" non va citato come misura.
3. **Il "Data dive" di Computer Weekly (Adshead, 2/6/2026) è uno studio DNS/RDAP su 29 enti, non un'analisi di spesa Tussell [P].**
   - Le cifre di £17,7 mld, del 55% "a hyperscaler o rivenditori" e degli oltre 1.100 enti, che il report precedente attribuiva all'articolo, non compaiono nel testo primario.
   - Le riporta The Next Web, accostandole all'articolo senza indicarne la fonte.
   - Vanno ritirate o marcate "fonte ignota". Il metodo dell'articolo è di fatto vicino a MxMap.
4. **Assemblée nationale, rapporto n. 3054, t. I [P].**
   - I 115 M€ Microsoft vengono da questionari alle amministrazioni, non da dati di appalto.
   - Gli 1,5 mld € sono un'estrapolazione: top 50 fornitori UGAP 2025 con nazionalità verificata a mano (79% USA, almeno 609 M€), divisi per una quota di mercato UGAP stimata al 40%.
5. **Cour des comptes, 22/10/2026 [P].**
   - I 100 M€ sono crediti di pagamento ricostruiti da questionari a 11 ministeri e includono licenze, prestazioni e personale.
   - I 130 M€ sono un costo evitato rispetto a MS365/Bleu su 860.000 postazioni, non un risparmio misurato.
   - A parte, la Corte stima 30–65 M€ di risparmio con software libero on-premises.
6. **BT-Drs. 21/5413 [P].**
   - Gli Anlagen 1–4 sono tabelle dentro il PDF: contratti quadro, contratti singoli, filiali, contratti quadro BeschA.
   - Per ogni contratto danno ente, controparte, oggetto, volume, durata e importo richiamato nel 2025.
   - Si possono usare solo dopo una pulizia manuale, perché l'estrazione testuale sfasa le colonne.
   - Il governo avverte che il volume dei contratti quadro è un tetto.
7. **Nessuno studio pubblica un dataset riutilizzabile, il codice, una licenza o un canale formale per estensioni nazionali.** L'unico con un perimetro multi-paese che include l'Italia (OCC) è stato commissionato da una parte interessata.

## 1. PE 778.576 "European Software and Cyber Dependencies" (Visionary Analytics per ITRE, dicembre 2025)

Fonte: [PDF](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU%282025%29778576_EN.pdf). L'URL con le parentesi non codificate risponde 403 (blocco CloudFront); quello con `%28 %29` funziona. Tutto ciò che segue è **[P]**.

- **Struttura.**
  - Annex 1: "TED data analysis", pp. 175–179.
  - Annex 2: elenco degli intervistati.
  - Annex 3: stime di quote di mercato (desk research, Synergy e altri).
  - Annex 4: iniziative nazionali di cloud sovrano.
- **Fonte e finestra.**
  - Estratto TED dalla "publicly available section on contracts awarded by EU institutions", 2020–2025, **13.238 avvisi**.
  - Nel testo principale (p. 60) il periodo è "2020 to mid-2025" e la nota 168 descrive TED come avvisi "from public sector bodies across all EU Member States".
  - Il perimetro effettivo (sole istituzioni UE o tutte le PA) resta quindi ambiguo nel documento. L'annesso indica le istituzioni UE.
- **Unità di analisi.** L'avviso, poi esploso in una riga per vincitore.
- **Valore.**
  - "Financial value of the awarded contract, as reported by the contracting authority", cioè l'aggiudicato, più la valuta.
  - Per i framework non è specificato se si tratti di massimale o di stima.
- **Variabili (Table 15).** Numero avviso, data, titolo, buyer, procedura, descrizione, contraente, valore, valuta.
- **Identificazione ICT.**
  1. Traduzione dell'intero file in inglese con Google Translate, soprattutto del campo Titolo.
  2. Parole chiave sul **titolo** ("Software solutions", "SaaS", "Cloud computing", "IT services", "Cybersecurity"…; lista dichiarata "non limitata a").
  3. Match del contraente normalizzato con una lista curata dei "top 100 global IT and software companies".
  4. Classificazione della pertinenza del titolo con **ChatGPT API** (yes/no/uncertain), poi revisione manuale di tutte le etichette AI.
  5. Deduplica per numero di avviso.
  - Non viene usato alcun codice CPV.
  - Risultato: circa **315 avvisi**.
- **Multi-aggiudicatari.**
  - Riguardano il 41,5% degli avvisi (162).
  - Le righe vengono separate sul separatore "---", **duplicando il valore della gara su ogni riga**. Si arriva così a 778 righe-contraente.
  - Per i valori dei multi-winner gli autori usano un foglio separato (pivot e COUNTIF) "to avoid double-counting". Non è chiaro come sia stato calcolato l'88%.
- **Entity resolution e capogruppo.**
  - Dizionario dei top 100 con il paese della **sede della capogruppo**: copre 321 righe (41,3%).
  - Per le altre 457 righe (58,7%): ChatGPT API con prompt "ignora le filiali, restituisci il paese della capogruppo", poi revisione manuale.
  - Classificazione EU_Status sul paese della sede. Non vengono usati GLEIF né Orbis.
- **Regola di giurisdizione.**
  - Conta la sede della capogruppo del **vincitore**; il prodotto non è considerato.
  - Il testo stesso ammette che i vincitori più frequenti (Accenture 5%, Deloitte 4%, NTT Data 4%…) sono integratori "rather than software vendors" e che la lista dei vincitori non riflette lo stack software.
- **Risultati.**
  - 59% dei vincitori con sede UE. Paesi più frequenti: Francia 18%, USA 18%, Regno Unito 10%.
  - Circa **88% del valore**, dove disponibile, a consorzi con almeno un membro non UE; 12% a fornitori o consorzi puramente europei.
  - Il 53% dei vincitori compare in meno dell'1% dei casi.
- **Dati, codice, licenza.** Non pubblicati. Lavoro in R ed Excel, nessun repository citato.
- **Limiti dichiarati.** Solo quello su integratori e vendor. Nessuna analisi di sensibilità.
- **Apertura a contributi.** Nessuna dichiarata. Contatto: Policy Department ECTI (ecti-poldep-b@europarl.europa.eu).
- **Per noi.**
  - È il precedente UE più vicino per la vista *fornitore × sede della capogruppo*.
  - La lente *prodotto* supera proprio il limite che lo studio stesso dichiara.

## 2. Compass Lexecon per Open Cloud Coalition, "Quantifying EU Public Sector Dependence on Productivity Software" (luglio 2025)

Fonte: [PDF integrale, 36 pp.](https://opencloudcoalition.com/wp-content/uploads/2025/07/OCCEU-methodology-and-results-report.pdf). Autori: K. Prasad, A. Fazal, K. Nimbalkar, A. Amin, con commenti di J. Padilla. Tutto **[P]**.

Il report ha tre componenti.

**(a) Quote di mercato Statista 2023, poi "aggiustate".**
- Statista misura i ricavi a livello di produttore, esclusi i rivenditori.
- Scenario 2: si assume che il 90% dei ricavi Microsoft passi da partner. Il valore è preso da articoli di stampa e blog (Wire19, Volpi, Channelnomics).
- Scenario 3: si aggiunge Google al 38,2%.
- Da qui il "fino al 77% UE, 73–80% nei paesi". Le ipotesi vengono da stampa e settore, non sono misurate.
- Italia, segmento Office, quota base: Microsoft 48%.

**(b) "Incidence share".**
- Ricerca per parola chiave via **TED Search API** sugli avvisi con CPV **48000000** ("Software package and information systems"). Il CPV è scelto perché non ne esiste uno specifico per la produttività.
- Vendor cercati: quelli dei segmenti Collaboration e Office di Statista (Microsoft, Google, Discord, GoTo, RingCentral, Slack, TeamViewer, Webex, Zoho, Zoom).
- Unità: **numero di avvisi in cui il nome compare**, in qualunque punto (vincitore, specifiche, compatibilità, sistema esistente).
- Quota = menzioni del vendor / menzioni totali.
- Numeri:
  - **Italia 2024: 5 avvisi, tutti Microsoft (100%).**
  - **Italia 2023: 13 Microsoft + 5 Google = 72%.**
  - Germania 2024: 110 menzioni; Francia 2024: 8.
  - Livello UE 2024: 644 avvisi che citano Microsoft.
- Nessun valore economico. Non è dichiarata alcuna deduplica di lotti o rettifiche.

**(c) Revisione qualitativa su 189 avvisi.**
- Partenza: avvisi 2023–2024 (FR, DE, IT, PL, ES e livello UE) con "Microsoft" nel testo libero, esportati con **41 campi** prioritari. Totale: 562 avvisi.
- Esclusi quelli senza descrizione, vincitore o valore, più 12 poco informativi. Restano **189** avvisi.
- Traduzione con Google Translate e codifica manuale con un questionario strutturato (Appendice B).
- Il 91% (134 su 147) degli appalti per prodotti Microsoft è aggiudicato a soggetti legati a Microsoft, per lo più (82%) partner certificati o rivenditori. La relazione è verificata sui siti pubblici.
- È l'unico precedente che tratta esplicitamente il rivenditore come canale del prodotto, ma su un campione e senza importi aggregati.

**Limiti dichiarati.**
- Campi TED popolati in modo incoerente.
- Export limitato: 30.000 righe in Excel, 90.000 in CSV, a fronte di oltre 1.300 campi.
- Campione selezionato per completezza dei campi, quindi non casuale.
- Parte della navigazione in TED "reflect input from the OCC", cioè del committente.

**Dati, apertura, conflitto d'interessi.** Dati e codice non pubblicati. Nessuna apertura a contributi. Il committente è l'OCC: vedi il conflitto d'interessi segnalato nel report precedente.

**Per noi.**
- Prova che nei bandi il prodotto è riconoscibile dal testo.
- Per l'Italia TED è quasi inutile (5–18 avvisi l'anno): la BDNCP è indispensabile.

## 3. Tussell (UK): "Tech Titans" e "Public Sector Cloud Market Snapshot 2026"

- **Accesso.** I rapporti sono gated (download dietro modulo) e non sono stati scaricati. Pagine pubbliche: [Tech Titans](https://www.tussell.com/tech-titans-report), [Cloud snapshot 2026](https://www.tussell.com/public-sector-cloud-market-snapshot-2026), [VAR snapshot 2025](https://www.tussell.com/var-market-snapshot-2025).
- **Metodo.** Le pagine pubbliche non lo descrivono **[P, per l'assenza]**: nessuna indicazione su fonte (avvisi di aggiudicazione, call-off o spend file), tipo di valore, CPV o parole chiave, trattamento dei rivenditori.
- **Cifre, tutte [S].**
  - Nuovi contratti cloud cresciuti da £1,7 a £2,6 mld in quattro anni.
  - Spesa con fornitori IT di £16,9 mld nell'FY23/24, di cui il 22% a rivenditori a valore aggiunto (VAR).
  - Ricavi diretti dei Tech Titans: £16,5 mld nell'FY23/24.
  - L'analisi cloud 2022 usava una ricerca per parole chiave, con l'avvertenza di possibili dati "anomali non cloud".
- **Natura.** Tussell vende l'accesso alla piattaforma (G-Cloud 14, circa £11.400 l'anno per licenza [S]). Non c'è apertura a contributi: è un attore commerciale.
- **Rivenditori.** Il rapporto VAR è l'unico che li tratta, ma come mercato a sé, senza riattribuirli al prodotto [S].

## 4. Computer Weekly, "Data dive: Mapping the UK public sector's hyperscale dependence" (Antony Adshead, 2/6/2026)

Fonte: [articolo](https://www.computerweekly.com/news/366643799/Data-dive-Mapping-the-UK-public-sectors-hyperscale-dependence). WebFetch riceve 403, ma la pagina è stata scaricata con curl e letta. Tutto **[P]**.

- **Non è un'analisi di spesa.**
  - Metodo: ricognizione passiva DNS (record A, AAAA, MX, TXT, NS), RDAP, fonti IP e log di Certificate Transparency.
  - Perimetro: i domini di 19 dipartimenti e 10 council, cioè **29 enti**.
- **Risultati.**
  - 2.823 "connessioni": Microsoft 466, Google 264, AWS 137, 1.894 interne.
  - Il 96,55% degli enti risulta "soggetto a rischio giurisdizionale USA".
- **Cosa manca.**
  - Il testo primario non nomina mai Tussell, £17,7 mld, il 55%, i rivenditori o gli oltre 1.100 enti.
  - Queste cifre circolano tramite [The Next Web](https://thenextweb.com/news/uk-cloud-dependency-billion-pound-risk), che le accosta all'articolo senza indicarne la fonte [S].
- **Correzione al report precedente.** La descrizione "Computer Weekly su dati Tussell, rivenditori accorpati al prodotto" va ritirata finché non si trova la fonte vera.
- **Altri articoli.** Esistono "data dive" gemelli su NHS (id 366649921) e polizia (id 366650799), non letti.
- **Per noi.** Metodologicamente è vicino a MxMap (lato DNS), non allo studio sulla spesa.

## 5. Assemblée nationale: commissione d'inchiesta "dépendances et vulnérabilités dans le secteur du numérique" (presidente Latombe, relatrice Chatelain), rapporto n. 3054, t. I (453 pp., luglio 2026)

Fonte: [PDF t. I](https://www.assemblee-nationale.fr/dyn/17/rapports/cenum/l17b3054-t1_rapport-enquete.pdf), capitolo "C. Les dépenses de logiciels : 1,5 milliard…", pp. 102–110. Tutto **[P]**.

**Tre canali di dati.**
1. Questionari della relatrice alle amministrazioni. Gli enti dovevano compilare una tabella con la spesa per sviluppo e manutenzione (MCO) delle applicazioni metier e per le licenze dei software di supporto. Il modello è nell'Annexe 2, gli enti nell'Annexe 1.
2. Un **censimento governativo** svolto durante l'inchiesta con UGAP, DINUM e DAE. Copre 2,3 mld € aggregati contro i 4,2 mld dichiarati in audizione, quindi non è esaustivo.
3. Gli acquisti UGAP.

**I 115 M€ Microsoft 2025.**
- Perimetro della commissione: Stato più France Travail, Cnam, Cnav, CAF e AP-HP. Fonte: i questionari.
- Sul perimetro DINUM (UGAP + Chorus, senza operatori) la cifra è 98 M€.
- Altri editori: VMware 34,1, Oracle 23,1, Red Hat 17,1, IBM 12,6 M€. Il calcolo copre **solo i primi 7 fornitori**, "per troppe referenze diverse".
- Alcuni perimetri sono incompleti: per il ministero dell'Interno c'è solo la DGPN.
- Unità: la dichiarazione dell'ente. Valore: spesa per licenze 2025.
- Giurisdizione: l'editore del prodotto (Microsoft, Oracle…), coerente con la nostra lente.

**Gli 1,5 mld €/anno.**
- Base: top 50 fornitori UGAP 2025. La commissione ha verificato a mano la nazionalità della capogruppo, dopo che UGAP aveva ammesso "erreurs de méthodologie dans la classification des nationalités".
- Risultato: almeno 609 M€ a fornitori USA, pari al 79% (81% nel 2024).
- Estrapolazione: 609 M€ divisi per la quota di mercato UGAP stimata al 40% (1,174 mld su 2,95 mld di mercato secondo Exaegis) danno circa 1,5 mld.
- Quota USA sul totale UGAP: 46% se fuori dal top 50 nessun fornitore fosse americano, 73% se lo fosse la metà.
- Il governo aveva dichiarato 54–55,5% di editori francesi o europei; la commissione giudica quelle cifre "probabilmente errate".

**Limiti dichiarati.**
- Perimetri incompleti.
- Dipendenze di secondo livello non osservabili.
- Mancano le centrali CANUT e UniHA.
- Si assume che la struttura degli acquisti UGAP sia rappresentativa (spesa sostituibile stimata: 1.060 M€).

**Dati e apertura.** Solo tabelle nel PDF, nessun dataset né codice. Canale istituzionale, commissione ormai chiusa. Il rapporto non usa DECP né BOAMP: nessuna occorrenza nel testo [P].

## 6. Cour des comptes, "Les outils bureautiques et collaboratifs au sein de l'État" (22/10/2026)

Fonte: [PDF del rapporto](https://www.ccomptes.fr/sites/default/files/2026-10/20261022-Outils-bureautiques-et-collaboratifs-des-minist%C3%A8res_0.pdf). Tutto **[P]**.

**Metodo.**
- Inchiesta da dicembre 2024 ad aprile 2025.
- Ricerca documentale e **questionari** a 11 segretariati generali ministeriali, DINUM, DGFiP e DGGN, con interviste. In più, un sondaggio di soddisfazione degli agenti.
- Perimetro: amministrazioni centrali e servizi decentrati, circa **860.000 postazioni**. Esclusi operatori dello Stato, previdenza, ospedali ed enti locali.

**I 100 M€ (2025).**
- Sono crediti di pagamento consumati, cioè **pagato**.
- Includono licenze, prestazioni e **personale DSI dedicato**. Esclusi i sistemi operativi; inclusi DINUM e La Suite.
- La cifra è "reconstitué par la Cour": le risposte dei ministeri avevano qualità variabile e la "comptabilité analytique" è "défaillante".
- Media: 87 € per postazione all'anno su cinque anni. Interno 20 € ("sujet à caution"), Cultura 378 € (con MS365).
- "Plus de la moitié" della spesa va a Microsoft, tra licenze e prestazioni.

**Contesto Chorus.** L'aggregato "Informatique et télécom" vale 4,4 mld € di crediti di pagamento nel 2025, ma la nomenclatura Chorus non isola né il fornitore né il prodotto.

**I 30–65 M€.**
- Risparmio potenziale con software libero on-premises.
- Calcolo: la spesa per postazione (licenze + prestazioni, senza personale) di MEF (52 €) e Interno (15 €) applicata a 860.000 postazioni dà 45 e 13 M€. La differenza con i 76 M€ effettivi dà la forbice.

**I 130 M€.**
- Spesa supplementare evitata scegliendo una suite libera in cloud invece di MS365/Bleu, su 860.000 postazioni.
- È una proiezione su costi unitari che la Corte stessa dice "méritent d'être affinés": i livelli di servizio non sono stati comparati.

**Dati.** Nessun dataset pubblicato.

## 7. Bundestag, Drucksache 21/5413 (risposta del 14/4/2026 alle Kleine Anfragen 21/5006 e 21/5128, Die Linke)

Fonte: [PDF](https://dserver.bundestag.de/btd/21/054/2105413.pdf). Tutto **[P]**.

**Contenuto degli allegati.** Gli allegati non sono stampati nella Drucksache, ma sono dentro il PDF.
- **Anlage 1: contratti quadro** sopra 10.000 € con i gruppi USA elencati nella domanda (Alphabet, Adobe, Apple, Amazon, Meta, Microsoft, OpenAI, Cisco, Oracle, Citrix, Zoom). Colonne: Ressort/autorità, controparte, oggetto, volume in euro, durata, **volume richiamato nel 2025**.
- **Anlage 2: contratti singoli**, con la spesa 2025 suddivisa in licenze, supporto, consulenza e altri servizi.
- **Anlage 3:** risposta alla domanda 4 (filiali e altri contratti).
- **Anlage 4:** contratti quadro della Zentralstelle IT-Beschaffung del BeschA.

**Avvertenze del governo.**
- Il volume dei contratti quadro è "lediglich eine Höchstgrenze", solo un tetto.
- Il volume può essere espresso in giorni-persona.
- BND, BfV e BAMAD sono esclusi per Staatswohl (sicurezza dello Stato).

**Usabilità come dataset.**
- L'estrazione con pdftotext sfasa le righe: compaiono controparti e oggetti incrociati, per esempio "Microsoft Corporation — Adobe VIP Subscriptions" e "Cisco — Oracle DB-Lizenzen".
- Serve un'estrazione tabellare (camelot o tabula) oppure una trascrizione manuale con controllo.
- La controparte è indicata a livello di gruppo, scelta da un menu ("Auswahlfeld"). I rivenditori sono quindi probabilmente già ricondotti al gruppo, ma non è verificabile.
- È un buon termine di confronto per la colonna "pagato 2025 per prodotto USA", non un open data.

## 8. Altri studi (copertura parziale)

- **Stürmer / BFH-Uni Bern.**
  - Paper "When the exception becomes the norm" (2017, [BORIS](https://boris-portal.unibe.ch/entities/publication/2ed7ccee-ac75-4dfb-bc2d-216ad5d50839)): 2.754 procedure IT su simap in sette anni; il 47,2% di quelle sopra soglia OMC è stato aggiudicato senza gara. Propone una misura del lock-in [S, solo snippet; gli autori non sono confermati nella pagina].
  - È fuori dalla finestra 2019–2026, ma rilevante per il metodo: misura il lock-in come quota di affidamenti diretti dovuti a mancanza di alternative.
  - Stürmer dirige l'IPST della BFH [S].
- **Paesi Bassi.**
  - Il dataset "Totaaloverzicht Inkoopdata Rijksoverheid" su [data.overheid.nl](https://data.overheid.nl/en/dataset/totaaloverzicht-inkoopdata-rijksoverheid-2024) è in **CC-0**, annuale, per fornitore e ministero [S, non aperto].
  - Misura la spesa effettiva per fornitore contrattuale: i rivenditori non sono riattribuiti.
  - Secondo l'Algemene Rekenkamer, il 44% dei 1.588 servizi cloud viene da public cloud provider [S].
  - Da leggere: "Toestand van de Cloud" di Bert Hubert ([PDF](https://berthub.eu/articles/Toestand%20van%20de%20Cloud.pdf)).
- **DECP (Francia), PLACSP (Spagna), Spend Network/Open Opps, OCP, opentender/GTI.** In questa sessione non è stata trovata nessuna analisi pubblicata su Microsoft, AWS o cloud. Le ricerche web non hanno dato risultati pertinenti. È una lacuna di ricerca, non una prova di assenza.

## 9. Tabella di sintesi

| Studio | Unità | Valore | Identificazione ICT/cloud | Giurisdizione | Rivenditori | Multi-winner/framework | Dati aperti |
|---|---|---|---|---|---|---|---|
| PE 778.576 | Avviso TED, poi riga per vincitore | Aggiudicato | Parole chiave sul titolo + top 100 + ChatGPT + revisione | Sede della capogruppo del vincitore (dizionario + ChatGPT) | No (ammesso come limite) | Valore duplicato per riga; pivot separato | No |
| Compass/OCC | Avviso (menzione) | Nessuno | CPV 48000000 + nome del vendor | Marchio | Analisi qualitativa su 189 avvisi | No | No |
| Tussell | N/D (gated) | N/D | Parole chiave [S] | Fornitore | Rapporto VAR separato | N/D | No (commerciale) |
| CW data dive | Record DNS | Nessuno | DNS/RDAP/CT | Provider dell'infrastruttura | Non applicabile | Non applicabile | No |
| AN 3054 | Questionario dell'ente; acquisti UGAP | Spesa 2025 | Per editore | Editore (verifica manuale del top 50) | UGAP è un rivenditore; editori riattribuiti | Non applicabile | No |
| Cour des comptes | Questionario del ministero | Crediti di pagamento (pagato) | Perimetro bureautique | Editore | Non applicabile | Non applicabile | No |
| BT 21/5413 | Contratto | Volume (tetto) + richiamato 2025 | Domanda per gruppo USA | Gruppo | Probabilmente ricondotti al gruppo | Distingue quadro e singolo | Tabella nel PDF |

## 10. Conseguenze per il metodo italiano (BDNCP)

- **Originalità.** Nessuno attribuisce la giurisdizione al prodotto su dati di appalto censuari. I più vicini sono AN e Cour des comptes, che però usano questionari e UGAP, non registri di gara.
- **Allineamento con il PE.** Pubblicare anche una vista "sede della capogruppo del vincitore" con le stesse regole (UE/non UE, capogruppo). Il loro uso di ChatGPT con revisione manuale è un precedente accettabile per una classificazione LLM, purché revisionata.
- **Errori dei precedenti da non ripetere.**
  - Duplicare il valore sui multi-aggiudicatari.
  - Trattare i massimali dei framework come spesa. Su questo punto gli avvertimenti espliciti del governo tedesco e della commissione AN sono citabili.
- **Estensioni nazionali.** Nessuno studio prevede "country chapters". L'unica via è il contatto diretto: autori PE/ECTI, Compass Lexecon/OCC (con cautela), Stürmer/BFH.

## Non verificato / da fare

- Fonte vera delle cifre UK £17,7 mld, 55% e oltre 1.100 enti.
- Report Tussell completi (gated: servirebbe compilare il modulo).
- DECP, PLACSP e inkoopdata NL: aprire i dataset.
- Appendice A di Compass Lexecon (Table 18, 41 campi), per replicare l'export TED.
