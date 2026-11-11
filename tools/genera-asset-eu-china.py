#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera gli asset grafici dell'Europe–China Digital Commons Observatory per le
slide: il marchio e il QR del sito.

Il marchio è ridisegnato con PIL seguendo la geometria esatta di
site/assets/logo.svg del progetto eu-china-digital-commons (viewBox 120×80:
due cerchi r=30 in (44,40) e (76,40), la lente di intersezione piena, una
piccola rete bianca al centro). Si ridisegna invece di convertire l'SVG perché
cairosvg qui non ha la libreria cairo, e un PNG con il fondo bianco starebbe
male sulle slide scure.

Uscita:  static/slide/_assets/eu-china-commons-mark.png   (fondo trasparente)
         static/slide/_assets/eu-china-commons-qr.png     (tessera bianca)

Uso:  python tools/genera-asset-eu-china.py
"""
import io
import os

import segno
from PIL import Image, ImageChops, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(ROOT, "static", "slide", "_assets")

SITO = "https://eu-china-commons.eu/"

BLU_UE = (0x1F, 0x4F, 0xA3, 255)
ROSSO_CN = (0xB8, 0x32, 0x2A, 255)
VIOLA = (0x6B, 0x4F, 0xA3, 255)
BIANCO = (0xFF, 0xFF, 0xFF, 255)


def marchio(scala=24):
    """Ridisegna il marchio dell'osservatorio. `scala` = pixel per unità SVG."""
    s = scala * 2  # si disegna al doppio e si riduce: bordi puliti
    larghezza, altezza = 120 * s, 80 * s

    def cerchio(cx, cy, r):
        return [(cx - r) * s, (cy - r) * s, (cx + r) * s, (cy + r) * s]

    ue, cn = cerchio(44, 40, 30), cerchio(76, 40, 30)

    # la lente: intersezione dei due dischi, ottenuta con due maschere
    def disco(box):
        m = Image.new("L", (larghezza, altezza), 0)
        ImageDraw.Draw(m).ellipse(box, fill=255)
        return m

    lente = ImageChops.darker(disco(ue), disco(cn))

    img = Image.new("RGBA", (larghezza, altezza), (0, 0, 0, 0))
    img.paste(Image.new("RGBA", img.size, VIOLA), (0, 0), lente)

    d = ImageDraw.Draw(img)
    spessore = int(7 * s)
    # prima il rosso, poi il blu: così in alto il cerchio UE passa sopra,
    # come nell'SVG (dove un arco blu è ridisegnato sopra il rosso)
    d.ellipse(cn, outline=ROSSO_CN, width=spessore)
    d.ellipse(ue, outline=BLU_UE, width=spessore)

    # la rete condivisa, al centro della lente
    d.line([60 * s, 27 * s, 60 * s, 53 * s], fill=BIANCO, width=int(2 * s))
    for cy, r in ((27, 3.2), (40, 4.0), (53, 3.2)):
        d.ellipse(cerchio(60, cy, r), fill=BIANCO)

    return img.resize((120 * scala, 80 * scala), Image.LANCZOS)


def qr(lato=720, margine=28):
    """QR del sito su tessera bianca: scuro su chiaro, il verso che si legge."""
    codice = segno.make(SITO, error="h")
    buf = io.BytesIO()
    codice.save(buf, kind="png", scale=20, border=0)
    buf.seek(0)
    grezzo = Image.open(buf).convert("RGBA")
    utile = lato - 2 * margine
    grezzo = grezzo.resize((utile, utile), Image.NEAREST)
    tessera = Image.new("RGBA", (lato, lato), BIANCO)
    tessera.paste(grezzo, (margine, margine))
    return tessera


def main():
    os.makedirs(USCITA, exist_ok=True)
    for nome, immagine in (("eu-china-commons-mark.png", marchio()),
                           ("eu-china-commons-qr.png", qr())):
        percorso = os.path.join(USCITA, nome)
        immagine.save(percorso)
        print("%s  |  %dx%d  |  %d KB"
              % (os.path.relpath(percorso, ROOT), immagine.width, immagine.height,
                 os.path.getsize(percorso) // 1024))


if __name__ == "__main__":
    main()
