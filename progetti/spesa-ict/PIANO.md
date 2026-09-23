# Spesa ICT della PA italiana — piano di lavoro

**Stato:** proposta, in discussione · **Ultimo aggiornamento:** 2026-09-23

## 1. Obiettivo finale

Misurare **quanta parte della spesa ICT della PA italiana è orientata alla sovranità**
secondo i criteri MxMap, cioè la classificazione a quattro categorie per giurisdizione
del fornitore: `it`, `eu_non_it`, `extra_eu`, `unknown`.

È lo stesso indicatore che l'Osservatorio già pubblica sulla posta elettronica, applicato
a un secondo asse: il denaro. La domanda a cui rispondere è "verso quale giurisdizione va
l'euro speso in digitale dalla PA", non "quanto spende la PA in digitale".

## 2. Il confine

Regola unica per decidere se una fonte, un dataset o una lavorazione entra nel perimetro:

> **Serve a dire se un euro di spesa ICT è sovrano o no?**
> Se sì, dentro. Se no, fuori — anche quando è interessante.

### Dentro

**Anello 1 — la misura del denaro**

| Fonte | Perché serve |
|---|---|
| ANAC, dataset tabellari BDNCP (`cig`, `aggiudicazioni`, `aggiudicatari`, `partecipanti`, `subappalti`, `quadro-economico`, `stati-avanzamento`) | È la spina dorsale. `stati-avanzamento` e `quadro-economico` sono l'unico proxy pubblico del liquidato |
| Consip, `gare-asp` e `bandi-e-gare` | Gli unici dataset Consip record-level **con il CIG**, quindi agganciabili ad ANAC |
| Consip, ordini MePA e convenzioni (aggregati) | Il canale centralizzato vale una quota molto alta dell'ICT, soprattutto hardware e software |
| SIOPE via BDAP, voci ICT del piano dei conti | L'unica misura di **cassa** effettiva, ente per ente |
| PA Digitale 2026 (`teamdigitale/padigitale2026-opendata`) | Finanziamenti ICT-PNRR per singolo ente, con CUP, aggiornati ogni giorno |
| ACN, catalogo dei servizi cloud qualificati | Chi sono i fornitori cloud ammessi e con quale livello di qualificazione |
| IndicePA (CKAN) | Anagrafe degli enti, chiave di aggancio, più i responsabili della transizione al digitale |

**Anello 2 — l'attribuzione di sovranità (il nostro pezzo)**

- **Registro fornitore → gruppo → giurisdizione.** Non esiste in nessun progetto aperto
  italiano. È il contributo differenziale dell'Osservatorio e va pubblicato in CC BY-SA come
  dataset autonomo, riutilizzabile anche da terzi.
- **Perimetro ICT documentato.** Quali CPV, con le esclusioni motivate: la divisione 30 va
  ripulita da buoni pasto e cancelleria, i server stanno nella divisione 48 nonostante siano
  hardware, le licenze non hanno un CPV proprio.

**Anello 3 — contesto, solo come join opzionale**

TED, EU Financial Transparency System, OpenCUP e OpenCoesione servono a marcare la fonte di
finanziamento e a fare confronti europei. Non entrano nella misura principale.

### Fuori

- **Tutta la spesa non ICT.** Bilanci, sanità, pensioni, opere pubbliche: è il perimetro di
  DoveVannoINostriSoldi e di DataCivicLab, non il nostro.
- **I 23 portali regionali di e-procurement.** Dal 1° gennaio 2024 le piattaforme certificate
  devono comunicare ad ANAC (`comunicaAppalto`, `pubblicaAvviso`, `comunicaPostPubblicazione`):
  la sostanza dei contratti è già in ANAC. Il loro valore aggiunto sono i documenti e la
  tempestività, non contratti diversi.
