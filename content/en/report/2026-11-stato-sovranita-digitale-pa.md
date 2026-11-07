---
title: "State of Digital Sovereignty in the Italian PA - November 2026 (DRAFT)"
date: 2026-11-07
description: "Updated report on the state of digital sovereignty in the Italian public administration: new data and a hardened methodology (attribution on primary signals only)"
pdf: "/pdf/report-2026-11-sovranita-digitale-pa-en.pdf"
---

## Summary

This update captures the state of digital sovereignty in the Italian public administration as of 7 November 2026, based on **22,922 bodies** registered in IndicePA and analysed by [MxMap.it](https://mxmap.it/).

## Key figures

- **50.5%** of bodies use email providers under **Italian** jurisdiction;
- **43.3%** rely on providers subject to **non-EU** jurisdiction (CLOUD Act);
- **0.5%** use **European, non-Italian** providers;
- **5.7%** are **Unknown**: the technical evidence cannot prove who manages their email.

Among classified bodies only, the sovereignty index (share under Italian jurisdiction) is **53.6%**.

## What changed since the June report

The main difference is not in the bodies' behaviour but in the **methodology, which has been hardened**: since November 2026 the classifier attributes a cloud provider **only when primary signals are present** (MX routing, corroborated SPF, autodiscover, DKIM). Mere Microsoft/Google registrations (tenant, verification tokens) — which prove the use of cloud licences, not mail hosting — are no longer enough. Two effects:

1. hundreds of bodies behind antispam gateways, previously attributed to US clouds by presumption, are now honestly declared **Unknown** (hence the growth from 2.7% to 5.7%) or recognised as served by the **Italian IT vendor** that operates their mail;
2. the non-EU share falls accordingly (from 46.1% to 43.3%): dependence on foreign clouds remains the dominant phenomenon, but it is now measured **without overestimates**.

The full criteria are in the [methodology](/en/metodologia/) and, in technical detail, in the [MxMap methodology](https://mxmap.it/methodology.html).

## Methodology

The analysis classifies each body by the **legal sovereignty** of the provider managing its email — under which legal system (Italian, European or non-EU) the communications data falls — read from public DNS records and re-verified every night. The PDF report, marked DRAFT, is generated automatically from the same open data as the website.
