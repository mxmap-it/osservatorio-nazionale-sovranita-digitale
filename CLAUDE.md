# CLAUDE.md — Guida al progetto per Claude e per chi contribuisce

Questo file raccoglie ragionamenti, assunzioni, vincoli e convenzioni del progetto
**Osservatorio Nazionale Sovranità Digitale**, così che chiunque (umano o Claude)
possa contribuire in modo coerente. Leggilo prima di modificare il sito.

---

## 0. Ripartire da zero su un altro computer

Un `git clone` deve bastare. Se non basta, è un difetto da correggere: gli
artefatti costosi stanno in git e si **ripristinano**, non si rigenerano.

```bash
git clone https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale.git
cd osservatorio-nazionale-sovranita-digitale
python tools/verifica-ambiente.py     # dice subito cosa manca
hugo --quiet --gc                     # costruisce il sito in public/
```

**Per il solo sito serve unicamente [Hugo Extended](https://gohugo.io/installation/)**
(≥ 0.163). Nessuna dipendenza Python, nessun passo di build aggiuntivo: il
deploy su GitHub Pages fa esattamente questo.

**Per rigenerare PDF, slide e immagini** servono anche le librerie Python:

```bash
python -m pip install -r requirements.txt
```

### Font

I generatori **non** contengono più percorsi di sistema cablati (del tipo `C:/Windows/Fonts/arial.ttf`).
La risoluzione sta in `docs/_font.py`, che cerca una famiglia utilizzabile su
Windows, macOS e Linux:

- `registra_famiglia()` registra in reportlab i nomi `Arial`, `Arial-Bold`,
  `Arial-Italic`, `Arial-BoldItalic`, `Consolas`, `Mono` — **i nomi restano
  quelli anche quando il font sottostante è un altro**, così il corpo dei
  generatori non cambia;
- `percorso_sans(stile)` restituisce un *percorso*, per le librerie che vogliono
  un file e non un nome registrato (PIL, fpdf).

Ordine di preferenza: **Arial** (è il font dei PDF pubblicati), poi Liberation
Sans, DejaVu Sans, Arimo, Helvetica. Su Linux, dove Arial non c'è, i PDF
rigenerati avranno un font diverso: `_font.py` lo segnala su stderr. Non è un
problema, perché i PDF pubblicati si ripristinano da git.

Chi vuole **Segoe UI** lo chiede esplicitamente con
`percorso_sans(..., preferisci_segoe=True)`: lo usa solo la copertina LinkedIn,
che è disegnata con quello. Metterlo per primo ovunque cambierebbe le
interruzioni di riga di tutti i PDF.

### Che cosa NON va rigenerato

- `static/slide/romhack-2026-mxmap-italia.pptx` — il deck definitivo, rivisto a
  mano, con gli screenshot. `tools/genera-slide-romhack.py` produce solo una
  bozza in `static/slide/_bozza/` e **non deve** scrivere sul file pubblicato.
- I PDF in `static/pdf/` — sono la versione pubblicata e citata all'esterno.

---

## 1. Cos'è il progetto

Sito statico di **monitoraggio civico** che misura e racconta lo stato della
**sovranità digitale nella Pubblica Amministrazione italiana**, partendo dai
servizi di **posta elettronica** (~23.000 enti dell'IndicePA).

- **Sito live:** https://osservatorio.mxmap.it/
- **Repo:** https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale
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
3. **Workflow PDF (bilingue):** ogni PDF ha un generatore IT `docs/genera_<x>.py`
   e uno EN `docs/genera_<x>_en.py` (stessa struttura reportlab/fpdf, testo tradotto,
   numeri in formato EN `{n:,}`, watermark "BOZZA"→"DRAFT", footer brand EN). Output
   in `static/pdf/`: `<kebab>.pdf` (IT) e `<kebab>-en.pdf` (EN). Il link nelle pagine
   è language-aware: `{{ printf "pdf/<kebab>%s.pdf" (cond $isEN "-en" "") | relURL }}`
   + `download`. Eccezione: `eu-briefing-...pdf` è già in inglese → linkato uguale in
   entrambe le lingue. Aggiornando un PDF IT, **rigenera anche l'EN** e committa insieme
   generatori + PDF + layout. Verifica `200 application/pdf`.
4. **Git su Windows/PowerShell:** usa il **tool Bash** per i commit, oppure
   here-string isolata; non concatenare il commit con `;` in PowerShell.
5. **Link a MxMap:** i **link pubblici** (header, contenuti, footer, PDF) puntano
   al dominio `https://mxmap.it/`. Il **dato** (`kpi.json`) e quindi
   `KPI_SOURCE_URL` dell'Action restano su `https://fpietrosanti.github.io/mxmap.it/`
   (endpoint dati verificato). NB: al momento `mxmap.it` può avere il custom
   domain GitHub Pages non ancora configurato (errore certificato): i link
   diventano validi quando il dominio è attivo.
6. **Bilingue IT + EN — tieni l'inglese sempre aggiornato.** L'italiano è la
   lingua primaria; l'**inglese (`en`) è una traduzione di prima classe, da
   mantenere sincronizzata**. Ogni modifica a testo/contenuto **deve aggiornare
   anche la versione EN** nello stesso commit. Due meccanismi:
   (a) **chrome + homepage + stringhe UI brevi/ripetute** → chiavi in
   `i18n/it.toml` + `i18n/en.toml` (`{{ i18n "chiave" }}`);
   (b) **layout di sezione con prosa lunga** → condizionale inline
   `{{ if $isEN }}EN{{ else }}IT{{ end }}` (`{{ $isEN := eq site.Language.Lang "en" }}`
   subito dopo `{{ define "main" }}`), IT ed EN nello stesso file.
   I **contenuti markdown** hanno la copia in `content/en/<path>` (layout custom →
   solo frontmatter tradotto; pagine rese da `_default/single|list` → anche il
   corpo). Numeri: `(cond $isEN "- . ," "- , .")`. `head.html` è già bilingue
   (description con statistiche, robots index it+en, hreflang, JSON-LD). Le altre
   22 lingue UE restano `noindex` finché non tradotte. Non lasciare mai una pagina
   EN con testo italiano residuo.

   **⚠️ ECCEZIONE — materiali del progetto documentario (`progetti/documentario-cloud-act/`
   e la pagina `/progetto-documentario/`).** Qui la regola **non** si applica commit per
   commit: sono **bozze in revisione continua**, e tradurre un bersaglio in movimento
   produce spreco e disallineamento. Decisione del committente (29/07/2026): **si lavora
   solo in italiano**; l'inglese si fa **in un unico passaggio alla fine**, su suo
   esplicito «visto si stampi». Fino ad allora **non tradurre** script, storyboard,
   booklet, dossier, pagina di progetto né schede grafiche.
   **Ma va predisposto fin da subito**: stringhe dell'interfaccia in file dati con
   entrambe le chiavi (`it`/`en`), template che pesca in base alla lingua, e per gli SVG
   il template cerca il suffisso `-en` con ricaduta sull'italiano se assente. Così alla
   fine basta popolare, senza toccare codice.
   **Il resto del sito pubblico resta sotto la regola 6 piena.**
7. **Header:** nessun brand MxMap a sinistra; link MxMap + un solo link GitHub a
   destra (vedi `layouts/partials/header.html`).
8. **Tono:** civico, non ideologico, basato su dati verificabili. "Non siamo
   contro un fornitore: documentiamo una dipendenza giurisdizionale."
9. **⚠️ Quando cambia un FATTO, propagalo a TUTTI gli artefatti.** È l'errore più
   facile da commettere e il più costoso: il sito si corregge subito, i PDF no —
   **i PDF non si aggiornano da soli**. Ogni volta che una verifica ribalta o
   precisa un fatto già pubblicato, fai il giro completo **nello stesso commit**:
   (a) pagine del sito, IT **ed** EN; (b) **generatori PDF** IT ed EN, con
   rigenerazione e copia in `static/pdf/`; (c) dossier di ricerca in
   `progetti/*/ricerca/`; (d) documenti di sintesi (es. `STATO-DELLE-CONOSCENZE.md`,
   script, pagine di progetto). Poi **verifica per esclusione**: estrai il testo dei
   PDF con `pypdf` e cerca le formulazioni ormai superate ("in corso di verifica",
   "in discussione", "non risulta"), che sono la spia di un artefatto rimasto
   indietro. Un documento scaricabile che promette una verifica già conclusa è
   peggio di un documento che tace.
10. **Gerarchia delle fonti e affidabilità dichiarata.** Per le affermazioni forti
   — soprattutto se riguardano soggetti nominati (aziende, istituzioni, persone in
   carica) — vale: **fonte primaria letta direttamente** > fonte secondaria
   specializzata > stampa. Distingui sempre **"ho letto il testo e non c'è"** da
   **"non sono riuscito a leggere il testo"**: l'assenza documentata è utilizzabile,
   l'assenza presunta no. Marca esplicitamente ciò che è **deduzione** e non fatto
   accertato. Cita **anche i dati che contraddicono la tesi**: ometterli è
   manipolatorio e la controparte li conosce. Diffida delle fonti in **conflitto
   d'interesse** (un fornitore che si autoinserisce fra i qualificabili) e, se le
   citi, dichiara la loro natura.
11. **Pagine di lavoro non pubbliche: "non linkata" NON basta.** Una pagina non
   collegata finisce comunque in sitemap e su Google. Servono tre livelli, tutti e
   tre: (a) `noindex: true` nel frontmatter → `head.html` emette
   `robots noindex,nofollow,noarchive,nosnippet`; (b) esclusione dalla sitemap via
   `layouts/_default/sitemap.xml`, che salta le pagine con `noindex`; (c)
   `build: { list: never }` per tenerla fuori da liste di sezione e feed RSS
   (**`_build` è stato rimosso in Hugo 0.145+**, usa `build`). Verifica sempre con:
   presenza del meta robots, `0` occorrenze in `public/*/sitemap.xml`, `0` link da
   altre pagine, `0` nel feed. Queste pagine possono restare **solo in italiano**
   quando sono documenti di lavoro per interlocutori italiani: la regola 6 vieta
   una pagina EN mezza tradotta, non impone che ogni pagina esista in EN.

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
dagli item Osservatorio in sospeso. Issue: https://github.com/mxmap-it/mxmap.it/issues

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

## 12. Il documento mastro sul PSN, e il vincolo di allineamento pagina ↔ PDF

La pagina **`/psn/`** — *«Perché il PSN non garantisce la sovranità digitale»* — è il
**documento mastro** del progetto sul Polo Strategico Nazionale. Non è una pagina
divulgativa con qualche fonte in fondo: è un atto d'accusa documentato, scritto per
essere **verificato da un tecnico**, non creduto da un lettore.

### 12.1 Che cosa deve garantire, sempre

1. **Ogni affermazione ha la sua fonte in linea.** Un esperto di sicurezza o di
   infrastrutture che legge deve poter cliccare, aprire il documento e confermare —
   senza cercare. Le fonti in fondo non bastano: servono **accanto alla frase**.
2. **Ogni citazione è verbatim da un documento letto per intero**, mai da resoconti
   di seconda mano. Se una fonte è stata letta solo in parte, si dichiara.
3. **Le tre convenzioni non si mescolano mai** (sono nella sezione «Come verificare»):
   *zero occorrenze* = ricerca full-text eseguita e dichiarata · *non documentato* =
   letto e non trovato · *non trovato* = non siamo riusciti a individuarlo.
4. **Le scansioni sono riproducibili**: si dichiarano l'insieme dei documenti e i
   termini cercati, comprese le insidie di estrazione (es. il PDF della Guida alla
   Convenzione si estrae **senza spazi**: una ricerca ingenua dà zeri falsi).
5. **Le fonti-file sono archiviate in `progetti/documentario-cloud-act/fonti/`**,
   perché la prova non dipenda dalla permanenza in rete dei siti dei fornitori.
6. **Si riconosce sempre per primo ciò che funziona.** Il consolidamento del PSN è un
   guadagno reale; Nitro, Alloy, BYOK e i controlli Google sono ingegneria seria.
   Chi attacca ignorandolo perde il confronto — e ha ragione chi glielo fa notare.
7. **Si giudica il quadro normativo, mai le aziende.** Né i fornitori né i partner
   italiani sono accusati di illeciti: non ne abbiamo prova e non la cerchiamo.

### 12.2 🚨 VINCOLO — pagina e PDF non si scrivono due volte

Il documento uscirà anche come **PDF «PSN — Analisi dei Profili di Sovranità
Digitale»**, accanto ai brief. **Il PDF non va mai scritto a mano in parallelo alla
pagina**: due sorgenti divergono al primo aggiornamento, ed è esattamente l'errore che
la regola 9 esiste per impedire.

✅ **Sorgente unica, già realizzata**: il PDF si **genera dalla pagina costruita**
(`public/psn/`), non da un testo gemello. Lo strumento è **`tools/genera-pdf-psn.py`**:

```
hugo --quiet --gc
python tools/genera-pdf-psn.py --lang both
```

Produce `static/pdf/psn-analisi-profili-sovranita-digitale.pdf` e la versione inglese,
leggendo l'HTML renderizzato: titoli, paragrafi, tabelle, riquadri e link diventano il
PDF senza che nessuno riscriva il testo. Ogni modifica al layout si riflette nel PDF alla rigenerazione
successiva, senza intervento manuale.
⚠️ Vale anche per **i due brief** (technical advice e policy advice): le tabelle di
sintesi che riprendono questa analisi **citano la sezione della pagina**, e i numeri
che vi compaiono si aggiornano dalla stessa fonte.
🔴 **Prima di ogni pubblicazione**: rigenerare il PDF e verificare che non contenga
frasi che la pagina non contiene più (stessa tecnica della regola 9 — estrazione del
testo e ricerca delle formulazioni superate).

### 12.3 Che cosa alimenta la pagina

Reperti **A50–A56** di `STATO-DELLE-CONOSCENZE.md` (PSN, Google, Oracle, Amazon,
ANSSI) e trappole **35–47**. Ogni modifica sostanziale alla pagina va riflessa nel
registro, e viceversa.

---

## 11. Repo e contatti collegati

- **MxMap.it** (fonte dati): https://github.com/mxmap-it/mxmap.it
- **Telegram** (aggiornamenti): https://t.me/+Ot-M_g0dkh1kMGI0
- **Issue/contatti:** https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale/issues
