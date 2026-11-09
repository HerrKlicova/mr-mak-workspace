"""Página de escucha de obra y pitido (Nuria): prueba_obra_pitido.mp3 y la variante 1 de cada sonido, incrustados en base64.

Uso: python escucha_obra_pitido.py <entrega>
"""
import base64
import html
import json
import sys
from pathlib import Path

NOMBRES = {
    "obra_pala": ("Palada", "Una palada en tierra o arena. Palas cada 1,0–1,6 s por zapador, como mucho 3 a la vez."),
    "obra_saco": ("Saco terrero", "Un saco que cae sobre la pila y se asienta. Uno por saco colocado."),
    "obra_malla": ("Malla del HESCO", "La malla se despliega y traquetea. Uno por HESCO."),
    "tren_pitido_electrico": ("Pitido eléctrico", "Toque corto de dos tonos al salir, oído desde el andén. Tras el cierre de puertas, 0,5–1 s antes del arranque."),
    "tren_pitido_diesel": ("Pitido diésel", "Un toque corto de bocina de aire de la 333. Mismo momento que el eléctrico."),
}


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def num(v, d=1):
    return f"{v:.{d}f}".replace(".", ",").replace("-", "−")


def main(entrega):
    e = Path(entrega)
    m = json.loads((e / "medidas.json").read_text(encoding="utf-8"))
    filas = []
    for sid, (titulo, nota) in NOMBRES.items():
        clips = m["clips"].get(sid, [])
        if not clips:
            continue
        c1 = clips[0]
        durs = [c["dur_s"] for c in clips]
        lufs = [c["lufs_i"] for c in clips]
        picos = [c["pico_dbfs"] for c in clips]
        filas.append(f"""
    <li class="snd">
      <div class="snd-head">
        <h3>{html.escape(titulo)}</h3>
        <code>sfx_{sid}_1..{len(clips)}</code>
      </div>
      <p class="nota">{html.escape(nota)}</p>
      <audio controls preload="none" src="data:audio/ogg;base64,{b64(e / c1['archivo'])}"></audio>
      <dl class="med">
        <div><dt>Duración</dt><dd>{num(min(durs))}–{num(max(durs))} s</dd></div>
        <div><dt>Pico</dt><dd>{num(max(picos))} dBFS</dd></div>
        <div><dt>LUFS</dt><dd>{num(min(lufs))} a {num(max(lufs))}</dd></div>
      </dl>
    </li>""")
    mp3 = b64(e / "prueba_obra_pitido.mp3")
    pagina = f"""<title>Sonido de obra y pitido del tren</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Una columna de escucha: la prueba arriba y una ficha por sonido, en rejilla que se apila en el móvil */
:root {{
  --bg: #eef0ea; --panel: #f8f9f5; --fg: #1d221c; --muted: #5b6458; --line: #cfd4c8; --accent: #4f6b2c;
  --f-disp: "Barlow Condensed", "Arial Narrow", sans-serif;
  --f-body: "Source Sans 3", "Segoe UI", sans-serif;
  --f-mono: "JetBrains Mono", Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #151913; --panel: #1d221b; --fg: #e3e7dc; --muted: #9aa392; --line: #333b30; --accent: #a9c774; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #151913; --panel: #1d221b; --fg: #e3e7dc; --muted: #9aa392; --line: #333b30; --accent: #a9c774; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--f-body);
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
audio {{ width: 100%; }}
ul.lista {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px }}
.snd {{ border-top: 3px solid var(--accent); background: var(--panel); padding: 14px 16px 16px; display: grid; gap: 8px; min-width: 0 }}
.snd-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap }}
code {{ font: 12px var(--f-mono); color: var(--muted); overflow-wrap: anywhere }}
.nota {{ color: var(--muted); font-size: 14px }}
.v1 {{ border-top: 1px dashed var(--line); padding-top: 8px }}
.med {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 0; font-variant-numeric: tabular-nums }}
.med dt {{ font: 11px var(--f-mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
.med dd {{ margin: 0; font-size: 14px }}
.pie {{ color: var(--muted); font-size: 14px }}
</style>
<div class="wrap">
  <header>
    <div class="eyebrow">Reparar el muro · D-N170 · 3D mono</div>
    <h1>Sonido de obra y pitido del tren</h1>
    <p class="lead">Cinco sonidos con cinco variantes cada uno. Aquí suena la variante 1 de cada uno. Escúchalo con auriculares a volumen normal: los niveles están horneados. La obra queda por debajo del combate (−28 y −30 LUFS frente a los −18 del fusil de cerca). <strong>Pitidos v2 (9-nov, mezcla de Lucía):</strong> subidos a −22,5 LUFS con ganancia fija, sin limitador; en la zona quedan 6 dB por debajo de la alarma de ataque.</p>
  </header>
  <section class="prueba" aria-labelledby="t-prueba">
    <h2 id="t-prueba">Prueba de conjunto</h2>
    <audio controls preload="none" src="data:audio/mpeg;base64,{mp3}"></audio>
    <ol>
      <li>10 s de reparación: una palada cada 1,2 s, un saco cada 3 s y una malla.</li>
      <li>Salida eléctrica: aviso de puertas, cierre, pitido y, 0,7 s después, el arranque.</li>
      <li>Aparte, salida diésel: pitido y arranque de la 333.</li>
    </ol>
  </section>
  <section aria-labelledby="t-sonidos">
    <h2 id="t-sonidos">Cada sonido, variante 1</h2>
    <ul class="lista">{''.join(filas)}
    </ul>
  </section>
  <p class="pie">Medidas sobre las 5 variantes de cada sonido. Los pitidos v1 (−27 a −29 LUFS) se guardan en v1_pitido. — Nuria (Sonido)</p>
</div>
"""
    (e / "escucha.html").write_text(pagina, encoding="utf-8")
    print("escucha.html", round((e / "escucha.html").stat().st_size / 1e6, 2), "MB")


if __name__ == "__main__":
    main(sys.argv[1])
