"""Ambiente de día de Sagunto y de Nules, y transición del atardecer (Nuria, 9-nov-2026). Encargo de Lucía, D-N157.

Mismo método que farp_nules_avisos.py: ElevenLabs eleven_text_to_sound_v3, clave SOLO de ELEVENLABS_API_KEY (nunca se
imprime ni se guarda). Si la API rechaza el modelo, se detiene y no cae a otro.
Todo mono, 44,1 kHz, OGG Vorbis, nivel horneado por sonoridad integrada (LUFS) y sin normalizar al importar.

Referencia (medida en 8baca89, sin tocar los archivos de Unity): en la zona, la noche suena con
sfx_amb_estacion_pequena_1 (−30,0 LUFS) a 0,10 → nivel efectivo −50,0 LUFS (cámara cerca).
- Día (Sagunto y Nules): 3 dB por debajo → −53,0 LUFS sonando a 1,0. Bucles de 20 s con fundido cruzado de 1,5 s.
- Atardecer: 1,5 dB por debajo de la noche → −51,5 LUFS. 20 s sin bucle: el día se apaga y acaba en el carácter
  de la noche, para fundirlo 3 s con el ambiente de noche.
Descartes: tomas mudas (HTTP 200 sin señal), insectos (chicharras o grillos: un pico agudo fijo y sostenido),
música o voces (varios tonos sostenidos distintos), y en los bucles los sucesos que se reconocerían al repetirse.

Uso:
  python ambiente_dia.py creditos
  python ambiente_dia.py generar <brutos> [ids...]          (reanudable)
  python ambiente_dia.py extra <brutos> <id> <sufijo> <n>   (n tomas más de un prompt)
  python ambiente_dia.py calibrar                           (prueba los detectores con sonidos ya entregados)
  python ambiente_dia.py post <brutos> <entrega>              (renumera TODO: no usar si ya hay variantes en el juego)
  python ambiente_dia.py completar <brutos> <entrega>         (solo tomas nuevas, a números libres; no pisa nada)
  python ambiente_dia.py escucha <entrega>
"""
import base64
import html
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from farp_nules_avisos import lanzar, trabajos_de, medir_ogg, num  # noqa: E402
from maquina_escribir import SR, a_ogg, creditos, db, leer, lufs  # noqa: E402
from nh90_betera import bucle, costura, cruce_cero, sucesos as sucesos_bucle, ventana_estable  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
NOCHE = Path(r"C:\Dev\TBD\Assets\TBD\Resources\Audio\sfx_amb_estacion_pequena_1.ogg")
NOCHE_VOL = 0.10
NOCHE_LUFS = -30.0                                   # medido (ebur128, estéreo y mezcla mono dan lo mismo)
NOCHE_EFECTIVO = NOCHE_LUFS + 20 * np.log10(NOCHE_VOL)   # −50,0
DIA_LUFS = round(NOCHE_EFECTIVO - 3.0, 1)            # −53,0
ATARDECER_LUFS = round(NOCHE_EFECTIVO - 1.5, 1)      # −51,5

