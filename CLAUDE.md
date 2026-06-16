# CLAUDE.md — Guida al progetto per Claude e per chi contribuisce

Questo file raccoglie ragionamenti, assunzioni, vincoli e convenzioni del progetto
**Osservatorio Nazionale Sovranità Digitale**, così che chiunque (umano o Claude)
possa contribuire in modo coerente. Leggilo prima di modificare il sito.

---

## 1. Cos'è il progetto

Sito statico di **monitoraggio civico** che misura e racconta lo stato della
**sovranità digitale nella Pubblica Amministrazione italiana**, partendo dai
servizi di **posta elettronica** (~23.000 enti dell'IndicePA).

- **Sito live:** https://osservatorio.mxmap.it/
- **Repo:** https://github.com/fpietrosanti/osservatorio-nazionale-sovranita-digitale
- **Fonte dati:** progetto **MxMap.it** → https://mxmap.it/ (dominio pubblico)
- **Fondatore:** Fabio Pietrosanti
- **Licenza:** contenuti, dati e codice sotto **CC BY-SA 4.0**

**Missione:** non solo raccogliere dati, ma diffonderli a *tutti gli stakeholder*
(decisori, regolatori, PA, provider, ricercatori, giornalisti, società civile,
istituzioni UE) perché ciascuno agisca nel proprio ambito. È un progetto
dichiaratamente **multi-stakeholder** e parte di un **movimento europeo** (vedi
la pagina `/iniziative/` e la famiglia MxMap).

---

## 2. Concetti chiave e assunzioni (LEGGERE)

- **"Sovranità" = giurisdizione giuridica del provider**, cioè sotto quale
  ordinamento ricadono i dati in base a *chi* gestisce il servizio (operatore
  italiano / UE / extra-UE). **NON** è la collocazione fisica/tecnica dei server
  (dove "si trova l'MX"). Sono due dimensioni diverse: un provider legalmente
  italiano può ospitare su infrastruttura estera, e un servizio estero può avere
  datacenter in UE ma restare soggetto al **CLOUD Act**. Nei contenuti del sito
  parliamo di **sovranità giuridica**, non di collocazione tecnica dell'MX.
- **Il dato non si legge "direttamente" da IndicePA.** IndicePA è l'anagrafe
  ufficiale ma è sporca/incompleta sui domini email non-PEC. MxMap fa
  estrazione + correzione + validazione + arricchimento. La bonifica continua di
  IndicePA è una **dipendenza core** (issue MxMap #2).
- **Classificazione di sovranità a 4 bucket** (dal `kpi.json`): `extra_eu`
  (CLOUD Act), `eu_non_it` (UE non italiano), `it` (italiano), `unknown`.
- **Placeholder vs dati reali.** I numeri del **sito** sono live da MxMap. I
  **PDF** restano con placeholder (`—%`) finché non esce il *report definitivo*:
  non rigenerarli con numeri reali finché il fondatore non lo richiede.
- **Esempi ≠ adesioni.** Le associazioni elencate in "Chi Siamo" sono **esempi**
  dell'ecosistema da coinvolgere, **non** contribuzioni confermate. Non
  presentare alcuna organizzazione come aderente senza conferma esplicita.

---

## 3. Stack tecnico

- **Hugo Extended v0.163.1** (static site generator).
- **Bootstrap Italia v2.18.1** via CDN (design system della PA italiana). Usa i
  suoi componenti (callout, card, accordion, table) e gli sprite SVG da
  `https://cdn.jsdelivr.net/npm/bootstrap-italia@2.18.1/dist/svg/sprites.svg`.
- **GitHub Pages** + GitHub Actions per il deploy.
- **Multilingua:** 24 lingue UE già configurate in `hugo.toml` (default `it`).
  I contenuti tradotti **non** esistono ancora: l'infrastruttura è pronta, le
  traduzioni sono lavoro futuro. Non rimuovere le lingue.
- **PDF:** generati con **reportlab** (e uno con fpdf2) da script in `docs/`.

---

## 4. Struttura del repository

```
content/            # contenuti (markdown). Una cartella per sezione.
  _index.md         # homepage (front matter; il layout è layouts/index.html)
  chi-siamo/ decisori/ stakeholder/ press/ dati-aperti/ iniziative/
  kit-attivisti/ ricercatori/ partecipa/ metodologia/ faq/ report/ news/ presentazioni/
layouts/            # template Hugo
  index.html        # homepage (hero, KPI, banner evento, ultimi report/news)
  _default/         # single.html / list.html generici
  <sezione>/single.html   # layout dedicati type-based (es. decisori, press, iniziative)
  partials/         # head.html, header.html, footer.html, date-it.html, kpi-pct.html
data/
  kpi.json          # KPI da MxMap (vedi §5). Sovrascritto dalla GitHub Action.
static/pdf/         # PDF scaricabili serviti su /pdf/<nome>.pdf
docs/               # generatori PDF (genera_*.py) + copie "sorgente" dei PDF
.github/workflows/  # deploy.yml (deploy Pages) + update-kpi.yml (sync KPI)
hugo.toml           # config: baseURL, menu (IT/EN), lingue, params evento, mxmapURL
```

**Layout type-based:** una pagina con `type: "press"` nel front matter usa
`layouts/press/single.html`. Per aggiungere una sezione: crea
`content/<nome>/index.md` (con `type: "<nome>"`) + `layouts/<nome>/single.html`.

**Menu:** definito in `hugo.toml` (`[[languages.it.menus.main]]`). 12 voci; è già
pieno — preferisci linkare le pagine nuove da pagine esistenti piuttosto che
aggiungere voci di menu.

---

## 5. Flusso dati KPI (MxMap → sito)

```
MxMap pipeline → https://fpietrosanti.github.io/mxmap.it/kpi.json
        │  (GitHub Action update-kpi.yml, ogni giorno 05:20 UTC + manuale)
        ▼
data/kpi.json → site.Data.kpi → layout (homepage, decisori, press) → deploy
```

- **`data/kpi.json`**: schema con `totals` (n_entities, coverage_pct),
  `sovereignty.{extra_eu,eu_non_it,it,unknown}.{count,pct,label}`,
  `top_providers[]`, `by_cluster[]`, `confidence`. Il seed committato ha
  `"placeholder": true`; il file reale di MxMap non ha quel flag.
- **`layouts/partials/kpi-pct.html`**: riceve `(dict "v" <pct> "ready" <bool>)`
  e stampa la percentuale oppure `—%` quando non disponibile. Uno `0%` reale va
  mostrato come `0%` (non come `—%`) → per questo serve il flag `ready`.
- **`update-kpi.yml`**: fa `curl` del `kpi.json`, lo **valida** (jq: deve avere
  `.totals` e `.sovereignty`), e **solo se cambiato** lo committa e rifà
  build+deploy. Se il fetch fallisce o il file non è valido → **no-op**, non
  sovrascrive i dati buoni. URL sorgente override via repo variable
  `KPI_SOURCE_URL`.
- **Importante:** usa sempre l'URL **di produzione** di MxMap
  (`fpietrosanti.github.io/mxmap.it/...`), mai l'URL di sviluppo.

---

## 6. Vincoli e convenzioni (REGOLE)

1. **Commit & push di ogni modifica**, in commit piccoli e descrittivi. Il deploy
   parte da `push` su `main`.
2. **Verifica via DOM/HTTP, MAI screenshot.** Usa il dev server e controlla con
   fetch+DOMParser / richieste HTTP. Non catturare lo schermo dell'utente.
3. **Workflow PDF:** ogni nuovo PDF → genera in `docs/` → copia in `static/pdf/`
   con nome kebab-case → linka dalla pagina pertinente con
   `{{ "pdf/<nome>.pdf" | relURL }}` + attributo `download` → verifica
   `200 application/pdf` → commit di generatore + PDF + layout insieme.
4. **Git su Windows/PowerShell:** usa il **tool Bash** per i commit, oppure
   here-string isolata; non concatenare il commit con `;` in PowerShell.
5. **Link a MxMap:** i **link pubblici** (header, contenuti, footer, PDF) puntano
   al dominio `https://mxmap.it/`. Il **dato** (`kpi.json`) e quindi
   `KPI_SOURCE_URL` dell'Action restano su `https://fpietrosanti.github.io/mxmap.it/`
   (endpoint dati verificato). NB: al momento `mxmap.it` può avere il custom
   domain GitHub Pages non ancora configurato (errore certificato): i link
   diventano validi quando il dominio è attivo.
6. **Lingua dei contenuti:** italiano. EN/altre lingue solo quando si avviano le
   traduzioni vere.
7. **Header:** nessun brand MxMap a sinistra; link MxMap + un solo link GitHub a
   destra (vedi `layouts/partials/header.html`).
8. **Tono:** civico, non ideologico, basato su dati verificabili. "Non siamo
   contro un fornitore: documentiamo una dipendenza giurisdizionale."

---

## 7. Mappa delle sezioni (e a chi servono)

| Sezione | URL | Pubblico |
|---|---|---|
| Home | `/` | tutti — hero + KPI sovranità + evento |
| Per i Decisori | `/decisori/` | politici, dirigenti PA — KPI, rischi, raccomandazioni, brief |
| Stakeholder | `/stakeholder/` | tutti gli stakeholder + Business Case (provider) |
| Press Kit | `/press/` | giornalisti — numeri citabili, angoli, download, contatti |
| Dati Aperti | `/dati-aperti/` | sviluppatori, analisti — dataset, dizionario, licenza |
| Iniziative | `/iniziative/` | famiglia MxMap UE + altri indici di sovranità |
| Kit Attivisti | `/kit-attivisti/` | cittadini/attivisti — passi pratici, accesso civico |
| Scheda Ricercatori | `/ricercatori/` | accademici — domande di ricerca, citazione |
| Metodologia | `/metodologia/` | come si misura; limiti IndicePA |
| Chi Siamo | `/chi-siamo/` | missione, multi-stakeholder, principi |
| Partecipa | `/partecipa/` | hub "scegli il tuo profilo" |
| FAQ | `/faq/` | domande comuni |
| Report / News | `/report/`, `/news/` | pubblicazioni periodiche |

---

## 8. Documenti PDF e generatori

In `docs/genera_*.py` (reportlab; font Arial da `C:\Windows\Fonts`). Output in
`docs/` e copia in `static/pdf/`. Stile condiviso: blu `#0066B2`, box grigi,
footer con licenza e numero pagina.

- Policy Brief (decisori) · Technical Brief (AgID/ACN/Garante) · Business Case
  (provider/Consip) · EU Briefing (EN, istituzioni UE) · Slide Deck (16 slide) ·
  Kit Attivisti · Scheda Ricercatori · Visione Strategica.

I PDF mantengono i **placeholder** finché il report definitivo non è pronto.

---

## 9. Come contribuire — task comuni

- **Avviare il preview:** dev server Hugo su `:1313` (config `osservatorio-hugo`).
- **Aggiungere una pagina:** `content/<nome>/index.md` (`type: "<nome>"`) +
  `layouts/<nome>/single.html`; linkala da pagine esistenti.
- **Aggiornare i KPI a mano:** Actions → "Update KPI from MxMap" → Run workflow
  (o aspetta le 05:20 UTC). In locale, per testare il rendering con dati reali,
  scarica il `kpi.json` in `data/kpi.json` e ricontrolla, poi ripristina il seed.
- **Rigenerare un PDF:** `python docs/genera_<doc>.py` poi copia in `static/pdf/`.
- **Verifica:** controlla le pagine con fetch + DOMParser; per i PDF, `HEAD` →
  `200 application/pdf`. Niente screenshot.

---

## 10. Roadmap

Lo stato è "MVP completo": sito, sezioni, documenti, KPI live e Action di sync
sono in produzione. La roadmap nasce dalle **issue di MxMap** (la fonte dati) e
dagli item Osservatorio in sospeso. Issue: https://github.com/fpietrosanti/mxmap.it/issues

### Dipendenze dalla qualità del dato (MxMap)
- **[MxMap #4]** Sistemare le ~700 PA in anomalia → 100% copertura con rendiconto.
- **[MxMap #5]** Validazione via **Email Bounce** (accuratezza, prima sugli enti a
  scoring basso, poi su tutti) — da integrare anche in MxMap upstream.
- **[MxMap #2]** Software per un **IndicePA bonificato** (dipendenza core):
  misurare la qualità del dato e attivare segnalazioni PEC a enti/AgID.
- **[MxMap #6]** Pagina di **diagnostica** delle dimensioni di raccolta e
  classificazione, con bottone di segnalazione problemi di qualità.

### Attivazione stakeholder
- **[MxMap #3]** Supporto **mailing agli stakeholder** (email e report per
  tipologia, DB contatti) — dopo il rilascio del report ufficiale.

### Osservatorio (sito)
- **Presentazione alla Camera dei Deputati**: deck di lancio con dati reali, alla
  data evento (oggi placeholder `eventDate` in `hugo.toml`, "da confermare").
- **Aggiornare i PDF** con i numeri reali quando esce il report definitivo (in un
  unico passaggio su tutti i documenti).
- **Visualizzare `by_cluster` e `top_providers`** (già nel `kpi.json`, non ancora
  mostrati sul sito): es. classifica provider e sovranità per categoria di ente.
- **Traduzioni UE** dei contenuti (infrastruttura 24 lingue già pronta).
- **Comunicati stampa** nella sezione Press (oggi placeholder).
- Proporre a David Huser di aggiungere l'istanza **IT** all'elenco ufficiale
  della famiglia MxMap.

---

## 11. Repo e contatti collegati

- **MxMap.it** (fonte dati): https://github.com/fpietrosanti/mxmap.it
- **Telegram** (aggiornamenti): https://t.me/+Ot-M_g0dkh1kMGI0
- **Issue/contatti:** https://github.com/fpietrosanti/osservatorio-nazionale-sovranita-digitale/issues
