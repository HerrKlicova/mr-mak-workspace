# Valoración franca del núcleo · Lucía (Diseño), 11-11 22:50

Eugenio (22:39 y 22:40): «hay miles de zombis en Castelló», «quiero ver el helicóptero moverse hacia Nules en tiempo real», «está mal hecho el núcleo del juego desde el principio».

## Respuesta corta

**Eugenio tiene razón en lo importante.** El núcleo está mal planteado desde el principio. No hay que tirar el juego, pero sí hay que rehacer el núcleo. Parchear lo que tenemos no basta.

El fallo de base es este: hicimos primero la zona (un juego táctico con su propia simulación) y después le pegamos encima una red de estaciones con **otra simulación distinta** (NightSim), además de un mapa que no es un mundo, sino un panel. El resultado:

- Lo que pasa depende de si lo miras o no. La misma noche gasta casi el doble de munición en pantalla que fuera de ella.
- Las unidades que salen de una zona dejan de existir como cosas que se ven. Por eso el helicóptero no vuela por el mapa: no hay ningún sitio donde dibujarlo.
- Cada zona es una escena aparte que se recrea al entrar. Por eso aparecen cosas que no deberían estar, como la horda de Castelló a las 14:18 o el tren equivocado.

Todo eso viola la regla que nosotros mismos escribimos en la D-N186 (persistencia, tiempo real y una sola simulación). Llevamos días calibrando una simulación contra la otra, y eso es tratar el síntoma.

## Lo que hoy no tiene sentido para un jugador

1. **Castelló de día, a las 14:18, con miles de zombis** pegados a la estación sin atacar (captura de Eugenio). Es la horda del cerco dibujada en la zona, cuando debería ser solo una amenaza en el mapa.
2. **El helicóptero o el tren que mandas a Nules desaparece.** No se mueve por el mapa ni se ve llegar.
3. **Dos trenes en Sagunto** sin que se entienda cuál es cuál ni para qué sirve cada uno.
4. **Cumples el objetivo y no pasa nada.** El cartel de la D-N204 es un parche.
5. **La hora de la zona y la de la red no coinciden.**
6. **El mismo combate da otro resultado según lo mires o no.**
7. Fallos menores: la formación se parte en el muro, el VAMTAC se frena. Se arreglan, pero no son el problema.

## Las dos opciones

| | A) Arreglar sobre lo que hay | B) Rehacer el núcleo y conservar el resto |
|---|---|---|
| Qué es | Congelar novedades, calibrar NightSim contra la zona, añadir un vuelo animado en el mapa y parchear las entradas a las zonas. | Un solo mundo simulado donde cada unidad tiene una posición y se mueve en tiempo real. La zona es la cámara acercada a ese mundo, no una escena aparte. **Corrección tras Nacho: el mundo único es NightSim y NetWorld (enteros, deterministas, ya simulan lo que no miras); la zona deja de simular y solo dibuja.** |
| Qué se reutiliza | Todo. | Arte, modelos, estaciones y niveles, unidades y su combate, interfaz v3, tutorial, sonido y lockstep. Calculo que la mayor parte del trabajo hecho (SIN VERIFICAR: lo tienen que estimar Iker, Nacho y Marcos). |
| Qué se tira | Nada. | La simulación propia de la zona (cuerpos, campo de flujo y pila física), el mapa como panel y la carga y descarga de zonas como escenas. |
| Riesgo | Seguiremos encontrando «cosas sin sentido», porque cada parche tapa una diferencia entre dos mundos. | Durante unos días no hay build jugable nueva. La actual se queda como referencia. |

**Recomiendo la B**: rehacer el núcleo, no el juego. Empezar de cero del todo tiraría lo que sí funciona (Sagunto, el tutorial, el combate en la zona, el arte), y eso no lo veo justificado.

## Recorte del MVP (si se aprueba la B)

- **Solo Sagunto y Nules jugables.** Castelló, solo como marcador en el mapa, sin zona.
- **Un helicóptero y un tren** que se ven moverse por el mapa en tiempo real, salir de una estación y llegar a la otra.
- **Una noche completa** en una zona, con el mismo resultado se mire o no.
- Un único reloj.
- **Congeladas todas las mecánicas nuevas** (socorro, panel de carga, cerco) hasta que esto funcione.
- El reparto de pulido del 19 queda suspendido salvo arte y sonido, que no dependen del núcleo.
- Prueba de que está hecho: Eugenio manda el helicóptero a Nules y lo ve volar y llegar, sin nada que no tenga sentido. La juega antes alguien del equipo, con ventana.

Plazos: no prometo horas (norma de Eugenio). Iker, Nacho y Marcos tienen que estimarlo antes de empezar.

Queda registrado como propuesta **D-N205**, pendiente del sí de Eugenio.

## Corrección (22:55), tras la estimación de Nacho

Me equivoqué al escribir que NightSim desaparecía. Es al revés. Nacho lo ha leído en el código de main 9772c9de: NightSim y NetWorld son enteros y deterministas, y ya simulan todas las estaciones. Lo que se tira es la simulación propia de la zona, que usa float y rompería el lockstep. La zona pasa a dibujar lo que diga NightSim, y así el resultado es el mismo se mire o no por construcción, no por calibración. Detalle en [estimacion-D-N205-nacho.md](estimacion-D-N205-nacho.md).

- **La parte de Nacho cuesta de 7 a 11 días.** Faltan las estimaciones de Marcos (vista de la zona) y de Iker (mapa y reloj único).
- **Reutilizable:** NetWorld ~90 %, UnitsWorld ~95 %, NightGame ~90 %, NightSim ~85 %. Del ECS de la zona solo se conserva la presentación (~30 %).
- **Castelló, confirmado:** es el cerco de 4400 de la D-N188, metido en la zona sin un comportamiento de cerco (NetWorld.cs:1117, Night.cs:126). Hay un parche, nacho/cerco-anillo a7cd6f02, sin compilar; con el recorte de la B sobra.
- **El helicóptero volando en el mapa no depende del núcleo.** NetWorld ya tiene destino, rumbo y tiempo restante de cada NH90, así que es trabajo de vista de Iker y se puede hacer ya, elija Eugenio A o B.
- **Riesgo:** al principio la pila y la trepada se verán peor (son números por tramo), y las cifras de Hugo habrá que rehacerlas una vez con NightSim.
