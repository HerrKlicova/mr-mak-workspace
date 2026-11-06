# Encargo para Marcos · Fase A de Pixelab y prueba de audio

Iris (Herramientas IA), 5-nov-2026. **Cambio 22:40**: las voces de prueba son Reig y Mora (guion de Lucía). **Aprobado por Mak** (D-N10): fase A de Pixelab (~450 generaciones) y prueba de audio de ElevenLabs (~60), solo con modelos estables y sin cambiar de plan. Las fases B a G **no se lanzan**: esperan a Eugenio.

Sin prisa: hazlo cuando no frene el hito 3. Para en cuanto el gasto real se desvíe más de un 20 % de lo previsto y avísame.

---

## 0. Antes de empezar (2 comprobaciones, sin coste)
1. **Plan de ElevenLabs**: consulta `GET https://api.elevenlabs.io/v1/user/subscription` con la clave de la variable de entorno y apunta `tier`, `character_count` y `character_limit` en `Audio/Pruebas/registro.csv`. **Si `tier` no es Pro (o superior de pago), no generes música** y avísame: sin plan de pago no hay licencia comercial.
2. **Saldo de Pixelab**: apunta el saldo antes y después de la fase.

## 1. Reglas comunes de Pixelab
- Herramienta: `pixen` (1 generación por imagen). **Nunca** `create_ui_asset` ni `create_image_pro` (10 cada una).
- Prefijo de estilo (todas): `pixel art, gritty post-apocalyptic military, muted desaturated palette, rust, olive drab, concrete grey, dried blood red, high contrast silhouettes, no text, transparent background`
- Sufijo de icono: `single centered game icon, bold readable silhouette, 1px dark outline, flat, no gradient`
- Sufijo de marcador del mapa: `old military staff map symbol, railway map symbology, flat, top-down`
- Si la herramienta acepta imagen de paleta o de referencia, usa `docs/arte/paleta_propuesta_32.png`.
- **Semilla fija por familia** (cargas, alertas, órdenes, estaciones, trenes, unidades) y 8 variantes cambiando solo la semilla secundaria.
- Tamaños: 16×16 y 32×32 cuando se indica; si no, solo 32×32.
- Posproceso **sin gastar generaciones**:
  `python docs/arte/herramientas/pixel_post.py <carpeta_bruta> <carpeta_final> --quitar-fondo`
  (quita el fondo si no viene transparente y reduce a la paleta de 32). Guarda los brutos también.
- Archivos: `Art/Pixelab/<bloque>/vm_<bloque>_<nombre>_<variante>.png` y registro en `Art/Pixelab/registro.csv`.
- Al acabar cada bloque: **hoja de contacto** (todas las variantes en una imagen, a ×4 con filtro de punto) en `Art/Pixelab/contacto/`.

## 2. Fase A · lista exacta

### A1. Cargas (16 y 32 px) · 5 × 8 × 2 = 80
| Nombre | Prompt (tras el prefijo) |
|---|---|
| municion | `ammunition crate with bullets` |
| combustible | `fuel jerrycan` |
| materiales | `stack of steel beams and planks` |
| viveres | `food ration box and water canteen` |
| poblacion | `group of three civilian survivors silhouettes` |

### A2. Alertas (16 y 32 px) · 6 × 8 × 2 = 96
| Nombre | Prompt |
|---|---|
| ataque | `warning sign with zombie hand, attack alert` |
| via_cortada | `broken railway track, cut line alert` |
| tren_detenido | `stopped locomotive with stop symbol` |
| sin_municion | `empty ammunition crate with red cross mark` |
| sin_combustible | `empty jerrycan with red cross mark` |
| asedio | `fortified wall surrounded by horde, siege alert` |

### A3. Órdenes (16 y 32 px) · 6 × 8 × 2 = 96
| Nombre | Prompt |
|---|---|
| aguantar | `raised fist shield, hold position order` |
| seguir | `arrow along railway, proceed order` |
| retirarse | `arrow turning back, retreat order` |
| desplegar | `soldiers stepping off train car, deploy order` |
| embarcar | `soldiers boarding train car, embark order` |
| escoltar | `shield beside locomotive, escort order` |

### A4. Estado de estación (32 px, marcador del mapa) · 4 × 8 = 32
Misma forma para las cuatro: `railway station symbol, circle with platform mark`. Cambia solo el estado: `safe, calm`, `threatened, warning`, `under siege, enemies around`, `lost, ruined`. El color definitivo lo pone Unity con los tokens de Lucía, así que pide el dibujo en grises de la paleta.

