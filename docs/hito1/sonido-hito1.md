# Sonido del Hito 1, núcleo v2 (Nuria, 11-nov)

Encargo: `docs/hito1-reparto.md`. Uso primero lo que ya existe en `Assets/TBD/Resources/Audio`. He medido todos los clips (LFS y ebur128). Nivel efectivo = LUFS + 20·log10(vol), sin contar `GlobalGain` 0,45, que va igual para todo.

Rama de tbd: **`nuria/sonido-hito1`**. Solo cambian los archivos de audio y no toca código, porque el código del Hito 1 aún no existe. En la rama:
- `tren_salida` y `tren_llegada` normalizados a −20,5 LUFS. Antes había 8,7 dB y 4,7 dB de diferencia entre variantes. La 5 de salida no llegaba al nivel y se ha cambiado por la 6, así que quedan 5.
- `ui_construir` normalizado a −26,3 y `ui_error` a −24,3.

## Tabla de evento → archivo

| Evento | Archivo | Llamada | Vol. | 2D/3D | Estado |
|---|---|---|---|---|---|
| **Trazar vía: el tramo de la vista previa es válido** (al soltar el clic) | `sfx_ui_construir_1..6` (−26,3) | `Sfx.Play("ui_construir", Vector3.zero, 0.6f, 0.1f)` | 0,6 | 2D | ✅ ya existe |
| **Trazar vía: el tramo no es válido** | `sfx_ui_error_1..6` (−24,3) | `Sfx.Play("ui_error", Vector3.zero, 0.5f, 0.3f)` | 0,5 | 2D | ✅ |
| **Tender vía** (la cuadrilla trabaja en la cabeza de obra) | ahora `sfx_muro_construccion_1..6` (−19,3 a −22,4) → **nuevo** `sfx_via_tendido_1..5` (−24) | `Sfx.PlayAt("via_tendido", cabeza, 0.8f, 1.2f)` cada 1,2 a 2 s mientras trabaja | 0,8 | 3D, 120 m | ⏳ provisional hasta generar |
| **Tramo de vía terminado** | **nuevo** `sfx_via_tramo_hecho_1..5` (−24) | `Sfx.PlayAt("via_tramo_hecho", fin_del_tramo, 0.9f, 0.5f)` | 0,9 | 3D | ⛔ falta generar |
| **El tren sale** | secuencia de `SalidaTren` (aviso, cierre, silbato y arranque; ya conectada en el juego viejo) + `sfx_tren_salida_1..5` (−20,5) | `Sfx.PlayAt("tren_salida", locomotora, 0.8f, 5f)` | 0,8 | 3D, 300 m | ✅ |
| **El tren llega** | `sfx_tren_llegada_1..6` (−20,5) | `Sfx.PlayAt("tren_llegada", anden, 0.8f, 5f)` | 0,8 | 3D, 300 m | ✅ |
| **Tren en marcha** (bucle en la locomotora) | ahora `sfx_tren_marcha` (1 variante, −15,4) → **nuevo** `sfx_tren_rodando_1..5` (bucle, −22) | `Sfx.LoopAt("tren_"+id, "sfx_tren_rodando_"+(1+id%5), pos, 0.6f*velocidad01, 250f)` | 0,6 × velocidad | 3D | ⏳ provisional |
| **Tren parado en el andén** | `sfx_tren_ralenti_1..6` (−20,0 a −21,4, bucle) | `Sfx.LoopAt("ralenti_"+id, …, 0.3f, 60f)` | 0,3 | 3D | ✅ |
| **Carga y descarga de munición** | `sfx_farp_caja_municion_1..5` (−25,2 a −26,8) | `Sfx.PlayAt("farp_caja_municion", vagon, 0.8f, 0.6f)` por cada unidad que pasa | 0,8 | 3D | ✅ |
| **Carga y descarga de material de vía** | ahora `sfx_muro_construccion` → **nuevo** `sfx_carga_material_1..5` (−24) | `Sfx.PlayAt("carga_material", vagon, 0.8f, 0.8f)` por cada unidad | 0,8 | 3D | ⏳ provisional |
| **Un soldado se queda sin munición** (aprieta y no dispara) | **nuevo** `sfx_sin_municion_clic_1..5` (−28) | `Sfx.PlayAt("sin_municion_clic", soldado, 0.7f, 1.5f)` | 0,7 | 3D, solo cerca (40 m) | ⛔ falta generar |
| **Aviso «sin munición»** (pelotón a 0, o almacén de B vacío) | `sfx_municion_baja_1..5` (−24, normalizados el 11-nov) | `Sfx.Play("municion_baja", Vector3.zero, 0.6f, 10f)` una vez al llegar a 0. Vuelve a poder sonar cuando se rearma | 0,6 | 2D | ✅ |

## Ambiente por nivel de zum (cuanto más lejos, menos detalle)

Son cuatro niveles, los de la lámina de Bruno. Todos son bucles 2D con fundido según la altura de la cámara, sin cortes:

| Nivel | Qué suena | Archivos | Vol. |
|---|---|---|---|
| **Mapa** (todo el terreno) | Solo viento suave. Ni pájaros ni detalle | `sfx_amb_viento_1` (−30,1) | 0,08 |
| **Comarca** | Viento y una huerta lejana y apagada | `sfx_amb_viento_1` 0,06 + `sfx_amb_huerta_1` (−28 a −31) 0,10 | — |
| **Pueblo** | Huerta completa, y la acequia cuando el foco está cerca del cauce | `sfx_amb_huerta_1` 0,25 + `sfx_amb_nules_acequia_1` (−32) en 3D a 60 m | — |
| **Soldado** | Lo mismo que en pueblo, más el caserío infestado en 3D si está cerca | `sfx_amb_huerta_1` 0,3 + `sfx_amb_ciudad_infestada_1` (−28 a −30) en 3D en el caserío, 150 m | — |

Regla: `k = clamp01((altura − h_pueblo) / (h_mapa − h_pueblo))`. Huerta × (1 − k), viento × k. Las alturas de cada nivel las fija la escena de Marcos. Los sonidos de unidades y trenes ya se apagan solos con la distancia (`Sfx.Ear`), así que desde el mapa solo quedan el ambiente y los avisos 2D.

## Lo nuevo (pendiente de créditos)

Script: `herramientas/sonido/hito1_sonido.py`. Pide 6 tomas de cada uno de los 5 sonidos (136 s en total) y se queda con las 5 mejores. Gasta unos **820–1.640 créditos** (tope de 1.800) y no reintenta ninguna llamada. Lo comprobé en seco con archivos de prueba, sin llamar a ElevenLabs. Se lanza en el PC, desde `C:\Dev\mr-mak-workspace`: `python herramientas\sonido\hito1_sonido.py`.

— Nuria (Sonido)
