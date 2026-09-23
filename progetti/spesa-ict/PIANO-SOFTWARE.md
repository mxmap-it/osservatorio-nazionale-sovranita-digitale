# Piano software — cosa riusiamo, cosa costruiamo

**Stato:** proposta, in discussione · **Verifiche:** 2026-09-23 · Vedi [PIANO.md](PIANO.md) e [CENSIMENTO-FONTI.md](CENSIMENTO-FONTI.md)

## 1. Il principio

Riusiamo tutto ciò che è **libreria o servizio invocabile**. Non riusiamo ciò che è
**applicazione**: un'applicazione altrui si adotta intera o non si adotta, e adottarla intera
significa ereditare il suo perimetro, che non è il nostro.

Sulle licenze la posizione del progetto è che **va bene qualunque licenza libera**: rilasciamo
tutto comunque, quindi il copyleft non è un ostacolo e possiamo riusare anche AGPL. Restano però
tre vincoli che non dipendono dalle nostre preferenze:

1. **"Nessuna licenza" non vuol dire libero.** Un repo senza licenza dichiarata è di fatto tutti
   i diritti riservati e non è riusabile, per quanto sembri aperto.
2. **Alcune licenze non sono libere**, e restano fuori a prescindere: la Elastic License, che
   vieta di offrire il software come servizio gestito, e le clausole non commerciali come il
   CC BY-NC.
3. **I contributi verso l'esterno seguono la licenza del repo che li ospita.** Se vogliamo che il
   nostro livello di qualità finisca dentro `source-observatory`, quel codice deve essere MIT.
   È l'unico vincolo che ci obbliga a tenere separate due parti del nostro lavoro (§5).

I nostri dati escono in **CC BY-SA 4.0** in ogni caso.

## 2. Matrice di riuso

Tutte le licenze e le date di attività sono verificate il 2026-09-23.

### Da riusare

| Serve per | Software | Licenza | Come lo usiamo |
|---|---|---|---|
| Motore di pipeline dati | **`dataciviclab/toolkit`** | MIT | Come **libreria**. `dataset.yml` + SQL, esecuzione RAW → CLEAN → MART su DuckDB, output Parquet, `metadata.json` e `validation.json` a ogni run. Ha già i plugin sorgente `http_file`, `ckan`, `sdmx`, `sparql`. Ci evita di scrivere un ETL nostro |
| Radar disponibilità delle fonti | **`dataciviclab/source-observatory`** | MIT | Già monitora 36 cataloghi con check giornaliero, inventario settimanale e `readiness_score`. **ANAC e Consip sono già dentro.** Lo usiamo come livello di base e contribuiamo upstream le fonti mancanti |
| Validazione metadati DCAT | **`ISAITB/shacl-validator`** | EUPL-1.2 | Servizio Docker con REST API, self-hostabile. Shapes canoniche da `SEMICeu/DCAT-AP` (CC BY 4.0, release 3.0.1) |
| Qualità del contenuto tabellare | **`frictionless-py`** | MIT | Libreria pura: schema, tipi, valori nulli, unicità. Il grosso delle nostre metriche di contenuto |
| Qualità avanzata, integrità referenziale | **Great Expectations** | Apache-2.0 | Solo se frictionless non basta. Nota: il repo è ora sotto `fivetran/` |
| Scarico Pubblicità a Valore Legale ANAC | **`aborruso/anac-pl-pp-cli`** | Apache-2.0 | Binario Go invocabile. È l'unico strumento al mondo su quella fonte |
| Scoperta BDAP e IndicePA | **`aborruso/openbdap-pp-cli`**, **`openipa`** | Apache-2.0 | Per la scoperta; l'ingestione resta in toolkit |
| Manipolazione OCDS | **`ocdskit`** | BSD-3 | Priorità bassa finché l'OCDS di ANAC resta fermo |
| Convenzione di provenienza | **source-spec di DoveVannoINostriSoldi** | — | Riusiamo la **convenzione** (hash, byte, data di acquisizione, limiti dichiarati), non il codice. Un formato di metadati si può adottare senza vincoli di licenza |
| Anagrafe imprese e LEI | **GLEIF golden copy** | CC0 | Bulk giornaliero, nessuna registrazione |
| Motore di entity resolution | **`opensanctions/nomenklatura`** | MIT | Libreria agnostica rispetto alla fonte, si usa sui nostri dati. Il *dataset* OpenSanctions è invece CC BY-NC e non ci serve |
| Pubblicazione | **Sito Hugo dell'Osservatorio** | — | Consuma già `kpi.json`: stesso schema per la dashboard qualità |
| **Moduli di ingestione già scritti** | **`AgID/cruscotto-italia`**, `etl/sources/` | AGPL-3.0 | Un modulo per fonte, già pronti su quelle che ci servono: `siope.py` (34 KB), `pnrr_progetti.py` (20 KB), `bdap.py` (18 KB), `anac.py` (13 KB). Da leggere e, dove conviene, sollevare di peso: è codice pubblico di un'amministrazione, scritto sulle stesse fonti |
| Ingestione ANAC tabellare e ledger sorgenti | **DoveVannoINostriSoldi**, `scripts/etl/` | AGPL-3.0 | Stessa logica: gli script ANAC e le loro spec sorgente sono la cosa più vicina a quello che ci serve |

