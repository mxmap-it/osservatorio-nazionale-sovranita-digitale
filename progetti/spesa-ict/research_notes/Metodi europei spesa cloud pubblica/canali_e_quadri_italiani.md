# Canali d'acquisto cloud della PA italiana e quadri di classificazione (ricerca 27/10/2026)

Legenda: **[P]** letto sulla fonte primaria in questa sessione; **[S]** fonte secondaria o snippet di ricerca; **[K]** solo conoscenza pregressa, non verificata (da usare come pista). Sessione breve (circa 15 chiamate): diverse domande restano aperte e sono elencate nei Gap.

## 1. Consip: canali per il cloud e tracciabilità in ANAC

### Takeaway
Il canale Consip principale per l'hyperscale pubblico è l'**Accordo Quadro "Cloud IaaS e PaaS"** (ID 2213, poi **ID 2746 "Cloud IaaS e PaaS 2"**). I lotti sono **per CSP**: il Lotto 1 di ID 2746 riguarda i servizi **Amazon** ed è stipulato con **Fastweb**. Una sola delibera di adesione basta quindi a dare insieme prodotto (AWS) e rivenditore (Fastweb) e a classificare la spesa per giurisdizione del prodotto. Il predecessore SPC Cloud Lotto 1 (RTI TIM/Poste/HPE) è scaduto nel 2022.

