# Plantillas de asentamiento para el núcleo v2: pueblo de la huerta y ciudad en ruinas. 5 variantes de cada una (semillas 1..5).
# Álvaro (Niveles), 11-nov. Coordenadas LOCALES en metros con el origen en el centro (X este, Z norte); se colocan en el mundo con un desplazamiento y un giro de 0/90/180/270.
# Salida por variante: <tipo>_v<n>_edificios.csv (esquema de obstáculos, mm, lo lee NightSim.LosSceneFromCsv), <tipo>_v<n>_calles.csv, <tipo>_v<n>_puntos.csv (zombis y botín) y <tipo>_v<n>.png.
# Uso: python3 -I plantillas_hito1.py <carpeta de salida>
import csv, json, math, os, random, sys
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(OUT, exist_ok=True)
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
except Exception: F = FB = ImageFont.load_default()
ESTADOS = ['sano', 'danado', 'ruina', 'derrumbado']          # derrumbado: queda un montón de escombro de 2 m que tapa el paso

def fila_casas(r, x0, x1, z_fachada, hacia, fondo_min, fondo_max, frente_min, frente_max, plantas, out, pref):
    """Hilera entre medianeras a lo largo de X, con la fachada en z_fachada; hacia = +1 si el fondo crece hacia +Z."""
    x = x0
    while x < x1 - frente_min:
        fr = min(r.uniform(frente_min, frente_max), x1 - x)
        fo = r.uniform(fondo_min, fondo_max); pl = r.choice(plantas)
        za, zb = (z_fachada, z_fachada + fo) if hacia > 0 else (z_fachada - fo, z_fachada)
        out.append(dict(id=f'{pref}_{len(out):03d}', x0=x, x1=x + fr, z0=za, z1=zb, plantas=pl, uso='vivienda')); x += fr
def fila_casas_z(r, z0, z1, x_fachada, hacia, fondo_min, fondo_max, frente_min, frente_max, plantas, out, pref):
    z = z0
    while z < z1 - frente_min:
        fr = min(r.uniform(frente_min, frente_max), z1 - z)
        fo = r.uniform(fondo_min, fondo_max); pl = r.choice(plantas)
        xa, xb = (x_fachada, x_fachada + fo) if hacia > 0 else (x_fachada - fo, x_fachada)
        out.append(dict(id=f'{pref}_{len(out):03d}', x0=xa, x1=xb, z0=z, z1=z + fr, plantas=pl, uso='vivienda')); z += fr

def manzana(r, bx0, bz0, bx1, bz1, fondo, frente, plantas, out, pref, chaflan=0.0):
    """Manzana cerrada: cuatro hileras alrededor de un patio. Sin solapes: las hileras E y O van entre las N y S."""
    c = chaflan
    fila_casas(r, bx0 + c, bx1 - c, bz0, +1, fondo[0], fondo[1], frente[0], frente[1], plantas, out, pref)
    fila_casas(r, bx0 + c, bx1 - c, bz1, -1, fondo[0], fondo[1], frente[0], frente[1], plantas, out, pref)
    fila_casas_z(r, bz0 + fondo[1] + 0.5, bz1 - fondo[1] - 0.5, bx0, +1, fondo[0], fondo[1], frente[0], frente[1], plantas, out, pref)
    fila_casas_z(r, bz0 + fondo[1] + 0.5, bz1 - fondo[1] - 0.5, bx1, -1, fondo[0], fondo[1], frente[0], frente[1], plantas, out, pref)

def estados(r, eds, pesos):
    for e in eds:
        e['estado'] = r.choices(range(4), pesos)[0]
        if e['uso'] != 'vivienda': e['estado'] = min(e['estado'], 2)      # los edificios con botín nunca están derrumbados: el botín tiene que poder sacarse
        h = e['plantas'] * 3.2 + 0.4
        e['alto'] = {0: h, 1: h, 2: max(3.0, h * 0.6), 3: 2.0}[e['estado']]

