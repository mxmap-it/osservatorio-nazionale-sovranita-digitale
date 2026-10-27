# Tassonomia: cloud esterno vs infrastruttura propria nella spesa pubblica, e fattibilità della misura

*Note di ricerca, 27/10/2026. Legenda: [P] verificato su fonte primaria (anche solo tramite estratto del motore di ricerca della pagina primaria); [S] seconda mano (stampa, aggregatori); [K] solo conoscenza pregressa, da verificare. Sessione breve (circa 12 chiamate): molte voci sono da approfondire. AgID (agid.gov.it) è stato di nuovo irraggiungibile: redirect 302 a manutenzione.agid.gov.it il 27/10/2026.*

## 1. Definizioni standard da adottare

### Takeaway
Conviene usare NIST SP 800-145 come ossatura concettuale: 5 caratteristiche, 3 modelli di servizio (IaaS, PaaS, SaaS), 4 modelli di deployment. Il criterio operativo di Eurostat ("cloud a pagamento, fornito via Internet, su server condivisi o dedicati") serve a delimitare cosa conta come **spesa** cloud. Il cloud privato "dedicato" erogato da un terzo va in un bucket separato.

### Cited Findings
- NIST SP 800-145 (Mell e Grance, 2011): il modello si compone di 5 caratteristiche essenziali, 3 modelli di servizio e 4 modelli di deployment. NIST dichiara che la tassonomia non prescrive metodi di erogazione [P] — [NIST CSRC](https://csrc.nist.gov/pubs/sp/800/145/final); [PDF](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)
- Eurostat (indagine ICT nelle imprese) conta servizi "payable": pay-per-user, pay-per-use o prepagati. Il fornitore può erogarli da server condivisi (cloud pubblico) o da un'infrastruttura a uso esclusivo (cloud privato). Imprese UE che usano cloud a pagamento nel 2025: 52,74% (+7,42 p.p. sul 2023). L'Italia è tra i paesi oltre il 70% [P] — [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Cloud_computing_-_statistics_on_the_use_by_enterprises)
- TBM Taxonomy v4.0: il cost pool "Cloud Vendor" (provider di public cloud IaaS/PaaS/SaaS esterni) è separato dal cost pool "Hardware". Quest'ultimo comprende acquisti non capitalizzati, leasing, manutenzione e supporto, **ammortamento degli acquisti capitalizzati** [P] — [TBM placemat v4.0 (WA state)](https://cybersecurity.wa.gov/sites/default/files/2023-07/TBM%20Taxonomy%20v4.0%20Placemat.pdf)
- TBM v5.0.1: i cost pool classificano il "cosa si compra" (allineati al piano dei conti); le Resource Tower classificano il "per cosa si usa" (Servers, WAN, Help desk…). Public cloud e SaaS hanno un trattamento dedicato [S] — [TBM Council](https://www.tbmcouncil.org/learn-tbm/tbm-modeling/mapping-to-solutions/); [Finout](https://www.finout.io/blog/technology-business-management)

### Inferences
- Proposta di bucket per analisi-spesa-ict, ricalcati su TBM: (1) cloud pubblico esterno IaaS/PaaS; (2) SaaS in abbonamento; (3) cloud qualificato "dedicato" o housing di terzi (PSN, in-house regionali); (4) licenze software perpetue + manutenzione; (5) hardware (acquisto/leasing/manutenzione); (6) opere e impianti di data center; (7) personale ICT interno; (8) servizi professionali e outsourcing di gestione.
- Nei dati di appalto, SaaS e licenza perpetua si distinguono soprattutto da testo e oggetto (canone, abbonamento, "subscription", durata) più che dal CPV: i CPV 48xxxxxx coprono sia pacchetti software sia licenze; 72xxxxxx coprono i servizi. Serve classificazione testuale (LLM o regole) sull'oggetto del contratto [K].

### Gaps
- Il testo di ISO/IEC 22123-1:2023 (vocabolario cloud) e le tassonomie Gartner/IDC dei "public cloud services" sono a pagamento: non verificati.
- Il perimetro del "EU Cloud Sovereignty Framework" non è stato verificato in questa sessione (vedi il report "Misure europee").

## 2. Come le indagini ufficiali classificano la spesa ICT

### Takeaway
Tra le fonti trovate, solo i Paesi Bassi pubblicano in modo sistematico la spesa ICT statale divisa per tipologia, personale interno compreso. L'Italia (AgID) distingue corrente da capitale, ma lo fa su un panel. Nessuna fonte trovata isola i capex dei data center propri come voce autonoma.

### Cited Findings
- AgID, "La spesa ICT nella PA 2024" (maggio 2025): spesa del panel da circa 3,8 a quasi 5 mld € tra 2022 e 2025, attribuita al PNRR. In tutti i comparti la spesa corrente prevale sulla spesa in conto capitale e va soprattutto a manutenzione e assistenza hardware e software [S, sintesi del comunicato] — [AgID notizia](https://www.agid.gov.it/it/notizie/spesa-ict-nella-pa-pubblicato-il-nuovo-report-di-agid); [PDF](https://www.agid.gov.it/sites/agid/files/2025-05/Rapporto_La_spesa_ICT_nella_PA_2024.pdf) (non letto: sito in manutenzione)
- Paesi Bassi, JBR / Rijks ICT-dashboard: le "ICT-kosten" coprono hardware, software, connessioni voce e dati, personale ICT. Il dataset aperto 2015–2020 è diviso per capitolo di bilancio e per tipologia: acquisto hw/sw, inhuur, servizi ICT esternalizzati, connessioni, gestione e manutenzione. Nel 2018: 3,11 mld €, di cui circa 907 mln di personale ICT interno e circa 2,207 mld materiali; esclusi i sistemi d'arma. Per il 2020 open data (oltre 3 mld) e JBR (2.803 mln) divergono [S/P] — [Jaarrapportage Bedrijfsvoering Rijk 2016](https://kennisopenbaarbestuur.nl/binaries/kennisbankopenbaarbestuur/documenten/rapporten/2017/05/01/jaarrapportage-bedrijfsvoering-rijk-2016/jaarrapportage-bedrijfsvoering-rijk-2016.pdf); [officielebekendmakingen blg-1122351](https://zoek.officielebekendmakingen.nl/blg-1122351.pdf); [Tweede Kamer via berthub](https://berthub.eu/tkconv/getraw/2021D40185)
- Germania: il Bundesrechnungshof (2025) giudica la IT-Konsolidierung Bund molto indietro sugli obiettivi. L'obiettivo di ridurre gli oltre 1.300 data center e server room federali è stato abbandonato. Già nel 2015 la Corte dei conti federale lamentava che il BMI non conoscesse inventario, affitti e costi operativi dei DC. Le cifre di costo sono in conflitto: 1 → 3,5 mld € secondo netzpolitik, 836 mln € secondo Tagesspiegel; probabilmente il perimetro è diverso [S] — [netzpolitik.org](https://netzpolitik.org/2025/bundesrechnungshof-bundesregierung-verfehlt-ziele-der-it-konsolidierung/); [Computerwoche](https://computerwoche.de/article/2748914/leere-rechenzentren-ungenutzte-router-so-verschwendet-der-bund-steuern.html)

### Inferences
- Il modello olandese (personale interno + inhuur + materiale + esternalizzato, per ministero) è il riferimento più vicino a ciò che serve all'Osservatorio per la "infrastruttura propria".
- Il caso tedesco mostra che persino un governo con un programma dedicato non conosceva il costo dei propri DC: è un argomento forte sulla difficoltà della misura.

### Gaps
- UK (CDDO, Digital Spend Controls), Francia (programmi 129/352), Istat "ICT nelle PA": non verificati in questa sessione.
- Categorie esatte del rapporto AgID (presenza di una voce "cloud" o "data center", nota metodologica): non leggibili, sito in manutenzione. Da riprovare.

## 3. Fonti italiane per l'infrastruttura propria

### Takeaway
L'Italia ha un censimento fisico dei DC (2019–2020) ma nessun costo associato. SIOPE ha codici utilizzabili per l'hardware (U.2.02.01.07) e per i servizi informatici (U.1.03.02.19), ma nessun codice specifico per il cloud: la spesa AWS finisce nello stesso codice dei servizi generici.

### Cited Findings
- Censimento AgID (concluso febbraio 2020): 1.252 DC di quasi mille PA; 35 candidabili PSN, 27 in Gruppo A, 1.190 in Gruppo B. L'82% delle PA dichiara un DC di proprietà, il 18% usa DC di terzi. Età: 13% pre-1996, 28% 1996–2005, 46% 2006–2015, 13% post-2015. Fase precedente (2018): 860 DC [P] — [AgID 20/02/2020](https://www.agid.gov.it/it/agenzia/stampa-e-comunicazione/notizie/2020/02/20/cloud-pa-concluso-il-censimento-ict); [AgID 19/07/2018](https://www.agid.gov.it/it/agenzia/stampa-e-comunicazione/notizie/2018/07/19/piano-triennale-conclusa-seconda-fase-del-censimento-ict-pa)
- Le PA che non hanno partecipato al censimento sono classificate d'ufficio in Gruppo B [S] — [Agenda Digitale](https://www.agendadigitale.eu/infrastrutture/data-center/datacenter-della-pubblica-amministrazione-il-punto-su-censimento-e-azioni-agid/)
- Stima "oltre 11.000 DC tradizionali, circa 95% non conformi" senza fonte nominata: inattendibile [S] — [lentepubblica](https://lentepubblica.it/cittadini-e-imprese/pa-digitale-e-fabbisogno-tecnologico-chi-fornisce-data-center/)
- SIOPE U.2.02.01.07.001 "Server": usato da ARPA Piemonte per l'acquisto di server (cap. "Acquisto di attrezzature informatiche", 50.755,20 €, determina 849 del 6/11/2025) [P, uso del codice; la descrizione del livello IV non è verificata su fonte MEF] — [ARPA Piemonte](https://bandi.arpa.piemonte.it/sites/default/files/allegati/bandi-appalti/2025/227/Determina_n.%20849%20del%2006.11.2025.pdf)
- SIOPE U.1.03.02.19.003 usato dalla Regione Siciliana per un contratto di infrastruttura cloud AWS (DDA n. 12 del 31/01/2023, 5.707,43 €) [P] — [Regione Siciliana](https://regione.sicilia.it/index%2ephp/istituzioni/servizi-informativi/decreti-e-direttive/dda-n-12-31012023). U.1.03.02.19.005 usato per l'assistenza hardware di server e switch (Provincia di Reggio Emilia) [P] — [Provincia RE](https://protocollo.provincia.re.it/AttiVisualizzatore/download/determina/107010?fId=109712)
- PNRR 1.1/1.2: fino a 1,9 mld €. Per la 1.2: Comuni 734 mln, scuole 130 mln, ASL 235 mln [S]. A ottobre 2024 oltre 4.000 enti migrati [P] — [CS DTD-PSN 10/10/2024](https://polostrategiconazionale.it/app/uploads/2024/10/CS-DTD-PSN-Cloud-10-ottobre-2024.pdf). Luglio 2026: oltre il 75% delle circa 13.000 PA ha migrato in cloud qualificato, e il PSN ha servito oltre 280 PA centrali e strutture sanitarie [S] — [Corriere Comunicazioni](https://www.corrierecomunicazioni.it/digital-economy/cloud/pnrr-province-citta-metropolitane-e-consorzi-comunali-migrano-in-cloud/); [Agenda Digitale](https://www.agendadigitale.eu/cittadinanza-digitale/il-cloud-si-impone-tra-le-amministrazioni-locali-italiane-grazie-al-pnrr-i-dati/)

### Inferences
- SIOPE consente una vista **pagato** su hardware (conto capitale) contro servizi informatici (corrente). Il cloud però va riconosciuto dal beneficiario del pagamento (SIOPE+ riporta il beneficiario? [K], da verificare) o dall'incrocio con il CIG.
- I DC del Gruppo B (1.190) sono l'universo "infrastruttura propria da dismettere". Incrociandoli con le PA beneficiarie della 1.2 si ottiene una stima di quanta infrastruttura propria sia stata spenta, ma non del suo costo.

### Gaps
- Il testo ufficiale del piano dei conti integrato (DPR 132/2013 / allegati MEF-RGS) per U.2.02.01.07 e U.1.03.02.19 non è stato letto: le voci di V livello (es. "servizi di gestione e manutenzione applicazioni", "servizi di rete", "servizi per i sistemi e relativa manutenzione") sono da verificare. Un codice specifico per il cloud non risulta [K].
- Lotti Consip (SPC Cloud lotto 1, Accordo Quadro Public Cloud IaaS/PaaS, convenzione PSN, gare Data Center): non verificati qui.
- Nessuna serie ufficiale sul numero di DC dismessi dopo il 2020.

## 4. Metodi per stimare il costo dell'infrastruttura propria

### Takeaway
Il riferimento metodologico più maturo è TBM (cost pool → tower, con ammortamento nel pool hardware). Le Corti dei conti (GAO USA, BRH DE) mostrano che anche con un mandato di legge il costo dei DC propri resta stimato male: gli inventari si ottengono, i costi no.

### Cited Findings
- USA: FDCCI (2010) → DCOI (OMB, dopo FITARA 2014). GAO verifica ogni anno inventari e risparmi. Nel 2017 raccomanda di riportare i risparmi in modo coerente tra i canali; nel 2018, 14 agenzie non raggiungevano nessun target di ottimizzazione; nel 2021 chiede di rivedere la metrica di utilizzo dei server. Dal 2016, 126 raccomandazioni, 110 attuate [P] — [GAO-18-264](https://www.gao.gov/assets/gao-18-264.pdf); [GAO-23-105946](https://www.gao.gov/assets/gao-23-105946.pdf)
- TBM: ammortamento dei capitalizzati nel cost pool hardware, cloud vendor separato [P] — [TBM v4.0 placemat](https://cybersecurity.wa.gov/sites/default/files/2023-07/TBM%20Taxonomy%20v4.0%20Placemat.pdf)
- BRH 2015: il BMI non conosceva affitti e costi operativi dei DC federali [S] — [netzpolitik.org](https://netzpolitik.org/2025/bundesrechnungshof-bundesregierung-verfehlt-ziele-der-it-konsolidierung/)

### Inferences
- Convenzione pratica proposta, [K] da validare: server e storage ammortizzati in 5 anni, client in 3–4, rete in 5–7, impianti DC in 10–15. Per gli enti in contabilità finanziaria (comuni, regioni) l'ammortamento non è nel bilancio di cassa. Va ricostruito dagli impegni in conto capitale (U.2.02.01.07) spalmati sugli anni.
- Il TCO di un DC proprio = ammortamento hw + ammortamento impianti/opere + energia + manutenzione + personale + licenze. Energia e quota di personale sono quasi mai separabili dai dati pubblici.

### Gaps
- La metodologia di calcolo dei risparmi DCOI (appendici GAO-20-279 / GAO-21-212) non è stata letta.
- Gli studi UK NAO e NL Algemene Rekenkamer sulla consolidazione DC non sono stati verificati.

## 5. Valutazione di fattibilità

### Takeaway
Cloud esterno: fattibile da ANAC/BDNCP + SIOPE, con classificazione testuale. Infrastruttura propria: misurabile solo **in parte**. La componente acquisti (hardware, manutenzione, opere DC) si ricava da CPV e SIOPE. Personale, energia e ammortamenti richiedono indagini o ricerca documentale per progetto (piani triennali ICT degli enti, PIAO, relazioni sulla gestione).

### Cited Findings
- La spesa ICT della PA è prevalentemente corrente e va a manutenzione e assistenza hw/sw [S] — [AgID notizia](https://www.agid.gov.it/it/notizie/spesa-ict-nella-pa-pubblicato-il-nuovo-report-di-agid)
- I codici SIOPE distinguono già hardware (U.2.02.01.07) e servizi informatici (U.1.03.02.19), ma il cloud AWS cade nei servizi generici [P] — [Regione Siciliana](https://regione.sicilia.it/index%2ephp/istituzioni/servizi-informativi/decreti-e-direttive/dda-n-12-31012023)

### Inferences (matrice di fattibilità)
| Componente | Fonte | Fattibilità |
|---|---|---|
| Cloud IaaS/PaaS/SaaS esterno | BDNCP (CPV 72xxxxxx, 48xxxxxx + testo oggetto + aggiudicatario/rivenditore) | Alta, previa classificazione testuale |
| Hardware server/storage | CPV 30200000, 48820000 (server), 30233000 (storage); SIOPE U.2.02.01.07 | Alta per gli acquisti, media per l'attribuzione "DC proprio" (anche client e PC finiscono qui) |
| Manutenzione hw/sw | CPV 50300000, 72250000…; SIOPE U.1.03.02.19 | Media: si mescola con servizi di gestione esterni |
| Opere e impianti DC | CPV 45xxxxxx con testo "data center/CED"; 31xxxxxx (UPS), 39717200 (condizionamento) | Bassa-media: solo ricerca testuale |
| Energia del DC | Non separabile | Molto bassa |
| Personale ICT interno | Conto annuale RGS (profili non ICT-specifici) | Bassa: serve un'indagine |
| Ammortamento | Ricostruito dagli impegni in conto capitale | Stima modellistica |

- Per le PA grandi (ministeri, regioni, in-house) conviene un agente di ricerca per singolo progetto (piani triennali, PIAO, delibere CED) su un campione, non sull'universo.

### Gaps
- Non verificato se SIOPE+ espone il beneficiario e il CIG negli open data (servirebbe per legare pagato e contratto).
- Nessuna fonte pubblica trovata sui costi energetici dei CED della PA italiana.
