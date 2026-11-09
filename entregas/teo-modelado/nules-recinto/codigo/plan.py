"""Port de RecintoPlan.Plan (TBD Net/RecintoPlan.cs, marcos/noche-prototipo) para Sagunto."""
import math, json, sys
HT, ST, HC, HE, SE = 10.0, 8.0, 1.11, 2.78, 3.9
HV = ["MallaLimpia", "Geotextil", "Escalonado", "RemateSacos", "Red"]; SV = ["Recto", "Talud", "Irregular", "Tablon", "Red"]
EST = ["e0_Sano", "e1_Danado", "e2_MuyDanado", "e3_Brecha"]
M32 = 0xFFFFFFFF
MEJORAS = True
SIN_REMATE = set()   # lados sin remate junto a las puertas (Álvaro, 9-nov: muro oeste, la vuelta pisa la banqueta)
def f32(x):
    import struct; return struct.unpack('f', struct.pack('f', x))[0]
def variant(x, z, n=5):
    a = int(f32(f32(x) * 10.0)); b = int(f32(f32(z) * 10.0))
    h = ((a & M32) * 0x83B58237 + (b & M32) * 0x833E3E29 + 0xA9D919BF) & M32
    return h % n
def nombre(p, hesco, v, e=0): return "SM_%s_v%d_%s_%s" % (p, v % 5, (HV if hesco else SV)[v % 5], EST[e])
def yaw_afuera(nx, nz): return (math.degrees(math.atan2(nx, nz)) + 360) % 360
def alineado(p, q, r):
    c = (q[0]-p[0])*(r[1]-q[1]) - (q[1]-p[1])*(r[0]-q[0]); d = (q[0]-p[0])*(r[0]-q[0]) + (q[1]-p[1])*(r[1]-q[1])
    return abs(c) < 1e-3 and d > 0
def plan(poly, material, edificio, huecos):
    res = []; n = len(poly)
    area = sum(poly[i][0]*poly[(i+1)%n][1] - poly[(i+1)%n][0]*poly[i][1] for i in range(n)); ccw = area > 0
    for i in range(n):
        if edificio(i): continue
        a, b = poly[i], poly[(i+1)%n]; dx, dz = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dz)
        if L < 0.5: continue
        ux, uz = dx/L, dz/L; nx, nz = (uz, -ux) if ccw else (-uz, ux)
        yaw = yaw_afuera(nx, nz); m = material(i); hes = m == "H"; r0 = HE if hes else SE
        pe, ne = edificio((i-1)%n), edificio((i+1)%n)
        ir, fr = alineado(poly[(i-1)%n], a, b), alineado(a, b, poly[(i+2)%n])
        cortes = sorted(huecos.get(i, []))
        desde = 0.0; troz = []
        for A, B in cortes:
            if A > desde: troz.append((desde, A))
            desde = max(desde, B)
        if desde < L: troz.append((desde, L))
        if not pe and not ir:
            pv = poly[(i-1)%n]; wx, wz = pv[0]-a[0], pv[1]-a[1]
            sg = lambda v: (v > 0) - (v < 0)
            sx, sz = sg(ux + sg(wx)), sg(uz + sg(wz))
            ye = 0 if (sx > 0 and sz < 0) else 90 if (sx < 0 and sz < 0) else 180 if (sx < 0 and sz > 0) else 270
            res.append(dict(malla=nombre("HescoEsquina" if hes else "SacosEsquina", hes, variant(a[0], a[1])), x=a[0], z=a[1], yaw=ye, largo=0, escala_x=0, espejo=False, lado=i))
        for s0, s1 in troz:
            ie, fe = s0 == 0, s1 >= L - 1e-3
            def remate(s, hacia):
                x, z = a[0]+ux*s, a[1]+uz*s; r = math.radians(yaw); bx, bz = math.cos(r), -math.sin(r)
                return dict(malla=nombre("HescoRemate" if hes else "SacosRemate", hes, variant(x, z)), x=x, z=z, yaw=yaw, largo=0, escala_x=0, espejo=(bx*ux+bz*uz)*hacia < 0, lado=i)
            rem0 = (not ie or pe) and not (ie and ir); rem1 = (not fe or ne) and not (fe and fr)
            l0 = s0 + (0 if (ie and ir) else r0); l1 = s1 - (0 if (fe and fr) else r0)
            if i in SIN_REMATE:
                if rem0 and not ie: rem0 = False; l0 = s0
                if rem1 and not fe: rem1 = False; l1 = s1
            if MEJORAS and l1 - l0 < -0.05 and hes:
                # trozo corto (entre dos puertas, o entre esquina y puerta): sin remates, se rellena con cortos de HESCO
                c0 = s0 if rem0 else l0; c1 = s1 if rem1 else l1; resto = c1 - c0
                if resto <= 0.05: continue   # la esquina ya cubre el trozo (p. ej. la jamba dentro del brazo de la esquina)
                k = max(1, min(4, round(resto / HC))); l = k * HC; c = (c0 + c1) / 2; x, z = a[0]+ux*c, a[1]+uz*c
                res.append(dict(malla=nombre("HescoCorto%d" % k, hes, variant(x, z)), x=x, z=z, yaw=yaw, largo=l, escala_x=1.0, espejo=False, lado=i, nota="trozo de %.2f m: corto en lugar de remates" % resto))
                continue
            if rem0: res.append(remate(s0, +1))
            if rem1: res.append(remate(s1, -1))
            if l1 - l0 < 0.3: continue
            paso = HT if hes else ST; s = l0
            if MEJORAS and not hes:
                # sacos: el trozo se reparte en n tramos iguales (escala 0,7–1,4) en vez de un resto aplastado
                Lt = l1 - l0; nn = max(1, math.ceil(Lt / ST - 0.2)); lp = Lt / nn
                for j in range(nn):
                    c = l0 + j*lp + lp/2; x, z = a[0]+ux*c, a[1]+uz*c
                    res.append(dict(malla=nombre("MuroSacos", hes, variant(x, z)), x=x, z=z, yaw=yaw, largo=lp, escala_x=lp/ST, espejo=False, lado=i))
                continue
            def pon(s, l, pieza, esc):
                c = s + l/2; x, z = a[0]+ux*c, a[1]+uz*c
                res.append(dict(malla=nombre(pieza, hes, variant(x, z)), x=x, z=z, yaw=yaw, largo=l, escala_x=esc, espejo=False, lado=i))
            while l1 - s >= paso - 1e-3: pon(s, paso, "MuroHesco" if hes else "MuroSacos", 1.0); s += paso
            resto = l1 - s
            if resto < 0.3: continue
            if hes and MEJORAS:
                # cortos seguidos y centrados en el resto (de 4 celdas como mucho cada uno); mejor solapar un poco que dejar un agujero
                k = max(1, math.ceil(resto/HC - 0.15)); s1_ = s + resto/2 - k*HC/2
                while k > 0:
                    kk = min(4, k); pon(s1_, kk*HC, "HescoCorto%d" % kk, 1.0); s1_ += kk*HC; k -= kk
            elif hes:
                while resto >= HC*0.5:
                    k = max(1, min(4, round(resto/HC))); l = k*HC; pon(s, min(l, resto+0.3), "HescoCorto%d" % k, 1.0); s += l; resto = l1 - s
            else: pon(s, resto, "MuroSacos", resto/ST)
    return res
