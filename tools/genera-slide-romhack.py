#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera il deck per il talk RomHack Camp 2026.

  MXMap Italia: National Observatory for Digital Sovereignty
  Fabio Pietrosanti (naif) — 2 ottobre 2026, 15:10, STAGE 2, 20' lightning talk, EN

Il deck e' una PRIMA VERSIONE da rivedere a mano: esce in .pptx proprio perche'
sia modificabile. I numeri non sono scritti a mano, vengono da data/kpi.json,
cosi' non possono divergere dal sito.

Marchio e QR sono rigenerati qui: il logo esiste solo in SVG e cairo non e'
disponibile su questa macchina, quindi il simbolo viene ridisegnato con PIL
dalle stesse primitive dell'SVG.

Uso:  python tools/genera-slide-romhack.py
"""
import io
import json
import os

import segno
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "slide", "romhack-2026-mxmap-italia.pptx")
TMP = os.path.join(ROOT, "static", "slide", "_assets")

NAVY = RGBColor(0x17, 0x32, 0x4D)
NAVY_SCURO = RGBColor(0x0E, 0x20, 0x33)
BLU = RGBColor(0x6D, 0xB3, 0xFF)
BIANCO = RGBColor(0xFF, 0xFF, 0xFF)
GRIGIO = RGBColor(0x9E, 0xB2, 0xC6)
ROSSO = RGBColor(0xFF, 0x6B, 0x74)
VERDE = RGBColor(0x5C, 0xB8, 0x8A)

W, H = Inches(13.333), Inches(7.5)

K = json.load(io.open(os.path.join(ROOT, "data", "kpi.json"), encoding="utf-8"))
T, S = K["totals"], K["sovereignty"]
PROV = {p["name"]: p for p in K["top_providers"]}


# --------------------------------------------------------------------------- asset
def simbolo(path, px=512):
    """Il marchio dell'Osservatorio, bianco su trasparente."""
    ss = 4
    im = Image.new("RGBA", (px * ss, px * ss), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    sc = px * ss / 68.0
    cx, cy = 34 * sc, 40 * sc
    def P(x, y):
        return (cx + (x - 34) * sc, cy + (y - 40) * sc)
    for raggio, alpha in ((29, 110), (21, 180), (13, 255)):
        x0, y0 = P(34 - raggio, 40 - raggio)
        x1, y1 = P(34 + raggio, 40 + raggio)
        dr.arc([x0, y0, x1, y1], 180, 360, fill=(255, 255, 255, alpha), width=round(3.4 * sc))
    r = 5 * sc
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 255))
    for i, c in enumerate(((0x5C, 0xB8, 0x8A), (255, 255, 255), (0xFF, 0x6B, 0x74))):
        x0, y0 = P(20 + i * 9.5, 52)
        x1, y1 = P(20 + i * 9.5 + 9, 55)
        dr.rectangle([x0, y0, x1, y1], fill=c + (255,))
    im.resize((px, px), Image.LANCZOS).save(path)


def qr(path, dati):
    segno.make(dati, error="h").save(path, scale=14, border=2, dark="#17324D", light="#FFFFFF")


# --------------------------------------------------------------------------- slide
prs = Presentation()
prs.slide_width, prs.slide_height = W, H
VUOTA = prs.slide_layouts[6]


def fondo(s, colore=NAVY):
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = colore


def txt(s, testo, x, y, w, h, size=18, bold=False, colore=BIANCO, align=PP_ALIGN.LEFT,
        interlinea=1.18, spazio=6):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    righe = testo.split("\n") if isinstance(testo, str) else testo
    for i, riga in enumerate(righe):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = interlinea
        p.space_after = Pt(spazio)
        marcato = riga.startswith("**") and riga.endswith("**")
        r = p.add_run()
        r.text = riga[2:-2] if marcato else riga
        r.font.size = Pt(size)
        r.font.bold = bold or marcato
        r.font.color.rgb = colore
        r.font.name = "Segoe UI"
    return tb


def barra(s, colore=BLU, alto=Inches(0.09)):
    sh = s.shapes.add_shape(1, 0, 0, W, alto)
    sh.fill.solid(); sh.fill.fore_color.rgb = colore
    sh.line.fill.background()
    sh.shadow.inherit = False


