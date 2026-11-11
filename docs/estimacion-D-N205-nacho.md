# D-N205: estimación de la parte de simulación · Nacho, 11-11 23:00

Sin compilar nada. Leído el código de main 9772c9de.

## 1. Castelló a las 14:18: confirmado con el código

- Es el cerco de la D-N188, de 4400 zombis.
  - Al entrar, `ZoneSpawnPermil` suma `CercoZombies` (NetWorld.cs:1117), así que la zona crea los 4400 (PrototypeBootstrap.cs:253).
  - Night.cs:126 los conserva a propósito: según la D-N188, el cerco se combate en la zona.
- Salen con el reparto de asedio de `SpawnInitialHorde`, que es un bloque de 14 m contra el muro oeste (SimWorldSetup.cs:116).
  - Castelló no tiene muro, así que el campo de flujo los lleva a todos a la fachada del edificio. Eso es la mancha de la captura.
- La D-N184 decía «el cerco es de vista y no ataca», y la D-N188 lo metió en la zona sin darle un comportamiento propio.
- **Arreglo de parche**, por si se sigue con A: `nacho/cerco-anillo` a7cd6f02, SIN COMPILAR.
  - El cerco se reparte en un anillo a 15–35 m alrededor del recinto, por los cuatro lados, y se queda quieto.
  - Solo persigue a la tropa que se le acerque a 25 m, y si la pierde vuelve a su sitio. Nunca va a por la estación.
  - Con el recorte de la B (Castelló sin zona), sobra.

## 2. Qué se puede reutilizar

| Pieza | Se reutiliza | Por qué |
|---|---|---|
| **NetWorld** (red, trenes, almacenes, cerco, guardado, lockstep) | ~90 % | Ya es un mundo único, con tick fijo y enteros, y ya es determinista. Los NH90 ya tienen destino, km, rumbo y segundos que les quedan (Aerodromo.cs), así que su posición en el mapa se calcula sin rehacer nada. **Ver volar el helicóptero es trabajo de vista (Iker), no del núcleo.** |
| **UnitsWorld** (infantería, fuego, LOS, rejilla de paso, vehículos) | ~95 % | Es la misma clase en la zona y en NightSim. |
| **NightGame** (reloj, victoria y derrota, rezagados, daño a estación y tren) | ~90 % | Ya lo comparten los dos mundos. |
| **NightSim** (horda como puntos, tramos, pila, trepada, bot) | ~85 % | Es entero y determinista, con 1421 pruebas, y ya simula las estaciones que no miras. |
| **ECS de la zona** (cuerpos, campo de flujo, pila física) | ~30 % | Se conserva la presentación (render, animación, instancias). Se tira su simulación propia. |

## 3. Cómo lo haría: NightSim como la única simulación

La zona deja de simular y pasa a dibujar lo que diga NightSim. Es lo que pide la B («la zona es la cámara acercada»), y es lo más barato que conozco.

- Se mire o no, el resultado es el mismo por construcción, no por calibración.
- La otra vía, hacer del ECS el mundo único para todas las estaciones, la desaconsejo:
  - El ECS usa float, y Burst no garantiza el mismo resultado en dos máquinas. Eso rompe el lockstep del hito 7.
  - Habría que simular miles de cuerpos en cada estación a la vez.

Tareas de mi parte, en días de trabajo:

| Tarea | Días |
|---|---|
| NightSim también para la estación que miras. Las órdenes del jugador van a su UnitsWorld (el mismo que hoy). | 2–3 |
| Los zombis del ECS como marionetas que siguen las posiciones de NightSim, interpoladas a 60 fps. Se quitan el campo de flujo, la pila física y la trepada como simulación. | 2–3 |
| Pila y trepada visibles a partir del estado de NightSim (pila por tramo, los que suben, las brechas). | 1–2 |
| Vehículos y helicópteros: posición continua en la red y en la zona, desde los datos que ya hay. | 1 (con Iker) |
| Pruebas: goldens nuevos, desincronización y «mirar o no da lo mismo» como prueba automática. | 1–2 |
| **Total de mi parte** | **7–11 días** |

Esto no incluye lo de Marcos (vista de la zona, selección y cámara) ni lo de Iker (mapa, reloj único y vuelo en el mapa). La calibración de NightSim contra la zona se deja: deja de hacer falta.

## 4. Riesgos

- **Se notará en el aspecto.** La pila y la trepada de NightSim son números por tramo. Dibujarlas creíbles (montón, gente subiendo) es trabajo de vista, y al principio se verán peor que la pila física de ahora.
- **Rendimiento.** NightSim mueve 6700 zombis (difícil) sin problema. «Decenas de miles» en una estación habría que medirlo, pero es más barato que con cuerpos.
- **Balance.** Las cifras de Hugo (munición, {m}) están sacadas de la zona. Con un solo mundo hay que rehacerlas una vez con NightSim. Hoy NightSim gasta un 25 % menos que la zona en Nules N2.
- **Unos días sin build jugable nueva**, como dice Lucía.

## 5. Mi opinión

- Estoy de acuerdo con el diagnóstico de Lucía en lo de las dos simulaciones.
- No todo lo de la lista es del núcleo:
  - el cerco y el VAMTAC ya tienen parche;
  - el helicóptero en el mapa sale de NetWorld tal como está.
- Si se elige la B, la haría con NightSim como mundo único, no con un mundo nuevo.

— Nacho (Simulación)