def pueblo(seed):
    r = random.Random(1000 + seed); eds = []; calles = []; pts = []
    W, H = 260, 220
    # retícula: calle mayor E–O (8 m) en Z 0, calle N–S (8 m) en X 0; calles de 5 m cada ~48 × 38 m; plaza de 40 × 30 m en el cruce (al NE)
    xs = [-130, -82, -36, 4, 44, 88, 130]; zs = [-110, -72, -34, 4, 40, 76, 110]
    xs = [xs[0]] + [v + r.uniform(-4, 4) for v in xs[1:-1]] + [xs[-1]]; zs = [zs[0]] + [v + r.uniform(-4, 4) for v in zs[1:-1]] + [zs[-1]]
    for i in range(len(xs)): calles.append(('calle_ns_%d' % i, xs[i], -H / 2, xs[i], H / 2, 8 if i == 3 else 5))
    for j in range(len(zs)): calles.append(('calle_eo_%d' % j, -W / 2, zs[j], W / 2, zs[j], 8 if j == 3 else 5))
    plaza = (xs[3] + 4, zs[3] + 4, xs[4] - 2.5, zs[4] - 2.5)
    for i in range(len(xs) - 1):
        for j in range(len(zs) - 1):
            ancho_i = (4 if i in (2, 3) else 2.5); bx0 = xs[i] + (4 if i == 3 else 2.5); bx1 = xs[i + 1] - (4 if i + 1 == 3 else 2.5)
            bz0 = zs[j] + (4 if j == 3 else 2.5); bz1 = zs[j + 1] - (4 if j + 1 == 3 else 2.5)
            if (i, j) == (3, 3):          # plaza con la iglesia al norte
                eds.append(dict(id='iglesia', x0=bx0 + 8, x1=bx0 + 30, z0=bz1 - 20, z1=bz1, plantas=4, uso='iglesia'))
                eds.append(dict(id='campanario', x0=bx0 + 30, x1=bx0 + 36, z0=bz1 - 6, z1=bz1, plantas=7, uso='campanario'))
                pts.append(('plaza', 'plaza', (bx0 + bx1) / 2, (bz0 + bz1) / 2 - 6, 0, 'plaza mayor con fuente')); continue
            if r.random() < 0.08:          # solar o huerto
                pts.append(('solar_%d_%d' % (i, j), 'solar', (bx0 + bx1) / 2, (bz0 + bz1) / 2, 0, 'solar o huerto, abierto')); continue
            manzana(r, bx0, bz0, bx1, bz1, (9, 13), (5, 8), [1, 2, 2, 2, 3], eds, 'casa')
    # edificios con botín (sustituyen a la casa que caiga en su sitio)
    especiales = [('cooperativa', 'material', 24, 16, 2), ('farmacia', 'raciones', 8, 10, 2), ('ayuntamiento', 'municion', 16, 12, 3), ('gasolinera', 'gasoil', 18, 12, 1), ('almacen', 'raciones', 20, 14, 1)]
    for nom, rec, a, f, pl in especiales:
        if nom == 'gasolinera':      # fuera del casco, junto a la carretera de entrada (oeste)
            cx, cz = -W / 2 - 18, zs[3] - 14
        elif nom == 'cooperativa':   # en el borde este, junto a la vía del tren si la hay
            cx, cz = W / 2 + 16, zs[2] + r.uniform(-10, 10)
        else:
            k = r.randrange(len(eds)); e = eds[k]
            while e['uso'] != 'vivienda': k = r.randrange(len(eds)); e = eds[k]
            cx, cz = (e['x0'] + e['x1']) / 2, (e['z0'] + e['z1']) / 2
            eds = [q for q in eds if not (q['uso'] == 'vivienda' and q['x0'] < cx + a / 2 and q['x1'] > cx - a / 2 and q['z0'] < cz + f / 2 and q['z1'] > cz - f / 2)]
        eds.append(dict(id=nom, x0=cx - a / 2, x1=cx + a / 2, z0=cz - f / 2, z1=cz + f / 2, plantas=pl, uso=nom))
        pts.append(('botin_' + nom, 'botin', cx, cz, 0, f'{rec}: depósito de {nom}'))
    estados(r, eds, [35, 35, 22, 8])
    # zombis: densidad por manzana (más en la plaza y la iglesia); unos 450 ± 80
    total = 0
    for e in eds:
        n = int(round((e['x1'] - e['x0']) * (e['z1'] - e['z0']) / 60 * r.uniform(0.6, 1.4)))
        if e['uso'] in ('iglesia', 'ayuntamiento'): n *= 3
        if n: pts.append(('zg_' + e['id'], 'zombis', (e['x0'] + e['x1']) / 2, (e['z0'] + e['z1']) / 2, n, 'grupo dentro o junto al edificio')); total += n
    return dict(tipo='pueblo', W=W, H=H, eds=eds, calles=calles, pts=pts, zombis=total)

