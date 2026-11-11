"""Puerta de vehículos E4 de Sagunto (D-N198): apertura y cierre. Nuria, 11-nov-2026.

ElevenLabs Text to Sound Effects v3 (eleven_text_to_sound_v3). La clave se lee SOLO de la variable de entorno
ELEVENLABS_API_KEY; nunca se imprime ni se guarda. Sin reintentos: si una llamada falla, el script para
(una llamada fallida puede estar cobrada y repetirla cobraría dos veces).

Gasto: 6 tomas de apertura y 6 de cierre, de 5 s cada una, a unos 12 créditos/s, son ~720 créditos (tope 900).
Se quedan las 5 mejores de cada una (descarta las mudas o sin golpe final).
Salida: entregas/sonido-puerta-e4/sfx_puerta_e4_{abrir,cerrar}_1..5.ogg, mono, 44,1 kHz,
a −24,0 LUFS y con un pico de −1,5 dBFS como mucho (nivel horneado, como los vehículos). Necesita ffmpeg en el PATH.

Uso (desde C:\\Dev\\mr-mak-workspace):  python herramientas\\sonido\\puerta_e4.py
Es reanudable: no vuelve a pedir las tomas que ya están en brutos.
"""
import json
import math
import os
import struct
import subprocess
import sys
import urllib.request
from pathlib import Path

API = "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_192"
MODELO = "eleven_text_to_sound_v3"
RAIZ = Path(__file__).resolve().parents[2]
BRUTOS = RAIZ / "herramientas" / "sonido" / "brutos_puerta_e4"
SALIDA = RAIZ / "entregas" / "sonido-puerta-e4"
OBJ_LUFS, PICO_MAX, TOMAS, QUEDAN, DUR = -24.0, -1.5, 6, 5, 5.0
TOPE_LLAMADAS = 12
PROMPTS = {
    "abrir": "Heavy steel military vehicle gate sliding open on rusty rollers outdoors, metal grinding and rattling, "
             "loose chain-link mesh shaking, ends with a solid metal stop thud. No voices, no music.",
    "cerrar": "Heavy steel military vehicle gate sliding shut on rollers outdoors, grinding metal, then a loud latch clank "
              "and a steel bolt locking. No voices, no music.",
}


def pedir(clave, texto):
    cuerpo = json.dumps({"text": texto, "model_id": MODELO, "duration_seconds": DUR, "prompt_influence": 0.5}).encode()
    req = urllib.request.Request(API, data=cuerpo, method="POST",
                                 headers={"xi-api-key": clave, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return r.read()


def muestras(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-f", "f32le", "-ac", "1", "-ar", "44100", "-"],
                         capture_output=True, check=True).stdout
    return struct.unpack(f"<{len(raw) // 4}f", raw)


def lufs(f):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(f), "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True)
    for linea in reversed(r.stderr.splitlines()):
        if linea.strip().startswith("I:"):
            return float(linea.split()[1])
    return -99.0


def nota(x):
    """Toma válida si no es muda y tiene un golpe final (el tope o el cerrojo) en el último 40 %."""
    if not x:
        return -1.0
    rms = math.sqrt(sum(v * v for v in x) / len(x))
    if rms < 1e-3:
        return -1.0
    cola = x[int(len(x) * 0.6):]
    pico_cola = max(abs(v) for v in cola)
    return pico_cola / rms


def main():
    clave = os.environ.get("ELEVENLABS_API_KEY")
    if not clave:
        sys.exit("Falta la variable de entorno ELEVENLABS_API_KEY")
    BRUTOS.mkdir(parents=True, exist_ok=True)
    SALIDA.mkdir(parents=True, exist_ok=True)
    llamadas = 0
    for nombre, texto in PROMPTS.items():
        for i in range(1, TOMAS + 1):
            f = BRUTOS / f"{nombre}_v{i:02d}.mp3"
            if f.exists() and f.stat().st_size > 0:
                continue
            if llamadas >= TOPE_LLAMADAS:
                sys.exit("Tope de llamadas alcanzado: paro")
            llamadas += 1
            try:
                datos = pedir(clave, texto)
            except Exception as e:  # sin reintentos (puede estar cobrada)
                sys.exit(f"ERROR en {f.name}: {type(e).__name__} {getattr(e, 'code', '')}. Paro sin reintentar.")
            f.write_bytes(datos)
            print("ok", f.name, len(datos), flush=True)
    print(f"llamadas nuevas: {llamadas} (~{llamadas * DUR * 12:.0f} créditos)")
    for nombre in PROMPTS:
        tomas = sorted(BRUTOS.glob(f"{nombre}_v*.mp3"))
        notas = [(nota(muestras(t)), t) for t in tomas]
        buenas = [t for n, t in sorted(notas, key=lambda p: -p[0]) if n > 0][:QUEDAN]
        print(nombre, "notas:", ", ".join(f"{t.stem}={n:.1f}" for n, t in notas))
        if len(buenas) < QUEDAN:
            print(f"AVISO: solo {len(buenas)} tomas válidas de {nombre}")
        for k, t in enumerate(buenas, 1):
            dst = SALIDA / f"sfx_puerta_e4_{nombre}_{k}.ogg"
            l0 = lufs(t)
            gan = OBJ_LUFS - l0
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(t), "-ac", "1", "-ar", "44100",
                            "-af", f"volume={gan:.2f}dB,alimiter=limit={10 ** (PICO_MAX / 20):.4f}:level=disabled",
                            "-c:a", "libvorbis", "-q:a", "6", str(dst)], check=True)
            print(f"{dst.name}: {t.stem}, {l0:.1f} → {lufs(dst):.1f} LUFS")
    print("hecho")


if __name__ == "__main__":
    main()