def marchio(s, x=None, y=None, cm=Inches(0.62)):
    s.shapes.add_picture(P_SIMBOLO, x if x is not None else W - cm - Inches(0.45),
                         y if y is not None else H - cm - Inches(0.35), cm, cm)


def pie(s, testo="osservatorio.mxmap.it  ·  mxmap.it"):
    txt(s, testo, Inches(0.7), H - Inches(0.72), Inches(8), Inches(0.4), size=11, colore=GRIGIO)


def slide_titolo(titolo, sotto, extra=None):
    s = prs.slides.add_slide(VUOTA); fondo(s, NAVY_SCURO); barra(s)
    s.shapes.add_picture(P_SIMBOLO, Inches(0.75), Inches(0.95), Inches(1.5), Inches(1.5))
    txt(s, titolo, Inches(0.75), Inches(2.75), Inches(11.8), Inches(2), size=40, bold=True)
    txt(s, sotto, Inches(0.75), Inches(4.5), Inches(11.8), Inches(1), size=20, colore=BLU)
    if extra:
        txt(s, extra, Inches(0.75), Inches(5.5), Inches(11.8), Inches(1.4), size=14, colore=GRIGIO)
    return s


def slide_sezione(numero, titolo, occhiello=None):
    s = prs.slides.add_slide(VUOTA); fondo(s, NAVY_SCURO); barra(s)
    txt(s, numero, Inches(0.9), Inches(2.3), Inches(3), Inches(1.4), size=64, bold=True, colore=BLU)
    txt(s, titolo, Inches(0.9), Inches(3.5), Inches(11.5), Inches(1.6), size=34, bold=True)
    if occhiello:
        txt(s, occhiello, Inches(0.95), Inches(4.9), Inches(11), Inches(1), size=17, colore=GRIGIO)
    marchio(s)
    return s


def slide(titolo, righe, occhiello=None, nota=None, size=19):
    s = prs.slides.add_slide(VUOTA); fondo(s); barra(s)
    txt(s, titolo, Inches(0.75), Inches(0.55), Inches(11.9), Inches(1), size=29, bold=True)
    y = Inches(1.75)
    if occhiello:
        txt(s, occhiello, Inches(0.78), Inches(1.5), Inches(11.8), Inches(0.6), size=15, colore=BLU)
        y = Inches(2.15)
    txt(s, righe, Inches(0.78), y, Inches(11.8), Inches(4.4), size=size, interlinea=1.28, spazio=11)
    if nota:
        txt(s, nota, Inches(0.78), H - Inches(1.25), Inches(11.2), Inches(0.7), size=12, colore=GRIGIO)
    marchio(s)
    return s


def slide_numeri(titolo, blocchi, nota=None):
    """blocchi: [(cifra, etichetta, colore)]"""
    s = prs.slides.add_slide(VUOTA); fondo(s); barra(s)
    txt(s, titolo, Inches(0.75), Inches(0.55), Inches(11.9), Inches(1), size=29, bold=True)
    n = len(blocchi)
    larghezza = Inches(11.8 / n)
    for i, (cifra, etichetta, colore) in enumerate(blocchi):
        x = Inches(0.78) + Emu(int(larghezza) * i)
        txt(s, cifra, x, Inches(2.3), larghezza, Inches(1.5), size=54, bold=True, colore=colore)
        txt(s, etichetta, x, Inches(3.85), Inches(int(larghezza) / 914400 - 0.25), Inches(1.6),
            size=15, colore=GRIGIO, interlinea=1.25)
    if nota:
        txt(s, nota, Inches(0.78), H - Inches(1.25), Inches(11.2), Inches(0.7), size=12, colore=GRIGIO)
    marchio(s)
    return s


