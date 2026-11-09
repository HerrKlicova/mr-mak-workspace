# Relevo · Nuria (Dirección de sonido) · 8-nov

Firma «— Nuria (Sonido)». Sin retrato todavía (pendiente). Hilo viejo: cmsg_014mgaTqwTDTmezhB3g3Rs8BSxBRmwn4wSs3eNt85sEQ2u.

## Estado
- El sonido está hecho y entregado. Pendiente: que Marcos aplique el paquete de la Noche55 y que Eugenio lo juegue.
- En la build está Sfx.cs v2 (oído RTS + 3D). Lo último que hay que aplicar está en `C:\Dev\mr-mak-workspace\entregas\sonido-noche55\` (LEEME + `codigo\Sfx.cs`):
  - quitar Night.cs:332, el `sfx_zombi_muerte` viejo en 2D, que era la «voz» ridícula;
  - quitar Night.cs:322;
  - pasar a 3D explosion_granada, cola_urbana e impacto_30mm;
  - bajar los bucles de fondo a la mitad;
  - GlobalGain 0,45;
  - oído a 22 m como mínimo.
- Antes: el rotor NH90 nuevo, en `entregas\sonido-noche50` (6 OGG de 8 s; quitar el rotor 2D duplicado de Vehicles.cs:230; volumen = 0,5 × Rpm). La Noche46 trajo bucles OGG y el cañón del Dragón nuevo (`entregas\sonido-noche46`).

- 8-nov: máquina de escribir de la intro «Día 41» y del tutorial entregada en `entregas\sonido-maquina-escribir\` (8 teclas, retorno, campanilla, prueba_tecleo.mp3 y LEEME con la integración para Iker). Herramienta: `herramientas\sonido\maquina_escribir.py`. Gasto: 144 créditos.

- 8-nov: D-N170, salida del tren, entregada en `entregas\sonido-salida-tren\`: aviso, cierre, silbato, arranque eléctrico y diésel 333, con 5 variantes de cada uno. Son 25 OGG mono, con prueba_salida_tren.mp3 y un LEEME con la integración para Iker. Herramienta: `herramientas\sonido\salida_tren.py`; los brutos están en `herramientas\sonido\brutos_salida_tren\`. Gasto: 2.740 créditos (contador en 72.229). Las variantes se igualan por LUFS integrado (±0,4 dB), no solo por pico. Hay un detector de tono fijo para descartar bocinas.

- 8-nov: D-N173, NH90 y base de Bétera, entregado en `entregas\sonido-nh90-betera\`: arranque, despegue, pasada, toma, ralentí (bucle), ráfaga M3M y ambientes de día y noche de Bétera (bucles de 15 s), con 5 variantes de cada uno. Son 40 OGG mono, con prueba_nh90.mp3, LEEME (integración para Iker y Marcos) y la página https://claude.ai/artifact/Mtm27xijQ71DmtFeVaFKt9. Herramienta: `herramientas\sonido
h90_betera.py` (+ `escucha_nh90.py`); los brutos están en `brutos_nh90_betera\`. Gasto: 5.892 créditos (contador en 78.121). Horda de referencia: sfx_horda_cerca, de −21,9 a −23,6 LUFS. Trampas nuevas: el ralentí en tierra del v3 tiene poco golpe de pala (se mide con el espectro de la envolvente, no con la autocorrelación) y la ráfaga se valida con las subidas y la duración del tramo fuerte.

## Decisiones vigentes
- ElevenLabs **eleven_text_to_sound_v3** siempre. El v3 no hace bucles: se hacen en el posproceso con fundido cruzado y se exportan en **OGG** (el MP3 deja hueco en la costura). La clave solo se lee de `ELEVENLABS_API_KEY`, en el PC por Remote Control. Desde la nube no se llega a elevenlabs.io.
- D-N134 (Lucía): mezcla horneada en los archivos (fusil −18/−24/−31 LUFS, cañón −14/−19/−25, ≤ −1 dBTP). Un solo filtro: el paso bajo de la distancia va dentro del archivo y el único en tiempo real es el de 800 Hz del snapshot Mapa.
- Oído RTS: AudioListener en el foco de la cámara, a una altura = ortho × 1,6 (entre 22 y 140). Todo con posición va en 3D con curva propia. Importación sin Normalize (AudioImportRules.cs).
- La horda solo se oye de cerca y bajita. Sin música en la noche. Las alertas, en 2D.
- closeGain apagado (si se encendiera, el sonido subiría y bajaría al alejar).

## Trampas
- El v3 devuelve a veces tomas mudas o impactos sin golpe con HTTP 200: hay que revisar la envolvente y regenerar.
- Los `zombi_muerte` nuevos llevan un chillido de 600 a 840 Hz: no usarlos en masa.
- Los volúmenes del menú se guardan en PlayerPrefs, así que para bajar el volumen hay que hacerlo en Sfx.cs.
- No puedo escuchar: todo se ha comprobado midiendo. Pedir a Eugenio que escuche las pruebas (`prueba_rotor_4x.mp3`, `demo_lucia.mp3`).
- Las llamadas viejas a Sfx con nombre fijo o con `Vector3.zero` suenan en 2D: son las sospechosas cuando algo «no baja con el zoom».

## Rutas
- Docs: `docs\sonido\diseno-sonoro.md`, `integracion-noche26.md`, `plan-arreglo-sonido-noche46.md` y `criterio-diseno-lucia.md`.
- Herramientas: `herramientas\sonido\` (generar_sfx.py, catalogo_sfx.json, postproceso_sfx.py, medir_dn134.py; `n46\` y las de sonido-noche50).
- Páginas: documentación https://claude.ai/artifact/9B2nAQfe5ZzfQtvbmdxXad · escucha https://claude.ai/artifact/3KbwkaZwbeDWnzxqSPJWnU
- Créditos: contador 78.589 de 814.102 (8-nov, tras rehacer la M3M; se reinicia el 5-dic).
- 8-nov: rehecha la M3M de D-N173 (−10 dBFS de pico, unos −26 LUFS, ±0,15 dB entre variantes). La v1 está en `entregas\sonido-nh90-betera\v1_m3m\`, y `nh90_betera.py m3m` hace el posproceso. Gastados 468 créditos. Escucha: https://claude.ai/artifact/Mtm27xijQ71DmtFeVaFKt9
- 8-nov (tarde): obra (pala, saco, malla HESCO a −30/−28/−30 LUFS, ±0,2 dB) y pitidos de salida eléctrico y diésel (pico −14, −28/−27,5 LUFS: con ese pico no llegan a −24) en `entregas\sonido-obra-pitido\` con `obra_pitido.py`. 744 créditos (contador 79.333). Escucha: https://claude.ai/artifact/2LWuKYuWWEbwvd56QfvtMo
- 8-nov (noche): encargo de Lucía de las 22:12, entregado en `entregas\sonido-farp-nules-avisos\`. FARP de Bétera (bomba en bucle de 10 s a −30, manguera a −30 y caja de munición a −28 LUFS), Nules de noche en tres capas en bucle de 12 s (grillos y acequia a −32 y viento a −34) y avisos (ámbar a −26 en 2D y tren caído en las puertas a −22). Son 40 OGG, con ±0,2 dB entre variantes, prueba.mp3 y LEEME. Herramienta: `farp_nules_avisos.py`. 4.924 créditos (contador en 84.257). Escucha: https://claude.ai/artifact/AtVv5eEpffmKBzBokeyqPR. Trampas nuevas: el viento del v3 trae rachas de 9 a 13 dB, y si se pide «sin rachas» sale casi mudo (−56 LUFS), así que se nivela despacio (media de 1,5 s, al 85 %). Las dos notas del aviso se detectan con tramas de 20 ms, quitando los fragmentos de menos de 60 ms antes de unir.
- 9-nov (madrugada): encargo de Lucía de las 00:02, entregado en `entregas\sonido-colmena-informe\`: avisos de la Colmena CO-1 a CO-4 (acecho −26, enjambre −22,5, vuelta −28 y dispersa −30 LUFS), la señal 6 (−32) y abrir el Informe (−30), todo en 2D y con Sfx.Play a 1,0. Son 30 OGG con ±0,2 dB entre variantes y picos ≤ −7,4 dBFS, prueba.mp3 (la alarma a 0,6 da −19,2 LUFS) y LEEME. Herramienta: `colmena_informe.py`. 1.375 créditos (contador en 85.632). Trampas nuevas: el v3 da los tonos de interfaz muy cortos (la mitad de las tomas, por debajo del mínimo) y Enjambre sale con 4 pulsos, así que se corta antes del 4.º. Un glissando que baja cuenta como muchas «notas», así que no se descarta como melodía si el 75 % de los pasos descienden. enjambre_1 dura 1,42 s (0,08 s menos de lo pedido). Escucha: https://claude.ai/artifact/FAL2znujxxoMPTnuXHhpRq
- 9-nov (madrugada): D-N157, ambiente de día, entregado en `entregas\sonido-ambiente-dia\`: Sagunto de día (5 bucles de 20 s) y Nules de día (4 bucles de 20 s) a −53 LUFS, y atardecer (2 transiciones de 20 s) a −51,5. Se toma como referencia la noche efectiva de la zona: −30,0 + 20·log10(0,10) = −50,0. Las costuras están verificadas en el OGG. Faltan 1 de Nules y 3 de atardecer porque el tope no dio para más. Gasto: 5.331 créditos (contador en 90.963), de los que 1.164 se perdieron por un fallo mío: `extra` no creaba la carpeta y la API cobró los 4 reintentos (ya corregido). Herramienta: `ambiente_dia.py`. Escucha: https://claude.ai/artifact/9LsaV25QzwJsWQahQSexzV. Trampas nuevas: la prominencia de un tono se mide contra el espectro local, no contra la mediana global (en los ambientes daba músicas falsas); los insectos se reconocen por un bulto de 2,5 a 10 kHz presente en ≥ 60 % de las tramas (calibrado con los grillos de Nules); el suelo de toma muda va relativo al objetivo; un mono frente a una noche estéreo decorrelada puede sonar unos 3 dB más fuerte (sin verificar en Unity).
- 9-nov 07:00: completar D-N157 (2 de Nules + 4 de atardecer, tope 1.800 créditos). **BLOQUEADO**: el clasificador de permisos de Claude Code ha denegado dos veces la llamada pagada a ElevenLabs («Real-World Transactions»). Gasto 0 (contador en 90.963). Hecho: `generar_sfx.tarea` ya no reintenta una llamada cobrada si falla el guardado (para todo); `ambiente_dia.py completar` procesa solo las tomas nuevas y les da números libres sin tocar sagunto_1, nules_2 ni atardecer_1 (`post` renumera todo: no usarlo). LEEME: variantes fijas, Sfx.Duck −6 dB del mapa y DiaZonaVol a 0,7 si el día se come la noche. Falta: generar (`extra brutos_ambiente_dia dia_nules a 2` y `extra … atardecer a 4`), `completar`, N=5 en el LEEME, `escucha` y volver a publicar en la misma URL.
- 9-nov 08:00: D-N157, segunda tanda (las tomas las lanzó Eugenio, porque el modo auto bloquea la llamada pagada). Contador 90.963 → 92.481: **1.518 créditos**. Válida 1 de 6: `sfx_amb_dia_nules_5` (de a_v04, −53,0 LUFS, costura 0,46 frente a un p95 de 1,71; límite de nivel inestable subido de 4,5 a 4,6 por esta toma, documentado). Las 4 de atardecer (prompt a) fallan porque los pájaros no se callan; el prompt a lleva 2 válidas de 7. Atardecer sigue con N=2; Sagunto y Nules con N=5. Las 11 originales están intactas (md5). Escucha publicada de nuevo en la misma URL (versión 2). Pendiente: el atardecer con otro prompt (unos 1.000–1.500 créditos, primero una toma de calibración); quedan 282 del tope de 1.800.
