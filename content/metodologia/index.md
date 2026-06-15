---
title: "Metodologia"
description: "Come vengono raccolti e analizzati i dati sulla sovranità digitale"
---

## Fonte dei dati

L'Osservatorio si basa sui dati raccolti dal progetto [MxMap.it](https://mxmap.it/), che mappa i record MX (Mail Exchange) di tutti i domini della Pubblica Amministrazione italiana registrati nell'Indice delle Pubbliche Amministrazioni (IndicePA).

## Qualità e limiti della fonte

IndicePA è l'anagrafe ufficiale degli enti, ma **non è una base dati pulita da cui inferire in modo immediato e senza rielaborazioni il dominio di posta "normale" (non-PEC) di ciascun ente**: i domini email vi sono spesso incoerenti, incompleti o assenti. Per questo i dati di MxMap **non derivano da una lettura diretta di IndicePA**, ma da una rielaborazione strutturata — estrazione, correzione, validazione e arricchimento dei domini — documentata nella [metodologia di scoperta di MxMap](https://mxmap.it/methodology.html).

Il miglioramento e la bonifica continua di IndicePA sono perciò una **dipendenza funzionale core** dell'Osservatorio, da affrontare con un progetto dedicato, tracciato in [mxmap.it#2 — *Software per un IndicePA ben manutenuto e bonificato*](https://github.com/fpietrosanti/mxmap.it/issues/2): misurare in modo autonomo la qualità del dato e attivare cicli di segnalazione (anche via PEC verso gli enti e AgID) per correggerlo alla fonte.

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

## Frequenza di aggiornamento

I dati vengono raccolti periodicamente e i report vengono pubblicati con cadenza regolare per monitorare l'evoluzione nel tempo.

## Metodologie e iniziative collegate

La metodologia dell'Osservatorio è condivisa con la famiglia di progetti **MxMap**, attiva in diversi paesi europei, e si affianca ad altre iniziative che misurano la sovranità digitale con approcci complementari. L'elenco completo è nella pagina [Iniziative collegate in Europa](/iniziative/).
