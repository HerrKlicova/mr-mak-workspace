"""Posproceso del lote de Pixelab (Iris, 5-nov-2026).

Uso:
    python pixel_post.py <entrada.png|carpeta> <salida_carpeta> [--paleta paleta_propuesta_32.hex] [--quitar-fondo] [--tol 24]

1. Quitar fondo (opcional): si la imagen no trae transparencia, toma el color de
   las 4 esquinas como fondo y lo vuelve transparente (tolerancia --tol).
2. Reducir a la paleta: cada píxel opaco pasa al color más cercano de la paleta
   (distancia euclídea en RGB). La alfa se binariza (>=128 opaco), como pide el
   pixel art con filtro de punto.
No genera nada ni gasta generaciones. Requiere Pillow.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image


def leer_paleta(ruta):
    cols = []
    for linea in Path(ruta).read_text().split():
        linea = linea.strip().lstrip("#")
        if len(linea) == 6:
            cols.append(tuple(int(linea[i:i + 2], 16) for i in (0, 2, 4)))
    if not cols:
        sys.exit(f"Paleta vacía: {ruta}")
    return cols


def mas_cercano(c, paleta, cache):
    if c in cache:
        return cache[c]
    r, g, b = c
    mejor = min(paleta, key=lambda p: (p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2)
    cache[c] = mejor
    return mejor


def procesar(img, paleta, quitar_fondo, tol):
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()
    fondo = None
    if quitar_fondo:
        alfas = [px[x, y][3] for x in range(w) for y in range(h)]
        if min(alfas) == 255:  # sin transparencia: usar el color de las esquinas
            esquinas = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
            fondo = max(set(esquinas), key=esquinas.count)[:3]
    cache = {}
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if fondo and sum((u - v) ** 2 for u, v in zip((r, g, b), fondo)) <= tol * tol * 3:
                a = 0
            if a < 128:
                px[x, y] = (0, 0, 0, 0)
            else:
                px[x, y] = (*mas_cercano((r, g, b), paleta, cache), 255)
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("salida")
    ap.add_argument("--paleta", default=str(Path(__file__).resolve().parent.parent / "paleta_propuesta_32.hex"))
    ap.add_argument("--quitar-fondo", action="store_true")
    ap.add_argument("--tol", type=int, default=24)
    a = ap.parse_args()
    paleta = leer_paleta(a.paleta)
    ent = Path(a.entrada)
    archivos = sorted(ent.glob("*.png")) if ent.is_dir() else [ent]
    out = Path(a.salida)
    out.mkdir(parents=True, exist_ok=True)
    for f in archivos:
        procesar(Image.open(f), paleta, a.quitar_fondo, a.tol).save(out / f.name)
        print(f"ok {f.name}")


if __name__ == "__main__":
    main()
