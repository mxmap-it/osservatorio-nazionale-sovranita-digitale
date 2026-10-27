# Misurare la spesa cloud della PA, prodotto per prodotto

*Rapporto di ricerca, 27/10/2026. Base per la metodologia pubblicata di analisi-spesa-ict (issue mxmap-it/analisi-spesa-ict#48).*

**Legenda.**
- **[P]**: letto sulla fonte primaria in questa sessione.
- **[P-nostro]**: misurato da noi sui dati ANAC.
- **[S]**: di seconda mano (stampa, aggregatori, snippet). Non va presentato come fatto.
- **[K]**: conoscenza pregressa non verificata. È solo una pista.

Il rapporto sostituisce e corregge, sui punti indicati, il precedente "Misure europee sovranità digitale".

## Sintesi

In Europa nessuno ha misurato la spesa pubblica in cloud attribuendo la giurisdizione al **prodotto** su dati di appalto censuari. I precedenti si dividono in tre famiglie.

- **Studi su avvisi TED che classificano il vincitore.**
  - PE 778.576 attribuisce la giurisdizione alla sede della capogruppo del vincitore.
  - Compass Lexecon/OCC conta le *menzioni* di un marchio, non gli euro.
- **Inchieste istituzionali basate su questionari.**
  - Assemblée nationale e Cour des comptes. Misurano per editore, ma su perimetri parziali e con estrapolazioni.
- **Risposte parlamentari contratto per contratto.**
  - Bundestag 21/5413. È la più vicina a un dataset, ma è una tabella in PDF.

**Nessuno di questi studi pubblica dati o codice, né offre un canale per contributi o estensioni nazionali [P].** Il vuoto che l'Osservatorio può riempire è quindi reale.

Il pilota sui dati ANAC 2025 [P-nostro] dà tre indicazioni operative:

1. Gli importi sono dominati dai **massimali degli accordi quadro**. Vanno esclusi dalla somma: si contano i contratti attuativi.
2. La lente prodotto si può ottenere in modo deterministico **ereditandola dai lotti per fornitore cloud dell'AQ Consip ID 2746**. Nel lotto AWS l'aggiudicatario registrato è Fastweb.
3. Il "cloud generico" è in gran parte **SaaS verticale italiano**. Richiede un secondo livello: dove gira quel SaaS.

La metodologia proposta ha questi elementi:

- definizioni NIST/Eurostat;
- perimetro CPV pubblicato con varianti di sensibilità;
- classificazione a cascata, nell'ordine: regex, poi dizionario dei marchi, poi eredità dai lotti, poi LLM validato su un gold standard con kappa;
- livelli di confidenza e una quota indeterminata dichiarata;
- doppia lente prodotto/capogruppo, per confrontarsi con lo studio PE;
- valori attuativi, e il pagato SIOPE come serie separata.

La spesa in **infrastruttura propria** è misurabile bene solo per la parte acquisti. Personale, energia e ammortamenti richiedono ricerca documentale su un campione di enti.

## Due correzioni al rapporto precedente

Il rapporto precedente conteneva due errori, che vanno rettificati esplicitamente.

**Computer Weekly.** Il "Data dive: Mapping the UK public sector's hyperscale dependence" (Adshead, 2/6/2026) **non è un'analisi di spesa su dati Tussell**.
- È una ricognizione passiva DNS, RDAP e Certificate Transparency sui domini di **29 enti**: 19 dipartimenti e 10 council.
- Risultati: 2.823 "connessioni" (Microsoft 466, Google 264, AWS 137) e il 96,55% degli enti esposto a rischio giurisdizionale USA ([Computer Weekly](https://www.computerweekly.com/news/366643799/Data-dive-Mapping-the-UK-public-sectors-hyperscale-dependence)) [P].
- Le cifre di **£17,7 mld**, del **55%** "a hyperscaler o rivenditori" e degli oltre 1.100 enti **non compaiono nel testo**. Circolano tramite [The Next Web](https://thenextweb.com/news/uk-cloud-dependency-billion-pound-risk), che le accosta all'articolo senza citarne la fonte [S].
- **L'affermazione del rapporto precedente è ritirata.** La fonte di quelle cifre è ignota. Il metodo di Computer Weekly è, di fatto, parente di MxMap, non dello studio di spesa.

**PE 778.576.** Lo studio **contiene davvero un Annex 1 "TED data analysis" (pp. 175–179)** ([PDF PE](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU%282025%29778576_EN.pdf)) [P]. Era sbagliata la nota che lo descriveva come sola desk research. Il perimetro però è ambiguo all'interno del documento:
- l'annesso indica come fonte la sezione TED sui "contracts awarded by EU institutions";
- il testo principale (p. 60, nota 168) parla di avvisi "from public sector bodies across all EU Member States".

Le cifre dello studio vanno quindi citate con questa riserva.

## Come gli studi europei hanno costruito i dati

La tabella confronta le scelte di costruzione dei dati. Tutte le celle sono [P] salvo dove indicato.

| Dimensione | PE 778.576 (Visionary Analytics/ITRE, 2025) | Compass Lexecon per OCC (2025) | Assemblée nationale n. 3054 (2026) | Cour des comptes (22/10/2026) | Bundestag Drs. 21/5413 (2026) | Tussell (UK) |
|---|---|---|---|---|---|---|
| Fonte | Estratto TED 2020–2025, 13.238 avvisi | TED Search API, CPV 48000000; export di 41 campi | Questionari agli enti; censimento UGAP/DINUM/DAE; top 50 fornitori UGAP | Questionari a 11 ministeri, DINUM, DGFiP, DGGN | Risposta del governo, Anlagen 1–4 nel PDF | Piattaforma commerciale [S] |
| Unità di analisi | Avviso, poi una riga per vincitore (778 righe) | Avviso in cui compare il nome del vendor | Dichiarazione dell'ente; fornitore UGAP | Dichiarazione del ministero | Contratto quadro o singolo | N/D (gated) |
| Valore | Aggiudicato dichiarato dalla stazione appaltante; per i framework non è chiaro | Nessuno (solo conteggi) | Spesa licenze 2025; 1,5 mld estrapolato | Crediti di pagamento (pagato), personale incluso | Volume del quadro (tetto) + richiamato 2025 | N/D [S] |
| Identificazione ICT/cloud | Google Translate; parole chiave sul **titolo**; top 100 vendor; ChatGPT yes/no/uncertain; revisione manuale; **nessun CPV** | CPV 48000000 + nomi di vendor Statista | Per editore, primi 7 fornitori | Perimetro "bureautique" | Domanda per gruppo USA (11 gruppi) | Parole chiave [S] |
| Fornitore vs prodotto vs rivenditore | Solo vincitore. Ammette che i vincitori sono integratori "rather than software vendors" | Revisione qualitativa di 189 avvisi: il 91% dei contratti Microsoft va a soggetti legati a Microsoft, l'82% a partner o rivenditori | Editore del prodotto; UGAP è un rivenditore | Editore | Controparte a livello di gruppo (menu); rivenditori probabilmente ricondotti, non verificabile | Rapporto VAR separato, senza riattribuzione [S] |
| Nazionalità | Sede della capogruppo: dizionario per il 41,3% delle righe, ChatGPT + revisione per il 58,7%; niente GLEIF | Marchio | Capogruppo verificata a mano (UGAP aveva ammesso errori) | Editore | Gruppo | Fornitore [S] |
| Deduplicazione | Per numero di avviso; multi-vincitore separati duplicando il valore, poi un pivot separato | Non dichiarata | Non applicabile | Non applicabile | Distingue quadro e singolo | N/D |
| Risultato chiave | 59% di vincitori UE; ~88% del valore a consorzi con almeno un membro extra-UE | Italia 2024: 5 avvisi, 100% Microsoft; 2023: 18 avvisi, 72% | 115 M€ Microsoft (questionari); ≥609 M€ USA nel top 50 UGAP (79%) → ~1,5 mld | 100 M€ ricostruiti; >50% a Microsoft | Tabelle per contratto | Spesa con fornitori IT £16,9 mld, 22% VAR [S] |
| Dati, codice, contributi | No, no, no | No, no, no | No, no, no | No, no, no | Tabella in PDF, no, no | Commerciale, no |
| Fonte | [PDF](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778576/ECTI_STU%282025%29778576_EN.pdf) | [PDF](https://opencloudcoalition.com/wp-content/uploads/2025/07/OCCEU-methodology-and-results-report.pdf) | [PDF t. I](https://www.assemblee-nationale.fr/dyn/17/rapports/cenum/l17b3054-t1_rapport-enquete.pdf) | [PDF](https://www.ccomptes.fr/sites/default/files/2026-10/20261022-Outils-bureautiques-et-collaboratifs-des-minist%C3%A8res_0.pdf) | [PDF](https://dserver.bundestag.de/btd/21/054/2105413.pdf) | [Tech Titans](https://www.tussell.com/tech-titans-report) |

**Come leggere la tabella.** Ogni studio ha risolto un solo pezzo del problema che dobbiamo affrontare.

- **PE 778.576** risolve l'entity resolution del vincitore fino alla capogruppo. Ammette però che il vincitore non è lo stack software [P].
- **Compass Lexecon** mostra che il prodotto è riconoscibile dal testo e che il canale passa dai rivenditori. Lo fa però su un campione selezionato per completezza dei campi, senza importi, con parte della navigazione in TED guidata dal committente [P].
- **Assemblée nationale** attribuisce per editore. I suoi 1,5 mld € derivano però da 609 M€ divisi per una quota di mercato UGAP *stimata* al 40% [P].
- **Cour des comptes**:
  - i suoi 100 M€ sono ricostruiti dalla Corte a causa di una contabilità analitica "défaillante";
  - i 130 M€ sono un costo evitato rispetto a MS365/Bleu, non un risparmio misurato;
  - i 30–65 M€ sono un risparmio potenziale con software libero on-premises [P].
- **Bundestag** distingue esplicitamente il tetto del quadro dal richiamato. Il governo avverte che il volume è "lediglich eine Höchstgrenze" [P]. L'estrazione testuale del PDF sfasa le colonne, per esempio "Cisco — Oracle DB-Lizenzen" [P].

**Fuori finestra o non verificati.**
- Il dataset olandese "Totaaloverzicht Inkoopdata Rijksoverheid" è in CC-0, per fornitore contrattuale, senza riattribuzione dei rivenditori ([data.overheid.nl](https://data.overheid.nl/en/dataset/totaaloverzicht-inkoopdata-rijksoverheid-2024)) [S, non aperto].
- Stürmer et al. (Berna, 2017) misurano il lock-in come quota di affidamenti diretti: 47,2% sopra soglia OMC su 2.754 procedure simap ([BORIS](https://boris-portal.unibe.ch/entities/publication/2ed7ccee-ac75-4dfb-bc2d-216ad5d50839)) [S].
- Su DECP, PLACSP, Spend Network, OCP e opentender non è stata trovata alcuna analisi pubblicata su cloud o Microsoft. È una lacuna di ricerca, non una prova di assenza.

**Per l'Italia TED è quasi inutile: 5–18 avvisi l'anno nel campione OCC [P]. La base deve essere la BDNCP.**

## Errori metodologici da non ripetere

Gli studi esistenti offrono, nell'ordine, sei errori da evitare.

1. **Duplicare il valore sui multi-aggiudicatari.** PE 778.576 separa i vincitori su "---" e copia il valore della gara su ogni riga. L'88% del valore "a consorzi con membri extra-UE" poggia su queste righe, ed è poco chiaro come sia stato calcolato [P].
2. **Sommare i massimali degli accordi quadro come spesa.**
   - Il governo tedesco lo dice esplicitamente [P].
   - Il nostro pilota mostra che nel "cloud generico" i primi 10 CIG valgono l'**85,3%** dell'importo [P-nostro].
3. **Confondere vincitore e prodotto.** È il limite dichiarato del PE [P]. Il caso Fastweb/AWS (sotto) ne è la prova italiana.
4. **Contare menzioni invece di euro**, come fa Compass Lexecon. La sua "incidence share" non va mai citata come quota di spesa [P].
5. **Estrapolare da una quota di mercato stimata**, come i 609 M€ / 40% dell'AN, o **chiamare "risparmio" un costo evitato**, come i 130 M€ della Cour des comptes. Se si fanno, vanno etichettati come scenari [P].
6. **Affidare la nazionalità a un LLM senza dichiararne la validazione.** Il PE dichiara una revisione manuale, ma senza metriche. La letteratura considera la validazione per task contro un gold standard umano un requisito minimo per pubblicare ([Törnberg 2024](https://arxiv.org/pdf/2402.05129); [OLAF](https://arxiv.org/html/2512.15979v1)) [P].

## Il pilota ANAC 2025: l'85% del cloud è massimali, e il fornitore non è il prodotto

**Come è stato costruito il pilota.**
- Script: `tools/analisi/pilota_classificazione.py` nel repo mxmap-it/analisi-spesa-ict.
- Metodo: regex a priorità su `oggetto_lotto` e `oggetto_gara`.
- Dati: dataset ANAC `cig-2025` (12 file mensili).
- Perimetro CPV provvisorio: 48\*, 72\*, 302\*, 3223–3226\*, 50312\*, 50320\*, 51611\*, 64216\*, 64222\*, 79342\*.
- Risultato: **111.681 CIG ICT per 41,39 mld €** di importi di lotto [P-nostro].
- Perimetro e regex sono provvisori e **la precisione non è ancora misurata**. Le cifre sono ordini di grandezza, non risultati.

| Classe | CIG | % CIG | Importo | % importo |
|---|---|---|---|---|
| Non classificato | 97.353 | 87,2 | 25,32 mld | 61,2 |
| Cloud generico (cloud/SaaS/IaaS/hosting senza marchio) | 7.447 | 6,7 | 12,80 mld | 30,9 |
| Infrastruttura propria (server, storage, CED…) | 3.985 | 3,6 | 0,76 mld | 1,8 |
| Microsoft cloud | 964 | 0,9 | 0,16 mld | 0,4 |
| Licenze big tech on-prem (Microsoft, Oracle, VMware) | 853 | 0,8 | 1,08 mld | 2,6 |
| Altri SaaS USA (Salesforce, ServiceNow, Zoom, Adobe…) | 418 | 0,4 | 0,20 mld | 0,5 |
| PSN | 285 | 0,3 | 0,93 mld | 2,2 |
| Google | 194 | 0,2 | 0,02 mld | 0,04 |
| Operatori cloud IT/UE (Aruba, Seeweb, WIIT, Retelit…) | 99 | 0,1 | 0,08 mld | 0,2 |
| AWS | 60 | 0,05 | 0,04 mld | 0,1 |
| Oracle cloud | 23 | 0,02 | 0,006 mld | 0,01 |

### I massimali gonfiano il cloud generico

Il "cloud generico" vale circa 13 mld €, ma l'85,3% sta in dieci CIG [P-nostro]:
- AQ Consip, 3,78 mld;
- AQ Banca d'Italia, 3,0 mld;
- AQ InfoCamere "servizi applicativi in ottica cloud", 2 × 1,6 mld;
- lotti Consip IaaS/PaaS.

Sommare i CIG padre insieme ai loro derivati conta due volte e scambia il massimale per spesa.

**Regola adottata:**
- i CIG di accordo quadro si escludono dalla somma;
- si sommano i contratti attuativi, riconoscibili dal campo ANAC `cig_accordo_quadro` valorizzato;
- per la cassa si usa SIOPE, come serie separata.

### I lotti Consip AQ 2746 danno il prodotto

L'AQ Consip **ID 2746 "Cloud IaaS e PaaS 2"** ha un lotto per ogni fornitore cloud. Nei dati ANAC [P-nostro]:

| CIG del lotto | Fornitore cloud |
|---|---|
| B6A19F425E | Lotto 1, AWS (aggiudicatario Fastweb) |
| B6A19F5331 | Lotto 2, Google |
| B6A19F6404 | Lotto 3, Microsoft |
| B6A19F74D7 | Oracle |
| B6A19F85AA | IBM |
| B6A19F967D | Aruba |

Una determina ARERA conferma su fonte primaria che il Lotto 1 (CIG B6A19F425E) "ha ad oggetto i servizi Amazon ed è stato stipulato con Fastweb S.p.a." ([ARERA 76/2026/DAGR](https://www.arera.it/fileadmin/allegati/docs/26/76-26-dagr.pdf)) [P].

I contratti attuativi riportano il CIG del lotto in `cig_accordo_quadro`. Nel solo delta ANAC di ottobre 2026 [P-nostro]:

| Fornitore cloud | Adesioni | Importo |
|---|---|---|
| Microsoft | 16 | 8,94 M€ |
| Oracle | 7 | 7,23 M€ |
| AWS | 10 | 4,75 M€ |
| Google | 4 | 1,92 M€ |
| Aruba | 3 | 0,59 M€ |
| IBM | 0 | – |

**È la prova diretta che il fornitore registrato (Fastweb, italiano) non è il prodotto (AWS).** Una vista basata solo sul vincitore, come quella del PE, classificherebbe quella spesa come italiana.

### Il cloud generico è soprattutto SaaS verticale italiano

Il "cloud generico" contiene soprattutto SaaS verticale italiano: Spaggiari, Halley, Urbi/PA Digitale, cartelle cliniche, protocollo [P-nostro].

- Il prodotto è italiano.
- L'hosting sottostante può però essere su un hyperscaler USA.
- Serve quindi un secondo attributo, la **giurisdizione dell'infrastruttura di erogazione**. Le fonti sono il catalogo ACN e le dichiarazioni dei fornitori.

### Le altre lezioni del pilota

- **L'87% dei CIG ICT non è né cloud né infrastruttura riconoscibile.** È atteso: il cloud si misura come sottoinsieme, non come quota dell'ICT.
- **La classe "infrastruttura propria" ha falsi positivi**, come "Jira Data Center", "server proxy" in abbonamento e "crioconservazione". Servono regole che combinino CPV e testo.
- **Sono pronti 50 CIG casuali per classe** in `lavoro/pilota/2025-campioni.json`, per la validazione manuale [P-nostro].

## Metodologia proposta per la spesa cloud: lente prodotto, cascata validata, valori attuativi

### Definizioni

**Ossatura concettuale.** Si adotta NIST SP 800-145: 5 caratteristiche essenziali, 3 modelli di servizio (IaaS/PaaS/SaaS) e 4 modelli di deployment ([NIST](https://csrc.nist.gov/pubs/sp/800/145/final)) [P].

**Cosa conta come spesa cloud.** Si adotta il criterio operativo Eurostat: servizi **a pagamento** (per utente, per uso o prepagati), forniti da un terzo su server condivisi o dedicati ([Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Cloud_computing_-_statistics_on_the_use_by_enterprises)) [P].

**Bucket di spesa.** Seguono la separazione TBM fra il cost pool "Cloud Vendor" e quello "Hardware" ([TBM v4.0](https://cybersecurity.wa.gov/sites/default/files/2023-07/TBM%20Taxonomy%20v4.0%20Placemat.pdf)) [P]:
1. cloud pubblico IaaS/PaaS;
2. SaaS in abbonamento;
3. cloud qualificato dedicato o housing di terzi (PSN, in-house regionali);
4. licenze perpetue e manutenzione;
5. hardware;
6. opere e impianti di data center;
7. personale ICT interno;
8. servizi professionali.

### Perimetro CPV

Il CPV 2008 non ha un codice cloud. La lista va quindi **pubblicata e versionata**, con quattro varianti:
- **stretta**: cloud e data center;
- **media**: la lista del pilota;
- **larga**: ICT intero;
- **solo testo**: senza filtro CPV.

Per ciascuna variante si riporta la quota extra-UE risultante.

Il CPV dichiarato è un segnale ausiliario, non una verità. La letteratura lo tratta come rumoroso e cerca di prevederlo dal testo:
- Siciliani et al., CLiC-it 2023, su circa 5M descrizioni ANAC ([ACL](https://preview.aclanthology.org/moar-dois/2023.clicit-1.47.pdf)) [P];
- il dataset SoBigData, per sola ricerca non commerciale ([D4Science](https://ckan-sobigdata.d4science.org/dataset/italian_common_procurement_vocabulary_cpv_)) [P].

### Cascata di classificazione

Si applica a `oggetto_lotto` e `oggetto_gara`.

1. **Regex deterministiche** per i marchi espliciti.
2. **Dizionario dei marchi versionato.** Ogni voce collega marchio, sviluppatore e capogruppo, usando:
   - QID Wikidata (P178, P749, P159, P17) [S];
   - vendor CPE NIST ([NVD](https://nvd.nist.gov/developers/products)) [P];
   - LEI della capogruppo ultima da GLEIF Level 2 ([GLEIF](https://www.gleif.org/en/services/gleif-services/access-lei-data/lei-download)) [P].
   - Il dizionario va rilasciato con licenza aperta: oggi in Europa non esiste.
3. **Eredità dai lotti.** È una tabella mantenuta a mano "CIG del lotto AQ/convenzione → prodotto". Copre:
   - AQ 2746 e il suo predecessore ID 2213;
   - licenze Consip;
   - PSN per voce di catalogo:
     - Industry Standard / private cloud: IT/UE, stack da verificare;
     - Hybrid on PSN Site: Microsoft Azure;
     - PSN Managed: Google o Oracle;
     - Secure Public Cloud: il CSP scelto ([PSN](https://polostrategiconazionale.it/en/solutions/cloud-services-with-csp)) [P].
   - Il solo contratto di adesione PSN non basta. Servono i Piani dei Fabbisogni [S].
4. **LLM solo sul residuo ambiguo**, con queste regole di riproducibilità:
   - model ID fissato, temperatura 0, prompt versionato;
   - cache JSONL per CIG con hash del prompt;
   - un modello open-weight di backup validato sullo stesso gold, perché i modelli proprietari vengono deprecati ([Cheng et al.](https://arxiv.org/abs/2412.14461)) [P].

**Validazione:**
- gold standard stratificato di 1.000–2.000 CIG (per classe, CPV, importo, anno), con sovra-campionamento dei testi generici;
- doppia annotazione su almeno il 20%, con **κ di Cohen umano come tetto di riferimento**;
- precision, recall e F1 per classe e per strato;
- aggregati corretti per precision e recall, con intervalli bootstrap ([Törnberg](https://arxiv.org/pdf/2402.05129)) [P].

Il precedente ChatGPT con revisione manuale del PE rende accettabile l'uso di un LLM. La nostra validazione deve però essere misurata e pubblicata.

### Livelli di confidenza e quota indeterminata

Ogni CIG riceve un'etichetta di provenienza:

| Etichetta | Significato |
|---|---|
| `brand_esplicito` | Marchio nel testo |
| `brand_da_lotto` | Ereditato da AQ, convenzione o PSN |
| `brand_da_fornitore` | Fornitore mono-marchio, per esempio Aruba diretto |
| `llm_validato` | Assegnato dall'LLM sul residuo |
| `multi_prodotto` | Più prodotti. Il CIG si conta in ogni marchio con un flag, **senza ripartire l'importo** |
| `non_determinabile` | Nessun prodotto attribuibile |

La quota `non_determinabile` **si pubblica, non si imputa**. Il modello è il "tipo ignoto per il 26%" della Rekenkamer, citato nel rapporto precedente.

### Doppia lente

Ogni euro riceve due attributi:
- **giurisdizione del prodotto**: la nostra lente principale;
- **giurisdizione della capogruppo ultima del vincitore**: le stesse regole UE/non UE del PE, quindi confrontabile.

La **matrice di riconciliazione** incrocia contraente IT/UE/extra-UE con prodotto IT/UE/extra-UE. La cella "contraente IT, prodotto USA" quantifica l'effetto rivenditore che nessuno studio ha misurato in euro.

Per il SaaS va aggiunto un terzo attributo: la **giurisdizione dell'infrastruttura di erogazione**.

### Valori

- **Si sommano** i contratti attuativi e gli affidamenti diretti. I massimali AQ si escludono dalla somma e si riportano a parte come "capienza".
- **Multi-aggiudicatari**: non vanno ripartiti in parti uguali. Se si ripartiscono, la regola va dichiarata.
- **Pagato**: è una serie SIOPE separata, mai sommata all'aggiudicato. SIOPE non ha un codice cloud: un contratto AWS della Regione Siciliana è registrato su U.1.03.02.19.003 come i servizi generici ([Regione Siciliana](https://regione.sicilia.it/index%2ephp/istituzioni/servizi-informativi/decreti-e-direttive/dda-n-12-31012023)) [P]. Il pagato serve quindi come vincolo di plausibilità. L'attribuzione richiede il legame CIG–pagamento, da verificare.
- **PNRR 1.2**: è uno strato a sé. Il finanziamento lump sum misura il contributo, non il pagamento al fornitore [K]. Il ponte verso il fornitore è CUP → CIG.

### Asse qualitativo

Ogni prodotto si mappa su tre scale:
- i **4 bucket mxmap**, per continuità con l'osservazione DNS della posta;
- la **scala 1–5**, da 1 = cloud globale USA a 5 = infrastruttura nativa UE;
- una **stima proxy SEAL 0–4**, con la regola dell'anello più debole del Cloud Sovereignty Framework ([guidance](https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en)) [P]. Va dichiarato che non è una valutazione SEAL vera.

Il livello ACN QC non è un proxy della giurisdizione. Il Regolamento non contiene requisiti di proprietà o sede non extra-UE del fornitore. I requisiti di sovranità sono operativi: metadati in UE, autorizzazione degli accessi extra-UE e, solo a QC4, HYOK e autonomia operativa ([ACN](https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud)) [P]. Il livello QC resta quindi un asse "sicurezza", distinto.

## Infrastruttura propria: gli acquisti sì, il costo pieno solo per campione

**Lo stato delle fonti italiane.**
- L'Italia ha un censimento fisico dei data center, ma senza costi: **1.252 DC** di quasi mille PA, di cui 1.190 in Gruppo B, censimento chiuso nel febbraio 2020 ([AgID](https://www.agid.gov.it/it/agenzia/stampa-e-comunicazione/notizie/2020/02/20/cloud-pa-concluso-il-censimento-ict)) [P].
- Il rapporto AgID "La spesa ICT nella PA 2024" non è leggibile: il sito è in manutenzione (redirect verificato il 27/10/2026) [P sul fallimento].

**L'esperienza estera.** Anche governi con un mandato dedicato non conoscono il costo dei propri data center.
- Nel 2015 il BMI tedesco non conosceva affitti e costi operativi dei DC federali [S].
- GAO segue la DCOI dal 2016: su 126 raccomandazioni, 110 sono state attuate ([GAO-23-105946](https://www.gao.gov/assets/gao-23-105946.pdf)) [P].
- Il modello di riferimento è olandese: le ICT-kosten includono il personale interno. Nel 2018 erano 3,11 mld €, di cui circa 907 M€ di personale [S/P].

| Componente | Fonte | Fattibilità |
|---|---|---|
| Hardware server/storage | CPV 302\*, 48820000; SIOPE U.2.02.01.07 ([uso del codice, ARPA Piemonte](https://bandi.arpa.piemonte.it/sites/default/files/allegati/bandi-appalti/2025/227/Determina_n.%20849%20del%2006.11.2025.pdf)) [P] | Alta per gli acquisti; media per l'attribuzione al DC (client mescolati, falsi positivi del pilota) |
| Manutenzione hw/sw | CPV 50312\*, 72250000; SIOPE U.1.03.02.19 | Media: si mescola con la gestione esterna |
| Opere e impianti DC | CPV 45\* con testo "data center/CED"; UPS, condizionamento | Bassa-media, solo testuale |
| Energia del DC | Nessuna fonte pubblica separata | Molto bassa |
| Personale ICT | Conto annuale RGS (profili non ICT-specifici) | Bassa: serve un'indagine |
| Ammortamenti | Ricostruiti dagli impegni in conto capitale con vite utili convenzionali (server 5 anni, impianti 10–15) [K] | Stima modellistica |
| Capex dismesso (PNRR 1.2) | Incrocio DC del Gruppo B con beneficiari 1.2 | Conta i DC, non il costo |

**Raccomandazione.**
- Sull'universo si misura **solo la componente acquisti**, con la stessa pipeline e la stessa validazione del cloud.
- Il **costo pieno** (TCO = ammortamenti + impianti + energia + manutenzione + personale + licenze) si stima su un **campione stratificato di enti**: ministeri, regioni, in-house, ASL e comuni grandi.
- Il campione si costruisce con agenti di ricerca per progetto su:
  - piani triennali ICT;
  - PIAO;
  - delibere CED;
  - relazioni sulla gestione.
- Ogni stima va documentata con fonte e livello di attendibilità.
- Il risultato va presentato come **intervallo modellistico**, non come misura. È lo stesso criterio che rimproveriamo alle estrapolazioni dell'AN.

## Dove offrire l'estensione italiana

Nessuno degli studi offre un canale per capitoli nazionali [P]. L'estensione italiana va quindi proposta attivamente, con un prodotto che agli altri manca:
- dataset aperto per CIG;
- codice;
- dizionario marchio→capogruppo;
- metriche di validazione.

**Le controparti, in ordine di priorità:**

1. **Autori di PE 778.576 e Policy Department ECTI** (ecti-poldep-b@europarl.europa.eu) [P]. Offriamo una replica italiana della loro lente "capogruppo del vincitore" sulla BDNCP, affiancata dalla lente prodotto che supera il limite che loro stessi dichiarano. Chiediamo di chiarire il perimetro dell'annesso e il calcolo dell'88%.
2. **Open Contracting Partnership** (engage@ / data@open-contracting.org) e **Government Transparency Institute** (info@govtransparency.eu) [P]. Sono il canale naturale per pubblicare la classificazione come estensione o lista di codici su dati OCDS e per farla replicare in altri paesi.
3. **Assemblée nationale e Cour des comptes**: canali non verificati. Possiamo offrire il confronto per editore (Microsoft, VMware, Oracle) con le loro cifre 2025.
4. **Interface, CASSIS Bonn, EuroStack/EDRIX** [P]. Sono i consumatori di un indicatore paese basato sulla spesa.
5. **Compass Lexecon/OCC**: solo per la lista dei 189 avvisi e le query, dichiarando il conflitto d'interessi del committente.
6. **Stürmer/BFH** [S]: per la misura del lock-in tramite gli affidamenti diretti.

## Verifiche aperte

**Correzioni e cifre da chiarire.**
- Fonte vera delle cifre UK £17,7 mld, 55% e oltre 1.100 enti.
- Perimetro dell'Annex 1 di PE 778.576 e calcolo dell'88%.
- Report Tussell completi (gated).

**Fonti da aprire o estrarre.**
- Appendice A di Compass Lexecon (41 campi).
- Estrazione tabellare (camelot o tabula) degli Anlagen di BT 21/5413.
- Dataset DECP, PLACSP e inkoopdata NL.

**Dati italiani.**
- Mappa completa lotti → CSP → aggiudicatario per ID 2213 e 2746.
- Listino PSN (Allegato C) e Piani dei Fabbisogni.
- Open data Consip degli ordinativi.
- Nome e copertura del campo `cig_accordo_quadro` su tutti gli anni.
- Esistenza di un export strutturato del catalogo ACN.
- Presenza di beneficiario e CIG negli open data SIOPE+.
- Open data delle candidature PA Digitale 2026 (il repo GitHub ipotizzato risponde 404 [P]).
- Rapporto AgID 2024.

**Metodo.**
- Precisione del pilota sui campioni da 50 CIG.
- Gold standard e κ.
- Copertura di Wikidata P178/P749 per i prodotti SaaS.
- Soglie SecNumCloud (§19.6 non letto).

## Conclusione

Il contributo italiano non sta nella fonte, ma nella **costruzione**. La BDNCP, il legame `cig_accordo_quadro` e i lotti Consip per fornitore cloud permettono di fare in modo deterministico e censuario ciò che gli studi europei hanno fatto con questionari, menzioni o vincitori. Il caso Fastweb/AWS mostra che le due lenti divergono davvero. Senza la lente prodotto, una parte della spesa negli hyperscaler USA risulta "italiana".

Il rischio speculare è ripetere gli errori altrui in forma nuova: massimali sommati, LLM non validati, estrapolazioni presentate come misure. La metodologia regge solo se pubblica insieme dataset, codice, quota indeterminata e metriche di validazione. È proprio questo che, oggi, nessuno in Europa offre da estendere.
