"""Previa del plano táctico del mapa de operaciones: el mismo cálculo que MapaTactico.cs, pasado a Python. Bruno, 8-nov.

Porta PlaceholderRelief (Relief.cs) y MapaTactico.Pintar para ver, sin Unity, cómo queda la vista a 2,5 km de Nules y a 230 km.
Uso: python3 previa_mapa_tactico.py <carpeta>
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

K = 3.5
NODOS = [("Sagunto", 53, 73), ("Puçol", 52, 75), ("Valencia", 50, 80), ("Almenara", 54, 71), ("Nules", 55, 68), ("Castellón", 58, 63),
         ("Segorbe", 47, 68), ("Barracas", 42, 62), ("Teruel", 33, 52), ("Caminreal", 27, 36), ("Calamocha", 28, 34), ("Cariñena", 30, 20),
         ("Zaragoza", 38, 10)]
ARISTAS = [(0, 1), (1, 2), (0, 3), (3, 4), (4, 5), (0, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]
M32 = 0xFFFFFFFF


def lerp(a, b, t): return a + (b - a) * t


def smooth(e0, e1, x):
    t = max(0.0, min(1.0, (x - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def coast_x(my):
    if my >= 84: return 53
    if my >= 74: return lerp(56, 53, (my - 74) / 10)
    if my >= 63: return lerp(61, 56, (my - 63) / 11)
    if my >= 48: return lerp(72, 61, (my - 48) / 15)
    if my >= 40: return lerp(76, 72, (my - 40) / 8)
    return 80


def segdist(px, py, ax, ay, bx, by):
    vx, vy = bx - ax, by - ay
    l2 = vx * vx + vy * vy
    t = max(0, min(1, ((px - ax) * vx + (py - ay) * vy) / l2)) if l2 > 0 else 0
    dx, dy = px - (ax + t * vx), py - (ay + t * vy)
    return math.hypot(dx, dy)


def hsh(x, y):
    h = ((x & M32) * 0x8da6b343 ^ (y & M32) * 0xd8163841 ^ 0x9E3779B9) & M32
    h ^= h >> 15; h = (h * 0x2c1b3c6d) & M32; h ^= h >> 12; h = (h * 0x297a2d39) & M32; h ^= h >> 15
    return h


def value(x, y):
    x0, y0 = math.floor(x), math.floor(y)
    fx, fy = x - x0, y - y0
    fx = fx * fx * (3 - 2 * fx); fy = fy * fy * (3 - 2 * fy)
    a, b = hsh(x0, y0) / 4294967295.0, hsh(x0 + 1, y0) / 4294967295.0
    c, d = hsh(x0, y0 + 1) / 4294967295.0, hsh(x0 + 1, y0 + 1) / 4294967295.0
    return lerp(lerp(a, b, fx), lerp(c, d, fx), fy)


def fbm(x, y):
    s, amp, f, norm = 0, .5, 1, 0
    for o in range(6):
        s += amp * value(x * f + o * 17.3, y * f - o * 9.1); norm += amp; amp *= .5; f *= 2.03
    return s / norm


def raw(mx, my):
    inland = coast_x(my) - mx
    if inland < 0: return max(-400, inland * 60)
    base = 60 + 900 * smooth(2, 32, inland)
    r = fbm(mx / 7.0, my / 7.0); r = 1 - abs(2 * r - 1)
    h = base + 700 * r * r * smooth(3, 14, inland)
    h -= 650 * math.exp(-((mx - 38) ** 2 + (my - 10) ** 2) / 260.0)
    v = min(segdist(mx, my, NODOS[a][1], NODOS[a][2], NODOS[b][1], NODOS[b][2]) for a, b in ARISTAS)
    h *= lerp(.45, 1.0, smooth(.3, 5, v))
    h += 25 * (fbm(mx * 3, my * 3) - .5)
    return max(2, h)


def altura(mx, my):
    h = raw(mx, my)
    for (_, nx, ny) in NODOS:
        d = math.hypot((mx - nx) * K * 1000, (my - ny) * K * 1000)
        if d > 1000: continue
        h = lerp(raw(nx, ny), h, smooth(300, 1000, d))
    return h


def X(h): return (h >> 16 & 255, h >> 8 & 255, h & 255)


NAVY, SOMBRA, GP, OG, HOR, HORC, OLO, OLC, ROJO = (X(0x181c30), X(0x303424), X(0x48403c), X(0x605c48), X(0x6c7874), X(0x94948c),
                                                   X(0x50541c), X(0x88885c), X(0x982420))
BANDAS = [SOMBRA, GP, OG, HOR, HORC]
CORTES = [150, 500, 1000, 1500]
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def h01(x, y, s):
    h = (x * 374761393 + y * 668265263 + s * 1274126177) & M32
    h = ((h ^ (h >> 13)) * 1274126177) & M32
    return ((h ^ (h >> 16)) & 0xffff) / 65535


def radio(n):
    return {"Valencia": 2600, "Zaragoza": 2600, "Castellón": 1800, "Sagunto": 1400, "Teruel": 1100, "Segorbe": 750, "Nules": 750, "Puçol": 750}.get(n, 550)


def pintar(mx0, dmx, my0, dmy, w, h, detalle):
    H = [[altura(mx0 + x * dmx, my0 + y * dmy) for x in range(-1, w + 1)] for y in range(-1, h + 1)]
    mTx, mTy = abs(dmx) * K * 1000, abs(dmy) * K * 1000
    paso, pf = (50, 250) if detalle else (200, 1000)
    im = Image.new("RGB", (w, h)); px = im.load()
    for y in range(h):
        for x in range(w):
            mx, my = mx0 + x * dmx, my0 + y * dmy
            hc, hW, hE, hN, hS = H[y + 1][x + 1], H[y + 1][x], H[y + 1][x + 2], H[y][x + 1], H[y + 2][x + 1]
            b = BAYER[y & 3][x & 3]
            if hc < 0:
                px[x, y] = HORC if (hW >= 0 or hE >= 0 or hN >= 0 or hS >= 0) else NAVY
                continue
            k = 0
            while k < len(CORTES) and hc >= CORTES[k]: k += 1
            if k < len(CORTES):
                lo = 0 if k == 0 else CORTES[k - 1]; f = (hc - lo) / (CORTES[k] - lo)
                if f > .8 and (f - .8) / .2 * 16 > b: k += 1
            gx, gy = (hE - hW) / (2 * mTx), (hS - hN) / (2 * mTy)
            sol = .7 * (gx + gy); pend = math.hypot(gx, gy)
            if sol > .04 and min(1, sol / .25) * 16 > b: k += 1
            c = BANDAS[min(k, 4)]
            if math.floor(hc / paso) != math.floor(hE / paso) or math.floor(hc / paso) != math.floor(hS / paso):
                fuerte = math.floor(hc / pf) != math.floor(hE / pf) or math.floor(hc / pf) != math.floor(hS / pf)
                if fuerte or pend < .5: c = BANDAS[min(k + (2 if fuerte else 1), 4)]
            pxm, pym = mx * K * 1000, my * K * 1000
            if detalle and hc < 150 and coast_x(my) - mx < 8:
                fila = math.floor(pym / 260.0); ancho = 220 + 260 * h01(fila, 0, 71); u = pxm + fila * 37.0
                linde = (u % ancho) < mTx * .9 or (pym % 260.0) < mTy * .9
                if linde and b < 5: c = OLO
                elif not linde and h01(math.floor(u / ancho), fila, 72) > .9: c = GP
            dcar = 1e18
            for i, (a, bb) in enumerate(ARISTAS):
                A, B = NODOS[a], NODOS[bb]
                ax, bx = A[1] + 600 / 3500, B[1] + 600 / 3500
                den = max(1e-9, (bx - ax) ** 2 + (B[2] - A[2]) ** 2)
                t = max(0, min(1, ((mx - ax) * (bx - ax) + (my - A[2]) * (B[2] - A[2])) / den))
                L = math.sqrt(den); nx_, ny_ = -(B[2] - A[2]) / L, (bx - ax) / L          # normal del tramo
                sd = (mx - ax) * nx_ + (my - A[2]) * ny_                                   # distancia con signo a la recta
                along = ((mx - ax) * (bx - ax) + (my - A[2]) * (B[2] - A[2])) / L
                if along < -0.05 or along > L + 0.05: continue
                dcar = min(dcar, abs(sd - .12 * math.sin(t * math.pi * 3 + i)) * K * 1000)
            if dcar < max(mTx, 18) * .8: c = HOR
            for nid, (n, nx, ny) in enumerate(NODOS):
                dx, dy = (mx - nx) * K * 1000, (my - ny) * K * 1000
                r = radio(n); d = math.hypot(dx, dy)
                if d > r * 1.25: continue
                ang = math.atan2(dy, dx)
                borde = r * (.85 + .25 * math.sin(ang * 3 + nid) + .12 * math.sin(ang * 7 + nid * 2))
                if d > borde: continue
                if not detalle: c = OG; break
                man = 70 + 40 * h01(nid, 1, 73)
                calle = (dx % man) < mTx * .9 or (dy % man) < mTy * .9
                c = SOMBRA if calle else (OG if h01(math.floor(dx / man), math.floor(dy / man), 74 + nid) > .12 else GP)
                if d > borde - max(mTx, 1): c = OLC
                break
            px[x, y] = c
    return im


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "."); out.mkdir(parents=True, exist_ok=True)
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    # de cerca: parche de 12 km alrededor de Nules, 512 téxeles (23 m por téxel), como el parche de detalle
    TW, S = 512, 12.0
    n = NODOS[4]; mx0 = n[1] - S / 2 / K; my0 = n[2] + S / 2 / K
    im = pintar(mx0, S / K / (TW - 1), my0, -S / K / (TW - 1), TW, TW, True)
    big = im.resize((1080, 1080), Image.NEAREST); d = ImageDraw.Draw(big)
    def P(mx, my): return ((mx - mx0) / (S / K) * 1080, (my0 - my) / (S / K) * 1080)
    for a, b in ARISTAS:
        A, B = NODOS[a], NODOS[b]; d.line([P(A[1], A[2]), P(B[1], B[2])], fill=(0xd4, 0xd0, 0xcc), width=4)
    cx, cy = P(n[1], n[2]); d.rectangle([cx - 12, cy - 12, cx + 12, cy + 12], fill=(0x70, 0x78, 0x4c), outline=(0xd4, 0xd0, 0xcc), width=3)
    d.text((cx + 20, cy - 12), "Nules", font=fnt, fill=(0xd4, 0xd0, 0xcc))
    d.text((16, 1040), "Previa · 2,5 km sobre Nules (vista cenital; en el juego, con perspectiva) · 23 m por téxel", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16), fill=(0xf0, 0xdc, 0x9c))
    big.save(out / "mapa_tactico_nules_2500m.png")
    # de lejos: el terreno grueso de la costa (Valencia–Castellón), 0,6 km por téxel como TexW=396
    du = (80 - 14) / 395
    mx0, my0 = 38, 58
    im2 = pintar(mx0, du, my0, du, 170, 170, False).resize((510, 510), Image.NEAREST)
    d2 = ImageDraw.Draw(im2)
    def Q(mx, my): return ((mx - mx0) / du * 3, (my - my0) / du * 3)
    for a, b in ARISTAS:
        A, B = NODOS[a], NODOS[b]; d2.line([Q(A[1], A[2]), Q(B[1], B[2])], fill=(0xd4, 0xd0, 0xcc), width=2)
    for (nn, x, y) in NODOS:
        qx, qy = Q(x, y)
        if 0 <= qx < 510 and 0 <= qy < 510:
            d2.rectangle([qx - 4, qy - 4, qx + 4, qy + 4], fill=(0x70, 0x78, 0x4c), outline=(0xd4, 0xd0, 0xcc))
            d2.text((qx + 7, qy - 7), nn, font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12), fill=(0xd4, 0xd0, 0xcc))
    im2.save(out / "mapa_tactico_costa_lejos.png")
    print("hecho")


if __name__ == "__main__":
    main()