### Da non riusare, e perché

| Software | Licenza | Perché no |
|---|---|---|
| **`cardinal-rs`** (OCP) | MIT | Misura red flag corruttivi, non sovranità. Fuori perimetro, non fuori qualità |
| **Backend gare PA di P. Biase** | CC BY-NC-SA | La clausola non commerciale non è software libero, e il metodo di classificazione si retro-alimenta |
| **`soda-core`** | Elastic License 2.0 | Non è open source secondo OSI e vieta l'offerta come servizio gestito |
| **piveau / MQA di data.europa.eu** | Apache-2.0 | Il codice vivo è su GitLab, non su GitHub, ed è uno stack a microservizi che ha senso solo se gestisci un portale. Riusiamo la *metodologia* (405 punti su cinque dimensioni), non il software |
| **`piersoft/mqa-monitor`**, **`SEMICeu/semic-shacl-validator`** | nessuna | Sembrano aperti ma non dichiarano licenza: tutti i diritti riservati. Da contattare, semmai, chiedendo di aggiungerne una |
| **Open Data Certificate**, **OpenDataMonitor** | MIT / — | Morti: 2021 e dominio spento |

## 3. Cosa costruiamo noi

Quattro pezzi, tutti assenti in ciò che esiste.

**1. Il livello di qualità che manca al radar.** `source-observatory` misura la salute della
*fonte*: la sua stessa documentazione dice che lo stato radar descrive la salute della fonte,
non l'aggiornamento del dataset. Manca tutto il resto, cioè quello che serve a noi:

- **continuità temporale** — quali mesi mancano davvero nella serie;
- **persistenza** — quali risorse spariscono, che è il caso di Consip e dei delta ANAC;
- **qualità del contenuto** — riempimento dei campi, codici fiscali con checksum valido, date
  impossibili, importi negativi o anomali, unicità delle chiavi;
- **agganciabilità** — il tasso di join reale su CIG, CUP, codice fiscale ente, codice IPA;
- **pagelle per produttore** — l'artefatto di advocacy, che nessuno produce.

**2. L'archivio delle risorse deperibili.** Nessuno lo fa e ogni mese si perde qualcosa.

**3. Il perimetro ICT documentato.** Una tabella di CPV con esclusioni motivate e i test che
la verificano. Poco codice, molta metodologia.

**4. Il registro fornitore → gruppo → giurisdizione**, con una scala di ambizione realistica
(sezione seguente).

## 4. Il registro fornitori: quanto è realistico

La verifica sulle fonti aperte di proprietà societaria dà un esito netto e va accettato:

- **GLEIF** (CC0, bulk giornaliero) contiene circa 259.000 entità italiane, ma le relazioni di
  controllo dichiarate sono poche: circa **6.800 entità italiane con capogruppo diretta** e
  **7.150 con capogruppo ultima**, di cui l'82,9% con capogruppo a sua volta italiana. Restano
  **circa 1.200 imprese italiane con controllante estero verificabile**, cioè lo 0,03% delle
  imprese italiane. Oltre sei milioni di record sono "reporting exception", cioè entità che
  dichiarano di non avere un parent identificato.
- **Buona notizia sul join**: il 96,4% dei LEI italiani ha il campo `registeredAs` popolato e il
  90,5% in formato codice fiscale a 11 cifre. **La chiave partita IVA → LEI funziona.**
- Tutto il resto è chiuso: il Registro Imprese non pubblica la catena di controllo, BRIS consente
  solo ricerche umane una società per volta, il registro dei titolari effettivi richiede interesse
  legittimo e pagamento, OpenCorporates ha il bulk commerciale, il Public CbCR parte solo a fine
  2026 e senza database centrale. Con copertura ampia c'è solo ORBIS di Moody's, commerciale.

