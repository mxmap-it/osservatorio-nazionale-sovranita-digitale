---
title: "Stato della Sovranità Digitale nella PA - Novembre 2026 (BOZZA)"
date: 2026-11-07
description: "Aggiornamento del report sullo stato della sovranità digitale nella PA italiana: nuovi dati e metodologia irrobustita (attribuzione solo su segnali primari)"
pdf: "/pdf/report-2026-11-sovranita-digitale-pa.pdf"
---

## Sommario

Questo aggiornamento fotografa lo stato della sovranità digitale nella Pubblica Amministrazione italiana al 7 novembre 2026, sulla base di **22.922 enti** registrati nell'IndicePA e analizzati da [MxMap.it](https://mxmap.it/).

## Dati principali

- **50,5%** degli enti usa provider di posta sotto giurisdizione **italiana**;
- **43,3%** si affida a provider soggetti a giurisdizione **extra-UE** (CLOUD Act);
- **0,5%** usa provider **europei non italiani**;
- **5,7%** risulta **Sconosciuto**: l'evidenza tecnica non consente di provare chi gestisca la posta.

Sui soli enti classificati, l'indice di sovranità (quota sotto giurisdizione italiana) è del **53,6%**.

## Che cosa è cambiato rispetto al report di giugno

La differenza principale non è nei comportamenti degli enti ma nella **metodologia, irrobustita**: da novembre 2026 il classificatore attribuisce un provider cloud **solo in presenza di segnali primari** (routing MX, SPF corroborato, autodiscover, DKIM). Le semplici registrazioni Microsoft/Google (tenant, token di verifica) — che provano l'uso di licenze cloud, non l'hosting della posta — non bastano più. Due effetti:

1. centinaia di enti dietro filtri antispam, prima attribuiti per presunzione ai cloud statunitensi, oggi sono dichiarati onestamente **Sconosciuti** (da qui la crescita dal 2,7% al 5,7%) o riconosciuti come gestiti dal **fornitore informatico italiano** che ne opera la posta;
2. la quota extra-UE scende di conseguenza (dal 46,1% al 43,3%): la dipendenza dai cloud esteri resta il fenomeno dominante, ma ora è misurata **senza sovrastime**.

I criteri completi sono nella [metodologia](/metodologia/) e, in dettaglio tecnico, nella [metodologia di MxMap](https://mxmap.it/methodology.html).

## Metodologia

L'analisi classifica ogni ente in base alla **sovranità giuridica** del provider che ne gestisce la posta elettronica — sotto quale ordinamento (italiano, europeo o extra-UE) ricadono i dati delle comunicazioni — letta dai record DNS pubblici e riverificata ogni notte. Il report in PDF, marcato BOZZA, è generato automaticamente dagli stessi dati aperti del sito.
