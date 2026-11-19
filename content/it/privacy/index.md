---
title: "Privacy"
description: "Che cosa raccolgono i siti dell'Osservatorio Nazionale Sovranità Digitale: niente cookie, statistiche aggregate su un server in UE, nessun indirizzo IP conservato."
---

**In breve:** questo sito non usa cookie né strumenti di profilazione. Contiamo le visite con un contatore che gira sul nostro server in Unione europea, non conserva indirizzi IP e produce solo totali. Gli stessi criteri valgono per [mxmap.it](https://mxmap.it/) e [analisi-spesa-ict.mxmap.it](https://analisi-spesa-ict.mxmap.it/).

## Statistiche di accesso

Usiamo [GoatCounter](https://www.goatcounter.com/), software libero, installato su un server dell'Osservatorio in Francia (Scaleway, Parigi) all'indirizzo `stats.mxmap.it`. Nessun servizio di statistiche di terzi riceve dati sulle visite.

Per ogni pagina vista, il contatore riceve:

- l'indirizzo della pagina, senza parametri;
- il titolo della pagina;
- il sito da cui si arriva, se il browser lo comunica;
- nome e versione del browser e del sistema operativo;
- la larghezza dello schermo.

Dall'indirizzo IP ricava, al momento della visita, il **paese** e la **regione** (per l'Italia); poi l'indirizzo viene scartato e **non è mai salvato**. Per contare una persona una volta sola anche se ricarica la pagina, il contatore calcola un codice temporaneo che resta solo in memoria per alcune ore e non è legato a nessuna identità. Nel database restano **solo totali per pagina e per giorno** (o per ora): non esiste un elenco di visite o di visitatori.

- **Niente cookie**, niente `localStorage`, niente impronta del browser: sul tuo dispositivo non viene scritto né letto nulla, per questo non c'è un banner di consenso.
- Se il browser invia **Do Not Track** o **Global Privacy Control**, la visita non viene contata affatto.
- Il server web che riceve i conteggi non tiene registri degli accessi.

I totali sono pubblicati nella pagina [Statistiche](/statistiche/) e ogni lunedì dal bot Telegram, mostrando solo le voci con almeno 5 visite. La [dashboard in tempo reale](https://stats.mxmap.it/) è pubblica.

## Ospitalità del sito

I siti sono pubblicati con **GitHub Pages** (GitHub Inc., gruppo Microsoft, Stati Uniti). Come qualunque server web, GitHub riceve l'indirizzo IP e i dati tecnici di ogni richiesta per servire le pagine e proteggerle dagli abusi, secondo la propria [informativa](https://docs.github.com/it/site-policy/privacy-policies/github-general-privacy-statement); non abbiamo accesso a quei dati. È una dipendenza da un fornitore soggetto al CLOUD Act, la stessa che documentiamo per le PA, e la dichiariamo. I caratteri e le librerie grafiche sono serviti dal sito stesso, senza CDN esterni.

## Comunità Telegram

Il bot dell'Osservatorio legge i messaggi del gruppo Telegram per misurare la partecipazione e sintetizzare i temi discussi. Non conserva nomi né username: le persone sono contate con un codice anonimo, le sintesi non nominano né citano nessuno e i messaggi restano sul nostro server. Chi non vuole esserci scrive `/escludimi` nel gruppo: i suoi messaggi vengono cancellati e da quel momento ignorati.

## Contatti

Per domande su questi trattamenti apri una [issue su GitHub](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues) o usa i contatti nella pagina [Chi siamo](/chi-siamo/).
