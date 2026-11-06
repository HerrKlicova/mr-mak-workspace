"""Ejecuta un lote de generaciones de Pixelab desde un archivo de trabajos (JSON Lines).

Cada línea de trabajos:
  {"bloque":"iconos","nombre":"municion","variante":"a","tool":"create_image_pixen","args":{...},"seed":1,"coste":1}

Hace: enviar -> esperar -> descargar -> reducir a la paleta de 32 colores -> comprobar transparencia -> registrar.
Es reanudable: lo ya enviado queda en estado.jsonl y no se vuelve a pagar.

Uso:  python lote.py <trabajos.jsonl> [--hilos 6] [--max N]
"""
import argparse
import csv
import io
import json
import os
import re
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixelab_mcp import Client  # noqa: E402

CARD = r"C:\Dev\mr-mak-workspace\workspace\2026-11-05_rts-zombi"
LOTE = os.path.join(CARD, "assets", "pixelab", "lote")
RAW = os.path.join(os.environ.get("LOTE_RAW", os.path.join(LOTE, "_raw")))
PALETA = os.path.join(CARD, "assets", "paleta", "paleta_32.hex")
ESTADO = os.path.join(LOTE, "estado.jsonl")
REGISTRO = os.path.join(LOTE, "registro_lote.csv")
COLUMNAS = ["id", "bloque", "nombre", "herramienta", "prompt", "semilla", "coste_generaciones", "fecha",
            "archivo", "transparencia", "paleta", "aprobado(s/n)"]

_lock = threading.Lock()


def cargar_paleta():
    cols = []
    for tok in open(PALETA, encoding="utf-8").read().split():
        tok = tok.strip().lstrip("#")
        if re.fullmatch(r"[0-9a-fA-F]{6}", tok):
            cols.append(tuple(int(tok[i:i + 2], 16) for i in (0, 2, 4)))
    return cols


PAL = cargar_paleta()


def a_paleta(img):
    """Cada píxel opaco pasa al color más cercano de la paleta; alfa binario (sin semitransparencias)."""
    img = img.convert("RGBA")
    px = img.load()
    cache = {}
    cambiados = 0
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a < 128:
                px[x, y] = (0, 0, 0, 0)
                continue
            k = (r, g, b)
            if k not in cache:
                cache[k] = min(PAL, key=lambda c: (c[0] - r) ** 2 + (c[1] - g) ** 2 + (c[2] - b) ** 2)
            c = cache[k]
            if c != k:
                cambiados += 1
            px[x, y] = (c[0], c[1], c[2], 255)
    return img


def transparencia(img, esperada):
    """'ok' si hay alfa y el borde no está opaco; 'FONDO' si el borde es opaco y se esperaba transparente."""
    img = img.convert("RGBA")
    w, h = img.size
    borde = [img.getpixel((x, 0)) for x in range(w)] + [img.getpixel((x, h - 1)) for x in range(w)] \
        + [img.getpixel((0, y)) for y in range(h)] + [img.getpixel((w - 1, y)) for y in range(h)]
    opacos = sum(1 for p in borde if p[3] > 127) / len(borde)
    if not esperada:
        return "no aplica"
    return "ok" if opacos < 0.5 else "FONDO (%.0f%% del borde opaco)" % (opacos * 100)


def descargar(job_id, limite=240, tool=""):
    if tool == "create_ui_asset":
        url = "https://api.pixellab.ai/mcp/ui-assets/%s/download" % job_id
    else:
        url = "https://api.pixellab.ai/mcp/images/%s/download" % job_id
    t0 = time.time()
    while time.time() - t0 < limite:
        try:
            r = urllib.request.urlopen(url, timeout=60)
            if r.status == 200:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (423, 404, 425):
                raise
        time.sleep(4)
    raise TimeoutError("no terminó: " + job_id)


def clave(t):
    return "%s|%s|%s" % (t["bloque"], t["nombre"], t["variante"])


