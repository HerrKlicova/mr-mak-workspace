"""Botón principal del parte, opción C de Lucía (7-nov 07:39). Bruno (Arte técnico).

Problema (QA15/QA20): el botón principal del parte usa ui_boton_encima (placa olive 70784c) y el texto en hueso
solo da 3,1:1; en la build, con el fallo de espacio de color, «Seguir» y «Volver a empezar» casi no se leen.
Opción C: el principal usa la placa de ui_boton_normal (50541c, hueso encima 5,2:1) y se marca como el estado
«encima» del menú (retoque D de la D-N115): borde en crema f0dc9c y la cuña crema a la izquierda.
Piezas nuevas (no se toca ninguna de las que ya hay, ui_boton_* sigue igual para el panel de órdenes):
- ui_boton_principal (48x16, 9-slice 4,4,4,4): ui_boton_normal con el borde exterior en crema.
- ui_boton_cuna (4x7): la cuña, pieza aparte para que no se estire con el 9-slice; va en (x + 4, y + h/2 - 3).

Uso: python build_parte_boton.py <carpeta>
"""
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_uidemo_referencia as ur  # noqa: E402

CREMA = (0xf0, 0xdc, 0x9c, 255)


def principal():
    im = ur.tex("ui_boton_normal").copy(); px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            if px[x, y][3] and px[x, y][:3] == (0x48, 0x40, 0x3c):
                px[x, y] = CREMA
    return im


def cuna():
    im = Image.new("RGBA", (4, 7), (0, 0, 0, 0)); px = im.load()
    for k in range(4):
        for j in range(k, 7 - k):
            px[k, j] = CREMA
    return im


def parte_c(L, p):
    """ur.parte con el botón principal nuevo."""
    orig = ur.Lienzo.slice

    def sl(self, n, x, y, w, h, nf=1, f=0):
        if n == "ui_boton_encima" and h == 18:
            orig(self, "ui_boton_principal", x, y, w, h)
            self.pieza("ui_boton_cuna", x + 4, y + h / 2 - 3)
        else:
            orig(self, n, x, y, w, h, nf, f)
    ur.Lienzo.slice = sl
    try:
        ur.parte(L, p)
    finally:
        ur.Lienzo.slice = orig


def contraste(a, b):
    def L(c):
        r = [(v / 255) / 12.92 if v / 255 <= .03928 else ((v / 255 + .055) / 1.055) ** 2.4 for v in c[:3]]
        return .2126 * r[0] + .7152 * r[1] + .0722 * r[2]
    la, lb = L(a), L(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def main(out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    ur._cache["ui_boton_principal"] = principal(); ur._cache["ui_boton_cuna"] = cuna()
    principal().save(out / "ui_boton_principal.png"); cuna().save(out / "ui_boton_cuna.png")
    capt = {}
    for nombre, vic in (("victoria", True), ("derrota", False)):
        p = dict(ur.PARTE, victoria=vic)
        for v, f in (("actual", ur.parte), ("C", parte_c)):
            L = ur.Lienzo(); ur.hud(L); f(L, p); im = L.final()
            capt[(nombre, v)] = im
            im.save(out / f"parte_{nombre}_{v}_1080.png")
    # hoja: recorte de la zona de botones x3 (base 640 -> 1080), actual arriba y C abajo
    cajas = {"victoria": (140 * 3, 270 * 3, 500 * 3, 304 * 3), "derrota": (140 * 3, 246 * 3, 500 * 3, 280 * 3)}
    w, h = 360 * 3, 34 * 3
    hoja = Image.new("RGB", (2 * w + 48, 2 * h + 48), (0x18, 0x1c, 0x30))
    for i, n in enumerate(("victoria", "derrota")):
        for j, v in enumerate(("actual", "C")):
            hoja.paste(capt[(n, v)].crop(cajas[n]).convert("RGB"), (16 + i * (w + 16), 16 + j * (h + 16)))
    hoja.save(out / "muestra_parte_boton_C.png")
    print("hueso sobre 50541c: %.1f:1 · hueso sobre 70784c: %.1f:1 · crema sobre panel 283440: %.1f:1" % (
        contraste((0xd4, 0xd0, 0xcc), (0x50, 0x54, 0x1c)), contraste((0xd4, 0xd0, 0xcc), (0x70, 0x78, 0x4c)),
        contraste(CREMA, (0x28, 0x34, 0x40))))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out_parte_boton")