**Conseguenza di progetto: il registro non può essere esaustivo, e non deve provarci.**
Si costruisce **per valore, non per numerosità**: i primi qualche centinaio di fornitori coprono
la gran parte del valore ICT aggiudicato. Per ciascuno una riga curata a mano, con la fonte
dell'attribuzione e la data, più l'arricchimento automatico da GLEIF dove esiste. Una copertura
dichiarata come "l'85% del valore, il 3% dei fornitori" è un risultato solido; una copertura
finta del 100% sarebbe l'errore che abbiamo criticato negli altri.

## 5. Un progetto software o più d'uno?

**Uno solo di codice, più un repository di dati.**

L'archivio e il monitor **sono la stessa macchina**: scarica, verifica l'hash, conserva, misura.
Non si può misurare la freschezza senza scaricare, né la persistenza senza avere lo storico.
Separarli significherebbe scrivere due volte il livello di acquisizione. Vanno quindi insieme.

Il registro fornitori è invece un'altra cosa: ha cadenza diversa, è curato a mano, il suo valore
è il **dato** e non il codice, e va citato e versionato come dataset autonomo. Sta in un repo suo.

La pubblicazione non richiede un terzo progetto: il sito Hugo dell'Osservatorio consuma già un
JSON di KPI, e la dashboard qualità segue lo stesso schema.

```
osservatorio-dati-spesa                        archivio + monitor qualità + perimetro ICT
  pacchetto acquisizione   (AGPL-3.0)          può sollevare i moduli di AgID e DVINS
  pacchetto qualità        (MIT)               libreria pura, contribuibile a monte
registro-fornitori-sovranita     (CC BY-SA)    dataset curato + arricchimento GLEIF
osservatorio-...-sovranita-digitale            pubblicazione: dashboard e report
```

La divisione in due pacchetti dentro lo stesso repo non è formalismo: se il pacchetto qualità
importasse quello di acquisizione, diventerebbe AGPL insieme a lui e non potrebbe più essere
contribuito a `source-observatory`, che è MIT. Va quindi scritto come **libreria pura che lavora
su file e tabelle**, senza dipendere dal livello che li ha scaricati. È una buona architettura
anche a prescindere dalla licenza.

Più tre contributi verso l'esterno, che valgono più di un quarto repo nostro:

1. le fonti mancanti nel registry di `source-observatory`;
2. le shapes **DCAT-AP_IT**, che oggi non esistono in alcuna forma ufficiale riusabile — sarebbe
   un contributo al paese, non solo a noi;
3. il registro fornitori offerto a DoveVannoINostriSoldi, che ha già l'indice nazionale degli
   operatori su cui applicarlo.

## 6. Vincoli operativi

- **ANAC blocca gli IP cloud**, e il WAF respinge gli user-agent non-browser. Il monitor gira sul
  nostro server, non su GitHub Actions. È il vincolo che ha determinato le scelte di tutti gli
  altri progetti, non solo le nostre.
- L'API CKAN di ANAC funziona ma **non è documentata**: i dataset vanno scoperti via API, mai
  indovinando gli URL.
- I file OCDS mensili superano i 3 GB: l'elaborazione va fatta in streaming, non in memoria.

## 7. Ordine di lavoro

| # | Cosa | Costruito o riusato | Ordine di grandezza |
|---|---|---|---|
| 1 | Archivio delle risorse deperibili (delta ANAC, annualità Consip) | toolkit + poco nostro | giorni |
| 2 | Metriche di continuità, persistenza, contenuto | nostro, sopra frictionless | settimane |
| 3 | Pagelle per produttore e dashboard nazionale | nostro + Hugo esistente | settimane |
| 4 | Perimetro ICT documentato | nostro, metodologico | giorni |
| 5 | Registro fornitori: top per valore, curato, con GLEIF | nostro + GLEIF + nomenklatura | settimane, poi continuo |
| 6 | Shapes DCAT-AP_IT | nostro, contributo esterno | opzionale |

Il punto 1 va fatto per primo perché è l'unico con una scadenza imposta da altri.

## 8. Decisioni aperte

1. Contribuire le fonti mancanti a `source-observatory` upstream, oppure tenere un registry nostro?
   La prima è più utile a tutti, la seconda è più veloce.
2. Contattare DataCivicLab prima di costruire il livello qualità, per evitare che lo stiano già
   facendo, e semmai costruirlo insieme.
3. Quanto sollevare da `AgID/cruscotto-italia`: i moduli `siope.py`, `bdap.py`, `anac.py` e
   `pnrr_progetti.py` coprono quattro delle nostre fonti e sono già scritti. Vanno letti prima
   di decidere, ma se reggono è lavoro risparmiato.
