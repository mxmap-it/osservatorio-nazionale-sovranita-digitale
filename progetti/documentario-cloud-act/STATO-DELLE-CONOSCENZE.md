# STATO DELLE CONOSCENZE — progetto documentario CLOUD Act

Aggiornato al 28 luglio 2026. Documento di controllo: separa ciò che è **verificato su fonte primaria**
da ciò che è **riportato da fonti secondarie** e da ciò che è **ancora aperto**.
Serve a decidere cosa può andare in onda e cosa no.

**Legenda affidabilità**
🟢 **A — CERTO**: fonte primaria letta direttamente. Utilizzabile in trasmissione.
🟡 **B — SOLIDO, DA CONFERMARE**: fonte secondaria affidabile o fonte primaria letta tramite intermediario. Utilizzabile con verifica finale.
🔴 **C — APERTO**: non verificato. **Non utilizzabile.**
⚫ **D — CONTRADDITTORIO**: le fonti confliggono. Da risolvere.

---

## 🟢 A — VERIFICATO SU FONTE PRIMARIA

### A1. Chi gestisce la posta delle istituzioni italiane
Interrogazione diretta dei record MX (dato pubblico, ripetibile da chiunque in cinque secondi).

| Dominio | Provider | |
|---|---|---|
| carabinieri.it | `smtp.google.com` | 🇺🇸 Google |
| poliziadistato.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| governo.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| istruzione.it | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| **acn.gov.it** | `mail.protection.outlook.com` | 🇺🇸 Microsoft |
| difesa.it | `mx.difesa.it` | 🇮🇹 propria |
| gdf.gov.it | `mercurio-e01.gdf.it` | 🇮🇹 propria |
| guardiacostiera.gov.it | `mail.guardiacostiera.gov.it` | 🇮🇹 propria |

**Come rifarlo**: `nslookup -type=MX carabinieri.it`
**⚠️ Limite da rispettare**: prova che la **posta istituzionale ordinaria** è gestita da quei fornitori.
NON prova nulla sulle reti operative/classificate, che sono separate. Non dire «Trump legge le indagini».

### A2. Il PSN è costruito sui quattro hyperscaler statunitensi
Dichiarazione del PSN stesso: «These services, currently created in partnership with **Oracle, Google,
Microsoft Azure, AWS**, may also be provided with other Cloud Service Providers in the future.»
Public Cloud PSN Managed → Oracle e Google · Hybrid Cloud → Azure · Secure Public Cloud → AWS, Azure, Google Cloud.
🔗 https://www.polostrategiconazionale.it/en/solutions/cloud-services-with-csp/

### A3. Le difese tecniche dichiarate dal PSN
«Encryption-key management **outside the CSP's control perimeter**» ·
«Confidential computing, **where activated**, makes it impossible for cloud service provider operators to
access even the data during processing».
**Da notare**: nella pagina non compare mai il CLOUD Act. E «where activated» è condizionale.

### A4. Microsoft gestisce già cloud «nazionali» operati da terzi
«National clouds are physical and logical network-isolated instances… **operated by local personnel**.»
«Microsoft is the technology provider, but **Microsoft doesn't operate the service**. 21Vianet independently
operates, provides, and manages the delivery of Microsoft cloud services… keep data within China.»
Esistono: **Microsoft Cloud for US Government** e **Azure/Office 365 operati da 21Vianet in Cina**.
🔗 https://learn.microsoft.com/en-us/partner-center/enroll/csp-national-clouds-overview

### A5. Che cosa chiede la campagna EUCS High+
Testo della lettera aperta del 10/06/2024 (estratto direttamente dal PDF): «High+ criteria» = **criteri di
immunità**; lo schema è **volontario**; «Cloud providers not meeting the High+ criteria will remain fully
able to offer their solutions to us **without any market distortion**»; «several non-EU providers are
progressively setting up corporate partnerships within the EU».
Destinatari: Stati membri, esperti ECCG, Commissione.
🔗 https://sovereignedge.eu/wp-content/uploads/2024/06/EUCS_OpenLetter_10June2024.pdf

### A6. I 62 sostenitori di EUCS High+
Iniziativa coordinata dall'ufficio di Bruxelles di **Airbus**. Italiani presenti: **Leonardo, Fincantieri,
Generali, Telecom Italia**. Presenti anche Banque de France, Crédit Agricole, Caisse des Dépôts, EDF,
OVHcloud, IONOS, Deutsche Telekom, Orange, Capgemini, Thales, Sopra Steria, Cigref, Beltug e altri.
🔗 https://eucshighplus.eu/
⚠️ Nell'elenco «Aruba» rimanda a **arubanetworks.com** (HPE, statunitense), **non** ad Aruba S.p.A. italiana.

### A7. Il regolamento ACN NON contiene alcuna clausola di immunità ✅ *(era C1, risolto)*
Letto il **testo primario integrale**: `RegolamentoCloud.pdf`, **88 pagine**, articolato (27 artt.) +
Allegati 1-4 — tutti nello stesso PDF, nessun allegato separato non letto. 326.143 caratteri analizzati.

**Scansione lessicale sull'intero testo — occorrenze:**
`extraterritoriale` **0** · `CLOUD Act` **0** · `nazionalità` **0** · `sede legale` **0** ·
`capogruppo` **0** · `capitale` **0** · `assetto proprietario` **0** · `paese terzo` **0** ·
`sovranità` **0** · `PSN`/`Polo Strategico Nazionale` **0**.

È **«ho letto il testo e il requisito non c'è»**, non «non sono riuscito a leggere il testo».

**Dove avrebbe dovuto trovarsi**: Allegato 4, §§2-5 (requisiti QC1-QC4). **Cosa c'è invece**: certificazioni
ISO (9001, 27001+27017/27018, 22301, 20000) e CSA STAR L2. L'unico requisito geografico riguarda *l'ente
certificatore*, non il fornitore — e ammette l'IAF MLA, che include **ANAB (USA)**.

**L'unica clausola sul tema** — PR.DS-01 15_S (All. 3, p. 78) / 6_S (All. 2, p. 44), **solo dati strategici**:
il fornitore «*segnala all'ACN e all'amministrazione ogni richiesta di accesso a dati o metadati da parte di
entità extra-UE*», con accesso «*solo a valle di un'autorizzazione esplicita*».
🎯 **È un obbligo procedurale che presuppone e ammette l'accesso extra-UE**, non un divieto strutturale.
Ed è **ineseguibile per costruzione**: un ordine CLOUD Act con *gag order* vieta giuridicamente al fornitore
proprio quella segnalazione. **La norma chiede una comunicazione che la legge americana proibisce.**

**Tre reperti ulteriori:**
1. Per i dati **strategici bastano QC3 o QC4** (art. 17 c. 4 lett. c). **Nessun obbligo di PSN** — mai nominato.
2. **HYOK + accesso esclusivo alle chiavi è requisito del solo QC4** (All. 4 §5.1, 18_SS/19_SS): un dato
   strategico può stare legittimamente su QC3 con il solo BYOK.
3. **Localizzazione UE derogabile** — «*salvo motivate e documentate ragioni di natura normativa o tecnica*»
   (PR.DS-01 1_O/2_O) — ed è **territoriale, non giurisdizionale**: un datacenter irlandese di controllata
   USA la soddisfa restando nel perimetro *ratione personae* del CLOUD Act.

**Confronto con SecNumCloud 3.2** (ANSSI, 8 marzo 2022, 55 pp., letto direttamente) — §19.6 «*Protection
vis-à-vis du droit extra-européen*», requisiti **cumulativi**: (a) sede statutaria + amministrazione centrale
+ stabilimento principale in UE; (b) capitale e diritti di voto extra-UE **≤24% individuale / ≤39%
collettivo**, diretti o indiretti, senza veto né nomina della maggioranza degli organi; (c) **impossibilità
tecnica** per società terza extra-UE di ottenere i dati; (d) autonomia d'esercizio o qualificazione a cascata
del subfornitore; (e) legami con governi stranieri come elemento di valutazione. Più §19.2.c: «*Les opérations
d'administration et de supervision du service doivent être réalisées depuis l'Union Européenne*».

> **ANSSI aziona tre leve: societaria, tecnica e operativa. ACN aziona solo quella tecnica in forma
> attenuata e sostituisce quella societaria con una procedurale. La leva societaria — la sola che
> neutralizzi il CLOUD Act — è integralmente assente.**

🔗 https://www.acn.gov.it/portale/cloud/regolamento-cloud-per-la-pa · 🔗 https://cyber.gouv.fr/
⚠️ **Limite dichiarato**: il catalogo `catalogocloud.acn.gov.it` restituisce una pagina di login del Portale
Fornitori e va aperto a mano (non incide sulla risposta: i requisiti sono nell'Allegato 4, letto per intero).
Nessuna determinazione successiva modificativa rinvenuta — affidabilità MEDIA su questo punto specifico.

### A8. 🔥 La gara del cloud di Stato fu vinta da Aruba e Fastweb — non dalla cordata che gestisce il PSN
**AFFIDABILITÀ ALTA** — Corte dei conti, Delib. 30/2024/G (7 febbraio 2024), p. 16, testuale:
«*il 22 giugno 2022 la gara è stata aggiudicata al RTI costituito da **Aruba e Fastweb** (mandataria);
il **7 luglio 2022**, il RTI promotore ha esercitato il **diritto di prelazione** previsto dalla procedura
di gara. Pertanto, la realizzazione e la gestione del PSN sono state affidate all'operatore economico
costituito dal raggruppamento **Sogei, Leonardo, C.D.P Equity e Tim**.*»
L'offerta vincente aveva uno sconto medio del **39,19%**.

**Il contenzioso** — TAR Lazio n. 4338/2023 dichiarò **inammissibile l'offerta del RTI TIM** per due difetti
fisici: distanza minima di 500 km fra le due region (rispettata solo sulla direttrice Pomezia–Santo Stefano
Ticino, **513 km**) e rischio sismico di **Pomezia, passata da zona 3 a 2B**. Il **Consiglio di Stato,
Sez. V, 24 ottobre 2023, n. 9210** ha confermato accertando **l'illegittimo esercizio della prelazione**;
la Corte dei conti registra che l'Amministrazione voleva impugnare anche l'accertamento, nella motivazione,
«*addirittura di un "affidamento diretto" della concessione*».
Il raggruppamento ha però **continuato a gestire il PSN**: per le opere PNRR l'art. 125 c.p.a. (richiamato
dall'art. 48 c. 4 d.l. 77/2021) esclude subentro e inefficacia del contratto — il rimedio è solo risarcitorio.
**Risarcimenti richiesti: Fastweb € 551.938.000 · Aruba € 27.126.000 · totale € 579.064.000.**

⚠️ **CONTRO-ARGOMENTO OBBLIGATORIO**: il diritto di prelazione del promotore era **previsto ex ante dalla
lex specialis** (art. 183 c. 15 d.lgs. 50/2016) e noto a tutti i concorrenti. Non fu un espediente
sopravvenuto. Il contro-contro-argomento è che il Consiglio di Stato ha accertato illegittimo *quell'esercizio*.
🔴 **DA VERIFICARE, priorità alta**: l'esito finale della domanda risarcitoria (giustizia-amministrativa.it)
e i testi integrali di TAR Lazio 4338/2023 e Cons. Stato Sez. V 9210/2023.

### A9. Il denaro non è tracciabile — ed è un'assenza documentata, non una supposizione
Scaricati i dataset ufficiali del DTD: **22.162 candidature finanziate** sulla misura 1.2 per
**€ 1.343.231.660**, venti colonne, **nessun campo fornitore**. Verifica diretta e riproducibile.
**Tre cause strutturali documentate**: (1) erogazione a *lump sum*, che elimina la rendicontazione delle
fatture; (2) il DTD si dichiara per iscritto «*estraneo al rapporto*» tra amministrazione e concessionario;
(3) **10.947 scuole e 10.887 comuni** sono stazioni appaltanti autonome.

> **La conclusione sostenibile non è «miliardi finiti in America» — non ne abbiamo la prova. È: l'Italia ha
> speso 1,9 miliardi per la sovranità digitale costruendo un sistema in cui è impossibile sapere quanta parte
> di quel denaro abbia comprato tecnologia sovrana. L'opacità è il fatto verificabile.**

⚠️ Due punti da chiarire col DTD: il totale di € 1,343 mld **eccede la dotazione di 1.000 mln**, e manca la
legenda ufficiale degli stati `E`/`R`/`A`.

### A10. Composizione del catalogo ACN — Google è il primo fornitore del cloud della PA italiana
Catalogo scaricato e analizzato (**2.107 schede, 826 fornitori**): **Google Cloud Italy è il primo fornitore
con 59 servizi qualificati**. Il PSN vende sei servizi denominati alla lettera «*Secure Public Cloud Amazon
Web Services / Microsoft / Google*».
⚖️ **Contro-fatto onesto da riportare**: i **nove servizi di livello massimo (QC4)** sono tutti e soli
nativi PSN. **Sulla fascia dei dati strategici la linea tiene.** Va detto.

### A11. Non solo non esiste un vincolo a comprare europeo: la legge vieta di discriminare gli USA
**Art. 69 d.lgs. 36/2023** obbliga a trattare gli operatori statunitensi **non meno favorevolmente**, in
quanto firmatari dell'Accordo sugli appalti pubblici dell'OMC. L'**IPI (Reg. UE 2022/1031)** è per
costruzione **inapplicabile ai firmatari dell'AAP**: è strutturalmente cieco proprio verso il maggiore
fornitore extra-UE.

> 🔑 **Perché questo rafforza la tesi invece di indebolirla**: non si *può* escludere Microsoft per legge —
> e infatti la Francia non l'ha fatto. Ha scritto un **requisito di sicurezza** che un fornitore soggetto a
> legge extra-UE non può soddisfare se non ristrutturandosi. **La via della certificazione non è una
> preferenza: è l'unica porta compatibile con il diritto degli appalti.**

### A12. Il Data Privacy Framework **non copre** il CLOUD Act — e lo dice per iscritto ✅ *(era C6, risolto)*
È la replica standard dei fornitori: «col DPF il problema è risolto». Ora abbiamo la confutazione su fonte
primaria, e sta in tre reperti.

**1. Il DPF cede il passo, testualmente.** *DPF Principles*, Principio I.5(a), letto verbatim sul PDF del
Dipartimento del Commercio USA: «*Adherence to these Principles may be limited: (a) to the extent necessary
to comply with a **court order** or meet public interest, **law enforcement**, or national security
requirements…*»
🎯 Un mandato §2703 **è letteralmente** una di quelle cose. **Il DPF non limita il CLOUD Act: gli cede il
passo per iscritto.**

**2. Chi subisce un ordine CLOUD Act non ha accesso al tribunale del ricorso.** EO 14086, Sez. 4: una
*covered violation* è quella che «*arises from **signals intelligence activities***». Un ordine di procedura
penale non lo è → **niente DPRC**. Confermato indipendentemente da COM(2024) 451.

**3. La Commissione, certificando il DPF, non ha esaminato lo strumento.** COM(2024) 451 final (22 pp.,
letto integralmente): ricerca full-text → **0 occorrenze di «CLOUD Act»**, e testualmente «*the below
findings only concern developments in the area of **national security***».

**Il resto del quadro, tutto da fonte primaria:**
- **La Commissione aveva indicato dove si sarebbe rotto** (COM(2024) 451, conclusione, ottobre 2024):
  vigilare su rapporti PCLOB, modifiche alla 702, nomine PCLOB. **Tutti e tre sono poi saltati.**
  Contestualmente ha diradato le revisioni a **tre anni** — prossima nel **2027**.
- **PCLOB senza quorum dal 27 gennaio 2025**: prova materiale nel *Staff Report* del 25 settembre 2025,
  uscito come rapporto dello staff endorsato da **un solo** membro (Beth A. Williams).
- **Formula fissa di risposta al ricorrente** (EO 14086 §3(d)(i)(H)), verbatim: nessuna motivazione, e
  «*without confirming or denying*».
- **Latombe T-553/23** (respinto il 3/9/2025) con il limite decisivo: il Tribunale ha giudicato la situazione
  **al 10 luglio 2023**. Impugnazione depositata il 31/10/2025.
- **Trump v. Slaughter** (29 giugno 2026, 6-3) supera *Humphrey's Executor*; noyb ha chiesto il ritiro
  dell'adeguatezza lo stesso giorno, la Commissione «valuterà».
  ⚖️ **Esiste però una contro-analisi forte** (Christakis/Propp/Swire, IAPP, 8 luglio 2026) secondo cui la
  sentenza non travolge la DPRC. **Va citata per prima, non per ultima**: anticiparla ci rende inattaccabili.

⚠️ **Accessi falliti dichiarati**: eur-lex (decisione 2023/1795), curia, europarl, edpb.europa.eu, justice.gov,
federalregister.gov (l'EO è stato letto su *The American Presidency Project*). Il numero della causa d'appello
CGUE (C-703/25 P) e l'ECLI della sentenza Latombe sono **DA VERIFICARE**.
🔗 Il dossier `01b` elenca **18 URL primari** da aprire a mano.

### A13. ⚠️ L'asimmetria esiste, ma NON funziona come credevamo — tesi corretta ✅ *(era C7)*

**Tre assunti di partenza sono risultati SBAGLIATI e vanno abbandonati:**

❌ **«Il Buy American Act impedisce di comprare tecnologia europea».** Falso, e c'è la prova nel testo:
la **FAR 25.103(e)** contiene un'**esenzione esplicita per l'information technology che sia *commercial
product***. Inoltre il BAA copre solo *supplies* e materiali da costruzione, **non i servizi**. Il Berry
Amendment riguarda cibo, tessuti, calzature e bandiere.
🚨 **Se in TV diciamo «gli USA escludono per legge il software europeo», veniamo smentiti in cinque minuti.**

❌ **«FedRAMP impone la cittadinanza statunitense al personale».** Falso: l'ufficio FedRAMP ha scritto
«*there is no government-wide requirement on citizenship*». L'obbligo di dichiarare proprietà/controllo/
influenza straniera (**FOCI Declaration**, policy A2LA R311, in attuazione del §3612 del FedRAMP
Authorization Act) è imposto ai **3PAO — gli auditor**, non ai fornitori cloud. Il divieto esplicito su
cittadinanza e localizzazione esiste solo nel **DoD Cloud SRG** per i livelli IL4/IL5, cioè **solo Difesa**.
L'esclusione reale è la **somma di quattro strati**, nessuno dei quali dice «vietato agli europei».

❌ **«Il Documento 79 cinese ordina di rimuovere il software straniero».** Trappola documentata: **CSET
(Georgetown)** ha tradotto il documento SASAC n. 79/2022 e annota testualmente che «*the publicly available
version of Document 79 translated below does not mention anything about removing foreign software*». La
storia «Delete America» viene dal *Wall Street Journal* (7 marzo 2024), su **fonti anonime** e un documento
non copiabile.
✅ **Sostituirlo con la lista MIIT/CISEC del 26 dicembre 2023** — 18 CPU, 6 sistemi operativi, 11 database,
tutti cinesi: pubblica e verificabile.

**Quello che invece REGGE ed è più forte:**

🎯 **Priorità 1 da verificare a mano — potrebbe essere il fatto più forte dell'intero blocco**: contare sul
**FedRAMP Marketplace** quanti CSP con casa madre europea siano autorizzati. L'unico caso emerso è
**SAP NS2**, che è una controllata **statunitense** di SAP.
> Se confermato: **per vendere al governo americano un europeo deve diventare americano — esattamente ciò
> che l'Europa non chiede agli americani.** Questa è l'asimmetria vera, e non ha bisogno di leggi inventate.

**IPI**: attivato **una sola volta in tre anni** — Reg. esec. (UE) 2025/1197, 19 giugno 2025, contro la Cina,
dispositivi medici sopra 5 M€. **Mai contro gli USA, mai sul digitale.** L'FSR ha soglie da 250 M€,
inutilizzabile per un ente locale.
**CADA** (COM(2026) 502, 3 giugno 2026): introduce quattro livelli di sovranità e il Livello 3 richiede
«*personnel citizenship*» — **l'UE copia il meccanismo americano** — ma la preferenza europea è
dichiaratamente «*ancillary and not decisive*». Revisione delle direttive appalti slittata a settembre 2026.

⚖️ **Dato che contraddice la nostra tesi e va citato comunque**: Eurostat mostra un disavanzo UE di
**126,3 mld €** sui canoni di proprietà intellettuale, ma un **avanzo di 60,4 mld €** sui servizi di
telecomunicazione e informatica (effetto Irlanda). **Ometterlo sarebbe manipolatorio.**

**Tema scuola — il vuoto è la notizia:**
Non esiste **alcun dato pubblico** su quante scuole italiane usino Google o Microsoft. Nella misura 1.2 le
scuole sono conteggiate dentro le «oltre 12.700 PA locali e scuole»: **un target europeo certificato senza
che sia pubblico su quali infrastrutture siano finiti i dati degli studenti.**
→ FOIA al MIM + incrocio del catalogo ACN con gli avvisi PNRR: **sarebbe lo scoop del blocco**.

⚠️ **Il «lock-in di competenze» non regge come vorremmo**: nessuno studio empirico longitudinale reperito.
Esiste advocacy (FSFE, 2011) e letteratura sul lock-in *istituzionale* (LiMux/Monaco), che è altra cosa.
⚠️ **Due casi europei finiscono con un adeguamento, non con un'espulsione**: Paesi Bassi (SURF/SIVON
rinegoziano con Google) ed EDPS/Commissione. Il caso forte è il **Baden-Württemberg**, che ha davvero
rinunciato a M365 nelle scuole. Il «divieto dell'Assia 2019» fu **ritirato dopo tre settimane**, e nel
novembre 2025 l'HBDI avrebbe dichiarato M365 conforme — **verifica urgente**.

### A14. L'EUCS **non esiste ancora** — contraddizione D1 risolta ✅
**Prova decisiva, fonte primaria istituzionale**: nella proposta **COM(2026) 502 final** (*Cloud and AI
Development Act*, Bruxelles 3.6.2026) la Commissione scrive che ENISA sta sviluppando l'EUCS «*which has
**not yet been adopted***» e che «*work will resume*».
👉 **Nessun atto giuridico, non in vigore, zero certificati emessi.**

1. **Nessun livello High contiene requisiti di sovranità**: rimossi il 22 marzo 2024, **mai reintrodotti**.
   Il CADA formalizza il principio opposto: «*cybersecurity must be distinguished from sovereignty
   requirements*» e «*Certification under the Cybersecurity Act… is not suited for addressing sovereignty
   concerns*».
2. **«High+» non è mai stato un livello formale**: il Cybersecurity Act (Reg. 2019/881, art. 52) ne prevede
   tre. Era l'**etichetta negoziale** dei criteri di immunità.
3. **La sovranità è rinata altrove**: i *Union assurance levels* 1-4 del CADA (art. 16 + All. II). Il
   **livello 4** è nella sostanza l'High+ mancato — stabilimento UE, personale cittadino UE, nessun controllo
   di paese terzo, supporto tecnico solo dall'UE, SBOM, separazione effettiva capogruppo/controllate extra-UE.
   ⚠️ Ma vincola **gli appalti pubblici**, non il mercato, ed è **ancora una proposta in codecisione**.

🚨 **Su sota.io**: la pagina è stata riletta e **nella versione online oggi afferma l'opposto** di quanto
riportato in precedenza — «*Even EUCS High does not currently mandate that cloud providers be EU-incorporated
or EU-controlled*». Contiene inoltre una colonna «EUCS Status (2026)» per singoli fornitori che è
**inesistente**. **Confermato: non usare quelle tabelle come fonte.**

### A15. 🔄 L'Italia ha chiesto la sovranità — e l'ha co-scritta. Narrativa da rovesciare
**«L'Italia non ha chiesto la sovranità» è FALSO.** Va corretto ovunque.

- **Luglio 2021** — l'Italia è **coautrice con Francia, Germania e Spagna** del non-paper che aggiungeva
  **immunità dal diritto straniero** e localizzazione UE al livello «high» dell'EUCS. Prova indiretta ma
  solida: esiste un documento olandese il cui *titolo* la nomina — «*Opinion of the Netherlands on the
  non-paper by **DE, ES, FR and IT** on the EUCS requirements for immunity from non-EU laws*» (citato due
  volte nel cepInput 8/2025). Fonte sull'autoria: Kenneth Propp, Cross-Border Data Forum, 13.9.2022 —
  **fonte ostile ai requisiti, che nondimeno attesta la paternità italiana**.
- **Dicembre 2022** — l'Italia **non firma** il non-paper contrario degli undici Stati (DK, EE, FI, EL, IE,
  LV, LT, PL, SK, SE, NL).
