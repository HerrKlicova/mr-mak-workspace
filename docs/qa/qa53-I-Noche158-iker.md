# QA53 · I-Noche158 (Iker, 11-nov)

Build: `I-Noche158` desde `main` de TBD en 30b2ecd1 (rama iker/f1-aire, fusionada a main).
Tests dotnet: 1406 correctas, 0 fallos (I-Noche157; 158 solo añade código de vista).
Capturas: `docs/capturas/qa53/I-Noche158/` (9).

No encontré `docs/qa/qa53-I-Noche152.md` de Sara en ningún repo; los 7 puntos son los del encargo.

| # | Punto | Resultado | Cómo se comprobó |
|---|---|---|---|
| 1 | Integrar marcos/muro-y-vision | PASA | Fusión limpia; la línea de visión de VehicleFire revisada (usa UnitsWorld.LineOfSight con los sólidos de LosInit; 12 pruebas como máximo). Test I-Noche153 del pelotón dentro del recinto: ok. |
| 2 | Línea de visión en las noches iniciales | PASA (Sagunto) / SIN DATOS (Nules) | Log: «línea de visión de Sagunto: 35 sólidos». Nules no tiene inventario (`nules_obstaculos_v1.csv` no existe): va sin regla hasta que Álvaro lo haga. |
| 3 | Siluetas de vehículos | PASA | Ahora Dragón 3,0 × 8,0 y VAMTAC 2,2 × 5,0. La caja de mallas sigue saliendo grande aunque se quiten sombras y anillo (4,3 × 10,8 y 3,1 × 8,5), así que se usan las medidas a mano; la caja medida solo se acepta si no pasa del 110 %. |
| 4 | Build y tests | PASA | I-Noche157 y 158 compilan sin errores; escenas sin cambios. |
| 5 | Tutorial entero + mapa y vuelta | PASA | Tutorial completo (28 pasos hasta «terminado»). La corrida automática antes forzaba «ataque rechazado» a los 3 s; ahora espera la señal real: 1.9 se cierra por tiempo y 1.10 no sale mientras quedan zombis (2 corridas). Salida al mapa y vuelta: «noche de Sagunto: la suya, reanudada», muro al 999 ‰, 113 tramos, 31 obras; no empieza horda nueva. |
| 6 | Sin tutorial, mapa a 40, 150 y 300 km | PASA (fallo arreglado en I-Noche159) | Capturas 01–04. Las etiquetas de nodos y trenes no se pisan a ningún zoom (a 300 km se agrupan en «Sagunto +1»). Fallo: el aviso rojo «Hay un tren parado en Nules…» queda tapado por la barra «Sagunto en combate» (se corta en «…de la noche»). |
| 7 | Zombis persiguiendo vehículos y soldados sin disparar a través de edificios | NO VERIFICADO | Con -vehdemo el VAMTAC 1 recibe la orden de salir al oeste pero no se mueve (vel 0 en 1.814 líneas): la puerta de vehículos E4 está cerrada con muro al empezar («puerta PuertaVeh cerrada con muro»), y el A* no encuentra salida. Sin vehículos fuera no hay persecución que capturar. Lo de los edificios está cubierto por código y tests (D-N174), no por captura. |

## Otros hallazgos

- Reloj: la hora de la zona y la de la red no coinciden (zona 02:41, red 19:24; zona 08:05, red 15:07). Además, con el tutorial, la hora de la zona se queda parada (00:07 en una corrida, 02:30 en otra) mientras la horda sigue. Puede ser cosa del capítulo 3; lo tiene que mirar Nacho.
- Al volver a la zona, a las 22:00 de la red sale «empieza la noche de Sagunto» y justo después «resultado=victoria». No empieza otra horda (correcto), pero los dos mensajes juntos confunden.
- Muchísimo aviso «CollisionMeshData couldn't be created… UCX_PilaZombi_*» (unas 25.000 líneas por corrida): las mallas de colisión de la pila no son legibles. Ensucia el log y puede costar rendimiento (Bruno o Teo: marcar Read/Write o quitar los UCX).

## Herramientas nuevas (QA)

- `-mapa-capturas 40,150,300`: al entrar en el mapa saca una captura a cada distancia (Captures/qa/mapa_<km>km_<n>.png).
- `-tutorial-auto` ya no fuerza horda_avanza ni ataque_rechazado (espera hasta 600 s a la señal de la zona).

## I-Noche159 (main en el commit del aviso)
- El aviso «Hay un tren parado en Nules…» se parte en dos líneas dentro del panel y la barra «Sagunto en combate» ya no pisa el panel de la izquierda (captura 10).

## Repaso con la especificación de Sara (qa53-I-Noche152.md, que en realidad es la de I-Noche153)
Lo de arriba son corridas automáticas (-menu-auto, -tutorial-auto); la qa53 de Sara la corre Marcos a mano a 1920×1080 sin -menu-auto. Lo que ya adelantan estas corridas:
- Punto 2 (salir y volver): Sagunto con tutorial y sin él, muros y noche iguales al volver. Faltan Nules y Castellón, los daños, la posición de la tropa y los sacos con capturas en el mismo encuadre.
- Punto 3 (la noche del tutorial trae zombis): ✅ `oleada=1 hora=22:00 total=5250`.
- Punto 6 (VAMTAC al otro lado del muro oeste): se para y nunca se queda atravesado, pero no sale porque E4 está cerrada con muro (pregunta a Eugenio en curso).
- `desync_red=False` en todas las corridas y ninguna línea «Red: desincronización».
- Puntos 1, 4, 5 y 7: no los cubren estas corridas.
