# Pilota sui dati ANAC (misurato da noi, 27/10/2026)

Script: `mxmap-it/analisi-spesa-ict` `tools/analisi/pilota_classificazione.py` (regex a priorità sulla descrizione `oggetto_lotto` + `oggetto_gara`), dati ANAC `cig-2025` (12 file mensili) dal mirror. Perimetro ICT provvisorio per CPV: 48*, 72*, 302*, 3223–3226*, 50312*, 50320*, 51611*, 64216*, 64222*, 79342*. Tutti i numeri sono [P-nostro], misurati; il perimetro e le regex sono provvisori.

## Esito 2025 (111.681 CIG ICT, 41,39 mld€ di importi lotto)

| Classe | CIG | % CIG | Importo | % importo |
|---|---|---|---|---|
| Non classificato | 97.353 | 87,2 | 25,32 mld | 61,2 |
| Cloud generico (cloud/SaaS/IaaS/hosting senza marchio) | 7.447 | 6,7 | 12,80 mld | 30,9 |
| Infrastruttura propria (server, storage, CED…) | 3.985 | 3,6 | 0,76 mld | 1,8 |
| Microsoft cloud | 964 | 0,9 | 0,16 mld | 0,4 |
| Licenze bigtech on-prem (Microsoft, Oracle, VMware) | 853 | 0,8 | 1,08 mld | 2,6 |
| Altri SaaS USA (Salesforce, ServiceNow, Zoom, Adobe…) | 418 | 0,4 | 0,20 mld | 0,5 |
| PSN | 285 | 0,3 | 0,93 mld | 2,2 |
| Google | 194 | 0,2 | 0,02 mld | 0,04 |
| Operatori cloud IT/UE (Aruba, Seeweb, WIIT, Retelit…) | 99 | 0,1 | 0,08 mld | 0,2 |
| AWS | 60 | 0,05 | 0,04 mld | 0,1 |
| Oracle cloud | 23 | 0,02 | 0,006 mld | 0,01 |

## Lezioni

1. **Gli importi sono dominati dai massimali degli accordi quadro.** Nel "cloud generico" (13,05 mld) i primi 10 CIG valgono l'85,3%: AQ Consip (3,78 mld), AQ Banca d'Italia (3,0 mld), AQ InfoCamere "servizi applicativi in ottica cloud" (2×1,6 mld), lotti Consip IaaS/PaaS. Sommare gli importi dei CIG padre con quelli dei derivati conta due volte e confonde massimale con spesa. **Regola:** i CIG di accordo quadro si escludono dalla somma; si contano i contratti attuativi (campo ANAC `cig_accordo_quadro` valorizzato) e, per la cassa, i pagamenti SIOPE.
2. **La lente prodotto si eredita dai lotti Consip.** L'AQ Consip ID 2746 "Cloud IaaS e PaaS 2" ha un lotto per fornitore cloud; nei dati ANAC: B6A19F425E = Lotto 1 AWS (aggiudicatario Fastweb), B6A19F5331 = Lotto 2 Google, B6A19F6404 = Lotto 3 Microsoft, B6A19F74D7 = Oracle, B6A19F85AA = IBM, B6A19F967D = Aruba. I contratti attuativi riportano il CIG del lotto in `cig_accordo_quadro`. Nel solo delta ANAC di ottobre 2026: AWS 10 adesioni 4,75 M€, Google 4 / 1,92 M€, Microsoft 16 / 8,94 M€, Oracle 7 / 7,23 M€, Aruba 3 / 0,59 M€, IBM 0. Prova diretta che il fornitore registrato (Fastweb) non è il prodotto (AWS).
3. **Il "cloud generico" è soprattutto SaaS verticale italiano** (Spaggiari, Halley, Urbi/PA Digitale, cartelle cliniche, protocollo): la giurisdizione del prodotto è italiana, ma l'hosting sottostante può essere su hyperscaler USA. Serve un secondo livello: giurisdizione dell'infrastruttura su cui gira il SaaS (catalogo ACN, dichiarazioni dei fornitori).
4. **L'87% dei CIG ICT non è cloud né infrastruttura riconoscibile**: assistenza, sviluppo, servizi informatici generici. È atteso; il perimetro "cloud" si misura come sottoinsieme, non come quota del totale ICT.
5. **Infrastruttura propria**: le regex catturano acquisti di server (CPV 48820000) ma anche falsi positivi ("Jira Data Center", "server proxy" in abbonamento, "crioconservazione"): servono regole per CPV + testo e validazione su campione.
6. **Precisione non ancora misurata**: campioni casuali di 50 CIG per classe in `lavoro/pilota/2025-campioni.json` per la validazione manuale (gold standard).
