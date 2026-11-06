# Relevo · Hugo (Economía y balance)

Última actualización: 6-nov-2026, 17:15 (Madrid). Quien lea esto es el nuevo Hugo. Continúa desde aquí y desde los archivos enlazados, y no des nada por sabido fuera de ellos.

## 1. Quién eres y cómo trabajas

- **Hugo**, 51 años, ex de Renfe (logística ferroviaria). Metódico y escéptico: discutes con datos, mides antes de opinar y, si te equivocas, lo dices («confesión de método»). Siempre en español.
- **Firma** en cada mensaje: «— Hugo (Economía) · [retrato](/mnt/project-files/equipo/retrato_hugo_64_x4.png)».
- **Mak** (el coordinador) es el director y decide las dudas. **Eugenio** es el dueño del juego. Su regla: «a todas mis preguntas respondo lo que tú recomiendas», así que aplicas la recomendación y avisas, salvo pagos, credenciales o acciones irreversibles. No escribes código de Unity.
- **Con quién hablas**: Lucía (diseño) y Nacho (simulación en C#), por mensaje a su hilo. Hoy Mak suele pedir que a Nacho le contestes directamente. **Marcos (Unity) no recibe mensajes de hilos**: todo para él va por Mak (message_coordinator). Cuando Mak te pregunta algo, le contestas a él.
- **Registro**: todo lo que decides va a `docs/decisiones-noche.md`. **Solo se añade al final, nunca se reescribe.** Si te equivocas de número, añades una nota de corrección (como D-N63).
- **Ciclo de un cambio de balance**: cambias el `PARAM` de `sim_economia.py`, mides con 1000 partidas, regeneras los CSV (`python3 generar_csv.py`) y los casos (`python3 casos_prueba.py`), anotas la decisión con el porqué y la cifra medida, y avisas a quien lo integra.

## 2. Archivos (en `/mnt/project-files/docs/economia/`)

| Archivo | Para qué |
|---|---|
| `sim_economia.py` | El modelo Monte Carlo. **`PARAM` es la fuente de verdad.** Políticas: tortuga, equilibrada y prisa. `python3 sim_economia.py --csv series > resultados.txt` (unos 16 s con 300 partidas). Para medir variantes: `S.monte_carlo(1000, P, pols=['equilibrada','prisa'])` sobre una copia de `PARAM` (unos 40 s). |
| `generar_csv.py` → `csv/` | Los CSV que lee Unity: separados por «;», todo entero y milésimas con floor. Las filas nuevas se añaden **aquí**, no a mano en el CSV, porque al regenerar se pisan. Las descripciones cambian «;» por «,». |
| `casos_prueba.py` → `csv/casos_prueba.csv` | Los casos P1 a P10 en aritmética entera, para el lockstep. |
| `csv/referencia_*.csv` | Validación contra Unity: asedios de los días 1–20, masa en el campo y total por huella. |
| `resultados.txt`, `series/` | La última ejecución con 300 partidas y una partida de ejemplo por política. |
| `economia-balance.md` | El documento v1. **Está desfasado en números**: manda `PARAM`. |
| Repo del juego (solo lectura) | Clon en `/home/claude/herrklicova/tbd`. Los PR de Nacho se revisan con `git fetch origin pull/N/head:prN`. |

## 3. Números vigentes (Normal)

- **Colmena**: H = H0·(1+d/20)^α·√(1+k·huella), con H0 1550, α 1,55 y k 0,24. Rampa 0,15/0,35/0,65/0,85; primer asedio el día de índice 1. Interdicción máxima del 37 %.
- **Resultado con 1000 partidas**: equilibrado **13,2–13,8 %** de derrotas (el umbral de Lucía es el 14 %, así que **no hay holgura**), prisa 42–43 % y escasez 55 %. Zaragoza llega el día 14 y Teruel, el día 3. Si la demo resulta dura, la primera palanca es **H0 1500**. k 0,23 no sirve: baja la prisa, pero el equilibrado sube al 13,3 % con 300 partidas.
- **Director (D-N33, D-N34, D-N37)**: presupuesto = curva × 1,36; el 600 ‰ va a asedios. Los asedios duran 2 días, con 12 h de hueco. El objetivo se sortea con probabilidad ∝ peso². El asedio va en un canal aparte de la emboscada y el corte.
- **Combate (D-N27)**: sin muros, tope de 54 abatidos por tirador y 0,014 bajas por zombi en contacto. El tren parado cuenta como muro. 1 u de munición = 400 zombis.
- **Trenes**: 5 vagones de carga × 20 u, más **1 vagón de pasajeros de 40 plazas aparte** (D-N64: quitar uno de carga sube el equilibrado al 34,5 %). Tren nuevo: 120 u + 30 de combustible, 3 días. Tren 3: 60 + 15, 36 h, y toma la tripulación de 10. Tren de obras: 20 + 5, 36 h; sus 8 obreros son su tripulación y se descuentan **al salir** del taller. Cancelar un tren sin empezar devuelve el 100 %; empezado, floor(50 % de lo cobrado). El taller trabaja 24 h.
- **Obras (D-N44, D-N45, D-N59)**: nivel S0 = valor defensivo ÷ 30 u, con máximo de 5. Sacos 2 u y HESCO 6 u por cada 10 m. Horario de obra de 06:00 a 18:00. Puente: 192 obrero·h. El sondeo solo sale cuando la obra trabaja; el peso ×1,5 y la huella cuentan mientras está en curso, también de noche. Mantenimiento: el 1 % exacto del valor al día.
- **Sagunto (D-N63)**: empieza con **120 u ya construidas** (nivel 4) en un recinto de 86 × 41 m. Lleva HESCO en el frente oeste y las alas, sacos en el resto y 2 puertas de vía (la del este, bloqueada). El andén va centrado. Sin ese muro, la prisa llega al 50 %.
- **Automatismos del H6 (D-N66)**: el viaje manual **no puede costar horas-tren** (1 h de espera por tren y día en la etapa 1 retrasa Teruel un día y sube el equilibrado al 16 %). Lucía lo resolvió con «Salir» armable en cualquier momento y con carga durante la espera. Mínimos de serie en Sagunto: munición 40, víveres 30, combustible 25, sin máximo.

## 4. Pendiente

1. **Mantenimiento en el PR #21 (Nacho)**: `MaintenanceU` redondea hacia arriba (2 u al día en Sagunto). Pedí un remanente en E4 por nodo para pagar el 1 % exacto (adenda de D-N63). Comprueba que se aplica.
2. **P10 (Marcos)**: la anchura del frente de la pila en la zona (muro de 1,2/2,1 m), y luego la fila `pila_frente_efectivo_m`.
3. **Medir Fácil (k 0,18) y Veterano (k 0,33)** con 1000 partidas.
4. **Prueba de Eugenio**: vigilar el hambre y la dureza; la primera palanca es H0 1500. Sara mide las horas paradas por tren en la etapa 1 (objetivo ≤ 0,5 h).
5. **Fuera del MVP**: medir la locomotora pesada (nunca más eficiente en combustible por u·km) y la rampa de Barracas cuando existan.

## 5. Trampas conocidas

- **300 partidas frente a 1000**: con 300, el equilibrado salía al 11,7 % y era en realidad un 13,2–13,8 %. El error típico con 300 es de ~1,9 puntos; con 1000, de ~1,1. **Mide siempre con 1000** y compara las variantes con las mismas semillas.
- **Choques de numeración D-N**: ha pasado cinco veces. Busca el último con `grep -o "D-N[0-9]*" decisiones-noche.md | sort -n` (también los encabezados `###`, no solo los `##`) justo antes de escribir, y vuelve a mirar unos 10 s después.
- **Unidades con Sara y Unity**: los recuentos de Sara van en grupos de 10 (curva ÷ 10), y su «día 1» es mi índice 0.
- **El modelo va por días y no transporta personas** (`tomar()` es instantáneo). Lo que dependa de horas o de plazas no sale de él sin un parche. Lo que dependa de horas-tren es muy sensible (Teruel).
- **El tren visual (64 m, locomotora y dos vagones) no es el tren del modelo** (5 vagones de carga): es una abstracción y no hay que cuadrarlos.
- **La carpeta compartida tarda**: vuelve a leer tras escribir. Haz copias de seguridad en el scratchpad antes de tocar `PARAM`.
- **No inventes**: si un número no está medido, dilo o mídelo. Una «palanca» sin medir ya te tocó corregirla (k 0,23).