def slide_washing(marchio_nome, claim, realta, prova, nota=None):
    s = prs.slides.add_slide(VUOTA); fondo(s); barra(s, ROSSO)
    txt(s, "SOVEREIGNTY WASHING", Inches(0.75), Inches(0.5), Inches(11.9), Inches(0.5),
        size=13, bold=True, colore=ROSSO)
    txt(s, marchio_nome, Inches(0.75), Inches(0.95), Inches(11.9), Inches(0.9), size=31, bold=True)
    txt(s, "THE CLAIM", Inches(0.78), Inches(2.05), Inches(5.6), Inches(0.4), size=12, bold=True, colore=BLU)
    txt(s, claim, Inches(0.78), Inches(2.5), Inches(5.6), Inches(2.4), size=16, interlinea=1.25)
    txt(s, "WHAT IT ACTUALLY DOES", Inches(6.9), Inches(2.05), Inches(5.7), Inches(0.4),
        size=12, bold=True, colore=ROSSO)
    txt(s, realta, Inches(6.9), Inches(2.5), Inches(5.7), Inches(2.4), size=16, interlinea=1.25)
    txt(s, prova, Inches(0.78), Inches(5.2), Inches(11.8), Inches(1), size=15, bold=True, colore=VERDE,
        interlinea=1.2)
    if nota:
        txt(s, nota, Inches(0.78), H - Inches(1.1), Inches(11.2), Inches(0.6), size=11, colore=GRIGIO)
    marchio(s)
    return s


def slide_contatti():
    s = prs.slides.add_slide(VUOTA); fondo(s, NAVY_SCURO); barra(s)
    txt(s, "Contribute", Inches(0.75), Inches(0.5), Inches(11.9), Inches(0.9), size=33, bold=True)
    txt(s, "The measurement is done. The hard part is what follows.",
        Inches(0.78), Inches(1.35), Inches(11.8), Inches(0.5), size=16, colore=BLU)
    voci = [
        (P_QR_TG, "Telegram", "t.me/+Ot-M_g0dkh1kMGI0", "Join the community"),
        (P_QR_OSS, "Observatory", "osservatorio.mxmap.it", "Papers, briefs, roadmap"),
        (P_QR_GH, "GitHub", "github.com/mxmap-it", "Software, data, issues"),
    ]
    for i, (png, nome, url, sotto) in enumerate(voci):
        x = Inches(0.9 + i * 4.15)
        s.shapes.add_picture(png, x, Inches(2.15), Inches(2.0), Inches(2.0))
        txt(s, nome, x, Inches(4.3), Inches(3.6), Inches(0.5), size=19, bold=True)
        txt(s, url, x, Inches(4.75), Inches(3.9), Inches(0.5), size=13, colore=BLU)
        txt(s, sotto, x, Inches(5.15), Inches(3.6), Inches(0.5), size=12, colore=GRIGIO)
    txt(s, "Technical · Legal · Political · Dissemination — every one of them is a blocker today.",
        Inches(0.78), Inches(6.1), Inches(11.8), Inches(0.6), size=15, bold=True)
    txt(s, "Fabio Pietrosanti (naif) — fabio@pietrosanti.it — Hermes Center · onData · Copernicani",
        Inches(0.78), Inches(6.65), Inches(11.8), Inches(0.5), size=12, colore=GRIGIO)
    return s


# --------------------------------------------------------------------------- costruzione
os.makedirs(TMP, exist_ok=True)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
P_SIMBOLO = os.path.join(TMP, "simbolo.png")
P_QR_TG = os.path.join(TMP, "qr-telegram.png")
P_QR_OSS = os.path.join(TMP, "qr-osservatorio.png")
P_QR_GH = os.path.join(TMP, "qr-github.png")
simbolo(P_SIMBOLO)
qr(P_QR_TG, "https://t.me/+Ot-M_g0dkh1kMGI0")
qr(P_QR_OSS, "https://osservatorio.mxmap.it")
qr(P_QR_GH, "https://github.com/mxmap-it")

pct = lambda k: "%.1f%%" % S[k]["pct"]
n = lambda k: "{:,}".format(S[k]["count"]).replace(",", ".")

slide_titolo(
    "MXMap Italia",
    "National Observatory for Digital Sovereignty",
    "Fabio Pietrosanti (naif)  ·  RomHack Camp 2026  ·  2 October, STAGE 2\n"
    "Hermes Center for Transparency and Digital Human Rights",
)

slide("Who is speaking, and why this exists",
      ["**Fabio Pietrosanti (naif)** — hacking since '95, security since 2000. "
       "Co-founder of Hermes Center; built GlobaLeaks.",
       "",
       "This project started from one question nobody had answered with data: **who actually "
       "operates the digital infrastructure of the Italian state?**",
       "",
       "Not who owns the building. Not where the disk sits. Who holds the keys, the control "
       "plane, and the legal obligation to comply when a foreign authority asks."],
      occhiello="The premise")

