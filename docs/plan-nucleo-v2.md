# Núcleo v2: el juego que describe Eugenio · Lucía (Diseño), 11-11 23:05

Eugenio (22:44): «un mapa enorme explorable donde construyas vías… que las unidades se muevan en tiempo real mandándolas TÚ… líneas automatizadas de trenes… pueblos, ciudades en ruinas con muchos zombis… moverte por todo el mapa viéndolo en detalle… construir carreteras».

## 1. Valoración franca

Esto es otro juego, no una versión arreglada del actual. Hoy la red es fija: tres estaciones unidas por vías que ya existen, un mapa que es un panel y zonas que son escenas aparte. En ese juego no se construye nada y no hay mundo entre estaciones. **La D-N205 (que la zona dibuje lo que simula la red) arreglaba el juego actual, pero no lleva al que quiere Eugenio.** La retiro y la sustituyo por este plan.

Hace falta un núcleo nuevo. No hace falta empezar de cero: buena parte de lo construido sirve como piezas.

## 2. El núcleo que hace falta

1. **Un mundo continuo.** Un único terreno grande, cargado por trozos, con zum continuo desde el mapa hasta el detalle, sin escenas ni pantallas de carga. Es la «escena única» de Marcos, que ahora es obligatoria.
2. **Red construible.** Vías y carreteras trazadas por el jugador sobre el terreno, que forman un grafo por el que circulan trenes y vehículos, con cruces, desvíos y estaciones colocables.
3. **Líneas automáticas.** Una línea es una lista de paradas con qué carga o descarga en cada una; el tren la repite solo. El panel de carga de la D-N200 se convierte en las órdenes de la línea.
4. **Unidades en tiempo real.** Seleccionar y mandar a cualquier punto del mundo, viéndolas moverse siempre. El combate de unidades actual (UnitsWorld) sirve.
5. **Zombis a escala de mundo, con nivel de detalle.** Lejos de la cámara, densidad por casilla (barato, como NightSim). Cerca, individuos con cuerpo. Una sola simulación con dos niveles de detalle, para que el resultado no dependa de si se mira o no.

## 3. Qué se aprovecha y qué no

| Se aprovecha | No se aprovecha |
|---|---|
| Arte: estaciones, edificios, unidades, vehículos, trenes, muros. | La red fija de tres estaciones y sus distancias. |
| El combate y movimiento de unidades (UnitsWorld, línea de visión, rejilla de paso). | El mapa como panel. |
| La horda como densidad y el bot de NightSim, como nivel de detalle lejano. | Las zonas como escenas cargadas al entrar. |
| La economía de NetWorld (almacenes, munición, carga) como reglas. | Las cifras de equilibrio de Hugo, que hay que rehacer. |
| Interfaz v3, sonido, tutorial (como guion) y Sagunto como nivel de referencia. | El lockstep, si el juego es de un jugador (decisión de Eugenio, abajo). |

## 4. Lo que nos hace originales

El género y las mecánicas de construir vías y montar líneas son de todos. Nada se copia de Transport Fever: ni interfaz, ni nombres, ni aspecto. Nuestro gancho es otro:

- **Construir vía es avanzar el frente.** Las cuadrillas que tienden vía necesitan escolta; cada kilómetro se gana a los zombis.
- **Las ciudades en ruinas son a la vez botín y peligro.** Limpiarlas da recursos y nuevas estaciones.
- **La noche ataca la red.** Una vía cortada o un tren detenido en mitad de una horda es el drama del juego. La defensa de Sagunto que ya tenemos encaja como el asedio de una estación.

## 4 bis. Dos géneros en un solo bucle (Eugenio, 22:45)

Eugenio pide una gestión de recursos militares seria y entretenida, una gestión de transportes también entretenida y que los dos géneros se mezclen. La regla de diseño es que **ninguno de los dos funciona sin el otro**:

- **El ejército consume.** Munición, combustible, raciones y repuestos se gastan al combatir, al moverse y con el paso del tiempo. Un pelotón sin munición no dispara, un VAMTAC sin gasoil se queda parado y una guarnición sin raciones pierde moral y acaba desertando.
- **El transporte abastece.** Esos recursos solo llegan donde llega una vía o una carretera y una línea que los lleve. La capacidad, la frecuencia y el tiempo de viaje deciden cuánto frente puedes mantener.
- **El ejército abre camino al transporte.** Tender vía exige limpiar y escoltar el tramo, y una vía sin guardia la cortan los zombis de noche.
- **El transporte hace crecer al ejército.** Las ciudades limpiadas dan supervivientes (nuevos soldados y obreros), chatarra (material de vía) y depósitos (munición y gasoil), pero solo si alguien se los lleva a la base.

La parte seria está en las cuentas: cada unidad tiene un consumo visible por hora y en combate, cada almacén muestra para cuánto tiempo le llega lo que tiene, y una línea muestra cuántas unidades por hora entrega. La parte entretenida está en las decisiones: adelantar el frente o reforzar lo que ya tienes, una línea rápida de munición o una lenta de material, arriesgar un tren por una zona sin limpiar.

Recursos del MVP, solo cuatro: **munición, gasoil, raciones y material de vía**, además de los soldados como recurso humano.

## 5. MVP que lo demuestra (corte vertical)

Un trozo de costa de unos 8 × 8 km (tamaño SIN VERIFICAR, lo fija Marcos según rendimiento), con Sagunto ya defendido y un pueblo en ruinas lleno de zombis.

1. Moverse por todo el trozo con zum continuo desde el mapa hasta ver un soldado.
2. Trazar una vía desde Sagunto hasta una estación nueva, con una cuadrilla que hay que escoltar.
3. Crear una línea de dos paradas que lleve munición y se repita sola.
4. Trazar una carretera y llevar por ella un VAMTAC que no cabe en el tren.
5. Mandar tropa a mano, en tiempo real, a limpiar el pueblo.
6. Una noche en la que la horda ataca la línea.

Queda congelado todo lo demás: Castelló, el socorro, el cerco, el NH90, y el pulido del 19 salvo arte y sonido.

**Prueba de que está hecho:** alguien del equipo hace los seis pasos seguidos con ventana, y después Eugenio.

## 5 bis. Primer hito jugable, pequeño y concreto (Hito 1)

Antes del corte completo, una prueba de que el núcleo nuevo funciona:

- Un terreno de 2 × 2 km en una sola escena, con zum continuo del mapa al soldado.
- Dos estaciones ya colocadas. El jugador traza la vía entre ellas con el ratón.
- Una línea de dos paradas: un tren va, carga, vuelve y descarga solo, en bucle.
- Un pelotón que se manda a mano a cualquier punto y se ve andar.
- Un grupo de zombis (cien o así) en un caserío que reacciona al pelotón.
- **El cruce de los dos géneros, ya en el Hito 1.** Cada soldado del pelotón lleva 60 cartuchos y el puesto avanzado (la estación B) empieza con poca munición (cifras SIN VERIFICAR, para Hugo). Sin la línea, el pelotón se queda seco a mitad del caserío; con la línea llevando munición de A a B, se rearma en B y termina el trabajo. Limpiar el caserío deja un depósito de material de vía que hay que traer a A con el mismo tren.
- En pantalla: la munición de cada soldado, lo que tiene cada almacén y lo que entrega la línea por hora.

Sin noche, sin gasoil, sin raciones y sin carreteras todavía. Eso llega en el corte completo. **Está hecho** cuando alguien del equipo lo juega con ventana durante diez minutos sin nada raro. Es lo primero que vería Eugenio.

## 6. Plazos

No prometo horas. Las estimaciones que hay (Iker 10–15 días, Marcos 8–23, Nacho 7–11) eran para la D-N205 y no sirven para esto. Iker, Marcos y Nacho tienen que volver a estimar contra el corte del punto 5. Mi impresión, SIN VERIFICAR, es que hablamos de semanas y no de días.

Los NH90 visibles en el mapa (1–2 días de Iker) serían trabajo para el mapa actual, que se va a tirar. Recomiendo no hacerlos.

## 7. Decisión que es de Eugenio

**¿Un jugador o multijugador?** El lockstep (todo en enteros, mismo resultado en dos máquinas) es lo que hoy impide usar el motor de Unity como mundo único y encarece todo. Si el juego es de un jugador, se puede quitar y el núcleo nuevo sale bastante más barato. Recomiendo un jugador.
