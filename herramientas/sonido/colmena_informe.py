"""Avisos de la Colmena (CO-1 a CO-4), aviso ámbar de la señal 6 y abrir el Informe de inteligencia (Nuria, 9-nov-2026).
Encargo de Lucía del 9-nov, 00:02. Textos de contexto en docs/informe-textos.md («Avisos de la Colmena»).

Mismo método que farp_nules_avisos.py: ElevenLabs eleven_text_to_sound_v3, clave SOLO de ELEVENLABS_API_KEY (nunca se
imprime ni se guarda). Si la API rechaza el modelo, se detiene y no cae a otro.
Todo es interfaz: 2D, mono, 44,1 kHz, OGG Vorbis, nivel horneado por sonoridad integrada (LUFS), sin normalizar en la
importación, variantes a ±0,5 dB entre sí y picos por debajo de −3 dBFS. Sistema militar, no terror: sin voces, sin
gritos ni rugidos y sin música (se descartan las tomas con melodía: más de 3 notas distintas).

Uso:
  python colmena_informe.py creditos
  python colmena_informe.py generar <brutos> [ids...]          (reanudable)
  python colmena_informe.py extra <brutos> <id> <sufijo> <n>   (n tomas más de un prompt)
  python colmena_informe.py post <brutos> <entrega>            (OGG + medidas.json + prueba.mp3)
  python colmena_informe.py escucha <entrega>
"""
import base64
import html
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import farp_nules_avisos as fna  # noqa: E402
from farp_nules_avisos import a_lufs, medir_ogg, notas, num, subidas  # noqa: E402
from maquina_escribir import SR, a_ogg, creditos, db, leer, lufs  # noqa: E402
from obra_pitido import env_db, recortar, sucesos  # noqa: E402
from salida_tren import tono_fijo  # noqa: E402

