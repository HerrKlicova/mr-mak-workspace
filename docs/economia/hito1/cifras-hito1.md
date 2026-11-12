# Cifras del Hito 1 y consumos del corte completo · Hugo (Economía), 11-11 23:40 (definitivas 23:56)

> **Cifras definitivas (medidas en NightSim, §4):** 35 cartuchos por soldado · caja de **105** cartuchos (3 cargadores) · B empieza con 1 caja · línea de 4 cajas · puntería 6000 ‰ (acierto ×6) · vuelta del tren ~7,2 min · A con 16 palés · caserío 4 palés. Las tablas de §1 conservan el razonamiento con k supuesto; donde choquen, manda §3–§4.
Encargo: docs/hito1-reparto.md. Plan: docs/plan-nucleo-v2.md (§5 bis). Modelo: `modelo_hito1.py` (enteros, como pide la D-N206). Lo que no está medido va marcado SIN VERIFICAR.

## 0. La cifra que lo decide todo: k (cartuchos por zombi abatido)
Todo el Hito 1 cuelga de **k**, cuántos cartuchos gasta un soldado por zombi abatido. Hoy no está medido para un pelotón a pie contra un caserío. Por eso las cifras van **atadas a k con una regla**, para que, cuando Nacho mida k en NightSim con el pelotón con munición, salgan solas sin rehacer nada.

**Valor de trabajo: k = 5** (SIN VERIFICAR). Razón: con zombis hay que acertar a la cabeza, y en la zona del juego viejo se abatía 1,6–1,9 veces menos por munición que en NightSim (pulido del 19), así que prefiero quedarme alto.

## 1. Cifras del Hito 1
| Cifra | Valor (k = 5) | Regla (para cualquier k) | Por qué |
|---|---|---|---|
| Zombis del caserío | 100 | — | D-N207 |
| Soldados del pelotón | 8 | — | un pelotón |
| **Cartuchos por soldado** | **35** (1 cargador; era 30 con k supuesto, ver §3) | cargador = 100 × k ÷ 16, redondeado a 5 | el pelotón entero (8 × 30 = 240) llega para la **mitad** del caserío |
| **Caja de munición** | **105 cartuchos (3 cargadores de 35)** — cifra definitiva, medida en §4; era 120 | 3 cargadores | unidad de carga del tren y del almacén |
| **Munición inicial en B** | **1 caja (105)** | 1 caja | rearmarse una vez en B lleva al pelotón al **75 %**, y ahí se queda sin la línea |
| Munición inicial en A | 20 cajas | — | no hay producción en el Hito 1 |
| **Capacidad del tren** | **6 plazas** (2 vagones × 3) | — | 1 plaza = 1 caja de munición o 1 palé de material |
| Orden por defecto de la línea | A → B: 4 cajas; B → A: lo que haya de material (2 plazas) | — | la línea lleva munición y trae material en el mismo viaje |
| Velocidad del tren | 40 km/h | — | vía de obra |
| Carga y descarga | 15 s por plaza | — | se ve cargar sin aburrir |
| **Tiempo de la línea** (vía A–B de 1250 m, Álvaro) | ida 112 s a velocidad de crucero; **ciclo 430 s ≈ 7,2 min** en el juego (Iker: aceleración y frenada de 0,9 m/s² y 3 s mínimos por parada; el cálculo sin ellas da 405 s) | ciclo = 2 × vía ÷ velocidad + 15 s × 12 plazas movidas | 1234 m en recta + entradas (docs/hito1/terreno/posiciones_hito1.csv) |
| **Entrega de la línea** | **4 cajas por viaje, un viaje cada 7,2 min reales** (33 cajas por hora real; el texto saca la cifra de la vuelta medida) | 4 cajas por ciclo | en pantalla «por viaje», no «por hora»: con el reloj a ×30 (D-N208) la hora confunde |
| Consumo del pelotón en combate | 120 cartuchos/min = 7200/h | 8 × 15 por minuto | **la línea sostiene el 56 % de un combate continuo** (480 cartuchos cada 7,2 min frente a 120 por minuto): se ve que una línea sola no alimenta un frente en lucha sin pausa |
| **Material del caserío** | **4 palés** | — | 2 viajes de vuelta del tren; 1 palé = 100 m de vía |
| Material inicial en A | **16 palés** | techo(vía ÷ 100 m) + piezas especiales + 2 | 13 de recta + 1 más por el paso a nivel con la carretera vieja (cruce = 2) + 2 de margen; el caserío da 400 m más |
| Distancia B–caserío | 213 m al centro (terreno v2 de Álvaro; antes 237) | — | el modelo usa 200 m: ir y volver, 2 × 143 s andando |
| Tiempo de trazado y línea | ~2 min | — | supuesto del modelo |