- **15-16 aprile 2024, ECCG** — l'ACN rappresenta l'Italia; il voto sulla proposta belga che rimuove la
  sovranità è rinviato. Il **17 aprile Butti**, su *La Verità*: la proposta «*permetterebbe ai fornitori…
  anche quelli che operano sotto la giurisdizione di governi esterni all'UE, di essere certificati come
  sicuri*»; e «*altri paesi invece, tra cui l'Italia, hanno sollecitato l'adozione di standard più elevati
  e rigorosi*».
- **ACN, Relazione annuale al Parlamento**: lo schema dovrà «*contemperare le esigenze di mercato con le
  istanze di autonomia e di non dipendenza da tecnologie extra-UE*».
- **Fronte opposto italiano**: **AmCham Italy** firmataria nel maggio 2024 della dichiarazione per adottare
  l'EUCS **senza** sovranità.
- ✅ **Risolve il dubbio di A6**: **Aruba S.p.A. è firmataria certa** della lettera del **10 aprile 2024**
  con TIM (fonte Reuters). ⚠️ È una lettera **diversa** da quella del 10 giugno 2024 di eucshighplus.eu:
  per quest'ultima l'ambiguità «Aruba / arubanetworks» **resta valida**.

> **🎯 LA TESI CORRETTA, ed è più forte di quella sbagliata:**
> Il divario non è fra l'Italia e le sue parole. È **fra ciò che l'Italia ha chiesto a Bruxelles e ciò che
> ha scritto in casa propria**. Per cinque anni ha premuto per la clausola di immunità a livello europeo e
> ha perso. Negli stessi anni **non l'ha mai introdotta nel proprio schema nazionale** — l'unico strumento
> che non dipendeva dal voto di nessun altro. E ora, con il CADA, la decisione torna agli Stati membri via
> valutazione di rischio (art. 29): **quella valutazione non è ancora stata fatta.**

⚠️ **Coalizione dei dodici (dic. 2023)**: **l'elenco non esiste in fonte pubblica**. L'EUISS cita «twelve
Member States» senza nominarne alcuno tranne i Paesi Bassi. **L'esclusione dell'Italia è una deduzione
solida, non un fatto accertato** — va detto così in onda.

**Non pubblici**: il non-paper 2021, i verbali ECCG, le istruzioni di posizione ad ACN, l'elenco dei dodici.
**Due strade a maggior rendimento**: (1) **accesso agli atti al Consiglio** (Reg. 1049/2001) per il non-paper
DE/ES/FR/IT; (2) la **relazione del Governo ex art. 6 l. 234/2012** su COM(2026) 502 — atto parlamentare
pubblico che contiene la posizione negoziale italiana.

### A16. 🎯 Zero fornitori cloud europei sono autorizzati FedRAMP ✅ *(era C9, risolto)*
Verificato direttamente sull'elenco pubblico del FedRAMP Marketplace (`marketplace.fedramp.gov`,
endpoint dati `/marketplace/products/__data.json`, **684 prodotti**, 511 certificati — letto il 29/07/2026).

**Ricerca per nome — tutti ASSENTI:**
`OVHcloud` · `IONOS` · `Deutsche Telekom` / `T-Systems` · `Scaleway` · `Hetzner` · `Exoscale` ·
`Stackit` · `CloudFerro` · `Cloud Temple` · `Oodrive` · `Docaposte` · `Outscale` · `Aruba S.p.A.` ·
`Orange Business` · `Telefónica` · `Capgemini` · `Sopra Steria` · `Bleu` · `S3NS` · `Infomaniak` ·
`Nextcloud` · `Proton`

**I gruppi europei presenti ci sono tutti tramite una società statunitense costituita apposta:**
- **SAP** → *SAP National Security Services Inc. (SAP NS2)*
- **Siemens** → *Siemens Government Technologies* (che veicola anche *Mendix Cloud for Government*)
- **Software AG** → *Software AG Government Solutions*
- **Darktrace** (UK) → *Darktrace Federal Inc.*
- **Ericsson** (SE) → *Ericsson – NetCloud Federal*

> **Per vendere al governo americano un europeo deve prima diventare americano.
> È esattamente ciò che l'Europa non chiede agli americani.**

⚠️ **Falsi positivi da non ripetere**: la ricerca testuale grezza segnala «Atos» dentro *Kratos* ed
«Eviden» dentro *evidence*. **Nessuno dei due è presente.** E le occorrenze di «Aruba» sono
**Aruba Networks (HPE, statunitense)**, non Aruba S.p.A. — conferma l'avvertenza di A6.

### A17. Le scuole: il dato ce l'abbiamo già, ed è il peggiore del dataset ✅ *(era C10, non serve FOIA)*
Dai dati dell'Osservatorio, il cluster **Istruzione** è quello con la **quota extra-UE più alta di tutta
la Pubblica Amministrazione italiana**:

| Cluster | Enti | Quota extra-UE | Provider dominante |
|---|---|---|---|
| **Istruzione** | **8.321** | **77,2%** | **Google Workspace** |
| PA Centrale | 55 | 61,8% | Microsoft 365 |
| Sanità | 234 | 52,6% | Microsoft 365 |

**8.321 istituti = il 36% di tutti gli enti misurati.** È il cluster più grande, ed è quello messo peggio.

⚠️ **Precisione obbligatoria**: il dato misura il **dominio di posta istituzionale** degli istituti
registrati in IndicePA. È prova diretta della piattaforma adottata dalla scuola, **non** una misura di
quanti studenti usino quotidianamente un applicativo. Il FOIA al Ministero **non serve più**.

### A18. Come funziona davvero il protezionismo americano — non per divieto, ma per stratificazione
Censiti **25 strumenti**: **7 mordono direttamente sul cloud, 5 indirettamente, 13 no.** Il conteggio onesto
rende la mappa incontestabile.

**Ciò che NON regge (e va detto noi per primi):**
- **FAR 25.103(e)** — esenzione espressa per l'IT commerciale (base: §535(a) Consolidated Appropriations
  Act 2004). Il Buy American Act **non** blocca il software europeo.
- **15 CFR §7.4** — la lista dei *foreign adversaries* è **tassativa**: Cina, Cuba, Iran, Corea del Nord,
  Russia, regime Maduro. Le regole ICTS **non si applicano agli europei**.
- 🚨 **41 U.S.C. §1323 contiene un divieto espresso**: «*Nothing in this section shall be construed… to
  authorize the issuance of an exclusion or removal order **based solely on the fact of foreign
  ownership**.*» **È il contro-argomento più forte contro la nostra tesi: va citato per primo.**
  Non la distrugge — la costringe a essere precisa.

**Ciò che regge, ed è il meccanismo vero:**
- **32 CFR §117.11(d)** (FOCI) — *Voting Trust* e *Proxy Agreement* impongono alla capogruppo estera di
  **cedere l'esercizio del controllo societario a cittadini statunitensi con nulla osta**. È il cuore.
  *(SAP NS2 come applicazione concreta: la qualificazione «Proxy Agreement» viene da fonti secondarie,
  perché gli accordi FOCI non sono pubblici — MEDIA.)*
- **DFARS 252.239-7010(b)(3)** (gen. 2023) — dati governativi da mantenere negli Stati Uniti.
- **DoD Cloud SRG** — *US persons* per IL4/IL5, cittadinanza + clearance SECRET per IL6.
  ⚠️ **La riga più importante è anche la meno documentata**: confermata da cinque fonti indipendenti ma
  **il PDF originale non è mai stato letto**. È il primo documento da aprire a mano.
- **CMMC** (DFARS 252.204-7021, efficace 10/11/2025) — estende i requisiti cloud all'intera filiera privata
  della difesa: sposta la barriera dal cliente pubblico ai fornitori.

**⚠️ DUE CORREZIONI CHE CAMBIANO LA SCENEGGIATURA:**
1. **La barriera FedRAMP NON è il costo: è la *sponsorship* di agenzia.** FedRAMP 20x sta abbassando costi
   e tempi **di proposito** (Fase 3 nel Q3-Q4 2026). **Se il documentario poggia sul costo, è smentito entro
   un anno.** Sponsorship, cittadinanza e controllo societario invece non si abbassano.
   *(Nota: la base legale FedRAMP, 44 U.S.C. §§3607-3616, ha una sunset al 23 dicembre 2027.)*
2. **Nel 2025-2026 gli USA NON hanno introdotto alcuna restrizione verso i fornitori europei.** Anzi: EO
   14275 e il *Revolutionary FAR Overhaul* vanno in direzione **deregolatoria**, e l'*America First
   Investment Policy* (21/02/2025) **favorisce** gli investitori alleati. Le novità restrittive riguardano
   la Cina. **Va detto in voce**: gli Stati Uniti non hanno chiuso agli europei perché non ne hanno
   bisogno — l'effetto è già prodotto dallo strato costruito fra il 2011 e il 2019.

⚠️ **Limiti**: `ecfr.gov` e `federalregister.gov` reindirizzano (302) e non sono stati leggibili;
`uscode.house.gov` irraggiungibile. Ripiego su Cornell LII e govinfo XML, con le righe interessate
degradate a MEDIA. 20 URL da aprire a mano elencati nel dossier 11.

### A19. 🎬 LE QUATTRO VOCI AL SENATO FRANCESE — sei anni, tre aziende, un solo «no»
La segnalazione «anche AWS e Google risposero» era **vera**, ma riferita a **un'altra commissione**.
Entrambe le cose stanno in piedi:

- **Commissione 2025** (rapporto n° 830): il dossier 02 aveva ragione. Tomo I integrale scaricato ed
  estratte le tre liste ufficiali: la `LISTE DES CONTRIBUTIONS ÉCRITES` contiene **solo Microsoft France**
  fra gli hyperscaler. AWS e Google non compaiono né lì né fra le persone audite.
- **Commissione 2019** — *commission d'enquête sur la souveraineté numérique*, rapporto n° 7 (2019-2020):
  **tutti e tre furono auditi sotto giuramento.**
  - **Google France** (Benoît Tabaka) — 17 luglio 2019
  - **Microsoft** (Marc Mossé, Mathieu Coulaud) — 18 luglio 2019
  - **AWS France** (Julien Groues, DG; Stéphan Hadinger, CTO) — **3 settembre 2019**, 16h15-16h50

La domanda del presidente Montaugé ad AWS era **più ampia** di quella del 2025, perché nominava le
controllate: «*Pouvez-vous nous assurer qu'Amazon, **ou ses filiales**, ne permet pas et ne permettra pas
aux autorités américaines de prendre connaissance des données de nos concitoyens…?*»

**Nessuno dei tre rispose sì o no.** AWS smontò «i miti» sul CLOUD Act e concluse «*nous appliquons la
loi*». Google affermò che «*ces dispositions ne sont pas entrées en vigueur, en l'absence de conclusion des
accords bilatéraux*». ⚠️ **CORREZIONE (v. A27)**: qui era stato scritto «giuridicamente scorretto» in modo
troppo netto. La verifica sul verbatim ampio mostra che **il dubbio resta**: non è falsa testimonianza.

> 🎯 **Il «No, je ne peux pas le garantir» di Carniaux (10 giugno 2025) è il primo «no» esplicito in sei
> anni.** Il dossier 12 contiene il verbatim integrale delle quattro voci con traduzione e un **blocco di
> montaggio a quattro voci**: è materiale da mandare in onda affiancato.

### A20. 🔥 Il CTO di AWS ha enunciato lui stesso, sotto giuramento, la dottrina che oggi lo smentisce
**3 settembre 2019**, Stéphan Hadinger, CTO di AWS France, davanti al Senato francese:
«*une société non américaine sera aussi soumise au Cloud Act si elle a […] **une filiale ou des employés
sur le territoire américain***» — citando il DOJ (Richard Downing) per cui «*la plupart des grands
fournisseurs de cloud américains ou non américains étaient soumis à la juridiction des États-Unis*».

È **il principio che rende non immune l'AWS European Sovereign Cloud**, enunciato da AWS stessa.

### A21. Nitro: cosa dice davvero l'audit — e cosa esclude
Rapporto **NCC Group** letto per intero. Quattro limiti dichiarati dall'auditor stesso:
1. È **pagato da AWS**;
2. è una ***design review* senza test**: l'auditor dichiara di non poter attestare che l'implementazione
   corrisponda al progetto;
3. mette **fuori perimetro** il piano di controllo EC2, l'hypervisor, il firmware e le Nitro Card;
4. 🎯 riga decisiva: fornisce «*no assurance with regards to any future chosen or **compelled** technical
   changes*» — l'auditor **esclude espressamente** la garanzia contro modifiche tecniche **imposte**.
   Che è esattamente lo scenario CLOUD Act.

Contrappeso indipendente, non pagato da AWS — **Trail of Bits**: «*you must completely trust AWS*».

### A22. Il test giuridico, risolto su fonte primaria DOJ
Scaricato il **white paper DOJ 2019** (dava 403 nel dossier 01, oggi risponde 200). La **FAQ n° 25** pone
letteralmente la nostra domanda e risponde: «*The analysis remains the same **regardless of corporate
structure** […] Whether a company exercises sufficient control over data held by a subsidiary is a
**fact-dependent inquiry***.»

**Verdetto sulla tesi Amazon: regge nella sostanza, ma va corretta in due punti.**
- ❌ Dire «è una controllata, **quindi** soggetta al CLOUD Act» è **troppo netto**: il DOJ dice
  *fact-dependent*, e **non è stata trovata né letta alcuna sentenza** che applichi il §2713 a una
  controllata estera con personalità giuridica distinta.
- ✅ La **difesa crittografica di AWS** (chiavi in *external key store*) è **tecnicamente valida per il
  dato a riposo** e va riconosciuta.
- ⚖️ **AWS non ha mai preteso di essere immune** dal CLOUD Act. L'equivoco è **commerciale**, e sta tutto
  nella parola «sovereign».

⚠️ **Lacune**: catena di controllo azionaria **non letta su visura** (handelsregister.de a pagamento);
**nessuna giurisprudenza letta**. 14 URL primari da aprire a mano nel dossier 12.

### A23. ⚡ UN VETTORE NUOVO: non l'accesso ai dati, ma la REVOCA del servizio e dell'identità
> 🗂️ **DECISIONE EDITORIALE (29/07/2026): A23-A26 NON entrano nel documentario.** Le prove reggono, ma il
> vettore è diverso dalla tesi del film (sanzioni su persone fisiche ≠ giurisdizione sui dati della PA) e
> per l'Italia il rischio è dichiarato **teorico**. Materiale conservato: vale per **un pezzo a sé** sul
> rapporto fra sanzioni e identità digitale. **Non citarlo nello script, nello storyboard o nel fumetto.**
Distinto dal CLOUD Act e da tenere separato in tutto il racconto. Qui non si tratta di **leggere** i dati,
ma di **spegnere** l'accesso di una persona ai propri strumenti digitali.

**Il fondamento è nel testo presidenziale.** EO 14203 §3, letto verbatim: vieta «*the provision of funds,
goods, or **services***» a un soggetto designato. La parola «servizi» è nell'ordine esecutivo: non serve
interpretazione.

**E le aziende lo hanno messo per iscritto.** Facebook, 28 dicembre 2017 (caso Kadyrov): «*Facebook has a
**legal obligation** to disable these accounts.*» Ammissione scritta dell'obbligo, con otto anni d'anticipo.
**Microsoft è già stata multata** (~3,3 M$, aprile 2023, OFAC+BIS) per aver fornito servizi a *blocked
persons*: non un'azienda che sceglie, ma **una recidiva sotto vigilanza**.

### A24. 🎯 I DUE CASI SOLIDI SONO CITTADINI EUROPEI — e non sono quelli che si citano di solito
🚨 **Il caso Karim Khan è il PIÙ FRAGILE del dossier, non il più forte.** La fonte è AP (Molly Quell,
15 maggio 2025): «*Microsoft, for example, cancelled Khan's email address… **ICC staffers said***» —
funzionari **anonimi**, nessun documento. Brad Smith ha smentito il 4 giugno 2025. **Ma la smentita nega
la cessazione dei servizi alla Corte come organizzazione, non la disconnessione dell'account individuale:
le due affermazioni possono essere entrambe vere.** Da maneggiare con estrema cautela.