slide("The next decade, and why this is built to last",
      ["**Measure, permanently.** Not a study that ages. An instrument that re-runs itself and "
       "publishes the result, every month, with the method public so anyone can redo or dispute it.",
       "**Cover the money, not just the machines.** Who operates the infrastructure is half the "
       "answer. The other half is how much public money buys it, and whose jurisdiction it lands in.",
       "**Report annually, as political action.** A national account of digital sovereignty, "
       "generated from the data, presented where decisions are made.",
       "**Hand it over.** Open data, open source, open method — so the counting survives us and "
       "can be rebuilt in any other European country."],
      occhiello="Here to stay")

# ---- 1. metodo
slide_sezione("01", "The method", "Where the numbers come from, and why you can trust them")

slide("This is not our idea. It is upstream research.",
      ["**MXmap** — David Huser, mapping how Swiss municipalities host their email and how deeply "
       "their DNS is tied to US hyperscalers. Live at mxmap.ch.",
       "**SecAssure 2026** — the project grew into a team research effort covering **~15,300 "
       "municipalities** in Germany, Austria and Switzerland.",
       "   Paper: papers.mxmap-project.org/secassure2026.pdf (accepted manuscript)",
       "   Site: secassure2026.mxmap-project.org  ·  Code: github.com/mxmap/secassure2026",
       "",
       "**MXMap Italia is the Italian adaptation of that work** — same method, same code lineage, "
       "a different country and a much larger set of public bodies."],
      occhiello="Credit where it belongs",
      nota="We follow upstream rather than fork it: fixes produced by that community reach us instead of ageing in a private copy.")

slide("How the measurement actually works",
      ["**Stage 1 — resolve domains.** Enumerate public bodies from IndicePA, reconcile with other "
       "sources, verify candidate domains with MX lookups, score source agreement.",
       "**Stage 2 — classify providers.** For every domain, resolve all MX hosts, pattern-match, "
       "then run concurrent probes: **SPF, DKIM, DMARC, Autodiscover, CNAME chain, SMTP banner, "
       "tenant lookup, ASN, TXT verification, SPF IP ranges**.",
       "**Weighted evidence → confidence score 0–100.** A gateway appliance in front of Microsoft "
       "is not Microsoft; a self-hosted server whose DKIM points to Google is Google. The look-through "
       "is the hard part, and it is where naive scans get it wrong.",
       "",
       "Everything is public DNS. No intrusion, no authentication, no scraping of private systems."],
      occhiello="Technical core", size=17)

# ---- 2. risultati
slide("Ongoing: following the money, not just the machines",
      ["Knowing **who operates** the infrastructure is half the answer. The other half is "
       "**how much public money buys it, and whose jurisdiction it lands in.**",
       "",
       "We are building the second instrument: Italian public spending on cloud services, "
       "**year by year**, split between providers under US control and providers in Italy and "
       "Europe — automated and re-run like the DNS measurement, on open procurement data.",
       "",
       "**The sharpest test case is «Cloud Italia» and the PNRR migration funds**, allocated to move "
       "public administration onto infrastructure officially described as sovereign. Public money, "
       "a public sovereignty claim, and an outcome nobody has yet measured in euros.",
       "",
       "Status: prototype running, classifier not yet trained, data to be completed via transparency "
       "portals and freedom-of-information requests. We are saying it out loud because that is the "
       "state it is in."],
      occhiello="In progress — the missing half", size=16,
      nota="Every figure will ship with its method, as the DNS measurement does: reproducible or it does not count.")

slide_sezione("02", "The results", "22,987 Italian public bodies, 97% coverage")

slide_numeri("Who operates the email of the Italian state",
             [(pct("extra_eu"), "under non-EU jurisdiction\n(CLOUD Act reachable)\n%s bodies" % n("extra_eu"), ROSSO),
              (pct("it"), "Italian providers\n%s bodies" % n("it"), VERDE),
              (pct("eu_non_it"), "European providers\noutside Italy\n%s bodies" % n("eu_non_it"), BLU),
              (pct("unknown"), "unclassified\n%s bodies" % n("unknown"), GRIGIO)],
             nota="Source: mxmap.it on IndicePA data · %d bodies, %.2f%% coverage · snapshot %s · CC BY-SA 4.0"
                  % (T["n_entities"], T["coverage_pct"], K["generated_at"][:10]))

