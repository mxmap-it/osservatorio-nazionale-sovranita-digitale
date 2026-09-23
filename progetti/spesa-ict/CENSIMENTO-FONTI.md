# Censimento delle fonti sulla spesa pubblica italiana

**Verifiche effettuate il 2026-09-23.** Le righe marcate *verificato* sono state controllate con
una richiesta HTTP reale in quella data. Le altre vengono da documentazione di terzi e vanno
ricontrollate prima dell'uso.

## 1. Appalti e contratti

| Fonte | Cosa misura | Chiavi | Licenza | Note |
|---|---|---|---|---|
| **ANAC — dataset tabellari BDNCP** `dati.anticorruzione.it/opendata` | Base d'asta, aggiudicazioni, aggiudicatari, partecipanti, subappalti, quadro economico, stati di avanzamento | CIG, CUP, CF ente, AUSA | CC BY-SA 4.0 | *verificato.* Aggiornamento mensile il giorno 2. 70 dataset. API CKAN funzionante ma **non documentata**: richiede user-agent da browser |
| **ANAC — OCDS bulk** | Stesso contenuto in Open Contracting Data Standard | ocid, CIG | CC BY 4.0 | *verificato.* **Fermo a marzo 2026.** File mensili molto grandi (gennaio 2025 oltre 3 GB) |
| **ANAC — delta mensili** (`cig`, `smartcig`, `aggiudicazioni`) | Aggiornamenti incrementali dall'ultimo file annuale | CIG | CC BY-SA 4.0 | *verificato.* **Solo gli ultimi sei mesi in linea.** `cig-2026` non esiste: il 2026 vive solo qui |
| **ANAC — smartCIG** | Affidamenti sotto soglia | CIG semplificato | CC BY-SA 4.0 | Copre la parte sotto soglia, esclusa dall'OCDS |
| **ANAC — Pubblicità a Valore Legale** `pubblicitalegale.anticorruzione.it` | Avvisi che fanno fede per legge dal 2024 | CIG | — | La fonte più tempestiva. Categoria merceologica in testo libero, non CPV |
| **ANAC — attestazioni SOA** | Qualificazione delle imprese di lavori | CF impresa | CC BY-SA 4.0 | Sottoutilizzato |
| **Consip** `dati.consip.it` | 16 dataset: ordini MePA e convenzioni, RdO e trattative dirette, cataloghi, operatori economici, `gare-asp` | CIG (solo in `gare-asp` e `bandi-e-gare`), CF PA, codice IPA | CC BY 4.0 | *verificato.* **Finestra mobile di 3 anni**: 2022 e 2023 rispondono 404. Endpoint SPARQL e RDF disponibili |
| **TED — API v3 eForms** `api.ted.europa.eu` | Bandi e aggiudicazioni sopra soglia UE | numero avviso, CPV, CF ente | riuso UE | API anonima senza chiave. **Il CIG non è un campo standard eForms** |
| **Portale MIT / HUB Contratti Pubblici** | Bandi ed esiti del settore infrastrutture | CIG | — | **Congelato al 31 dicembre 2023** |
| **Piattaforma Contratti Pubblici (PCP)** | API di comunicazione ad ANAC | CIG | — | Riservata alle stazioni appaltanti via PDND. Documentazione pubblica su `anticorruzione.github.io` |

## 2. Spesa, bilanci, cassa

| Fonte | Cosa misura | Chiavi | Licenza | Note |
|---|---|---|---|---|
| **BDAP Open Data** `bdap-opendata.rgs.mef.gov.it` | Circa 3.700 dataset: bilancio dello Stato, gestione delle spese, SIOPE, opere pubbliche, bilanci degli enti, debito | CF ente, capitolo, piano dei conti | CC BY | *verificato.* API CKAN funzionante |
| **SIOPE** (via BDAP) | **Pagamenti e incassi di cassa** per codice gestionale | CF ente, codice gestionale | riuso libero | *verificato.* È la via per la spesa ICT bottom-up |
| **soldipubblici.gov.it** | — | — | — | *verificato.* **Dismesso**, reindirizza alla manutenzione AgID |
| **CPT — Conti Pubblici Territoriali** | Spesa consolidata del Settore Pubblico Allargato, società partecipate incluse | regione, settore | aperta | Serie 2000-2023, annuale |
| **Eurostat `gov_10a_exp`** | Spesa per funzione COFOG | paese, COFOG | riuso UE | *verificato.* La vecchia bulk facility è stata dismessa nel 2023: si usa l'API SDMX |

## 3. Progetti, finanziamenti, anagrafi

