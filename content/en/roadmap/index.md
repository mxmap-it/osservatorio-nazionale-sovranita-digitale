---
title: "Roadmap"
description: "What the Observatory already measures, what it is building, and what is still missing before the national account of digital sovereignty in Italian public administration is complete"
keywords: ["observatory roadmap", "digital sovereignty", "public ICT spending", "public cloud", "automated measurement", "national account"]
---

Today we know **who operates** the digital infrastructure of Italian public administration. We do not yet know **what it costs, or where the money goes**.

The Observatory's national account will only be complete when both measurements sit side by side: who runs the services, and how much of the public money spent on cloud reaches providers under United States control rather than European and Italian ones.

This page states where we are. It contains no dates, only states. We will write dates when they are true.

## The measurement

### In production — who operates the infrastructure

The survey of which company actually runs the official email of **22,987 public bodies**, read from public DNS records and re-run automatically. It is the foundation everything else rests on, and it is already public and reproducible: [methodology](/en/metodologia/), [open data](/en/dati-aperti/).

### In progress — staying aligned with MxMap upstream

The scanning engine derives from the open source MxMap project. It must be kept **aligned with upstream development**, so that fixes and new checks produced by the community reach us too, instead of drifting into a copy that ages. This is a maintenance decision rather than a feature one: it determines whether the instrument will still be alive in three years.

### In progress — longitudinal analysis

Today we publish a snapshot. What is needed is the **time series**: how the composition of providers changes over time, body by body, with the variations made visible. Without it there is no way to say whether the country is moving, in which direction and how fast — and no way to verify the effect of any public decision.

### To start — measuring public cloud spending

The missing piece, and the most demanding one. Measuring **how much public spending on cloud services reaches providers under United States control and how much stays in Europe and Italy**, broken down **year by year** and re-run automatically over time, on the same footing as MxMap: open data, published method, figures anyone can reproduce.

The prototype already exists and is openly partial. Turning it into a reliable measure requires training the classifier that identifies cloud spending items, completing the data through scraping of public transparency sections and freedom-of-information requests where necessary, and a share of manual curation that cannot be removed.

The software will be built by **reusing existing free software components wherever possible** rather than writing new ones. This is not an ideological preference: every component written from scratch is a maintenance cost somebody will carry for years, and an observatory that does not survive its own maintenance is of no use to anyone.

### To start — automated production of the official report

The account must be **generated from the data**, not rewritten by hand for each edition. It is the condition for it to appear regularly rather than whenever someone finds the time, and for its claims to remain checkable against the figures they come from.

## The community

### In progress — onboarding the technical communities

The Observatory is an open, multi-stakeholder project. Work is under way to bring in the **cybersecurity**, **open source** and **legaltech** communities: these are the three competences needed together, because the question is technical, infrastructural and legal at once, and none of the three covers it alone.

You can take part through [GitHub](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues) and the [Telegram channel](https://t.me/+Ot-M_g0dkh1kMGI0), or from the [Contribute](/en/partecipa/) page.

## Publication and dissemination

### To start — the first official report

The first complete edition of the national account, with both measurements.

### To start — a national conference

A public moment where the data is presented and argued in front of those who decide, not merely published.

### To start — at least ten articles in specialist journals

With the involvement of stakeholders from the different sectors concerned. The aim is not press coverage: it is that the subject be discussed by people competent enough to challenge it.

### To start — a mass mailing to every public body

A direct communication to **all** administrations: both those that come out as sovereign and those that do not.

Both will be told **why** their position is what we measured, and **what concrete actions** they can take to improve their state of sovereignty. Writing to those already in good standing is not a courtesy: a sound choice that nobody acknowledges produces no imitation, and most bodies have no idea that they stand in a different position from their neighbours.

## How to contribute

Every item on this page is work someone has to do. Anyone willing to take one on will find it on [GitHub Issues](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues); the data and the method are public so that they can be redone, and disputed, without asking our permission.
