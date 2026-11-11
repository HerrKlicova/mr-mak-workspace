"""Sonidos nuevos del Hito 1 del núcleo v2 (Nuria, 11-nov-2026). Tabla completa: docs/hito1/sonido-hito1.md.

ElevenLabs Text to Sound Effects v3 (eleven_text_to_sound_v3). La clave se lee SOLO de la variable de entorno
ELEVENLABS_API_KEY; nunca se imprime ni se guarda. Sin reintentos: si una llamada falla, el script para
(una llamada fallida puede estar cobrada y repetirla cobraría dos veces).

Pide 6 tomas de cada sonido y se queda con las 5 mejores. Gasto: 30 tomas, 136 s en total. A 6–12 créditos/s son
~820–1.640 créditos; el tope del script es de 1.800 (corta antes de pasarlo según la duración pedida).
Salida: entregas/sonido-hito1/sfx_<id>_1..5.ogg, mono, 44,1 kHz, nivel horneado (LUFS de la tabla) y pico ≤ −1,5 dBFS.
Los bucles («bucle» = True) se cierran con un fundido cruzado de 1,5 s. Necesita ffmpeg y numpy.

Uso (desde C:\\Dev\\mr-mak-workspace):  python herramientas\\sonido\\hito1_sonido.py
Reanudable: no vuelve a pedir las tomas que ya están en herramientas\\sonido\\brutos_hito1.
"""
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np

API = "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_192"
MODELO = "eleven_text_to_sound_v3"
RAIZ = Path(__file__).resolve().parents[2]
BRUTOS = RAIZ / "herramientas" / "sonido" / "brutos_hito1"
SALIDA = RAIZ / "entregas" / "sonido-hito1"
SR, TOMAS, QUEDAN, PICO_MAX, CRUCE = 44100, 6, 5, -1.5, 1.5
TOPE_CREDITOS, CR_POR_S = 1800, 12          # se calcula con el peor caso (12 créditos/s)

SONIDOS = [
    dict(id="via_tendido", dur=4.0, lufs=-24.0, bucle=False,
         text="Railway track crew working outdoors: heavy sledgehammer strikes driving steel spikes into wooden sleepers, "
              "metallic ringing, a steel rail dropped onto gravel ballast. No voices, no music."),
    dict(id="via_tramo_hecho", dur=2.0, lufs=-24.0, bucle=False,
         text="A heavy steel rail section clanks into place and a fishplate bolt is tightened with a wrench, "
              "short and solid, outdoors. No voices, no music."),
    dict(id="tren_rodando", dur=12.0, lufs=-22.0, bucle=True,
         text="Steady loop of a freight train rolling at medium speed heard from beside the track: rhythmic wheel clacks "
              "over rail joints, diesel engine hum, wagons creaking, constant level, no horn, no braking. No voices, no music."),
    dict(id="carga_material", dur=4.0, lufs=-24.0, bucle=False,
         text="Workers loading steel rails and wooden railway sleepers onto a flatbed wagon: heavy metal clanks, "
              "wood thuds, chains rattling, outdoors. No voices, no music."),
    dict(id="sin_municion_clic", dur=1.0, lufs=-28.0, bucle=False,
         text="An assault rifle trigger pulled on an empty magazine: two dry metallic clicks, close, no gunshot. "
              "No voices, no music."),
]


def pedir(clave, s):
    cuerpo = json.dumps({"text": s["text"], "model_id": MODELO, "duration_seconds": s["dur"],
                         "prompt_influence": 0.5}).encode()
    req = urllib.request.Request(API, data=cuerpo, method="POST",
                                 headers={"xi-api-key": clave, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return r.read()


def leer(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def lufs(x):
    """Sonoridad integrada aproximada (K-weighting con ffmpeg ebur128 sobre el array)."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", "ebur128", "-f", "null", "-"], input=x.astype(np.float32).tobytes(), capture_output=True)
    for linea in reversed(r.stderr.decode(errors="replace").splitlines()):
        if linea.strip().startswith("I:"):
            return float(linea.split()[1])
    return -99.0


def nota(x, bucle):
    """Mayor es mejor. 0 = toma muda. Sueltos: golpe claro (pico frente a RMS). Bucles: nivel estable en el tiempo."""
    rms = float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0
    if rms < 1e-3:
        return 0.0
    if not bucle:
        return float(np.max(np.abs(x)) / rms)
    w = SR // 2
    tramos = [np.sqrt(np.mean(x[i:i + w] ** 2)) + 1e-9 for i in range(0, len(x) - w, w)]
    var_db = 20 * np.log10(max(tramos) / min(tramos))
    return 1.0 / (1.0 + var_db)


def cerrar_bucle(x):
    n = int(CRUCE * SR)
    cola, cuerpo = x[-n:], x[:-n].copy()
    f = np.linspace(0, 1, n)
    cuerpo[:n] = cuerpo[:n] * np.sqrt(f) + cola * np.sqrt(1 - f)
    return cuerpo


def guardar(x, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-c:a", "libvorbis", "-q:a", "6", str(dst)], input=x.astype(np.float32).tobytes(), check=True)


def main():
    clave = os.environ.get("ELEVENLABS_API_KEY")
    if not clave:
        sys.exit("Falta la variable de entorno ELEVENLABS_API_KEY")
    BRUTOS.mkdir(parents=True, exist_ok=True)
    SALIDA.mkdir(parents=True, exist_ok=True)
    gasto = 0.0
    for s in SONIDOS:
        for i in range(1, TOMAS + 1):
            f = BRUTOS / f"{s['id']}_v{i:02d}.mp3"
            if f.exists() and f.stat().st_size > 0:
                continue
            if gasto + s["dur"] * CR_POR_S > TOPE_CREDITOS:
                sys.exit(f"Tope de {TOPE_CREDITOS} créditos: paro antes de {f.name}")
            gasto += s["dur"] * CR_POR_S
            try:
                datos = pedir(clave, s)
            except Exception as e:  # sin reintentos (puede estar cobrada)
                sys.exit(f"ERROR en {f.name}: {type(e).__name__} {getattr(e, 'code', '')}. Paro sin reintentar.")
            f.write_bytes(datos)
            print("ok", f.name, len(datos), flush=True)
    print(f"créditos estimados de esta tanda (peor caso): {gasto:.0f}")
    for s in SONIDOS:
        tomas = sorted(BRUTOS.glob(f"{s['id']}_v*.mp3"))
        notas = [(nota(leer(t), s["bucle"]), t) for t in tomas]
        buenas = [t for n, t in sorted(notas, key=lambda p: -p[0]) if n > 0][:QUEDAN]
        print(s["id"], "notas:", ", ".join(f"{t.stem}={n:.2f}" for n, t in notas))
        if len(buenas) < QUEDAN:
            print(f"AVISO: solo {len(buenas)} tomas válidas de {s['id']}")
        for k, t in enumerate(buenas, 1):
            x = leer(t)
            if s["bucle"]:
                x = cerrar_bucle(x)
            x = x * 10 ** ((s["lufs"] - lufs(x)) / 20)
            pk = 20 * np.log10(np.max(np.abs(x)) + 1e-12)
            if pk > PICO_MAX:
                x = x * 10 ** ((PICO_MAX - pk) / 20)
            dst = SALIDA / f"sfx_{s['id']}_{k}.ogg"
            guardar(x, dst)
            print(f"{dst.name}: {t.stem}, {lufs(x):.1f} LUFS, pico {20 * np.log10(np.max(np.abs(x)) + 1e-12):.1f}")
    print("hecho")


if __name__ == "__main__":
    main()