### Medida (modelo, 1000 semillas por caso; cada disparo abate con probabilidad 1/k)
| k | Cargador / caja | Sin línea: primer «sin munición» (p10 / p50 / p90 de zombis abatidos) | Sin línea: abatidos al final (p50) | Sin línea: caserío limpio | Con línea: caserío limpio | Con línea: tiempo hasta limpiarlo (p50, B–caserío 150 / 200 m) |
|---|---|---|---|---|---|---|
| 4 | 25 / 100 | 42 / 50 / 58 | 75 | 0,4 % | **100 %** | 12,2 / 10,4 min |
| **5** | **30 / 120** | **40 / 48 / 56** | **72** | **0 %** | **100 %** | 13,1 / 16,0 min |
| 6 | 40 / 160 | 45 / 54 / 62 | 80 | 0,9 % | **100 %** | 10,3 / 12,1 min |

**Lectura:** con la regla, el pelotón se queda seco a mitad del caserío (p50 48–54 de 100), el rearme en B lo lleva a unos tres cuartos y ahí se para; con la línea lo termina siempre. Funciona igual para k de 4 a 6, que es lo que buscaba: la historia no depende de acertar k, solo el tamaño del cargador.
**Límite del modelo:** no simula bajas ni que los zombis se acerquen; el pelotón dispara hasta vaciar. Si en NightSim el pelotón pierde hombres, quedarse seco a mitad pasa a ser peligroso, que me parece bien, pero hay que medirlo.

### Lo que pido a Nacho para cerrar
1. **k**: pelotón de 8 con fusiles contra los 100 del caserío, munición sin límite, 200 semillas: cartuchos gastados ÷ abatidos (p10, p50, p90), y bajas.
2. Con la regla aplicada a ese k: pelotón con 1 cargador y 1 caja en B, sin línea y con un tren que deja 4 cajas en B a los ~4 min. Objetivo: sin línea, caserío limpio ≤ 5 %; con línea, ≥ 95 %.

## 2. Corte completo: consumos de los cuatro recursos (ajustado a la D-N208)
Escala de tiempo (D-N208, provisional): **movimiento, combate, trenes y carga a 1:1**; el reloj de día y noche a ×30 (1 día de juego = 48 min reales: ~28 de día y ~20 de noche; 1 hora de juego = 2 min reales). **La munición y el gasoil se gastan por acción** (disparo, metro recorrido, metro de vía); **las raciones y el desgaste, por día de juego.** No hay consumo «por hora» en reposo de munición ni de gasoil.

| Recurso | Unidad | Quién consume | Por acción | Por día de juego | Notas |
|---|---|---|---|---|---|
| **Munición** | cartucho (caja de 105) | fusilero | 1 por disparo; 15 por minuto real de combate | — | k = 5 cartuchos por zombi (SIN VERIFICAR) |
| | | ametrallador | 60 por minuto real de combate | — | 1 caja = 2 min de fuego |
| | | VAMTAC con ametralladora | 60 por minuto real de combate | — | de la misma caja |
| **Gasoil** | litro (bidón de 20 L) | VAMTAC | 20 L por 100 km recorridos (1 L cada 5 km) | — | depósito 80 L = 400 km |
| | | locomotora diésel | 3 L por km recorrido | — | ciclo A–B del Hito 1 (2,5 km): ~7,5 L |
| | | cuadrilla de vía | 10 L por cada 100 m tendidos | — | la máquina de tender |
| **Raciones** | ración (caja de 24) | soldado u obrero | — | 3 (se cobran al amanecer) | sin raciones: −moral al primer día; deserción desde el tercero (detalle, Lucía) |
| **Desgaste** (sin recurso propio en el MVP) | — | vehículos y vía | — | (Lucía) | si se le pone coste, en palés de material |
| **Material de vía** | palé | tender vía recta | 1 por 100 m | — | |
| | | curva / desvío / topera / cruce | 1,5 por 100 m de curva / 2 / 1 / 2 por pieza | — | |
| | | estación pequeña | 5 | — | |
| | | reparar vía cortada | 1 por cada 50 m dañados | — | |

