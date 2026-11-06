"""Pasa los brutos de ElevenLabs a retratos de 64 px con la regla de estética única.
Uso: python3 -I procesar_retratos.py <brutos> <salida>
Fondo fuera a resolución completa, reducción BOX a 64, y luego unificar (paleta de 32,
contorno de 1 px, motas, 16 colores). Hoja de contacto a x4 sobre #181c30."""
import sys
from pathlib import Path
from PIL import Image

SK = Path("/mnt/project-files/docs/arte/pixel-codigo/skill/scripts")
sys.path.insert(0, str(SK))
import unificar as U  # noqa: E402
from pixelvm import Sprite, check, contact_sheet  # noqa: E402

TOL = {"hugo": 34}


def fondo_por_relleno(im, tol):
    """Quita el fondo con un relleno desde los bordes (no por color global, que agujerea el pelo
    gris). El color de fondo es la mediana de la fila superior."""
    from collections import deque
    w, h = im.size
    px = im.load()
    fila = sorted(px[x, 0][:3] for x in range(w))
    bg = fila[len(fila) // 2]
    cerca = lambda p: max(abs(p[i] - bg[i]) for i in range(3)) <= tol
    vis = set()
    q = deque((x, y) for x in range(w) for y in (0,) if cerca(px[x, y]))
    q.extend((x, y) for x in (0, w - 1) for y in range(h) if cerca(px[x, y]))
    while q:
        x, y = q.popleft()
        if (x, y) in vis:
            continue
        vis.add((x, y))
        px[x, y] = (0, 0, 0, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in vis and px[nx, ny][3] and cerca(px[nx, ny]):
                q.append((nx, ny))
    return im


ORDEN = ["mak", "lucia", "marcos", "nacho", "iris", "hugo", "sara", "elena", "bruno", "teo", "paula"]


def main():
    ent, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    tam = int(sys.argv[3]) if len(sys.argv) > 3 else 64
    hechos = []
    for m in ORDEN:
        f = next(iter(sorted(ent.glob(f"bruto_{m}.*"))), None)
        if not f:
            continue
        im = fondo_por_relleno(Image.open(f).convert("RGBA").resize((256, 256), Image.BOX), TOL.get(m, 26))
        im = im.resize((tam, tam), Image.BOX)
        s = U.unificar(im, tam, False, 20, 40, 16)
        s.save(out / f"retrato_{m}_{tam}.png")
        s.img.resize((tam * 4, tam * 4), Image.NEAREST).save(out / f"retrato_{m}_{tam}_x4.png")
        print(m, check(s, max_colores=16) or "OK")
        hechos.append((m, s))
    filas = [[s for _, s in hechos[k:k + 6]] for k in range(0, len(hechos), 6)]
    if filas:
        contact_sheet(filas, out / f"contacto_equipo_{tam}.png", scale=4)


if __name__ == "__main__":
    main()
