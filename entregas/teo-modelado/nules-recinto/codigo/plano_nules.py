import json, sys
from PIL import Image, ImageDraw, ImageFont
d = json.load(open(sys.argv[1])); out = sys.argv[2]
S = 9; X0, X1, Z0, Z1 = 70, 206, 32, 118; M = 40
W, H = int((X1-X0)*S)+2*M, int((Z1-Z0)*S)+2*M+150
im = Image.new('RGB', (W, H), (246, 244, 238)); dr = ImageDraw.Draw(im)
try:
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: F = FB = ImageFont.load_default()
P = lambda x, z: (M + (x-X0)*S, M + (Z1-z)*S)
def rect(x0, z0, x1, z1, fill=None, outline=None, w=1):
    a, b = P(min(x0,x1), max(z0,z1)), P(max(x0,x1), min(z0,z1)); dr.rectangle([a, b], fill=fill, outline=outline, width=w)
for gx in range(70, 210, 10):
    dr.line([P(gx, Z0), P(gx, Z1)], fill=(225, 222, 214)); dr.text(P(gx-1.2, Z0+0.2), str(gx), fill=(130,130,130), font=F)
for gz in range(40, 120, 10):
    dr.line([P(X0, gz), P(X1, gz)], fill=(225, 222, 214)); dr.text(P(X0+0.3, gz+1.6), str(gz), fill=(130,130,130), font=F)
# contexto (estacion_nules.json y nules-nivel.md)
rect(104.5, 96, 125.5, 113, fill=(214, 206, 190), outline=(150,140,120)); dr.text(P(105, 106), "edificio de viajeros", fill=(90,80,60), font=F); dr.text(P(105, 103.5), "(hace de muro norte)", fill=(90,80,60), font=F)
for zv, nm in ((62.6, ""), (66.4, "vías generales"), (49, "apartado")):
    dr.line([P(X0, zv), P(X1, zv)], fill=(120,132,150), width=2)
    if nm: dr.text(P(130, zv+2.2), nm, fill=(60,70,90), font=F)
rect(118, 48, 182, 50, fill=(120, 132, 150)); dr.text(P(140, 47.6), "tren del capítulo 3 (apartado)", fill=(60,70,90), font=F)
COL = {'Hesco': (176, 160, 112), 'Sacos': (150, 170, 190)}
def eje(yaw): return 'x' if int(round(yaw)) % 180 == 0 else 'z'
puertas = d['puertas']
for i, p in enumerate(d['piezas']):
    c = COL[p['material']]; t = 1.11 if p['material'] == 'Hesco' else 1.0; x, z = p['x'], p['z']
    r0 = 2.78 if p['material'] == 'Hesco' else 3.9
    nm = p['malla']
    if nm.startswith(('SM_HescoEsquina','SM_SacosEsquina')):
        rect(x-t/2, z-t/2, x+t/2, z+t/2, fill=c, outline=(60,60,60))
        sx = 1 if x < 136 else -1; sz = 1 if z < 68 else -1
        rect(x, z-t/2, x+sx*r0, z+t/2, fill=c, outline=(60,60,60)); rect(x-t/2, z, x+t/2, z+sz*r0, fill=c, outline=(60,60,60))
    elif nm.startswith(('SM_HescoRemate','SM_SacosRemate')):
        # brazo alejándose del hueco más cercano y celda de vuelta hacia dentro
        if eje(p['yaw']) == 'x':
            gp = min(puertas, key=lambda q: abs(q['pos'][0]-x)+abs(q['pos'][1]-z)); s = 1 if x > gp['pos'][0] else -1
            if z > 95 and 104 <= x <= 126: s = -1 if x < 115 else 1
            rect(x, z-t/2, x+s*r0, z+t/2, fill=c, outline=(60,60,60)); inz = 1 if z < 68 else -1
            rect(x, z+inz*t/2, x+s*1.11, z+inz*(t/2+1.11), fill=c, outline=(60,60,60))
        else:
            gp = min(puertas, key=lambda q: abs(q['pos'][0]-x)+abs(q['pos'][1]-z)); s = 1 if z > gp['pos'][1] else -1
            rect(x-t/2, z, x+t/2, z+s*r0, fill=c, outline=(60,60,60)); inx = 1 if x < 136 else -1
            rect(x+inx*t/2, z, x+inx*(t/2+1.11), z+s*1.11, fill=c, outline=(60,60,60))
    else:
        L = p['largo']
        if eje(p['yaw']) == 'x': rect(x-L/2, z-t/2, x+L/2, z+t/2, fill=c, outline=(60,60,60))
        else: rect(x-t/2, z-L/2, x+t/2, z+L/2, fill=c, outline=(60,60,60))
    # número
    ox = 0; oz = 0
    if eje(p['yaw']) == 'x': oz = 2.4 if z < 68 else -1.4
    else: ox = -3.2 if x < 136 else 1.4
    dr.text(P(x+ox-0.5, z+oz+0.6), str(i), fill=(30,30,30), font=F)
for q in puertas:
    a, b = q.get('hueco_z') or q['hueco_x']; am, bm = q.get('hueco_muro_z') or q['hueco_muro_x']; x, z = q['pos']; q.setdefault('id', q['tipo'] + (' oeste' if x < 136 and 'hueco_z' in q else ' este' if 'hueco_z' in q else ' sur'))
    if 'hueco_z' in q:
        rect(x-0.45, am, x+0.45, a, fill=(90,90,90)); rect(x-0.45, b, x+0.45, bm, fill=(90,90,90))
        dr.line([P(x, a), P(x, b)], fill=(40, 110, 70), width=3)
        lx = x-9 if x < 136 else x+1.6
        dr.text(P(lx, (a+b)/2+1.8), q['id'].replace('_',' '), fill=(40,110,70), font=FB)
        dr.text(P(lx, (a+b)/2+0.2), "Z %.1f–%.1f" % (a, b), fill=(40,110,70), font=F)
    else:
        rect(am, z-0.45, a, z+0.45, fill=(90,90,90)); rect(b, z-0.45, bm, z+0.45, fill=(90,90,90))
        dr.line([P(a, z), P(b, z)], fill=(40,110,70), width=3)
        dr.text(P(a-1, z-1.2), q['id'].replace('_',' ') + "  X %.0f–%.0f" % (a, b), fill=(40,110,70), font=FB)
# leyenda
y = H - 140
dr.text((M, y), "Nules · recinto con el kit de defensas (vista desde arriba, +Z arriba, 1 cuadro = 10 m)", fill=(30,30,30), font=FB)
for k, (lab, c) in enumerate([("HESCO 2,1 m (este y alas desde X 173)", COL['Hesco']), ("Sacos 1,2 m (resto)", COL['Sacos']), ("Jambas de puerta", (90,90,90)), ("Hueco libre de la puerta", (40,110,70))]):
    xx = M + (k % 2) * 420; yy = y + 30 + (k // 2) * 24
    dr.rectangle([xx, yy, xx+28, yy+14], fill=c); dr.text((xx+36, yy), lab, fill=(40,40,40), font=F)
dr.text((M, y + 84), "Los números son los de nules_piezas.csv. Remates: brazo a lo largo del muro y una celda de vuelta hacia dentro.", fill=(70,70,70), font=F)
im.save(out); print(im.size)
