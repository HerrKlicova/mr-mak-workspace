"""Retratos del equipo con ElevenLabs Image & Video (6-nov-2026).

API oficial: POST https://api.elevenlabs.io/v1/flows/image  y  GET /v1/flows/image/{id}
(docs: elevenlabs.io/docs/api-reference/flows/image/create). Requiere plan Pro.
La clave se lee SOLO de la variable de entorno ELEVENLABS_API_KEY; nunca se imprime ni se guarda.
Solo biblioteca estándar.

Uso:  python generar_retratos.py <salida_brutos> [ids...]   (sin ids: los de "prueba")
      python generar_retratos.py <salida_brutos> --todos
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.elevenlabs.io/v1/flows/image"
CONF = json.loads((Path(__file__).resolve().parent / "retratos_equipo.json").read_text(encoding="utf-8"))


def pedir(metodo, url, cuerpo=None):
    clave = os.environ.get("ELEVENLABS_API_KEY")
    if not clave:
        sys.exit("Falta la variable de entorno ELEVENLABS_API_KEY")
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo,
                                 headers={"xi-api-key": clave, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"status": "http_error", "code": e.code, "body": e.read().decode(errors="replace")[:500]}


def main():
    salida = Path(sys.argv[1])
    salida.mkdir(parents=True, exist_ok=True)
    ids = sys.argv[2:] or CONF["prueba"]
    if ids == ["--todos"]:
        ids = list(CONF["miembros"])
    trabajos = {}
    for m in ids:
        cuerpo = {"model_id": CONF["modelo"], "prompt": CONF["prefijo"] + CONF["miembros"][m],
                  "aspect_ratio": "1:1", "resolution": "1K"}
        r = pedir("POST", API, cuerpo)
        print(m, "->", r.get("status"), r.get("id", r))
        if r.get("id"):
            trabajos[m] = r["id"]
    registro = {}
    fin = time.time() + 600
    while trabajos and time.time() < fin:
        time.sleep(5)
        for m, gid in list(trabajos.items()):
            r = pedir("GET", f"{API}/{gid}")
            st = r.get("status")
            if st == "completed":
                ext = ".png" if "png" in r.get("content_mime_type", "png") else ".jpg"
                destino = salida / f"bruto_{m}{ext}"
                with urllib.request.urlopen(r["content_url"], timeout=120) as f:
                    destino.write_bytes(f.read())
                registro[m] = {"id": gid, "archivo": destino.name, "mime": r.get("content_mime_type")}
                print("ok", m, destino.name)
                del trabajos[m]
            elif st in ("failed", "http_error"):
                registro[m] = {"id": gid, "error": r}
                print("FALLO", m, r)
                del trabajos[m]
    for m in trabajos:
        print("SIN TERMINAR", m, trabajos[m])
    (salida / f"registro_{int(time.time())}.json").write_text(json.dumps(registro, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
