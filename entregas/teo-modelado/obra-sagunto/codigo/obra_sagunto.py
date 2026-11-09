"""Obra en curso de Sagunto: para cada tramo de la simulación (Works.Snapshot → PiecesFromWorks), qué pieza del kit de obra sale en cada estado y dónde.
Reproduce NetWorld.SagunteStart + Obras.PlanWall (módulo de 10 m, la vía libre con TrackHalfMm) en mm locales al nodo (andén = (0, 0))."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from plan import variant
TRACK = int(sys.argv[2]) if len(sys.argv) > 2 else 2500        # 2500 = hueco de 5 m (aprobado); hoy el código tiene 1600
X, Y, A, MOD = 43000, 20500, 14500, 10000
OX, OZ = 113.0, 64.5                                            # (0, 0) local = (113; 64,5) del mundo
def ceil_div(a, b): return -(-a // b)
piezas = []
def wall(kind, *pts):
    for k in range(0, len(pts) - 2, 2):
        ax, ay, bx, by = pts[k:k+4]; subs = []
        if ax == bx and (min(ay, by) < -TRACK < TRACK < max(ay, by)):      # cruza la vía: trozo, puerta, trozo
            s = 1 if by > ay else -1; c0, c1 = -TRACK * s, TRACK * s
            subs = [(ax, ay, ax, c0, False), (ax, c0, ax, c1, True), (ax, c1, bx, by, False)]
        else: subs = [(ax, ay, bx, by, False)]
        for sx, sy, ex, ey, gate in subs:
            L = abs(ex - sx) + abs(ey - sy)
            if gate: piezas.append(dict(kind="PuertaVia", x0=sx, y0=sy, x1=ex, y1=ey)); continue
            n = ceil_div(L, MOD); prev = 0
            for j in range(1, n + 1):
                t = L * j // n
                piezas.append(dict(kind=kind, x0=sx + (ex - sx) * prev // L, y0=sy + (ey - sy) * prev // L, x1=sx + (ex - sx) * t // L, y1=sy + (ey - sy) * t // L)); prev = t
g0 = -18000; g1 = g0 + 8000
wall("Hesco", -X, -Y, -X, Y); wall("Hesco", -X + A, Y, -X, Y); wall("Hesco", -X, -Y, -X + A, -Y)
wall("Sacos", -X + A, Y, X, Y); wall("Sacos", X, Y, X, -Y); wall("Sacos", X, -Y, g1, -Y)
piezas.append(dict(kind="PuertaVehiculos", x0=g0, y0=-Y, x1=g1, y1=-Y))
wall("Sacos", g0, -Y, -X + A, -Y)
segs = []
for p in piezas:
    if p["x0"] == p["x1"]: side = 0 if p["x0"] < 0 else 1; a0, a1 = sorted((p["y0"], p["y1"]))
    else: side = 2 if p["y0"] < 0 else 3; a0, a1 = sorted((p["x0"], p["x1"]))
    segs.append(dict(p, side=side, a0=a0, a1=a1))
segs.sort(key=lambda s: (s["side"], s["a0"]))
YAW = {0: 270, 1: 90, 2: 180, 3: 0}; LADO = {0: "oeste", 1: "este", 2: "sur", 3: "norte"}
out = []
for i, s in enumerate(segs):
    cxl = (s["x0"] + s["x1"]) / 2; cyl = (s["y0"] + s["y1"]) / 2
    x, z = round(OX + cxl / 1000, 3), round(OZ + cyl / 1000, 3); L = (s["a1"] - s["a0"]) / 1000
    m = "10m" if s["kind"] == "Hesco" else "8m"; v = variant(x, z); vh = (v + 2) % 5
    herr = "SM_ObraHerramientas_v%d_%s" % (vh, m)
    if s["kind"] in ("PuertaVia", "PuertaVehiculos"):
        rep = dict(piezas=["SM_ObraPuertaApuntalada_v%d_8m" % v, "SM_ObraHerramientas_v%d_8m" % vh])
        rec = "SM_ObraReconstruccion_v{k}_8m"; herr = "SM_ObraHerramientas_v%d_8m" % vh
    elif s["kind"] == "Hesco":
        rep = dict(piezas=["SM_ObraHescoAbierto_v{p}_10m", herr], v_por_vida="vida < 0,5 → v0 · < 0,8 → v1 · ≥ 0,8 → v2")
        rec = "SM_ObraReconstruccion_v{k}_10m"
    else:
        rep = dict(piezas=["SM_ObraSacos_v%d_8m" % v, herr]); rec = "SM_ObraReconstruccion_v{k}_8m"
    out.append(dict(tramo=i, lado=s["side"], lado_nombre=LADO[s["side"]], tipo=s["kind"], a0_mm=s["a0"], a1_mm=s["a1"], largo_m=L,
                    x=x, z=z, yaw=YAW[s["side"]], reparar=rep,
                    reconstruir=dict(en_cola=rec.format(k=3), trabajando=[rec.format(k="{p}"), herr], v_por_avance="WorkTicks/RebuildTicksFor < 1/3 → v0 · < 2/3 → v1 · resto → v2")))
json.dump(dict(track_half_mm=TRACK, origen_mundo=[OX, OZ], ruta="Models/Defensas/obra/", tramos=out), open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(out))
for t in out: print(t["tramo"], t["lado_nombre"], t["tipo"], t["a0_mm"], t["a1_mm"], t["largo_m"], (t["x"], t["z"]), t["yaw"], t["reparar"]["piezas"])
