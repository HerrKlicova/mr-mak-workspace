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
- Créditos: unos 43.000 gastados en total (contador 62.481 de 814.102; se reinicia el 5-dic).
