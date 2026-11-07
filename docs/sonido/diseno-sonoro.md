# Diseño sonoro de Vía Muerta · v1 (Nuria, 7-nov-2026)

Documento de dirección de sonido. Parte del criterio de Lucía (docs/sonido/criterio-diseno-lucia.md) y de la investigación de abajo. La guía práctica para Marcos (archivos, eventos y mezclador) está en docs/sonido/integracion-noche26.md.

## 1. Lo que he aprendido (investigación, 7-nov)
Fuentes al final. Algunas páginas no se pudieron abrir desde la nube (asoundeffect.com, designingsound.org, elevenlabs.io): de esas solo tengo el resumen del buscador y lo marco así.

1. **Un arma son capas, no un sonido.** La práctica habitual divide el disparo en mecánica, graves, detalle cercano, detalle lejano y cola. En Apex Legends cada arma tiene al menos cuatro capas que cambian con la distancia, de muy cerca a muy lejos, y además ecualización dinámica según la distancia y hacia dónde apunta (resumen del buscador, sin abrir la página). El cuerpo del disparo se graba seco y la cola (el eco del entorno) va aparte, a veces desplazada en el tiempo.
2. **En un RTS la cámara es el oyente y hay que fingir la masa.** En Supreme Commander el motor pedía más de 4.000 sonidos a la vez; su diseñador dejaba sonar en torno al 10 % con límites de voces por sonido y por grupo (unidades en movimiento, armas, explosiones, ambiente), y el zoom estratégico recortaba lo que se oía. En los foros de Unity se repite la misma idea: no se lanza un sonido por unidad, se crea la impresión con bucles de grupo y variantes que no llaman la atención.
3. **El volumen como prioridad (HDR de DICE).** En Frostbite (Battlefield: Bad Company) cada sonido tiene una «sonoridad» lógica; el sistema escala la mezcla según lo más fuerte que suena en ese momento y descarta lo que queda por debajo. Lo fuerte tapa lo débil de forma natural, y eso también sirve para descartar voces. Audiokinetic matiza que conviene un rango finito, no infinito.
4. **La horda es un sistema, no un sample.** En Dying Light 2 un sistema detecta grupos de zombis, pone un emisor junto a cada grupo y genera un ambiente de horda alrededor del jugador (resumen del buscador). En Left 4 Dead el peso de la amenaza es el volumen abrumador de los infectados comunes, y su mezcla sube y baja según un «director». Las librerías profesionales de horda se graban por estados: reposo, detección, excitación, ataque.
5. **Impacto y peso.** Golpe = transitorio agudo + cuerpo medio + subgrave corto + cola. Para que algo pese más: más cuerpo y subgrave, una cola más larga y áspera y saturación (que engorda los graves sin subir el pico). Truco de contraste: quitar graves y bajar todo justo antes del golpe grande hace que parezca mucho mayor. Hay que hacerle hueco con ducking. Y no abusar del subgrave, o todo se vuelve barro.
6. **Herramientas.**
   - **Unity 6 nativo** (AudioSource, AudioMixer con snapshots y ducking, y el **Audio Random Container**, que elige variantes al azar sin repetir y varía volumen, tono y tiempo). Basta para un proyecto de complejidad media. **Lo propongo para el MVP.**
   - **FMOD Studio**: el preferido para equipos pequeños, con buena integración en Unity; tiene sentido si llega música adaptativa. Las condiciones de licencia que dan los blogs no coinciden entre sí, así que están SIN VERIFICAR. Si se adopta, se comprueba en la web oficial (y nada de pagos sin Eugenio).
   - **Wwise**: más profundo, pensado para proyectos grandes. No lo necesitamos.
   - **Steam Audio** (Valve, Apache 2.0, gratis): oclusión y reverberación físicas. Con cámara cenital casi no aporta; queda descartado por ahora.
   - **ElevenLabs Sound Effects v3**: `model_id = eleven_text_to_sound_v3` en `POST /v1/sound-generation`, según el blog oficial de ElevenLabs (resumen del buscador). **El v3 todavía no hace bucles** (`loop` solo funciona con v2). Como la norma es usar siempre v3, los bucles se hacen después, con un fundido cruzado en ffmpeg. Si salen tomas que no se parecen a lo pedido, se sube `prompt_influence` (por defecto 0,3). En los prompts importa el orden de los sucesos.

