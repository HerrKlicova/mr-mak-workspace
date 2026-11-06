"""Monta un GIF a partir de la carpeta de fotogramas que graba el prototipo (F10 en el juego).

Uso:  python hacer_gif.py <carpeta_fotogramas> <salida.gif> [--escala 1] [--fps 15] [--max-fotogramas 240]

- Los fotogramas del juego ya son la imagen final a mitad de tamaño; --escala 2 amplía con vecino más cercano (sin suavizar).
- El GIF usa una paleta de 64 colores calculada por cuadro, así que el bloom y la gradación se ven aproximados.
- Solo para hitos importantes (primera escena funcionando, la horda apilándose...), por petición de Eugenio.
"""
import argparse
import glob
import os

from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("salida")
    ap.add_argument("--escala", type=int, default=1)
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--max-fotogramas", type=int, default=240)
    a = ap.parse_args()

    ficheros = sorted(glob.glob(os.path.join(a.carpeta, "f_*.png")))
    if not ficheros:
        raise SystemExit("No hay fotogramas f_*.png en " + a.carpeta)
    if len(ficheros) > a.max_fotogramas:
        paso = len(ficheros) / a.max_fotogramas
        ficheros = [ficheros[int(i * paso)] for i in range(a.max_fotogramas)]

    cuadros = []
    for f in ficheros:
        im = Image.open(f).convert("RGB")
        im = im.resize((im.width * a.escala, im.height * a.escala), Image.NEAREST)
        cuadros.append(im.convert("P", palette=Image.ADAPTIVE, colors=64))

    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    cuadros[0].save(a.salida, save_all=True, append_images=cuadros[1:], duration=int(1000 / a.fps), loop=0,
                    optimize=False, disposal=1)
    print("GIF: %s (%d fotogramas, %.1f MB)" % (a.salida, len(cuadros), os.path.getsize(a.salida) / 1e6))


if __name__ == "__main__":
    main()