UI = ", isolated interface sound, no background, no music, no melody, no voices, no speech, no screams"
# id -> dict(tipo, lufs, dmin, dmax, hueco, prompts [(suf, texto, dur pedida, influencia, n)])
SONIDOS = {
    "acecho": dict(tipo="acecho", lufs=-26, dmin=1.0, dmax=2.0, hueco=0.15, prompts=[
        ("a", "military command console alert tone, electronic, low, muffled, a single dull deep tone that holds "
              "briefly and fades" + UI, 1.8, 0.75, 3),
        ("b", "low radar warning tone on a military control panel, one muffled electronic hum note, calm and "
              "serious" + UI, 1.8, 0.75, 2),
        ("c", "deep muted electronic status tone from a military operations computer, single low soft beep with a "
              "short decay" + UI, 1.6, 0.75, 2),
        # reposición: la a y la c salen de 0,4 a 0,9 s (más cortas que el mínimo de 1 s)
        ("d", "military command console alert tone, one low muffled electronic tone that sustains for a full second "
              "and then slowly decays, deep and dull, about two seconds long" + UI, 2.0, 0.75, 0),
    ]),
    "enjambre": dict(tipo="enjambre", lufs=-22.5, dmin=1.4,  # 1,5 pedido; 1,4 por el tope de créditos (ver LEEME)
                    dmax=2.0, hueco=0.04, prompts=[
        ("a", "military command console alert, three firm low electronic pulses, beep beep beep, deep and urgent "
              "but restrained" + UI, 2.0, 0.75, 3),
        ("b", "radar warning tone, two or three strong deep electronic pulses in a row, military control room "
              "alert" + UI, 2.0, 0.75, 2),
        ("c", "three short low buzzing warning pulses from a military computer terminal, evenly spaced, firm"
              + UI, 1.8, 0.75, 2),
        # reposición: tres pulsos repartidos en casi 2 s (la b sale de 0,6 a 1,2 s)
        ("d", "military radar warning alert, exactly three deep firm electronic pulses, one every half second, the "
              "last one ringing out briefly" + UI, 2.0, 0.75, 0),
    ]),
    "vuelta_acecho": dict(tipo="vuelta", lufs=-28, dmin=1.0, dmax=2.0, hueco=0.15, prompts=[
        ("a", "military command console tone, electronic, low, muffled, a single tone gliding downward in pitch and "
              "fading out" + UI, 1.8, 0.75, 3),
        ("b", "descending electronic power-down tone on a military radar console, low pitch sliding down and dying "
              "away" + UI, 1.8, 0.75, 2),
        ("c", "soft low electronic alert stand-down tone, pitch falling, quietly fading away, military control "
              "panel" + UI, 1.6, 0.75, 2),
    ]),
    "dispersa": dict(tipo="dispersa", lufs=-30, dmin=1.0, dmax=2.0, hueco=0.15, prompts=[
        ("a", "soft gentle electronic tone from a military console, warm and quiet, slowly fading away to silence"
              + UI, 1.8, 0.75, 3),
        ("b", "calm all-clear tone on a military radar screen, soft muted electronic note that gently fades out"
              + UI, 1.8, 0.75, 2),
        ("c", "quiet soft electronic chime from a military computer, smooth, mellow, dissolving and fading"
              + UI, 1.6, 0.75, 2),
        # reposición: la a sale muda o sin caída y la c es un siseo agudo
        ("d", "one soft mellow low electronic tone from a military console, gentle, fading out slowly over two "
              "seconds" + UI, 2.0, 0.75, 0),
    ]),
    "senal6": dict(tipo="toque", lufs=-32, dmin=0.4, dmax=0.8, hueco=0.06, prompts=[
        ("a", "single short soft electronic blip, subtle military console notification, one quiet tick tone"
              + UI, 0.6, 0.75, 3),
        ("b", "one brief muted electronic beep from a military control panel, discreet and soft" + UI, 0.6, 0.75, 2),
        ("c", "tiny soft click tone, single short interface notification, military terminal, quiet" + UI,
         0.6, 0.75, 2),
        # reposición: la a, la b y la c salen de 0,1 a 0,3 s (más cortas que el mínimo de 0,4 s)
        ("d", "one soft muted electronic ping from a military console with a gentle ringing decay of half a second, "
              "discreet notification" + UI, 0.8, 0.75, 0),
    ]),
    "informe": dict(tipo="papel", lufs=-30, dmin=0.6, dmax=1.2, hueco=0.08, prompts=[
        ("a", "a sheet of paper report quickly pulled out and unfolded, short dry paper rustle, close up"
              + UI, 1.0, 0.75, 3),
        ("b", "short burst of an old teletype printer, quick dry mechanical clatter, a few characters printed, "
              "then stops" + UI, 1.0, 0.75, 2),
        ("c", "military intelligence dossier opened on a desk, one quick dry paper page flip" + UI, 1.0, 0.75, 2),
    ]),
}
SALIDA = {"acecho": "sfx_colmena_acecho", "enjambre": "sfx_colmena_enjambre",
          "vuelta_acecho": "sfx_colmena_vuelta_acecho", "dispersa": "sfx_colmena_dispersa",
          "senal6": "sfx_ui_aviso_senal6", "informe": "sfx_ui_informe_abrir"}
N_FINAL = 5
TECHO = -3.0     # pico máximo (dBFS)
ALARMA = Path(r"C:\Dev\TBD\Assets\TBD\Resources\Audio\sfx_alarma_ataque_1.mp3")   # solo lectura
ALARMA_VOL = 0.6

fna.SONIDOS = SONIDOS   # los ayudantes de generación de farp_nules_avisos leen este diccionario


# ---------- análisis ----------
def centroide(x):
    sp = np.abs(np.fft.rfft(x)) ** 2
    f = np.fft.rfftfreq(len(x), 1 / SR)
    return float((sp * f).sum() / (sp.sum() + 1e-12))


def tono_dominante(x, fmin=50, fmax=4000, tr=0.04):
    """Frecuencia del pico espectral por tramas de 40 ms (solo las tramas a menos de 20 dB del máximo)."""
    n = int(SR * tr)
    f = np.fft.rfftfreq(n, 1 / SR)
    m = (f >= fmin) & (f <= fmax)
    e = np.array([np.sqrt(np.mean(x[i:i + n] ** 2) + 1e-12) for i in range(0, len(x) - n, n)])
    if not len(e):
        return []
    edb = 20 * np.log10(e)
    out = []
    for k, i in enumerate(range(0, len(x) - n, n)):
        if edb[k] > edb.max() - 20:
            sp = np.abs(np.fft.rfft(x[i:i + n] * np.hanning(n)))
            out.append((k * tr, float(f[m][np.argmax(sp[m])])))
    return out


