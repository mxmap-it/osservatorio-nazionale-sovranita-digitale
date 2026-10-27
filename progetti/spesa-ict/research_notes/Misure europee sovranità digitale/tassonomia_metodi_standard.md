# Tassonomia dei metodi e degli standard per misurare la sovranità digitale

Note di ricerca, 2026-10-27, prodotte con poche ricerche. Etichette di affidabilità usate qui:
- **[P]** = verificato in fonte primaria
- **[S]** = fonte secondaria (stampa, blog di vendor, aggregatore)
- **[K]** = conoscenza di fondo del ricercatore, NON verificata in questa sessione. Da controllare prima di pubblicare.

Le fonti primarie non sono state lette direttamente: il PDF della Commissione sul Cloud Sovereignty Framework non è stato estratto (stream binari compressi), e il referenziale ANSSI SecNumCloud e il Regolamento ACN non sono stati aperti. Nessuna affermazione qui sotto ha quindi la piena etichetta [P].

## Famiglie di metodi e quale funziona meglio per una misura basata sulla spesa

### Takeaway
Esistono 7 famiglie: indici compositi, misura dell'infrastruttura, stime di quota di mercato, survey, analisi di appalti/spesa, flussi di scambio di servizi/BoP, framework di valutazione/certificazione. Per una misura basata sulla spesa, il nucleo è l'analisi di appalti/spesa (CPV + aggiudicatario → produttore → capogruppo ultima → giurisdizione). I framework di certificazione servono come scala ordinale, i dati BoP/servizi come controllo top-down della coerenza.

