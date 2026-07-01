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

## Update frequency

Data is collected periodically and reports are published at regular intervals to monitor its evolution over time.

## Related methodologies and initiatives

The Observatory's methodology is shared with the **MxMap** family of projects, active in several European countries, and stands alongside other initiatives that measure digital sovereignty with complementary approaches. The full list is on the [Related initiatives in Europe](/iniziative/) page.
