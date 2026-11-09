# Plano de Nules B (terreno definitivo, §15). python3 -I plano_nules_b.py <carpeta docs/niveles>
import csv, json, os, sys
from PIL import Image, ImageDraw, ImageFont
D = sys.argv[1] if len(sys.argv) > 1 else '.'
S = 4; X0, Z0, X1, Z1 = -2, -2, 258, 130; M = 40
W, H = int((X1 - X0) * S) + 2 * M, int((Z1 - Z0) * S) + 2 * M + 150
im = Image.new('RGB', (W, H), (245, 243, 236)); dr = ImageDraw.Draw(im)
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: F = FB = ImageFont.load_default()
def P(x, z): return (M + (x - X0) * S, M + (Z1 - z) * S)
def R(x0, z0, x1, z1, **k): a = P(x0, z1); b = P(x1, z0); dr.rectangle([a, b], **k)
for x in range(0, 257, 10): dr.line([P(x, Z0), P(x, Z1)], fill=(228, 226, 218))
for z in range(0, 129, 10): dr.line([P(X0, z), P(X1, z)], fill=(228, 226, 218))
for x in range(0, 257, 50): dr.text((P(x, Z0)[0] - 8, P(x, Z0)[1] + 4), str(x), fill=(120, 120, 120), font=F)
for z in range(0, 129, 20): dr.text((6, P(0, z)[1] - 7), str(z), fill=(120, 120, 120), font=F)
R(26, 68.2, 231, 79.2, fill=(222, 218, 205)); R(26, 53.8, 231, 60.8, fill=(222, 218, 205))
R(85.5, 96.5, 256, 111, fill=(236, 232, 214))
dr.text(P(140, 105), 'explanada Z 96–111 (sin sólidos)', fill=(110, 105, 90), font=F)
for z in (49, 62.6, 66.4): dr.line([P(0, z), P(256, z)], fill=(110, 110, 120), width=2)
obs = list(csv.DictReader(open(os.path.join(D, 'nules_obstaculos_v1.csv'), encoding='utf-8'), delimiter=';'))
for o in obs:
    x0, z0, x1, z1 = [float(o[k]) / 1000 for k in ('x0_mm', 'z0_mm', 'x1_mm', 'z1_mm')]
    t = o['tipo']
    if o['forma'] == 'seg':
        col = (176, 160, 112) if t == 'muro_hesco' else (150, 165, 185) if t == 'muro_sacos' else (40, 110, 70) if t == 'puerta' else (120, 110, 90)
        dr.line([P(x0, z0), P(x1, z1)], fill=col, width=7 if t != 'tapia' else 3)
    else:
        col = (214, 205, 188) if t in ('edificio', 'casa') else (200, 196, 186)
        R(min(x0, x1), min(z0, z1), max(x0, x1), max(z0, z1), fill=col, outline=(120, 110, 95))
dr.text(P(106, 110), 'edificio', fill=(70, 60, 50), font=F)
for x in range(30, 231, 50):
    dr.ellipse([P(x, 69.6)[0] - 3, P(x, 69.6)[1] - 3, P(x, 69.6)[0] + 3, P(x, 69.6)[1] + 3], fill=(40, 52, 64))
    dr.ellipse([P(x, 59.4)[0] - 3, P(x, 59.4)[1] - 3, P(x, 59.4)[0] + 3, P(x, 59.4)[1] + 3], fill=(40, 52, 64))
g = json.load(open(os.path.join(D, 'guarnicion_puestos_v1.json'), encoding='utf-8'))['estaciones']['Nules_B_terreno_propio']
for q in g['pelotones']:
    x, z = q['x_mm'] / 1000, q['y_mm'] / 1000; c = P(x, z)
    dr.rectangle([c[0] - 8, c[1] - 6, c[0] + 8, c[1] + 6], fill=(40, 52, 64)); dr.text((c[0] + 11, c[1] - 8), q['tipo'], fill=(40, 52, 64), font=FB)
def flecha(x0, z0, x1, z1, txt):
    dr.line([P(x0, z0), P(x1, z1)], fill=(60, 60, 60), width=4); a = P(x1, z1); dr.ellipse([a[0] - 6, a[1] - 6, a[0] + 6, a[1] + 6], fill=(60, 60, 60)); dr.text((P(x0, z0)[0] + 4, P(x0, z0)[1] + 4), txt, fill=(30, 30, 30), font=FB)
flecha(2, 64.5, 30, 64.5, 'Na 50 %  (vía)'); flecha(40, 129, 70, 101, 'Nc 40 %  (norte, por la plaza)'); flecha(95, 129, 92, 101, ''); flecha(254, 64.5, 232, 64.5, ''); dr.text((P(226, 70)[0], P(226, 70)[1]), 'Nb 10 %', fill=(30, 30, 30), font=FB)
y = P(0, Z0)[1] + 30
dr.text((M, y), 'Nules B · terreno definitivo (§15): dos flancos, la vía al oeste y el norte; vista desde arriba, +Z arriba, 1 cuadro = 10 m', fill=(20, 20, 20), font=FB)
dr.text((M, y + 24), 'Ocre: HESCO 2,1 m · azul: sacos 1,2 m · verde: puertas · gris: andenes (0,68 m) · puntos: postes de catenaria (mástil) · rectángulos oscuros: guarnición', fill=(60, 60, 60), font=F)
dr.text((M, y + 44), 'Nd (calle del polígono) queda al 0 %. Sin colores rojos ni ámbar.', fill=(60, 60, 60), font=F)
im.save(os.path.join(D, 'nules_terreno_b.png')); print('ok', W, H)
