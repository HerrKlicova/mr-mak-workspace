"""Comprueba los colores de una captura de la build contra los valores exactos del kit UiNoche.

Uso:  python comprobar_color.py <captura.png> [hud|parte|menu]
La captura puede tener cualquier tamaño 16:9 (960x540, 1280x720, 1920x1080): las cajas están en la base
640x360 y se escalan. En cada caja se busca el color de fondo (el más repetido) y, si se pide, el color del
texto (que debe aparecer al menos en unos pocos píxeles). Tolerancia: ±3 por canal.
Bruno (Arte técnico), 07-11. Valores sacados de los PNG del kit y de UiNocheKit (Hueso, Crema, Beige...).
"""
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from collections import Counter

from PIL import Image

# (nombre, caja en base 640x360 (x, y, ancho, alto), fondo esperado, texto esperado o None)
PRUEBAS = {
    "hud": [
        ("placa del reloj", (292, 7, 56, 16), "181c30", "d4d0cc"),
        ("primer aviso (panel)", (34, 31, 160, 18), "181c30", "d4d0cc"),
        ("primera fila de frentes", (508, 31, 84, 14), "181c30", "d4d0cc"),
        ("panel de órdenes (fondo)", (508, 340, 8, 12), "181c30", None),
    ],
    "parte": [
        ("panel del parte (victoria)", (160, 150, 40, 40), "181c30", None),
        ("título «Amanece en Sagunto»", (250, 100, 140, 16), None, "f0dc9c"),
        ("etiquetas (Beige)", (186, 150, 80, 60), None, "b4a080"),
    ],
    "menu": [
        ("botón Jugar (retoque D)", (40, 123, 100, 14), "283440", "d4d0cc"),
        ("botón Continuar inactivo (retoque D)", (40, 149, 100, 14), "181c30", "6c7874"),
    ],
}


def _cerca(a, b, tol=3):
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def _hex(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def comprobar(ruta, grupo):
    im = Image.open(ruta).convert("RGB")
    k = im.width / 640
    ok_total = True
    for nombre, (x, y, w, h), fondo, texto in PRUEBAS[grupo]:
        caja = im.crop((round(x * k), round(y * k), round((x + w) * k), round((y + h) * k)))
        c = Counter(caja.getdata())
        dom = c.most_common(1)[0][0]
        linea = f"{nombre:42s} fondo {'%02x%02x%02x' % dom}"
        ok = True
        if fondo:
            bien = _cerca(dom, _hex(fondo))
            ok &= bien
            linea += f" (esperado {fondo}: {'OK' if bien else 'MAL'})"
        if texto:
            n = sum(v for col, v in c.items() if _cerca(col, _hex(texto)))
            bien = n >= 4
            ok &= bien
            linea += f" · texto {texto}: {n} px {'OK' if bien else 'MAL'}"
        ok_total &= ok
        print(linea)
    print("TODO BIEN" if ok_total else "HAY DIFERENCIAS")


if __name__ == "__main__":
    comprobar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "hud")
