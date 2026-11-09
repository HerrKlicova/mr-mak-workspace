# Sonido de la Colmena e informe (encargo de Lucía, 9-nov, 00:02)

Los avisos de la Colmena (CO-1 a CO-4, en `docs/informe-textos.md`), el aviso ámbar de la señal 6 y el sonido de abrir el Informe de inteligencia. Todo es interfaz y suena a sistema militar: tonos electrónicos graves, papel y nada de voces, gritos, rugidos ni música.

- 30 OGG: mono, 44,1 kHz, Vorbis, nivel horneado por LUFS integrado y **sin normalizar**. Hay 5 variantes de cada sonido.
- `prueba.mp3` (21,4 s): acecho → enjambre → vuelta a acecho → dispersa, con 2 s entre cada uno, y después la señal 6 y abrir el informe. Al final va la alarma de ataque del juego (`sfx_alarma_ataque_1`, leída del proyecto Unity sin tocarlo) a 0,6.
- `escucha.html` (https://claude.ai/artifact/FAL2znujxxoMPTnuXHhpRq): la prueba y las 5 variantes de cada sonido, para elegir.
- `medidas.json`: las medidas de cada OGG, las candidatas y los descartes con su motivo.
- Herramienta: `herramientas/sonido/colmena_informe.py`. Brutos en `herramientas/sonido/brutos_colmena_informe/`.

## Medidas (sobre los OGG finales)

| Sonido | Archivos | LUFS | Pico máx. | Duración |
|---|---|---|---|---|
| CO-1 Al acecho | `sfx_colmena_acecho_1..5` | −26,0 (las 5) | −15,5 dBFS | 1,24–1,44 s |
| CO-2 Enjambre | `sfx_colmena_enjambre_1..5` | −22,4 a −22,5 | −9,2 dBFS | 1,42–1,74 s |
| CO-3 Vuelta a Al acecho | `sfx_colmena_vuelta_acecho_1..5` | −28,0 | −15,7 dBFS | 1,24–1,76 s |
| CO-4 Dispersa | `sfx_colmena_dispersa_1..5` | −30,0 | −15,2 dBFS | 1,05–1,35 s |
| Señal 6 (ámbar) | `sfx_ui_aviso_senal6_1..5` | −32,0 | −17,1 dBFS | 0,42–0,57 s |
| Abrir el Informe | `sfx_ui_informe_abrir_1..5` | −29,9 a −30,1 | −7,4 dBFS | 0,77–0,95 s |

- Entre las variantes de un mismo sonido hay 0,2 dB de diferencia como mucho (se pedía ±0,5). Todos los picos están por debajo de −3 dBFS.
- La referencia es la alarma de ataque a 0,6, que da −19,2 LUFS medidos (se esperaba −19,3). Enjambre queda 3,3 dB por debajo.
- Enjambre: la variante 1 tiene 2 pulsos y las otras 4 tienen 3. El v3 suele dar 4 pulsos cada 0,5 s, así que se corta justo antes del 4.º con 40 ms de fundido.
- **Fuera de rango:** `sfx_colmena_enjambre_1` dura 1,42 s, 0,08 s menos del mínimo de 1,5 s. Lo acepté para no pasar del tope de créditos. Si Lucía no la quiere, se queda con las otras 4.
- Vuelta a Al acecho: todas bajan de tono (glissando) y se apagan. Dispersa: se desvanecen entre 26 y 37 dB.
- Abrir el Informe: las 5 son de papel (sacar y desplegar la hoja o pasar una página). Las dos de teletipo llevaban un tono fijo de motor y las descarté.

## Descartes (43 de 73 tomas)

- 28 demasiado cortas tras quitar el silencio: 11 de acecho (de 0,35 a 0,99 s), 10 de enjambre (de 0,57 a 1,36 s) y 7 de la señal 6 (de 0,09 a 0,29 s). El v3 tiende a dar tonos muy cortos.
- 2 mudas con HTTP 200 (dispersa).
- 3 con siseo agudo o poco graves (2 de dispersa con un centroide de 9 a 14 kHz y 1 de enjambre).
- 2 de dispersa con varios golpes y 1 que no se desvanece. 2 de vuelta que no se apagan.
- 2 de teletipo con un tono fijo de 650 a 730 Hz.
- 3 válidas que sobraban.
- No hubo descartes por voz o música en las finales: ninguna tiene más de 3 notas distintas salvo los glissandos, y ninguna lleva un tono fijo que parezca bocina. **No puedo escuchar:** todo está comprobado midiendo. Que Lucía o Eugenio confirmen de oído que nada suena a terror.

## Créditos

ElevenLabs `eleven_text_to_sound_v3`, la clave solo de `ELEVENLABS_API_KEY`. El contador estaba en 84.257 antes y en 85.632 después: **1.375 créditos** (el tope era 1.500). Fueron 73 tomas.

## Notas para Iker (integración)

- Los OGG van a `Assets/TBD/Resources/Audio`. Al importar, sin Normalize (AudioImportRules.cs).
- Todos se tocan con `Sfx.Play` a **1,0**, en **2D**. Los niveles ya van horneados: no hay que tocar el volumen.
- Un sonido por cada cambio de estado de la Colmena: CO-1 al pasar a Al acecho, CO-2 a Enjambre, CO-3 al bajar de Enjambre a Al acecho y CO-4 a Dispersa. Si llegan dos cambios seguidos, suena solo el último.
- La señal 6 suena una vez cada 10 s como mucho.
- Abrir el Informe suena una vez al abrir el panel.
- Todos en silencio al pausar.
- La variante se elige por semilla (determinista), como en el resto de estructuras.

— Nuria (Sonido)
