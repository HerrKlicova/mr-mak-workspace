import json, sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import plan as P
poly = [[70,44],[84.5,44],[156,44],[156,85],[84.5,85],[70,85]]
n = len(poly)
mat = lambda i: "H" if max(poly[i][0], poly[(i+1)%n][0]) <= 84.5 else "S"
puertas = [
 dict(id="via_oeste", tipo="via", pos=[70,64.5], yaw=270, hueco=[62.0,67.0], hueco_muro=[61.1,67.9], malla="Defensas/puerta_via/SM_PuertaVia_v1_ChapaOndulada", col="Defensas/colision/SM_PuertaVia_Col", nota="5 m (D-N151); la vía pasa por ella"),
 dict(id="via_este", tipo="via", pos=[156,64.5], yaw=90, hueco=[62.0,67.0], hueco_muro=[61.1,67.9], malla="Defensas/puerta_via/SM_PuertaVia_v4_Blindada", col="Defensas/colision/SM_PuertaVia_Col", nota="solo visual en el MVP, cerrada; Z SIN VERIFICAR (la misma que la oeste)"),
 dict(id="vehiculos_sur", tipo="vehiculos", pos=[99,44], yaw=180, hueco=[95.0,103.0], hueco_muro=[94.1,103.9], malla="Defensas/muro/SM_PuertaVehiculos_v2_Tablones", col="Defensas/colision/SM_PuertaVehiculos_Col", nota="E4, D-N111"),
]
huecos = {}
for p in puertas:
    px, pz = p["pos"]
    for i in range(n):
        a, b = poly[i], poly[(i+1)%n]
        if a[0] == b[0] == px and min(a[1],b[1]) <= pz <= max(a[1],b[1]):
            sg = 1 if b[1] > a[1] else -1; h = [(v - a[1])*sg for v in p["hueco_muro"]]
        elif a[1] == b[1] == pz and min(a[0],b[0]) <= px <= max(a[0],b[0]):
            sg = 1 if b[0] > a[0] else -1; h = [(v - a[0])*sg for v in p["hueco_muro"]]
        else: continue
        huecos.setdefault(i, []).append((min(h), max(h))); p["lado"] = i
P.MEJORAS = '--literal' not in sys.argv
if P.MEJORAS: P.SIN_REMATE = {5}
pz = P.plan(poly, mat, lambda i: False, huecos)
for q in pz:
    for k in ("x","z","largo","escala_x"): q[k] = round(q[k], 3)
out = sys.argv[1]
json.dump(dict(recinto=poly, material_por_lado=[mat(i) for i in range(n)], puertas=puertas, piezas=pz), open(out,'w'), ensure_ascii=False, indent=1)
print(len(pz))
for q in pz: print(q)