### Autonomía (lo que el jugador debe ver en cada almacén y unidad)
| Caso | Cuenta | Resultado |
|---|---|---|
| Pelotón con 1 cargador por soldado | 35 ÷ 15 por minuto | 2,3 min reales de fuego, unos 58 zombis (medido) |
| Pelotón con 1 caja de reserva | 105 ÷ 120 por minuto | ~1 min real más |
| 1 caja de raciones | 24 ÷ 3 por soldado y día | 8 soldados un día (48 min reales) |
| Guarnición de 24 con 1 caja de raciones | 24 ÷ 72 al día | un tercio de día: ~16 min reales |
| VAMTAC con el depósito lleno | 80 L ÷ 1 L cada 5 km | 400 km (a 1:1 son horas reales de conducción: el gasoil pesa por distancia, no por tiempo) |
| Línea de 4 cajas cada 7,2 min reales | 33 cajas por hora real | sostiene a 1 pelotón en combate el 56 % del tiempo |
| Raciones de 1 pelotón al día | 8 × 3 = 24 | 1 caja = 1 plaza de tren por pelotón y día: en un tren de 6 plazas, las raciones de 3 pelotones ocupan la mitad de un viaje diario |

**Aviso de unidades en pantalla:** como el reloj va a ×30 y el movimiento a 1:1, «por hora» confunde. Propongo mostrar la munición y la entrega de las líneas **por minuto real** (o «por viaje») y las raciones **por día**. «36 cajas/h» de la línea sería «4 cajas por viaje · un viaje cada 6,7 min» (aprobado por Lucía; con la física del tren de Iker la vuelta es de 7,2 min).

### Reglas de equilibrio que propongo para el corte
1. **Una línea no basta para un frente en combate continuo** (sostiene el 60 % de un pelotón). Obliga a elegir: segunda línea, tren más largo o pausas en el frente.
2. **Las raciones son el reloj lento** (por día de juego, 48 min reales) y la munición el rápido (minutos): se mueven en el mismo tren y compiten por las plazas.
3. **El gasoil es el coste de moverse** (por km), no de luchar ni de esperar: hace que llevar el VAMTAC lejos pese, y que una línea larga gaste.
4. **El material es el recurso del avance**: 1 palé = 100 m. Limpiar un caserío (4 palés) paga 400 m de vía; así el frente avanza al ritmo de lo que limpias.

## 3. Calibración con NightSim (Nacho, 11-11 23:22; rama nacho/hito1 18f1cc7d, 40 semillas)
- Pelotón de B: 4 fusiles, 2 MG ligeras, 2 lanzagranadas. Con munición sin límite: **0 bajas** en 40/40; se abate a 40–43 m de media. Las 8 bajas de la primera medida eran por quedarse seco sin retirarse: **corregido, el pelotón sin munición vuelve solo a B.**
- k según la puntería (UnitsWorld.HitScalePm, solo en Mundo; la noche vieja no se toca): 1000 → 26,6; 4000 → 7,7; 5000 → 6,3; **6000 → 5,4**; 7000 → 4,6. **Propuesta: 6000 para el Hito 1.** Unidad: HitScalePm va en milésimas, así que 6000 = la probabilidad de acierto de la tabla actual del fusil y las MG multiplicada por 6 (1000 = la de antes, sin cambio).
- Sin línea, 35 cartuchos por soldado, puntería 6000: k 4,8; abate ~58 y se queda seco a mitad; se retira en 40/40, aniquilado en 1/40, 8 bajas en total. **Cumple el objetivo de Lucía.**

