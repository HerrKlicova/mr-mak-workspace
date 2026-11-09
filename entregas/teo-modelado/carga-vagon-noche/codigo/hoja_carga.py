"""Tira de candidatas para la carga del vagón (Lucía, 9-nov): solo cambia el material «carga» (845c28).
Render con la luz de Bruno (build_dia_horda.py: E calima, N luna) y medidas por cara calibradas con la build (Sara)."""
import sys, json, math, importlib.util, textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont
spec = importlib.util.spec_from_file_location("bdh", "/tmp/claude-0/build_dia_horda.py"); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
sys.path.insert(0, "/tmp/claude-0/carga"); import tabla as TB
OUT = sys.argv[1]
M = json.load(open("/tmp/claude-0/carga/mallas/mallas.json"))
CAND = ["b4a080", "b8b8b8", "f0dc9c", "94948c", "a86c50", "845c28"]
PX = B.PX; W, H = 170, 84; S = 3
right = np.array([1.0, 0, 0]); fwd = np.array([0, -math.sin(B.PITCH), math.cos(B.PITCH)]); up = np.cross(fwd, right) * -1
if up[1] < 0: up = -up
def lin(h): return B.s2l(B.hexrgb("#" + h))
def escena(key, cand):
    T = []; A = []; C = []
    d = M[key]
    for t, c in zip(np.array(d["T"]), d["C"]):
        t = np.stack([t[:, 2], t[:, 1], -t[:, 0]], 1)          # el vagón a lo largo de X, con un lateral mirando al sur (a la cámara)
        n = np.cross(t[1] - t[0], t[2] - t[0]); n = n / max(np.linalg.norm(n), 1e-9)
        if c == "845c28": cls, c = "carga", cand
        elif c == "88885c" and abs(n[2]) > 0.7: cls = "lateral"
        else: cls = "tren"
        T.append(t); A.append(lin(c)); C.append(cls)
    g = 40
    for q in (((-g, 0, -g), (-g, 0, g), (g, 0, g)), ((-g, 0, -g), (g, 0, g), (g, 0, -g))):
        T.append(np.array(q, float)); A.append(lin("b4a080")); C.append("suelo_in")
    return np.array(T), np.array(A), np.array(C, object)
def panel(key, cand, luz):
    T, A, C = escena(key, cand)
    c = np.array([0, 1.4, 0]); x0, y0 = c @ right - W * PX / 2, c @ up + H * PX / 2
    depth, tid = B.raster(T, right, up, fwd, x0, y0, PX, W, H)
    img, _, _, ok = B.render(T, A, C, B.VARIANTES[luz], (depth, tid, right, up, fwd, x0, y0))
    cl = np.full(tid.shape, "", object); cl[ok] = C[tid[ok]]
    Lp = B.lstar_lin(img)
    srgb = (B.l2s(img) * 255 + 0.5).astype(np.uint8); srgb[~ok] = (0x30, 0x34, 0x24)
    med = {k: round(float(np.median(Lp[cl == k])), 1) for k in ("carga", "lateral") if (cl == k).any()}
    med["px_carga"] = int((cl == "carga").sum())
    return Image.fromarray(np.repeat(np.repeat(srgb, S, 0), S, 1)), med
