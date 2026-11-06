"""Bloque de VFX animados del lote v1.3 con vfx_workbench de Pixelab (gratis: no gasta generaciones).

Para cada efecto: start --preset -> parches (color, tamaño) -> export -> descarga hoja PNG + JSON -> reducción a la paleta.
Uso: python vfx.py [nombre ...]      (sin argumentos: todos)
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image  # noqa: E402
from lote import LOTE, a_paleta, anotar_registro  # noqa: E402
from pixelab_mcp import Client  # noqa: E402

from datetime import date  # noqa: E402

OUT = os.path.join(LOTE, "vfx")

HUMO_CLARO = ["#6c7874", "#94948c", "#b8b8b8", "#d4d0cc"]
POLVO = ["#543820", "#845c28", "#a86c50", "#b4a080"]

EFECTOS = [
    # nombre, preset, parches (lista de operaciones de render), descripción
    ("fogonazo", "impact_burst", [], "fogonazo de disparo"),
    ("rafaga", "smg_burst", [], "ráfaga de disparos con casquillos y humo"),
    ("explosion_pequena", "explosion", [{"op": "scale", "factor": 0.6}], "explosión pequeña"),
    ("explosion_media", "explosion", [], "explosión media"),
    ("explosion_grande", "ground_blast", [], "explosión grande de suelo"),
    ("fuego", "flame", [], "fuego en bucle"),
    ("fuego_grande", "flame", [{"op": "scale", "factor": 1.6}], "fuego grande en bucle"),
    ("humo", "smoke_puff", [], "bocanada de humo"),
    ("vapor", "smoke_puff", [{"op": "set", "path": "ramps.main", "value": HUMO_CLARO}], "vapor de locomotora"),
    ("chispas_via", "spark_hit", [], "chispas sobre el raíl"),
    ("sangre", "impact_burst", [{"op": "set", "path": "ramps.main", "value": "blood"}], "salpicadura de sangre"),
    ("impacto", "impact_burst", [], "impacto de chispa"),
    ("polvo_obra", "shockwave", [{"op": "set", "path": "ramps.main", "value": POLVO}], "polvo de obra"),
    ("niebla", "night_fog", [], "niebla baja en bucle"),
    ("brasas", "ash_embers", [], "brasas y ceniza en bucle"),
    ("lluvia", "slant_rain", [], "lluvia inclinada en bucle"),
    ("nieve", "snow_drift", [], "nieve en bucle"),
    ("gas_toxico", "toxic_cloud", [], "nube tóxica"),
]


def step_id(texto):
    m = re.search(r"(?:effect step|step):\s*([0-9a-f-]{36})", texto)
    return m.group(1) if m else None


def correr(c, argv):
    return c.call("vfx_workbench", {"argv": argv})


def hacer(c, nombre, preset, parches, desc):
    t = correr(c, ["start", "--preset", preset])
    sid = step_id(t)
    if not sid:
        raise RuntimeError("sin step: " + t[:200])
    if parches:
        t = correr(c, [sid, "render", json.dumps({"patch": parches})])
        sid = step_id(t) or sid
    t = correr(c, [sid, "export", "--name", "vm_vfx_" + nombre])
    m = re.search(r"download (https://\S+?/):\s*(.+)", t)
    if not m:
        raise RuntimeError("sin descarga: " + t[:300])
    base = m.group(1)
    archivos = [a.strip() for a in m.group(2).split(",")]
    os.makedirs(OUT, exist_ok=True)
    png = next(a for a in archivos if a.endswith(".png"))
    js = next((a for a in archivos if a.endswith(".json")), None)
    datos = urllib.request.urlopen(base + png, timeout=60).read()
    ruta_png = os.path.join(OUT, "vm_vfx_%s.png" % nombre)
    open(os.path.join(OUT, "_crudo_%s.png" % nombre), "wb").write(datos)
    from io import BytesIO
    a_paleta(Image.open(BytesIO(datos))).save(ruta_png)
    if js:
        open(os.path.join(OUT, "vm_vfx_%s.json" % nombre), "wb").write(urllib.request.urlopen(base + js, timeout=60).read())
    anotar_registro({"id": sid, "bloque": "vfx", "nombre": nombre, "herramienta": "vfx_workbench preset " + preset,
                     "prompt": desc, "semilla": "", "coste_generaciones": 0, "fecha": date.today().isoformat(),
                     "archivo": "assets/pixelab/lote/vfx/vm_vfx_%s.png" % nombre, "transparencia": "ok",
                     "paleta": "32 colores", "aprobado(s/n)": ""})
    return t


def main():
    pedidos = set(sys.argv[1:])
    c = Client()
    for nombre, preset, parches, desc in EFECTOS:
        if pedidos and nombre not in pedidos:
            continue
        try:
            t = hacer(c, nombre, preset, parches, desc)
            aviso = re.search(r"still warns:[^\n]*", t)
            print("OK  %-20s %s" % (nombre, (aviso.group(0)[:110] if aviso else "")), flush=True)
        except Exception as e:  # noqa: BLE001
            print("FALLO %s: %s" % (nombre, str(e)[:200]), flush=True)


if __name__ == "__main__":
    main()