### Cifras corregidas (sustituyen a las de la §1 donde choquen)
| Cifra | Antes (k = 5 supuesto) | Ahora (k medido) | Motivo |
|---|---|---|---|
| Cartuchos por soldado | 30 | **35** | 100 × 5,4 ÷ 16 = 33,75 → 35 |
| Caja | 120 (4 cargadores) | **105 (3 cargadores)** | con k 4,8 y una caja de 140, el pelotón limpiaba sin línea el 7,6 % de las veces (> 5 %); con 105, el 0,7 % (modelo, 1000 semillas) |
| Munición inicial en B | 1 caja | **1 caja (105)** | lleva al pelotón a ~80 % sin limpiar |
| Línea por defecto | 4 cajas | **4 cajas (420 cartuchos)** | con línea, 100 % limpio en el modelo |
| Combate continuo del pelotón | 120/min | 120/min | la línea entrega 420 cada 7,2 min = 58/min: **sostiene el 49 %** de un combate continuo |
Modelo con k 4,8 y caja 105: sin línea, primer seco p10/p50/p90 = 50/58/67, abatidos p50 80, limpio 0,7 %; con línea, 100 %. Pendiente: la prueba de Nacho con línea (recarga en B y vuelta).

## 4. Medida final (Nacho, 11-11 23:55; nacho/hito1 dd639af8, 100 semillas, puntería 6000 ‰ = acierto ×6, 35 cartuchos, B con 1 caja de 105, recarga en B del almacén de la red)
| | Sin línea | Con línea (4 cajas en B a los 4 min) |
|---|---|---|
| Caserío limpio en 20 min | **0/100** | **96/100** |
| k global | 4,8 | 5,2 |
| Bajas | 0 en total | 1 en total |
| Aniquilado | 0/100 | 0/100 |
| Al acabar | quedan 41,6 zombis de media; el pelotón se retira y espera en B | 0,1 de media; tiempo p50 690 s (11,5 min) |
**Cumple los tres objetivos de Lucía** (sin línea ≤ 5 % y sin morir; con línea ≥ 95 % con 0–2 bajas). Constante en el juego: Mundo.CartuchosPorCaja = 105.

**Remedida con el reloj del guion (Nacho, 12-11 01:49; 100 semillas, corte 24 000 ticks, carga a 5 s por hueco, oleada final de rezagados de la D-N207 ampliada: ≤ 15 zombis van hacia el pelotón):**
| | Sin línea | Con las entregas reales de Marcos | Con la primera entrega a los 8600 ticks |
|---|---|---|---|
| Caserío limpio | **0/100** (41,6 vivos de media) | **100/100** | **99/100** |
| Tiempo (p50) | — | 465 s | — |
| Bajas | 0 | 0 | — |
La lección se mantiene con el reloj real.

## 5. Coste de la vía (12-11 01:05, a pregunta de Sara)
1. **Sin redondeo por tramo.** El material se guarda y se cobra en **metros enteros** (1 palé = 100 m). Recta: sus metros; curva: ×1,5; paso a nivel o cruce: 200 m por pieza; desvío: 200 m; topera: 100 m. En pantalla, palés con un decimal.
2. **Borrar vía devuelve el 100 %** en el Hito 1 (probar trazados sin castigo; el guion de borrar y rehacer no se queda sin material). En el corte completo, menos (por decidir).
3. **Material inicial de A = coste real del trazado A–B + 2 palés**, redondeado arriba. Con 1250 m en recta y el paso a nivel son 14 + 2 = 16; si la curva nueva sube el coste, A sube con él (Iker da el coste real).
4. **Medido por Iker (marcos/mundo-zum dbb03ed8):** recta A–B 14,9 palés (1485 m con curvas a 1,5); guion A → P → B 17,0. **A empieza con 19 palés** (coste del guion + 2). Sobra 2 con el guion y 4,1 con la recta.

## 6. Carga del tren a 5 s por hueco (12-11 01:20, a raíz de las sondas de Marcos)
- Marcos, guion con 19 palés + e97a27be: 88, 89 y 73 abatidos de 100 (k 5,6; la munición cuadra con Nacho). Causa: el reloj. Nacho probó con la primera entrega a los 7200 ticks y 20 min de margen; en el guion llega hacia los 11 000 y la sonda corta a 18 000–24 000.
- **Cambio:** carga y descarga **5 s por hueco (150 ticks)** en vez de 15 s, en A y en B. No toca la lección sin línea (más cajas en B sí la rompían; bajar k obligaba a recalibrar el cargador). Primera entrega hacia los 8600 ticks; vuelta ≈ 5,3 min; la línea sostiene ≈ 66 % de un combate continuo (antes 49 %).
- Pendiente: Nacho, 100 semillas con la entrega real del guion y corte a 24 000 ticks.