slide("Which companies, concretely",
      ["**Google Workspace — %s of public bodies (%s)**" % ("%.1f%%" % PROV["Google Workspace"]["pct"],
                                                            "{:,}".format(PROV["Google Workspace"]["count"]).replace(",", ".")),
       "**Microsoft 365 — %s (%s)**" % ("%.1f%%" % PROV["Microsoft 365"]["pct"],
                                        "{:,}".format(PROV["Microsoft 365"]["count"]).replace(",", ".")),
       "Italian providers — %.1f%%   ·   self-run infrastructure — %.1f%%   ·   Italian cloud — %.1f%%"
       % (PROV["Provider Italiano"]["pct"], PROV["Infrastruttura autonoma"]["pct"], PROV["Cloud Italiano"]["pct"]),
       "",
       "**For email, the dependency has two names.** AWS appears on 7 bodies, Zoho on 2 — "
       "statistically irrelevant here.",
       "AWS and Oracle matter enormously elsewhere: in the national cloud programme. Different "
       "service, same jurisdiction problem."],
      occhiello="Top providers", size=18)

# ---- 3. diritto
slide_sezione("03", "Why jurisdiction beats geography", "The legal core, in four minutes")

slide("The CLOUD Act, in one sentence",
      ["A US provider must produce data in its **possession, custody or control** — "
       "**regardless of where that data is stored**. 18 U.S.C. §2713.",
       "",
       "**Storing data in Milan does not change who can be compelled to hand it over.** "
       "The obligation attaches to the company, not to the disk.",
       "",
       "Add **FISA 702** for foreign-intelligence collection, and gag orders that can forbid "
       "telling the customer it happened. The Italian body may never learn that it occurred.",
       "",
       "**GDPR Article 48** says a foreign order is not, by itself, a lawful basis for transfer. "
       "That is a genuine conflict of laws — and the provider sits on both sides of it."],
      occhiello="Legal", size=18,
      nota="This is why the map classifies by jurisdiction of the operator, not by datacentre location.")

slide("FISA Section 702 — the part that fits us exactly",
      ["The CLOUD Act is about stored records in criminal process. **Section 702 is about "
       "foreign intelligence**, and its scope is the uncomfortable one for us.",
       "",
       "**It targets non-US persons reasonably believed to be located outside the United States.** "
       "An Italian municipality, its staff and its citizens are precisely that category — not an "
       "edge case, the intended one.",
       "",
       "It compels **US electronic communication service providers** to assist. There is no "
       "individual warrant naming your city council: collection runs under programmatic "
       "certifications, with directives to the provider.",
       "",
       "**And the provider may be barred from telling you.** The absence of a notification is not "
       "evidence that nothing happened."],
      occhiello="Legal — the second instrument", size=17)

slide("What Microsoft said under oath",
      ["In June 2025, before a French Senate committee, Microsoft's representative was asked "
       "whether the company could guarantee that data held in its sovereign French cloud would "
       "never be handed to US authorities.",
       "",
       "**«Non posso garantirlo.»  —  I cannot guarantee it.**",
       "",
       "That is not an activist's claim. It is sworn testimony from the vendor, and it is the "
       "shortest available summary of everything on the previous slide."],
      occhiello="The admission", size=19)

# ---- 4. geopolitica
slide_sezione("04", "The geopolitical layer", "Dependency is not a technical property. It is leverage.")

slide("Why this is a security question, not a procurement one",
      ["**Dependency is leverage.** Infrastructure a foreign executive can throttle, price, "
       "deprecate or condition is a policy instrument pointed at you — whoever currently holds it "
       "and however friendly they are today.",
       "**Europe wrote the rule, then removed it.** The EU cloud certification scheme (EUCS) once "
       "carried immunity-from-extraterritorial-law criteria at its highest level. They were dropped "
       "in 2024 — and Italy was among the states that did not defend them.",
       "**Someone did write it down.** France's SecNumCloud requires the provider to be established "
       "in the EU, to be under European capital control, and to be administered from the EU. "
       "Three conditions, verifiable, pass or fail.",
       "**And private buyers act on it.** Airbus, which asked the EU for that criterion, then used "
       "it in its own tender and moved critical applications to a European provider."],
      occhiello="Geopolitics", size=17)