def ciudad(seed):
    r = random.Random(2000 + seed); eds = []; calles = []; pts = []
    W = H = 640
    nx = 5; paso = W / nx; calle = 13.0; gran = 30.0    # ensanche: 5 × 5 manzanas de ~115 m con chaflanes de 10 m; calles de 13 m y una gran vía de 30 m
    xs = [-W / 2 + i * paso for i in range(nx + 1)]; zs = list(xs)
    gv = r.randrange(2, nx - 1)                         # la gran vía (E–O)
    for i, v in enumerate(xs): calles.append(('calle_ns_%d' % i, v, -H / 2, v, H / 2, calle))
    for j, v in enumerate(zs): calles.append(('calle_eo_%d' % j, -W / 2, v, W / 2, v, gran if j == gv else calle))
    celdas = [(i, j) for i in range(nx) for j in range(nx)]; r.shuffle(celdas)
    tipos_s = [('hospital', 'raciones'), ('mercado', 'raciones'), ('cuartel', 'municion'), ('almacenes', 'material'), ('cocheras', 'gasoil')]
    singulares = {celdas[k]: tipos_s[k] for k in range(5)}       # las 5 manzanas singulares, una de cada recurso clave
    for i in range(nx):
        for j in range(nx):
            bx0, bx1 = xs[i] + calle / 2, xs[i + 1] - calle / 2
            bz0 = zs[j] + ((gran if j == gv else calle) / 2); bz1 = zs[j + 1] - ((gran if j + 1 == gv else calle) / 2)
            roll = r.random(); sing = singulares.get((i, j))
            if sing:
                nom, rec = sing
                eds.append(dict(id=f'{nom}_{i}_{j}', x0=bx0 + 6, x1=bx1 - 6, z0=bz0 + 6, z1=bz1 - 6, plantas=r.choice([2, 3, 4]), uso=nom))
                pts.append((f'botin_{nom}_{i}_{j}', 'botin', (bx0 + bx1) / 2, (bz0 + bz1) / 2, 0, f'{rec}: {nom}')); continue
            if roll < 0.07: pts.append((f'parque_{i}_{j}', 'parque', (bx0 + bx1) / 2, (bz0 + bz1) / 2, 0, 'jardín, abierto')); continue
            manzana(r, bx0, bz0, bx1, bz1, (14, 20), (12, 22), [5, 6, 6, 7, 8], eds, f'bloque_{i}_{j}', chaflan=10)
    estados(r, eds, [10, 35, 40, 15])
    # escombros en la calle (tapan el paso, no del todo la vista): delante de los derrumbados
    for e in eds:
        if e['estado'] == 3:
            cx, cz = (e['x0'] + e['x1']) / 2, (e['z0'] + e['z1']) / 2
            pts.append(('escombro_' + e['id'], 'escombro', cx, cz, 0, 'montón de 2 m en la calle: tapa el paso'))
    # coches abandonados en las calles (tapan el paso de vehículos)
    for k in range(60):
        c = r.choice(calles); t = r.random()
        pts.append((f'coche_{k:02d}', 'coche', c[1] + (c[3] - c[1]) * t + r.uniform(-3, 3), c[2] + (c[4] - c[2]) * t + r.uniform(-3, 3), r.choice([0, 90, 180, 270]) + r.uniform(-25, 25), 'coche abandonado'))
    total = 0
    for e in eds:
        n = int(round((e['x1'] - e['x0']) * (e['z1'] - e['z0']) * e['plantas'] / 160 * r.uniform(0.6, 1.4)))
        if e['uso'] in ('hospital', 'mercado', 'cuartel'): n *= 2
        if n: pts.append(('zg_' + e['id'], 'zombis', (e['x0'] + e['x1']) / 2, (e['z0'] + e['z1']) / 2, n, 'grupo')); total += n
    return dict(tipo='ciudad', W=W, H=H, eds=eds, calles=calles, pts=pts, zombis=total)

