import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import plan as P
f = sys.argv[1]; d = json.load(open(f))
VP = ["TuboChapa", "ChapaOndulada", "Tablones", "MallaEspino", "Blindada"]
carp = {"via_doble": ("Nules/puerta_via_doble", "SM_PuertaViaDoble"), "via": ("Defensas/puerta_via", "SM_PuertaVia"), "vehiculos": ("Defensas/muro", "SM_PuertaVehiculos")}
for p in d['puertas']:
    x, z = p['pos']; v = P.variant(x, z); c, m = carp[p['tipo']]
    p['malla'] = "%s/%s_v%d_%s" % (c, m, v, VP[v]); p['col'] = "Defensas/colision/%s_Col" % m
    if 'hueco_z' in p: p['hueco_muro_z'] = [round(p['hueco_z'][0]-0.9, 2), round(p['hueco_z'][1]+0.9, 2)]; p['yaw'] = 270 if x < 100 else 90
    else: p['hueco_muro_x'] = [round(p['hueco_x'][0]-0.9, 2), round(p['hueco_x'][1]+0.9, 2)]; p['yaw'] = 180
json.dump(d, open(f, 'w'), ensure_ascii=False, indent=1)
