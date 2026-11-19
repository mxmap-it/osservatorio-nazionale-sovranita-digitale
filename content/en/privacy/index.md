---
title: "Privacy"
description: "What the websites of Italy's National Digital Sovereignty Observatory collect: no cookies, aggregate statistics on a server in the EU, no IP addresses stored."
---

**In short:** this site uses no cookies and no profiling tools. We count visits with a counter that runs on our own server in the European Union, stores no IP addresses and produces only totals. The same rules apply to [mxmap.it](https://mxmap.it/) and [analisi-spesa-ict.mxmap.it](https://analisi-spesa-ict.mxmap.it/).

## Visit statistics

We use [GoatCounter](https://www.goatcounter.com/), open-source software, installed on an Observatory server in France (Scaleway, Paris) at `stats.mxmap.it`. No third-party analytics service receives data about visits.

For each page view the counter receives:

- the page address, without parameters;
- the page title;
- the referring site, if the browser sends it;
- browser and operating system name and version;
- the screen width.

At the moment of the visit it derives the **country** and, for Italy, the **region** from the IP address; the address is then discarded and **never stored**. To count a person once even if they reload the page, the counter computes a temporary code that lives in memory only, for a few hours, and is not linked to any identity. The database holds **only totals per page and per day** (or hour): there is no list of visits or visitors.

- **No cookies**, no `localStorage`, no fingerprinting: nothing is written to or read from your device, which is why there is no consent banner.
- If your browser sends **Do Not Track** or **Global Privacy Control**, the visit is not counted at all.
- The web server that receives the counts keeps no access logs.

The totals are published on the [Statistics](/en/statistiche/) page and every Monday by the Telegram bot, showing only items with at least 5 visits. The [live dashboard](https://stats.mxmap.it/) is public.

## Hosting

The sites are published with **GitHub Pages** (GitHub Inc., Microsoft group, United States). Like any web server, GitHub receives the IP address and technical data of each request in order to serve the pages and protect them from abuse, under its own [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement); we have no access to that data. It is a dependency on a provider subject to the CLOUD Act, the same kind we document for Italian public bodies, and we declare it. Fonts and design libraries are served by the site itself, with no external CDN.

## Telegram community

The Observatory's bot reads the messages of the Telegram group to measure participation and summarise the topics discussed. It stores no names or usernames: people are counted through an anonymous code, summaries neither name nor quote anyone, and messages stay on our server. Anyone who does not want to be included writes `/escludimi` in the group: their messages are deleted and ignored from then on.

## Contact

For questions about this processing, open an [issue on GitHub](https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues) or use the contacts on the [About us](/en/chi-siamo/) page.