def guarda(t, n):
    pre = os.path.join(OUT, f"{t['tipo']}_v{n}")
    mm = lambda v: int(round(v * 1000))
    with open(pre + '_edificios.csv', 'w', newline='\n', encoding='utf-8') as fo:
        w = csv.writer(fo, delimiter=';', lineterminator='\n')
        w.writerow(['id', 'tipo', 'forma', 'x0_mm', 'z0_mm', 'x1_mm', 'z1_mm', 'medio_grosor_mm', 'altura_mm', 'tapa_vision', 'tapa_paso', 'fuente', 'nota'])
        for e in t['eds']:
            w.writerow([e['id'], 'edificio', 'caja', mm(e['x0']), mm(e['z0']), mm(e['x1']), mm(e['z1']), 0, mm(e['alto']), 'si', 'si', f'plantillas_hito1.py v{n}', f"{e['uso']}; {e['plantas']} plantas; {ESTADOS[e['estado']]}"])
    with open(pre + '_calles.csv', 'w', newline='\n', encoding='utf-8') as fo:
        w = csv.writer(fo, delimiter=';', lineterminator='\n'); w.writerow(['id', 'x0_m', 'z0_m', 'x1_m', 'z1_m', 'ancho_m'])
        for c in t['calles']: w.writerow([c[0]] + [round(v, 2) for v in c[1:5]] + [c[5]])
    with open(pre + '_puntos.csv', 'w', newline='\n', encoding='utf-8') as fo:
        w = csv.writer(fo, delimiter=';', lineterminator='\n'); w.writerow(['id', 'tipo', 'x_m', 'z_m', 'valor', 'nota'])
        for p in t['pts']: w.writerow([p[0], p[1], round(p[2], 2), round(p[3], 2), round(p[4], 1) if isinstance(p[4], float) else p[4], p[5]])
    # plano
    S = 2.0 if t['tipo'] == 'pueblo' else 1.0; Mg = 40
    Wp, Hp = int((t['W'] + 120) * S) + 2 * Mg, int((t['H'] + 60) * S) + 2 * Mg + 40
    img = Image.new('RGB', (Wp, Hp), (180, 160, 128)); d = ImageDraw.Draw(img)
    ox, oz = Wp / 2, Mg + (t['H'] / 2 + 30) * S
    P = lambda x, z: (ox + x * S, oz - z * S)
    for c in t['calles']:
        if c[5] == 0: d.rectangle([P(c[1], c[4]), P(c[3], c[2])], fill=(96, 92, 72)); continue
        hw = c[5] / 2
        if c[1] == c[3]: d.rectangle([P(c[1] - hw, c[4]), P(c[1] + hw, c[2])], fill=(108, 120, 116))
        else: d.rectangle([P(c[1], c[2] + hw), P(c[3], c[2] - hw)], fill=(108, 120, 116))
    colE = {0: (212, 208, 204), 1: (148, 148, 140), 2: (96, 92, 80), 3: (40, 36, 30)}
    for e in t['eds']:
        d.rectangle([P(e['x0'], e['z1']), P(e['x1'], e['z0'])], fill=colE[e['estado']], outline=(28, 24, 18))
    for p in t['pts']:
        a = P(p[2], p[3])
        if p[1] == 'botin': d.rectangle([a[0] - 5, a[1] - 5, a[0] + 5, a[1] + 5], fill=(40, 52, 64), outline=(240, 236, 228)); d.text((a[0] + 7, a[1] - 6), p[0].replace('botin_', ''), fill=(28, 24, 18), font=F)
        elif p[1] in ('plaza', 'parque', 'solar'): d.text((a[0] - 12, a[1] - 6), p[1], fill=(28, 24, 18), font=F)
        elif p[1] == 'escombro': d.ellipse([a[0] - 3, a[1] - 3, a[0] + 3, a[1] + 3], fill=(136, 136, 92))
    d.text((Mg, 12), f"Plantilla {t['tipo']} v{n} · {t['W']} × {t['H']} m · {len(t['eds'])} edificios · {t['zombis']} zombis · Álvaro, 11-nov", fill=(28, 24, 18), font=FB)
    d.text((Mg, Hp - 30), 'edificios: claro sano · gris dañado · oscuro ruina · negro derrumbado; cuadro azul = botín; origen en el centro; norte arriba', fill=(28, 24, 18), font=F)
    img.save(pre + '.png')
    nb = sum(1 for p in t['pts'] if p[1] == 'botin')
    return dict(variante=n, edificios=len(t['eds']), zombis=t['zombis'], botin=nb)

resumen = {}
for n in range(1, 6):
    resumen.setdefault('pueblo', []).append(guarda(pueblo(n), n))
    resumen.setdefault('ciudad', []).append(guarda(ciudad(n), n))
json.dump(resumen, open(os.path.join(OUT, 'plantillas_hito1.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps(resumen, ensure_ascii=False))