**I due casi incontestabili:**

1. **Beti Hohler**, giudice slovena — marzo 2026, verbatim:
   > «*My Apple ID, iCloud, Amazon, Airbnb, PayPal, and other accounts have all been blocked or cancelled.
   > **These cancellations happened overnight without advance warning.***»
   **Nessuna azienda l'ha mai contestato.**
2. **Nicolas Guillou**, giudice francese — documentato in un **atto parlamentare francese** (interrogazione
   11576 Lachaud, 9 dicembre 2025) **con risposta ufficiale del Governo** del 10 febbraio 2026, in cui la
   Francia si dichiara «*favorable à l'activation du règlement de blocage*».
   **È la migliore fonte documentale dell'intero dossier.**

### A25. L'asimmetria fra denaro e dati — è il fatto analitico più forte
Per i **fondi** bloccati la legge americana prescrive conto fruttifero, interessi, *audit trail* e
restituzione in caso di delisting. Per i **dati**: **nulla**. Nessuna regola su conservazione,
esportabilità o restituzione. **L'assenza di disciplina è essa stessa il risultato.**

E il **Regolamento di blocco UE non è stato attivato** a 17 mesi dall'EO, nonostante due risoluzioni del
Parlamento europeo (9 luglio e 11 settembre 2025) e la richiesta di Spagna, Slovenia e Francia.

**Italia**: esistono designati reali (23 agosto 2024, EO 14024 — Fagima Fresatrici S.p.A., Idronaut S.r.l.
e quattro persone fisiche), ma **nessun effetto digitale documentato**. ⚠️ **Il rischio per un ente
pubblico italiano è dichiarato TEORICO**: va detto così.

### A26. ⚠️ SEI CORREZIONI — casi che circolano e che NON reggono
1. **Bensouda (2020) non perse servizi digitali**, solo bancari. **Il precedente digitale del 2020 non esiste.**
2. **A Moraes non è stato tolto Gmail**: la stampa brasiliana descriveva ipotesi. Ed è stato **delistato il
   12 dicembre 2025**.
3. **L'interruzione Microsoft in Russia (2024) ha base giuridica EUROPEA, non americana.** Usarla come prova
   del potere USA è **smentibile in dieci secondi**.
4. **Huawei è Entity List/BIS**, non OFAC/IEEPA: strumenti diversi, non cumulabili nel racconto.
5. **X/Starlink 2024 è il fenomeno OPPOSTO** — uno Stato che interdice un'azienda. Citarlo come conferma
   **dimostra la tesi della controparte**.
6. **L'impegno Microsoft del 30 aprile 2025** copre gli ordini di sospendere le «*cloud operations in
   Europe*» e **non menziona mai le sanzioni individuali**: copre lo scenario mai accaduto, non quello
   già accaduto tre volte.

🔴 **DA VERIFICARE A MANO, priorità 1**: nel **febbraio 2026 Microsoft si sarebbe scusata con la *Business
and Trade Committee* dei Comuni**, chiedendo la correzione del verbale dopo che un dirigente aveva
attribuito alla CPI — «*not Microsoft*» — la disattivazione della posta di Khan. Riportato in modo
concorde ma **la fonte non è stata aperta** (The Register blocca i bot): **serve il verbale parlamentare
originale**. La voce sulla presunta minaccia di Microsoft alla Corte è marcata DA VERIFICARE: **se la
fonte primaria olandese non si trova, quel punto va eliminato dal film.**
Bloccati anche `federalregister.gov` ed `ecfr.gov`: 31 CFR Part 528 e la **General License D-2** non letti
in originale — la clausola di esclusione dei *blocked persons* nella D-2 dirime il contro-argomento
«esistono licenze per i servizi essenziali». 25 URL da aprire a mano nel dossier 13.

### A27. Il caso Tabaka risolto: imprecisione con effetto fuorviante, **non** falsa testimonianza
Letti integralmente il resoconto ufficiale della commissione 2019 (189.384 caratteri) e il **rapporto n° 7
tomo I** (570.803 caratteri). Tre reperti:

1. **La domanda riguardava inequivocabilmente il §2713.** Il presidente Montaugé lo definisce lui stesso:
   «*le Cloud Act permet aux autorités américaines de disposer des données que vous stockez, **quel que soit
   le lieu de stockage***». Non nomina mai gli accordi bilaterali. Nomina invece **Airbus Defence and Space
   e Atos** come clienti a rischio.
2. **Il verbatim ampio consente due letture.** L'antecedente grammaticale di «*ces dispositions*» è la frase
   precedente sulla relazione bilaterale — quindi **l'ipotesi della definizione ristretta regge**, ed è la
   stessa che Google metterà per iscritto nel white paper 2022 (v. A28). **Ma una frase resta irriducibile**:
   «*quand bien même le Cloud Act entrerait en vigueur et obligerait Google à communiquer les données de ses
   clients*». **Il dubbio resta, e va dichiarato.**
3. **La smentita migliore è del Senato stesso, e non accusa nessuno.** «Tabaka» ricorre **0 volte** nel
   rapporto finale. Ma il riquadro didascalico sul CLOUD Act scrive: «*Il vise principalement à réaffirmer
   le droit […] la communication de toutes données stockées, même à l'étranger. **Il prévoit aussi, et
   indépendamment**, la conclusion d'accords bilatéraux*». **La parola «indépendamment» è del Senato francese.**

**PRIORITÀ 1**: ascoltare il **video ufficiale del 17/07/2019** — il *compte rendu* è rivisto, non stenografico.
**Bonus (nota 180 del rapporto)**: sei giorni prima, **OVH** rispose alla stessa domanda — ed è l'unica
risposta **strutturale** anziché procedurale. Il contrasto è materiale da montaggio.

### A28. Google smonta il mito della geografia — per iscritto, in un proprio documento
**Google Cloud Whitepaper, «Government Requests for Cloud Customer Data», febbraio 2022**, pag. 5, verbatim:
> «*the CLOUD Act clarifies that the U.S. government can compel production of data where the data is under
> the "possession, custody, or control" of a provider subject to US jurisdiction, **regardless of where that
> data is physically stored**. In other words, **data localization requirements do not impact whether a
> cloud provider may have to disclose data** in response to a government request.*»

E ammette la coercibilità: offre cifratura che tiene i dati illeggibili «*even if Google is compelled to
turn over the data*». **La difesa è tecnica, non giuridica.**
Pag. 6: definisce «CLOUD Act request» **in senso stretto** (solo accordi bilaterali con governi stranieri
qualificati), escludendo espressamente le «*U.S. request*» sui poteri preesistenti — cioè proprio il
meccanismo che conta. È la chiave di lettura di A27.
La procedura in quattro passi è tutta condizionata da «*unless prohibited by law*»: **stesso schema e stesso
limite della clausola italiana PR.DS-01** (A7).

### A29. Google, la FISA 702 e la scuola italiana
**Google ammette la FISA 702 in un documento destinato alle scuole** — white paper *Workspace for
Education*, agosto 2021: «*To the extent Google LLC may receive targeted requests […] under Downstream 702,
we **carefully review** each request*». **Non dice che rifiuterebbe.**

**Nessuna audizione di Google in un parlamento europeo dopo il 2019** (verificato sulle liste ufficiali 2025).

**S3NS**: qualificazione ANSSI del **17 dicembre 2025** — prima volta IaaS+PaaS+CaaS insieme (non «30
servizi»: correggere il dossier 08). S3NS oggi si dichiara «*fully owned by Thales*» mentre nel 2022 si
parlava di Google in minoranza: **forchetta 0%-24% da chiudere**. Non intacca la tesi, perché SecNumCloud
§19.6 fissa il tetto proprio al 24%.

> **LA TENSIONE, ed è l'argomento più forte del film a favore della regolazione.**
> Google ha **la posizione dichiarativa più debole** e **il rimedio strutturale più avanzato**.
> La spiegazione non è ipocrisia: **S3NS esiste perché la Francia ha scritto il §19.6.**
> Un fatto scomodo per noi diventa la prova che **la regola funziona**.

**Scuola** — esiti effettivi, tutti diversi: **Danimarca** ordine ai 53 comuni (non sanzione a Google) ·
**Paesi Bassi** adeguamento (**è il contro-argomento più forte di Google**) · **Germania** cautelare chiuso
da transazione (OVG NRW 19 B 417/22) · **Italia: nessun provvedimento, a fronte di 8.321 istituti.**
E **nemmeno Google pubblica dati di diffusione in Italia**: la misurazione dell'Osservatorio resta
**l'unica fonte esistente**.

### A30. AWS European Sovereign Cloud — la catena societaria, letta sul registro
Quattro società tedesche identificate con numero di registro, tribunale, sede, capitale e amministratori:
holding **AWS European Sovereign Cloud GmbH** (Potsdam HRB 40853) · **Amazon Data Services ESC GmbH**
(Potsdam HRB 40822) · **Amazon ESC Trust Services GmbH** (Potsdam HRB 40804) · **AWS ESC Development
Center GmbH** (München HRB 268806).

🔻 **DUE RETTIFICHE AL DOSSIER 12 — la seconda riguarda noi:**
1. «Amazon Germany Holdco 1 GmbH» **non è una controllante intermedia**: è il nome che la holding stessa
   portava fra il 21/10/2021 e il 23/07/2025 (e prima ancora *SCUR-Alpha 1391 GmbH*).
2. 🚨 **`handelsregister.de` NON è a pagamento.** È gratuito e senza registrazione dal 1° agosto 2022
   (riforma DiRUG). La *Gesellschafterliste* del 21/10/2025 è **pubblica e scaricabile**.
   **L'opacità era nostra, non di AWS.** Va aperta a mano (il portale respinge le richieste automatiche).

**Reperto nuovo**: nessuna delle entità è stata «costituita per questo scopo» come afferma il white paper —
sono **società di comodo (*Vorratsgesellschaften*) del 2020-21 rinominate**. È prassi legittima in Germania,
ma **la frase del white paper è imprecisa**.

🎯 **E una scelta lessicale che fa lavoro**: sul proprio sito AWS scrive che la ESC opera «*under a parent
company that is **locally controlled** in the European Union*» — **«controlled», mai «owned»**.
Controllo operativo, non proprietà. È la stessa distinzione su cui si regge tutto il capitolo.

### A31. 🎯 La giurisprudenza non esiste, ma la dottrina è netta — e viene da una fonte non allineata
Confermato: **nessuna sentenza** applica il §2713 a una controllata estera con personalità giuridica
distinta. Ma il saggio di **Hemmings, Srinivasan e Peter Swire**, *Journal of National Security Law &
Policy* 10:631 (2020), letto integralmente, conclude:

> «*a court would **almost certainly** find that a parent has control over a wholly-owned subsidiary for
> purposes of the CLOUD Act*»

E gli autori **dissentono dal Dipartimento di Giustizia nel verso più severo**. Con la giurisprudenza sul
*control test* nella discovery federale: Bank of Nova Scotia, Marc Rich, Uranium Antitrust, Gerling,
Zenith, Pitney Bowes.

⚖️ **Perché conta**: Swire è lo stesso autore della **contro-analisi che ci contraddice** sul Data Privacy
Framework (v. A12). Una fonte non allineata alla nostra tesi che conclude a nostro favore vale il doppio.

### A32. 🇮🇹 AWS in Italia — discrepanza chiusa, e un virgolettato pesante
Le tre cifre in conflitto erano **tre cose diverse**: **2 mld** = Region di Milano (annuncio 2022) ·
**1,2 mld** = piano 2024-2029 (29/11/2024) · **3,2 mld** = cumulato dal 2012.
Delibera del Consiglio dei ministri **ex art. 13 D.L. 104/2023**: commissario straordinario con poteri di
ordinanza e autorizzazione unica.

> **Il ministro Urso, in quell'occasione: «Oggi facciamo un ulteriore passo verso la sovranità digitale.»**

Nel catalogo ACN: schede **IA-5789 / PA-5790** (fornitore **PSN**, livello 2, 06/06/2025-06/06/2028);
**AWS qualificata QC2 su 228 prodotti**.

### A33. AWS pubblica meno degli altri
Report di trasparenza H2 2025 (pubblicato 30/01/2026, URL migrato di CDN ma non rimosso): **nessuna
menzione dell'European Sovereign Cloud**. Due pagine, **numeri in forma di immagine** — non leggibili
automaticamente — nessuna serie storica, e **nessuna cifra sulle opposizioni** benché AWS rivendichi
«*a long track record*» di contestazione degli ordini.
Confronto: Microsoft e Google pubblicano di più.

🔴 **NUOVO PUNTO APERTO — priorità alta**: AWS invoca fra le proprie difese l'**immunità sovrana** (FSIA),
argomento **pertinente proprio alla PA italiana** e **non ancora verificato**. Da chiudere.

### A34. 🇩🇪🇦🇹🇨🇭 Le migrazioni davvero concluse sono **militari** — e il resto è più fragile
23 casi censiti nell'area germanofona e Benelux. Il pattern che emerge non era atteso:

**Concluse (non annunciate):**
- **BwMessenger** (Bundeswehr, Matrix/Element) — **oltre 100.000 utenti dal 2020**, certificato BSI per
  materiale classificato *VS-NfD*. **È l'unica migrazione open source su larga scala conclusa dell'area.**
- **Bundesheer austriaco** — **16.000 postazioni LibreOffice**, con decisione motivata **esplicitamente
  dalla sovranità**, non dal risparmio.

🎯 **Reperto singolo più forte**: il **Comando Cyber dell'esercito svizzero** lascia Microsoft 365 per
**openDesk** (autunno 2026). Il comandante dichiara pubblicamente che M365 «**non è adatto**» alle esigenze
di riservatezza, e la stampa svizzera lo collega al CLOUD Act.
⚠️ **È annunciato, non fatto.**

### A35. I due fallimenti — documentati, e più istruttivi dei successi
- **Dataport Phoenix**: chiuso a ottobre 2024. **~140 mln € spesi, ~90 persi, 36,5 svalutati.** Fallimento
  **accertato dalla Corte dei conti di Amburgo**: «non pianificato in modo economico fin dall'inizio».
  Il codice però **è diventato openDesk**. La FSFE lo denunciava come *open-washing* già nel 2023.
- **LiMux Monaco**: 14.800 desktop, delibera 23/11/2017, **86-89 mln €** per tornare a Windows.
  🎯 **Il dato che ribalta la vulgata**: il **68,6% dei dipendenti era soddisfatto del *software***, solo il
  **32% dell'*organizzazione***. E la perizia Accenture chiedeva di **aggiungere** Windows, non di togliere
  Linux. **Nel maggio 2026 la nuova coalizione ha rimesso l'open source come regola.**
  > L'arco completo dimostra una cosa che serve al film: **la sovranità è reversibile in entrambe le direzioni.**

### A36. ⚖️ I due contro-fatti che il documentario NON può omettere
- La **Germania federale ha speso 481,4 mln € in licenze Microsoft nel 2025**, **+75,6% in due anni**
  (risposta a interrogazione parlamentare) — e **non ha cifre attendibili** per Länder e comuni.
- La **Confederazione svizzera ha COMPLETATO** il rollout di Microsoft 365 su **~54.000 postazioni** a
  dicembre 2025 — **mentre l'EMBAG è in vigore**.

👉 Chi migra e chi acquista sono **lo stesso Stato**. Ometterlo renderebbe il film propagandistico.

### A37. 🚨 SEI NUOVE TRAPPOLE dall'area germanofona
25. **Schleswig-Holstein NON è passata a Linux.** L'80% riguarda **LibreOffice**; il sistema operativo è
    ancora in fase pilota. **La stampa lo confonde sistematicamente** — e noi con lei, se non stiamo attenti.
26. **I numeri di Schleswig-Holstein non sono sinonimi**: 25.000 / 30.000 / 60.000 circolano come se lo
    fossero, ma **i 60.000 sono *dipendenti***, non postazioni migrate.
27. **L'art. 9 EMBAG svizzero obbliga a *pubblicare* il codice che l'amministrazione sviluppa, NON a usare
    open source.** Verbatim tedesco agli atti. Dire il contrario è l'errore più diffuso sul caso svizzero.
28. **Clarence e S3NS girano su Google Distributed Cloud Hosted**; Proximus vende anche Azure Local.
    Il comunicato del Governo lussemburghese **non nomina mai Google**.
29. **openDesk: 100.000 vs 80.000 postazioni** dalla stessa fonte nello stesso periodo — e il ministero che
    lo commissiona **lo testa su 80 postazioni**. Non citare cifre senza qualificarle.
30. **Il rischio simmetrico**: raccontare solo i successi. Vale quanto raccontare solo i fallimenti.

### A38. La gara UE da 180 milioni — e il livello che nessuno raggiunge
17 aprile 2026: **prima volta che la sovranità è un criterio misurato** in una gara della Commissione.
Esito: **tre aggiudicatari SEAL-3, uno SEAL-2, nessuno SEAL-4** — il livello con catena europea completa,
dai chip al software.

⚠️ **ATTENZIONE ALLA COLLISIONE DI SCALE**: la scala **SEAL 0-4** della gara UE (⚠️ **cinque** livelli, non quattro — SEAL-2 era la
soglia minima di ammissibilità) **non è** la nostra scala 0-4. Vanno tenute distinte e mai sovrapposte nel racconto: una misura i fornitori, l'altra i modelli.

### A39. 🚨 IL CASO DANIMARCA NON ESISTE NELLA FORMA IN CUI CIRCOLA
Verificato **in danese**. È il caso più citato d'Europa, e la stampa internazionale lo ha travisato.

- **24 giugno 2025**, cinque giorni dopo l'annuncio, *Version2*: «**Digitaliseringsministeriet maner til ro:
  Vil ikke droppe Microsoft**» — **il ministero smentisce i titoli internazionali**.
- Il pilota è di **38 dipendenti** su Collabora, con problemi documentati (interlinea, font mancanti,
  blocchi). Titolo danese del dicembre 2025: «*Sto diventando grigio*».
  ⚖️ **Prosegue comunque**: non è una marcia indietro, è **una migrazione faticosa**. Va detto così.
- 🔻 **Nelle stesse settimane** lo Stato danese ha firmato **il più grande rinnovo Microsoft della sua
  storia**: **4,2 mld DKK / 5 anni / ~100.000 dipendenti**, più **4,1 mld DKK** per 96 comuni.
  Contro **80 mln DKK** per il piano sovranità 2026-2029. **Rapporto ~100 a 1.**
  Motivazione ufficiale del contratto quinquennale: serve **più tempo per studiare le alternative**.
- **Copenaghen non ha deciso di abbandonare Microsoft**: ha deliberato **un'analisi**. Lo dice il catalogo
  ufficiale del Governo danese: «*il caso non tocca risultati ed esperienze concrete*».

🚨 **TRAPPOLA 31 — la più pericolosa del registro**: **non dire «la Danimarca ha abbandonato Microsoft».**
È falso, è verificabile in cinque minuti, ed è ciò che ci farebbe smontare più in fretta di ogni altra cosa,
perché è il caso che tutti credono di conoscere.

### A40. 🎯 Il vero caso danese è **Aarhus** — piccolo, concluso, e scritto da un governo
60 sistemi migrati **da Azure a Hetzner**, conclusa nella **primavera 2025**: da **842.000 a 233.000
DKK/anno**, **ripagata in 4 mesi**.
Fonte: **catalogo casi ufficiale del Governo danese** (PA Consulting, gennaio 2026), scaricato ed estratto.

🎯 **E la motivazione della migrazione, nel documento governativo, cita testualmente che il supporto Azure
può avvenire *dagli Stati Uniti*.**
> **È l'Atto 4 del nostro film, scritto da un governo europeo.** Vale più di qualunque nostra spiegazione.

### A41. 🔥 Bruxelles ha scritto i criteri che a Roma si dice non si possano scrivere
**Aprile 2026**: la Commissione europea aggiudica **180 mln € di cloud sovrano a nove aziende europee,
zero americane** — Post Telecom, OVHcloud, Clever Cloud, STACKIT, Scaleway, Proximus, S3NS, Clarence,
Mistral — valutandole su **otto criteri di sovranità**.
*(Conferma incrociata con A38, che sullo stesso bando rileva: tre aggiudicatari SEAL-3, uno SEAL-2,
**nessuno SEAL-4**. I due dossier si confermano a vicenda su aspetti diversi.)*