# ---- 5. cybersecurity
slide("France wrote it down: SecNumCloud 3.2",
      ["ANSSI's qualification referential does something no Italian document does: it states "
       "**conditions on the provider itself**, not on the technology.",
       "",
       "**Establishment in the European Union.**",
       "**European capital control** — a cap on non-EU holdings.",
       "**Administration and operation of the service from the EU.**",
       "",
       "Three requirements. Verifiable. A provider either satisfies them or does not — there is no "
       "configuration that makes a non-compliant company compliant.",
       "",
       "**This matters beyond France.** It is the template the European debate keeps returning to, "
       "and the reference point for the Cloud and AI Development Act now under discussion, whose "
       "highest levels would require that no third country hold effective control over design, "
       "development and maintenance."],
      occhiello="The measure that actually measures", size=16)

slide("EUCS High+: the criterion Europe wrote, then dropped",
      ["The European cloud certification scheme once carried immunity from extraterritorial law at "
       "its highest level. **It was removed in 2024.**",
       "",
       "An open letter asked the Union to restore a criterion protecting the most sensitive data "
       "**«from access or operational disruption arising from non-European extraterritorial laws»**. "
       "**62 organisations** signed. The campaign site declares it is run by Airbus's Brussels office.",
       "",
       "**Five Italian signatories: Leonardo · Fincantieri · Generali · Telecom Italia · Aruba.**",
       "",
       "**Read that against the previous section.** Leonardo and TIM are two of the four companies "
       "that hold the national cloud concession. The same names asking Europe for immunity criteria "
       "are inside the programme that does not impose them."],
      occhiello="The letter, and who signed it", size=16,
      nota="Airbus later applied the criterion in its own tender and moved critical applications to a European provider.")

slide_sezione("05", "Why it belongs at a security conference", "Threat models, not slogans")

slide("The cybersecurity case",
      ["**Lawful access is a threat model.** If your adversary model excludes the operator and the "
       "state that can compel it, your model is incomplete — and for a public body it is the one "
       "actor able to obtain everything, silently and legally.",
       "**Concentration is systemic risk.** Two vendors carry %.0f%% of Italian public email. "
       "A single outage, breach or policy change propagates across the whole state at once."
       % (PROV["Google Workspace"]["pct"] + PROV["Microsoft 365"]["pct"]),
       "**You cannot do incident response on what you cannot see.** Logs, retention and forensic "
       "access are set by contract; the responder's authority ends where the provider's console begins.",
       "**Supply chain and NIS2.** Public bodies must assess supplier risk. Jurisdiction of the "
       "operator is a supplier risk — and today it is absent from almost every Italian risk assessment.",
       "**This map is free reconnaissance — for everyone.** It is public DNS: attackers already "
       "have it. The only question is whether defenders do."],
      occhiello="Relevance", size=16)

# ---- 6. PSN
slide_sezione("06", "Sovereignty washing", "One slide each — the arguments used on technicians and decision makers")

slide("How the trick works, before the examples",
      ["Every one of these measures is **real engineering**. None of them is fake. That is exactly "
       "what makes the move effective.",
       "",
       "The sleight of hand is always the same: **a genuine technical control is offered as an "
       "answer to a legal question.**",
       "",
       "Encryption, key custody, enclaves and policy constraints change *how hard* it is to reach "
       "the data. **They do not change who is legally obliged to try when compelled.** "
       "A company subject to US law remains subject to US law after you enable the feature."],
      occhiello="The pattern", size=19)

slide_washing(
    "Microsoft",
    ["EU Data Boundary — data stays in Europe.",
     "Customer Lockbox and approval workflows.",
     "«Sovereign Cloud», operated with local partners.",
     "Customer-managed keys."],
    ["Residency ≠ jurisdiction: §2713 follows the company.",
     "Lockbox governs support access, not legal process.",
     "Partner operation leaves the control plane and the software with Microsoft.",
     "Keys held in the same legal estate can be compelled."],
    "Their own witness, under oath, June 2025: «I cannot guarantee it.»",
    nota="18.3% of Italian public bodies — 4,203 — run their official email on Microsoft 365.")