def leer_estado():
    hechos = {}
    if os.path.exists(ESTADO):
        for linea in open(ESTADO, encoding="utf-8"):
            linea = linea.strip()
            if linea:
                d = json.loads(linea)
                hechos[d["key"]] = d
    return hechos


def anotar_estado(d):
    with _lock:
        with open(ESTADO, "a", encoding="utf-8") as f:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


def anotar_registro(fila):
    with _lock:
        nuevo = not os.path.exists(REGISTRO)
        with open(REGISTRO, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(COLUMNAS)
            w.writerow([fila.get(c, "") for c in COLUMNAS])


def procesar(trabajo, hechos):
    k = clave(trabajo)
    prev = hechos.get(k)
    if prev and prev.get("terminado"):
        return k, "ya hecho", 0
    cli = Client()
    if prev:
        job_id = prev["job_id"]
    else:
        txt = cli.call(trabajo["tool"], trabajo["args"])
        m = re.search(r"job_id:\s*([0-9a-f-]{36})", txt) or re.search(r"\bid:\s*([0-9a-f-]{36})", txt)
        if not m:
            raise RuntimeError("sin job_id: " + txt[:200])
        job_id = m.group(1)
        anotar_estado({"key": k, "job_id": job_id, "coste": trabajo.get("coste", 1), "enviado": time.strftime("%F %T")})
    datos = descargar(job_id, tool=trabajo["tool"])
    bloque, nombre, var = trabajo["bloque"], trabajo["nombre"], trabajo["variante"]
    raw_dir = os.path.join(RAW, bloque)
    out_dir = os.path.join(LOTE, bloque)
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)
    fn = "vm_%s_%s_%s.png" % (bloque, nombre, var)
    open(os.path.join(raw_dir, fn), "wb").write(datos)
    img = Image.open(io.BytesIO(datos))
    esperada = bool(trabajo["args"].get("no_background"))
    tr = transparencia(img, esperada)
    quant = a_paleta(img) if not trabajo.get("sin_paleta") else img.convert("RGBA")
    quant.save(os.path.join(out_dir, fn))
    anotar_registro({
        "id": job_id, "bloque": bloque, "nombre": "%s_%s" % (nombre, var), "herramienta": trabajo["tool"],
        "prompt": trabajo["args"].get("description", ""), "semilla": trabajo["args"].get("seed", ""),
        "coste_generaciones": trabajo.get("coste", 1), "fecha": date.today().isoformat(),
        "archivo": "assets/pixelab/lote/%s/%s" % (bloque, fn), "transparencia": tr,
        "paleta": "32 colores" if not trabajo.get("sin_paleta") else "sin reducir", "aprobado(s/n)": "",
    })
    anotar_estado({"key": k, "job_id": job_id, "terminado": True, "transparencia": tr})
    return k, tr, trabajo.get("coste", 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("trabajos")
    ap.add_argument("--hilos", type=int, default=6)
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    os.makedirs(LOTE, exist_ok=True)
    trabajos = [json.loads(l) for l in open(a.trabajos, encoding="utf-8") if l.strip()]
    if a.max:
        trabajos = trabajos[:a.max]
    hechos = leer_estado()
    pendientes = [t for t in trabajos if not hechos.get(clave(t), {}).get("terminado")]
    print("%d trabajos, %d pendientes" % (len(trabajos), len(pendientes)), flush=True)
    gasto = 0
    fallos = []
    with ThreadPoolExecutor(max_workers=a.hilos) as ex:
        futs = {ex.submit(procesar, t, hechos): t for t in pendientes}
        for f in as_completed(futs):
            t = futs[f]
            try:
                k, tr, c = f.result()
                gasto += c
                print("OK  %-40s %s" % (k, tr), flush=True)
            except Exception as e:  # noqa: BLE001
                fallos.append((clave(t), str(e)[:200]))
                print("FALLO %s: %s" % (clave(t), str(e)[:200]), flush=True)
    print("Resumen: %d correctos, %d fallos, gasto estimado %s generaciones" % (len(pendientes) - len(fallos), len(fallos), gasto))
    for k, e in fallos:
        print(" -", k, e)


if __name__ == "__main__":
    main()