## 2. Pilares (los de Lucía, traducidos a reglas de sonido)
| Pilar | Regla |
|---|---|
| El sonido es información | Cada aviso de juego tiene un sonido propio e inconfundible. Alarma roja **solo** para ataque o brecha; el ámbar es un tono distinto y más suave. |
| La distancia la decide la cámara | Cuatro capas por arma ligadas al zoom: **cerca** (mecánica, chasquido, casquillos), **media** (estampido y cola), **lejos** (retumbar con paso bajo, como una tormenta) y **mapa** (murmullo de la estación). |
| Silencio tenso con estallidos | Ambiente muy bajo (−24 dB LUFS relativos). El contraste da el miedo: antes de cada oleada, el ambiente y la horda bajan y se quitan graves durante 1,5 s; después llega el golpe. |
| La horda se oye antes de verse | Lecho continuo de dos capas (lejos y cerca) por grupo, cuyo volumen sigue al número de zombis. Nunca un zombi solista; los gemidos sueltos solo se oyen con mucho zoom. |
| Lo nuestro militar, lo suyo orgánico | Armas, motores e interfaz secos, mecánicos y reales. La horda es carne, roce, respiración y gemido. |
| El tren es el corazón | La llegada del tren baja la horda −6 dB durante 4 s y es el único sonido «cálido» (bocina grave de dos tonos y frenos largos). |

## 3. Distancia y zoom
`z` = zoom normalizado (0 = Z al máximo, 1 = X al máximo).
| Capa | z | Qué se oye | Tratamiento en tiempo real |
|---|---|---|---|
| Cerca | < 0,35 | Disparo completo, mecánica, casquillos e impactos sueltos | 3D (spatialBlend 0,7), sin filtro |
| Media | 0,35–0,7 | Estampido y cola; sin impactos pequeños | Ecualización ya horneada, sin filtro en el mezclador; 3D 0,5 |
| Lejos | ≥ 0,7 | Retumbar del frente, ráfagas de grupo, cañón | 2D; paso bajo de 1,8 kHz ya horneado, sin filtro en el mezclador; sin impactos de bala |
| Mapa | fuera de la estación | Murmullo de combate por estación activa | Snapshot `Mapa`: −18 dB, paso bajo a 800 Hz |
Un solo filtro por sonido (D-N134): la distancia viene horneada en los archivos; el único filtro en tiempo real es el del snapshot Mapa.
Fundido cruzado de 0,15 en `z` entre capas. La cola se lanza 40–120 ms después del cuerpo cuanto más lejos esté, porque el sonido tarda en llegar.

## 4. Jerarquía de mezcla y voces
1. Alertas → 2. Armas y explosiones → 3. Horda → 4. Vehículos y tren → 5. Ambiente y música.
- Alertas hacen ducking de −8 dB sobre todo lo demás; el 30 mm hace ducking de −3 dB sobre los fusiles durante 300 ms, para que se sienta más gordo.
- **Sonoridad como prioridad (al estilo HDR):** cada evento lleva un valor de sonoridad (fusil 0,5; MG 0,6; 30 mm 1,0; brecha 1,0; impacto de bala 0,2). Por fotograma se ordenan y suenan los de más peso hasta llenar el tope de la categoría.
- Topes: 48 voces reales y 256 virtuales en total. Armas 12, Impactos 8, Horda 6, Muros 3, Vehículos 4, Tren 2, Ambiente 3, Alertas 2, UI 2.
- **Fuego de pelotón**: los disparos se cuentan por celda de 20 m. Con menos de 4 tiradores suena cada ráfaga (con 80 ms mínimo entre sonidos de la misma celda); con 4 o más, un bucle de pelotón cuyo volumen sigue al número de tiradores. Así suenan todas las balas, no solo las trazadoras.