slide_washing(
    "Google",
    ["Assured Workloads — sovereignty controls.",
     "Sovereign Controls «by Partners», operated locally.",
     "Key Access Justifications: you see, and can deny, every key access request.",
     "Data residency and personnel-location policies."],
    ["Assured Workloads is a set of organisation policy constraints — real, but configuration, not immunity.",
     "The partner operates; Google still supplies and controls the platform.",
     "KAJ is the strongest control on this slide — and it governs the technical path, not a court order to the parent.",
     "Residency again answers the wrong question."],
    "The most honest of the four — and still not a jurisdictional answer.",
    nota="27.7% of Italian public bodies — 6,374 — run their official email on Google Workspace. The largest single dependency.")

slide_washing(
    "Amazon Web Services",
    ["European Sovereign Cloud, a separate EU entity with EU staff.",
     "Nitro System: «AWS operators cannot access customer data.»",
     "Nitro Enclaves for isolated processing.",
     "External key management, audited by third parties."],
    ["The German entity is 100% owned by A100 ROW, Inc., Wilmington, Delaware — we have the notarised shareholder list.",
     "Nitro System and Nitro Enclaves are different things; the System-level claim is regularly answered with Enclaves documentation.",
     "Corporate separation inside the same ultimate parent does not create legal separation.",
     "Audits verify the mechanism works as described — not that the company is beyond reach."],
    "Ownership chain, from the notarised German commercial register: sole shareholder, 100%, Delaware.",
    nota="Marginal for email (7 bodies) — central in the national cloud programme.")

slide_washing(
    "Oracle",
    ["Alloy — a cloud region you operate yourself.",
     "Operator Access Control: the customer approves operator sessions.",
     "Exadata Cloud@Customer — hardware on your own premises.",
     "«Your realm, your control plane.»"],
    ["The realm runs Oracle's software and depends on Oracle for updates and lifecycle.",
     "Approval covers routine operator sessions, not the vendor's legal obligations.",
     "Hardware on-premises still runs a stack you do not control and cannot fork.",
     "In the PSN catalogue, not all services sit in PSN datacentres — some remain the vendor's."],
    "Physical location is the most persuasive illusion of the four, and the least relevant.",
    nota="Also relevant: none of these vendors accepts the three SecNumCloud requirements.")

slide("Now the measures themselves, one at a time",
      ["The four vendors reuse the same handful of controls. Judge each on what it actually does.",
       "",
       "**Every one of them is real. None of them answers the jurisdictional question.**"],
      occhiello="From vendors to mechanisms", size=20)

slide_washing(
    "Measure 1 — Data residency",
    ["«Your data never leaves the European Union.»",
     "EU Data Boundary, EU regions, in-region processing and storage commitments."],
    ["Answers a geographic question nobody asked.",
     "18 U.S.C. §2713 attaches to the company's possession, custody or control — not to the "
     "location of the disk.",
     "A US provider with data in Milan is still a US provider served with a US order."],
    "Residency is necessary for other reasons. It is not sovereignty, and it never was.")

slide_washing(
    "Measure 2 — Customer-managed keys (BYOK / HYOK / EKM)",
    ["«You hold the keys. We cannot read your data without them.»",
     "External key stores, hold-your-own-key, key access logging and revocation."],
    ["Better than provider-managed keys — genuinely.",
     "But data must be decrypted to be processed, and processing happens on their silicon, in "
     "their memory, under their control plane.",
     "If the key store sits in the same legal estate, it is reachable by the same order.",
     "Revocation is a kill switch, not a shield: it protects future access, not the session in flight."],
    "Key custody moves the problem. It does not remove the party able to be compelled.")

slide_washing(
    "Measure 3 — Confidential computing",
    ["«The operator cannot read your data, even in memory.»",
     "Hardware enclaves — Intel TDX, AMD SEV-SNP — with remote attestation.",
     "Microsoft ships a whole Confidential tier on this basis; the PSN catalogue sells it as "
     "sovereignty."],
    ["The strongest measure on offer, and still not an answer.",
     "ANSSI's technical position is explicit that it does not remove exposure to extraterritorial "
     "jurisdiction.",
     "It protects against the operator reading RAM. It does not govern the control plane, the "
     "attestation service, the images you are allowed to run, or a court order to the parent.",
     "And note the wording: enclaves do NOT «process encrypted data». Inside the enclave the data "
     "is plaintext to the CPU; the memory around it is encrypted."],
    "Protecting data from the operator is not the same as protecting it from the operator's government.",
    nota="Homomorphic encryption and MPC genuinely compute on ciphertext — and are not what these products ship for general workloads.")