AMB = ", isolated ambience, no music, no voices, no speech, no talking"
SONIDOS = {
    "dia_sagunto": dict(tipo="bucle", lufs=DIA_LUFS, largo=20.0, cruce=1.5, prompts=[
        ("a", "quiet small Spanish town railway station next to farmland on a cool November morning, soft gentle "
              "breeze, a few distant sparrows chirping now and then, a train rumbling faintly very far away, faint "
              "hum of an almost empty town in the background, calm and steady, late autumn, no insects" + AMB,
         22.0, 0.5, 2),
        ("b", "calm late autumn morning at the edge of a small town beside orchards, light wind, sparse occasional "
              "sparrow chirps, very distant railway sound and a faint far-off overhead line hum, distant quiet "
              "empty town, steady and even, no crickets, no cicadas" + AMB, 22.0, 0.5, 2),
        ("c", "outskirts of an empty small town on a cold quiet morning, soft wind, a few far-away birds, a "
              "faraway train on a railway line, very low distant city hum, constant and unchanging, no insects"
         + AMB, 22.0, 0.5, 1),
    ]),
    "dia_nules": dict(tipo="bucle", lufs=DIA_LUFS, largo=20.0, cruce=1.5, prompts=[
        ("a", "orange grove on a cool November morning, gentle breeze rustling orange tree leaves, a few sparse "
              "sparrows far away, very quiet trickle of an irrigation ditch, a train on a railway line far away, "
              "calm and steady, late autumn, no insects" + AMB, 22.0, 0.5, 2),
        ("b", "Mediterranean citrus orchard in the morning in late autumn, soft wind in the leaves, occasional "
              "distant bird chirp, a very faint low water trickle in a small channel, faint faraway railway "
              "rumble, constant and even, no crickets, no cicadas" + AMB, 22.0, 0.5, 2),
        ("c", "quiet orange orchard on a cold calm morning, light leaf rustle in a soft breeze, sparse far birds, "
              "barely audible water trickle, very distant train, steady, no insects" + AMB, 22.0, 0.5, 1),
    ]),
    "atardecer": dict(tipo="transicion", lufs=ATARDECER_LUFS, largo=20.0, prompts=[
        ("a", "late autumn dusk in farmland near a small town: at first a few sparrows chirping and a soft breeze, "
              "then the birds gradually fall silent and the wind slowly grows a little stronger and colder, ending "
              "in an empty, quiet, cold evening with only the wind, no insects, no crickets" + AMB, 20.3, 0.5, 3),
        ("b", "transition from late afternoon to nightfall in a November orchard, birds slowly going quiet one by "
              "one, light wind rising slightly, ending empty, still and cold with a faint distant hum, no insects, "
              "no crickets, no cicadas" + AMB, 20.3, 0.5, 2),
    ]),
}
SALIDA = {"dia_sagunto": "sfx_amb_dia_sagunto", "dia_nules": "sfx_amb_dia_nules", "atardecer": "sfx_amb_atardecer"}
N_FINAL = 5
TECHO = -1.5


def generar(brutos, ids):
    brutos = Path(brutos)
    brutos.mkdir(parents=True, exist_ok=True)
    t = []
    for sid, s in SONIDOS.items():
        if not ids or sid in ids:
            t += trabajos_de(brutos, sid, s)
    lanzar(t)


def extra(brutos, sid, suf, n):
    Path(brutos).mkdir(parents=True, exist_ok=True)   # sin esto el guardado falla y la API cobra cada reintento
    lanzar(trabajos_de(Path(brutos), sid, SONIDOS[sid], suf, int(n)))


# ---------- detectores ----------
def filtro(x, af):
    r = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", af,
                        "-f", "f32le", "-"], input=x.astype(np.float32).tobytes(), capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()[:len(x)]


def banda(x, lo=None, hi=None, orden=4):
    """Filtro empinado (cada pasada de ffmpeg es de 12 dB/oct; 4 pasadas = 8.º orden)."""
    af = []
    if lo:
        af += [f"highpass=f={lo}"] * orden
    if hi:
        af += [f"lowpass=f={hi}"] * orden
    return filtro(x, ",".join(af))