### Cited Findings
- ARERA, determinazione 76/DAGR/2026: adesione al **Lotto 1 dell'AQ Consip ID 2746 "Cloud IaaS e PaaS 2"**, il cui Lotto 1 (**CIG B6A19F425E**) "ha ad oggetto i servizi Amazon ed è stato stipulato con Fastweb S.p.a.". Importo 1.830.000 € IVA inclusa per 36 mesi. Base normativa: obbligo Consip ex L. 208/2015 art. 1 c. 512 [P] — [ARERA 76/2026/DAGR](https://www.arera.it/fileadmin/allegati/docs/26/76-26-dagr.pdf)
- La gara Consip **ID 2213** è un "accordo quadro per la fornitura di servizi cloud IaaS e PaaS in un modello di erogazione pubblico" con servizi connessi e professionali. La documentazione cita un Lotto 1 e i lotti 7–11, con capitolati distinti; esistono almeno sei "tranche" [S, titoli documenti Consip] — [Errata corrige n. 2](https://www.consip.it/sites/default/files/bandi/documentazione_non_firmata/ID%202213%20-%20Gara%20public%20cloud%20-%20Errata%20corrige%20n%202%20e%20Chiarimenti.pdf); [VI tranche](https://www.consip.it/sites/default/files/bandi/documentazione_non_firmata/ID%202213%20-%20VI%20TRANCHE%20Chiarimenti%20e%20Errata%20corrige%207.pdf)
- Un RTI Engineering–Leonardo–SMI si sarebbe aggiudicato i lotti 8 e 10 dell'AQ Cloud IaaS e PaaS [S] — [Startmag](https://www.startmag.it/innovazione/cloud-cosa-fara-engineering-con-leonardo-per-regioni-inps-inail-banca-ditalia-e-consob/)
- AgID ha aderito più volte al Lotto 1 (Compute, Storage, Network, Security, Container, Database ecc.) [S, snippet; atti non letti] — [trasparenza AgID 6754](https://trasparenza.agid.gov.it/download/6754.html)
- SPC Cloud Lotto 1 (IaaS/PaaS/SaaS): aggiudicato all'RTI Telecom Italia, Poste Italiane, Postel, Postecom e HPE Services Italia, massimale 500 M€. Contratto quadro in scadenza il 20/7/2022, esteso al 31/12/2022 [S, snippet da comunicato AgID/Consip e determine] — [comunicato AgID-Consip](https://www.agid.gov.it/sites/default/files/repository_files/ufficio_stampa/consip_e_agid_sottoscritti_i_contratti_per_la_connettivita_e_aggiudicati_i_primi_due_lotti_della_gara_per_i_servizi_cloud.pdf); [ART det. 138/2021](https://autorita-trasporti.it/wp-content/uploads/2021/07/det_00138_05-07-2021.pdf)

### Inferences
- In un AQ con lotti per CSP, ogni contratto derivato (appalto specifico, con CIG derivato proprio) eredita il prodotto dal lotto. Per questo è necessaria una **tabella di decodifica "CIG accordo quadro/lotto → CSP"** (per ID 2746: B6A19F425E → AWS). Nella BDNCP il CIG derivato dovrebbe riportare il riferimento al CIG dell'AQ o della convenzione e la modalità "adesione ad accordo quadro/convenzione" [K: verificare il nome esatto del campo nel dataset ANAC, ad esempio `cig_accordo_quadro`].
- Il fornitore registrato in BDNCP è il **rivenditore** (Fastweb), che è italiano. Una vista basata solo sul vincitore classificherebbe come "italiana" una spesa AWS. È il caso più pulito per mostrare la differenza tra vista per fornitore e vista per prodotto.

### Gaps
- Mappa completa lotti → CSP → aggiudicatario per ID 2213 e ID 2746 (Microsoft Azure, Google, Oracle, eventuali CSP UE), con date di attivazione e scadenza: non trovata. Fonti da consultare: pagine "iniziativa" su consip.it e acquistinretepa.it e avvisi di aggiudicazione GUUE/TED.
- Licenze Microsoft via Consip (convenzione/AQ "Licenze Software Multibrand", "Microsoft Enterprise Agreement" [K]), convenzione Data Center e categorie MePA del cloud: non verificate.
- Open data Consip (dati.consip.it, dataset "contratti/ordinativi per iniziativa"): non consultati in questa sessione. Restano da verificare il contenuto (ordinativi con CIG derivato?) e la licenza.

## 2. Polo Strategico Nazionale (PSN)

### Takeaway
Il PSN offre tre famiglie di servizi su tecnologia hyperscaler USA: **Public Cloud PSN Managed** (Google, Oracle), **Hybrid Cloud on PSN Site** (Microsoft Azure) e **Secure Public Cloud** (Azure, Google, AWS). Accanto a queste c'è il private cloud/Industry Standard su infrastruttura PSN. La spesa PSN va quindi scomposta per **voce di catalogo**: il contraente (PSN S.p.A., italiano) non dice nulla sulla giurisdizione della tecnologia.

### Cited Findings
- Pagina PSN "Cloud services with CSP": Public Cloud PSN Managed con Google e Oracle, su data center PSN o region italiane, gestito da personale PSN "con separazione logico-fisica" e chiave root controllata per region, fruibile anche in modalità disconnessa. Hybrid Cloud on PSN Site con Microsoft Azure (Azure Arc come piano di controllo; SOC, CERT e key management PSN). Secure Public Cloud su Azure, Google Cloud e AWS in region italiane, con chiavi gestite da PSN fuori dal controllo del CSP. Altri CSP potranno aggiungersi [P] — [PSN](https://polostrategiconazionale.it/en/solutions/cloud-services-with-csp)
- Il Piano dei Fabbisogni PSN (2025) contiene tabelle dedicate a "Secure Public Cloud on Google GCP" e "on Amazon AWS" e una voce "altri servizi a listino". L'Allegato C della Convenzione del 24/08/2022 è l'"Offerta economica – Catalogo dei Servizi" [S, snippet; docx non letto] — [Piano dei Fabbisogni v1 2025](https://www.polostrategiconazionale.it/app/uploads/2025/08/PSN_PianoDeiFabbisogni-v1.docx); [Piano dei Fabbisogni 2023](https://www.polostrategiconazionale.it/app/uploads/2023/11/PSN_PianoDeiFabbisogni.pdf)
- Deck PSN di ottobre 2025: il private cloud si paga a canone annuo fatturato bimestralmente, i servizi CSP a consumo, e prezzi e modalità sono fissati dalla Convenzione [S, snippet] — [Deck PSN 2025](https://www.polostrategiconazionale.it/app/uploads/2025/10/Draft_-v12_2025-DECK-Polo-Strategico-Nazionale-1.pdf); [Guida alla Convenzione](https://www.polostrategiconazionale.it/app/uploads/2025/08/PSN_Guida-alla-Convenzione_.pdf)
- Nel 2023 Corriere Comunicazioni descriveva Public Cloud PSN Managed come Oracle + Google, in linea con la pagina attuale [S] — [CorCom](https://www.corrierecomunicazioni.it/pa-digitale/polo-strategico-nazionale-ecco-tutti-i-servizi-erogati-dai-cloud-service-provider/)
- Dal rapporto di sintesi esistente: delibera Corte dei conti 30/2024/G (investimento PSN di 723 M€ a carico dell'aggiudicatario, convenzione di 13 anni) e contratto MAECI–PSN (10 anni, circa 54,8 M€) [P, già in `reports/Misure europee sovranità digitale.md`].

### Inferences
- Lente di prodotto proposta: (a) Industry Standard / private cloud su infrastruttura PSN → "IT/UE, stack da verificare" (hardware e hypervisor possono essere USA); (b) Hybrid on PSN Site → Microsoft; (c) PSN Managed → Google o Oracle; (d) Secure Public Cloud → il CSP scelto. Servono i Piani dei Fabbisogni o i contratti di adesione con il dettaglio delle voci. Il solo importo contrattuale non basta.
- Il PSN è un caso intermedio: operatore e chiavi italiani, tecnologia USA. Va tenuto come bucket a sé, coerente con i "4 bucket" mxmap.

### Gaps
- Listino (Allegato C) non letto. Elenco pubblico dei contratti di adesione PSN (ente, importo, voci) non trovato. Gli atti vanno cercati nelle sezioni "Amministrazione trasparente" degli enti o in BDNCP; il CIG del contratto di adesione PSN va verificato.
- Compagine societaria (TIM, Leonardo, CDP, Sogei) non riverificata in questa sessione [K].

## 3. PNRR M1C1 Investimenti 1.1 e 1.2

### Takeaway
La Misura 1.2 finanzia la migrazione dei sistemi, dati e applicazioni delle PA locali verso "servizi cloud qualificati", con candidature su PA Digitale 2026. In questa sessione non ho trovato un dataset aperto delle candidature con CUP: il repository GitHub ipotizzato non esiste (404).

### Cited Findings
- La Misura 1.2 ha l'obiettivo di migrare sistemi, dati e applicazioni delle amministrazioni locali verso servizi cloud qualificati. Le candidature si presentano online su PA Digitale 2026, che genera la domanda; l'avviso riaperto 1.2 aveva scadenza il 6/12/2024 [S] — [Provincia di Trento](https://www.provincia.tn.it/News/Approfondimenti/Missione-1-Componente-1-Investimenti-1.1-e-1.2-Abilitazione-e-facilitazione-migrazione-al-Cloud); [lentepubblica](https://lentepubblica.it/pa-digitale/finanziamenti-pnrr-2024-cloud-comuni/)
- Documento DTD "PA digitale 2026 – le misure" [S, PDF non letto] — [innovazione.gov.it](https://assets.innovazione.gov.it/1643296664-pa-digitale-2026_le-misure.pdf)
- `github.com/italia/padigitale2026-opendata` → HTTP 404 [P, verificato].
- Dal rapporto esistente: secondo la Corte dei conti, in ReGIS "non si registrano pagamenti" sui progetti a costi reali; il DTD dichiara oltre 280 PA centrali e oltre 12.700 PA locali migrate [P/S].

### Inferences
- Le Misure 1.2 sono finanziate a **lump sum** (importo forfettario per pacchetto di servizi migrati [K]). L'importo PNRR misura quindi il finanziamento, non il pagamento al fornitore. Il collegamento CUP → CIG (BDNCP riporta il CUP sui CIG) resta il ponte verso il fornitore effettivo.

### Gaps
- Open data ufficiali delle candidature/finanziamenti (padigitale2026.gov.it, sezione open data; OpenCoesione/Italia Domani "progetti PNRR" con CUP), importi per avviso e definizione formale di "migrazione ammissibile" (lift&shift, SaaS qualificato): non verificati in questa sessione [K: esistono su italiadomani.gov.it i dataset "Progetti" con CUP].

## 4. ACN – Regolamento unico cloud (27/6/2024)

### Takeaway
Il Regolamento definisce **tre classi di dati** (ordinari/critici/strategici) e **quattro livelli** per i servizi (AC/QC1–4) e per le infrastrutture (AI1–4). I dati strategici richiedono livello 3 o 4. Il testo **non contiene un requisito di proprietà o sede non extra-UE** del fornitore. I requisiti di "sovranità" sono operativi: metadati in UE, notifica e autorizzazione degli accessi extra-UE e, solo a QC4, HYOK, autonomia operativa e vetting del personale. Per questo il livello QC non può fare da proxy della giurisdizione.

### Cited Findings (tutti [P], testo del Regolamento, firmato 27/06/2024, applicabile dal 1/8/2024, ex art. 33-septies c. 4 DL 179/2012 — [ACN regolamentocloud](https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud))
- Art. 3: sono "ordinari" i dati la cui compromissione non produce i pregiudizi delle lettere b e c; "critici" quelli con pregiudizio a funzioni rilevanti per società, salute, sicurezza pubblica e benessere economico; "strategici" quelli con pregiudizio alla sicurezza nazionale. I dati soggetti al Perimetro (DL 105/2019) sono strategici. Per i dati soggetti al D.lgs. 65/2018 (NIS): critici se non a valenza nazionale, strategici se a valenza nazionale.
- Art. 12: livelli infrastruttura AI1–AI4 (Allegato 4, sezioni 6–9). Ordinari su tipologie a–d, critici su b–d, strategici su c–d, cioè **AI3/AI4**. Art. 15: servizi cloud AC1–AC4 (Allegato 4, sezioni 2–5) con la stessa regola: strategici solo su **AC3/AC4**.
- Allegato 4, §4: QC3 richiede le caratteristiche dell'Allegato 3 per i dati strategici e le certificazioni ISO 22301, ISO/IEC 20000 e CSA STAR Level 2, emesse da enti accreditati in uno Stato membro UE o in un paese con mutuo riconoscimento.
- Allegato 4, §5 (QC4): HYOK con HSM presso l'amministrazione o presso un terzo da essa scelto; accesso esclusivo dell'amministrazione alle chiavi e ai dati in chiaro; HSM dedicato; il fornitore deve essere "autonomo nella fornitura del servizio cloud, disponendo di proprie capacità per operare l'infrastruttura fisica e logica"; vetting del personale privilegiato, con l'elenco a disposizione dell'amministrazione, che può chiederne la rimozione.
- Requisiti "S" (Allegati 2 e 3): il fornitore segnala ad ACN e all'amministrazione **ogni richiesta di accesso da parte di entità extra-UE** e concede l'accesso solo con autorizzazione esplicita dell'amministrazione. Per i dati strategici "tutte le tipologie di metadata devono essere trattate mediante infrastrutture localizzate sul territorio dell'Unione europea" (salvo quelli necessari all'erogazione di specifici servizi). In generale i metadati vanno trattati in UE salvo motivate ragioni.
- Dal rapporto esistente: AWS è qualificata QC2 [P, fonte del fornitore].

### Inferences
- Nel testo letto (ricerca per parole chiave) non risultano criteri di capitale o controllo societario come quelli di SecNumCloud. Un hyperscaler USA può in teoria arrivare a QC3; a QC4 i vincoli HYOK e di autonomia lo rendono praticabile solo tramite operatori come il PSN. Nella metodologia: livello QC = asse "sicurezza", distinto dall'asse "giurisdizione".

### Gaps
- Catalogo ACN (catalogocloud.acn.gov.it): la home risponde con un'app Astro di circa 12 MB, con LoginPage e componenti per fornitori. Nell'HTML non compaiono nomi di fornitori né livelli QC, e non ho trovato endpoint JSON/CSV o export. **Nessun open data strutturato verificato**; servirebbe ispezionare le chiamate di rete col browser [P sul fallimento].
- Numero del decreto "21007/24": non visibile nell'estratto (il testo riporta solo la firma del 27/06/2024) ed è confermato solo da fonte secondaria [S] — [Studio Stefanelli](https://www.studiolegalestefanelli.it/it/approfondimenti/servizi-cloud-per-le-pa-e-protezione-dei-dati-cosa-prevede-il-nuovo-regolamento-acn/).

## 5. AgID "La spesa ICT nella PA" 2024/2025

### Takeaway
Non disponibile: il PDF 2024 reindirizza ancora a `manutenzione.agid.gov.it` (HTTP 302, 27/10/2026) [P sul fallimento]. Restano valide solo le cifre del comunicato già nel rapporto di sintesi (panel di 77 enti, spesa da circa 3,8 a quasi 5 mld €, 44% in innovazione).

### Cited Findings
- Redirect verificato — [PDF AgID](https://www.agid.gov.it/sites/agid/files/2025-05/Rapporto_La_spesa_ICT_nella_PA_2024.pdf)

### Gaps
- Categorie di spesa e cifre cloud del rapporto: non lette. Riprovare più tardi o cercare una copia su Wayback.
