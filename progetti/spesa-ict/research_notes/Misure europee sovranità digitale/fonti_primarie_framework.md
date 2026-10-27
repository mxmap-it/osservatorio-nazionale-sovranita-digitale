# Fonti primarie: framework di valutazione della sovranità digitale e letteratura sulla misurazione

Legenda: [P] = verificato sul testo primario in questa sessione (2026-10-27); [S] = fonte secondaria; [M] = solo da memoria/training del ricercatore, NON verificato, da controllare prima di usarlo.

## 1. Commissione europea: Cloud Sovereignty Framework (v1.2.1, ottobre 2025)

### Takeaway
I testi primari sono due: il framework originale di gara, "Version 1.2.1 – Oct. 2025", DG DIGIT, Cloud III DPS; e il documento successivo "Implementation guidance" con il calcolatore. Il framework ha 8 obiettivi (SOV-1..SOV-8) e livelli SEAL-0..SEAL-4. Il SEAL complessivo è il livello più basso ottenuto tra gli obiettivi e funziona da soglia minima. Lo score ponderato (somma 100%) serve solo a confrontare le offerte che superano quella soglia.

### Cited Findings
- [P] Testata: "European Commission, Directorate-General for Digital Services, Luxembourg – Cloud Sovereignty Framework – Version 1.2.1 – Oct. 2025". Il framework attinge a CIGREF Trusted Cloud Referential v2, Gaia-X, ENISA/NIS2/DORA, "Cloud de Confiance" e "Souveräner Cloud". — [PDF v1.2.1 (copia ospitata da ppc.land)](https://ppc.land/content/files/2025/11/Cloud-Sovereignty-Framework.pdf)
- [P] Gli 8 obiettivi: SOV-1 Strategic (ancoraggio all'ecosistema UE/SEE, stabilità della proprietà, influenza sulla governance); SOV-2 Legal & Jurisdictional (esposizione a leggi extra-UE con portata extraterritoriale, "e.g., US CLOUD Act, Chinese Cybersecurity Law"); SOV-3 Data & AI (controllo delle chiavi solo da parte del cliente, confinamento in UE "with no fallback to third countries"); SOV-4 Operational; SOV-5 Supply Chain (origine geografica dei componenti); SOV-6 Technology (apertura, lock-in); SOV-7 Security & Compliance; SOV-8 Environmental Sustainability. — stesso PDF
- [P] Fattori che contribuiscono a SOV-1: organi decisionali nella giurisdizione UE; garanzie contro il cambio di controllo; quota di finanziamento da fonti UE; investimenti, occupazione e valore creato nell'UE. — stesso PDF
- [P] Pesi nello score ("Weight in Scoring"): SOV-1 15%, SOV-2 10%, SOV-3 10%, SOV-4 15%, SOV-5 20%, SOV-6 15%, SOV-7 10%, SOV-8 5%; totale 100%. Nel PDF la colonna dei pesi è estratta nell'ordine 15/10/10/15/20/15/10/5. L'abbinamento ai singoli SOV coincide con quello delle fonti secondarie (Ayedo, BlackBerry). Il testo motiva i pesi bassi di SOV-2 e SOV-7 col fatto che la procedura contiene già "significant safeguards" in quei domini. — stesso PDF; conferma [S] [Ayedo](https://ayedo.de/en/cloud-sovereignty-framework/), [BlackBerry](https://www.blackberry.com/en/secure-communications/insights/blog/sovereignty-effective-assurance-levels-explainer)
- [P] SEAL nella v1.2.1, 5 livelli: SEAL-0 No Sovereignty (controllo esclusivo extra-UE, giurisdizione interamente extra-UE); SEAL-1 Jurisdictional Sovereignty (il diritto UE si applica formalmente ma con scarsa applicabilità pratica; controllo esclusivo extra-UE); SEAL-2 Data Sovereignty (diritto UE applicabile ed effettivo, dipendenze extra-UE materiali, controllo extra-UE indiretto); SEAL-3 Digital Resilience (attori UE con influenza significativa ma non piena, controllo extra-UE marginale); SEAL-4 Full Digital Sovereignty (pieno controllo UE, solo diritto UE, nessuna dipendenza critica extra-UE). Nell'Implementation guidance il SEAL-3 è chiamato "Technological Sovereignty". — [PDF v1.2.1](https://ppc.land/content/files/2025/11/Cloud-Sovereignty-Framework.pdf); [Implementation guidance, commission.europa.eu](https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en)
- [P] Regola di aggregazione: "The overall SEAL level is the lowest SEAL level achieved in any of the objectives". Il documento sottolinea "the prevalence of the SEAL criterion over the Sovereignty Score": la stazione appaltante fissa il SEAL minimo, e lo score confronta solo le offerte che lo raggiungono. Lo score è la somma pesata dei punti per obiettivo (punti ottenuti / punti massimi × peso). La formula nel PDF è un'immagine e l'estrazione testuale la rende illeggibile; la sua forma testuale viene da Ayedo [S]. — Implementation guidance (link sopra)
- [P] Nella gara reale il minimo richiesto era SEAL-2. Il questionario aveva 43 domande: 9 sui soli contraenti e subcontraenti (dimensioni strategica e giurisdizionale) e 19 ripetute per ogni dimensione tecnica. La valutazione deve risalire l'intera catena di subcontraenti e fornitori, hardware e open source inclusi. — Implementation guidance
- [P] Lezioni apprese: la Commissione stessa scrive che il SEAL-4 "is not today relevant… considering existing dependence to specific supply chains (chips, hardware)" e propone di allentarlo; segnala inoltre il carico di lavoro dovuto all'autodichiarazione. — Implementation guidance

### Inferences
- Per il metodo basato sulla spesa: la regola "minimo tra gli obiettivi" corrisponde a un approccio per anello più debole. Un acquisto di prodotto extra-UE erogato da un integratore italiano resta SEAL-0/1 sugli obiettivi SOV-1, SOV-2 e SOV-5. La scala a 5 livelli dell'Osservatorio può allinearsi a SEAL-0..4.
- La giurisdizione del prodotto (IT/UE/extra-UE) è un indicatore proxy soprattutto per SOV-1, SOV-2 e SOV-5, che insieme valgono il 45% dello score.

### Gaps
- Il calcolatore (xlsx) e le tabelle domanda per domanda nella guidance sono immagini o allegati e non sono stati estratti.
- La copia della v1.2.1 letta qui viene da ppc.land; non ho trovato un URL ufficiale della Commissione per la v1.2.1. Il link commission.europa.eu porta alla guidance.

## 2. ANSSI SecNumCloud 3.2: proprietà, controllo e immunità al diritto extra-UE (§19.6)

### Takeaway
Non sono riuscito a leggere il testo primario: il PDF di cyber.gouv.fr restituisce una pagina HTML a curl e un contenuto vuoto a WebFetch. Le soglie del 24% individuale e del 39% collettivo sono quindi solo [S].

### Cited Findings
- [S] La v3.2 è datata 8 marzo 2022 e introduce i criteri di protezione dal diritto extra-europeo; il §19.6 e gli allegati 1 e 2 risultano modificati. — [URL ufficiale (non scaricabile in sessione)](https://cyber.gouv.fr/uploads/2014/12/secnumcloud-referentiel-exigences-v3.2.pdf); [CMS Law](https://cms.law/fr/fra/news-information/secnumcloud-un-referentiel-technico-juridique-desirable-bientot-incontournable)
- [S] Il fornitore deve avere sede legale in uno Stato membro UE. Capitale sociale e diritti di voto non possono essere detenuti, direttamente o indirettamente, da entità extra-UE oltre il 24% individualmente e il 39% collettivamente. — [Generation NT](https://www.generation-nt.com/actualites/secnumcloud-referentiel-anssi-securite-souverainete-2071995); la soglia del 39% è riportata da una sola fonte in ricerca
- [S] I servizi "joint venture" con tecnologia USA (Bleu, S3NS) sono ammissibili: la v3.2 non vieta la tecnologia americana, ma solo il controllo extra-UE. — [Le Monde Informatique](https://www.lemondeinformatique.fr/les-dossiers/lire-secnumcloud-bientot-remplace-par-l-eucset-8201-1454.html)
- [S] Un post di Landot Avocats (agosto 2026) segnala un'evoluzione del referentiel nel 2026. — [Landot](https://blog.landot-avocats.net/2026/08/17/important-notamment-pour-certains-marches-publics-evolution-du-referentiel-dexigences-relatif-aux-prestataires-de-services-dinformatique-en-nuage/)

### Inferences
- SecNumCloud distingue tra il controllo societario (soglie) e l'origine della tecnologia. Per il metodo dell'Osservatorio conviene distinguere tra prodotto extra-UE e operatore UE.

### Gaps
- Testo letterale del §19.6 non letto: va scaricato a mano dal browser.
- Contenuto della possibile revisione 2026 non verificato.

## 3. ACN: qualificazione cloud per la PA italiana

### Takeaway
L'atto è il "Regolamento unico per le infrastrutture digitali e i servizi cloud per la PA", adottato con Decreto direttoriale ACN n. 21007/24 del 27 giugno 2024 e in vigore dal 1° agosto 2024 [S]. Prevede la classificazione dei dati in ordinari, critici e strategici e livelli QC1–QC4 (privati) e AC1–AC4 (pubblici), con requisiti nell'Allegato 4. I requisiti specifici su controllo estero e giurisdizione non sono stati verificati sul testo primario.

### Cited Findings
- [S] Il nome, il numero del decreto, la data e l'entrata in vigore sono quelli indicati sopra. Sono "strategici" i dati e servizi la cui compromissione può comportare un rischio elevato per la sicurezza nazionale. La classificazione va aggiornata almeno ogni due anni. La qualificazione dura al massimo 36 mesi e l'ACN decide in genere entro 60 giorni. — [Agenda Digitale](https://www.agendadigitale.eu/infrastrutture/il-nuovo-regolamento-per-il-cloud-della-pa-novita-e-impatti/)
- [S] I servizi privati ottengono i livelli QC1–QC4 tramite verifica ex ante e iscrizione al catalogo ACN; gli operatori pubblici rilasciano dichiarazioni di adeguatezza AC1–AC4. I livelli sono cumulativi (QC2 richiede QC1). Le infrastrutture passano da QI a AI. — [QuiFinanza](https://quifinanza.it/innovazione/regolamento-unico-infrastrutture-servizi-cloud/832868/); [Salesforce](https://www.salesforce.com/it/blog/salesforce-qualificata-qc2-per-acn-agenzia-nazionale-per-la-cybersecurity/)
- [M] Corrispondenza tra livelli e dati, da verificare: QC1 corrisponde ai dati ordinari, QC2 ai critici, QC3 e QC4 agli strategici, e il QC4 aggiunge requisiti di controllo e giurisdizione. Sempre da memoria [M]: già la Determinazione ACN 307/2022 prevedeva, per i servizi che trattano dati strategici, garanzie su sede e controllo nell'UE e su protezione da accessi extra-UE. Secondo la Strategia Cloud Italia 2021, il PSN ospita dati strategici e critici in data center sul territorio nazionale ed è gestito da una società a controllo pubblico (TIM, CDP, Leonardo, Sogei). Nessuno di questi punti è verificato in sessione.

### Gaps
- Il testo dell'Allegato 4 (requisiti QC3/QC4 su controllo estero e localizzazione) e le regole PSN non sono stati letti dalla fonte primaria (acn.gov.it).

## 4. EUCS: stato al 2026

### Takeaway
I requisiti di sovranità e il livello "high+" sono stati eliminati nella bozza del marzo 2024. Non ho trovato una fonte primaria che attesti l'adozione del regolamento di esecuzione al 2026. La revisione del Cybersecurity Act ("CSA2", proposta a gennaio 2026) potrebbe reintrodurre un livello di sovranità [S, fonte vendor].

### Cited Findings
- [S] La bozza del 22 marzo 2024 ha rimosso i requisiti di sovranità e, con essi, il livello high+. Gli Stati membri possono applicare regole proprie, che però restano fuori dalla certificazione. — [InCyber](https://incyber.org/en/article/cloud-european-union-slightly-loosens-sovereignty-criteria/); [Hogan Lovells](https://service.betterregulation.com/sites/default/files/engage.hoganlovells.com-EUCS%20controversial%20data%20sovereignty%20issues%20continue%20to%20drive%20debate%20for%20cloud%20services.pdf); [R Street](https://www.rstreet.org/research/cybersecurity-score-european-cybersecurity-certification-scheme-for-cloud-services-eucs/)
- [S] Secondo 6clicks, la proposta CSA2 (gennaio 2026) reintrodurrebbe un livello di sovranità nell'EUCS, con la Francia come promotrice. Fonte vendor, non verificata. — [6clicks](https://www.6clicks.com/resources/blog/csa2-is-raising-the-stakes-on-sovereignty-and-french-enterprises-are-taking-notice)

### Gaps
- Manca una fonte primaria (ENISA/Commissione/Gazzetta ufficiale UE) sull'adozione formale dell'EUCS e sullo stato di CSA2.

## 5. BSI C5 (DE) ed ENS (ES)

### Takeaway
Non verificato in sessione: le conclusioni qui sotto vengono solo da memoria [M].

### Cited Findings
- [M] BSI C5:2020 non pone requisiti di proprietà o controllo. Impone però criteri di trasparenza: il fornitore deve dichiarare sede del trattamento, giurisdizione e obblighi di divulgazione verso autorità, e il cliente valuta. Il C5:2025 (bozza/rilascio 2025) non ha introdotto soglie di controllo estero. Da verificare su bsi.bund.de.
- [M] ENS (Real Decreto 311/2022) è un quadro di misure di sicurezza a livelli (básica, media, alta) senza criteri di nazionalità o controllo. Le guide CCN-STIC per i servizi cloud non impongono la proprietà UE. Da verificare.

### Gaps
- Nessuna lettura primaria. Per C5 e ENS la giurisdizione va trattata come elemento di trasparenza, non come criterio di esclusione, finché non sarà verificato.

## 6. Letteratura accademica sulla misurazione della sovranità digitale

### Takeaway
Esiste una revisione sistematica (Fratini et al., 271 articoli) che però è concettuale e non propone indicatori. Diverse fonti affermano che manchi un framework quantitativo consolidato. Gli indici esistenti (ECFR, Kaloudis) sono pochi e non sono stati letti in sessione.

### Cited Findings
- [S] Fratini, S., Hine, E., Novelli, C., Roberts, H., Floridi, L., "Digital Sovereignty: A Descriptive Analysis and a Critical Evaluation of Existing Models". La rivista è, secondo memoria [M], Digital Society (Springer), 2024. Revisione sistematica di 271 articoli peer-reviewed su Google Scholar. Individua quattro modelli (rights-based, market-oriented, centralisation, state-based) e conclude che nessuno coniuga regolazione completa e reattività all'innovazione. Non propone indicatori. — [The Living Library](https://thelivinglib.org/?p=58311)
- [S] Roberts, H., Cowls, J., Casolari, F., Morley, J., Taddeo, M., Floridi, L. (2021), "Safeguarding European values with digital sovereignty", Internet Policy Review 10(3), DOI 10.14763/2021.3.1575. Analisi di politiche, non di misure. — [policyreview.info](https://policyreview.info/cite/1575)
- [M] Pohle, J., Thiel, T. (2020), "Digital sovereignty", Internet Policy Review 9(4), DOI 10.14763/2020.4.1532. Saggio concettuale (sovranità statale, economica, individuale), senza indicatori. Da verificare.
- [M] Floridi, L. (2020), "The Fight for Digital Sovereignty: What It Is, and Why It Matters, Especially for the EU", Philosophy & Technology 33, pp. 369–378. Concettuale. Da verificare.
- [S] Kaloudis, M. (2022), "Sovereignty in the Digital Age – How Can We Measure Digital Sovereignty and Support the EU's Action Plan?". La rivista è, secondo memoria [M], New Global Studies. Propone indicatori; contenuto non letto. — citato in [ITS 2025 (UPM)](https://oa.upm.es/92000/1/ITS-E-2025-54.pdf)
- [S] Esiste un working paper ITS 2025 (UPM) dedicato alla misurazione. Dichiara che "a robust framework for measuring digital sovereignty quantitatively has not been developed". — [UPM](https://oa.upm.es/92000/1/ITS-E-2025-54.pdf)
- [S] Un'altra revisione sistematica sulla sovranità digitale UE combina analisi qualitativa e topic modelling LDA (autori non identificati). Altre proposte: l'ECFR European Sovereignty Index (2022), un indice applicato al caso TYPO3 e un approccio della HSE (2026). — [ejobsat (2022)](https://ejobsat.cz/pdfs/ejo/2022/02/07.pdf); [TYPO3](https://news.typo3.com/article/conception-of-an-index-for-digital-sovereignty-based-on-the-example-of-typo3); [HSE](https://digitlab.hse.ru/en/news/1172677256.html)

### Inferences
- Gli indicatori basati sulla spesa per giurisdizione del prodotto appaiono poco presenti nella letteratura accademica. Questa conclusione è un'inferenza dalla ricerca limitata svolta qui, non un risultato di una ricerca bibliografica esaustiva.

### Gaps
- Indicatori di Kaloudis ed ECFR non letti. Nessuna ricerca su Scopus o Web of Science.

## 7. Codici CPV ICT/cloud (CPV 2008, Reg. CE 213/2008)

### Takeaway
I codici CPV non sono stati verificati in sessione sulla fonte ufficiale (SIMAP/EUR-Lex) e restano [M]. Nel CPV 2008 non risulta un codice specifico per il cloud.

### Cited Findings
- [M] Codici, da verificare su https://simap.ted.europa.eu/cpv o sul Reg. (CE) 213/2008:
  - 48000000-8: pacchetti software e sistemi di informazione.
  - 72000000-5: servizi informatici (consulenza, sviluppo software, Internet e supporto). Sotto quest'albero: 72300000-8 servizi di elaborazione dati; 72317000-0 servizi di archiviazione dati; 72400000-4 servizi Internet; 72500000-0 servizi informatici.
  - 30200000-1: apparecchiature informatiche.
  - 32000000-3: apparecchiature radiotelevisive, comunicazioni e telecomunicazioni.
  - 50300000-8: riparazione e manutenzione di PC e apparecchiature di telecomunicazione.
  - 64200000-8: servizi di telecomunicazione.
- [M] Il cloud viene di solito codificato con 72300000/72317000/72400000/72500000 o 48000000 (SaaS). Il CPV 2008 non è stato rivisto; la revisione è in discussione da anni.

### Gaps
- Le cifre di controllo e le descrizioni ufficiali vanno confermate sul download ufficiale del CPV prima dell'uso.
