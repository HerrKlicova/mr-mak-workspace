"""Hoja de contacto de un bloque de Pixelab: una fila por nombre, una columna por variante, a x4 con filtro de punto.
Uso:  python hoja_contacto.py <bloque> [--tam 32]        (ej.: A2_alertas)
Lee las imágenes sin paleta de assets/pixelab/lote/_raw/<bloque>, las pasa por pixel_post.py (paleta de 32 y fondo quitado, sin gastar
generaciones) a assets/pixelab/faseA/final/<bloque> y escribe assets/pixelab/contacto/<bloque>.png (mismo formato que A1_cargas.png).
"""
import argparse
import os
import re
import subprocess
import sys
from collections import OrderedDict

from PIL import Image, ImageDraw

CARD = r"C:\Dev\mr-mak-workspace\workspace\2026-11-05_rts-zombi\assets"
RAW = os.path.join(CARD, "pixelab", "lote", "_raw")
FINAL = os.path.join(CARD, "pixelab", "faseA", "final")
CONTACTO = os.path.join(CARD, "pixelab", "contacto")
POST = os.path.join(CARD, "fase-a", "pixel_post.py")
PALETA = os.path.join(CARD, "fase-a", "paleta_propuesta_32.hex")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bloque")
    ap.add_argument("--zoom", type=int, default=4)
    a = ap.parse_args()
    raw = os.path.join(RAW, a.bloque)
    fin = os.path.join(FINAL, a.bloque)
    os.makedirs(fin, exist_ok=True)
    os.makedirs(CONTACTO, exist_ok=True)
    subprocess.run([sys.executable, POST, raw, fin, "--paleta", PALETA, "--quitar-fondo"], check=True, capture_output=True)
    filas = OrderedDict()
    pat = re.compile(r"vm_%s_(.+)_v(\d+)\.png$" % re.escape(a.bloque))
    for f in sorted(os.listdir(fin)):
        m = pat.match(f)
        if m:
            filas.setdefault(m.group(1), {})[int(m.group(2))] = os.path.join(fin, f)
    if not filas:
        print("sin imágenes en", fin)
        return
    vmax = max(max(v) for v in filas.values())
    tam = max(Image.open(p).width for v in filas.values() for p in v.values())
    z = a.zoom
    cell = tam * z + 8
    lab = 150
    W = lab + vmax * cell
    H = len(filas) * cell + 24
    sheet = Image.new("RGBA", (W, H), (40, 40, 44, 255))
    dr = ImageDraw.Draw(sheet)
    for v in range(vmax):
        dr.text((lab + v * cell + tam * z // 2 - 6, 6), "v%d" % (v + 1), fill=(220, 220, 220, 255))
    for r, (n, vs) in enumerate(filas.items()):
        dr.text((6, 24 + r * cell + cell // 2 - 6), n, fill=(220, 220, 220, 255))
        for v, p in vs.items():
            im = Image.open(p).convert("RGBA")
            im = im.resize((im.width * z, im.height * z), Image.NEAREST)
            sheet.alpha_composite(im, (lab + (v - 1) * cell + 4 + (tam * z - im.width) // 2, 24 + r * cell + 4 + (tam * z - im.height) // 2))
    out = os.path.join(CONTACTO, a.bloque + ".png")
    sheet.convert("RGB").save(out)
    print(out, sheet.size, sum(len(v) for v in filas.values()), "imágenes")


main()