- **I documenti di gara in massa.** Irreperibili: circa 0% sul perimetro ANAC. Li useremo solo
  come **campione**, dove esistono (SATER/Emilia-Romagna è di fatto l'unico portale che li espone).
- **Un aggregatore generalista della spesa pubblica.** Esiste già due volte: Cruscotto Italia di
  AgID (AGPL) e DataCivicLab (MIT, dati derivati in Parquet su bucket pubblico). Non ne serve un terzo.
- **La normalizzazione di tutto in un unico schema.** Competenza, cassa, aggiudicato, ordinato e
  consolidato non sono sommabili: un numero unico di "spesa pubblica" sarebbe un numero falso.

### Regola di stop

Quando una lavorazione non cambia la risposta sovrano/non sovrano, si ferma. Vale in particolare
per la ricostruzione del liquidato contratto per contratto, che con i dati pubblici oggi non si
chiude: la catena impegno → contratto → pagamento non ha un ponte tra il mondo RGS e il mondo appalti.

## 3. Cosa si può dire, e cosa no

Il dato pubblico **non consente** di affermare "il X% della tecnologia della PA è estera".
Due limiti strutturali, entrambi verificati:

1. **ANAC registra chi firma il contratto, non di chi è la tecnologia.** L'aggiudicatario è quasi
   sempre una società italiana anche quando rivende prodotto estero.
2. **Il divieto di citare marchi nelle specifiche tecniche** (art. 79 e Allegato II.5 del
   d.lgs. 36/2023) sopprime deliberatamente il segnale, e l'oggetto del bando è comunque troppo
   corto per contenerlo.

Quello che si può pubblicare in modo difendibile è un **pavimento misurato**: la cattura estera
diretta più le menzioni esplicite dove il prodotto è nominato, con la dichiarazione aperta che la
dipendenza reale è più alta e che il dato pubblico ne struttura la maschera. È una posizione più
solida di una percentuale finta-precisa, e coerente con la nostra metodologia sulla posta.

## 4. Il byproduct necessario: monitoraggio della qualità dei dati aperti

Serve a noi come guardiano della pipeline e vale come prodotto pubblico autonomo di advocacy:
misurare chi pubblica bene è una leva di cambiamento, ed è coerente con un osservatorio orientato
al cambiamento e non alla sola osservazione.

### Cosa misura

| Dimensione | Esempi di metrica |
|---|---|
| **Disponibilità** | stato HTTP di ogni risorsa dichiarata, tempo di risposta, blocchi WAF |
| **Freschezza** | scarto tra periodo di riferimento e data di pubblicazione; rispetto della cadenza dichiarata |
| **Continuità** | mesi mancanti nella serie |
| **Persistenza** | da quanto una risorsa è in linea e se le vecchie spariscono |
| **Stabilità** | cambi di URL, di schema, di colonne, di codifica |
| **Conformità** | licenza dichiarata e leggibile da macchina, DCAT-AP_IT, checksum, API documentata |
| **Qualità del contenuto** | riempimento dei campi chiave, validità (codici fiscali con checksum, date fuori range, importi negativi o anomali), unicità delle chiavi, integrità tra dataset collegati |
| **Agganciabilità** | tasso di join effettivo su CIG, CUP, codice fiscale ente, codice IPA |

### Cosa produce

1. **Una pagella per ogni produttore** — ANAC, Consip, RGS, DPCoe, AgID/DTD, ACN, IndicePA,
   ISTAT — con storico, andamento e una segnalazione formale allegata.
2. **Una dashboard nazionale pubblica** sullo stato dei dati aperti italiani della spesa, con un
   indice sintetico e il dettaglio per dataset.
3. **Un registro delle anomalie** con evidenza riproducibile, ciascuna con data, query e risultato:
   il reperto, non l'opinione.
4. Tutto in CC BY-SA, leggibile da macchina, con un feed.

### Anomalie già documentate (2026-09-23)

- **ANAC**: il feed OCDS bulk è fermo a **marzo 2026** (aprile, maggio e giugno rispondono 404),
  mentre i dataset tabellari sono aggiornati al 2 settembre 2026.
- **ANAC**: i dataset delta (`cig`, `smartcig`, `aggiudicazioni`) conservano **solo gli ultimi sei
  aggiornamenti mensili**; il file annuale `cig-2026` non esiste ancora. Tutto il 2026 vive quindi
  solo nei delta, e chi non archivia ogni mese ha un buco fino a gennaio 2027. La conservazione non
  è documentata da nessuna parte: si deduce solo elencando le risorse via API.
- **ANAC**: l'API REST OCDS è dichiarata sul portale ma tutti gli endpoint rispondono 404, e il file
  `swagger.json` non è JSON valido. L'API CKAN invece funziona, ma non è documentata e richiede uno
  user-agent da browser perché il WAF blocca gli altri.
- **Consip**: finestra mobile di tre anni. `ordini-mepa-2022.csv` e `ordini-mepa-2023.csv` rispondono
  404, il 2024-2026 risponde 200. Nessuna politica di conservazione pubblicata.
- **soldipubblici.gov.it**: dismesso, reindirizza alla pagina di manutenzione AgID.
- **Portale MIT / HUB Contratti Pubblici**: bandi ed esiti congelati al 31 dicembre 2023.
- **opentender.eu**: la piattaforma gira, ma il dato italiano è fermo a **marzo 2024**.

### Vincolo tecnico da tenere presente

**ANAC blocca gli IP cloud.** Chi ci riesce usa runner non-cloud o proxy. Il monitor va fatto girare
sul nostro server, non su GitHub Actions.

## 5. Sequenza

| Fase | Contenuto | Esito pubblicabile |
|---|---|---|
| **0. Archiviazione** | Registro fonti con hash e data, scarico mensile di ciò che scade: delta ANAC, annualità Consip | Nessuno, ma ogni mese di ritardo è dato perso per sempre |
| **1. Monitor** | Sonde, metriche, pagelle, dashboard nazionale | Il byproduct: dashboard e prima tornata di pagelle ai produttori |
| **2. Attribuzione** | Perimetro ICT documentato e registro fornitore → gruppo → giurisdizione | Il dataset aperto che oggi non esiste |
| **3. Report** | Spesa ICT per giurisdizione, con il pavimento dichiarato | Il report sulla sovranità della spesa |

La fase 0 parte per prima perché è l'unica con una scadenza imposta da altri.

## 6. Rapporti con gli altri progetti

- **DoveVannoINostriSoldi** (AGPL, dati CC BY-SA): il più vicino a noi per metodo e licenza. Ha già
  il registro sorgenti con hash e l'indice nazionale degli operatori. Interlocutore naturale per il
  registro fornitori.
- **DataCivicLab** (MIT) e **Cruscotto Italia** (AgID, AGPL): presidiano il livello di acquisizione.
  Da riusare, non da duplicare.
- **onData / aborruso**: strumenti puntuali già pronti, tra cui l'unico al mondo che attacca la
  Piattaforma di Pubblicità a Valore Legale.
- **AppaltIntel / Proteggimi** e **Atoka PA / SpazioDati**: commerciali. Nessuna condivisione di
  metodo o di lavorazioni.

## 7. Decisioni aperte

1. Il registro fornitore → giurisdizione: dataset autonomo dell'Osservatorio o contributo dentro
   DoveVannoINostriSoldi?
2. Dove gira il monitor: server esistente o macchina dedicata?
3. La dashboard nazionale sta dentro osservatorio.mxmap.it o su un sottodominio proprio?
4. Accesso civico ad AgID per il censimento del patrimonio ICT, che è per singolo ente, include voci
   di costo e licenze software, ed è l'unico dato rilevante non pubblicato.
