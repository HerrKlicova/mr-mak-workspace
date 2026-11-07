# Sonido de Noche26: qué es cada archivo y dónde va (Nuria → Marcos) · 7-nov

Está hecho para tu `Sfx.cs` (`PlayDist(evento, ortho, vol, minGap)` con cerca < 14 ≤ media < 34 ≤ lejos). El diseño completo está en docs/sonido/diseno-sonoro.md.

**Dónde están**: `C:\Dev\mr-mak-workspace\entregas\sonido-noche26\unity\Audio\`. Copia todo el contenido a `Assets/TBD/Resources/Audio/`. Son MP3 de 192 kbps a 48 kHz, con la mezcla ya hecha (D-N134, abajo). Los másteres WAV están en `entregas\sonido-noche26\master\` y el listado completo, en `manifiesto.csv`.

**Importación**: lo de menos de 3 s, Decompress On Load. Bucles y ambientes, Streaming. Lo mono es para fuentes 3D; lo estéreo (bucles, ambientes y capas «lejos»), en 2D.

## Mezcla hecha en los archivos (D-N134, 7-nov)
Como la mezcla viene hecha en los archivos, **en `Sfx.PlayDist` pon los volúmenes 1, 1 y 1 para cerca, media y lejos, y vol 1,0 tanto en el fusil como en el cañón** (antes: fusil 0,7). No compenses nada más por distancia.
- Sonoridad integrada por distancia (cerca / media / lejos): fusil_rafaga, ametralladora, tirador, granada_40 y peloton −18 / −24 / −31 LUFS; cohete −14 / −24 / −31; canon_30 −13 / −19 / −25 (medido: −14,0 / −19,3 / −25,3, el limitador no deja subir más el cerca).
- Capas lejos con paso bajo a 1,8 kHz de pendiente pronunciada: por encima de 2 kHz quedan al menos 30 dB por debajo del total.
- `horda_acercandose` crece sin saltos de más de 3 LU entre ventanas de 3 s.
- Ningún archivo pasa de −1 dBTP (pico verdadero, medido sobre el MP3).
- Medidas de cada archivo: `entregas\sonido-noche26\medidas_dn134.csv` (las de antes, en `medidas_dn134_antes.csv`). Se repite con `herramientas\sonido\postproceso_sfx.py` y se mide con `herramientas\sonido\medir_dn134.py`.

## 1. Eventos con distancia (`PlayDist`): `sfx_<evento>_<cerca|media|lejos>_<1..8>.mp3`
| Evento | Cuándo | Notas |
|---|---|---|
| `fusil_rafaga` | ráfaga de G36E | Ya lo tienes conectado. Toma real a cada distancia. |
| `ametralladora` | MG4E (también la del VAMTAC) | Ya conectado. La «media» es la «cerca» con paso bajo y eco, ya hecho en el archivo. |
| `granada_40` | AG36 | Ya conectado. «Media» y «lejos», derivadas. |
| `canon_30` | 30 mm del Dragón | Ya conectado. Toma real a cada distancia. Ya viene 4,4 LU por encima del fusil en el archivo: vol 1,0, igual que el fusil. |
| `tirador` | G28, disparo suelto | Nuevo. |
| `cohete` | C90 | Nuevo. |
| `peloton` | **bucle** mientras ≥4 tiradores disparan en la misma celda de 20 m | Nuevo. Volumen = min(1, tiradores/8). Con el bucle sonando, no lances ráfagas sueltas de esa celda. |
| `horda` | **bucle** de lecho de la horda | Nuevo. Volumen = min(1, zombis vivos en la estación/150). Es lo que hace que la horda «se oiga antes de verse». |

## 2. Eventos sin distancia: `sfx_<evento>_<1..8>.mp3`
Te pido un `Sfx.Play(evento, posicion, vol, minGap)` que elija la variante al azar (sin repetir la anterior), con tono ±5 %. Con zoom lejano (ortho ≥ 34), no lances los marcados «solo cerca».
| Evento | Cuándo | Tipo | Notas |
|---|---|---|---|
| `g36e_mecanica` | tras cada ráfaga, cerca | suelto | Solo cerca. Casquillos y cerrojo. vol 0,5 |
| `g36e_recarga` | recarga de pelotón | suelto | Solo cerca |
| `cola_urbana` | 60–120 ms tras un disparo fuerte (30 mm, G28, C90) | suelto | Eco de estación; da tamaño |
| `batalla_mapa` | **bucle** por cada estación en combate mientras estás en el mapa | bucle | 2D, vol 0,3 |
| `impacto_carne` | bala que da a un zombi | suelto | Solo cerca. minGap 0,05 |
| `impacto_hormigon` | bala en muro o suelo | suelto | Solo cerca |
| `impacto_metal` | bala en vehículo o tren | suelto | Solo cerca |
| `impacto_30mm` | impacto del cañón | suelto | A cualquier zoom |
| `explosion_granada` | impacto del AG36 | suelto | A cualquier zoom |
| `explosion_grande` | impacto del C90 o explosión de vehículo | suelto | A cualquier zoom |
| `zombi_caida` | muere un zombi | suelto | Solo cerca. minGap 0,08 |
| `zombi_muerte` | muere un zombi (1 de cada 4) | suelto | Solo cerca |
| `zombi_gemido` | aleatorio, 1 cada 2–4 s, en un zombi a la vista | suelto | Solo cerca |
| `horda_acercandose` | aviso de oleada, una vez | suelto | 2D. 5 variantes (la 6.ª se descartó por saltos de sonoridad) |
| `horda_excitada` | la horda detecta a tus unidades o llega al muro | suelto | 3D en el grupo |
| `zombi_golpe_muro` | **bucle** en cada tramo de muro con atacantes | bucle | 3D, alcance 40 m |
| `muro_impacto` | golpe fuerte al muro | suelto | minGap 0,3 |
| `muro_brecha` | brecha en el muro | suelto | Junto con `alarma_ataque` |
| `muro_construccion` | construir o reparar | suelto | |
| `tren_llegada` | llega el tren | suelto | Baja la horda −6 dB durante 4 s: es el alivio |
| `tren_salida` | sale el tren | suelto | |
| `tren_ralenti` | **bucle** con el tren parado | bucle | 3D |
| `tren_bocina` | aviso del tren | suelto | |
| `vamtac_motor` | **bucle** con el VAMTAC moviéndose | bucle | 3D, tono 0,85–1,15 según velocidad |
| `dragon_motor` | **bucle** con el Dragón moviéndose | bucle | Ídem |
| `nh90_rotor` | **bucle** con el NH90 en vuelo | bucle | 3D, alcance 120 m |
| `nh90_aterrizaje` / `nh90_despegue` | al tomar tierra o despegar | suelto | |
| `amb_estacion_pequena` | **bucle** de ambiente en estaciones pequeñas (Sagunto) | bucle | 2D, vol 0,5 |
| `amb_huerta` | **bucle** en estaciones de huerta (Nules) | bucle | 2D |
| `amb_ciudad_infestada` | **bucle** en Castellón | bucle | 2D |
| `amb_viento` | **bucle** con zoom lejano (X), encima del ambiente | bucle | vol = z |
| `fuego_crepitar` | **bucle** en cada fuego de suelo | bucle | 3D, alcance 25 m |
| `ui_clic` | clic de interfaz | suelto | 2D |
| `ui_orden` | orden dada a una unidad | suelto | |
| `ui_construir` | colocar una estructura | suelto | |
| `ui_error` | acción no permitida | suelto | |
| `alarma_ataque` | **solo** ataque o brecha (rojo 982420) | suelto | Prioridad máxima |
| `aviso_ambar` | aviso ámbar | suelto | |
| `radar_ping` | barrido del radar | suelto | |
| `radar_contacto` | el radar detecta la horda | suelto | |
| `aviso_horda` | aviso previo de la horda | suelto | Sirena lejana |
| `municion_baja` | unidad con poca munición | suelto | |
| `estacion_caida` / `estacion_liberada` | cae o se libera una estación | suelto | |

## 3. Mezcla (AudioMixer `Mezcla`)
Grupos: Alertas, UI, Armas, Impactos, Horda, Muros, Vehículos, Tren y Ambiente.
- Las Alertas hacen ducking a Armas, Horda y Ambiente: −8 dB, ataque de 20 ms y liberación de 400 ms.
- El `canon_30` hace ducking de −3 dB a Armas durante 300 ms, para que «pegue».
- Antes de la oleada (cuando suena `aviso_horda`), Ambiente y Horda bajan −6 dB durante 1,5 s, sin filtro: el silencio antes del golpe.
- Un solo filtro (D-N134). Las capas media y lejos ya llevan su ecualización en el archivo (lejos: paso bajo de 1,8 kHz). En el mezclador NO se pone ningún paso bajo por distancia, ni en Armas, ni en Impactos, ni en Horda. El único filtro en tiempo real es el paso bajo de 800 Hz del snapshot Mapa.
- Pon un limitador en Master a −1 dB.
- Snapshots `Partida` y `Mapa`. En `Mapa`, Armas, Impactos y Horda van a −18 dB con paso bajo de 800 Hz, así que la noche se sigue oyendo fuera de pantalla. La transición dura 0,5 s.

## 4. Voces
- `AudioSettings`: 48 voces reales y 256 virtuales. Usa un pool de AudioSource, sin `Instantiate` por disparo.
- Topes por grupo: Armas 12, Impactos 8, Horda 6, Muros 3, Vehículos 4, Tren 2, Ambiente 3, Alertas 2 y UI 2. Si se llena un grupo, se descarta el sonido más lejano a la cámara. La columna `sonoridad` del manifiesto es su prioridad.
- Los sonidos no siguen a las trazadoras, sino a todos los disparos agrupados por celda: ráfagas sueltas por debajo de 4 tiradores, y el bucle `peloton` desde 4.

## 5. Control de calidad (7-nov)
- Hay 449 MP3 en `unity/Audio` para 69 eventos (tras la D-N134; antes eran 450). Ninguno pasa de −1 dBTP (pico verdadero); medidas en `medidas_dn134.csv`.
- Revisé las 402 tomas por su envolvente: el rango dinámico en ventanas de 10 ms y si tienen transitorio. Descarté 18 (impactos sin transitorio, clics y munición casi mudos, una mecánica y un ambiente 16 dB por debajo de sus hermanas) y las regeneré. Hormigón y metal fallaron también con el mismo prompt, así que lo cambié en `catalogo_sfx.json` (golpe único con ataque fuerte, 1,0 y 0,8 s, influencia 0,75) y las repetí. Todo lo descartado está en `entregas/sonido-noche26/descartes/`, con la ronda en el nombre.
- `postproceso_sfx.py` ahora normaliza el pico antes de recortar el silencio. Si una toma queda vacía, se para con un mensaje claro.
- Demo de mezcla: `entregas/sonido-noche26/demo/demo_lucia.mp3` (45,7 s; fusil a 0,7 y cañón a 1,0).

— Nuria (Sonido)