| Fonte | Cosa misura | Chiavi | Licenza | Note |
|---|---|---|---|---|
| **OpenCoesione** | Costo, impegni e **pagamenti** per progetto | CUP | CC BY 4.0 | *verificato.* Pubblicato anche in Parquet. Bimestrale |
| **ItaliaDomani / ReGiS** | Progetti PNRR con finanziamento | CUP, CLP | CC BY 4.0 | *verificato.* I path dei file cambiano a ogni rilascio |
| **openpnrr.it** (Openpolis, non ufficiale) | Progetti PNRR più `cig_gare-pnrr.csv` | CUP, CIG | ODbL 1.0 | **L'unico ponte pubblico CUP → CIG** |
| **OpenCUP** | Costo e finanziamento dei progetti d'investimento | CUP, CF soggetto | CC BY | Bulk libero da 2,2 GB. L'API documentata **non è aperta**: risponde 401 |
| **IndicePA** `indicepa.gov.it/ipa-dati` | 28 dataset: enti, unità organizzative, domicili digitali, **responsabili della transizione al digitale** | codice IPA, CF | CC BY 4.0 | *verificato.* Aggiornamento giornaliero |
| **EU Financial Transparency System** | Beneficiari del bilancio UE 2007-2025 | **partita IVA** | riuso UE | Bulk libero. Sottoutilizzato in Italia |

## 4. ICT in senso stretto

| Fonte | Cosa misura | Formato | Note |
|---|---|---|---|
| **PA Digitale 2026** `teamdigitale/padigitale2026-opendata` | Finanziamenti ICT-PNRR per singolo ente | CSV e JSON, CC BY 4.0 | *verificato.* Ricostruito ogni giorno. La fonte open più granulare sull'ICT per ente |
| **ACN — catalogo servizi cloud qualificati** | Infrastrutture e servizi qualificati, con fornitore e livello | CSV, IODL 2.0 | Misura i servizi qualificati, non la spesa. Il portale risponde 403 ai bot |
| **AgID — rilevazione annuale spesa ICT** | Spesa corrente e investimenti per cluster di amministrazioni | **solo PDF** | Circa 77 amministrazioni, oltre il 90% della spesa ICT |
| **AgID/DTD — Censimento del patrimonio ICT** | Per **singolo ente**: organizzazione ICT, data center, migrazione cloud, **voci di costo e licenze software** | **non pubblicato** | Triennale. È il dato più rilevante che manca. Candidato per un accesso civico |
| **Corte dei conti — referto sull'informatica pubblica** | Stime di spesa ICT complessiva | solo PDF | Cadenza irregolare |
| **Anitec-Assinform, Osservatori Politecnico** | Mercato digitale e spesa ICT della PA | a pagamento | Citabili, non riusabili |

## 5. Il perimetro ICT sui CPV

Divisioni di riferimento: **48** software e sistemi informativi, **72** servizi IT, **30** macchine
per ufficio e computer, **32** apparecchiature TLC, **64** servizi di telecomunicazione.

Tre avvertenze verificate su dati reali:

1. **La divisione 30 non è hardware ICT.** I codici più frequenti sono buoni pasto e cancelleria.
   Serve una lista bianca di codici, altrimenti il perimetro è falso.
2. **I server stanno nella 48** (CPV 48820000), cioè un prodotto hardware classificato come software.
3. **Le licenze non hanno un CPV proprio.** Licenza perpetua, canone SaaS e sviluppo su misura
   ricadono indistintamente sotto 48 e 72.

## 6. Chiavi di collegamento

- **CIG**: lega tutti i dataset ANAC, e Consip solo tramite `gare-asp` e `bandi-e-gare`.
- **CUP**: lega OpenCUP, OpenCoesione, ReGiS e il monitoraggio opere pubbliche.
- **CUP → CIG**: nei dati ufficiali non c'è. L'unico ponte pubblico pronto è il file di openpnrr.it.
- **Codice fiscale ente / codice IPA**: il collante lato amministrazione. Attenzione: il codice AUSA
  identifica la stazione appaltante in ANAC e non coincide con il codice IPA.
- **Capitolo di bilancio e codice gestionale SIOPE**: vivono solo nel mondo RGS e **non hanno un
  ponte con il mondo appalti**. È la discontinuità strutturale del sistema informativo italiano:
  la catena impegno → contratto → pagamento non si ricostruisce senza passaggi euristici.

## 7. Chi scarica cosa

| Fonte | Biase | DVINS | AppaltIntel | Atoka PA | DataCivicLab | Cruscotto AgID | onData |
|---|---|---|---|---|---|---|---|
| ANAC OCDS | ● | | ● | | ● | ● | |
| ANAC tabellari | | ● | ● | ● | ● | | |
| ANAC partecipanti e subappalti | | | ● | | | | |
| ANAC Pubblicità Legale | | | ● | | | | ● |
| XML Legge 190 per ente | | | | ● | | | |
| Consip | | ● | parziale | | ● | | |
| SIOPE | | ● | | | ● | ● | ● |
| BDAP, bilancio dello Stato | | ● | | | ● | ● | ● |
| OpenCoesione | | | contesto | | ● | | |
| PNRR ReGiS | | | contesto | | ● | ● | ● |
| OpenCUP | | | | ● | ● | | |
| TED | | ● | ● | via GUUE | | | |
| Portali regionali | | | ● (23) | | | | |
| Dati societari fornitori | | | | ● | ● | | |
| Dati derivati riutilizzabili | dump | ● | | | ● Parquet | ● | ● |

**Nessuno** scarica gli stati di avanzamento e il quadro economico di ANAC, il `gare-asp` di Consip,
l'EU Financial Transparency System. **Nessuno**, in Italia, fa entity resolution sui fornitori né li
collega al gruppo societario e alla giurisdizione.
