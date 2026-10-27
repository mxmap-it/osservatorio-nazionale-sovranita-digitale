# Classificazione delle descrizioni di gara (ICT, prodotto/brand, giurisdizione)

Legenda: [P] = fonte primaria (paper, documentazione ufficiale, dataset); [S] = fonte secondaria (blog commerciale, aggregatore, sintesi).
Nota di metodo: ricerca condotta con ~12 query/fetch; diversi PDF non erano raggiungibili (es. il PDF CLiC-it 2023 dà 404 sull'anteprima ACL). Quando cito una cifra presa solo dall'abstract o da una sintesi lo dico.

## 1. Lavori accademici e applicati sulla classificazione del testo degli appalti (CPV, Italia/ANAC)

### Takeaway
La previsione del CPV a partire dal testo è un problema studiato. Esiste un lavoro italiano direttamente pertinente: Siciliani, Tanzi, Basile e Lops (Bari), CLiC-it 2023, su circa 5 milioni di descrizioni ANAC. I numeri di accuratezza riportati (dal 76% al 95%) non sono confrontabili tra loro, perché cambiano il livello CPV, il dataset e la metrica. Per l'Osservatorio la classificazione per brand o prodotto è un compito diverso e più semplice della previsione CPV: va validato a parte.

### Cited Findings
- [P] Siciliani, Tanzi, Basile, Lops, "Automatic Generation of Common Procurement Vocabulary Codes", CLiC-it 2023. Costruiscono un corpus di circa 5M gare italiane dal sito ANAC e trattano il CPV sia come classificazione sia come generazione. Conclusione: i classificatori testuali vanno meglio, i modelli generativi sono "promettenti". Non ho potuto leggere i punteggi esatti perché il PDF non era accessibile. — [ACL preview PDF](https://preview.aclanthology.org/moar-dois/2023.clicit-1.47.pdf)
- [P] Dataset "Italian Common Procurement Vocabulary (CPV)" su SoBigData/D4Science: circa 5M coppie descrizione-CPV da open data ANAC, divise in circa 3,2M train, 800K dev e 1M test, in formato JSON, adatte a fine-tuning T5. Richiede login; licenza solo per ricerca non commerciale. — [D4Science CKAN](https://ckan-sobigdata.d4science.org/dataset/italian_common_procurement_vocabulary_cpv_)
- [P] Kayte e Schneider-Kamp (2019), TED UE: rete neurale (LSTM) per generare i titoli più SVM per il CPV principale. Riportano 95% di accuratezza nella classificazione del codice (livello e condizioni da verificare nel paper). — [SciTePress](https://www.scitepress.org/Papers/2019/83627/)
- [S] Haskoning, proof of concept: un modello per ogni livello della gerarchia CPV, circa 76% di accuratezza al livello più alto, con suggerimento delle top-5 previsioni. — [Haskoning](https://www.haskoning.com/en/projects/using-machine-learning-to-predicting-cpv-codes-from-tender-text)
- [S] Spend Network, classificatore commerciale: assegna 5 codici CPV di livello 3 con punteggio. Dichiara accuratezza 84%, precision 83% e recall 88%. Algoritmi non specificati, non open source. — [Spend Network](https://spendnetwork.com/new-year-new-tool-introducing-our-new-classifier/)
- [P] CNR, ITAL-IA 2023: similarità coseno sul testo "oggetto" ANAC per collegare i record ad altri dataset. Il match per CIG trova il 12,4% dei riferimenti, la similarità sul testo il 22,3%. I modelli migliori sono XGBoost, RF e SVM. Mostra che l'oggetto CIG è utilizzabile ma rumoroso. — [ITAL-IA 2023](https://ital-ia2023.isti.cnr.it/submission/100/presentation)
- [P] UniTo, AIxPA 2022: gli open data ANAC coprono circa 7,2M procedure dal 2007 al 2022, con il CIG come chiave e i campi oggetto e tipo di procedura. Una tesi UniTo 2019/20 usa NLP sull'oggetto per l'anomaly detection. — [Presentazione AIxPA](https://iris.unito.it/retrieve/e452a924-c3c7-48d4-8846-a2da437fdf6a/Presentazione%20AIxPA%20-%202%20dicembre%202022-2.pdf); [tesi](https://unitesi.unito.it/handle/20.500.14240/29990)

### Inferences
- Il CPV dichiarato in BDNCP serve come segnale ausiliario (ad esempio 72xxxxxx servizi IT, 48xxxxxx pacchetti software), non come verità. La letteratura stessa tratta il CPV come rumoroso e cerca di prevederlo.
- Il compito dell'Osservatorio è a due stadi: (a) è ICT o cloud? (b) quale prodotto o brand? Lo stadio (b) su testi brevi auto-esplicativi è una NER a dizionario, dove regex più gazetteer danno alta precisione. Il richiamo va invece misurato sui testi generici.

### Gaps
- Non ho trovato paper che riportino accuratezze di BERT italiano o multilingue (es. dbmdz/Italian BERT, UmBERTo) sulla previsione CPV su dati ANAC. Mi mancano anche i numeri esatti di Siciliani et al. (PDF non accessibile).
- Non ho trovato studi italiani che classifichino l'oggetto CIG per vendor o brand ICT.

## 2. NER di prodotto/brand e attribuzione della giurisdizione (gazetteer, Wikidata, CPE, GLEIF)

### Takeaway
Non esiste un dizionario aperto già pronto "prodotto → casa madre → paese". Va costruito combinando tre fonti: il dizionario CPE NIST per le varianti dei nomi vendor:prodotto, Wikidata per la catena prodotto → sviluppatore → sede o capogruppo, GLEIF Level 2 per la capogruppo legale. Il dizionario va versionato nel repo.

### Cited Findings
- [P] Il dizionario CPE NIST ha 1.632.075 CPE Names e oltre 420.000 match strings, accessibili via API 2.0 (`services.nvd.nist.gov/rest/json/cpes/2.0`), con paginazione. I CPE deprecati sono segnalati con `deprecatedBy` e `deprecates`: i nomi vendor e prodotto cambiano nel tempo. — [NVD Products API](https://nvd.nist.gov/developers/products)
- [P] GLEIF Level 2 ("who owns whom") registra il parent diretto e quello ultimo, entrambi di consolidamento contabile. Ci sono un file delle relazioni e un file delle eccezioni (nessun parent, opt-out, parent senza LEI). A fine Q1 2018 circa 838.000 entità, il 75% dei LEI, avevano dichiarato i parent; il dato attuale va verificato. Download concatenati gratuiti. — [GLEIF blog](https://www.gleif.org/en/newsroom/blog/connect-the-corporate-dots-globally-with-the-legal-entity-identifier-a-progress-report-on-collecting-data-on-who-owns-whom); [GLEIF download](https://www.gleif.org/en/services/gleif-services/access-lei-data/lei-download)
- [S] Wikidata è in CC0 ed è interrogabile via SPARQL. Le proprietà rilevanti per la catena sono P178 (sviluppatore), P127 (proprietario), P749 (organizzazione madre), P159 (sede) e P17 (paese). Questa mappatura viene dalla mia conoscenza dello schema Wikidata: non ho trovato un lavoro che la usi per l'analisi della dipendenza da vendor. — [Dublin Core/Wikidata](https://msi.dublincore.org/standards/wikidata)

### Inferences
- Protocollo proposto. (1) Gazetteer curato a mano dei brand rilevanti per la sovranità (Microsoft 365/Azure/Teams/Dynamics, AWS, Google Workspace/GCP, Oracle, Salesforce, ServiceNow, Aruba, TIM/Polo Strategico Nazionale, Fastweb, Register.it, OVHcloud...), con alias e regex. (2) Ogni voce collegata a un QID Wikidata, all'eventuale CPE vendor e al LEI della capogruppo. (3) La giurisdizione è il paese della capogruppo ultima (GLEIF Level 2). Va registrato anche il caso "operatore UE con stack USA" (es. PSN che rivende hyperscaler), perché pesa sulla soggezione al CLOUD Act.
- Il CPE copre bene il software on-premise e male i servizi cloud e i provider italiani di hosting: per questi serve curarli a mano.

### Gaps
- Non ho trovato dizionari aperti già pronti che colleghino brand cloud e giurisdizione. Non ho verificato il catalogo Joinup né SPDX: SPDX riguarda le licenze, non i vendor, quindi è probabilmente irrilevante.
- Non ho verificato la copertura effettiva di P178 e P749 in Wikidata per i prodotti SaaS.

## 3. Pratica di classificazione con LLM: validazione, riproducibilità, costi

### Takeaway
La letteratura in scienze sociali converge su alcuni punti: validazione obbligatoria per ogni task contro un gold standard umano; agreement chance-corrected (κ di Cohen) confrontato con l'agreement tra annotatori umani; modelli e parametri fissati e output in cache; un modello open-weight di riserva per la riproducibilità.

### Cited Findings
- [P] Gilardi, Alizadeh e Kubli, PNAS 2023 (doi 10.1073/pnas.2305016120): su 6.183 item (tweet e news), ChatGPT zero-shot supera i crowd worker in media di circa 25 punti di accuratezza. L'intercoder agreement è più alto sia dei crowd worker sia degli annotatori addestrati, a un costo inferiore a $0,003 per annotazione, circa 30 volte meno di MTurk. — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10372638/)
- [P] Törnberg, "Best Practices for Text Annotation with LLMs" (2024): la validazione è un requisito minimo per ogni pubblicazione, perché le prestazioni dipendono dal dataset e dal task. Raccomanda di giustificare la metrica (F1, ROC-AUC, κ), di confrontare con l'affidabilità inter-coder umana e di validare per sottogruppi. — [arXiv 2402.05129](https://arxiv.org/pdf/2402.05129)
- [P] Cheng, Mayya e Sedoc, "To Err Is Human; To Annotate, SILICON?" (arXiv 2412.14461): i modelli proprietari vengono deprecati e questo rende i risultati non riproducibili. Propongono un metodo di regressione per scegliere modelli open-weight di backup: per ogni task testato esiste almeno un modello open-weight senza differenze statisticamente rilevabili. — [arXiv](https://arxiv.org/abs/2412.14461)
- [P] OLAF (arXiv 2512.15979): molti studi riportano solo accuratezza grezza senza κ, e prompt, versioni del modello e parametri di decoding sono sotto-specificati. Sono minacce alla replicabilità. — [arXiv](https://arxiv.org/html/2512.15979v1)

### Inferences
Protocollo raccomandato per l'Osservatorio:
1. **Campione gold.** Campione stratificato di circa 1.000–2.000 CIG, per strato (regex positivo per brand, CPV ICT senza brand, CPV non ICT, importo, anno), con sovra-campionamento dei casi generici.
2. **Doppia annotazione umana** su almeno il 20% del campione, con κ di Cohen e linee guida scritte. Il κ umano è il tetto di riferimento.
3. **Metriche per classe** (precision, recall, F1) e per strato. Va riportato anche il tasso di "non determinabile".
4. **Correzione delle stime aggregate.** La spesa stimata va corretta con precision e recall misurate, con intervalli di confidenza bootstrap.
5. **Riproducibilità.** Model ID pinned, temperatura 0, prompt versionato nel repo, output in cache (JSONL per CIG con hash del prompt). Un modello open-weight di backup va validato sullo stesso gold.
6. **Pipeline a cascata**, per costi e trasparenza: prima regex e gazetteer (deterministici, auditabili), poi LLM solo sul residuo ambiguo.

### Gaps
- Non ho trovato benchmark di costo specifici per gli LLM sui testi di appalto italiani; le cifre di Gilardi riguardano tweet e news.

## 4. Gestione dell'ambiguità: descrizioni generiche, multi-prodotto, convenzioni Consip, rivenditori

### Takeaway
Non ho trovato letteratura specifica. La soluzione difendibile è una tassonomia con livelli di confidenza espliciti e una gerarchia di segnali ausiliari: testo, poi convenzione o accordo quadro Consip, poi identità del fornitore, poi CPV, poi importo. I contratti non attribuibili vanno riportati come quota "non determinata", non vanno imputati.

### Cited Findings
- [P] OCDS raccomanda di classificare gli item con schemi esistenti come il CPV. L'estensione tenderClassification colloca il CPV nel tender (scheme, id, description). Sono utili come campi ausiliari. — [OCDS codelists](https://standard.open-contracting.org/latest/en/schema/codelists/); [tenderClassification](https://extensions.open-contracting.org/en/extensions/tenderClassification/master/)

### Inferences
- **Etichette proposte**: `brand_esplicito` (alta confidenza), `brand_da_convenzione` (es. la convenzione o l'AQ Consip identifica il prodotto), `brand_da_fornitore` (fornitore mono-brand, es. Aruba diretto), `ict_generico_non_attribuibile`, `multi_prodotto`. Il contratto multi-prodotto va contato in ogni brand con un flag, senza ripartire l'importo, salvo regole documentate.
- **Rivenditori.** Il caso dei 66 fornitori diversi per Microsoft 365 conferma che la giurisdizione va attribuita al prodotto. Il rivenditore va registrato come dimensione separata (valore locale catturato).
- **Accordi quadro e convenzioni Consip.** Il CIG derivato e quello padre permettono di ereditare il prodotto. Va costruita una tabella mantenuta a mano delle iniziative Consip (es. licenze Microsoft, SPC Cloud, Public Cloud IaaS/PaaS) con i prodotti coperti.

### Gaps
- Non ho trovato fonti che documentino le convenzioni Consip a livello di prodotto né metodi pubblicati per attribuire la spesa nei contratti multi-prodotto.

## 5. Strumenti open source

### Takeaway
Esistono classificatori CPV aperti e non LLM (ad esempio TF-IDF più regressione logistica per la Spagna) e pipeline "GPT per etichettare + SVM addestrato". Non ho trovato strumenti aperti per l'attribuzione di brand o giurisdizione: va sviluppato in proprio.

### Cited Findings
- [P] hsilvosa/openplacsp-cpv-classifier (Hugging Face): suggerisce le divisioni CPV dal testo degli avvisi spagnoli con feature TF-IDF di parole e caratteri e 45 classificatori logistici lineari. L'autore avverte che non sostituisce il CPV legale. — [HF](https://huggingface.co/hsilvosa/openplacsp-cpv-classifier)
- [P] Garijo et al., SEPLN 2022: confronto di approcci di classificazione CPV su dati del Tesoro spagnolo, con un research object aperto. — [w3id](https://w3id.org/dgarijo/ro/sepln2022)
- [S] Applicazione accademica su dati TED: l'utente etichetta automaticamente con GPT, corregge a mano, poi addestra una SVM. È un pattern utile (distillazione verso un modello economico e auditabile). Dettagli non verificati. — [TIB AV](https://av.tib.eu/media/68534)
- [P] OCDS Cardinal (Rust, MIT): calcola red flag e indicatori su dati OCDS. Non è un classificatore. — [Cardinal docs](https://cardinal.readthedocs.io/)

### Gaps
- Non ho verificato i repo GitHub di Open Contracting Partnership, opentender/DIGIWHIST o eventuali "procurement-classifier" generici.
