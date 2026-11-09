"""Pitido del tren v2: ganancia fija a -22,5 LUFS (mezcla de Lucía), Nuria, 9-nov-2026.

Parte de las copias v1 (entregas/sonido-obra-pitido/v1_pitido/) y escribe los OGG
con el mismo nombre en entregas/sonido-obra-pitido/. Sin limitador salvo que un
archivo pase de -3 dBFS de pico o -1 dBTP (entonces limitador suave, y se apunta).

  python pitido_v2.py
"""
import json, re, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ENT = RAIZ / "entregas" / "sonido-obra-pitido"
V1 = ENT / "v1_pitido"
OBJ = -22.5
PICO_MAX, TP_MAX = -3.0, -1.0


def medir(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af",
                        "ebur128=peak=true+sample", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    resumen = r[r.rfind("Summary:"):]
    i = float(re.search(r"I:\s+(-?[\d.]+) LUFS", resumen).group(1))
    tp = float(re.search(r"True peak:\s+Peak:\s+(-?[\d.]+)", resumen).group(1))
    sp = float(re.search(r"Sample peak:\s+Peak:\s+(-?[\d.]+)", resumen).group(1))
    return dict(lufs=i, pico=sp, tp=tp)


def codificar(src, dst, gain_db, limitar=False):
    af = f"volume={gain_db:.2f}dB"
    if limitar:
        af += ",alimiter=limit=-3dB:attack=5:release=50:level=disabled"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src),
                    "-af", af, "-ac", "1", "-ar", "44100", "-c:a", "libvorbis", "-q:a", "6",
                    str(dst)], check=True)


def main():
    out = []
    for src in sorted(V1.glob("sfx_tren_pitido_*.ogg")):
        antes = medir(src)
        dst = ENT / src.name
        g = OBJ - antes["lufs"]
        codificar(src, dst, g)
        d = medir(dst)
        if abs(d["lufs"] - OBJ) > 0.05:  # corrección fina por la resolución de 0,1 de la medida
            g += OBJ - d["lufs"]
            codificar(src, dst, g)
            d = medir(dst)
        lim = d["pico"] > PICO_MAX or d["tp"] > TP_MAX
        if lim:
            codificar(src, dst, g, limitar=True)
            d = medir(dst)
        out.append(dict(archivo=src.name, antes=antes, ganancia_db=round(g, 2), despues=d, limitador=lim))
        print(f"{src.name}: {antes['lufs']} -> {d['lufs']} LUFS, +{g:.2f} dB, pico {d['pico']}, TP {d['tp']}, limitador={lim}")
    (ENT / "medidas_pitido_v2.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    # medidas.json (lo lee la página de escucha) y prueba de conjunto con los pitidos nuevos
    from obra_pitido import medir_ogg, prueba
    mpath = ENT / "medidas.json"
    m = json.loads(mpath.read_text(encoding="utf-8"))
    for sid in ("tren_pitido_electrico", "tren_pitido_diesel"):
        for c in m["clips"][sid]:
            c.update(medir_ogg(ENT / c["archivo"]))
            c["version"] = "v2 (ganancia fija a -22,5 LUFS)"
    mpath.write_text(json.dumps(m, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    prueba(ENT, RAIZ / "entregas" / "sonido-salida-tren")


if __name__ == "__main__":
    sys.exit(main())
