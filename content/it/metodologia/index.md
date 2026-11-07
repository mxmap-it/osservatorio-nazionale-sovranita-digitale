---
title: "Metodologia"
description: "Come vengono raccolti e analizzati i dati sulla sovranità digitale"
---

## Fonte dei dati

L'Osservatorio si basa sui dati raccolti dal progetto [MxMap.it](https://mxmap.it/), che mappa i record MX (Mail Exchange) di tutti i domini della Pubblica Amministrazione italiana registrati nell'Indice delle Pubbliche Amministrazioni (IndicePA).

## Qualità e limiti della fonte

IndicePA è l'anagrafe ufficiale degli enti, ma **non è una base dati pulita da cui inferire in modo immediato e senza rielaborazioni il dominio di posta "normale" (non-PEC) di ciascun ente**: i domini email vi sono spesso incoerenti, incompleti o assenti. Per questo i dati di MxMap **non derivano da una lettura diretta di IndicePA**, ma da una rielaborazione strutturata — estrazione, correzione, validazione e arricchimento dei domini — documentata nella [metodologia di scoperta di MxMap](https://mxmap.it/methodology.html).

Il miglioramento e la bonifica continua di IndicePA sono perciò una **dipendenza funzionale core** dell'Osservatorio, da affrontare con un progetto dedicato, tracciato in [mxmap.it#2 — *Software per un IndicePA ben manutenuto e bonificato*](https://github.com/mxmap-it/mxmap.it/issues/2): misurare in modo autonomo la qualità del dato e attivare cicli di segnalazione (anche via PEC verso gli enti e AgID) per correggerlo alla fonte.

## Cosa misuriamo

Per ogni ente della PA italiana, analizziamo:

- **Provider di posta elettronica**: quale servizio gestisce la posta dell'ente
- **Nazionalità del provider**: se il provider è italiano, europeo o extra-europeo
- **Giurisdizione dei dati**: sotto quale ordinamento giuridico ricadono i dati delle comunicazioni
- **Evoluzione temporale**: come cambiano questi parametri nel tempo

## Definizione di sovranità digitale

Ai fini di questo osservatorio, definiamo "sovranità digitale" come la capacità di un ente pubblico di mantenere il controllo effettivo sulle proprie infrastrutture digitali e sui dati dei cittadini, con particolare riferimento a:

1. **Giurisdizione**: i dati restano sotto la giurisdizione italiana/europea
2. **Controllo operativo**: l'ente mantiene il controllo sulle proprie infrastrutture
3. **Indipendenza tecnologica**: assenza di dipendenza critica da fornitori extra-europei

## Le quattro categorie di sovranità

Ogni ente classificato ricade in una di quattro categorie, definite dalla **giurisdizione giuridica del provider** che gestisce la posta (non dalla collocazione fisica dei server):

- **Italiano** (`it`): la posta è gestita da un operatore soggetto all'ordinamento italiano — cloud pubblico regionale, provider commerciale italiano o infrastruttura propria dell'ente.
- **UE non italiano** (`eu_non_it`): operatore europeo non italiano (es. OVH, Hetzner, IONOS, Infomaniak).
- **Extra-UE / CLOUD Act** (`extra_eu`): operatore soggetto a giurisdizioni extraeuropee, in pratica quasi sempre i cloud statunitensi (Microsoft 365, Google Workspace), raggiungibili dalle richieste del CLOUD Act statunitense ovunque si trovino i server.
- **Sconosciuto** (`unknown`): l'evidenza tecnica disponibile **non consente di provare** chi gestisce la posta — vedi sotto.

## Quando dichiariamo «Sconosciuto»

«Sconosciuto» non è un errore: è il **non-verdetto onesto** del metodo. Succede in due casi:

1. **Nessun record MX**: il dominio dell'ente non dichiara alcun server di posta (enti solo-PEC, domini vetrina, record IndicePA incoerenti).
2. **Backend dietro gateway non determinabile**: la posta dell'ente passa per un *security gateway* (filtro antispam come Sophos, Libraesva, Proofpoint) che nasconde la destinazione finale, e nessun segnale primario (SPF corroborato, autodiscover, DKIM) prova chi ci sia dietro. In questi casi **non attribuiamo un provider per presunzione**: avere ad esempio una registrazione Microsoft/Google (tenant, token di verifica) prova l'uso di licenze cloud, non l'hosting della posta.

Questa scelta — preferire un dichiarato «non lo sappiamo» a un'attribuzione non provata — segue il classificatore del paper accademico di riferimento della famiglia MxMap ed è il motivo per cui la quota di «Sconosciuto» non è zero. I criteri tecnici completi sono nella [metodologia di MxMap](https://mxmap.it/methodology.html#method-gateway_lookthrough); gli enti in questa condizione sono esposti pubblicamente nella [pagina anomalie](https://mxmap.it/anomalie.html) con una roadmap attiva di riduzione (incrocio con i dati di spesa ICT, verifica attiva, contatto diretto con gli enti).

## Frequenza di aggiornamento

I dati vengono raccolti periodicamente e i report vengono pubblicati con cadenza regolare per monitorare l'evoluzione nel tempo.

## Metodologie e iniziative collegate

La metodologia dell'Osservatorio è condivisa con la famiglia di progetti **MxMap**, attiva in diversi paesi europei, e si affianca ad altre iniziative che misurano la sovranità digitale con approcci complementari. L'elenco completo è nella pagina [Iniziative collegate in Europa](/iniziative/).

## Che cosa non misuriamo ancora

Questa pagina descrive ciò che l'Osservatorio misura oggi. Ciò che manca — in primo luogo la misurazione della spesa pubblica per i servizi cloud, anno per anno — è dichiarato nella [roadmap](/roadmap/), insieme allo stato di avanzamento di ogni pezzo.