def main():
    import os; os.makedirs(OUT, exist_ok=True)
    R = TB.R; latE = R["E"]["lat_s"]; LAT_N = 16.6
    ims = {}; meds = {}
    for cnd in CAND:
        for key in ("r2", "cerc"):
            for l in ("E", "N"):
                im, md = panel(key, cnd, l); ims[(cnd, key, l)] = im; meds[f"{cnd}_{key}_{l}"] = md; print(cnd, key, l, md, flush=True)
    filas = {}
    for cnd in CAND:
        e, n = R["E"][cnd], R["N"][cnd]
        filas[cnd] = dict(dia_L=round(e["L"], 1), dia_dL=round(e["L"] - latE, 1), noche_L=round(n["L"], 1), noche_dL=round(n["L"] - LAT_N, 1),
                          entrada=n["ent"], entrada_L=round(n["entL"], 1),
                          cumple=bool(e["L"] - latE >= 8 and n["L"] >= 24.6 and n["entL"] >= 25 and n["ent"] != "303424"))
    json.dump(dict(filas=filas, renders=meds, lateral_dia=round(latE, 1), lateral_noche_build=LAT_N), open(f"{OUT}/medidas_carga.json", "w"), indent=1, ensure_ascii=False)
    pw, ph = ims[(CAND[0], "r2", "E")].size
    lab = 330; top = 140; gap = 8; rowh = ph + 40; foot = 64
    hoja = Image.new("RGB", (lab + 4 * pw + 3 * gap + 16, top + len(CAND) * rowh + foot), (24, 28, 48))
    d = ImageDraw.Draw(hoja)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22); fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22); fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    d.text((16, 12), "Carga del vagón (cajas de munición de la R2 y carga del vagón cercano): 5 candidatas y la actual", fill=(212, 208, 204), font=f)
    for q, ln in enumerate(["Solo cambia el material «carga». Columnas: R2 de día · R2 de noche · vagón cercano v2 de día · de noche. Luz de Bruno: E (calima) y N (luna).",
                            "Día: ΔL* frente al lateral 88885c al sol (L* %.1f; el mismo modelo da 11 para 845c28, como midió Bruno). Noche: L* en pantalla estimada con la medida de Sara" % latE,
                            "en la build (lateral 16,6), y la entrada de T_Paleta32 donde cae el color iluminado (la del lateral es 303424). Hace falta: día ≥ 8, noche ≥ 24,6 y entrada ≥ 25."]):
        d.text((16, 44 + q * 21), ln, fill=(184, 184, 184), font=fs)
    cols = [("r2", "E"), ("r2", "N"), ("cerc", "E"), ("cerc", "N")]
    for i, cnd in enumerate(CAND):
        y = top + i * rowh; fr = filas[cnd]
        sw = tuple(int(cnd[k:k + 2], 16) for k in (0, 2, 4))
        d.rectangle([16, y + 6, 60, y + 50], fill=sw, outline=(212, 208, 204))
        tit = ("%d · #%s" % (i + 1, cnd)) if cnd != "845c28" else "Actual · #845c28"
        d.text((72, y + 4), tit, fill=(212, 208, 204), font=fb)
        txt = ["día ΔL* %+.1f" % fr["dia_dL"], "noche L* %.1f (ΔL* %+.1f)" % (fr["noche_L"], fr["noche_dL"]), "entrada %s (L* %.1f)" % (fr["entrada"], fr["entrada_L"]),
               "CUMPLE" if fr["cumple"] else "no cumple"]
        for q, t in enumerate(txt):
            okq = [fr["dia_dL"] >= 8, fr["noche_L"] >= 24.6, fr["entrada_L"] >= 25 and fr["entrada"] != "303424", fr["cumple"]][q]
            d.text((72, y + 34 + q * 20), t, fill=(212, 208, 204) if okq else (240, 220, 156), font=fs)
        for j, (k, l) in enumerate(cols):
            x = lab + j * (pw + gap); hoja.paste(ims[(cnd, k, l)], (x, y))
        if i == 0:
            for j, (k, l) in enumerate(cols):
                d.text((lab + j * (pw + gap) + 4, top - 22), {"r2": "R2 tropa", "cerc": "vagón cercano v2"}[k] + " · " + {"E": "día", "N": "noche"}[l], fill=(212, 208, 204), font=fs)
    d.text((16, hoja.size[1] - 54), "Amarillo = no llega. La noche del render es el modelo de Bruno, que sale algo más oscuro que la build en las caras de arriba; las cifras de noche van corregidas", fill=(148, 148, 140), font=fs)
    d.text((16, hoja.size[1] - 32), "con las dos medidas de Sara (845c28 → 14,9 y 847c34 → 20,7). La medida buena será la de Sara cuando Marcos reimporte. Teo, 9-nov.", fill=(148, 148, 140), font=fs)
    hoja.save(f"{OUT}/tira_carga_vagon.png")
main()
