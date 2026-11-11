# Terreno del Hito 1 (núcleo v2): 2048 × 2048 m de costa valenciana inventada, a 1 m por muestra (2049 × 2049).
# Álvaro (Niveles), 11-nov. Determinista: misma salida en cualquier máquina (semilla fija, solo numpy y PIL).
# Uso: python3 -I terreno_hito1.py <carpeta de salida>
# Coordenadas: X este (0..2048), Z norte (0..2048), metros. El mar queda al ESTE.
import csv, json, math, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
N = 2049; L = 2048.0
HMIN, HMAX = -10.0, 118.0                      # rango del uint16 (128 m, como un Terrain de Unity de 128 de alto)
rng = np.random.RandomState(20261111)
x = np.arange(N, dtype=np.float64); X, Z = np.meshgrid(x, x)      # X[z, x], Z[z, x]

def value_noise(cell, seed):
    r = np.random.RandomState(seed); g = int(L // cell) + 3
    v = r.rand(g, g)
    fx, fz = X / cell, Z / cell; ix, iz = fx.astype(int), fz.astype(int); tx, tz = fx - ix, fz - iz
    sx, sz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a = v[iz, ix]; b = v[iz, ix + 1]; c = v[iz + 1, ix]; d = v[iz + 1, ix + 1]
    return (a * (1 - sx) + b * sx) * (1 - sz) + (c * (1 - sx) + d * sx) * sz
def fbm(cells, seed):
    t = np.zeros_like(X); amp = 1.0; s = 0.0
    for i, c in enumerate(cells): t += amp * value_noise(c, seed + i); s += amp; amp *= 0.5
    return t / s

# ---------------------------------------------------------------- planta (todo en metros)
def costa_x(z): return 1785 + 35 * np.sin(z / 420.0 + 0.6) + 12 * np.sin(z / 97.0)          # línea de orilla
def cauce_z(xx): return 1880 - 0.10 * xx + 38 * np.sin(xx / 260.0 + 1.1) + 14 * np.sin(xx / 71.0)   # eje del cauce (baja hacia el mar, al ESE)
def carretera_x(z):                                                                          # carretera vieja
    # Lucía (11-nov 23:04): la recta A–B tiene que cortarla a 45–90° (el paso a nivel de Teo llega a 30°) y una sola vez.
    # La carretera sigue la dirección general de la recta (al NNE), al ESTE de ella en el sur y al OESTE en el norte, y la cruza
    # con una S en Z ≈ 1000: −130·tanh((z − 1000)/100) da un cruce de ~59° y un radio mínimo de ~100 m.
    linea = 1060.0 + (z - 430.0) * (240.0 / 1210.0)
    return linea - 130.0 * np.tanh((z - 1000.0) / 100.0) + 8 * np.sin(z / 133.0)

EST_A = dict(id='A', nombre='Estación A (base)', x=1060.0, z=430.0, ancho=41.0, fondo=86.0)       # recinto como el de Sagunto (86 × 41 m), girado: la vía corre a lo largo de Z
EST_B = dict(id='B', nombre='Estación B (puesto avanzado)', x=1300.0, z=1640.0, ancho=30.0, fondo=60.0)
CASERIO = dict(x=1440.0, z=1480.0, r=85.0)          # a ~213 m de B (Hugo: 150–250 m), al ESTE de la recta A–B; la carretera queda al oeste

cx = costa_x(Z); cz = cauce_z(X); rx = carretera_x(Z)
_zz = np.arange(0, L, 0.05); _k = np.argmin(np.abs(_zz - cauce_z(carretera_x(_zz))))
PZ = float(_zz[_k]); PX = float(carretera_x(np.array([PZ]))[0])          # puente: donde la carretera cruza el eje del cauce
# ---------------------------------------------------------------- relieve base: monte al oeste, huerta, marjal, playa, mar
d_mar = cx - X                                     # m hasta la orilla (positivo en tierra)
monte = np.clip((640 - X) / 640, 0, 1) ** 1.6      # 1 en X 0, 0 desde X 640
n_big = fbm([512, 256, 128], 11); n_mid = fbm([96, 48, 24], 31); n_fine = fbm([12, 6], 51)
h = 2.0 + 0.0105 * np.clip(d_mar, 0, None)         # huerta: sube ~1 m cada 95 m hacia el oeste (≈ 2 m junto al marjal, ≈ 18 m en X 600)
h += monte * (55 + 45 * n_big + 18 * (n_mid - 0.5))        # estribaciones: 60–110 m en el borde oeste
h += (1 - monte) * 1.2 * (n_mid - 0.5)             # la huerta casi plana, con bancales de ±0,6 m
h += 0.15 * (n_fine - 0.5)
# marjal: franja baja tras la playa (0,4–1,2 m), de 60 a 210 m de la orilla
marj = np.clip(1 - np.abs(d_mar - 135) / 80, 0, 1)
h = h * (1 - marj) + (0.8 + 0.4 * (n_mid - 0.5)) * marj
# playa y mar
playa = (d_mar >= 0) & (d_mar < 45)
h = np.where(playa, 0.1 + 1.6 * (np.clip(d_mar, 0, None) / 45.0) ** 1.5, h)
mar = d_mar < 0
h = np.where(mar, -0.2 - 9.0 * (1 - np.exp(d_mar / 140.0)), h)
# ---------------------------------------------------------------- cauce (rambla seca con cañas): lecho de 40 m, taludes de 1:2
dz = np.abs(Z - cz)
prof = np.where(X < 640, 6 + 9 * monte, 4.5 * np.clip(d_mar / 600, 0.35, 1))   # 15 m en el monte, 4,5 m en la huerta, 1,6 m al llegar al marjal
lecho = dz < 20; talud = (dz >= 20) & (dz < 20 + 2 * prof)
fondo = h - prof
h = np.where(lecho & ~mar, np.minimum(h, fondo), h)
f = (dz - 20) / np.maximum(2 * prof, 1e-6)
h = np.where(talud & ~mar, np.minimum(h, fondo + prof * f), h)
# ---------------------------------------------------------------- carretera vieja: 7 m de asfalto, explanada de 11 m, terraplén suave; puente sobre el cauce
def suaviza_1d(a, k):
    ker = np.ones(k) / k; p = np.pad(a, (k // 2, k // 2), mode='edge'); return np.convolve(p, ker, mode='valid')
ix_r = np.clip(np.rint(carretera_x(x)).astype(int), 0, N - 1)
perfil = h[np.arange(N), ix_r].copy()
puente = np.abs(x - cauce_z(carretera_x(x))) < 34              # tramo del puente
perfil_p = perfil.copy(); perfil_p[puente] = np.nan
idx = np.arange(N); ok = ~np.isnan(perfil_p)
perfil_p = np.interp(idx, idx[ok], perfil_p[ok])
rasante = suaviza_1d(perfil_p, 61) + 0.5                       # rasante a +0,5 m sobre el terreno medio
dr = np.abs(X - rx)
plat = dr < 5.5; mezcla = (dr >= 5.5) & (dr < 14)
ras = rasante[np.clip(Z.astype(int), 0, N - 1)]
road_mask = plat & ~puente[np.clip(Z.astype(int), 0, N - 1)]
h = np.where(road_mask, ras, h)
w_ = np.clip((dr - 5.5) / 8.5, 0, 1)
blend = mezcla & ~puente[np.clip(Z.astype(int), 0, N - 1)]
h = np.where(blend, ras * (1 - w_) + h * w_, h)
# ---------------------------------------------------------------- explanadas: estaciones (planas) y caserío (bancal suave)
def explanada(cxm, czm, ax, fz, borde, cota=None):
    global h
    dx = np.abs(X - cxm) - ax / 2; dzz = np.abs(Z - czm) - fz / 2
    dd = np.maximum(np.maximum(dx, dzz), 0)
    inside = (dx <= 0) & (dzz <= 0)
    c = float(np.median(h[inside])) if cota is None else cota
    w = np.clip(dd / borde, 0, 1); w = w * w * (3 - 2 * w)
    near = dd < borde
    h = np.where(near, c * (1 - w) + h * w, h); return round(c, 2)
cota_A = explanada(EST_A['x'], EST_A['z'], EST_A['ancho'] + 40, EST_A['fondo'] + 60, 40)   # recinto + vía y patio
cota_B = explanada(EST_B['x'], EST_B['z'], EST_B['ancho'] + 40, EST_B['fondo'] + 60, 35)
cota_C = explanada(CASERIO['x'], CASERIO['z'], 170, 150, 50)
h = np.clip(h, HMIN, HMAX)
# ---------------------------------------------------------------- usos del suelo (ids)
USOS = {0: 'mar', 1: 'playa', 2: 'marjal', 3: 'huerta', 4: 'secano', 5: 'monte', 6: 'cauce', 7: 'carretera', 8: 'explanada_estacion', 9: 'caserio', 10: 'naranjal'}
u = np.full((N, N), 3, np.uint8)
bx = 60 * (n_mid - 0.5) * 2 + 40 * (n_big - 0.5)
u[X < 640 + bx] = 4; u[(X < 380 + bx) | (h > 45)] = 5
u[(marj > 0.15) & (X > 1200)] = 2; u[playa] = 1; u[mar] = 0
u[(dz < 20) & ~mar] = 6
# naranjales: parcelas de la huerta (bloques de ~60 × 40 m) elegidos por ruido
parc = fbm([64], 71) > 0.55
u[(u == 3) & parc] = 10
u[road_mask] = 7
for e in (EST_A, EST_B):
    m = (np.abs(X - e['x']) <= (e['ancho'] + 40) / 2) & (np.abs(Z - e['z']) <= (e['fondo'] + 60) / 2); u[m] = 8   # misma explanada que explanada()
u[(X - CASERIO['x']) ** 2 + (Z - CASERIO['z']) ** 2 < CASERIO['r'] ** 2] = 9
# ---------------------------------------------------------------- caserío: edificios, tapias y zombis (deterministas)
casas = []   # (id, tipo, cx, cz, ancho_x, fondo_z, alto, yaw)
plan_c = [(-48, 20, 14, 10, 6.5, 0, 'alqueria'), (-22, 38, 10, 8, 5.5, 0, 'casa_ruina'), (4, 44, 10, 8, 5.5, 0, 'casa_ruina'), (30, 36, 12, 9, 6.0, 0, 'casa_ruina'),
          (-40, -14, 10, 8, 5.5, 90, 'casa_ruina'), (-14, -6, 8, 8, 5.0, 0, 'casa_ruina'), (12, 0, 16, 12, 9.0, 0, 'iglesia'), (40, 6, 10, 8, 5.5, 90, 'casa_ruina'),
          (-30, -46, 10, 8, 5.5, 180, 'casa_ruina'), (-4, -40, 10, 8, 5.5, 180, 'casa_ruina'), (24, -34, 22, 14, 7.0, 0, 'almacen_material'), (54, -26, 8, 8, 5.0, 0, 'casa_ruina'),
          (62, 30, 6, 6, 4.0, 0, 'caseta_pozo')]
for i, (ox, oz, a, f_, al, yaw, tipo) in enumerate(plan_c):
    casas.append(('caserio_%02d' % i, tipo, CASERIO['x'] + ox, CASERIO['z'] + oz, a, f_, al, yaw))
tapias = [((-70, -64), (70, -64)), ((70, -64), (70, 58)), ((-70, 58), (-10, 58)), ((10, 58), (70, 58)), ((-70, -64), (-70, -10)), ((-70, 10), (-70, 58))]   # cercado de tapia de 1,6 m con tres portillos (N, O y S-E abierto por el camino)
def dist_seg(x, z, a0, b0):
    (ax, az), (bx, bz) = a0, b0; dx, dz = bx - ax, bz - az
    t = max(0.0, min(1.0, ((x - ax) * dx + (z - az) * dz) / (dx * dx + dz * dz)))
    return math.hypot(x - ax - t * dx, z - az - t * dz)
zr = np.random.RandomState(4242); zombis = []
while len(zombis) < 100:
    ang = zr.rand() * 2 * math.pi; rad = 8 + zr.rand() * 70
    px, pz = CASERIO['x'] + rad * math.cos(ang), CASERIO['z'] + rad * math.sin(ang)
    if any(abs(px - c[2]) < c[4] / 2 + 1 and abs(pz - c[3]) < c[5] / 2 + 1 for c in casas): continue
    if any(dist_seg(px - CASERIO['x'], pz - CASERIO['z'], a0, b0) < 1.5 for a0, b0 in tapias): continue   # ni encima ni pegados a una tapia (medio grosor 0,25 m + holgura)
    zombis.append((round(px, 1), round(pz, 1)))
# ---------------------------------------------------------------- salida: alturas
os.makedirs(OUT, exist_ok=True)
q = np.rint((h - HMIN) / (HMAX - HMIN) * 65535).astype('<u2')
q.tofile(os.path.join(OUT, 'alturas_2049_u16le.raw'))                      # Unity: Terrain > Import Raw, 16 bit, Windows (little endian), 2049 × 2049, filas de Z = 0 hacia el norte
Image.fromarray(np.flipud(q).astype(np.uint16)).save(os.path.join(OUT, 'alturas_2049_u16.png'))   # PNG de 16 bits, con el norte arriba
Image.fromarray(np.flipud(u)).save(os.path.join(OUT, 'usos_2049.png'))
meta = dict(muestras=N, metros_por_muestra=1.0, lado_m=L, h_min_m=HMIN, h_max_m=HMAX, nivel_del_mar_m=0.0,
            raw='alturas_2049_u16le.raw: uint16 little endian, fila 0 = Z 0 (sur), columna 0 = X 0 (oeste); h = HMIN + v/65535·(HMAX−HMIN)',
            png='alturas_2049_u16.png y usos_2049.png: norte ARRIBA (fila 0 = Z 2048)', usos=USOS,
            cotas_explanada_m=dict(A=cota_A, B=cota_B, caserio=cota_C), generador='docs/niveles/herramientas/terreno_hito1.py', semilla=20261111)
json.dump(meta, open(os.path.join(OUT, 'terreno_hito1.json'), 'w'), ensure_ascii=False, indent=1)
def hm(px, pz): return float(h[int(round(min(max(pz, 0), L))), int(round(min(max(px, 0), L)))])
# ---------------------------------------------------------------- posiciones
with open(os.path.join(OUT, 'posiciones_hito1.csv'), 'w', newline='\n', encoding='utf-8') as fo:
    w = csv.writer(fo, delimiter=';', lineterminator='\n')
    w.writerow(['id', 'tipo', 'x_m', 'y_m', 'z_m', 'yaw_grados', 'ancho_m', 'fondo_m', 'nota'])
    for e, c in ((EST_A, cota_A), (EST_B, cota_B)):
        w.writerow([e['id'], 'estacion', e['x'], c, e['z'], 0, e['ancho'], e['fondo'], e['nombre'] + '; recinto ancho_m (X) × fondo_m (Z); la vía de la estación corre a lo largo de Z (norte–sur), por el centro del recinto; explanada plana a la cota y (recinto + 20 m a cada lado en X y 30 m en Z)'])
    w.writerow(['caserio', 'caserio', CASERIO['x'], cota_C, CASERIO['z'], 0, 140, 122, 'centro del cercado de tapias (X ±70, Z −64..58); unos cien zombis'])
    w.writerow(['deposito_material', 'deposito', CASERIO['x'] + 24, cota_C, CASERIO['z'] - 34, 0, 22, 14, 'almacén de material de vía del caserío: lo deja libre limpiar el caserío'])
    w.writerow(['peloton_inicio', 'peloton', EST_B['x'] - 10, cota_B, EST_B['z'] - 30, 180, 0, 0, 'el pelotón sale de B, al sur del andén'])
    w.writerow(['puente_carretera', 'puente', round(PX, 1), round(hm(PX, PZ + 40), 2), round(PZ, 1), 0, 9, 68, 'puente de la carretera vieja sobre el cauce (tablero a la rasante; SIN modelo)'])
    for i, (px, pz) in enumerate(zombis):
        w.writerow(['z%03d' % i, 'zombi', px, round(hm(px, pz), 2), pz, (i * 137) % 360, 0, 0, ''])
# ---------------------------------------------------------------- carreteras (polilínea cada 10 m, mm, para Via.Carreteras de Iker)
with open(os.path.join(OUT, 'carreteras_hito1.csv'), 'w', newline='\n', encoding='utf-8') as fo:
    w = csv.writer(fo, delimiter=';', lineterminator='\n')
    w.writerow(['carretera', 'orden', 'x_mm', 'z_mm', 'y_mm', 'ancho_mm', 'puente'])
    for k, zz in enumerate(range(0, 2049, 10)):
        xx = float(carretera_x(np.array([float(zz)]))[0])
        if xx < 0 or xx > L: continue
        w.writerow(['carretera_vieja', k, int(round(xx * 1000)), zz * 1000, int(round(float(rasante[min(zz, N - 1)]) * 1000)), 7000, 'si' if puente[min(zz, N - 1)] else 'no'])
# ---------------------------------------------------------------- obstáculos de visión (mismo esquema que sagunto_obstaculos_v1.csv, mm)
with open(os.path.join(OUT, 'obstaculos_hito1.csv'), 'w', newline='\n', encoding='utf-8') as fo:
    w = csv.writer(fo, delimiter=';', lineterminator='\n')
    w.writerow(['id', 'tipo', 'forma', 'x0_mm', 'z0_mm', 'x1_mm', 'z1_mm', 'medio_grosor_mm', 'altura_mm', 'tapa_vision', 'tapa_paso', 'fuente', 'nota'])
    mm = lambda v: int(round(v * 1000))
    for cid, tipo, ccx, ccz, a, f_, al, yaw in casas:
        if yaw in (90, 270): a, f_ = f_, a
        w.writerow([cid, 'edificio', 'caja', mm(ccx - a / 2), mm(ccz - f_ / 2), mm(ccx + a / 2), mm(ccz + f_ / 2), 0, mm(al), 'si', 'si', 'terreno_hito1.py', tipo])
    for i, ((ax0, az0), (ax1, az1)) in enumerate(tapias):
        w.writerow(['tapia_%d' % i, 'tapia', 'seg', mm(CASERIO['x'] + ax0), mm(CASERIO['z'] + az0), mm(CASERIO['x'] + ax1), mm(CASERIO['z'] + az1), 250, 1600, 'si', 'si', 'terreno_hito1.py', 'tapia de huerta de 1,6 m'])
    # naranjales junto al caserío: las parcelas que tocan el camino A–B tapan la vista a 3,5 m (no el paso)
    pm = np.array(parc); k = 0
    for gz in range(int(CASERIO['z'] - 260), int(min(CASERIO['z'] + 260, 1700)), 40):
        for gx in range(int(CASERIO['x'] - 260), int(CASERIO['x'] + 320), 60):
            ccx, ccz = gx + 30, gz + 20
            if (ccx - CASERIO['x']) ** 2 + (ccz - CASERIO['z']) ** 2 < (CASERIO['r'] + 25) ** 2: continue
            if u[int(ccz), int(ccx)] != 10: continue
            w.writerow(['naranjal_%02d' % k, 'arbolado', 'caja', mm(gx + 3), mm(gz + 3), mm(gx + 57), mm(gz + 37), 0, 3500, 'si', 'no', 'terreno_hito1.py', 'parcela de naranjos en hileras (se pasa entre las hileras)']); k += 1
    w.writerow(['estribo_n_puente', 'relieve', 'caja', mm(PX - 8), mm(PZ + 26), mm(PX + 8), mm(PZ + 34), 0, 2000, 'si', 'si', 'terreno_hito1.py', 'estribo del puente'])
    w.writerow(['estribo_s_puente', 'relieve', 'caja', mm(PX - 8), mm(PZ - 34), mm(PX + 8), mm(PZ - 26), 0, 2000, 'si', 'si', 'terreno_hito1.py', 'estribo del puente'])
# ---------------------------------------------------------------- plano con cotas (1 px = 2 m)
S = 2; P = N // S + 1; M = 60
hs = h[::S, ::S]; us = u[::S, ::S]
col = {0: (40, 52, 64), 1: (212, 208, 204), 2: (136, 136, 92), 3: (180, 160, 128), 4: (160, 150, 120), 5: (120, 116, 92), 6: (96, 92, 72), 7: (108, 120, 116), 8: (148, 148, 140), 9: (72, 64, 56), 10: (110, 120, 70)}
rgb = np.zeros(hs.shape + (3,), np.uint8)
for k_, c in col.items(): rgb[us == k_] = c
shade = np.clip(1 + 0.04 * (np.roll(hs, 1, 1) - hs) + 0.04 * (np.roll(hs, -1, 0) - hs), 0.75, 1.2)
rgb = np.clip(rgb * shade[..., None], 0, 255).astype(np.uint8)
lv = np.floor(np.where(hs > 0, hs, 0) / 5)
edge = (lv != np.roll(lv, 1, 0)) | (lv != np.roll(lv, 1, 1))
maj = np.floor(np.where(hs > 0, hs, 0) / 25); edge25 = (maj != np.roll(maj, 1, 0)) | (maj != np.roll(maj, 1, 1))
rgb[edge & (us != 0)] = (60, 56, 48); rgb[edge25 & (us != 0)] = (28, 24, 18)
img = Image.new('RGB', (rgb.shape[1] + 2 * M + 260, rgb.shape[0] + 2 * M), (212, 208, 204))
img.paste(Image.fromarray(np.flipud(rgb)), (M, M)); d = ImageDraw.Draw(img)
try:
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
except Exception: F = FB = ImageFont.load_default()
def Pp(px, pz): return (M + px / S, M + (L - pz) / S)
for v in range(0, 2049, 256):
    d.text((Pp(v, 0)[0] - 10, M + P + 4), str(v), fill=(28, 24, 18), font=F); d.text((8, Pp(0, v)[1] - 7), str(v), fill=(28, 24, 18), font=F)
def marca(px, pz, t, r=4):
    a = Pp(px, pz); d.ellipse([a[0] - r, a[1] - r, a[0] + r, a[1] + r], outline=(240, 236, 228), fill=(28, 24, 18)); d.text((a[0] + 7, a[1] - 7), t, fill=(240, 236, 228), font=FB)
for e, c in ((EST_A, cota_A), (EST_B, cota_B)):
    a, b = Pp(e['x'] - e['ancho'] / 2, e['z'] + e['fondo'] / 2), Pp(e['x'] + e['ancho'] / 2, e['z'] - e['fondo'] / 2)
    d.rectangle([a, b], outline=(240, 236, 228), width=2); marca(e['x'], e['z'], f"{e['id']} · cota {c:.1f} m")
marca(CASERIO['x'], CASERIO['z'], f'caserío · cota {cota_C:.1f} m · 100 zombis')
for px, pz in zombis: a = Pp(px, pz); d.point(a, fill=(240, 236, 228))
for cid, tipo, ccx, ccz, a_, f_, al, yaw in casas:
    if yaw in (90, 270): a_, f_ = f_, a_
    d.rectangle([Pp(ccx - a_ / 2, ccz + f_ / 2), Pp(ccx + a_ / 2, ccz - f_ / 2)], fill=(28, 24, 18))
for px, pz in ((60, 300), (200, 1200), (120, 1900), (500, 700), (800, 1500), (1400, 900), (1650, 300), (1600, 1500)):
    a = Pp(px, pz); d.text(a, f'{hm(px, pz):.0f}', fill=(28, 24, 18), font=F); d.point(a, fill=(28, 24, 18))
zc = float(cauce_z(800.0)); a = Pp(800, zc); d.text((a[0], a[1] + 14), f'cauce, lecho {hm(800, zc):.1f} m', fill=(240, 236, 228), font=F)
a = Pp(float(carretera_x(np.array([260.0]))[0]) + 20, 260); d.text(a, 'carretera vieja', fill=(28, 24, 18), font=F)
a = Pp(1900, 1000); d.text(a, 'MAR', fill=(212, 208, 204), font=FB)
a = Pp(1660, 1180); d.text(a, 'marjal', fill=(28, 24, 18), font=F)
d.line([Pp(EST_A['x'], EST_A['z'] + 25), Pp(EST_B['x'], EST_B['z'] - 20)], fill=(240, 236, 228), width=1)
lx = M + P + 20; ly = M
d.text((lx, ly), 'Terreno del Hito 1', fill=(28, 24, 18), font=FB); ly += 22
d.text((lx, ly), '2048 × 2048 m, 1 px = 2 m', fill=(28, 24, 18), font=F); ly += 16
d.text((lx, ly), 'curvas cada 5 m (gruesas cada 25)', fill=(28, 24, 18), font=F); ly += 16
d.text((lx, ly), 'X este, Z norte; norte arriba', fill=(28, 24, 18), font=F); ly += 16
d.text((lx, ly), 'línea fina: A–B en recta', fill=(28, 24, 18), font=F); ly += 16
d.text((lx, ly), f'A–B: {math.hypot(EST_B["x"] - EST_A["x"], EST_B["z"] - EST_A["z"]):.0f} m en recta', fill=(28, 24, 18), font=F); ly += 24
for k_, nm in USOS.items():
    d.rectangle([lx, ly, lx + 14, ly + 12], fill=col[k_]); d.text((lx + 20, ly - 1), nm.replace('_', ' '), fill=(28, 24, 18), font=F); ly += 17
d.text((M, 18), 'Hito 1 · terreno de costa · Álvaro (Niveles), 11-nov · generador: docs/niveles/herramientas/terreno_hito1.py', fill=(28, 24, 18), font=FB)
img.save(os.path.join(OUT, 'plano_cotas_hito1.png'))
print('cotas A, B, caserío:', cota_A, cota_B, cota_C, '| h min/max', round(float(h.min()), 2), round(float(h.max()), 2), '| zombis', len(zombis))
for nm, (px, pz) in {'A': (EST_A['x'], EST_A['z']), 'B': (EST_B['x'], EST_B['z']), 'caserio': (CASERIO['x'], CASERIO['z'])}.items():
    print(nm, 'distancia a costa', round(float(costa_x(np.array([pz]))[0] - px)), 'm; a carretera', round(float(carretera_x(np.array([pz]))[0] - px)), 'm; a cauce (Z)', round(float(cauce_z(np.array([px]))[0] - pz)), 'm')