def caida_db(x):
    """Diferencia de nivel entre el primer y el último cuarto del tramo vivo (positivo = se apaga)."""
    edb, n = env_db(x)
    vivo = np.where(edb > edb.max() - 40)[0]
    if len(vivo) < 8:
        return 0.0
    v = edb[vivo[0]:vivo[-1] + 1]
    q = max(1, len(v) // 4)
    return round(float(np.mean(v[:q]) - np.mean(v[-q:])), 1)


def pulsos(x, umbral=12, hueco=0.04):
    """Pulsos fuertes: tramos de la envolvente a menos de `umbral` dB del máximo, separados por más de `hueco`."""
    return [s for s in sucesos(x, hueco, umbral) if s[1] - s[0] >= 0.03]


def candidata(sid, s, f):
    x = leer(f)
    pk = db(np.abs(x).max())
    edb, _ = env_db(x)
    activa = float(np.mean(edb > edb.max() - 30))
    info = {"toma": f.name, "pico_bruto": round(pk, 1), "fraccion_activa": round(activa, 2),
            "dur_bruta": round(len(x) / SR, 2)}
    if pk < -45 or activa < 0.05:
        return None, {**info, "motivo": "muda o casi muda (envolvente)"}
    li = lufs(x)[0]
    info["lufs_bruto"] = round(li, 1)
    if li < -50:
        return None, {**info, "motivo": f"casi muda ({li:.1f} LUFS en bruto)"}
    y, fade = recortar(x, s["dmax"])
    dur = len(y) / SR
    info.update(dur_recortada=round(dur, 2), fade_ms=round(fade * 1000))
    if dur < s["dmin"]:
        return None, {**info, "motivo": f"demasiado corta tras recortar ({dur:.2f} s < {s['dmin']} s)"}
    ns = notas(y, fmin=80, fmax=4000)
    info.update(notas=ns, centroide_hz=round(centroide(y)), caida_db=caida_db(y), ataques_s=subidas(y)[:8])
    distintas = []
    for _, hz, _ in ns:
        if not any(abs(hz / d - 1) < 0.06 for d in distintas):
            distintas.append(hz)
    tipo = s["tipo"]
    # un glissando que baja da muchas «notas» seguidas, pero no es una melodía: ≥ 75 % de los pasos descienden
    pasos = [ns[k + 1][1] < ns[k][1] for k in range(len(ns) - 1)]
    info["glisando_baja"] = bool(pasos) and sum(pasos) / len(pasos) >= 0.75
    if len(distintas) > 3 and not info["glisando_baja"]:
        return None, {**info, "motivo": f"{len(distintas)} notas distintas (suena a melodía)"}
    if tipo == "enjambre":   # el v3 da a menudo 4 pulsos cada 0,5 s: se corta justo antes del 4.º con 40 ms de fundido
        p = pulsos(y)
        if len(p) > 3:
            fin = int(p[3][0] * SR)
            k = int(0.04 * SR)
            y = y[:fin].copy()
            y[-k:] *= np.cos(np.linspace(0, np.pi / 2, k)) ** 2
            info["cortada_al_3er_pulso_s"] = round(fin / SR, 2)
            if len(y) / SR < s["dmin"] - 0.05:
                return None, {**info, "motivo": f"tras dejar 3 pulsos dura {len(y) / SR:.2f} s"}
    if tipo in ("acecho", "vuelta", "dispersa", "enjambre") and info["centroide_hz"] > 2500:
        return None, {**info, "motivo": f"poco grave (centroide {info['centroide_hz']} Hz)"}
    if tipo == "acecho":
        if len(pulsos(y)) > 2:
            return None, {**info, "motivo": f"{len(pulsos(y))} golpes fuertes (se pide un tono)"}
    elif tipo == "enjambre":
        p = pulsos(y)
        info["pulsos"] = [(round(a, 2), round(b, 2)) for a, b, _ in p]
        if not 2 <= len(p) <= 3:
            return None, {**info, "motivo": f"{len(p)} pulsos fuertes (se piden 2 o 3)"}
    elif tipo == "vuelta":
        tt = tono_dominante(y)
        if len(tt) >= 6:
            q = max(2, len(tt) // 3)
            ini, fin = np.median([h for _, h in tt[:q]]), np.median([h for _, h in tt[-q:]])
            info["tono_ini_fin_hz"] = (round(ini), round(fin))
        else:
            ini = fin = 0
        if not (fin < ini * 0.94 or info["caida_db"] >= 10):
            return None, {**info, "motivo": "no desciende ni se apaga"}
        if info["caida_db"] < 4:
            return None, {**info, "motivo": f"no se apaga ({info['caida_db']} dB de caída)"}
    elif tipo == "dispersa":
        if info["caida_db"] < 6:
            return None, {**info, "motivo": f"no se desvanece ({info['caida_db']} dB de caída)"}
        if len(pulsos(y)) > 2:
            return None, {**info, "motivo": f"{len(pulsos(y))} golpes fuertes (se pide un tono suave)"}
    elif tipo == "toque":
        p = pulsos(y, 15, 0.06)
        info["pulsos"] = len(p)
        if len(p) > 2:
            return None, {**info, "motivo": f"{len(p)} toques (se pide uno)"}
    elif tipo == "papel":
        t, hz = tono_fijo(y, seg=0.4)
        info.update(tono_fijo_s=t, tono_fijo_hz=hz)
        if t >= 0.4:
            return None, {**info, "motivo": f"tono fijo {t} s a {hz} Hz (pitido o música, no papel)"}
    return y, info


def post(brutos, entrega):
    brutos, entrega = Path(brutos), Path(entrega)
    entrega.mkdir(parents=True, exist_ok=True)
    informe = {"clips": {}, "descartes": [], "candidatas": {}}
    for sid, s in SONIDOS.items():
        cand = []
        for f in sorted(brutos.glob(f"{sid}_*.mp3")):
            y, info = candidata(sid, s, f)
            if y is None:
                informe["descartes"].append(info)
            else:
                cand.append({**info, "y": y})
        for c in cand:
            c["pico_a_lufs"] = round(db(np.abs(a_lufs(c["y"], s["lufs"], False)).max()), 1)
        ok = [c for c in cand if c["pico_a_lufs"] <= TECHO]
        for c in [c for c in cand if c not in ok]:
            informe["descartes"].append({k: v for k, v in c.items() if k != "y"} |
                                        {"motivo": f"a {s['lufs']} LUFS el pico pasa de {TECHO} dBFS ({c['pico_a_lufs']})"})
        informe["candidatas"][sid] = [{k: v for k, v in c.items() if k != "y"} for c in ok]
        # las 5 con el pico más parejo a LUFS fijo
        cand = sorted(ok, key=lambda c: c["pico_a_lufs"])
        if len(cand) > N_FINAL:
            k0 = min(range(len(cand) - N_FINAL + 1),
                     key=lambda k: cand[k + N_FINAL - 1]["pico_a_lufs"] - cand[k]["pico_a_lufs"])
            elegidas, resto = cand[k0:k0 + N_FINAL], cand[:k0] + cand[k0 + N_FINAL:]
        else:
            elegidas, resto = cand, []
        if len(elegidas) < N_FINAL:
            print(f"AVISO: {sid}: solo {len(elegidas)} válidas", flush=True)
        informe["clips"][sid] = []
        for k, c in enumerate(elegidas, 1):
            dest = entrega / f"{SALIDA[sid]}_{k}.ogg"
            y = a_lufs(c["y"], s["lufs"], False)
            a_ogg(y, dest)
            for _ in range(2):   # el Vorbis mueve la sonoridad unas décimas: se corrige midiendo el OGG
                m = medir_ogg(dest)["lufs_i"]
                if abs(m - s["lufs"]) <= 0.1:
                    break
                y = y * 10 ** ((s["lufs"] - m) / 20)
                a_ogg(y, dest)
            m = medir_ogg(dest)
            informe["clips"][sid].append({"archivo": dest.name, "de": c["toma"],
                                          **{k2: c[k2] for k2 in ("notas", "centroide_hz", "caida_db", "pulsos",
                                                                  "tono_ini_fin_hz", "ataques_s") if k2 in c}, **m})
        for c in resto:
            informe["descartes"].append({k: v for k, v in c.items() if k != "y"} |
                                        {"motivo": "válida, sobrante (fuera de las 5 elegidas)"})
    (entrega / "medidas.json").write_text(json.dumps(informe, ensure_ascii=False, indent=1, default=float),
                                          encoding="utf-8")
    for sid, cl in informe["clips"].items():
        L = [c["lufs_i"] for c in cl]
        print(sid, len(cl), "LUFS", min(L, default=0), max(L, default=0), "pico máx",
              max([c["pico_dbfs"] for c in cl], default=0), "dur", [c["dur_s"] for c in cl])
    print("descartes:", json.dumps([(d["toma"], d["motivo"]) for d in informe["descartes"]], ensure_ascii=False,
                                   indent=0))


# ---------- prueba ----------
def prueba(entrega):
    e = Path(entrega)
    c = lambda s, k=1: leer(e / f"{SALIDA[s]}_{k}.ogg")  # noqa: E731
    hueco = lambda s: np.zeros(int(SR * s), np.float32)  # noqa: E731
    alarma = leer(ALARMA) * ALARMA_VOL
    partes = []
    for sid in ("acecho", "enjambre", "vuelta_acecho", "dispersa", "senal6", "informe"):
        partes += [c(sid), hueco(2.0)]
    partes += [alarma, hueco(0.5)]
    total = np.concatenate([hueco(0.3)] + [p.astype(np.float32) for p in partes])
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-c:a", "libmp3lame", "-b:a", "160k", str(e / "prueba.mp3")], input=total.tobytes(), check=True)
    i, _ = lufs(alarma)
    print("prueba:", round(len(total) / SR, 2), "s; alarma a 0,6:", round(i, 1), "LUFS, pico",
          round(db(np.abs(alarma).max()), 1), "dBFS")
    return round(i, 1)


# ---------- página de escucha ----------
FICHAS = [
    ("acecho", "CO-1 · Al acecho", "La Colmena deja de vagar. Tono sordo y grave. −26 LUFS."),
    ("enjambre", "CO-2 · Enjambre", "El más marcado: dos o tres pulsos graves. −22,5 LUFS, 3 dB por debajo de la alarma."),
    ("vuelta_acecho", "CO-3 · De Enjambre a Al acecho", "Tono que baja y se apaga. −28 LUFS."),
    ("dispersa", "CO-4 · Dispersa", "Tono suave que se desvanece. −30 LUFS."),
    ("senal6", "Señal 6 · aviso ámbar", "Toque breve y discreto, menos que los CO. −32 LUFS."),
    ("informe", "Abrir el Informe de inteligencia", "Papel o teletipo, breve y seco. −30 LUFS."),
]


def escucha(entrega):
    e = Path(entrega)
    m = json.loads((e / "medidas.json").read_text(encoding="utf-8"))
    b64 = lambda p: base64.b64encode(Path(p).read_bytes()).decode()  # noqa: E731
    filas = []
    for sid, titulo, nota in FICHAS:
        cl = m["clips"].get(sid, [])
        if not cl:
            continue
        durs, L, pk = [c["dur_s"] for c in cl], [c["lufs_i"] for c in cl], [c["pico_dbfs"] for c in cl]
        vars_ = "".join(f"""
        <li><span class="vn">{k}</span><audio controls preload="none" src="data:audio/ogg;base64,{b64(e / c['archivo'])}"></audio>
          <span class="vm">{num(c['dur_s'], 2)} s · {num(c['lufs_i'])} LUFS · {num(c['pico_dbfs'])} dBFS</span></li>"""
                        for k, c in enumerate(cl, 1))
        filas.append(f"""
    <li class="snd">
      <div class="snd-head"><h3>{html.escape(titulo)}</h3><code>{SALIDA[sid]}_1..{len(cl)}</code></div>
      <p class="nota">{html.escape(nota)}</p>
      <dl class="med">
        <div><dt>Duración</dt><dd>{num(min(durs), 2)}–{num(max(durs), 2)} s</dd></div>
        <div><dt>Pico máx.</dt><dd>{num(max(pk))} dBFS</dd></div>
        <div><dt>LUFS</dt><dd>{num(min(L))} a {num(max(L))}</dd></div>
      </dl>
      <ol class="vars">{vars_}
      </ol>
    </li>""")
    pagina = f"""<title>Sonido de la Colmena e informe</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Una columna: la prueba arriba y una ficha por sonido con sus 5 variantes para elegir */
:root {{
  --bg: #eceee9; --panel: #f7f8f4; --fg: #1c201c; --muted: #5a6259; --line: #cdd2c9; --accent: #8a5a12;
  --f-disp: "Barlow Condensed", "Arial Narrow", sans-serif;
  --f-body: "Source Sans 3", "Segoe UI", sans-serif;
  --f-mono: "JetBrains Mono", Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #141713; --panel: #1c201b; --fg: #e2e6dc; --muted: #9aa292; --line: #323a30; --accent: #e0a64a; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #141713; --panel: #1c201b; --fg: #e2e6dc; --muted: #9aa292; --line: #323a30; --accent: #e0a64a; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--f-body); margin: 0;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 32px 48px }}
.wrap {{ max-width: 960px; margin: 0 auto; display: grid; gap: 28px }}
.eyebrow {{ font: 600 13px/1 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--accent) }}
h1 {{ font: 700 clamp(34px, 6vw, 52px)/1 var(--f-disp); margin: 8px 0 10px; text-wrap: balance; letter-spacing: .01em }}
h2 {{ font: 700 26px/1.1 var(--f-disp); margin: 0 0 6px }}
h3 {{ font: 600 22px/1.1 var(--f-disp); margin: 0 }}
p {{ margin: 0; max-width: 65ch }}
.lead {{ color: var(--muted) }}
.prueba {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 20px; display: grid; gap: 12px }}
.prueba ol {{ margin: 0; padding-left: 20px; color: var(--muted) }}
audio {{ width: 100%; min-width: 0 }}
ul.lista {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px }}
.snd {{ border-top: 3px solid var(--accent); background: var(--panel); padding: 14px 16px 16px; display: grid; gap: 8px; min-width: 0 }}
.snd-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap }}
code {{ font: 12px var(--f-mono); color: var(--muted); overflow-wrap: anywhere }}
.nota {{ color: var(--muted); font-size: 14px }}
.med {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 0; font-variant-numeric: tabular-nums }}
.med dt {{ font: 11px var(--f-mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
.med dd {{ margin: 0; font-size: 14px }}
ol.vars {{ list-style: none; margin: 4px 0 0; padding: 0; display: grid; gap: 10px }}
ol.vars li {{ display: grid; grid-template-columns: 22px 1fr; column-gap: 8px; align-items: center }}
.vn {{ font: 600 14px var(--f-mono); color: var(--accent) }}
.vm {{ grid-column: 2; font: 12px var(--f-mono); color: var(--muted); font-variant-numeric: tabular-nums }}
.pie {{ color: var(--muted); font-size: 14px }}
</style>
<div class="wrap">
  <header>
    <div class="eyebrow">Interfaz · 2D · sistema militar</div>
    <h1>Sonido de la Colmena e informe</h1>
    <p class="lead">Seis sonidos con cinco variantes cada uno, para elegir. Escúchalo con auriculares a volumen normal: los niveles están horneados y todos suenan con Sfx.Play a 1,0. Mono, 44,1 kHz, OGG.</p>
  </header>
  <section class="prueba" aria-labelledby="t-prueba">
    <h2 id="t-prueba">Prueba de conjunto</h2>
    <audio controls preload="none" src="data:audio/mpeg;base64,{b64(e / 'prueba.mp3')}"></audio>
    <ol>
      <li>La secuencia de la Colmena: Al acecho → Enjambre → vuelta a Al acecho → Dispersa, con 2 s entre cada uno.</li>
      <li>El aviso de la señal 6 y abrir el Informe.</li>
      <li>Al final, de referencia, la alarma de ataque del juego a 0,6.</li>
    </ol>
  </section>
  <section aria-labelledby="t-sonidos">
    <h2 id="t-sonidos">Las cinco variantes de cada sonido</h2>
    <ul class="lista">{''.join(filas)}
    </ul>
  </section>
  <p class="pie">Medidas sobre los OGG finales. — Nuria (Sonido)</p>
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
        fna.generar(sys.argv[2], sys.argv[3:])
    elif cmd == "extra":
        fna.extra(*sys.argv[2:6])
    elif cmd == "post":
        post(sys.argv[2], sys.argv[3])
        prueba(sys.argv[3])
    elif cmd == "escucha":
        escucha(sys.argv[2])
    else:
        sys.exit(__doc__)
