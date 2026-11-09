"""Efectos de sonido de Vía Muerta con ElevenLabs Text to Sound Effects v3 (Nuria, 7-nov-2026).

Endpoint: POST https://api.elevenlabs.io/v1/sound-generation?output_format=...
Cabecera xi-api-key. Cuerpo: text, model_id, duration_seconds, prompt_influence.
Modelo: eleven_text_to_sound_v3 (blog oficial «SFX v3 for developers»). El v3 no admite loop;
los bucles se hacen en postproceso_sfx.py. Si la API rechaza el modelo, el script se detiene:
NO cae a otro modelo.
La clave se lee SOLO de la variable de entorno ELEVENLABS_API_KEY; nunca se imprime ni se guarda.
Solo biblioteca estándar. Reanudable: salta los archivos que ya existen. 4 peticiones en paralelo.

Uso:  python generar_sfx.py <carpeta_brutos> [--prueba] [ids...]
"""
import argparse
import json
import os
import sys
import time
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

API = "https://api.elevenlabs.io/v1/sound-generation"
MODELO = "eleven_text_to_sound_v3"
FORMATO = "mp3_44100_192"
CATALOGO = json.loads((Path(__file__).resolve().parent / "catalogo_sfx.json").read_text(encoding="utf-8"))
parar = threading.Event()


def generar(clave, s):
    cuerpo = {"text": s["text"], "model_id": MODELO, "duration_seconds": s["dur"],
              "prompt_influence": s["infl"]}
    req = urllib.request.Request(f"{API}?output_format={FORMATO}", data=json.dumps(cuerpo).encode(),
                                 method="POST", headers={"xi-api-key": clave, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return r.read()


def tarea(clave, s, f):
    for intento in range(4):
        if parar.is_set():
            return {"archivo": f.name, "estado": "parado"}
        try:
            datos = generar(clave, s)
        except urllib.error.HTTPError as e:
            cuerpo = e.read().decode(errors="replace")[:400]
            if e.code in (400, 401, 402, 403, 404, 422):
                print("ERROR", e.code, f.name, cuerpo, flush=True)
                parar.set()
                return {"archivo": f.name, "estado": f"error_{e.code}", "detalle": cuerpo}
            print("reintento", e.code, f.name, flush=True)
            time.sleep(4 * (intento + 1))
            continue
        except Exception as e:
            print("reintento red", f.name, type(e).__name__, flush=True)
            time.sleep(4 * (intento + 1))
            continue
        # La llamada ya está cobrada: un fallo al guardar NO se reintenta (repetiría el cobro), se para todo.
        try:
            f.write_bytes(datos)
        except OSError as e:
            print("ERROR local al guardar (no se reintenta la llamada)", f.name, type(e).__name__, flush=True)
            parar.set()
            return {"archivo": f.name, "estado": "fallo_local"}
        print("ok", f.name, len(datos), flush=True)
        return {"archivo": f.name, "estado": "ok", "bytes": len(datos)}
    return {"archivo": f.name, "estado": "fallo"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--prueba", action="store_true")
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    clave = os.environ.get("ELEVENLABS_API_KEY")
    if not clave:
        sys.exit("Falta la variable de entorno ELEVENLABS_API_KEY")
    sonidos = CATALOGO["sonidos"]
    if a.ids:
        sonidos = [s for s in sonidos if s["id"] in a.ids]
    if a.prueba:
        sonidos = [dict(s, var=1) for s in sonidos if s["id"] == "g36e_cerca"]
    salida = Path(a.salida)
    trabajos = []
    for s in sonidos:
        (salida / s["grupo"]).mkdir(parents=True, exist_ok=True)
        for v in range(1, s["var"] + 1):
            f = salida / s["grupo"] / f"sfx_{s['id']}_v{v:02d}.mp3"
            if not (f.exists() and f.stat().st_size > 0):
                trabajos.append((s, f))
    print("pendientes:", len(trabajos), flush=True)
    with ThreadPoolExecutor(4) as ex:
        registro = list(ex.map(lambda t: tarea(clave, *t), trabajos))
    (salida / f"registro_{time.strftime('%Y%m%d_%H%M%S')}.json").write_text(json.dumps(
        {"modelo": MODELO, "formato": FORMATO, "archivos": registro}, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(r["estado"] == "ok" for r in registro)
    print(f"hecho: {ok}/{len(trabajos)} nuevos", flush=True)
    if parar.is_set():
        sys.exit(2)


if __name__ == "__main__":
    main()