### A5. Marcador de tren (32 px) · 4 × 8 = 32
`armored train map marker` con: `moving`, `stopped`, `under attack`, y `work train with crane`.

### A6. Unidades (32 px) · 5 × 8 = 40
`rifle infantry squad`, `heavy machine gun team`, `8x8 armored personnel carrier`, `armored combat train`, `railway artillery wagon with howitzer turret`.

### A7. Prueba de texturas · 20 × 3 = 60
32×32 o 64×64, **seamless tileable texture**: ladrillo, ladrillo con grietas, chapa oxidada, chapa ondulada, hormigón, hormigón manchado, balasto, traviesas, teja árabe, tierra seca, hierba seca, asfalto roto, madera de vagón, pintura militar oliva desconchada, sacos terreros, HESCO, gravilla, barro, nieve sucia, óxido con remaches. Después: comprobar la costura en un cubo y un muro (Blender o Unity) y hacer una captura.

### A8. Prueba de 1 VFX · ~10–30
`diesel locomotive exhaust smoke, effect only, no character, no weapon, transparent background, 8-frame animation loop`, 64×64. Apunta **cuánto cuesta** de verdad: de eso depende el bloque D.

**Total previsto: ~440–460 generaciones.**

## 3. Prueba de audio (ElevenLabs) · ~60
- Efectos: `POST /v1/sound-generation`, `model_id: eleven_text_to_sound_v2` (no uses la v3 si figura como beta), `output_format: wav_44100`.
- Música: Eleven Music, modelo estable (no beta), y **solo si el plan es Pro o superior**.
- Voces: TTS con un modelo estable; procesado de radio después (filtro de banda de 300 a 3.400 Hz y un poco de distorsión), sin gastar créditos.
- Archivos en `Audio/Pruebas/` y registro `Audio/Pruebas/registro.csv` con estas columnas: `id, tipo, prompt, modelo, parametros, creditos_antes, creditos_despues, archivo, nota`.

| # | Tipo | Prompt (inglés) | Parámetros | Nº |
|---|---|---|---|---|
| 1 | SFX | `heavy diesel locomotive running steadily on old rails, rhythmic clack of wheels, engine rumble` | loop, 20 s | 4 |
| 1b | SFX | `diesel locomotive horn, two long blasts, distant valley echo` | 4 s | 3 |
| 2 | SFX | horda lejana: `distant zombie horde, low rumbling moans carried by wind`; media: `scattered zombie groans and shuffling nearby`; cercana: `dense crowd of zombies, footsteps, bodies colliding, banging` | loop, 25 s | 3 × 3 |
| 3 | SFX | `bodies climbing over each other against a wall, scraping, groaning, flesh pile`; `wooden gate splintering and giving way under pressure` | 8 s | 2 × 3 |
| 4 | SFX | coro: `thousands of moans layered into one deep sustained droning chord, eerie choir`; interferencia: `radio static with a slow breathing rhythm` | loop, 20 s | 2 × 3 |
| 4b | Música | motivo: `three descending dissonant notes sung by a choir of moaning voices, ominous, short sting` | 5–10 s | 3 |
| 5 | SFX | `single rifle shot`, `heavy machine gun burst`, `artillery howitzer firing from a train`, `large explosion with debris` | auto | 4 × 2 |
| 6 | SFX | alertas: `subtle military UI ping`, `urgent military alarm beep`, `critical siren blip` | 1–2 s | 3 × 2 |
| 7 | Voz | **Comandante Elena Reig** (jefa del nudo de Sagunto, valenciana, seca y práctica; voz del tutorial): «Valencia tiene comida y gente. Tráelas», «No puedes estar en todas partes». **Julián Mora** (radio e inteligencia; habla cuando suena el motivo): «Ha aprendido que el Tren 1 sale de Sagunto a las 06:00», «Ha aprendido tu horario automático». En español y una frase de cada uno en inglés. Elegir voces de la biblioteca que encajen (mujer madura y firme, hombre tranquilo y tenso) | — | 8 |
| 8 | Música | `tense ambient military score, calm, sparse` / `rising tension, alert` / `siege, relentless percussion, quoting a three-note descending motif` | 30–60 s | 3 × 2 |

## 4. Cuando acabes
Avísame con: saldo antes y después en Pixelab y ElevenLabs, ruta de las hojas de contacto y lo que no haya salido. Lo reviso con Lucía y se lo enseñamos a Eugenio por la mañana para decidir las fases B a G.