slide_washing(
    "Measure 4 — Operator access control",
    ["«No engineer touches your data without your approval.»",
     "Customer Lockbox, Operator Access Control, just-in-time access, approval workflows, "
     "session recording."],
    ["Governs routine support access by employees.",
     "Legal process does not arrive as a support ticket, and is not presented to you for approval.",
     "Where a gag order applies, the mechanism that would have shown you the access is precisely "
     "the one that stays silent."],
    "It is an insider-risk control. It was never a legal-process control.")

slide_washing(
    "Measure 5 — The locally operated «sovereign partner»",
    ["«The service is run by a local, trusted operator, with local staff.»",
     "Sovereign Controls by Partners, national partner clouds, delegated operations."],
    ["The partner operates. The vendor still supplies the platform, the updates, the roadmap and "
     "the code.",
     "Operational delegation is not ownership: you cannot fork it, audit it fully, or run it if "
     "the supplier stops.",
     "The dependency has been made harder to see, not smaller."],
    "Ask who can switch it off, not who logs in daily.")

slide_washing(
    "Measure 6 — A separate European legal entity",
    ["«A European company, European staff, European governance.»",
     "Dedicated EU subsidiaries for sovereign cloud offerings."],
    ["Corporate separation inside the same ultimate parent is not legal separation.",
     "AWS European Sovereign Cloud GmbH: the notarised German shareholder list shows a single "
     "shareholder at 100% — A100 ROW, Inc., Wilmington, Delaware.",
     "The structure is real. The question is what the parent can be compelled to do with what it "
     "controls."],
    "We read the notarised register so the claim does not rest on anyone's press release.")

slide("And this is where the national cloud programme lands",
      ["**PSN — Polo Strategico Nazionale.** Italy's answer: consolidate public administration onto "
       "a national strategic hub. The concession is held by a consortium of four Italian companies "
       "— **CDP Equity, TIM (lead), Sogei and Leonardo**.",
       "",
       "**Give it its due.** AgID found 95% of the public server rooms it surveyed deficient in "
       "security and reliability. Consolidating them was necessary and long overdue, and the "
       "programme genuinely improves on the basement datacentre.",
       "",
       "**But on sovereignty it is as far from the goal as it gets.** The cloud services sold "
       "through it are Microsoft, Google, AWS and Oracle — resold by Italian companies with no "
       "sovereignty leverage over any of them, reportedly on intermediation-level margins.",
       "",
       "**«Sovereignty» appears 31 times in the commercial documents and 0 times in the 86 pages "
       "of the concession and technical specifications.** None of SecNumCloud's three requirements "
       "is imposed on any supplier."],
      occhiello="The Italian case, in one slide", size=15,
      nota="We do not argue against the programme's stated goal. We ask that it be held to it.")

slide("What we are asking public bodies to do",
      ["**Know your own position.** Every body has a page on mxmap.it. Most have never looked.",
       "**Put jurisdiction in the risk assessment.** It is a supplier risk under NIS2, and it is "
       "almost universally missing.",
       "**Write it into the tender.** The instrument that reaches a foreign provider is not "
       "sanctions or golden power — it is the procurement requirement. France proved it can be drafted.",
       "**Self-hosting and free software are a real option** for a large share of these workloads, "
       "and 13.5% of Italian bodies already do it."],
      occhiello="Actionable", size=18)

slide_contatti()

# se il deck e' aperto in PowerPoint il file e' bloccato: si salva accanto,
# invece di perdere il lavoro
destinazione = OUT
try:
    prs.save(destinazione)
except PermissionError:
    import datetime
    base, est = os.path.splitext(OUT)
    destinazione = "%s-%s%s" % (base, datetime.datetime.now().strftime("%H%M"), est)
    prs.save(destinazione)
    print("(l'originale era aperto in PowerPoint: salvato accanto)")
print("%s  |  %d slide  |  %d KB" % (os.path.relpath(destinazione, ROOT),
                                     len(prs.slides._sldIdLst),
                                     os.path.getsize(destinazione) // 1024))
