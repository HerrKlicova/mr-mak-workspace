# Lo que falta para el MVP · partida de 30 minutos jugada por dentro (Lucía, 09-11 09:45)

El MVP está listo cuando la partida de 30 minutos (plan-partida-30min.md) **pasa la corrida A automática de punta a punta sin ningún S1 ni S2 abierto**. Entonces se avisa a Eugenio, que juega la B a mano por la noche con la lista de Sara, y se para (Eugenio, 09:40).

Estado de partida: la qa50 (I-Noche95, solo corrida A) no tiene ningún S1. El tutorial 1–3 y la noche 1 funcionan; el 2.4 ya no se atasca. Faltan T2, T6, T8 y T9, y la corrida manual.

## 1 · I-Noche96: lo que falta del recorrido (por orden)
| # | Qué | Decisión | Dueño |
|---|---|---|---|
| 1 | Arranque con 3 estaciones propias, cada una con su guarnición; Castellón cercada (mancha fija, sin ataque y sin trenes, con sus dos textos) | D-N183, D-N184 | Iker |
| 2 | Atardecer: aviso de horda y mancha que avanza en el mapa | D-N182 | Iker |
| 3 | Día 2: objetivo «Defiende Nules…» con su aviso | D-N179 | Iker |
| 4 | Segundo tren y emboscada: 300 en la vía al oeste de Nules, EM-1 y daño fuera de pantalla | 08:10, 08:20, 09:00 | Nacho (lógica, rama nacho/dn183-castellon) e Iker (disparo y aviso) |
| 5 | Cartel «{Estación} ha caído» con Seguir, Repetir la noche (atardecer.tbd) y Menú principal | 09:25 | Iker |
| 6 | Nules sobre el terreno de Sagunto: cartel «NULES», sin el campanario ni el pueblo | 09:40 | Marcos |
| 7 | Puestos de la guarnición de Nules en ese terreno, distintos de los de Sagunto | 09:40 | Álvaro → Iker |
| 8 | Ambiente: -ambientesuelo 0,5 y -ambientebalasto 1,5, medidos con el balasto en 1, 1,5 y 2,5 | 09:28 | Bruno y Sara |
| 9 | 1.8 visible: que cada paso del tutorial se vea al menos 3 s aunque su condición ya se cumpla | nuevo (S3 de la qa50) | Iker |
| 10 | Tutorial 3.7: «el tren espera en la puerta este» (Sagunto) | 09:42 | Iker (hecho en texto) |

## 2 · QA y entrega
| # | Qué | Dueño |
|---|---|---|
| 11 | qa51 de la I-Noche96: corrida A automática **sin ningún S1 ni S2 abierto**, que la juega Marcos y la informa Sara. La **corrida B, a mano, la juega Eugenio por la noche** con la lista de Sara (T1–T11, con los pasos cronometrados y comprobando que la escena de Nules no es la de Sagunto). Computer use no funciona desde el RC, y Eugenio ya lo tiene activado. | Marcos y Sara (A); Eugenio (B) |
| 12 | Corregir los S1 y S2 que salgan y volver a pasar la qa hasta que quede limpia | según el fallo |
| 13 | Tablón y mensaje a Eugenio con el enlace de la build, cuándo pasó la qa y qué hay provisional (Nules sobre Sagunto, Castellón cercada sin misión) | Lucía y coordinador |

## 3 · Si sobra tiempo (no retrasa la entrega)
- **Día 3 y noche 3** para que la partida pase de los 33 min: «Refuerza Sagunto: manda un pelotón desde Nules antes de la noche» y la noche 3 en Sagunto con una horda mayor que la de la noche 1. Hugo (cifras), Lucía (textos) e Iker (reutiliza el objetivo del día 2).
- **Sonidos que ya existen** para EM-1, «ha caído» y «Repetir la noche». Nuria pasa la tabla a Iker.
- **Diseño de la misión «Romper el cerco de Castellón»** (sin código). Lucía.

## Sigue parado
Todo lo que está en «Se para hasta que esto funcione» del plan, las hordas grandes, un Nules propio (opción B) y recuperar estaciones perdidas.

## Nota de diseño
El capítulo 3 de la build es «Pedir refuerzos»: un tren de Nules a Sagunto durante la noche 1. El plan decía «primer tren a Nules». **Se queda el de la build**, que funciona. El primer tren que manda el jugador es el del día 2, con el objetivo y la emboscada. El plan ya está corregido.