def picos_locales(x, fmin, fmax, tr, ancho_hz=400):
    """Por trama: (Hz, prominencia local en dB) del pico más destacado en fmin..fmax. La prominencia se mide contra el
    espectro suavizado (mediana móvil de `ancho_hz`), no contra la mediana de todo el espectro: en un ambiente con
    más graves que agudos, cualquier trama grave «destaca» 30–45 dB sobre la mediana global sin ser un tono."""
    n = int(SR * tr)
    f = np.fft.rfftfreq(n, 1 / SR)
    w = max(5, int(ancho_hz / (f[1] - f[0])) | 1)
    m = np.where((f >= fmin * 1.1) & (f <= fmax / 1.1))[0]    # fuera los bordes de la banda
    k = (len(x) - n) // n
    fr = x[:k * n].reshape(k, n) * np.hanning(n)
    sp = 20 * np.log10(np.abs(np.fft.rfft(fr, axis=1)) + 1e-9)
    pad = np.pad(sp, ((0, 0), (w // 2, w // 2)), mode="edge")
    suave = np.median(np.lib.stride_tricks.sliding_window_view(pad, w, axis=1), axis=2)
    r = (sp - suave)[:, m]
    j = np.argmax(r, axis=1)
    out = [(float(f[m][jj]), float(r[i, jj])) for i, jj in enumerate(j)]
    return out


def _suave_mediana(v, w):
    pad = np.pad(v, (w // 2, w // 2), mode="edge")
    return np.median(np.lib.stride_tricks.sliding_window_view(pad, w), axis=-1)


def insectos(x, fmin=2500, fmax=10000):
    """Chicharras o grillos: un bulto estrecho en el espectro medio de la toma (2,5–10 kHz; espectro suavizado a 100 Hz
    frente a la mediana móvil de 3 kHz) que además está en casi todas las tramas de 0,5 s (banda ±6 % frente a sus
    flancos, > 4 dB). Calibrado con los grillos de Nules (bulto 11,9–25,1 dB, presente en el 100 % de las tramas)
    frente a viento, acequia y la noche actual (≤ 5,8 dB) y a pájaros sueltos (≤ 27 % de las tramas).
    Devuelve (bulto dB, Hz, fracción de tramas)."""
    n = 4096
    k = len(x) // n
    P = np.mean(np.abs(np.fft.rfft(x[:k * n].reshape(k, n) * np.hanning(n), axis=1)) ** 2, axis=0)
    f = np.fft.rfftfreq(n, 1 / SR)
    L = 10 * np.log10(P + 1e-20)
    r = np.convolve(L, np.ones(9) / 9, "same") - _suave_mediana(L, int(3000 / (f[1] - f[0])) | 1)
    m = (f >= fmin) & (f <= fmax)
    j = int(np.argmax(r[m]))
    hz, bulto = float(f[m][j]), float(r[m][j])
    n = int(SR * 0.5)
    k = len(x) // n
    Q = np.abs(np.fft.rfft(x[:k * n].reshape(k, n) * np.hanning(n), axis=1)) ** 2
    g = np.fft.rfftfreq(n, 1 / SR)
    c = (g > hz * 0.94) & (g < hz * 1.06)
    fl = ((g > hz * 0.76) & (g < hz * 0.88)) | ((g > hz * 1.12) & (g < hz * 1.24))
    d = 10 * np.log10(Q[:, c].mean(1) / (Q[:, fl].mean(1) + 1e-20) + 1e-20)
    return round(bulto, 1), round(hz), round(float(np.mean(d > 4)), 2)


def tonos_sostenidos(x, fmin=150, fmax=2000, seg=0.3, umbral=12):
    """Música o voz: tramos de `seg` s o más con un pico de prominencia local > `umbral` dB fijo (±3 %). Un zumbido de
    catenaria da un solo tono; la música o una voz dan varios. Devuelve la lista de Hz distintos (agrupados al 6 %)."""
    picos = picos_locales(x, fmin, fmax, 0.1, 150)
    tramos, run = [], [picos[0]]
    for p in picos[1:] + [(0.0, -99.0)]:
        if p[1] > umbral and run[-1][1] > umbral and abs(p[0] - run[-1][0]) <= 0.03 * p[0]:
            run.append(p)
        else:
            if len(run) * 0.1 >= seg and run[-1][1] > umbral:
                tramos.append(np.median([q[0] for q in run]))
            run = [p]
    distintos = []
    for h in tramos:
        if all(abs(h / d - 1) > 0.06 for d in distintos):
            distintos.append(h)
    return [round(float(h)) for h in distintos]


def env_db(x, ms=20):
    n = int(SR * ms / 1000)
    m = len(x) // n
    return 10 * np.log10(np.mean(x[:m * n].reshape(m, n) ** 2, axis=1) + 1e-12)


def pios(x, ms=20, salto=8):
    """Trinos: tramas de la banda 2–8 kHz que pasan `salto` dB la mediana móvil de 1 s. Devuelve tiempos (s)."""
    e = env_db(banda(x, 2000, 8000), ms)
    w = int(1000 / ms)
    med = np.array([np.median(e[max(0, i - w // 2):i + w // 2 + 1]) for i in range(len(e))])
    on = np.where(e - med > salto)[0]
    out, ult = [], -999
    for i in on:
        if i - ult > 5:
            out.append(round(i * ms / 1000, 2))
        ult = i
    return out


def calibrar():
    """Validar los instrumentos antes de fiarse de un cero: grillos de Nules (deben dar insectos) frente a viento y
    acequia (no), y el ambiente de noche actual."""
    e = RAIZ / "entregas" / "sonido-farp-nules-avisos"
    for nombre in ("sfx_amb_nules_grillos_1", "sfx_amb_nules_grillos_3", "sfx_amb_nules_viento_1",
                   "sfx_amb_nules_acequia_1"):
        x = leer(e / f"{nombre}.ogg")
        print(nombre, "insectos", insectos(x), "tonos", tonos_sostenidos(x), "pios", len(pios(x)))
    x = leer(NOCHE)
    print("noche estación", "insectos", insectos(x), "tonos", tonos_sostenidos(x), "pios", len(pios(x)),
          "LUFS", round(lufs(x)[0], 1))


# ---------- candidatas ----------
def comunes(x, info):
    pk = db(np.abs(x).max())
    li = round(lufs(x)[0], 1)
    info.update(pico_bruto=round(pk, 1), lufs_bruto=li, dur_bruta=round(len(x) / SR, 2))
    if pk < -55 or li < -62:   # suelo relativo a un objetivo de −53: −54 en bruto es una toma válida
        return f"muda o casi muda ({li} LUFS en bruto, pico {round(pk, 1)} dBFS)"
    bulto, hz, frac = insectos(x)
    info.update(insectos_bulto_db=bulto, insectos_hz=hz, insectos_tramas=frac)
    if bulto >= 8 and frac >= 0.6:
        return f"insectos: banda fija a {hz} Hz, {bulto} dB, en el {round(frac * 100)} % de las tramas (chicharras o grillos)"
    ts = tonos_sostenidos(x)
    info["tonos_sostenidos_hz"] = ts
    if len(ts) >= 3:
        return f"{len(ts)} tonos sostenidos distintos ({ts} Hz): posible música o voz"
    return None


def candidata(sid, s, f):
    x = leer(f)
    info = {"toma": f.name}
    motivo = comunes(x, info)
    if motivo:
        return None, {**info, "motivo": motivo}
    if s["tipo"] == "bucle":
        F = s["cruce"]
        a0, rango = ventana_estable(x, s["largo"], F)
        if a0 is None or a0 + int(s["largo"] * SR) > len(x):
            return None, {**info, "motivo": f"demasiado corta para un bucle de {s['largo']:.0f} s"}
        a = cruce_cero(x, a0, int(0.004 * SR))
        b = cruce_cero(x, a + int(s["largo"] * SR), int(0.003 * SR))
        if b > len(x):
            return None, {**info, "motivo": "no cabe el bucle"}
        y = bucle(x, a, b, F)
        sp, rg = sucesos_bucle(y)
        info.update(rango_lufs_ventana=rango, dur_bucle=round(len(y) / SR, 3), suceso_max_db=sp, rango_p5_p95_db=rg,
                    pios=len(pios(y)), **costura(y))
        if sp > 6.0:
            return None, {**info, "motivo": f"suceso que destaca {sp} dB sobre la mediana (se notaría al repetirse)"}
        if rango > 4.6:   # 4,0 dejaba fuera una toma de 4,03; 4,5 una de 4,57 (nules_a_v04: costura 0,46 frente a 1,72, suceso 1,8, p5–p95 2,9)
            return None, {**info, "motivo": f"nivel inestable ({rango} dB de variación en la ventana)"}
        if info["salto_union_db"] > max(info["salto_dentro_p95_db"], 0.5):
            return None, {**info, "motivo": "la costura salta más que el 95 % de los saltos dentro del bucle"}
        return y, info
    # transición: 20 s desde el principio, con 30 ms de fundido de entrada y de salida (sin clic)
    n = int(s["largo"] * SR)
    if len(x) < n:
        return None, {**info, "motivo": f"demasiado corta ({len(x) / SR:.1f} s < {s['largo']} s)"}
    y = x[:n].copy()
    k = int(0.03 * SR)
    y[:k] *= np.linspace(0, 1, k)
    y[-k:] *= np.linspace(1, 0, k)
    p = pios(y)
    t1 = sum(1 for v in p if v < 7)
    t3 = sum(1 for v in p if v >= 13)
    grave = banda(y, None, 400)
    g1, g3 = round(lufs(grave[:5 * SR])[0], 1), round(lufs(grave[-5 * SR:])[0], 1)
    cola = y[-6 * SR:]
    sp, _ = sucesos_bucle(cola)
    info.update(pios_0_7s=t1, pios_13_20s=t3, viento_grave_ini=g1, viento_grave_fin=g3,
                viento_sube_db=round(g3 - g1, 1), suceso_final_db=sp)
    if t1 < 2:
        return None, {**info, "motivo": f"casi sin pájaros al principio ({t1} trinos en 0–7 s)"}
    if t3 > max(1, t1 // 3):
        return None, {**info, "motivo": f"los pájaros no se callan ({t1} trinos al principio, {t3} al final)"}
    if g3 - g1 < -1.0:
        return None, {**info, "motivo": f"el viento baja {round(g1 - g3, 1)} dB en vez de subir"}
    if sp > 6.0:
        return None, {**info, "motivo": f"el final no es estable (suceso de {sp} dB en los últimos 6 s)"}
    return y, info


def a_lufs(x, objetivo, es_bucle):
    i, _ = lufs(np.tile(x, 3) if es_bucle else x)
    return x * 10 ** ((objetivo - i) / 20)


def post(brutos, entrega):
    brutos, entrega = Path(brutos), Path(entrega)
    entrega.mkdir(parents=True, exist_ok=True)
    informe = {"referencia": {"noche_archivo": NOCHE.name, "noche_lufs": NOCHE_LUFS, "noche_vol": NOCHE_VOL,
                              "noche_efectivo": round(NOCHE_EFECTIVO, 1), "dia_lufs": DIA_LUFS,
                              "atardecer_lufs": ATARDECER_LUFS},
               "clips": {}, "descartes": [], "candidatas": {}}
    for sid, s in SONIDOS.items():
        es_bucle = s["tipo"] == "bucle"
        cand = []
        for f in sorted(brutos.glob(f"{sid}_*.mp3")):
            y, info = candidata(sid, s, f)
            if y is None:
                informe["descartes"].append(info)
            else:
                cand.append({**info, "y": y})
        informe["candidatas"][sid] = [{k: v for k, v in c.items() if k != "y"} for c in cand]
        if es_bucle:   # las 5 con menos sucesos y nivel más estable
            cand.sort(key=lambda c: c["suceso_max_db"] + 0.5 * c["rango_lufs_ventana"])
        else:          # las 5 con el apagado de pájaros más claro y el final más estable
            cand.sort(key=lambda c: c["pios_13_20s"] - 0.2 * c["pios_0_7s"] + 0.3 * c["suceso_final_db"])
        elegidas, resto = cand[:N_FINAL], cand[N_FINAL:]
        if len(elegidas) < N_FINAL:
            print(f"AVISO: {sid}: solo {len(elegidas)} válidas", flush=True)
        informe["clips"][sid] = []
        for k, c in enumerate(elegidas, 1):
            dest = entrega / f"{SALIDA[sid]}_{k}.ogg"
            y = a_lufs(c["y"], s["lufs"], es_bucle)
            if np.abs(y).max() > 10 ** (TECHO / 20):
                y = y * 10 ** (TECHO / 20) / np.abs(y).max()
            a_ogg(y, dest)
            for _ in range(3):   # el Vorbis mueve la sonoridad unas décimas: se corrige midiendo el OGG
                m = medir_ogg(dest, es_bucle)["lufs_i"]
                if abs(m - s["lufs"]) <= 0.1:
                    break
                y = y * 10 ** ((s["lufs"] - m) / 20)
                a_ogg(y, dest)
            m = medir_ogg(dest, es_bucle)
            if es_bucle:
                z = leer(dest)
                m["costura_ogg"] = costura(z)
                m["muestras_ogg"] = len(z)
                m["muestras_bucle"] = len(c["y"])
            informe["clips"][sid].append({"archivo": dest.name, "de": c["toma"],
                                          **{k2: c[k2] for k2 in ("suceso_max_db", "rango_lufs_ventana", "pios",
                                                                  "pios_0_7s", "pios_13_20s", "viento_sube_db",
                                                                  "suceso_final_db", "insectos_bulto_db", "insectos_tramas",
                                                                  "tonos_sostenidos_hz") if k2 in c}, **m})
        for c in resto:
            informe["descartes"].append({k: v for k, v in c.items() if k != "y"} |
                                        {"motivo": "válida, sobrante (fuera de las 5 elegidas)"})
    (entrega / "medidas.json").write_text(json.dumps(informe, ensure_ascii=False, indent=1, default=float),
                                          encoding="utf-8")
    for sid, cl in informe["clips"].items():
        L = [c["lufs_i"] for c in cl]
        print(sid, len(cl), "LUFS", min(L, default=0), max(L, default=0), "pico máx",
              max([c["pico_dbfs"] for c in cl], default=0), "dur", [c["dur_s"] for c in cl],
              "costura", [c.get("costura_ogg") for c in cl])
    print("descartes:", json.dumps([(d["toma"], d["motivo"]) for d in informe["descartes"]], ensure_ascii=False,
                                   indent=0))


def completar(brutos, entrega):
    """Rellena los huecos hasta N_FINAL SIN tocar los OGG ya entregados (algunos ya están en el juego): solo se
    analizan las tomas que no aparecen en medidas.json (ni como origen de un clip ni como descarte) y se escriben con
    el número siguiente libre. Añade sus medidas y descartes a medidas.json."""
    brutos, entrega = Path(brutos), Path(entrega)
    mj = entrega / "medidas.json"
    informe = json.loads(mj.read_text(encoding="utf-8"))
    vistas = {c["de"] for cl in informe["clips"].values() for c in cl} | {d["toma"] for d in informe["descartes"]}
    nuevas_desc = []
    for sid, s in SONIDOS.items():
        es_bucle = s["tipo"] == "bucle"
        cl = informe["clips"].setdefault(sid, [])
        hay = len(cl)
        tomas = [f for f in sorted(brutos.glob(f"{sid}_*.mp3")) if f.name not in vistas]
        if not tomas:
            continue
        cand = []
        for f in tomas:
            y, info = candidata(sid, s, f)
            if y is None:
                nuevas_desc.append(info)
            else:
                cand.append({**info, "y": y})
        informe["candidatas"].setdefault(sid, []).extend({k: v for k, v in c.items() if k != "y"} for c in cand)
        if es_bucle:
            cand.sort(key=lambda c: c["suceso_max_db"] + 0.5 * c["rango_lufs_ventana"])
        else:
            cand.sort(key=lambda c: c["pios_13_20s"] - 0.2 * c["pios_0_7s"] + 0.3 * c["suceso_final_db"])
        faltan = max(0, N_FINAL - hay)
        elegidas, resto = cand[:faltan], cand[faltan:]
        if len(elegidas) < faltan:
            print(f"AVISO: {sid}: faltan {faltan} y solo hay {len(elegidas)} válidas nuevas", flush=True)
        for k, c in enumerate(elegidas, hay + 1):
            dest = entrega / f"{SALIDA[sid]}_{k}.ogg"
            if dest.exists():
                sys.exit(f"ALTO: {dest.name} ya existe y no se pisa")
            y = a_lufs(c["y"], s["lufs"], es_bucle)
            if np.abs(y).max() > 10 ** (TECHO / 20):
                y = y * 10 ** (TECHO / 20) / np.abs(y).max()
            a_ogg(y, dest)
            for _ in range(3):
                m = medir_ogg(dest, es_bucle)["lufs_i"]
                if abs(m - s["lufs"]) <= 0.1:
                    break
                y = y * 10 ** ((s["lufs"] - m) / 20)
                a_ogg(y, dest)
            m = medir_ogg(dest, es_bucle)
            if es_bucle:
                z = leer(dest)
                m["costura_ogg"] = costura(z)
                m["muestras_ogg"] = len(z)
                m["muestras_bucle"] = len(c["y"])
            cl.append({"archivo": dest.name, "de": c["toma"],
                       **{k2: c[k2] for k2 in ("suceso_max_db", "rango_lufs_ventana", "pios", "pios_0_7s",
                                               "pios_13_20s", "viento_sube_db", "suceso_final_db",
                                               "insectos_bulto_db", "insectos_tramas", "tonos_sostenidos_hz")
                          if k2 in c}, **m})
        for c in resto:
            nuevas_desc.append({k: v for k, v in c.items() if k != "y"} | {"motivo": "válida, sobrante"})
    informe["descartes"].extend(nuevas_desc)
    mj.write_text(json.dumps(informe, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for sid, cl in informe["clips"].items():
        L = [c["lufs_i"] for c in cl]
        print(sid, len(cl), "LUFS", min(L), max(L), "dif", round(max(L) - min(L), 2))
        for c in cl:
            print("  ", c["archivo"], c["de"], c["lufs_i"], c["pico_dbfs"], c["dur_s"], c.get("costura_ogg"),
                  {k: c.get(k) for k in ("suceso_max_db", "rango_lufs_ventana", "pios_0_7s", "pios_13_20s",
                                         "viento_sube_db", "insectos_bulto_db", "insectos_tramas",
                                         "tonos_sostenidos_hz")})
    print("descartes nuevos:", json.dumps([(d["toma"], d["motivo"]) for d in nuevas_desc], ensure_ascii=False,
                                          indent=0))


# ---------- prueba ----------
GANANCIA_PRUEBA_DB = 20.0   # toda la prueba sube 20 dB por igual (deshace el 0,10 de la noche) para oírla a volumen normal


def prueba(entrega):
    e = Path(entrega)
    c = lambda s, k=1: leer(e / f"{SALIDA[s]}_{k}.ogg")  # noqa: E731
    dia_s = np.tile(c("dia_sagunto"), 2)[:20 * SR]
    dia_n = np.tile(c("dia_nules"), 2)[:20 * SR]
    for z in (dia_s, dia_n):   # 0,5 s de fundido en los cambios de escena de la prueba
        k = SR // 2
        z[:k] *= np.linspace(0, 1, k)
        z[-k:] *= np.linspace(1, 0, k)
    at = c("atardecer")
    noche = np.tile(leer(NOCHE), 2)[:13 * SR] * NOCHE_VOL      # la noche como suena en la zona (cámara cerca)
    F = 3 * SR                                                 # fundido de 3 s, potencia constante
    t = np.linspace(0, 1, F, endpoint=False)
    tramo = np.zeros(len(at) + len(noche) - F, np.float32)
    tramo[:len(at)] += at
    tramo[len(at) - F:len(at)] *= np.cos(t * np.pi / 2)
    noche[:F] *= np.sin(t * np.pi / 2)
    tramo[len(at) - F:] += noche
    tramo[-SR:] *= np.linspace(1, 0, SR)
    total = np.concatenate([dia_s, dia_n, tramo]).astype(np.float32) * 10 ** (GANANCIA_PRUEBA_DB / 20)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-c:a", "libmp3lame", "-b:a", "160k", str(e / "prueba.mp3")], input=total.tobytes(), check=True)
    g = GANANCIA_PRUEBA_DB
    print("prueba:", round(len(total) / SR, 2), "s; Sagunto", round(lufs(dia_s)[0] + 0, 1), "Nules",
          round(lufs(dia_n)[0], 1), "atardecer", round(lufs(at)[0], 1), "noche ×0,10", round(lufs(noche[F:])[0], 1),
          f"(en el juego; en el MP3 todo +{g:.0f} dB)")


# ---------- página de escucha ----------
FICHAS = [
    ("dia_sagunto", "Sagunto de día", "Pueblo con estación junto a la huerta, mañana de noviembre. Bucle de 20 s."),
    ("dia_nules", "Nules de día", "Naranjal con viento en las hojas, acequia muy baja y la vía lejos. Bucle de 20 s."),
    ("atardecer", "Atardecer", "20 s sin bucle: los pájaros se callan, el viento sube y acaba en la noche."),
]


def escucha(entrega):
    e = Path(entrega)
    m = json.loads((e / "medidas.json").read_text(encoding="utf-8"))
    b64 = lambda p: base64.b64encode(Path(p).read_bytes()).decode()  # noqa: E731
    ref = m["referencia"]
    secciones = []
    for sid, titulo, nota in FICHAS:
        cl = m["clips"].get(sid, [])
        if not cl:
            continue
        items = []
        for c in cl:
            items.append(f"""
        <li class="var">
          <div class="var-head"><span class="n">{html.escape(c['archivo'].rsplit('_', 1)[1][:-4])}</span><code>{html.escape(c['archivo'])}</code></div>
          <audio controls preload="none" src="data:audio/ogg;base64,{b64(e / c['archivo'])}"></audio>
          <p class="med">{num(c['lufs_i'])} LUFS · pico {num(c['pico_dbfs'])} dBFS · {num(c['dur_s'], 2)} s</p>
        </li>""")
        secciones.append(f"""
    <section class="snd" aria-labelledby="t-{sid}">
      <div class="snd-head"><h2 id="t-{sid}">{html.escape(titulo)}</h2><code>{SALIDA[sid]}_1..{len(cl)}</code></div>
      <p class="nota">{html.escape(nota)}</p>
      <ol class="vars">{''.join(items)}
      </ol>
    </section>""")
    pagina = f"""<title>Ambiente de día</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Página de escucha: la prueba arriba y, debajo, las 5 variantes de cada sonido para elegir */
:root {{
  --bg: #f1efe8; --panel: #faf9f5; --fg: #23211b; --muted: #645f52; --line: #d6d1c3; --accent: #8a5a1c;
  --f-disp: "Barlow Condensed", "Arial Narrow", sans-serif;
  --f-body: "Source Sans 3", "Segoe UI", sans-serif;
  --f-mono: "JetBrains Mono", Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #17150f; --panel: #201d16; --fg: #e8e3d6; --muted: #a39b88; --line: #3a352a; --accent: #e0a858; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #17150f; --panel: #201d16; --fg: #e8e3d6; --muted: #a39b88; --line: #3a352a; --accent: #e0a858; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--f-body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 32px 48px }}
.wrap {{ max-width: 960px; margin: 0 auto; display: grid; gap: 28px }}
.eyebrow {{ font: 600 13px/1 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--accent) }}
h1 {{ font: 700 clamp(34px, 6vw, 52px)/1 var(--f-disp); margin: 8px 0 10px; text-wrap: balance; letter-spacing: .01em }}
h2 {{ font: 700 26px/1.1 var(--f-disp); margin: 0 }}
p {{ margin: 0; max-width: 65ch }}
.lead {{ color: var(--muted) }}
.prueba {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 20px; display: grid; gap: 12px }}
.prueba ol {{ margin: 0; padding-left: 20px; color: var(--muted) }}
audio {{ width: 100%; }}
.snd {{ border-top: 3px solid var(--accent); padding-top: 14px; display: grid; gap: 10px }}
.snd-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap }}
code {{ font: 12px var(--f-mono); color: var(--muted); overflow-wrap: anywhere }}
.nota {{ color: var(--muted); font-size: 15px }}
ol.vars {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px }}
.var {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; display: grid; gap: 8px; min-width: 0 }}
.var-head {{ display: flex; gap: 10px; align-items: baseline; min-width: 0 }}
.n {{ font: 700 22px/1 var(--f-disp); color: var(--accent) }}
.med {{ font: 13px var(--f-mono); color: var(--muted); font-variant-numeric: tabular-nums }}
.pie {{ color: var(--muted); font-size: 14px }}
</style>
<div class="wrap">
  <header>
    <div class="eyebrow">D-N157 · Sagunto · Nules · atardecer</div>
    <h1>Ambiente de día</h1>
    <p class="lead">Noviembre en la huerta: viento suave, pocos pájaros y la vía a lo lejos, sin insectos, música ni voces. Debajo de la prueba están las variantes de cada sonido: {len(m['clips'].get('dia_sagunto', []))} de Sagunto, {len(m['clips'].get('dia_nules', []))} de Nules y {len(m['clips'].get('atardecer', []))} del atardecer. Las fijas que ya están en el juego son Sagunto 1, Nules 2 y atardecer 1. Todo es mono, 44,1 kHz y OGG, con el nivel horneado.</p>
  </header>
  <section class="prueba" aria-labelledby="t-prueba">
    <h2 id="t-prueba">Prueba de conjunto</h2>
    <audio controls preload="none" src="data:audio/mpeg;base64,{b64(e / 'prueba.mp3')}"></audio>
    <ol>
      <li>0–20 s: Sagunto de día (variante 1).</li>
      <li>20–40 s: Nules de día (variante 1).</li>
      <li>40–60 s: el atardecer (variante 1), que en los últimos 3 s se funde con el ambiente de noche actual; luego 10 s de noche.</li>
    </ol>
    <p class="nota">En el juego, la noche suena a {num(ref['noche_efectivo'])} LUFS, el día a {num(ref['dia_lufs'])} y el atardecer a {num(ref['atardecer_lufs'])}. Es muy bajo a propósito, así que en esta prueba todo está subido 20 dB por igual: las diferencias entre ellos son las del juego. Las variantes de abajo están al nivel real, así que sube el volumen para oírlas.</p>
  </section>
  {''.join(secciones)}
  <p class="pie">Nuria (Sonido)</p>
</div>
"""
    (e / "escucha.html").write_text(pagina, encoding="utf-8")
    print("escucha.html", round((e / "escucha.html").stat().st_size / 1e6, 2), "MB")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "creditos":
        creditos()
    elif cmd == "generar":
        generar(sys.argv[2], sys.argv[3:])
    elif cmd == "extra":
        extra(*sys.argv[2:6])
    elif cmd == "calibrar":
        calibrar()
    elif cmd == "post":
        post(sys.argv[2], sys.argv[3])
        prueba(sys.argv[3])
    elif cmd == "completar":
        completar(sys.argv[2], sys.argv[3])
    elif cmd == "escucha":
        escucha(sys.argv[2])
    else:
        sys.exit(__doc__)