## 5. Lista de sonidos (v1)
La tabla completa con los prompts está en docs/sonido/herramientas/catalogo_sfx.json; aquí, el resumen. Cinco variantes de cada sonido como mínimo.
- **Armas**: G36E cerca, media y lejos; mecánica y casquillos del G36E; MG4E cerca y lejos; G28 cerca; AG36 (lanzagranadas) disparo; C90 (lanzacohetes) disparo; 30 mm del Dragón cerca, media y lejos; pelotón cerca y lejos (bucles); cola de disparo en entorno urbano.
- **Impactos**: bala en zombi, bala en hormigón, bala en metal, explosión del 30 mm, explosión de granada o cohete, muerte de zombi (caída).
- **Horda**: lejos (bucle), cerca (bucle), acercándose, gemidos sueltos de cerca, gritos de excitación al detectar, golpes contra el muro (bucle).
- **Muros**: impacto fuerte, brecha y derrumbe, construcción o reparación.
- **Tren**: llegada, salida, marcha o ralentí (bucle), bocina.
- **Vehículos**: motor del VAMTAC, motor del Dragón, rotor del NH90 (bucles), aterrizaje o despegue del NH90.
- **Ambiente nocturno por estación**: estación pequeña (viento, catenaria, perro lejano), pueblo de huerta (grillos, acequia, viento entre naranjos), ciudad grande infestada (Castellón: alarmas lejanas de coches, chapa, cristales, tensión) y fuego crepitando.
- **Interfaz y alertas**: clic, orden dada, ataque o brecha (rojo), aviso (ámbar), radar, aviso previo de la horda (sirena lejana), munición baja, estación caída, estación liberada.

## 6. Proceso de producción
1. Se genera en el PC de Eugenio con `docs/sonido/herramientas/generar_sfx.py` (modelo v3; la clave solo se lee de `ELEVENLABS_API_KEY`).
2. Posproceso con ffmpeg (`postproceso_sfx.py`): recorte de silencios, normalización de sonoridad por grupo, bucles con fundido cruzado y WAV de 48 kHz y 16 bits.
3. Escucha y descarte: cada toma que no sirva se regenera. Lo que no esté comprobado frente a una referencia real queda marcado SIN VERIFICAR.
4. Entrega en `C:\Dev\mr-mak-workspace\entregas\sonido-noche26\` y demo para Eugenio en la galería.

## Fuentes
- Splice, «How to design a weapon sound for video games»: https://splice.com/blog/?p=16617
- A Sound Effect, Apex Legends: https://asoundeffect.com/apex-legends-sound (solo el resumen del buscador)
- Designing Sound, Frank Bry sobre Supreme Commander: https://designingsound.org/2010/12/29/frank-bry-special-sound-design-for-supreme-commander-this-is-just-way-too-big/ (solo el resumen del buscador)
- Ben Houge, el audio de EndWar: https://benhouge.com/endwar.html
- Unity Discussions, «RTS too many sounds»: https://discussions.unity.com/t/rts-too-many-sounds/767572
- DICE, «HDR Audio: Adaptive mixing in Frostbite»: https://www.slideshare.net/slideshow/adaptive-mixing-in-frostbite/3128152
- Designing Sound, HDR en Wwise: https://designingsound.org/2013/06/21/finding-your-way-with-high-dynamic-range-audio-in-wwise/
- A Sound Effect, audio de Dying Light 2: https://asoundeffect.com/dying-light-2-gameaudio/ (solo el resumen del buscador)
- Violet Recording, sonidos de impacto: https://violetrecording.com/how-to-make-impact-sounds/
- GameDev.net, «Bigger Than Big: The Game Audio Explosion»: https://gamedev.net/tutorials/audio/music-and-sound-fx/bigger-than-big-the-game-audio-explosion-r2317
- Unity 6, Audio Random Container: https://docs.unity3d.com/6000.1/Documentation/Manual/AudioRandomContainer-fundamentals.html
- Steam Audio: https://github.com/ValveSoftware/steam-audio/releases
- ElevenLabs, «SFX v3 for developers»: https://elevenlabs.io/blog/sfx-v3-for-developers (solo el resumen del buscador; el PC lo comprueba antes de generar)

— Nuria (Sonido)
