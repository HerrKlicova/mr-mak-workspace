# Plantillas de pueblo y de ciudad en ruinas (Álvaro, Niveles, 11-nov ~23:40)

Son para el corte completo del núcleo v2 (plan-nucleo-v2.md §4 y §5), después del Hito 1. Cada plantilla es un asentamiento en **coordenadas locales**, en metros, con el origen en el centro (X este, Z norte). Se coloca en el mundo con un desplazamiento y un giro de 0, 90, 180 o 270°. Hay **5 variantes** de cada una (semillas 1 a 5), todas del mismo generador determinista: `docs/niveles/herramientas/plantillas_hito1.py`, que se ejecuta con `python3 -I plantillas_hito1.py <carpeta>`.

| | Pueblo de la huerta | Ciudad en ruinas |
|---|---|---|
| Tamaño | 260 × 220 m | 640 × 640 m |
| Trazado | Retícula irregular (±4 m) de manzanas cerradas de ~45 × 38 m. Casas entre medianeras de 5–8 m de frente, 9–13 m de fondo y 1–3 plantas. Calle mayor y calle de cruce de 8 m; las demás, de 5 m. Plaza con iglesia y campanario | Ensanche de 5 × 5 manzanas de ~115 m con chaflanes de 10 m. Bloques de 5–8 plantas, de 12–22 m de frente y 14–20 m de fondo. Calles de 13 m y una gran vía de 30 m. Algún parque |
| Edificios | 339–411 | 304–363 |
| Estado | 35 % sano, 35 % dañado, 22 % ruina y 8 % derrumbado | 10 % sano, 35 % dañado, 40 % ruina y 15 % derrumbado (deja un escombro de 2 m que tapa el paso en la calle) |
| Botín (5 por variante) | Cooperativa (material), farmacia y almacén (raciones), ayuntamiento (munición) y gasolinera (gasoil, fuera del casco junto a la entrada oeste) | Hospital y mercado (raciones), cuartel (munición), almacenes (material) y cocheras (gasoil), cada uno en una manzana entera |
| Zombis | 436–515, en grupos por edificio (el triple en la iglesia y el ayuntamiento) | 4945–6054, en grupos por bloque según su superficie y plantas (el doble en el hospital, el mercado y el cuartel) |
| Además | Solares y huertos abiertos (8 %) | 60 coches abandonados en las calles; escombros delante de los derrumbados |

Los edificios con botín nunca salen derrumbados, porque el botín tiene que poder sacarse.

## Archivos (`docs/hito1/plantillas/`)

Para cada `<tipo>_v<n>`:
- `_edificios.csv`: cajas con el **mismo esquema que `sagunto_obstaculos_v1.csv`** (mm, locales). La altura depende del estado (plantas × 3,2 m + 0,4; ruina al 60 %; derrumbado 2 m), así que `NightSim.LosSceneFromCsv` lo lee para la línea de visión. La nota dice el uso, las plantas y el estado, para escoger el modelo (las casas en ruinas de Teo).
- `_calles.csv`: ejes de las calles, con su ancho.
- `_puntos.csv`: grupos de zombis (valor = número), botín, plaza, solares, parques, escombros y coches (valor = yaw).
- `.png`: el plano. Los edificios van de claro (sano) a negro (derrumbado), y el botín se marca con un cuadro azul.
- `plantillas_hito1.json`: resumen de las 10 variantes.

## Pendiente y SIN VERIFICAR
- Las cifras de zombis son para el nivel de detalle lejano (densidad). Las calibran Nacho y Hugo.
- Los edificios singulares de la ciudad son una caja por manzana. El hospital o el cuartel de verdad necesitarán su propia planta (patio, alas).
- No hay relieve propio: la plantilla se asienta sobre una explanada del terreno, como el caserío del Hito 1.
- Lo original es nuestro: el trazado sale de la huerta y del ensanche valencianos, no de ningún juego.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
