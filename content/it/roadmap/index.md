---
title: "Roadmap"
description: "Che cosa l'Osservatorio misura già, che cosa sta costruendo e che cosa manca perché il rendiconto nazionale sulla sovranità digitale della PA italiana sia completo"
keywords: ["roadmap osservatorio", "sovranità digitale", "spesa ICT PA", "cloud pubblico", "misurazione automatica", "rendiconto nazionale"]
---

Oggi sappiamo **chi opera** l'infrastruttura digitale della Pubblica Amministrazione italiana. Non sappiamo ancora **quanto costa, e dove va il denaro**.

Il rendiconto nazionale dell'Osservatorio sarà completo solo quando le due misure staranno una accanto all'altra: chi gestisce i servizi, e quanta parte della spesa pubblica per il cloud finisce a fornitori soggetti a controllo statunitense invece che a fornitori europei e italiani.

Questa pagina dice a che punto siamo. Non contiene date: contiene stati. Le date le scriveremo quando saranno vere.

## La misurazione

### In produzione — chi opera l'infrastruttura

La rilevazione di quale azienda gestisce davvero la posta elettronica ufficiale di **22.987 enti pubblici**, letta dai record DNS pubblici e rieseguita automaticamente. È la base su cui poggia tutto il resto, ed è già pubblica e riproducibile: [metodologia](/metodologia/), [dati aperti](/dati-aperti/).

### In lavorazione — allineamento continuo a MxMap upstream

Il motore di scansione deriva dal progetto open source MxMap. Va mantenuto **allineato allo sviluppo upstream**, così che correzioni e nuovi controlli prodotti dalla comunità arrivino anche qui, invece di divergere in una copia che invecchia. È una scelta di manutenzione, non di funzionalità: determina se fra tre anni lo strumento sarà ancora vivo.

### In lavorazione — analisi longitudinale

Oggi pubblichiamo una fotografia. Serve la **serie storica**: come cambia nel tempo la composizione dei fornitori, ente per ente, con le variazioni evidenziate. Senza questo non si può dire se il Paese si stia muovendo, in quale direzione e quanto in fretta — e non si può verificare l'effetto di nessuna decisione pubblica.

### Da avviare — la misurazione della spesa ICT per il cloud

Il pezzo che manca, e il più oneroso. Misurare **quanta spesa pubblica per servizi cloud finisce a fornitori soggetti a controllo statunitense e quanta resta in Europa e in Italia**, suddivisa **anno per anno** e riseguita automaticamente nel tempo, con lo stesso impianto di MxMap: dati aperti, metodo pubblicato, conti rifacibili da chiunque.

Il prototipo esiste già ed è dichiaratamente parziale. Perché diventi una misura affidabile servono: l'addestramento del classificatore che riconosce le voci di spesa cloud, il completamento dei dati tramite scraping delle sezioni Amministrazione trasparente e accessi civici dove necessario, e una quota di curation manuale che non è eliminabile.

Il software sarà costruito **riusando il più possibile componenti liberi già esistenti** anziché scrivendone di nuovi. Non è una preferenza ideologica: ogni componente scritto da zero è un costo di manutenzione che qualcuno dovrà sostenere per anni, e un osservatorio che non sopravvive alla propria manutenzione non serve a nulla.

### Da avviare — produzione automatizzata del report ufficiale

Il rendiconto va **generato dai dati**, non riscritto a mano a ogni edizione. È la condizione perché esca con regolarità invece che quando qualcuno trova il tempo, e perché ciò che afferma resti verificabile contro i numeri da cui proviene.

## La comunità

### In lavorazione — onboarding delle comunità tecniche

L'Osservatorio è un progetto aperto e multi-stakeholder. È in corso il coinvolgimento delle comunità **cybersecurity**, **open source** e **legaltech**: sono le tre competenze che servono insieme, perché la questione è tecnica, infrastrutturale e giuridica allo stesso tempo, e nessuna delle tre da sola la copre.

Si partecipa da [GitHub](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues) e dal [canale Telegram](https://t.me/+Ot-M_g0dkh1kMGI0), oppure dalla pagina [Partecipa](/partecipa/).

## Pubblicazione e disseminazione

### Da avviare — il primo report ufficiale

La prima edizione completa del rendiconto nazionale, con entrambe le misure.

### Da avviare — una conferenza nazionale

Un momento pubblico in cui i dati vengono presentati e discussi davanti a chi decide, non soltanto pubblicati.

### Da avviare — almeno dieci articoli su riviste specializzate

Con il coinvolgimento di stakeholder dei diversi settori toccati. L'obiettivo non è la rassegna stampa: è che l'argomento venga discusso da chi ha competenza per contestarlo.

### Da avviare — invio massivo a tutti gli enti pubblici

Una comunicazione diretta a **tutte** le amministrazioni: sia a quelle che risultano sovrane, sia a quelle che non lo sono.

A entrambe si spiegherà **perché** la loro posizione è quella rilevata e **quali azioni concrete** possono intraprendere per migliorare il proprio stato di sovranità. Scrivere anche a chi è già in regola non è una cortesia: una scelta corretta che nessuno riconosce non produce imitazione, e la maggior parte degli enti non sa di trovarsi in una condizione diversa da quella dei propri vicini.

## Come contribuire

Ogni voce di questa pagina corrisponde a lavoro che qualcuno deve fare. Chi vuole prenderne una in carico trova tutto su [GitHub Issues](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues); i dati e il metodo sono pubblici perché possano essere rifatti, e contestati, senza chiedere il permesso a noi.
