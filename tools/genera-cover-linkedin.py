#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la copertina LinkedIn dell'Osservatorio riproducendo il marchio di
static/brand/osservatorio-logo-horizontal.svg.

Formato: 1128x654. Lo strumento di ritaglio delle Pagine LinkedIn usa un
riquadro con proporzioni ~1.73:1; una striscia 1128x191 vi entra lasciando due
larghe bande nere. Il marchio e' comunque centrato nella fascia mediana, cosi'
resta visibile anche quando LinkedIn mostra la copertina come banda bassa.

Il logo esiste solo in SVG e cairo non e' disponibile su questa macchina, quindi
il marchio viene ridisegnato con PIL dalle stesse primitive geometriche e dagli
stessi colori dell'SVG. Il font e' Segoe UI, primo fallback dello stack
dichiarato nel logo ("Titillium Web","Segoe UI",Tahoma): Titillium e' presente
nel progetto solo come woff2, che PIL non legge.

Uso:
    python tools/genera-cover-linkedin.py              # 1128x654
    python tools/genera-cover-linkedin.py --striscia   # anche 1128x191
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = os.path.join(ROOT, "static", "brand")

SS = 3                    # supersampling, per archi e testo puliti

NAVY = (23, 50, 77)       # #17324D  fondo
BLU = (0, 102, 204)       # #0066CC  primario
BLU_CHIARO = (109, 179, 255)
BIANCO = (255, 255, 255)
GRIGIO = (143, 163, 184)
VERDE, GRIGIO_IT, ROSSO = (0, 135, 88), (154, 166, 178), (206, 43, 55)

FONT_DIR = "C:/Windows/Fonts"
F_BOLD = os.path.join(FONT_DIR, "segoeuib.ttf")
F_REG = os.path.join(FONT_DIR, "segoeui.ttf")


def mix(fg, bg, a):
    """Simula l'opacita' dell'SVG fondendo il colore col fondo."""
    return tuple(round(f * a + b * (1 - a)) for f, b in zip(fg, bg))


def testo_spaziato(dr, xy, testo, font, fill, spaziatura, misura_soltanto=False):
    """PIL non ha letter-spacing: disegna (o misura) carattere per carattere."""
    x, y = xy
    for ch in testo:
        if not misura_soltanto:
            dr.text((x, y), ch, font=font, fill=fill)
        x += dr.textlength(ch, font=font) + spaziatura
    return x - xy[0] - spaziatura


def marchio(dr, cx, cy, scala):
    """Punto centrale, tre archi concentrici e barre tricolore.

    Coordinate prese dall'SVG (viewBox 0 0 68 68), centro logico (34, 40).
    """
    def P(x, y):
        return (cx + (x - 34) * scala, cy + (y - 40) * scala)

    for raggio, opacita in ((29, 0.30), (21, 0.60), (13, 1.0)):
        x0, y0 = P(34 - raggio, 40 - raggio)
        x1, y1 = P(34 + raggio, 40 + raggio)
        dr.arc([x0, y0, x1, y1], 180, 360,
               fill=mix(BLU_CHIARO, NAVY, opacita), width=max(1, round(3.4 * scala)))

    r = 5 * scala
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLU_CHIARO)

    for i, colore in enumerate((VERDE, GRIGIO_IT, ROSSO)):
        x0, y0 = P(20 + i * 9.5, 52)
        x1, y1 = P(20 + i * 9.5 + 9, 55)
        dr.rectangle([x0, y0, x1, y1], fill=colore)


def genera(W, H, nome):
    im = Image.new("RGB", (W * SS, H * SS), NAVY)
    dr = ImageDraw.Draw(im)

    # il lockup non scala con l'altezza della tela: resta dimensionato sulla
    # larghezza, cosi' e' identico nelle due varianti
    s_titolo = round(W * 0.030)
    s_kicker = round(W * 0.0115)
    s_url = round(W * 0.0142)
    f_titolo = ImageFont.truetype(F_BOLD, s_titolo * SS)
    f_kicker = ImageFont.truetype(F_REG, s_kicker * SS)
    f_url = ImageFont.truetype(F_REG, s_url * SS)

    riga1, riga2 = "Osservatorio Nazionale", "Sovranità Digitale"
    kicker = "MONITORAGGIO CIVICO · PA ITALIANA"
    sp_kicker = s_kicker * 0.17

    # larghezza del blocco testo e del marchio, per centrare l'insieme
    w_testo = max(dr.textlength(riga1, font=f_titolo), dr.textlength(riga2, font=f_titolo),
                  testo_spaziato(dr, (0, 0), kicker, f_kicker, None, sp_kicker * SS, True))
    scala_marchio = W * 0.00135 * SS
    w_marchio = 58 * scala_marchio
    gap = W * 0.032 * SS
    w_tot = w_marchio + gap + w_testo

    x0 = (W * SS - w_tot) / 2
    cy = H * SS / 2

    marchio(dr, x0 + w_marchio / 2, cy - 4 * SS, scala_marchio)

    xt = x0 + w_marchio + gap
    h_riga = s_titolo * 1.24 * SS
    y = cy - h_riga - 6 * SS
    dr.text((xt, y), riga1, font=f_titolo, fill=BIANCO)
    dr.text((xt, y + h_riga), riga2, font=f_titolo, fill=BLU_CHIARO)
    testo_spaziato(dr, (xt + 2 * SS, y + h_riga * 2 + 10 * SS), kicker, f_kicker, GRIGIO, sp_kicker * SS)

    # firma centrata sotto il lockup, a distanza proporzionale all'altezza
    url = "osservatorio.mxmap.it"
    w_url = dr.textlength(url, font=f_url)
    y_url = cy + (H * SS * 0.5 - s_url * 2.4 * SS) if H > 300 else cy + h_riga * 1.9
    dr.text(((W * SS - w_url) / 2, y_url), url, font=f_url, fill=GRIGIO)

    im = im.resize((W, H), Image.LANCZOS)
    out = os.path.join(BRAND, nome)
    os.makedirs(BRAND, exist_ok=True)
    im.save(out, "PNG", optimize=True)
    print("%-28s %4dx%-4d  %3d KB" % (nome, W, H, os.path.getsize(out) // 1024))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--striscia", action="store_true",
                    help="genera anche la variante 1128x191")
    a = ap.parse_args()
    genera(1128, 654, "linkedin-cover.png")
    if a.striscia:
        genera(1128, 191, "linkedin-cover-striscia.png")