### Cited Findings
- **Indici compositi.** Kaloudis (2022) costruisce un modello gerarchico a componenti/sotto-componenti, alimentato da dati secondari a livello di Stato, e lo valida confrontandolo con indici esistenti [S, abstract] — [EJOBSAT](https://ejobsat.cz/artkey/ejo-202202-0007_from-quality-to-quantity-how-can-digital-sovereignty-be-parsed-into-measurable-components.php). Rodríguez Pita et al. (ITS 2025) propongono un Digital Sovereignty Framework quantificabile per valutare le politiche nel tempo [S, abstract] — [UPM ITS 2025](https://oa.upm.es/92000/1/ITS-E-2025-54.pdf). Esempi pratici: Digital Dependence Index; ECFR European Sovereignty Index, con un ambito tecnologia [S] — stessa ricerca, [Living Library](https://thelivinglib.org/?p=58311). TYPO3 ha proposto un indice a livello di prodotto e osserva che le applicazioni composte da più componenti non sono ancora misurabili [S] — [TYPO3](https://typo3.org/article/conception-of-an-index-for-digital-sovereignty-based-on-the-example-of-typo3).
  - Punti di forza: comparabilità tra Paesi, comunicazione efficace.
  - Punti deboli: pesi arbitrari, misure a posteriori e lente.
- **Critica metodologica.** Shashkov et al. osservano che i metodi esistenti misurano a posteriori, sono quantitativi, ignorano le caratteristiche qualitative delle tecnologie e soffrono di ritardi nella raccolta dati [S, abstract] — [Shashkov et al.](https://vestnik-pp.samgtu.ru/0207-3676/article/view/682746).
- **Misura dell'infrastruttura** (DNS/MX, hosting, ASN, CA TLS, geolocalizzazione IP): è la famiglia a cui appartiene MxMap/CAmap, insieme a EDRIX, Nextcloud DSI e SEAL (solo citati, come da istruzioni).
  - Punti di forza: osservabile, riproducibile, censuaria.
  - Punti deboli: misura l'uso, non la spesa. La geolocalizzazione IP non coincide con la giurisdizione [K].
- **Analisi di appalti/spesa.** Tussell (UK) ricava la spesa cloud da avvisi di aggiudicazione, inclusi i dati TED riusati su licenza CE. Per il 2026 riporta £2,6 mld di nuove aggiudicazioni cloud (+52% nominale, +23% reale in quattro anni) [S] — [Tussell snapshot](https://www.tussell.com/public-sector-cloud-market-snapshot-2026), [avviso Tussell (credito TED)](https://client.tussell.com/award_notices/1071065-916b6362707c2648df6b6fbd540f193d-cloud-platform-service-aws-environment). Il data dive di Computer Weekly citato da TNW riporta:
  - 95% degli enti pubblici UK spende in cloud hyperscale;
  - 55% di £17,7 mld (£9,9 mld) va a hyperscaler o loro rivenditori [S] — [The Next Web](https://thenextweb.com/news/uk-cloud-dependency-billion-pound-risk).

  La metrica che mette insieme "hyperscaler o rivenditori" è esattamente l'attribuzione di prodotto e non di rivenditore che usa il nostro progetto.
- **Flussi di scambio di servizi / BoP.** TiSMoS è un dataset del WTO, non dell'OECD. Copre oltre 200 economie, dal 2005 al 2022, con 55 categorie di servizi e una ripartizione per modo di fornitura. Combina dati BoP, statistiche sulle affiliate estere (FATS) e un modello di allocazione Eurostat-WTO. Gli input OECD (TEC) ed Eurostat (SBS) sono usati per stimare il modo 1 [S/P, pagina del dataset] — [WTO data TiSMoS](https://data.wto.org/en/dataset/tismos), [presentazione WTO](https://www.cepal.org/sites/default/files/presentations/trade-service-gats-mode-supply-wto-tismos-dataset-wto.pdf).
  - I servizi "digitalmente erogabili" si individuano partendo dalle voci EBOPS 2010 come limite superiore; le quote di modello e quelle da survey possono divergere molto [S] — [IMF Handbook](https://www.imf.org/-/media/files/publications/books/2023/english/hmdtea.pdf.md).
  - La BEA ammette che non è possibile sapere quale quota di questi scambi sia davvero erogata in digitale [S] — [BEA](https://www.bea.gov/sites/default/files/papers/Trends%20in%20Digitally%20Enabled%20Services.pdf).
- **Framework di valutazione/certificazione:** vedi la sezione successiva.

### Inferences
- Per una misura basata sulla spesa: il **metodo primario** è appalti/spesa (ANAC BDNCP/TED + Consip + SIOPE). La **validazione** usa la capogruppo ultima (GLEIF L2) per l'attribuzione di giurisdizione e la qualificazione ACN/SecNumCloud o il SEAL come asse ordinale. Il **controllo top-down** usa le importazioni di servizi ICT da BoP (Eurostat/Banca d'Italia, EBOPS SI) per verificare l'ordine di grandezza della spesa extra-UE.
- Le stime di quota di mercato (Synergy, IDC, Gartner) e le survey (Eurostat ICT usage in enterprises, che ha un modulo cloud [K]) sono utili solo come contesto: sono proprietarie, o misurano l'uso e non la spesa o la giurisdizione.

### Gaps
- Nessun TED-based cloud study a livello UE trovato in questa sessione (es. studi EuroStack, Open Contracting, Cloud Infrastructure Services Providers in Europe/CISPE). Andrebbe cercato in modo mirato.
- Survey Eurostat "ICT usage in enterprises" e "cloud computing services" (isoc_cicce_*): codici del dataset non verificati.

## Come i framework principali definiscono "sovrano" / "immune al diritto extra-UE"

### Takeaway
La soglia quantitativa più precisa e citabile è quella di SecNumCloud 3.2: capitale e diritti di voto detenuti da soggetti extra-UE non oltre il 24% per singolo soggetto e il 39% in aggregato, più un criterio di immunità alle leggi extraterritoriali. L'EUCS ha eliminato i requisiti di sovranità e il livello high+ nella bozza del marzo 2024. L'EU Cloud Sovereignty Framework della Commissione (v1.2.1, ottobre 2025) usa 8 obiettivi SOV con livelli SEAL 0–4, e il livello complessivo è il minimo tra gli obiettivi.

### Cited Findings
- **SecNumCloud 3.2 (ANSSI).**
  - Soglie di capitale e voto: individuale ≤24% e collettiva ≤39% per entità extra-UE; il punto è allineato alla bozza EUCS di allora [S] — [Generation-NT](https://www.generation-nt.com/actualites/secnumcloud-referentiel-anssi-securite-souverainete-2071995), [Le Monde Informatique](https://www.lemondeinformatique.fr/les-dossiers/lire-secnumcloud-bientot-remplace-par-l-eucset-8201-1454.html).
  - Il testo è ripreso in un emendamento all'Assemblée nationale per le entità NIS2 (si tratta di una proposta) [P per l'emendamento] — [Assemblée nationale](https://www.assemblee-nationale.fr/dyn/17/amendements/1112/CSCYBER/121.pdf).
  - Più di 350 requisiti, più un criterio di immunità legale contro CLOUD Act e simili [S] — [Qovery](https://www.qovery.com/blog/sovereign-cloud-options-french-public-sector-secnumcloud-vs-aws-europe).
  - Bleu e S3NS puntano alla qualificazione restando sotto il 24% [S] — [Le Monde Informatique](https://www.lemondeinformatique.fr/les-dossiers/lire-secnumcloud-bientot-remplace-par-l-eucset-8201-1454.html).
  - Requisiti su sede legale UE, personale e localizzazione dei dati in UE: [K], da verificare nel §19.6 del referenziale ANSSI.
- **EUCS (ENISA).** Le bozze 2023 limitavano la localizzazione al nuovo livello high+. La bozza del 22 marzo 2024 ha rimosso i requisiti di sovranità, sostituiti da attestazione per il livello high, e ha eliminato high+ [S] — [R Street](https://www.rstreet.org/research/cybersecurity-score-european-cybersecurity-certification-scheme-for-cloud-services-eucs/), [Digital SME](https://www.digitalsme.eu/?p=138991), [Eurosmart](https://www.eurosmart.com/?p=19100).
  - Conflitto di fonti: InCyber descrive una versione di novembre 2023 con "high" = almeno un datacenter UE e "high+" = tutti i datacenter in UE [S] — [InCyber](https://incyber.org/en/article/cloud-european-union-slightly-loosens-sovereignty-criteria/).
  - A giugno 2024 l'EUCS è stato tolto dall'agenda in attesa di una guida su come gli Stati membri possano aggiungere requisiti nazionali [S] — [Euronews](https://www.euronews.com/2024/06/18/decision-on-cloud-certification-scheme-delayed-to-mid-july).
  - Stato al 2026: non verificato.
- **EU Cloud Sovereignty Framework (Commissione, DIGIT).**
  - 8 obiettivi: strategico, legale/giurisdizionale, dati e AI, operativo, supply chain, tecnologia, sicurezza/compliance, ambientale.
  - SEAL da 0 a 4. L'ente appaltante fissa un minimo per obiettivo e il livello complessivo è il più basso raggiunto. Un punteggio pesato classifica poi le offerte conformi.
  - Versione 1.2.1, ottobre 2025; guida attuativa del 1° giugno 2026.
  - SOV-2 riguarda l'esposizione ad autorità estere; SOV-3 riguarda la localizzazione del trattamento e il controllo delle chiavi [S] — [arc42 quality](https://quality.arc42.org/standards/eu-cloud-sovereignty-framework), [heise](https://heise.de/-10922224).
  - Pesi riportati da un aggregatore (SOV-1 15%, SOV-2 10%, SOV-3 10%, SOV-4 15%, SOV-5 20%, SOV-6 15%, SOV-7 10%, SOV-8 5%) e definizioni SEAL (0 = controllo esclusivo non UE … 4 = pieno controllo UE senza dipendenze critiche): [S], da verificare nel PDF della Commissione — [PDF Commissione](https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en) (scaricato ma non estratto), [copia ppc.land](https://ppc.land/content/files/2025/11/Cloud-Sovereignty-Framework.pdf).
  - È stato usato per la gara cloud sovrano delle istituzioni UE da 180 mln € [S].
  - Nota: un blog ayedo parla di "SEAL-1…5", probabilmente per errore.
- **ACN, Italia.** Esistono 4 livelli di qualificazione cloud, da QC1 a QC4 (Allegato C). La classificazione dei dati è ordinari / critici / strategici. QC2 è richiesto per i dati critici su cloud pubblico (Determinazione ACN 307/2022). La qualifica vale 36 mesi (Regolamento unico n. 21007 del 27/06/2024) [S] — [AWS blog](https://aws.amazon.com/blogs/security/aws-achieves-qi2-qc2-qualification-to-host-critical-data-and-workloads-from-the-italian-public-administration/), [Segretari comunali / iusmanagement](https://www.segretaricomunalivighenzi.it/?p=13242), [Cybersecurity360](https://www.cybersecurity360.it/?p=61434).
  - L'associazione QC1 = ordinari, QC2 = critici, QC3 = strategici, con QC4 non descritto, è [S] non confermata.
  - Il dato più rilevante: AWS, MongoDB e Salesforce sono qualificati QC2. **La qualificazione ACN quindi non discrimina per giurisdizione fino a QC2.**
- **C5 (BSI), ENS (Spagna), Gaia-X labels:** non ricercati in questa sessione. Secondo [K]:
  - C5 è un catalogo di controlli con "criteri di trasparenza" sulla giurisdizione, non un requisito di proprietà.
  - ENS ha livelli bajo/medio/alto senza criteri di proprietà.
  - Le Gaia-X Label 2/3 richiedevano rispettivamente dati in UE e immunità al diritto extra-UE, con sede UE.

  Tutto da verificare.

### Inferences
- Una scala comparabile per il nostro livello 5 ("infrastruttura nativa europea") corrisponde a SEAL-4 e a SecNumCloud con soglia 24/39. Il nostro livello 1 ("US global cloud") corrisponde a SEAL-0/1.
- Conviene adottare la soglia 24%/39% come definizione operativa di "controllo extra-UE" nella regola di attribuzione, citandone la fonte.

### Gaps
- Testo primario non letto per: definizioni SEAL e pesi, §19.6 di SecNumCloud, Allegato C ACN (QC3/QC4 e requisiti di controllo estero), Gaia-X Labelling Criteria, C5:2020, ENS (RD 311/2022).

## Classificazioni per la comparabilità (Tussell, studi TED, EuroStack, Eurostat)

### Takeaway
Per i prodotti si usano CPV (unico codice comune a TED, ANAC e Tussell) e, per la parte statistica, EBOPS 2010/CPA. Per gli enti si usa COFOG/ESA S.13. Per proprietà e giurisdizione: capogruppo ultima secondo GLEIF Level 2 (consolidamento contabile), soglia di controllo 24/39, ISO 3166-1 + appartenenza UE/SEE.

### Cited Findings
- **GLEIF Level 2.** Registra la "capogruppo ultima di consolidamento contabile", cioè l'entità di livello più alto che redige il bilancio consolidato; la capogruppo diretta è quella di livello più basso. La scelta di definizioni contabili (convergenza IFRS/US GAAP) è dovuta alla loro applicabilità e verificabilità [P, blog GLEIF] — [GLEIF](https://www.gleif.org/en/newsroom/blog/taking-the-next-step-legal-entity-identifier-regulatory-oversight-committee-proposes-process-for-collecting-data-on-direct-and-ultimate-parents-of-legal-entities), [ontologia GLEIF L2](https://gleif.org/ontology/pylodev2/GLEIF_L2.html).
- Sotto IFRS il consolidamento si applica in genere quando c'è controllo. L'UN Global Group Registry accetta una capogruppo ultima solo da GLEIF, annual report, filing regolamentari o sito aziendale [P] — [UNSD GGR User Guide](https://unstats.un.org/unsd/business-stat/GGR/GGR-User-Guide-June22.pdf).
- **TiSMoS / EBOPS 2010** per il confronto con flussi di servizi: vedi la prima sezione [S/P] — [WTO](https://data.wto.org/en/dataset/tismos).
- **Tussell** usa dati TED [S] — [Tussell](https://client.tussell.com/award_notices/1071065-916b6362707c2648df6b6fbd540f193d-cloud-platform-service-aws-environment).
- **[K] da verificare:**
  - CPV divisioni 72 (servizi IT) e 48 (pacchetti software), con 72300000 (dati), 72317000 (archiviazione), 72400000 (Internet), 72222300, 48800000 (sistemi informativi e server); "cloud" non ha un codice CPV dedicato nel CPV 2008.
  - UNSPSC segmento 43 / famiglia 8111 (servizi IT), 81112000 (servizi dati online).
  - COFOG 01–10 per la funzione dell'ente.
  - Definizione OECD del settore ICT (ISIC Rev.4 26, 58.2, 61, 62, 63.1) / NACE Rev.2.1.
  - EBOPS SI (servizi di telecomunicazione, informatici e d'informazione), con SI2 = servizi informatici.
  - Regolamento UE 2019/452 sul FDI screening: "investitore estero", controllo "diretto o indiretto" (art. 4) senza soglia fissa.
  - CLOUD Act (18 U.S.C. §2713): si applica ai provider soggetti alla giurisdizione USA, indipendentemente dal luogo del dato.
  - FISA 702 (50 U.S.C. §1881a): si applica agli "electronic communication service provider" USA; riautorizzata ad aprile 2024 (RISAA) fino ad aprile 2026, stato successivo da verificare.

### Inferences
- Schema di codifica proposto:
  1. capogruppo ultima del **produttore** (GLEIF L2, con fallback su annual report);
  2. paese ISO 3166 della capogruppo, raggruppato in IT / UE-SEE / extra-UE;
  3. flag "esposto al diritto extraterritoriale" se la capogruppo è USA, oppure se un soggetto extra-UE supera il 24%/39%;
  4. corrispondenza con i 4 bucket mxmap e il livello 1–5.

  Pubblicare la tabella CPV → categoria (IaaS/PaaS/SaaS/datacenter/servizi) permette il confronto con TED/Tussell. Una tabella ponte CPV → EBOPS SI permette il confronto con Eurostat/BoP.

### Gaps
- Meta-analisi su Internet Policy Review, Telecommunications Policy e Policy & Internet: individuata solo la SLR di Fratini et al. (271 articoli; [S] tramite risultati di ricerca, URL non recuperato). Pohle & Thiel (2020, IPR, "Digital sovereignty") è un riferimento concettuale noto [K], non verificato qui.
- Metodologia EuroStack: non ricercata.
- Codici CPV e UNSPSC: da verificare sul regolamento CPV (CE 213/2008) e sul codeset UNSPSC.