> **Da mettere accanto ad A2** (il PSN costruito su Oracle, Google, Azure e AWS) **e ad A7** (il regolamento
> ACN: zero occorrenze di «CLOUD Act», «nazionalità», «capitale»).
> **La Commissione ha applicato a sé stessa i criteri che in Italia si dice non si possano scrivere** —
> e senza violare il diritto degli appalti, perché ha misurato la sovranità, non escluso una nazionalità.
> **È la risposta definitiva al contro-argomento di A11.**

### A42. I fallimenti dell'area — e il numero che ridimensiona tutto
- **Norvegia**: proposta di uscita da M365 **respinta**, **nessuno dei 21 emendamenti** approvato, e la
  ministra ridefinisce l'obiettivo come «**amministrare la dipendenza**».
- **Bulgaria**: obbligo di legge sull'open source **dal 2016** che dopo dieci anni non ha intaccato suite
  d'ufficio e cloud.
- **EDPS/Commissione**: la violazione più grave mai accertata si è chiusa **senza cambio di fornitore**.
- **Estonia** — il paese-simbolo del governo digitale — sta portando **15.000 postazioni *dentro* il cloud
  Microsoft**.
- **Polonia**: la «chmura krajowa» (cloud nazionale) è costruita **su Google e Microsoft**.

🔻 **IL NUMERO CHE RIDIMENSIONA TUTTO**: su **24 casi censiti nell'area, solo CINQUE sono migrazioni
concluse e verificate su fonte primaria.** Va detto in voce: è l'antidoto al trionfalismo, e ci protegge.

### A43. Tre casi nuovi, non ancora nel progetto
- 🇮🇪 **Irlanda**: gara Microsoft da **1 miliardo € annullata** nel luglio 2026 dopo contestazione in Dáil.
  **Nel Paese meno sospettabile d'Europa** — è la sede europea delle big tech.
- 🇮🇸 **Islanda**: nove risposte parlamentari che dichiarano la dipendenza **ministero per ministero**, con
  **Ísland.is** (il loro equivalente di SPID/IO) **su AWS**.
  👉 **È il modello procedurale che l'Italia non ha usato**: un parlamento che misura e pubblica.
- 🇷🇴 **Romania**: cloud di Stato PNRR operato dal servizio telecomunicazioni — con la critica di ApTI sul
  ruolo dell'intelligence, riportata per onestà.

### A44. 🎯 L'APPALTO CENTRALIZZATO EUROPEO ESISTE — ed è più avanti di un annuncio
Non è un annuncio politico: è il **Capo IV (artt. 37-40) della proposta CADA** (2026/0138 COD), testo
letto in originale (ST 10104/26, 130 pp.). Stato: **proposta legislativa formale**, con governance,
finanziamento e deroghe già scritti.

**Art. 37(3), verbatim**: la Commissione «*may act as a **central purchasing body** for contracting
authorities of Member States*» — contratti quadro, sistemi dinamici di acquisto, perfino rivendita
all'ingrosso.

🔻 **COSA MANCA PERCHÉ DIVENTI OPERATIVO** — è questo il finale del film:
1. approvazione del regolamento;
2. **un accordo fra Commissione e almeno DUE Stati membri (art. 38(1)) — che nessuno ha firmato**;
3. insediamento dello Steering Committee;
4. atti di esecuzione sui rimborsi;
5. **la piattaforma comune, che non esiste**;
6. il denaro.

📅 **Data dalla penna della Commissione**: «*The starting date of collection of the fee would be **2029**,
to allow for an initial setup process*». Apparato stimato ~**6 mln €/anno**.

