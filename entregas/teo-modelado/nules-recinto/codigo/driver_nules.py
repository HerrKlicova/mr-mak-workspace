import json, sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import plan as P
J = json.load(open(sys.argv[1])); out = sys.argv[2]
JAMBA = 0.9; ALA = 15.0
poly0 = J["recinto"]; maxX = max(p[0] for p in poly0)
poly = []
for i in range(len(poly0)):
    a, b = poly0[i], poly0[(i+1) % len(poly0)]; poly.append(a)
    if abs(a[1]-b[1]) < 1e-3 and (abs(a[0]-maxX) < 1e-3 or abs(b[0]-maxX) < 1e-3):
        x = maxX - ALA
        if min(a[0], b[0]) < x < max(a[0], b[0]): poly.append([x, a[1]])
if "--oeste-hesco" in sys.argv:      # Álvaro 9-nov (§14): HESCO en el muro oeste entre las jambas (Z 52,4–59,9) y desde la doble hasta pasar el andén (Z 80,21 = 10 m + 1 celda)
    OESTE_H = (52.4, 80.21); q = []
    for i in range(len(poly)):
        a, b = poly[i], poly[(i+1) % len(poly)]; q.append(a)
        if abs(a[0]-b[0]) < 1e-3 and abs(a[0]-85) < 1e-3:
            for zc in sorted([OESTE_H[1], 59.9, OESTE_H[0]], reverse=(b[1] < a[1])):
                if min(a[1], b[1]) < zc < max(a[1], b[1]): q.append([a[0], zc])
    poly = q
else: OESTE_H = None
n = len(poly)
edif = lambda i: poly[i][1] > 96 + 1e-3 or poly[(i+1) % n][1] > 96 + 1e-3
def mat(i):
    a, b = poly[i], poly[(i+1) % n]
    if min(a[0], b[0]) >= maxX - ALA - 1e-3: return "H"
    if OESTE_H and abs(a[0]-85) < 1e-3 and abs(b[0]-85) < 1e-3 and min(a[1], b[1]) >= OESTE_H[0]-1e-3 and max(a[1], b[1]) <= OESTE_H[1]+1e-3: return "H"
    return "S"
def huecos_de(conjamba, puertas):
    H = {}
    for p in puertas:
        px, pz = p["pos"]; hz, hx = p.get("hueco_z"), p.get("hueco_x"); e = JAMBA if conjamba else 0
        for i in range(n):
            a, b = poly[i], poly[(i+1) % n]; dx, dz = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dz)
            if L < 0.5: continue
            s = ((px-a[0])*dx + (pz-a[1])*dz)/L; ex = a[0]+dx*s/L-px; ez = a[1]+dz*s/L-pz
            if s < 0 or s > L or ex*ex+ez*ez > 1: continue
            if hz and abs(dx) < 1e-3: h = [(hz[0]-e-a[1])*math.copysign(1, dz), (hz[1]+e-a[1])*math.copysign(1, dz)]
            elif hx and abs(dz) < 1e-3: h = [(hx[0]-e-a[0])*math.copysign(1, dx), (hx[1]+e-a[0])*math.copysign(1, dx)]
            else: h = [s-4-e, s+4+e]
            H.setdefault(i, []).append((max(0, min(h)), min(L, max(h)))); p["lado"] = i
    return H
def coste(H):
    u = 0
    for i in range(n):
        if edif(i): continue
        a, b = poly[i], poly[(i+1) % n]; L = math.hypot(b[0]-a[0], b[1]-a[1])
        L -= sum(B-A for A, B in H.get(i, []))
        u += L * (0.6 if mat(i) == "H" else 0.2)
    return u
puertas = json.loads(json.dumps(J["puertas"]))
for p in puertas:
    if "--mover-vehiculos" in sys.argv and p["tipo"] == "vehiculos": p["hueco_x"] = [177.22, 185.22]; p["pos"] = [181.22, 40]
Hlib = huecos_de(False, puertas); Hm = huecos_de(True, puertas)
P.MEJORAS = True
if "--oeste-hesco" in sys.argv:   # sin remates (cortos) en las jambas de las dos puertas dobles: sus celdas caerían sobre el andén
    P.SIN_REMATE = {i for i in range(n) if any(p["tipo"] == "via_doble" and p.get("lado") == i for p in puertas)}
pz = P.plan(poly, mat, edif, Hm)
for q in pz:
    for k in ("x", "z", "largo", "escala_x"): q[k] = round(q[k], 3)
json.dump(dict(recinto=poly0, recinto_partido=poly, material_por_lado=[("E" if edif(i) else mat(i)) for i in range(n)], puertas=puertas, piezas=pz,
               coste_lineal_u=round(coste(Hlib), 2)), open(out, "w"), ensure_ascii=False, indent=1)
print("coste hueco libre", round(coste(Hlib), 2), "| con jambas", round(coste(Hm), 2))
for i in range(n): print(i, poly[i], poly[(i+1) % n], "E" if edif(i) else mat(i), Hm.get(i))
for k, q in enumerate(pz): print(k, q)
