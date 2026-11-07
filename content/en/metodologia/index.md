---
title: "Methodology"
description: "How data on digital sovereignty is collected and analysed"
---

## Data source

The Observatory is based on the data collected by the [MxMap.it](https://mxmap.it/) project, which maps the MX (Mail Exchange) records of all domains of the Italian Public Administration registered in the Index of Public Administrations (IndicePA).

## Quality and limits of the source

IndicePA is the official registry of public bodies, but **it is not a clean dataset from which the "normal" (non-PEC) mail domain of each body can be inferred immediately and without reworking**: the email domains it contains are often inconsistent, incomplete or absent. For this reason MxMap's data **does not derive from a direct reading of IndicePA**, but from a structured reworking — extraction, correction, validation and enrichment of the domains — documented in the [MxMap discovery methodology](https://mxmap.it/methodology.html).

The continuous improvement and cleaning of IndicePA is therefore a **core functional dependency** of the Observatory, to be addressed with a dedicated project, tracked in [mxmap.it#2 — *Software for a well-maintained and cleaned IndicePA*](https://github.com/mxmap-it/mxmap.it/issues/2): to measure data quality independently and activate reporting cycles (including via PEC to the bodies and AgID) to correct it at the source.

## What we measure

For each body of the Italian PA, we analyse:

- **Email provider**: which service manages the body's email
- **Nationality of the provider**: whether the provider is Italian, European or non-European
- **Data jurisdiction**: under which legal system the communications data falls
- **Evolution over time**: how these parameters change over time

## Definition of digital sovereignty

For the purposes of this observatory, we define "digital sovereignty" as the ability of a public body to maintain effective control over its own digital infrastructure and over citizens' data, with particular reference to:

1. **Jurisdiction**: the data remains under Italian/European jurisdiction
2. **Operational control**: the body maintains control over its own infrastructure
3. **Technological independence**: absence of critical dependence on non-European suppliers

## The four sovereignty categories

Every classified body falls into one of four categories, defined by the **legal jurisdiction of the provider** that manages its email (not by the physical location of the servers):

- **Italian** (`it`): email is managed by an operator subject to Italian law — regional public cloud, Italian commercial provider, or the body's own infrastructure.
- **EU non-Italian** (`eu_non_it`): a European, non-Italian operator (e.g. OVH, Hetzner, IONOS, Infomaniak).
- **Non-EU / CLOUD Act** (`extra_eu`): an operator subject to non-European jurisdictions — in practice almost always the US clouds (Microsoft 365, Google Workspace), reachable by US CLOUD Act requests wherever the servers are located.
- **Unknown** (`unknown`): the available technical evidence **cannot prove** who manages the email — see below.

## When we declare "Unknown"

"Unknown" is not an error: it is the method's **honest non-verdict**. It happens in two cases:

1. **No MX record**: the body's domain declares no mail server at all (certified-mail-only bodies, brochure domains, inconsistent IndicePA records).
2. **Backend behind a gateway cannot be determined**: the body's mail flows through a *security gateway* (an antispam filter such as Sophos, Libraesva, Proofpoint) that hides the final destination, and no primary signal (corroborated SPF, autodiscover, DKIM) proves what sits behind it. In these cases **we do not attribute a provider by presumption**: having, say, a Microsoft/Google registration (tenant, verification token) proves the use of cloud licences, not mail hosting.

This choice — preferring a declared "we don't know" over an unproven attribution — follows the classifier of the MxMap family's peer-reviewed reference paper, and is why the "Unknown" share is not zero. The full technical criteria are in the [MxMap methodology](https://mxmap.it/methodology.html#method-gateway_lookthrough); the bodies in this condition are publicly listed on the [anomalies page](https://mxmap.it/anomalie.html), with an active reduction roadmap (cross-checking ICT procurement data, active verification, direct outreach to the bodies).

## Update frequency

Data is collected periodically and reports are published at regular intervals to monitor its evolution over time.

## Related methodologies and initiatives

The Observatory's methodology is shared with the **MxMap** family of projects, active in several European countries, and stands alongside other initiatives that measure digital sovereignty with complementary approaches. The full list is on the [Related initiatives in Europe](/iniziative/) page.

## What we do not measure yet

This page describes what the Observatory measures today. What is still missing — first of all the measurement of public spending on cloud services, year by year — is set out in the [roadmap](/en/roadmap/), together with the state of progress of each piece.