⚠️ **Tre cose da non confondere**: la **gara da 180 mln** (conclusa, ma **solo per le istituzioni UE**);
il **Cloud Sovereignty Framework** (la metodologia — **l'unica cosa usabile domani mattina**); e il
**Capo IV** (lo strumento per gli Stati membri, non ancora esistente).

### A45. 🔥 La sequenza in due passi non va proposta: **è già scritta nell'Allegato II del CADA**
- **Livello 3**, criterio (i) ii, verbatim: «*where software components or products are **provided, owned,
  and licensed by a legal entity established in a third country***» — ammesso, con **audit del codice
  sorgente** e **piano di migrazione documentato**.
  👉 **È il modello Bleu/S3NS trasformato in criterio normativo**: software americano, operatore europeo.
- **Livello 4** toglie la deroga: «*a third country … **does not hold or exercise effective control** over
  the design, development, maintenance, and evolution*».

> **Il passo 1 e il passo 2 esistono, con i numeri di paragrafo.** Non dobbiamo proporre una strada:
> dobbiamo dire che **è stata scritta e non è ancora stata percorsa**.

🎯 **E il reperto che chiude l'atto**: **nel testo non c'è una sola data di calendario.** Sono segnaposto
tipografici mai compilati — `[date of entry into force plus 1 year]`.
**La regola è scritta. La data è bianca.** È esattamente lì che serve la spinta politica.

### A46. L'alibi italiano cade: un comune può aderire anche se l'Italia non aderisce
**Artt. 38(7) e 39(1)**: un ente locale può aderire alla centrale di committenza europea **anche se il
proprio Stato non vi partecipa** — ed è **per ciò stesso adempiente** al diritto UE degli appalti.

> Toglie insieme **l'alibi giuridico** («non possiamo, il codice appalti») **e quello politico**
> («decide Roma»). È la chiamata all'azione più concreta che il film possa fare.

**Unica scadenza vincolante con data certa in tutto il quadro**: **Data Act art. 29 — 12 gennaio 2027**,
divieto dei costi di uscita. È l'unica data che il finale può pronunciare.

### A47. 🎯 AIRBUS CHIUDE IL CERCHIO — ha chiesto la regola, poi l'ha applicata a sé stessa
**AFFIDABILITÀ: 🟢 ALTA** *(promosso da 🟡 il 02/08/2026: letto il comunicato ufficiale e la pagina
istituzionale Airbus. Il virgolettato Jestin, prima «da verificare», è ora **confermato alla lettera**.)*

**Primo tempo — Airbus chiede il criterio.** Il sito **eucshighplus.eu**, che raccoglie le adesioni alla
richiesta di reintrodurre i criteri **High+** nell'EUCS, è **gestito dall'ufficio di Bruxelles di Airbus**.
La lettera aperta dell'industria (**10 giugno 2024**, PDF originale già letto e citato sul sito) chiede una norma UE che protegga i dati più sensibili
«*against access or operational disruption resulting from non-EU extraterritorial laws*».
✅ **VERIFICATO DIRETTAMENTE IL 02/08/2026** leggendo il DOM del sito dal browser. *(Il precedente HTTP 503
non era un guasto: era un **blocco verso il fetcher automatico**. Da browser il sito risponde. ⚠️ Lezione
di metodo: un 503 su una fonte che ci serve va **riprovato da browser** prima di dichiararla irraggiungibile.)*

📌 **Il disclaimer, verbatim** — la gestione Airbus non è una ricostruzione, è scritta sul sito:
> «*European cloud users who agree with this position and want to support the open letter are asked to
> contact the **Airbus Brussels office, Avenue Marnix 28 1000 Brussels**, at Airbus-Brussels-Office@airbus.com,
> **which is responsible for this website***.»

📌 **Conteggio: 62 firmatari esatti**, contati uno per uno sull'elenco pubblicato. **Il nostro «chi lo
chiede: 62 organizzazioni» è confermato.**

🇮🇹 **I FIRMATARI ITALIANI** (richiesta esplicita del committente):
**Leonardo · Fincantieri · Generali · Telecom Italia (TIM) · Aruba** — e, da verificare la nazionalità,
**SPAC**.
🚨 **ARUBA È IL NOME CHE MANCAVA, ed è il più pesante di tutti**: è il principale fornitore cloud
italiano **e partner del PSN** (A2). Chiede a Bruxelles il criterio di immunità dalle leggi extraterritoriali
**mentre il PSN che contribuisce a costruire poggia su Oracle, Google, Azure e AWS**.
⚠️ Da rileggere A2 prima di usarlo, per attribuire ad Aruba **il ruolo esatto** nel PSN e non uno più grande
del vero. Ma la tensione è reale e va raccontata **senza accusare Aruba di incoerenza**: è semmai la prova
che *anche chi costruisce il PSN* considera insufficiente il quadro normativo in cui lo costruisce.

📌 **Che cosa chiede la lettera, verbatim**: un criterio UE che dia agli utenti «*transparency, choice,
and the necessary protection for their most sensitive data **against access or operational disruption
resulting from non-EU extraterritorial laws***».
✅ **E chiede il contrario dell'esclusione**: «*A voluntary High+ EUCS would **in no way exclude
non-European providers**, but simply offer an alternative*». È **volontario e centrato sull'utente**.
👉 Disinnesca in anticipo l'accusa di protezionismo — **la nostra risposta al contro-argomento di A11,
scritta da chi chiede la norma**, non da noi.

📌 **Due appigli in più dalla lettera**: si fonda sul **rapporto Draghi** (che raccomanda una politica
unica UE per l'acquisto di cloud da parte delle PA, con requisiti di residenza dei dati e controllo sovrano
su sicurezza e cifratura) e dichiara il sostegno di **45.000 PMI europee del digitale**.

**Secondo tempo — Airbus applica il criterio a sé stessa.** Gara di **sei mesi**, **~50 fornitori
consultati**, vinta da **Scaleway** (gruppo Iliad). Annuncio **16 luglio 2026**.
📌 **Il criterio, verbatim dal comunicato**: Airbus ha valutato i fornitori su tre dimensioni, fra cui
«*European jurisdiction, data protection and **protection against non-European extraterritorial
legislation***».
📌 **Catherine Jestin, Executive Vice President Digital, Airbus** — verbatim:
> «*This collaboration marks a significant milestone in our broader commitment to European digital
> sovereignty. By integrating a trusted, high-performance cloud environment that **keeps our critical data
> assets shielded from foreign extraterritorial laws**, we are ensuring that our digital infrastructure
> keeps pace with our aerospace innovation, while maintaining control and resilience of our industrial
> operations.*»

**Perimetro**: **~70 applicazioni critiche entro il 2028** (progettazione aeronautica, ingegneria,
produzione, operazioni interne), con un potenziale fino a **~900 in cinque-sei anni**.

🔗 Scaleway, comunicato ufficiale 16.07.2026 — https://www.scaleway.com/en/news/scaleway-secures-european-trusted-cloud-services-contract-with-airbus/
🔗 The Next Web, 17.07.2026 — https://thenextweb.com/news/airbus-scaleway-aws-sovereign-cloud
🔗 L'Usine Digitale / developpez.com, 16-17.07.2026 (conferma incrociata su gara, 2028 e cifre)

> **👉 Chi ha chiesto la regola l'ha poi usata come committente.** Non è un'opinione sulla sovranità:
> è un'azienda che mette a bando il proprio criterio e ci scrive sopra un contratto. È **il cerchio
> narrativo del film** — e l'unico caso in cui la tesi è provata da chi l'ha applicata a sé.

⚠️ **CONTRO-ARGOMENTO, da dire noi per primi**: Airbus è **un'azienda privata**, non uno Stato. Nessun
obbligo di legge, nessuna gara pubblica, nessun precedente giuridico. E ha **un interesse industriale
evidente** a promuovere fornitori europei. Va detto — e poi va detto che *proprio per questo* il caso pesa:
un'impresa che risponde ai propri azionisti ha ritenuto il rischio abbastanza concreto da spenderci sopra.

🚨 **TRAPPOLA 34 — non dire «Airbus ha abbandonato AWS».**
- Il **comunicato ufficiale non nomina mai AWS**: la sostituzione è ricostruzione di stampa.
- **Jestin dice l'opposto della versione forte**: «*We do not intend to move away from all non-European
  solutions; balance choices based on data criticality*». È una **scelta per criticità del dato**, non un'uscita.
- **Non dire «900 applicazioni»**: sono ~**70 entro il 2028**; 900 è il potenziale a cinque-sei anni.
✅ Formulazione sicura: «*Airbus ha messo a gara le proprie applicazioni critiche e le ha affidate a un
fornitore europeo, mettendo a punteggio la protezione dalle leggi extraterritoriali.*»

### A49. 🔥 AIRBUS SCRIVE LA NOSTRA TESI SUL PROPRIO SITO ISTITUZIONALE
**AFFIDABILITÀ: 🟢 ALTA** — fonte primaria, pagina corporate Airbus, **17 giugno 2026**.
🔗 https://www.airbus.com/en/newsroom/stories/2026-06-building-resilience-how-airbus-supports-european-digital-sovereignty-and-innovation

Airbus elenca in proprio i due rischi che il film racconta, **con queste parole**:
> - «*Ensuring operational continuity: making sure business can continue **without any external
>   interruptions***»
> - «*Controlling data access: **Protecting data from extraterritorial laws**, which are passed by a country
>   and apply to people, businesses, or actions happening outside of its own borders*»

👉 **Non è un attivista, un accademico o un giornalista: è il maggiore gruppo industriale europeo** che
definisce le leggi extraterritoriali come un rischio da cui proteggersi — e lo scrive sul proprio sito.
**Vale più di qualunque nostra spiegazione**, esattamente come A40 (il documento del Governo danese).

📌 Contesto utile: Airbus è **socio fondatore** della *European Sovereign Tech Industry Alliance*
(18.11.2025) e cofondatore di *European Tech Creators* (maggio 2026, con ASML, Ericsson, Mistral, Nokia,
SAP, Siemens); in Gaia-X dal 2021.

⚠️ **La riga che ci tiene onesti, dalla stessa pagina**: Airbus «*remains committed to using the best
solutions available on the market, **even if they come from outside the bloc***». **Va citata.** È la prova
che la posizione non è ideologica — ed è ciò che rende non ideologica anche la nostra.

### A48. Il confronto economico difendibile — spesa annua contro spesa annua
✅ **Da usare**: **151 mln €/anno** di lobbying tech a Bruxelles contro **~30 mln €/anno** della gara per il
cloud sovrano (180 mln «*over a period of 6 years*» — l'annualizzazione è **della fonte**, non nostra).
Rincalzo: bilancio **ENISA 25,2 mln €** (2023, fonte primaria).
❌ **Scartati**: capitalizzazione contro PIL (**stock contro flusso**) e fatturato contro PIL (**lordo contro
valore aggiunto**). Sconsigliate anche cifre puntuali sul capex degli hyperscaler: **le stime consultate
sono incoerenti fra loro**.

### A50. 🎯 IL PSN DESCRIVE DA SÉ LA PROPRIA ARCHITETTURA — e la parola «sovranità» non significa immunità
**AFFIDABILITÀ: 🟢 ALTA** — fonte primaria, pagina ufficiale PSN letta integralmente dal browser il
02/08/2026. 🔗 https://www.polostrategiconazionale.it/soluzioni/servizi-con-cloud-service-provider/

🚨 **CORREZIONE A UNA NOSTRA ASSUNZIONE.** Avevamo impostato la critica su «i servizi sono operati da
Microsoft, Google e Amazon». **La pagina non dice questo**, e affermarlo ci farebbe smontare con un
copia-incolla dal loro stesso sito. Dice tre cose diverse per **tre livelli diversi**.

**Cappello della pagina, verbatim**: la PA «potrà accedere in piena sicurezza, **autonomia e sovranità**»
ai servizi, «attualmente realizzati in partnership con **Oracle, Google, Microsoft Azure, AWS e Oracle**».

#### I tre livelli, con le parole loro
**1. Public Cloud PSN Managed** *(Oracle e Google)* — è il livello **più forte**, e va riconosciuto:
> «erogati da Cloud Service Provider (Oracle e Google) su Data Center del PSN o region italiane e
> **sono gestiti da personale del Polo Strategico Nazionale** con separazione logico-fisica dalla parte
> pubblica del CSP» · «gestione completa (dall'hardware alla piattaforma software) erogata da personale
> PSN» · «**Il controllo della Root Key** della region» · «erogazione dei servizi in modalità
> **completamente disconnessa dalle region pubbliche** del Cloud Service Provider»
⚠️ **Strutturalmente somiglia al modello 21Vianet/Bleu**: il fornitore dà la tecnologia, il personale
locale gestisce. **Non è «operato da Google».** Dirlo sarebbe falso.

**2. Hybrid Cloud on PSN site** *(Microsoft Azure)* — 🔥 **è qui il reperto**:
> «erogati da Cloud Service Provider (Microsoft Azure) tramite DC e infrastruttura proprietaria di Polo
> Strategico Nazionale» · «L'erogazione di servizi **IaaS & PaaS** equivalenti a quelli su Microsoft Azure
> Public Cloud» · 🎯 «**Un control plane unico con Microsoft Azure Arc**»

> 🔥 **IL PIANO DI CONTROLLO È DICHIARATO MICROSOFT, DAL PSN STESSO.**
> Il piano di controllo è esattamente il vettore che l'**Atto 4** del film descrive. Non dobbiamo
> dimostrarlo né dedurlo: **è scritto nella loro pagina commerciale, come una funzionalità.**

**3. Secure Public Cloud** *(Microsoft Azure, Google Cloud, AWS)*:
> «erogati da un Cloud Service Provider **pubblico**… localizzato in region italiana e securizzato
> utilizzando chiavi di crittografia gestite… dai sistemi del PSN» · «gestione delle chiavi di crittografia
> **esterna al perimetro di controllo del CSP**» · «**Sovereignty** sui dati memorizzati tramite gestione
> dei backup anche nel private cloud del PSN»
⚠️ **E la riserva se la scrivono da soli**: «Il confidential computing, **ove attivato**, rende impossibile
agli operatori del cloud service provider di accedere anche al dato durante l'elaborazione».
**«Ove attivato»**: la protezione più forte è **opzionale**, e la pagina non dice dove sia accesa.
👉 È esattamente la prima delle tre domande già previste al PSN nel diritto di replica.

#### 🎯 LA CRITICA, NELLA FORMA CHE REGGE IL CONTRADDITTORIO
Su questa pagina la parola «sovranità» indica **la posizione dei backup e la gestione delle chiavi**.
**Non indica l'immunità da una giurisdizione straniera.** Sono due cose diverse, e la seconda non è mai
nominata: nella pagina compaiono **zero occorrenze** di *nazionalità*, *controllo societario*, *CLOUD Act*,
*legge extraterritoriale*, *giurisdizione* — coerentemente con la scansione del regolamento ACN (**A7**).

> **La formulazione da usare:**
> Il PSN ha costruito una **separazione operativa** — personale proprio, chiavi proprie, region
> disconnesse. È più di quanto molti credano, e va riconosciuto.
> Ma **la separazione operativa non è immunità giurisdizionale**. La Francia ha scritto requisiti su
> **sede, capitale e controllo societario**; la Cina ha preteso **un operatore diverso dal fornitore**.
> L'Italia ha chiesto **una buona gestione** — e l'ha chiamata sovranità.

🚨 **TRAPPOLA 35 — non dire «i servizi del PSN sono operati da Microsoft, Google e Amazon».**
È falso per il livello *PSN Managed*, dove la pagina dichiara gestione da personale PSN e controllo della
Root Key. La formulazione corretta distingue i **tre livelli** e attacca **la parola**, non l'architettura.
✅ Ciò che si può dire, e che basta: **il piano di controllo del livello ibrido è Azure Arc**, il
confidential computing è **«ove attivato»**, e **nessun documento italiano pone requisiti di controllo
societario**.

⚠️ **RESTA DA VERIFICARE, e non è poco**: quale dei tre livelli sia effettivamente il più diffuso fra gli
enti aderenti. Se la quota maggiore fosse sui livelli 2 e 3, la critica si rafforza molto; se fosse sul
livello 1, va ridimensionata. **Senza questo dato non si può quantificare nulla in voce.**

### A51. 🔥 NEL MANUALE UFFICIALE DEL PSN, «SOVRANITÀ DEL DATO» È DEFINITA COME UNA COPIA DI BACKUP MENSILE
**AFFIDABILITÀ: 🟢 ALTA** — quattro documenti ufficiali PSN scaricati e letti integralmente il
02/08/2026 (testo estratto con pypdf, non riassunti di terzi).
🔗 `PSN-Concessione-Convenzione.pdf` (53 pp.) · `PSN_Guida-alla-Convenzione_.pdf` (11 pp.) ·
`PSN-Concessione-Caratteristiche-tecniche-dei-Servizi.pdf` (33 pp.) ·
`PSN-Manuale-Utente-SPC-Azure.pdf` (64 pp., ed. 04/04/2025)

#### 🎯 IL REPERTO CENTRALE — la definizione operativa, verbatim dal manuale
> «Il primo requisito è legato alla **sovranità del dato**: nel perimetro fisico del PSN deve essere
> disponibile e fruibile **una copia dei workload** erogati presenti sul Cloud Service Provider.
> Per soddisfare il requisito della sovranità del dato, la replica del dato su storage del PSN ha
> **frequenza mensile** e ne viene mantenuta **solo una versione**.»

E per la copia secondaria:
> «backup **ogni sei mesi** con retention di un anno, ovvero sempre 2 versioni per mantenere la richiesta
> di **sovranità del dato**.»

> 🔥 **Nel documento ufficiale del PSN, «sovranità del dato» non è una condizione giuridica:
> è una copia di backup replicata una volta al mese.**
> Non è una nostra interpretazione né una deduzione. È **la definizione operativa scritta nel manuale**,
> nel paragrafo che spiega come quel requisito viene soddisfatto.

#### ✅ CIÒ CHE VA RICONOSCIUTO — e va detto prima
Il **BYOK è reale e serio**, e negarlo ci farebbe perdere il contraddittorio (vale **A22**):
> «La gestione delle chiavi prevede l'utilizzo della modalità **Bring your own key (BYOK)**. Le chiavi di
> cifratura vengono create e gestite dall'infrastruttura **Thales** presente on-premises nei datacenter
> del PSN, **escludendo così, dalla gestione delle chiavi di cifratura, il CSP**.»

⚠️ **Ma il limite è scritto nelle righe accanto**, ed è tecnico, non polemico: l'**uso** delle chiavi passa
per risorse del fornitore — «attraverso un'**Azure Managed Identity** appositamente creata» e «gestite
attraverso la risorsa **Azure Disk Encryption Set**». Le chiavi sono **custodite** fuori dal CSP; per
cifrare e decifrare un disco in esecuzione devono però essere **rese utilizzabili alla piattaforma**.
👉 È il limite noto del BYOK rispetto al *confidential computing*, che protegge il dato **durante
l'elaborazione**. E qui viene il punto successivo.

#### 🚨 LA DISCREPANZA FRA IL MARKETING E IL MANUALE
La pagina commerciale (**A50**) promuove: «Il **confidential computing**, ove attivato, rende impossibile
agli operatori del cloud service provider di accedere anche al dato durante l'elaborazione».
**Nelle 64 pagine del manuale operativo del Secure Public Cloud Azure, «confidential computing» compare
ZERO volte.**
⚠️ **Da dire con precisione**: non stiamo affermando che non sia disponibile. Stiamo dicendo che
**il manuale utente del servizio non lo documenta**, e che il sito lo qualifica da sé con «ove attivato».
È esattamente la prima delle tre domande da porre al PSN nel diritto di replica.

#### 📉 LA SCANSIONE A ZERO OCCORRENZE — 161 pagine di documenti contrattuali e operativi
Cercati in tutti e quattro i documenti: **CLOUD Act · extraterritoriale · nazionalità · capogruppo ·
paese terzo · controllo societario · FISA · SecNumCloud · immunità · legge straniera · diritto straniero ·
autorità straniera · extra-UE**. → **ZERO occorrenze, in tutti e quattro.**

⚖️ **E le due parole che ricorrono vanno disinnescate da noi, perché non aiutano la tesi:**
- **«giurisdizione»** compare 2 volte nella Convenzione, ma riguarda **il contenzioso** sul concessionario
  («le controversie, i procedimenti giurisdizionali… nei confronti del Concessionario e dei soci»).
  **Non ha nulla a che vedere con la giurisdizione sui dati.** Citarla sarebbe scorretto.
- **«sede legale»** (5) e **«capitale sociale»** (2) riguardano **le parti del contratto**, non i fornitori.

#### 🎯 E QUI STA LA COSA PIÙ ELOQUENTE DI TUTTE
La Convenzione **sa scrivere clausole di controllo societario. Le ha scritte** — ma **solo sul
concessionario italiano**:
> «La Società di Progetto è sottoposta alla normativa dello Stato italiano in materia di **golden power**.»
> «Di tutte le **variazioni nel capitale sociale del Concessionario**… si impegna ad informare
> tempestivamente il Concedente… al **consenso del Concedente**.»

> **Lo Stato italiano ha preteso il golden power e il consenso su ogni variazione di capitale —
> della società italiana che gestisce i data center.
> E non ha scritto una sola riga sul controllo societario di chi fornisce la tecnologia che ci gira dentro.**
> Non è che non sapessero come si scrive quella clausola: **l'hanno scritta, e l'hanno puntata altrove.**
> È **esattamente il vuoto che SecNumCloud §19.6 riempie** (A7).

#### 📋 Il control plane, ora confermato su fonte contrattuale (non più solo marketing)
La **Guida alla Convenzione** (agosto 2025), su *Hybrid Cloud on PSN site*, verbatim:
> «Registrate nelle subscription delle Amministrazioni Utenti, che diventeranno «deployment target»
> utilizzabili attraverso il **control plane di Azure** (e.g., Portale, Powershell, CLI, RestAPI…)
> per mezzo del **Servizio Azure Arc**»
> «Caratterizzate da un **Management Plane** formato da… **una componente che sfrutta i Servizi cloud
> Azure** per le funzionalità di monitoraggio, gestione aggiornamenti, raccolta eventi di sicurezza e
> controllo security posture.»
👉 A50 lo rilevava sulla pagina commerciale. **Ora è in un documento della Convenzione.**

E sul livello più forte, *Public Cloud PSN Managed*, la Guida conferma la separazione **operativa**:
> «permette di implementare una logica di **separazione logica e fisica**, sia nella **gestione operativa**
> che nel **rilascio e controllo del software di base**»
✅ Va riconosciuto. ⚠️ **Ma è separazione operativa, non giurisdizionale**: in nessun punto si dice chi
controlla societariamente il fornitore, né quale legge si applica.

#### ⚠️ UNA DISCREPANZA MINORE, DA VERIFICARE PRIMA DI CITARE I FORNITORI
Il **sito** indica il *Secure Public Cloud* su «Microsoft Azure, Google Cloud **e AWS**»; la **Guida alla
Convenzione** scrive «Region pubbliche degli Hyperscaler (i.e., **Microsoft Azure e Google Cloud GCP**)»,
**senza AWS**. Non nominare AWS in quel contesto finché non è chiarito.

#### 🔴 CHE COSA MANCA ANCORA — e senza cui non si quantifica nulla in voce
**Quale dei tre livelli sia effettivamente il più adottato dagli enti.** Nessuno dei quattro documenti lo
dice. Finché non lo sappiamo, il film può **descrivere l'architettura** ma **non può dire «la PA italiana
sta prevalentemente su X»**.

### A52. 🔥 L'ANSSI SMONTA IL CONFIDENTIAL COMPUTING **E** IL BYOK — ed è l'agenzia che ha scritto il §19.6
**AFFIDABILITÀ: 🟢 ALTA** — PDF integrale (13 pp., v1.0, 17.10.2025) scaricato e letto per intero,
non la pagina di presentazione. 🔗 https://cyber.gouv.fr/sites/default/files/document/anssi-technical-position-paper-coco-v1.0.pdf

#### 🎯 Le quattro frasi che valgono l'intero approfondimento, verbatim
1. «*Confidential Computing is **not secure enough to protect data integrity and confidentiality against a
   hostile administrator performing targeted, active attacks***.»
2. «*The current analysis shows that Confidential Computing is **not sufficient on its own** … **to meet the
   requirements described in section 19.6 of the SecNumCloud 3.2 framework***.»
3. **Raccomandazione agli utenti**: «***Not rely on Confidential Computing if the cloud provider is
   considered untrusted or potentially hostile**: against an active attacker, there are **too many known
   vulnerabilities to effectively guard against**. In such situations, **switching to a trusted CSP or using
   dedicated bare-metal hardware in a controled physical environment is a prerequisite***.»
4. 🔥 **SUL BYOK** — è il reperto che chiude anche il secondo approfondimento:
   «*Note that **“Bring Your Own Key” (BYOK) approaches do not solve this issue, as the CSP still needs to
   be trusted to use the keys provided by the user***.»

> **La catena logica è chiusa e non richiede una nostra deduzione tecnica:**
> il **§19.6** è la clausola di immunità dalle leggi extraterritoriali — **l'ha scritta l'ANSSI** —
> e **l'ANSSI dichiara che il confidential computing non la soddisfa**.
> Ogni argomento che offra il confidential computing **in sostituzione** dei requisiti giurisdizionali
> è già smentito dall'autorità che quei requisiti li ha inventati.

#### ✅ Ciò che l'ANSSI riconosce alla tecnologia (da dire per primi, o perdiamo il contraddittorio)
«*complements effectively at-rest and in-transit encryption by encrypting data in-use*» · «*still provides
significant defence-in-depth*» · «*may raise the complexity of attacks from the host or other tenants*».
**Non è una cattiva tecnologia. È una buona tecnologia usata per rispondere alla domanda sbagliata.**

#### 🔧 Il modello di minaccia, con le parole dell'ANSSI
- **«malicious admin»**: «*an administrator of the host … They can control the creation and execution of
  workloads, including modifying them before they are started, and **reading or writing their memory at
  runtime***» → **è l'acquisizione dinamica della RAM**, confermata dall'agenzia.
- Fra gli attori contro cui il modello non regge: «*attackers with a **very high power to coerce
  suppliers***» → **è l'attore statuale, descritto per funzione.**
- «*physical attacks are **explicitly out-of-scope** of the security model*» — e l'ANSSI lo scrive
  **subito dopo** aver osservato che la tecnologia «*is often presented by commercial providers as …
  resistant to a physical attack*». **Corregge il marketing di persona.**

🚨 **TRAPPOLA 39 — non attribuire all'ANSSI parole che non ha usato.**
Nelle 13 pagine, **ZERO occorrenze** di *sovereign*, *state actor*, *extraterritorial*, *jurisdiction*,
*legal*, *law enforcement*, *compel*. **Verificato.** L'ANSSI **non** dice «il confidential computing non
protegge dagli attori statuali»: dice che non protegge da un **amministratore ostile attivo**, che non
soddisfa il **§19.6**, e che contro un fornitore potenzialmente ostile **non va usato**.
✅ **La conclusione politica è nostra; le premesse tecniche sono interamente dell'ANSSI.** Va detto così,
ed è più forte: significa che non stiamo forzando una fonte per farle dire ciò che ci serve.

🚨 **TRAPPOLA 40 — sul BSI non abbiamo nulla, e non va citato.**
Cercata una presa di posizione del **BSI** tedesco sull'insufficienza del confidential computing:
**non l'abbiamo trovata**. ⚠️ Attenzione alla distinzione (regola 10): *non l'abbiamo trovata*, **non**
*non esiste*. Il BSI ha pubblicato il **C3A** (27.04.2026, criteri di autonomia cloud) e il concetto di
**«Cyber Dominance»**, ma **non risulta una sua posizione specifica sul confidential computing**.
❌ **Su decisione del committente il BSI è stato rimosso dalla pagina**: se il BSI fosse più permissivo,
citarlo indebolirebbe l'argomento invece di rafforzarlo. **Si cita solo l'ANSSI, che è più stringente.**

#### 📄 Prodotto: pagina pubblica bilingue `/misure-tecniche/`
Analisi estesa in italiano e inglese: i tre stati del dato, che cos'è il confidential computing e che cosa
ottiene davvero, i quattro limiti, l'attestazione rotta (**CVE-2026-33697**, TU Dresden, AsiaCCS ed
ESORICS 2026), la gestione delle chiavi, il caso PSN e la conclusione. In menu in entrambe le lingue.

### A53. 🎯 IL DIVARIO CON LA FRANCIA NON È TECNOLOGICO: è una frase che non è stata scritta
**AFFIDABILITÀ: 🟢 ALTA** — sintesi dei reperti A7, A29, A50, A51, A52, tutti su fonte primaria.
Prodotta la tabella di confronto pubblica su **/misure-tecniche/**, sezione 7.1: otto requisiti per i tre
livelli PSN contro SecNumCloud §19.6.

🚨 **LA FORMULAZIONE DA NON USARE — diventa la trappola 41.**
❌ «I cloud francesi sono sovrani, quelli italiani no.» **Falso e smontabile con due nomi**: la Francia ha
**Bleu** (tecnologia Microsoft) e **S3NS** (tecnologia Google). Chi lo dice perde in dieci secondi.

✅ **LA FORMULAZIONE CHE REGGE.** La differenza non sta nella purezza dei fornitori: sta nel fatto che
**la Francia ha scritto un requisito misurabile e l'Italia non ne ha scritto alcuno**. Tre verifiche
binarie: dove è stabilita l'azienda, chi ne controlla il capitale, da dove il servizio è amministrato.

> 🔥 **E la regola ha prodotto il mercato.** Bleu e S3NS **esistono perché la regola esiste**: nessuna
> azienda americana si è ristrutturata per benevolenza, l'ha fatto perché altrimenti non poteva vendere
> allo Stato francese. **Un fatto scomodo per la nostra tesi è la prova che la regola funziona** (già in A29).

> **LA RIGA DA MANDARE IN ONDA:**
> **In Francia un fornitore americano ha dovuto cambiare struttura societaria per vendere allo Stato.**
> **In Italia non gli è stato chiesto di cambiare nulla.**

📊 **Gli otto requisiti della tabella**: sede nell'UE · tetto al capitale extra-UE (24%) ·
amministrazione dall'UE · immunità dichiarata · titolarità delle chiavi · protezione del dato in uso ·
**come viene definita la parola «sovranità»** · **il requisito è in un atto vincolante?**
⚠️ **Sul metodo, dichiarato nella pagina**: «non documentato» significa *letto e non trovato*; «zero
occorrenze» significa *ricerca full-text eseguita, esito riportato*. La distinzione è voluta (regola 10).

📍 **E il colpo finale è già nostro (A15)**: non è che l'Italia non ci avesse pensato. Nel **2021** ne
era **coautrice** a Bruxelles. Ha chiesto la regola lì, l'ha persa nel marzo 2024, e negli stessi cinque
anni **non l'ha mai scritta in casa propria** — l'unico strumento che non dipendeva dal voto di nessuno.

### A54. 🎯 «PSN MANAGED» SONO DUE ARCHITETTURE OPPOSTE — e il lato Google è il livello base francese
**AFFIDABILITÀ: 🟢 ALTA** — documentazione Google, pagina e listino PSN, tutti letti alla fonte.

**La pagina PSN, verbatim**: «The service is based on **two technologies: Google Assured Workload and Oracle
Alloy**» · «hosted in **Italian regions *or* within Polo Strategico Nazionale Data Centres**».
👉 Quell'«**or**» regge tutto: **non sono due fornitori dentro un'architettura, sono due architetture.**

| | **Lato Google** | **Lato Oracle** |
|---|---|---|
| Tecnologia | Assured Workloads | Oracle Alloy |
| Dove gira | **region italiane DI GOOGLE** — Milano `europe-west8`, Torino `europe-west12` | **dentro i DC del PSN** |
| Che cos'è | strato di **policy** su cloud pubblico | **realm separato**, hardware proprio |

🔥 **E il lato Google è lo stesso identico prodotto del livello base francese.** Confrontate le due pagine
Google: *Italy Data Boundary by PSN* e *France Data Boundary by S3NS* hanno **gli stessi 23 servizi con CMEK
obbligatoria**, gli stessi vincoli, le stesse restrizioni sui prodotti, la stessa esclusione dei server MCP.
**Cambia solo l'elenco delle region.**
⚖️ Sulla differenza di region **non si insiste** (decisione del committente): la Francia può aver esteso a
Belgio e Paesi Bassi per accordi propri. Si menziona e si va oltre.

📌 **Due ammissioni dentro la documentazione Google**, identiche nelle pagine italiana e francese:
- «gli *split boundaries* in Bigtable e Spanner **sono accessibili dal personale Google**… e **non sono
  soggetti ai controlli di accesso amministrativo**»
- «non fornisce controlli di residenza **per i dati in uso e in transito**» → **Google usa le nostre stesse
  tre categorie** e dichiara di coprire solo la prima.

🔴 **LA QUINTA OFFERTA — non tutto sta nei data center PSN.** Dal listino, verbatim: il *Secure Public
Cloud Oracle* offre «servizi **non erogabili tramite tecnologia Alloy o non implementabili nei Data Center
PSN**, grazie all'**utilizzo diretto della region pubblica Oracle**», per «superare i limiti» di Alloy —
**Exadata di nuova generazione (X9M, X11M)**, nuove classi compute, Object Storage avanzato.
⚠️ E la mitigazione è di nuovo condizionale: «utilizzo del modello BYOK **ove applicabile**».

### A55. 🔥 ORACLE ALLOY: l'operatore mette il palazzo, Oracle opera i servizi — e nessuna qualificazione ANSSI
**AFFIDABILITÀ: 🟢 ALTA** — documentazione e pagine Oracle lette (in parte dal browser, il fetcher dava 403);
catalogo ufficiale ANSSI di 130 pagine scaricato ed estratto.

**La divisione dei ruoli, verbatim da Oracle**:
> «Oracle Alloy combina una **cloud foundation gestita da Oracle** con uno strato di business e customer
> experience gestito dall'operatore. **Oracle fornisce la piattaforma cloud, le operazioni di servizio
> sicure e la gestione continua del ciclo di vita del prodotto.** L'operatore fornisce **l'ambiente di
> hosting** ed esercita il business cloud rivolto al cliente.»

🎯 **E Oracle chiama l'operatore *rivenditore***: «consente ai partner di **rivendere** servizi cloud
Oracle» · «il ciclo di vita del proprio **business di rivendita cloud**». **È l'Atto 4 del film, scritto dal
fornitore.**
📌 Dettaglio eloquente: il post Oracle intitolato **«Expanding Control & Flexibility»** per gli operatori
Alloy riguarda **valute multiple e rinnovi contrattuali**. Il controllo ampliato è **commerciale**.

**Aggiornamenti** — l'operatore «può gestire in autonomia tutte le attività operative standard, come il
**patching di base e gli aggiornamenti dei servizi**»; Oracle fa «troubleshooting, **upgrade non standard**,
risoluzione dei disservizi ed escalation». Il VP Dedicated Cloud: «un'intera region OCI che l'operatore può
gestire in autonomia, **assistito dagli upgrade e dal supporto di Oracle**».
**Sulle modifiche l'operatore ha una dashboard che «fornisce visibilità»** su cambiamenti «di **emergenza**,
mitiganti, normali e di routine». 🚨 **Verbi solo osservativi: nessuna approvazione documentata.**

✅ **Da riconoscere**: *Operator Access Control* è **più forte di qualunque cosa nel pacchetto Google** — il
cliente **approva o nega** l'accesso dei dipendenti Oracle, con limite di tempo, log dei comandi e
registrazione dei tasti.
🔴 **Ma con tre esclusioni dichiarate da Oracle**: non copre «le **azioni di automazione**… eseguite come
**`root`**… compreso l'accesso **basato su proxy**»; non copre «entità esterne… **o altro software del
control plane**»; **«non è una soluzione di conformità generale»**.
> **Il cancello controlla le persone. Non controlla l'automazione che gira come root.**

📉 **CATALOGO UFFICIALE ANSSI, 130 pagine — occorrenze:**
**Oracle 0 · Microsoft 0 · Amazon 0 · AWS 0 · Polo Strategico Nazionale 0.**
Qualificati SecNumCloud: **Thales Cloud Sécurisé — Cloud de confiance S3NS** (SaaS+PaaS+CaaS, 17/12/2025 →
17/12/2028, **l'unica con tre ambiti**) · Outscale · OVH (×2) · Cloud Temple (×2) · Orange Business ·
Worldline · Oodrive · Whaller · Index Education.
In istruttoria, **sedici**: Adista, **Bleu SAS**, BLUE, Cegedim, Cloud Temple, Ecritel, Free Pro, GIP Mipih,
ITS Integra, NumSpot, NRB, Orange Business, OVH, Prolival, Scaleway, Scalingo.

🕒 **E il dato che pesa**: il **9 febbraio 2021**, davanti all'Assemblea nazionale francese, la direttrice
generale di Oracle France annunciò di essere «in discussione con l'agenzia». **Cinque anni e mezzo dopo,
Oracle non compare né fra i qualificati né fra quelli in istruttoria.**
Microsoft ha costituito **Bleu** ed è in istruttoria; Google ha costituito **S3NS** ed è qualificata
(intestazione a **Thales Cloud Sécurisé**: il titolare è il socio europeo di controllo). **Oracle ha
annunciato una discussione.**

### A56. 🎯 NITRO ENCLAVES PROTEGGE DAL CLIENTE, NON DA AWS — e la «nuova capogruppo europea» è del 2021
**AFFIDABILITÀ: 🟢 ALTA** — documentazione AWS, annuncio ufficiale AWS, e **registro delle imprese tedesco
verificato su due servizi indipendenti**.

#### 🔥 Il modello di minaccia, verbatim dalla documentazione AWS
> «i dati e le applicazioni dentro l'enclave non possono essere acceduti da processi, applicazioni o utenti
> (**root o admin**) **dell'istanza padre**» · «Il Nitro Hypervisor garantisce che **l'istanza padre** non
> abbia accesso alle vCPU e alla memoria isolate dell'enclave»

👉 **Il soggetto escluso è il cliente stesso** — il proprio root, il proprio codice compromesso.
**AWS non è nominata.** È una difesa contro sé stessi, ed è buona ingegneria. **Non è la difesa di cui
parla il dibattito sulla sovranità.**

📌 Due dettagli dalla stessa pagina: «le enclave sono attive **solo mentre l'istanza padre è in stato
running**; se l'istanza è **arrestata o terminata**, le enclave sono terminate» — chi controlla l'hypervisor
controlla l'interruttore. E l'attestazione è integrata con **AWS KMS**, il servizio di chiavi gestito da AWS.

#### ⚖️ Come si tratta il «nemmeno i dipendenti AWS»
AWS fa **la dichiarazione più netta dei tre**: il Nitro System «fornisce un confine tale che **nessuno,
inclusi i dipendenti AWS, può accedere ai carichi di lavoro o ai dati**».
🚨 **Non si smentisce: si mostra che cosa la sostiene.** È l'audit NCC (**A21**), che dichiara da sé
quattro limiti — pagato da AWS, *design review* **senza test**, **fuori perimetro** il control plane EC2,
l'hypervisor, il firmware e le Nitro Card, e **nessuna garanzia** su modifiche tecniche future «scelte o
**imposte**».
> **La dichiarazione descrive un progetto. L'audit di quel progetto esclude espressamente il nostro scenario.**
Contrappeso indipendente — **Trail of Bits**: «devi fidarti completamente di AWS».

#### 🇩🇪 LA STRUTTURA TEDESCA, E CHE COSA DICE IL REGISTRO
✅ **Da riconoscere**: sul piano societario Amazon ha fatto **più di Google e Oracle in Italia**. Annuncio
AWS: «una nuova capogruppo e **tre controllate costituite in Germania**», direzione di «cittadini UE
residenti nell'UE», consiglio consultivo di quattro cittadini UE «fra cui **almeno un membro indipendente
non affiliato ad Amazon**», «legalmente obbligato ad agire nell'interesse dell'AWS European Sovereign
Cloud». Prima region: **Brandeburgo**.

🔥 **Ma il registro racconta un'altra storia** — *Amtsgericht Potsdam, HRB 40853*, verificato su due
servizi di registro indipendenti:
| Data | Iscrizione |
|---|---|
| **12-13.08.2021** | costituita come **SCUR-Alpha 1391 GmbH** · capitale **25.000 €** |
| **21.10.2021** | rinominata **Amazon Germany Holdco 1 GmbH** |
| **23.07.2025** | rinominata **AWS European Sovereign Cloud GmbH**, sede a Potsdam |
| **17.06.2025 → 03.12.2025** | **Kathrin Renz** — l'AD indicata nell'annuncio — nominata e poi **cessata** |
| oggi | **Stephane Israel** (14.11.2025), **Stefan A. Höchbauer** (21.01.2026) |
| oggetto | «la partecipazione in società che… supportano servizi di hosting di dati» |

> **La «nuova capogruppo europea» è una società di comodo del 2021 che fino al luglio 2025 si chiamava
> _Amazon Germany Holdco 1 GmbH_**, con il capitale minimo di legge e un oggetto sociale di holding.
> E **l'amministratrice presentata come volto della governance europea ha lasciato in circa sei mesi.**

🚨 **TRAPPOLA 45 — non presentare la società di comodo come uno scandalo.** Usare una società già
registrata e il capitale minimo di legge è **prassi ordinaria in Germania** e non prova malafede. Il punto
non è la prassi: è **la distanza fra quella prassi e il linguaggio dell'annuncio**.
🔴 **E un limite nostro, dichiarato**: l'**elenco dei soci è a pagamento e non l'abbiamo letto**.
**Non indichiamo alcuna percentuale di proprietà.** Fonti secondarie convergenti indicano il 100% ad
Amazon.com Inc., ma **finché non leggiamo la _Gesellschafterliste_ non lo scriviamo**.

#### 📝 La frase sul «non è mai successo», scritta meglio di quella di Microsoft
> «dal 2020 non ci sono state richieste di dati ad AWS che **abbiano portato alla divulgazione** di contenuti
> **archiviati fuori dagli Stati Uniti** da clienti **aziendali o governativi** al governo statunitense»

**Tre restrizioni in una riga**: non dice che non ci siano state *richieste*, ma che nessuna *ha portato a
divulgazione*; solo contenuti *fuori dagli USA*; solo clienti *aziendali o governativi*. Stessa classe del
verbatim Carniaux, e inverificabile per la stessa ragione.

#### 📉 E i due silenzi
- L'annuncio AWS sulla governance **non tratta in alcun punto il CLOUD Act**.
- Nel catalogo ufficiale ANSSI: **Amazon 0 · AWS 0**. Né qualificata né in istruttoria.
> Microsoft ha costituito **Bleu** ed è in istruttoria; Google ha costituito **S3NS** ed è qualificata.
> **Amazon ha costituito una GmbH tedesca e non l'ha portata alla qualificazione francese.**

#### ✅ E la domanda PSN/AWS è sciolta
Era aperta dal primo giorno: il sito PSN indicava AWS, la Guida alla Convenzione no. **Il listino risolve**:
«integrazione **4° cloud service provider AWS**» (2024), e il *Secure Public Cloud* è basato sui servizi
pubblici «degli hyperscaler Microsoft Azure, Google Cloud, **AWS** e Oracle, con region in territorio
italiano». **La Guida è semplicemente anteriore all'integrazione.**

---

## 🟡 B — SOLIDO, DA CONFERMARE PRIMA DELLA MESSA IN ONDA

### B1. La dichiarazione di Butti del 21 luglio 2026
75% raggiunto · oltre 13.000 PA · 1,9 miliardi PNRR · oltre 280 PA centrali/ASL su PSN · oltre 12.700 PA
locali **e scuole** su «cloud qualificati» · oltre 135.000 servizi.
Verbatim: «Con questo risultato **l'Italia si pone tra i Paesi europei più avanzati nella protezione dei
dati della pubblica amministrazione**.»
**Non usa mai l'espressione «sovranità digitale»**: parla di sicurezza e protezione dei dati.
🔗 https://www.key4biz.it/pnrr-butti-oltre-13mila-pa-in-cloud-75-centrati-obiettivi-ue/581879/
✅ **DECISO — si procede sul lancio d'agenzia.** Rischio residuo messo a verbale: la fonte è Adnkronos,
non l'atto originale del Dipartimento. Il virgolettato è stato ripreso in pari data da più testate in modo
concorde, quindi la citazione è solida; ma **in trasmissione va attribuita all'agenzia**, non presentata
come comunicato ufficiale. Se il comunicato primario emergesse, si aggiorna l'attribuzione.

### B2. La citazione del Senato francese
Scambio Wattebled/Carniaux del 10/06/2025, **sotto giuramento**, con richiamo alle pene per falsa
testimonianza. Risposta integrale: «Non, je ne peux pas le garantir, **mais, encore une fois, cela ne s'est
encore jamais produit**.» Ripresa nel rapporto del Senato n. 830 dell'8 luglio 2025.
🔗 https://www.senat.fr/compte-rendu-commissions/20250609/ce_commande_publique.html
🔗 Video ufficiale: https://videos.senat.fr/commission.COPU
**Da fare**: ricontrollare l'**audio del video** contro il resoconto scritto prima della messa in onda
(il *compte rendu* è un resoconto rivisto, non una trascrizione stenografica).

### B3. SecNumCloud 3.2 contiene la clausola di immunità
Richiede immunità dalle legislazioni extraterritoriali + **controllo europeo del capitale** + personale
operativo europeo. Unico schema nazionale che esclude *strutturalmente* il CLOUD Act.
Qualificati a metà 2026: **OVHcloud**; **S3NS** (fine 2025, 30 servizi, roadmap a 150). **Bleu** in corso.
🔗 https://www.erpimplementation.eu/en/erp-sovereign-cloud-europe-secnumcloud-hds-bsi-c5-2026/
**Da fare**: citare l'articolo/sezione sul **referenziale ANSSI originale**, non su fonte secondaria.
🔗 Riferimento primario da aprire: https://cyber.gouv.fr/ (sezione SecNumCloud)

### B4. Il lobbying tech a Bruxelles
€151 mln/anno (da €113 mln nel 2023) · top 10 = €49 mln, 7 su 10 statunitensi · Meta €10M, Microsoft €7M,
Apple €7M, Amazon €7M, Google €4,5M · **890 lobbisti** a tempo pieno · **437 badge permanenti** al PE
(su 720 deputati) · 378 incontri istituzionali nel primo semestre 2025 (~3 al giorno).
Fonte: Corporate Europe Observatory / LobbyControl su Registro trasparenza UE.
**⚠️ Sono sottostime**: il registro dichiara fasce, le analisi usano il limite inferiore.
**⚠️ CEO e LobbyControl sono ONG di advocacy**: dichiararlo.
🔗 Registro trasparenza UE: https://transparency-register.europa.eu/

### B5. La rimozione dei requisiti di sovranità dall'EUCS
22 marzo 2024: la terza bozza rimuove i requisiti di sovranità, sparisce il livello «High+».
Pressione **convergente**: industria USA + governo USA (via TTC/USTR) + **una coalizione di dodici Stati
membri guidata dai Paesi Bassi**. Fonte più autorevole: **EUISS** (istituto di studi strategici ufficiale UE).
Prova documentale più forte: comunicato **ITI**, *«ITI Urges EU Lawmakers to Drop Sovereignty Requirements
in Final EUCS»*.
**⚠️ Non dire «la lobby americana ha cancellato la regola»**: dodici governi europei hanno spinto nella
stessa direzione. La versione corretta è più scomoda, non meno.

### B6. Investimenti annunciati in Italia
Microsoft €4,3 mld (2 ottobre 2024, con incontro Brad Smith–Meloni tracciato su governo.it) ·
AWS €1,2 mld (novembre 2024, con accesso alla procedura per le infrastrutture strategiche nazionali) ·
Google $900M dal 2020 (region Milano e Torino con TIM) · Equinix €4 mld 2026-2033.
**⚠️ Cifre in conflitto tra fonti**: Microsoft €4,3 vs €10 mld; AWS €1,2 vs €2 mld. Da chiudere.

---

## ⚫ D — CONTRADDIZIONI ✅ RISOLTE

### D1. Stato reale dei livelli EUCS (🔴 bloccante)
- **EUISS** (dossier 04): i requisiti di sovranità furono **rimossi** il 22/03/2024.
- **sota.io** (2026): il livello **High** *include* proprietà europea, personale UE per accessi privilegiati
  e giurisdizione esclusivamente UE; i fornitori con capogruppo USA **non** possono qualificarsi.
Non possono essere entrambe vere.
🚨 **sota.io è un fornitore commerciale che elenca sé stesso tra i qualificabili**: conflitto d'interesse.
🔗 https://sota.io/blog/eucs-cloud-assurance-levels-which-providers-qualify-eu-sovereignty-2026
🔗 **Fonte da consultare per dirimere**: https://www.enisa.europa.eu/ (schema EUCS)
✅ **RISOLTA — vedi A14: ha ragione EUISS. L'EUCS non è ancora stato adottato e nessun livello contiene requisiti di sovranità.** La pagina sota.io, riletta, oggi afferma essa stessa l'opposto di quanto le era stato attribuito.

---

## 🔴 C — APERTO: NON UTILIZZABILE FINCHÉ NON VERIFICATO

| # | Domanda aperta | Perché è importante | Dove cercare |
|---|---|---|---|
| ~~C1~~ | ~~Il Regolamento ACN contiene una clausola di immunità?~~ | ✅ **RISOLTO — vedi A7. Risposta: NO**, verificato sul testo integrale | — |
| ~~C2~~ | ~~Come si è espressa l'Italia in sede ECCG?~~ | ✅ **RISOLTO — vedi A15. Ha co-scritto i criteri di immunità e ha perso** | — |
| ~~C3~~ | ~~Quanto denaro PNRR è finito a fornitori USA?~~ | ✅ **RISOLTO — vedi A9. Non è tracciabile, e l'assenza è documentata** | — |
| ~~C4~~ | ~~Quanti servizi qualificati ACN poggiano su tecnologia USA?~~ | ✅ **RISOLTO — vedi A10.** Catalogo analizzato: 2.107 schede, 826 fornitori | — |
| ~~C5~~ | ~~Esito causa Fastweb/Aruba~~ | 🗂️ **Vicenda esclusa dal film** (irregolarità negli appalti, non sovranità; l'offerta Aruba-Fastweb non è dimostrabilmente più sovrana). Resta nel dossier | — |
| ~~C6~~ | ~~Tenuta del Data Privacy Framework?~~ | ✅ **RISOLTO — vedi A12. Il DPF non copre il CLOUD Act e lo dice per iscritto** | — |
| ~~C7~~ | ~~Asimmetria USA/Cina/UE e scuola~~ | ✅ **RISOLTO — vedi A13, con tre assunti di partenza CORRETTI** | — |
| ~~C9~~ | ~~Fornitori cloud europei autorizzati FedRAMP?~~ | ✅ **RISOLTO — vedi A16. Zero.** | — |
| ~~C10~~ | ~~Dati delle scuole italiane?~~ | ✅ **RISOLTO — vedi A17. Istruzione 77,2%, il peggiore del dataset** | — |
| **C8** | **Aruba S.p.A.** è tra i firmatari EUCS High+? | Il link nell'elenco punta a HPE Aruba Networks | ✅ **parzialmente risolto in A15**: è firmataria certa della lettera del 10/04/2024; per quella del 10/06/2024 l'ambiguità resta |
| **C11** | Testo originale del **DoD Cloud SRG** | È la riga più importante del blocco asimmetria e non è mai stata letta in originale | PDF su `dl.dod.cyber.mil` — apertura manuale |
| **C12** | **Comune italiano** con videosorveglianza (o AI di riconoscimento) su AWS/Google/Microsoft | Servirebbe per il filone «Trump vede anche chi passa per strada». ⚠️ **Attenzione**: in Italia vige una moratoria sul riconoscimento facciale in luoghi pubblici — da verificare stato e portata prima di impostare la narrativa | Delibere comunali, bandi, provvedimenti del Garante |

*(Risolti: C1 → A7 · C2 → A15 · C3 → A9 · C4 → A10 · C6 → A12 · C7 → A13. Restano C5, C8, C9, C10 — tutte verifiche manuali su fonti non automatizzabili.)*

---

## 🔴 CORREZIONE APERTA — LA CONCLUSIONE È INCOMPLETA (riscontro esterno, da recepire)

**Il rilievo**: la conclusione attuale del film («non smettere di usare Microsoft, smettere di lasciarla
operare») presenta **una sola** via d'uscita — il *cloud di fiducia*, cioè tecnologia statunitense in licenza
operata da un'entità europea (livello 3 della scala). **Ne manca un'altra, ed è la più diretta**: usare
**direttamente fornitori nazionali ed europei**, che non sono affatto pochi, senza che debbano essere
piattaforme Microsoft, Amazon o Google (livello 4).

**Perché il rilievo è fondato e va recepito:**
- Il livello 3 continua comunque a far uscire **canoni di licenza** verso aziende statunitensi: risolve la
  giurisdizione, non la dipendenza economica né quella industriale.
- Presentare il livello 3 come *la* soluzione suggerisce implicitamente che **non esistano alternative
  native**. È falso, ed è la premessa che vogliamo smontare.

### 🎯 IL DATO CHE ROVESCIA LA CHIUSURA — ed è nostro

| | Enti | Quota |
|---|---|---|
| Provider italiano | 9.842 | 42,9% |
| Infrastruttura autonoma | 833 | 3,6% |
| Cloud italiano | 904 | 3,9% |
| **TOTALE ITALIANO** | **11.579** | **50,5%** |
| Extra-UE | 9.915 | 43,3% |

> **Gli enti italiani su fornitori italiani sono già PIÙ di quelli su fornitori extra-UE: 50,5% contro 43,3%.**
> L'alternativa non va inventata né importata: **è già la pratica maggioritaria della Pubblica
> Amministrazione italiana.** Undicimilacinquecento enti la usano oggi.

> 📅 **AGGIORNAMENTO 7 NOVEMBRE 2026 — metodologia irrobustita (mxmap.it#29, "scenario B").**
> Tutte le cifre di questo registro sono state riallineate ai dati del 7/11/2026. Due cambi di
> metodo, da conoscere per non farsi smontare in intervista:
> 1. il classificatore ora attribuisce un cloud **solo con segnali primari** (routing MX, SPF
>    corroborato, autodiscover, DKIM): le semplici registrazioni Microsoft/Google (tenant, token)
>    non bastano più → centinaia di enti dietro filtri antispam sono passati da "Microsoft/Google
>    presunto" a **Sconosciuto** (dal 2,7% al 5,7%) — per questo l'extra-UE scende da 46,1% a 43,3%:
>    **la dipendenza è misurata senza sovrastime, il che rende il dato PIÙ difendibile in camera**;
> 2. gli enti la cui posta è gestita dal **fornitore informatico** (Halley, farm Zimbra, ecc.) ora
>    contano come "Provider italiano", non come "Infrastruttura autonoma": per questo l'autonoma
>    crolla da 13,5% a 3,6% e i commerciali salgono — la lettura giusta è "gestita da un fornitore
>    italiano", NON "il Comune ha i suoi server". Mai più dire "un ente su otto fa da sé".

**Conseguenza narrativa**: il film non deve chiudere con «*ecco cosa si potrebbe fare*», ma con
**«ecco cosa metà di voi già fa — perché non gli altri?»**. Si passa da un finale prescrittivo a un finale
**fattuale**, che è più forte e non chiede al pubblico di fidarsi di una proposta.

### Da modificare quando si recepisce
- [ ] **SCRIPT Atto 11** (`La via d'uscita`): due strade, non una. La seconda è la nativa, con il 50,5%.
- [ ] **BOOKLET tavola 13**: idem — i tre precedenti (USA, Cina, Francia) illustrano il livello 3, ma la
      chiusura deve mostrare anche la via diretta.
- [ ] **STORYBOARD Atto 11** (inquadrature 104-116) e relativa scheda grafica.
- [ ] **Sito `/certificazioni/`**: la pagina ha già il livello 4 nella scala, ma la tesi finale in una riga
      («non smettere di usare Microsoft, smettere di lasciarla operare») va integrata.
- [ ] **Policy Brief IT+EN**: la raccomandazione n. 4 dice «non serve escludere i fornitori statunitensi:
      serve che il servizio sia operato da un'entità europea autonoma» — va aggiunta la via diretta.
- [ ] Valutare una **nuova scheda grafica** `13-alternativa-esiste-gia.svg` con il 50,5% contro il 43,3%.

⚠️ **Cautela**: «Provider italiano» e «Cloud italiano» sono categorie della classificazione MxMap, non un
elenco di aziende verificate una per una. Prima di nominare fornitori specifici in TV vanno verificati
singolarmente (sede, controllo societario, infrastruttura propria). Il **dato aggregato** è invece solido.

---

## 🔴 SECONDA CORREZIONE APERTA — la lettera EUCS High+ manca dal film

**Il rilievo**: la lettera per l'inclusione dei criteri High+ (`eucshighplus.eu`) — **del tutto analoga nella
sostanza a SecNumCloud**, perché chiede gli stessi criteri di immunità — è firmata anche da **aziende
italiane**, mentre il Governo non ha mai introdotto una regolamentazione nazionale equivalente.

**Verifica di copertura (fatta il 29/07/2026):**

| Artefatto | Aziende italiane firmatarie | EUCS High+ |
|---|---|---|
| Sito `/certificazioni/` | ✅ presenti | ✅ presente |
| Policy Brief IT+EN | ✅ presente | ✅ presente |
| **SCRIPT** | ❌ **assente** | ❌ **assente** |
| **BOOKLET** | ❌ **assente** | ❌ **assente** |
| Storyboard | 1 sola menzione | 2 menzioni |

👉 **Il nesso è documentato sul sito e nei PDF, ma NON arriva in televisione né al lettore del fumetto.**

### Come va formulato — attenzione, la versione ovvia è sbagliata

❌ **NON**: «l'industria italiana lo chiede, il Governo no» — implica che il Governo non l'abbia chiesto.
**È falso**, e lo abbiamo documentato in A15: l'Italia **co-scrisse** i criteri di immunità nel non-paper
del 2021 con Francia, Germania e Spagna, non firmò il non-paper contrario del 2022, e nell'aprile 2024 il
Sottosegretario contestò pubblicamente la loro rimozione.

✅ **La versione corretta è più netta e più scomoda:**

> **Le hanno chieste tutti. A Bruxelles.**
> Il Governo italiano le ha co-scritte nel 2021. L'industria italiana — **Leonardo, Fincantieri, Generali,
> Telecom Italia** — le ha sottoscritte nel 2024, insieme ad Airbus, Banque de France, Thales e altre
> cinquantotto organizzazioni.
> **E in Italia quella regola non l'ha scritta nessuno.**

Il paradosso non è fra industria e Governo: è fra **ciò che l'Italia chiede in Europa** e **ciò che non
scrive in casa propria** — l'unico strumento che non dipendeva dal voto di nessun altro.

### Da modificare
- [ ] **SCRIPT Atto 9** (`Bruxelles: l'Italia ha chiesto, e ha perso`, 15:45-17:00): aggiungere la lettera
      del 2024 e i quattro nomi italiani. L'atto già racconta la co-autoria del 2021: la lettera **completa
      l'arco** mostrando che la richiesta è continuata fino al 2024, e da parte dell'industria.
- [ ] **BOOKLET tavola 11** (atto 9): idem.
- [ ] **STORYBOARD** inquadrature 090-096: prevedere la scheda con i firmatari.
- [ ] Valutare una scheda grafica con i **62 firmatari** raggruppati per settore, evidenziando i quattro
      italiani. *(La lista completa è in A6.)*

⚠️ **Cautele già agli atti**: non presentarlo come ipocrisia delle aziende (trappola 5 — chiedere che uno
standard esista è compatibile con l'operare secondo le regole vigenti); e l'ambiguità «Aruba» nella lettera
del 10/06/2024 resta (v. A6), mentre **Aruba S.p.A. è firmataria certa** di quella del 10/04/2024 (A15).

---

## 🟠 TERZA CORREZIONE APERTA — il caso cinese c'è, ma è anonimo

**Verifica di copertura (29/07/2026)** — il caso **è già in tutti gli artefatti**, con il verbatim e la
struttura a tre precedenti (USA · Cina · Francia). Ma:

| Artefatto | Caso Cina | Verbatim «non gestisce il servizio» | **Nome del partner** |
|---|---|---|---|
| Script | ✅ | ✅ | ❌ **assente** |
| Booklet | ✅ | ✅ | ❌ **assente** |
| Storyboard | ✅ | ✅ | ❌ **assente** |
| Sito `/certificazioni/` | ✅ | ✅ | ✅ presente |

👉 Il film dice «**un'azienda cinese**». Il sito dice **21Vianet**. La differenza non è cosmetica:
un nome è **verificabile**, un'astrazione no. E qui il nome è la prova che il modello è **realizzato**,
non teorico.

### Come rafforzarlo
Nominare l'azienda e dire cosa fa, con il dettaglio che rende il modello concreto:
**Shanghai Blue Cloud Technology Co. (21Vianet)** — che secondo la documentazione Microsoft
«*gestisce, fornisce e amministra **in modo indipendente**»* l'erogazione dei servizi cloud Microsoft in
Cina, **su licenza della tecnologia**, con data center che mantengono i dati nel Paese.

**Il punto di forza da esplicitare**: non è un accordo commerciale qualsiasi. È **Microsoft che rinuncia a
gestire il proprio prodotto** in un mercato, perché quel mercato l'ha imposto come condizione.

### ⚠️ Il vincolo che diventa più stringente nominando l'azienda
La **trappola 7** resta e va rafforzata: **il modello cinese non tutela i diritti**, risponde a esigenze di
controllo statale. Nominare 21Vianet rende il caso più concreto e quindi **più facile da fraintendere**.
La formulazione deve restare **strettamente strutturale**:

> *Non stiamo dicendo che il modello cinese sia un buon modello. Stiamo dicendo una cosa sola:
> **quando un governo lo impone come condizione di mercato, il modello si realizza.**
> La Cina l'ha imposto. La Francia l'ha imposto. L'Italia no.*

### Da modificare
- [ ] **SCRIPT Atto 11**: sostituire «un'azienda cinese» con il nome e la citazione dell'indipendenza operativa.
- [ ] **BOOKLET tavola 13**: idem — il nome può stare su un'insegna disegnata, più efficace di una didascalia.
- [ ] **STORYBOARD** inquadrature 104-116: prevedere la sovrimpressione del nome.
- [ ] Valutare l'inserimento nella scheda **`01-scala-sovranita`** o in una nuova scheda dei tre precedenti.

---

## ✅ CHIUSO — il PSN misurato con il metro europeo (SecNumCloud / EUCS High+)

> **Prodotto il 02/08/2026.** Reperti **A50, A51, A52, A53** su fonte primaria; tabella pubblica a otto
> requisiti su **/misure-tecniche/** sezione 7.1; scheda **`15-psn-metro-europeo.svg`**; segmento in voce
> scritto nell'**Atto 7** e ripartito su quattro inquadrature (`065-BIS`–`065-QUINQUIES`).
> 🔴 **Resta ignoto un solo dato**: quale dei tre livelli PSN sia il più adottato dagli enti. Senza,
> si descrive l'architettura ma **non si quantifica in voce**.
>
> *Quanto segue resta come specifica di progetto e come riferimento per ogni futura revisione.*

### Specifica originaria

**Richiesta del committente (02/08/2026)**: produrre l'analisi che spiega **la differenza fra i requisiti del
PSN e quelli di SecNumCloud ed EUCS High+**, nella parte in cui il PSN **agisce da rivenditore di servizi
cloud Microsoft, Google e Amazon**.

🎯 **Perché serve, e perché è il pezzo che ancora manca.** Il film dice già che il PSN poggia su Oracle,
Google, Azure e AWS (**A2**) e che il regolamento ACN non nomina mai il CLOUD Act (**A7**). Ma non ha ancora
il **confronto articolo per articolo** fra ciò che il PSN chiede e ciò che chiedono i due metri europei.
Senza quel confronto la nostra resta un'affermazione; con quel confronto diventa **una misurazione**.
È anche ciò che rende dicibile la tensione su **Aruba** (A47): un partner del PSN che chiede a Bruxelles il
criterio di immunità che il PSN stesso non applica.

### 🎯 LA TESI DA VERIFICARE — dettata dal committente il 02/08/2026
*(È l'ipotesi guida dell'analisi. **Non è ancora un reperto**: è ciò che l'analisi deve dimostrare o
smentire su fonte primaria. Fino ad allora **non entra in voce nel film**.)*

**Il PSN va scomposto in due piani, e la critica riguarda solo il secondo.**

✅ **Piano 1 — il consolidamento. Qui il PSN fa una cosa utile, e va detto per primo.**
Portare in poche infrastrutture presidiate i server sparsi in migliaia di enti è un guadagno reale di
continuità, sicurezza fisica e gestione — **qualunque software ci giri sopra**. Chi attacca il PSN
ignorando questo perde il contraddittorio nei primi trenta secondi, e **merita di perderlo**.

🔴 **Piano 2 — i servizi cloud erogati come PaaS e SaaS. È qui che la parola «sovranità» non regge.**
Questi servizi sarebbero **interamente gestiti da Microsoft, Google e Amazon**, e **senza** i vincoli che
altrove sono stati imposti:
- **senza** i requisiti di **SecNumCloud** (sede, controllo del capitale, amministrazione del servizio
  dall'Unione — il §19.6);
- **senza** la separazione dell'operatore imposta alla Cina, dove il servizio è gestito da
  **21Vianet** e Microsoft dichiara di fornire la tecnologia ma di **non gestire il servizio** (A4).

> **È la critica più importante da rivolgere al programma italiano**, e va formulata così:
> **il PSN è un ottimo programma di consolidamento a cui è stato dato il nome di un programma di
> sovranità.** Le due cose non coincidono, e la seconda non è mai stata fatta.

🎯 **Il confronto che rende la tesi inattaccabile — tre paesi, stesso fornitore:**
| | Cosa ha preteso lo Stato | Esito |
|---|---|---|
| 🇨🇳 **Cina** | che il servizio sia **operato da un'azienda locale** | 21Vianet: «Microsoft non gestisce il servizio» |
| 🇫🇷 **Francia** | criteri di **capitale e amministrazione** (SecNumCloud §19.6) | Bleu e S3NS |
| 🇮🇹 **Italia** | *(da verificare: risulta nulla di equivalente)* | il fornitore resta l'operatore |

🚨 **VINCOLI DI FORMULAZIONE — la tesi è forte, e proprio per questo va detta con precisione**
1. **«Non ha niente di sovranità» non può essere affermato finché non abbiamo letto i capitolati.**
   Oggi abbiamo **indizi convergenti e forti** (A2: il PSN poggia su Oracle, Google, Azure e AWS; A7: il
   regolamento ACN ha **zero occorrenze** di CLOUD Act, nazionalità, capitale, paese terzo), **ma non la
   prova diretta di chi opera che cosa.** Quella prova è esattamente l'oggetto di questa analisi.
2. **Distinguere sempre «non c'è» da «non l'abbiamo trovato»** (regola 10). Il modello è la scansione a
   zero occorrenze: si dichiara che cosa è stato cercato, dove, e con quale esito.
3. **Nessuna accusa alle aziende.** Né ai fornitori, né ai partner italiani del PSN. Il bersaglio è **la
   scelta pubblica di non scrivere i requisiti**, non chi lavora dentro il perimetro che ne è risultato.
4. **Il piano 1 va riconosciuto prima del piano 2, in voce e non in nota.** È ciò che rende credibile il
   piano 2 — e senza, il pezzo suona come un attacco politico.
5. ⚠️ **Il modello cinese non va mai presentato come tutela dei diritti** (trappola 7). Serve **solo** a
   dimostrare che **quando un governo lo impone, il fornitore lo realizza**. Vale anche qui.

### 🔎 Che cosa serve per chiudere l'analisi — le domande a cui rispondere
1. **Quali servizi PSN sono erogati come PaaS/SaaS su tecnologia dei tre fornitori, e con quale modello
   operativo?** È la domanda centrale: chi ha le credenziali di amministrazione, da dove si opera,
   chi può aggiornare il piano di controllo.
2. **La qualificazione ACN distingue fra IaaS consolidato e servizi rivenduti?** E con quali requisiti
   diversi, se li distingue.
3. **Esiste, in qualunque atto italiano, un requisito di controllo societario o di nazionalità
   dell'operatore?** Se non esiste, dirlo con la stessa tecnica di A7.
4. **Le tre domande già previste al PSN nel diritto di replica** (confidential computing, chi opera
   l'infrastruttura, perché il CLOUD Act non è mai citato) **vanno poste per iscritto**: una risposta
   è un reperto, un rifiuto documentato è materiale narrativo.

### Come va costruita — tre colonne, stessa riga
Per ciascun requisito, mettere a confronto **PSN** / **SecNumCloud 3.2** / **EUCS High+**:
1. **Controllo del capitale e della governance** — SecNumCloud §19.6 (immunità da leggi extraterritoriali,
   soglie di partecipazione extra-UE); High+ come richiesto dalla lettera dei 62; PSN: **che cosa chiede?**
2. **Nazionalità e localizzazione del personale di esercizio e del supporto** — chi può mettere le mani sui
   sistemi, e da quale paese. È il punto su cui il documento del Governo danese (**A40**) cita testualmente
   il supporto «dagli Stati Uniti».
3. **Titolarità delle chiavi di cifratura** e possibilità tecnica del fornitore di accedere al dato in chiaro.
4. **Regime del software di terzi** — da confrontare con **CADA Allegato II livello 3** (software licenziato
   da un soggetto di paese terzo ammesso **con audit del codice sorgente e piano di migrazione**) e
   **livello 4** (nessun controllo effettivo di un paese terzo). Vedi **A45**.
5. **Reversibilità e uscita** — e la sola scadenza vincolante del quadro: **Data Act art. 29, 12 gennaio
   2027** (A46).
6. **Che cosa comporta esattamente il ruolo di rivenditore**: contratto, responsabilità, e soprattutto
   **se la catena di comando tecnica resti o meno presso il fornitore statunitense**.

### Vincoli di metodo — non negoziabili
✅ **Fonti primarie**: regolamento e determine ACN, capitolati e documentazione contrattuale PSN,
referenziale **SecNumCloud 3.2** in francese, testo della lettera EUCS High+ e proposta **CADA**.
🚨 **Se un requisito nel PSN non c'è, va detto che non c'è — e va distinto da «non l'abbiamo trovato»**
(regola 10 di CLAUDE.md). La scansione a zero occorrenze di A7 è il modello: si dichiara che cosa è stato
cercato, dove, e con quale esito.
⚠️ **Contro-argomento da anticipare**: il PSN persegue **obiettivi diversi** da SecNumCloud (continuità,
qualificazione, consolidamento dei data center) e non è nato come schema di immunità giurisdizionale.
Il confronto va posto come **«misura ciò che l'Europa misura?»**, non come «il PSN ha sbagliato tutto».
⚠️ **Nessuna accusa ad Aruba o agli altri partner**: il punto è il **quadro normativo**, non le aziende che
ci lavorano dentro.

📍 **Dove finirà nel film**: **Atto 7 — Lo Stato certifica, e non sa** (che nel passaggio a 30 minuti
cresce da 135" a 180" proprio per ospitarlo), con rimando al sito per la tabella completa.

---

## 📋 TODO DIFFERITO — analisi di fattibilità sulla produzione con AI generativa

**Richiesta del committente (29/07/2026)**: **a lavori conclusi e confermati**, produrre un'analisi di
fattibilità su **quali AI usare** (Claude stesso o altri) per realizzare:
1. il **booklet a fumetti**;
2. il **documentario video interamente virtuale**, con AI generativa e cattura di video/schermate di siti,
   immagini, schede e altro materiale esterno.

⚠️ **Da NON fare adesso**: l'analisi va scritta quando script, storyboard e booklet sono definitivi,
altrimenti si valuta una produzione su un bersaglio che si muove.

### Punti già identificati, da sviluppare nell'analisi

**Sul fumetto — il problema difficile è la coerenza, non la qualità del disegno**
- Marta, Sandro, la **Busta** e il **Cursore** devono restare riconoscibili su ~90 vignette in 13 tavole, due delle quali a doppia pagina.
  È il vincolo che decide la scelta del modello, non la resa estetica della singola immagine.
- ⚠️ **La regola «si disegnano le mani, non i volti» taglia due volte**: risolve l'identificabilità delle
  persone reali, **ma le mani sono il punto debole storico dei generatori di immagini**. Va verificato per
  primo, perché se non regge cambia la direzione artistica.
- **Il testo nei balloon va prodotto separatamente** (lettering in post): i modelli lo rendono male ed è
  comunque la prassi professionale del fumetto.
- Da valutare: i due «riquadri di onestà», la **mappina del viaggio** e l'**impronta fantasma** sono
  elementi grafici ricorrenti a precisione millimetrica — probabilmente **vettoriali fatti a mano**, non
  generati.

**Sul video — l'intuizione controintuitiva: forse serve poca AI generativa**
- Lo storyboard, **per scelta deliberata**, ha evitato tutto ciò che non si può filmare. Il risultato è che
  **una quota molto alta delle 139 inquadrature è tipografica o grafica**: il terminale, le tabelle, le 14
  schede SVG, i documenti, i verbatim. Quelle **non richiedono video generativo**: richiedono motion
  graphics, che è un problema risolto.
- 👉 **Da quantificare come prima cosa**: quante delle 139 inquadrature sono `GRAF`/`TXT`/`schermo` e quante
  richiedono davvero immagini generate. Il rapporto decide l'intero impianto produttivo.
- Ipotesi da valutare: rendering **programmatico** del blocco tipografico partendo dai dati già strutturati
  (storyboard + schede + file dati). Vantaggio non estetico ma **di manutenzione**: quando lo script cambia,
  il video si rigenera invece di essere rimontato.
- Servono comunque: **voce narrante** (qualità dell'italiano è il criterio), b-roll d'atmosfera per la
  *simulazione documentata*, e le **6-8 interviste**, che sono **persone reali e non sono sostituibili**.

**Vincoli non tecnici, che pesano quanto quelli tecnici**
- 🚨 **Dichiarazione dell'uso di AI**: un documentario sulla verificabilità e sulla fiducia che usasse
  materiale generato **senza dichiararlo** si smonterebbe da solo. La trasparenza qui non è conformità:
  è coerenza con la tesi.
- 🚨 **Nessuna immagine generata di persone reali identificabili.** Vale per Carniaux, Wattebled, Hadinger,
  Butti e per chiunque altro. La regola già adottata negli artefatti va estesa alla produzione.
- ⚖️ **Diritti sul materiale esterno**: video del Senato francese, immagini di stampa, schermate. Il tema
  esiste **a prescindere** dall'AI e va trattato separatamente.
- 🤔 **Questione di coerenza politica, da porre esplicitamente al committente**: un progetto sulla sovranità
  digitale che si produce interamente su modelli statunitensi. Non è una contraddizione insanabile — noi
  documentiamo la dipendenza, non la neghiamo — ma **va deciso consapevolmente e, se del caso, dichiarato**.
  Vanno considerate anche le alternative europee, con una valutazione onesta di dove reggono e dove no.

---

## ERRORI DA NON COMMETTERE (registro delle trappole già individuate)

1. **Il 43% non è una quota del 75%.** Sono universi diversi: il 43% misura la posta elettronica, il 75%
   la migrazione al cloud. Dire «di quel 75%, il 43% è americano» è indifendibile.
   Formulazione corretta: *«Il Governo dichiara. Noi abbiamo misurato.»*
2. **CLOUD Act ≠ FISA 702.** Per spiare un funzionario straniero lo strumento pertinente è la **702**
   (bersagli non-americani all'estero), non il CLOUD Act, che è procedura penale. Citarne uno solo ci
   espone a smentita da parte di un giurista.
3. **Non tutti i partner italiani sono «meri rivenditori».** Vero per system integrator e region
   hyperscaler; falso per operatori con infrastruttura propria (Aruba, Seeweb…) e per il PSN, che dichiara
   custodia delle chiavi. Servono le quattro categorie del dossier 07.
4. **Non dire «Butti ha rivendicato la sovranità digitale»**: non l'ha detto. Ha detto «protezione dei dati».
5. **Non accusare di ipocrisia** Leonardo, TIM, Fincantieri e Generali per aver firmato la lettera High+:
   chiedere che uno standard esista è compatibile con l'operare secondo le regole vigenti.
6. **Non tagliare** l'inciso «ma, ancora una volta, ciò non si è ancora mai verificato»: mandarlo in onda
   integralmente è ciò che rende la citazione inattaccabile.
7. **Non presentare il modello cinese come tutela dei diritti**: risponde a esigenze di controllo statale.
   L'argomento corretto è solo strutturale — *quando un governo lo impone, il modello si realizza*.
8. **Non confondere base d'asta e spesa effettiva.** I «2,7 miliardi» del PSN **non sono soldi che lo Stato
   versa**: sono il tetto di valore della concessione, cioè il fatturato potenziale massimo generabile in
   tredici anni vendendo servizi alle PA. La Corte dei conti segnala che è *l'errore giornalistico più
   frequente su questo dossier*. Farlo in TV significa regalare la replica.
9. **Non dire che la prelazione fu un espediente**: era prevista dal bando e nota a tutti prima delle offerte.
   Il fatto è un altro, ed è più forte: **il Consiglio di Stato ha accertato che quell'esercizio fu illegittimo**.
10. **Non dire che gli americani hanno il livello massimo di qualificazione**: i nove servizi QC4 sono tutti
    e soli nativi PSN. Dirlo rafforza la nostra credibilità sul resto.
11. **Non dire «il Buy American Act esclude il software europeo»**: la FAR 25.103(e) esenta l'IT commerciale
    e il BAA non copre i servizi. È l'errore che ci farebbe smontare più in fretta di tutti.
12. **Non dire «FedRAMP impone la cittadinanza americana»**: l'obbligo FOCI riguarda gli **auditor 3PAO**,
    non i fornitori cloud. Il divieto su cittadinanza esiste solo nel DoD Cloud SRG, cioè solo per la Difesa.
13. **Non citare il «Documento 79» cinese come ordine di rimuovere il software straniero**: la versione
    pubblica tradotta da CSET non lo dice. Usare invece la lista MIIT/CISEC del 26 dicembre 2023.
14. **Non omettere l'avanzo di 60,4 mld € sui servizi informatici** quando si cita il disavanzo di 126,3 mld
    sui canoni IP: ometterlo è manipolatorio, e la contro-parte lo sa.
15. **Non dire che l'Assia ha vietato Microsoft nelle scuole**: quel divieto fu ritirato dopo tre settimane.
    Il caso solido è il **Baden-Württemberg**.
16. **🔴 LA PIÙ IMPORTANTE — non dire «l'Italia non ha chiesto la sovranità»**: è falso. L'ha **co-scritta**
    nel 2021 con Francia, Germania e Spagna, non ha firmato il non-paper contrario nel 2022, e nell'aprile
    2024 il Sottosegretario ha pubblicamente contestato la rimozione. Il divario vero è **fra ciò che
    l'Italia ha chiesto a Bruxelles e ciò che ha scritto in casa propria**. Chi ha seguito il dossier lo sa,
    e la formulazione sbagliata ci farebbe passare per disinformati.
17. **Non affermare che l'Italia era tra i dodici Stati che chiesero la rimozione**: quell'elenco **non
    esiste in fonte pubblica**. È una deduzione, e va detta come tale.
18. **Non dire «è una controllata europea, quindi è soggetta al CLOUD Act»**: il DOJ qualifica la
    questione come *fact-dependent* e non esiste giurisprudenza nota che lo affermi. La formulazione
    corretta è che **la struttura societaria non muta di per sé l'analisi** — lo dice il DOJ — e che
    **AWS non ha mai sostenuto di essere immune**. L'equivoco sta nella parola «sovereign».
19. **Riconoscere che la cifratura con chiavi esterne di AWS è una difesa tecnicamente valida** per il
    dato a riposo. Negarlo ci fa perdere il contraddittorio su un punto in cui hanno ragione.
20. **VIETATO dire «Google ha mentito»** sull'audizione del 2019: il verbatim consente due letture e il
    dubbio resta. Formulazione corretta: **«Google usa una definizione di CLOUD Act che esclude proprio il
    meccanismo che conta»** — e la smentita si fa citando **il Senato francese**, che scrive «*et
    indépendamment*» senza accusare nessuno.
21. **Non dire che la Danimarca «ha vietato Google nelle scuole»**: l'autorità ha ordinato ai **53 comuni**
    di adeguarsi, non ha sanzionato Google.
22. **Non dire che la Germania ha vietato Google/Microsoft nelle scuole**: il procedimento OVG NRW era
    **cautelare** e si è chiuso con una **transazione**.
23. **Citare l'esito olandese anche se ci contraddice**: nei Paesi Bassi si è arrivati a un **adeguamento**,
    non a un divieto. È il contro-argomento più forte di Google e va anticipato.
24. **Non dire che l'EUCS «sta per essere adottato»**: al giugno 2026 la Commissione stessa scrive che
    «*non è ancora stato adottato*». Zero certificati emessi.


### Trappole 25-31 — dai dossier europei *(consolidate qui il 29/07/2026: erano finite dentro le voci dei
reperti A37 e A39, dove chi consulta il registro non le avrebbe trovate)*

25. 🚨 **LA PIÙ PERICOLOSA — non dire «la Danimarca ha abbandonato Microsoft».** È falso e verificabile in
    cinque minuti. Il ministero smentì i titoli internazionali **cinque giorni dopo**; il pilota è di
    **38 dipendenti**; e nelle stesse settimane lo Stato danese ha firmato **il più grande rinnovo
    Microsoft della sua storia** (4,2 mld DKK contro 80 mln per la sovranità: **rapporto 100 a 1**).
    **Copenaghen** non ha deciso di abbandonare Microsoft: ha deliberato **un'analisi**.
    ⚖️ Ma il pilota **prosegue**: non è una marcia indietro, è una migrazione faticosa. Dirlo così.
    Il caso danese **solido** è **Aarhus** (60 sistemi da Azure a Hetzner, concluso, ripagato in 4 mesi).
26. **Schleswig-Holstein NON è passata a Linux.** L'80% riguarda **LibreOffice**; il sistema operativo è
    ancora in fase pilota. La stampa lo confonde sistematicamente.
27. **I numeri di Schleswig-Holstein non sono sinonimi**: 25.000 / 30.000 / 60.000 circolano come se lo
    fossero, ma **i 60.000 sono *dipendenti***, non postazioni migrate.
28. **L'art. 9 EMBAG svizzero obbliga a *pubblicare* il codice sviluppato dall'amministrazione, NON a
    *usare* open source.** È l'errore più diffuso sul caso svizzero.
29. **Clarence e S3NS girano su Google Distributed Cloud Hosted**; Proximus vende anche Azure Local.
    Il comunicato del Governo lussemburghese **non nomina mai Google**.
30. **openDesk: 100.000 vs 80.000 postazioni** dalla stessa fonte nello stesso periodo — e il ministero che
    lo commissiona **lo testa su 80 postazioni**. Non citare cifre senza qualificarle.
31. **Non raccontare solo i successi.** Su 24 casi censiti nell'area nordica **solo cinque sono migrazioni
    concluse e verificate su fonte primaria**; la Germania federale ha speso **481,4 mln €** in licenze
    Microsoft nel 2025 (**+75,6% in due anni**) e la Svizzera ha **completato** il rollout di M365 su
    54.000 postazioni **mentre l'EMBAG era in vigore**. Chi migra e chi acquista sono **lo stesso Stato**.
    ⚠️ Vale anche il simmetrico: **non raccontare solo i fallimenti**. Monaco è tornata all'open source
    nel maggio 2026, e il 68,6% dei dipendenti era soddisfatto del *software* (solo il 32%
    dell'*organizzazione*).

32. **I 300 miliardi di EuroStack sono una *richiesta*, non uno stanziamento.** Citarli come fondi
    disponibili è falso.
33. 🚨 **DIVIETO ASSOLUTO del confronto capitalizzazione di borsa contro PIL.** È un errore di categoria
    (stock contro flusso) e qualunque economista lo smonta in diretta, portandosi via la credibilità del
    resto. Vale anche per fatturato contro PIL (lordo contro valore aggiunto).
    ✅ L'unico confronto difendibile è **spesa annua contro spesa annua** (v. A48).

34. **Non dire «Airbus ha abbandonato AWS».** Il comunicato ufficiale non nomina AWS; Jestin dichiara
    esplicitamente di **non** voler lasciare tutte le soluzioni non europee, ma di scegliere **per criticità
    del dato**. E le applicazioni sono **~70 entro il 2028**, non 900. Dettagli in A47.

35. 🚨 **Non dire «i servizi del PSN sono operati da Microsoft, Google e Amazon».** È falso per il
    livello *Public Cloud PSN Managed*, dove la pagina ufficiale dichiara gestione da **personale PSN** e
    **controllo della Root Key**. Distinguere i tre livelli e attaccare **la parola «sovranità»**, non
    l'architettura. Dettagli e formulazione corretta in **A50**.

36. **Non citare i due «giurisdizione» della Convenzione PSN come se riguardassero i dati.** Riguardano
    il **contenzioso** sul concessionario. Usarli sarebbe scorretto e verificabile in un minuto (A51).
37. **Non dire che il PSN «non ha il confidential computing».** Ciò che possiamo dire è che **il manuale
    utente del Secure Public Cloud Azure non lo documenta in 64 pagine**, mentre il sito lo qualifica da
    sé con «ove attivato». La differenza fra le due frasi è tutta (A51).
38. **Riconoscere il BYOK prima di criticarlo.** Le chiavi sono su HSM Thales on-premises, fuori dal CSP:
    è reale. Il limite — che l'**uso** delle chiavi passa per Managed Identity e Disk Encryption Set di
    Azure — va detto come **punto tecnico**, non come smascheramento (A51, e vale A22).

39. **Non attribuire all'ANSSI parole che non ha usato.** Zero occorrenze di *sovereign*, *state actor*,
    *extraterritorial*, *jurisdiction*, *legal* nelle 13 pagine. Dire: «la conclusione politica è nostra,
    le premesse tecniche sono dell'ANSSI» (A52).
40. **Non citare il BSI sul confidential computing.** Una sua posizione in merito **non è stata trovata**
    — il che è diverso dal dire che non esista. Rimosso dalla pagina per decisione del committente (A52).

41. 🚨 **Non dire «i cloud francesi sono sovrani, quelli italiani no».** Bleu è Microsoft e S3NS è
    Google: si viene smontati con due nomi. La formulazione corretta è che **la Francia ha scritto un
    requisito misurabile e l'Italia non ne ha scritto alcuno** — ed è più forte, perché Bleu e S3NS
    diventano **la prova che la regola funziona** (A53).

42. 🚨 **Non trattare «PSN Managed» come una cosa sola.** Sono **due architetture**: il lato Google gira
    sulle region di Google (Milano, Torino), il lato Oracle nei data center del PSN. Confonderle ci fa
    sbagliare in entrambe le direzioni (A54).
43. **Non dire «gli aggiornamenti li fa Oracle».** L'operatore gestisce **il patching di base e gli
    aggiornamenti standard**; Oracle produce gli aggiornamenti ed esegue **gli upgrade non standard**.
    La formulazione corretta è quella (A55). ⚠️ Non citare il numero dei servizi Alloy: Oracle stessa dice
    «più di 200» nella documentazione e «più di 100» nella pagina prodotto.
44. ⚠️ **L'assenza di qualificazione ANSSI non prova che una soluzione sia inadeguata.** Prova che **non è
    mai stata misurata con quel metro** — ed è più difendibile. Vale anche il simmetrico: **non abbiamo
    trovato** analisi ANSSI su Alloy, il che non significa che non esistano (A55, regola 10).

45. **Non presentare la società di comodo di AWS come uno scandalo.** Usare una GmbH già registrata e il
    capitale minimo è **prassi ordinaria in Germania**. Il punto è **la distanza fra la prassi e il
    linguaggio dell'annuncio**, non la prassi (A56).
46. ✅ **SCIOLTA il 05/08/2026 — la percentuale ora si può scrivere, ed è documentata.** L'**elenco notarile
    dei soci** (HRB 40853 P, autenticato a Monaco il 20.10.2025) registra un **socio unico**:
    **A100 ROW, Inc., Wilmington, Delaware** — State File no. 4517940 — 25.000 quote da 1,00 €,
    **«Summe der Beteiligung in %: 100»**. PDF archiviato in `fonti/registro-imprese/` — sha256 `69c7ef33bcad3264…`.
    ⚠️ **Ma la catena si ferma lì**: chi possieda A100 ROW **non è provabile allo stesso modo**, perché il
    **Delaware non pubblica le informazioni sui soci**. Fonti secondarie convergono su Amazon.com, Inc.:
    **si riporta come tale, non come prova**. ✅ E il punto non ne dipende: la capogruppo è già, su prova
    primaria, **interamente posseduta fuori dall'Unione**.
47. **Non dire che Nitro Enclaves è inutile o mal fatto.** È buona ingegneria: protegge dall'istanza padre,
    cioè dal cliente stesso. Si dice **dove AWS traccia il confine**, non che il confine sia finto (A56).

48. 🚨 **ERRORE GIURIDICO CORRETTO — il Golden Power.** Avevamo scritto che il contratto «sa scrivere
    una clausola di controllo societario e la applica al concessionario italiano, **mai al fornitore**».
    Implica che l'Italia **avrebbe potuto** applicarlo a Microsoft o AWS: **non poteva**, il Golden Power
    raggiunge per legge solo entità di diritto italiano. Qualunque amministrativista lo smonta in una
    battuta. ✅ **Formulazione corretta**: il Golden Power è stato usato dove poteva arrivare; lo strumento
    che raggiunge il fornitore **non è il Golden Power, è il requisito di gara** — ed è esattamente quello
    che la Francia ha scritto e l'Italia no. *(Rilievo esterno, accolto e corretto il 03/08/2026.)*
49. 🚨 **NON dire «nel manuale la sovranità è DEFINITA come un backup mensile».** Il verbatim sta nella
    sezione sul **servizio di backup** e dice che *uno dei due requisiti di quel servizio* è «legato alla
    sovranità del dato». Chi obiettasse «quella è la frequenza di RPO di un backup» **avrebbe ragione sul
    meccanismo**. ✅ **Formulazione corretta**: il manuale **attacca l'etichetta formale «sovranità del
    dato» a una misura di copia periodica fuori sito** — è uno **svuotamento semantico**, ed è l'unico
    punto in cui il termine viene legato a qualcosa di concreto. Più difendibile, e dice la stessa cosa.
50. **Il solo argomento terminologico sulle «zero occorrenze» è debole**: un contratto pubblico italiano non
    cita il CLOUD Act per nome. ✅ Va accompagnato dalla **scansione delle clausole sostanziali**, eseguita
    il 03/08/2026 sugli stessi quattro documenti: `art. 48` **0** · `autorità giurisdizionale` **0** ·
    `ordine di un paese terzo` **0** · `trasferimenti internazionali` **0** · `rogatoria` **0** ·
    `assistenza giudiziaria` **0** · `autorità estere` **0** · `extra-europee` **0**.
    ⚠️ Le due occorrenze di «richiesta di accesso» riguardano lo **Zero Trust sulle identità**: citarne il
    conteggio senza leggere il contesto sarebbe stato un errore.
51. 🚨 **NON dire che Bleu e S3NS sono «entità 100% europee».** SecNumCloud §19.6 fissa il tetto alla
    quota extra-UE al **24%**, non a zero: sono a **controllo** europeo, non al 100% europee. E **Bleu non
    è qualificata**: risulta *in istruttoria*. Presentarla come sovranità realizzata ripete l'errore già
    vietato per la Danimarca e per l'EUCS. *(Rilievo esterno **respinto** il 03/08/2026.)*
52. 🚨 **NON usare una colonna «soggetto a CLOUD Act / FISA 702»** in nessuna tabella. Il DOJ lo qualifica
    come accertamento **caso per caso** e non esiste giurisprudenza nota (vale A22). ✅ La colonna corretta
    è **«esposizione dichiarata o non esclusa»**, con l'appiglio che regge: il verbatim di Hadinger sotto
    giuramento e l'assenza di qualunque esclusione contrattuale. *(Rilievo esterno **respinto**.)*
53. ⚠️ **NON affermare che una National Security Letter possa obbligare a veicolare aggiornamenti firmware
    o dump della memoria.** È verosimile ma **non documentato** e non abbiamo la fonte. Ciò che abbiamo è
    più forte perché lo scrive l'auditor: nessuna garanzia su modifiche tecniche «scelte o **imposte**».

54. 🚨 **ERRORE TECNICO CORRETTO — la crittografia omomorfica.** Avevamo scritto: «non esiste una
    scorciatoia: **una CPU non può sommare due numeri cifrati senza prima decifrarli**». È **falso come
    proposizione universale**: crittografia omomorfica, calcolo multiparte sicuro e *privacy-preserving
    computation* fanno esattamente quello. Un crittografo lo vede alla prima lettura, e il costo non è la
    frase ma **la credibilità dell'intera pagina**. ✅ Formulazione corretta: **nei workload cloud ordinari**
    il dato dev'essere in chiaro dentro un contesto di esecuzione; le tecniche su dati cifrati esistono ma
    hanno maturità diverse e **non sono la base delle architetture qui descritte**.
    *(Rilievo esterno accolto il 03/08/2026.)*
55. 🚨 **Nitro System e Nitro Enclaves non sono la stessa cosa.** *Enclaves* isola l'enclave
    dall'**istanza padre** (ambiente del cliente); il *sistema Nitro* è l'architettura di piattaforma, ed è
    l'oggetto della dichiarazione «nessuno, inclusi i dipendenti AWS». **Rispondere a un'affermazione sul
    sistema con la documentazione delle enclave è un errore di categoria.** La risposta buona alla
    dichiarazione sul sistema è **l'audit NCC**, che ce l'abbiamo (A21).
56. **Non titolare «il meccanismo di verifica è stato rotto».** Il reperto riguarda **un modo diffuso di
    legare l'attestazione a un canale TLS**, non l'attestazione in generale. Il corpo del testo lo diceva
    già correttamente: **era il titolo a sovraestendere**, e i titoli sono ciò che resta.
57. **Non scrivere «società di comodo».** Si scrive **«veicolo societario preesistente»**. Per un giudizio
    più forte servirebbero statuto, patti parasociali, diritti di veto e composizione del consiglio —
    **nulla di ciò è stato letto** (estende la trappola 45).
58. 🎯 **Le qualificazioni si attaccano alle OFFERTE, non alle aziende.** Dire «Microsoft 0 nel catalogo»
    invita l'inferenza sbagliata: **Bleu, tecnologia Microsoft, è in istruttoria**, e **S3NS, tecnologia
    Google, è qualificata**. ✅ Lettura corretta: **nessuna offerta usata dal programma italiano possiede
    quella qualificazione, e nessuna è in istruttoria** — non che quelle tecnologie non possano sostenerne
    una. I casi francesi dimostrano il contrario.
59. **Il *gag order* è possibile, non automatico.** Va scritto «dove viene emesso, e non ogni ordine ne
    porta uno». La nostra tesi regge lo stesso ed è più difendibile.
60. ⚠️ **Non dire «l'Italia non si è mai posta il problema».** I documenti di **strategia cloud nazionale**
    — che **non abbiamo letto** — risultano riconoscere il rischio extra-UE, e l'Italia è **coautrice dei
    criteri europei di immunità nel 2021** (A15). ✅ La distinzione corretta, che regge: **riconoscere un
    rischio in una strategia non è tradurlo in requisiti vincolanti, criteri di esclusione, clausole
    contrattuali e conseguenze**. Il nostro reperto è **limitato al corpus contrattuale**.
61. **Non dichiarare che «tutte le citazioni sono da fonti primarie»** se si cita una testata. ✅ Formula:
    *sono state privilegiate fonti primarie; le fonti giornalistiche sono usate per contesto o come strada
    verso il documento originale*, mai come prova.
62. ⚠️ **Non sostenere che un ordine giuridico superi «sempre» qualunque misura tecnica.** Un ordine non
    rompe la crittografia né crea capacità che il destinatario non ha. ✅ Ciò che regge: le misure tecniche
    **riducono ciò che il fornitore detiene**, ma non eliminano obblighi di **assistenza prospettica**,
    accesso ai **metadati**, controllo del **software** e **disponibilità** del servizio. E nel caso che ci
    interessa è l'ANSSI a dire che quelle misure non soddisfano il §19.6.

### ⚠️ Nota d'uso — collisione di scale
La scala **SEAL 1-4** della gara UE **non è** la nostra scala **0-4**: una misura i *fornitori*, l'altra i
*modelli*. Non sovrapporle mai nel racconto.