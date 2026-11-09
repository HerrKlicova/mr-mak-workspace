# Sonido de obra y pitido del tren (Nuria, 8-nov-2026)

Encargo de Lucía (8-nov, tarde): obra de reparar el muro (`docs` construccion-reparar.md) y pitido de salida del tren (D-N170, sustituye la nota de «sin pitido»).

- Herramienta: `herramientas\sonido\obra_pitido.py` (`creditos` / `generar` / `post`). Tomas en bruto: `herramientas\sonido\brutos_obra_pitido\`. Medidas completas: `medidas.json`. Página: `herramientas\sonido\escucha_obra_pitido.py`.
- ElevenLabs `eleven_text_to_sound_v3`, clave solo de `ELEVENLABS_API_KEY`.
- Todo 3D: mono, 44,1 kHz, OGG Vorbis q6, nivel horneado, sin normalizar al importar.
- Escucha: https://claude.ai/artifact/2LWuKYuWWEbwvd56QfvtMo

## Medidas (5 variantes de cada sonido)

| Sonido | Duración | Pico | LUFS integrado | Objetivo |
|---|---|---|---|---|
| `sfx_obra_pala_1..5` | 1,13–1,20 s | −16,0 a −8,4 dBFS | −30,0 a −30,1 | −30 LUFS |
| `sfx_obra_saco_1..5` | 0,62–1,00 s | −9,2 a −6,6 dBFS | −28,0 a −28,1 | −28 LUFS |
| `sfx_obra_malla_1..5` | 1,78–2,18 s | −14,0 a −11,9 dBFS | −29,9 a −30,1 | −30 LUFS |
| `sfx_tren_pitido_electrico_1..5` | 1,76 s | −15,3 a −14,1 dBFS | −28,8 a −28,3 | pico −14, ~−24 LUFS |
| `sfx_tren_pitido_diesel_1..5` | 1,95–2,00 s | −14,3 a −14,1 dBFS | −27,8 a −27,3 | pico −14, ~−24 LUFS |

- Dispersión entre variantes: obra ≤ 0,2 dB; pitidos ≤ 0,5 dB. Ninguno pasa de −1 dBFS.
- La obra queda por debajo del combate: el fusil de cerca va a −18 LUFS (D-N134); la obra, a −28/−30.
- **Pitidos: no llegan a −24 LUFS.** Con el pico en −14 dBFS, una bocina tiene un factor de cresta de unos 13–14 dB y se queda en −27/−29 LUFS. He mantenido el pico como límite. Para llegar a −24 haría falta un limitador de 3–4 dB; no lo he aplicado sin que nadie lo escuche. Si Lucía lo quiere, es un cambio en el posproceso, sin generar de nuevo.
- Un solo suceso por clip en la obra (comprobado por la envolvente: un único tramo a menos de 12 dB del máximo). Los pitidos tienen un único toque largo y como mucho 3 notas.
- No puedo escuchar: todo está comprobado midiendo. Eugenio, escucha la prueba antes de darlo por bueno.

## Prueba (`prueba_obra_pitido.mp3`, 46 s)

10 s de reparación (palas cada 1,2 s en rueda de variantes, un saco cada 3 s y una malla a los 4 s) → 1 s → aviso de puertas y cierre de `entregas\sonido-salida-tren` → pitido eléctrico → 0,7 s → arranque eléctrico → 2 s → pitido diésel → 0,7 s → arranque diésel 333.

## Descartes (37 tomas en total)

- `tren_pitido_electrico_a_v02`: 4 notas distintas, posible melodía.
- `tren_pitido_electrico_a_v03` y `_c_v02`: poco tonales, no suenan a bocina.
- `tren_pitido_electrico_b_v02`: muy débil para su pico (−36 LUFS con pico −14).
- Válidas pero sobrantes (fuera de las 5 más parejas): `obra_pala_a_v02`, `obra_pala_b_v03`, `obra_saco_b_v01`, `obra_saco_b_v02`, `obra_malla_b_v01`, `obra_malla_b_v02`, `tren_pitido_diesel_a_v03`, `tren_pitido_diesel_b_v02`.
- Ninguna toma muda en esta tanda. El eléctrico se quedó con 4 válidas tras la primera tanda y pedí 2 tomas más con un tercer prompt.

## Créditos

Contador antes: 78.589; después: 79.333. **Gastados: 744** de un tope de 1.800. Son 61,2 s pedidos en 37 llamadas (~12 créditos por segundo).

## Para Iker y Marcos

- Los 25 OGG van a `Assets/TBD/Resources/Audio`. Importación sin Normalize (AudioImportRules.cs).
- Volumen 1. La variante, por semilla determinista (1..5).
- **Obra**: `PlayAt` sobre el tramo que se repara, distancia máxima 60 m.
  - Palas: una cada 1,0–1,6 s (aleatorio por semilla) por zapador; como mucho 3 palas sonando a la vez.
  - Saco: uno al colocar cada saco.
  - Malla: una al poner cada HESCO.
- **Pitido**: `PlayAt` en la cabeza del tren, justo antes de arrancar: después del cierre de puertas y 0,5–1 s antes del arranque. Distancia máxima 400 m. Eléctrico para las unidades eléctricas; diésel para la 333.

## Pitido v2 (mezcla de Lucía), 9-nov-2026

Los 10 pitidos se han subido con **ganancia fija, sin limitador**. Los v1 están guardados en `v1_pitido\` (con el `medidas.json`, la prueba y la página de antes). Herramienta: `herramientas\sonido\pitido_v2.py`; medidas: `medidas_pitido_v2.json`. Mono, 44,1 kHz, OGG Vorbis q6, mismo nombre.

| Sonido | Antes (LUFS) | Ganancia | Después (LUFS) | Pico | True peak |
|---|---|---|---|---|---|
| `sfx_tren_pitido_electrico_1..5` | −28,8 a −28,3 | +5,8 a +6,4 dB | −22,5 | −9,2 a −7,5 dBFS | −9,2 a −7,5 dBTP |
| `sfx_tren_pitido_diesel_1..5` | −27,8 a −27,3 | +4,9 a +5,2 dB | −22,5 a −22,6 | −9,1 a −8,9 dBFS | −9,0 a −8,8 dBTP |

- Ninguno pasa de −3 dBFS ni de −1 dBTP: **no ha hecho falta limitador en ninguno**.
- Dispersión entre variantes: 0,1 dB (dentro de ±0,5).
- Alarma de ataque medida de nuevo (`Assets\TBD\Resources\Audio\sfx_alarma_ataque_1..6.mp3`, solo lectura; idénticos a `entregas\sonido-noche26\unity\Audio`): −13,8 a −15,7 LUFS, media **−14,9 LUFS**, pico −2,2 dBFS. Confirma la medida de Iker.

**En la zona:** `PlayAt` a volumen **0,72** en la cabeza del tren, caída logarítmica de **20 a 400 m**. Queda 6 dB por debajo de la alarma, que va con `Sfx.Play` a 0,6.

**En el mapa:** `Sfx.Play` en 2D a volumen **0,36** (12 dB por debajo de la alarma), como mucho **una vez cada 10 s**.

**Sin ducking** y en **silencio al pausar**.

Cuenta:

- Alarma: −14,9 LUFS con volumen 0,6 (20·log10 0,6 = −4,4 dB) → **−19,3 LUFS** efectivos.
- Pitido en la zona: −22,5 LUFS con volumen 0,72 (−2,9 dB) → **−25,3 LUFS**, 6 dB por debajo de la alarma.
- Pitido en el mapa: −22,5 LUFS con volumen 0,36 (−8,9 dB) → −31,4 LUFS, 12 dB por debajo.

Esto sustituye la línea «Volumen 1» de los pitidos en «Para Iker y Marcos»; la obra sigue igual. La prueba `prueba_obra_pitido.mp3` y la página se han rehecho con los pitidos nuevos. No puedo escuchar: está comprobado midiendo.

— Nuria (Sonido)
