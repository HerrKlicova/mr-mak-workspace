# Plano de la salida de vehículos E4 de Sagunto (D-N198) y del parque E5. python3 -I plano_e4_sagunto.py <carpeta docs/niveles>
# Coches del atasco: misma cuenta que PrototypeBootstrap.BuildSaguntoWorld (C5), con math.hash(int2) de Unity.Mathematics.
import csv, math, os, sys
from PIL import Image, ImageDraw, ImageFont
D = sys.argv[1] if len(sys.argv) > 1 else '.'
S = 7; X0, Z0, X1, Z1 = 62, 8, 165, 92; M = 30
W, H = int((X1 - X0) * S) + 2 * M, int((Z1 - Z0) * S) + 2 * M + 96
img = Image.new('RGB', (W, H), '#d4d0cc'); d = ImageDraw.Draw(img)
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: F = FB = ImageFont.load_default()
def P(x, z): return (M + (x - X0) * S, M + (Z1 - z) * S)
def rect(x0, z0, x1, z1, fill=None, outline=None, w=1):
    a, b = P(min(x0, x1), max(z0, z1)), P(max(x0, x1), min(z0, z1)); d.rectangle([a, b], fill=fill, outline=outline, width=w)
def obb(cx, cz, L, Wd, yaw, fill, outline='#1c1812'):
    c, s = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))      # yaw de Unity: 0 = largo a lo largo de +X en la caja de AddCar
    pts = []
    for dx, dz in ((-L/2, -Wd/2), (L/2, -Wd/2), (L/2, Wd/2), (-L/2, Wd/2)):
        pts.append(P(cx + dx * c + dz * s, cz - dx * s + dz * c))
    d.polygon(pts, fill=fill, outline=outline)
def txt(x, z, t, f=F, col='#1c1812'): d.text(P(x, z), t, fill=col, font=f)
# rejilla cada 10 m
for x in range(70, 166, 10): d.line([P(x, Z0), P(x, Z1)], fill='#b4b0aa'); txt(x - 1, Z0 + 2.2, str(x))
for z in range(10, 92, 10): d.line([P(X0, z), P(X1, z)], fill='#b4b0aa'); txt(X0 + 0.3, z + 1.6, str(z))
# carretera vieja (Z 20–26) y pasillo de la E4
rect(X0, 20, X1, 26, fill='#6c7874'); txt(118, 19.2, 'carretera vieja (Z 20–26)')
rect(95, 20, 103, 44, fill='#88885c'); txt(103.6, 38, 'pasillo E4: 8 m (X 95–103)')
# inventario
for r in csv.DictReader(open(os.path.join(D, 'sagunto_obstaculos_v1.csv'), encoding='utf-8'), delimiter=';'):
    x0, z0, x1, z1 = (int(r[k]) / 1000 for k in ('x0_mm', 'z0_mm', 'x1_mm', 'z1_mm')); hg = int(r['medio_grosor_mm']) / 1000
    if max(x0, x1) < X0 or min(x0, x1) > X1 or max(z0, z1) < Z0 or min(z0, z1) > Z1: continue
    if r['tipo'] in ('casa', 'vehiculo', 'mueble') or r['id'] == 'bloque_pisos': continue
    if r['id'] == 'puerta_vehiculos_sur': continue
    if r['forma'] == 'seg': rect(x0 - hg, z0 - hg, x1 + hg, z1 + hg, fill='#283440' if r['tipo'].startswith('muro') or r['tipo'] == 'puerta' else '#605c48')
    else: rect(x0, z0, x1, z1, fill='#94948c', outline='#283440')
txt(100, 80, 'edificio de viajeros'); txt(128, 55.5, 'almacén muelle'); txt(83, 68.6, 'tren de noche')
# E4 abierta
d.line([P(95, 44), P(103, 44)], fill='#d4d0cc', width=3); txt(80.5, 42.6, 'E4 abierta →', FB)
# acopios (Z 57,5; 10 × 6 m)
for x, n in ((102, 'munición'), (121, 'combustible'), (148, 'materiales')): rect(x - 5, 54.5, x + 5, 60.5, fill='#b4a080', outline='#605c48'); txt(x - 4.6, 59.6, n)
# vehículos: ahora en Z 51 (silueta discontinua) y propuesto Z 50
for x, L, Wd, n in ((99, 8, 3, 'Dragón'), (91.5, 6, 2.2, 'VAMTAC'), (106.5, 6, 2.2, 'VAMTAC')):
    rect(x - Wd/2, 51 - L/2, x + Wd/2, 51 + L/2, outline='#1c1812')
    rect(x - Wd/2, 50 - L/2, x + Wd/2, 50 + L/2, fill='#50541c', outline='#1c1812')
# coches del atasco (hash de Unity)
Mk = 0xffffffff
def h(a, b): return ((a & Mk) * 0x83B58237 + (b & Mk) * 0x833E3E29 + 0xA9D919BF) & Mk
ax = 70.0; conflicto = []
for i in range(18):
    hh = h(i, 77); ax += 13 + (5.2 - 13) * (i / 17) + (hh & 3) * 0.6
    if ax > 250: break
    s = (hh >> 4) & 7; lane = 25.2 if s == 0 else 17.8 if s == 1 else 23 + (((hh >> 8) & 255) / 255 - 0.5) * 3.6
    yaw = (((hh >> 12) & 255) / 255 - 0.5) * 50 + (180 if ((hh >> 20) & 7) == 0 else 0)
    if ax > X1: continue
    malo = 91 <= ax <= 107
    obb(ax, lane, 4.2, 1.8, yaw, '#1c1812' if malo else '#94948c')
    if malo: conflicto.append((i, ax, lane)); d.line([P(ax, lane + 1), P(108, 31)], fill='#1c1812', width=2); txt(108.5, 32.6, f'coche {i} del atasco ({ax:.1f}; {lane:.1f}):', FB); txt(108.5, 30.2, 'tapa la salida', FB)
# título y leyenda
d.text((M, H - 86), 'Sagunto · salida de vehículos E4 (D-N198) y parque E5 · Álvaro, 11-nov', fill='#1c1812', font=FB)
d.text((M, H - 64), 'Vehículos (VAMTAC X 91,5 · Dragón X 99 · VAMTAC X 106,5): relleno = sitio propuesto, Z 50;', fill='#1c1812', font=F)
d.text((M, H - 46), 'contorno = el de ahora, Z 51 (el Dragón, de 8 m, pisa 0,5 m el acopio de munición).', fill='#1c1812', font=F)
d.text((M, H - 28), 'Pasillo X 95–103 hasta la carretera: libre salvo el coche oscuro (atasco calculado como en el código, C5).', fill='#1c1812', font=F)
out = os.path.join(D, 'sagunto_salida_e4.png'); img.save(out); print(out, conflicto)
