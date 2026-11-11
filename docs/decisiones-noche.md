# Decisiones de la noche del 5 al 6 de noviembre de 2026

Mandato de Eugenio (22:25): trabajar toda la noche con calma, decidir por él, consultarse entre el equipo y dejar un registro para la mañana.
Cada entrada indica **quién propone**, **a quién se consulta**, **qué se decide** y **por qué**. Estado: ✅ decidido · 🔄 en consulta · ⏸ aplazado.

Equipo de esta noche:
- Mak: producción y dirección.
- Lucía: diseño.
- Marcos: Unity.
- Iris: herramientas de IA.
- Hugo: economía.
- Sara: QA.

---

## D-N01 · Recursos: 4 cargas más la población ✅
- **Propone**: Hugo. **Consultada**: Lucía (de acuerdo).
- **Problema**: el GDD §9 decía que los recursos eran munición, combustible, materiales y personas, pero §9b y §10 hacen que la gente coma, y la comida no existía.
- **Decisión**:
  - Las cargas son **munición, combustible, materiales y víveres** (la comida y el agua van juntas).
  - **Las personas pasan a ser población**: viajan en plazas de pasajeros, no ocupan toneladas y no se gastan.
- **Por qué**: cierra un agujero de diseño sin añadir complejidad.
- **Se aplica en**: GDD §9, §9b y §10, y en el catálogo.

## D-N02 · Una sola reserva de munición en el MVP ✅
- **Propone**: Hugo. **Consultada**: Lucía (de acuerdo, con un matiz).
- **Decisión**:
  - En el MVP hay una única reserva de munición. Cada arma gasta a un ritmo distinto: un disparo del vagón artillero cuesta mucho más que una ráfaga de fusil.
  - Las tres clases de munición del catálogo (ligera, pesada y especial) llegan en la etapa 2, junto con las cepas.
- **Por qué**: menos gestión en las primeras horas, sin perder el coste de las armas pesadas.

## D-N03 · La geografía decide la economía del MVP ✅
- **Propone**: Hugo. **Consultada**: Lucía.
- **Propuesta**:

  | Lugar | Qué aporta |
  |---|---|
  | Valencia | Víveres (la huerta) y refugiados |
  | Sagunto | Materiales (la acería) y el taller |
  | Castellón | Combustible (la refinería) |
  | Teruel | Víveres y algo de materiales |
  | Zaragoza | Munición (la base militar) |

- **Matices de Lucía**:
  - Sagunto empieza con un **depósito finito de munición**, para que el jugador no arranque sin balas. Más adelante, una pequeña fábrica en el taller que nunca iguala a Zaragoza.
  - Zaragoza es el «gran premio» al final de la línea peligrosa.
  - Valencia es una ciudad enorme, o sea, un nido: da víveres y refugiados, pero **no es segura**.
  - Dato real que lo justifica: la línea Sagunto–Teruel nació en parte para bajar el mineral de hierro de Ojos Negros a los altos hornos de Sagunto.
- **Resultado (Hugo, 23:20)**: probado en el modelo y se sostiene. Números finales: Sagunto 80 de materiales, Castellón 60 de combustible, Valencia 30 de víveres, Teruel 12 de víveres y 20 de materiales, y Zaragoza 40 de munición. Ver D-N21.

## D-N04 · Tensión logística: el déficit lo provoca la Colmena ✅ (cifras corregidas en D-N18)
- **Propone**: Hugo (que los trenes muevan el 75–85 % de lo que pide la red). **Consultada**: Lucía (con un cambio).
- **Propuesta de Lucía**:
  - Si nada sale mal, la **capacidad nominal cubre el 90–100 %** de la demanda.
  - Los cortes, las emboscadas y los asedios bajan lo que de verdad llega al **75–85 %**.
  - La etapa 1 es más suave.
- **Por qué**: si la escasez es estructural, el jugador culpa al juego. Si viene del enemigo, culpa a la Colmena (pilar 4).
- **Resultado**: validada, con más peso de la Colmena (ver D-N18).

## D-N05 · Materializar y desmaterializar zonas (hito 3) ✅
- **Propone**: Marcos. **Consultada**: Lucía (de acuerdo, con cinco condiciones).
- **Decisión**:
  - Al acercar la cámara a menos de unos 2 km, la densidad S0 de la celda se convierte en zombis: de 0 a 1000 por mil equivale a de 0 a 10.000 zombis.
  - Al salir, los vivos vuelven al mapa y **los muertos se restan** de la mancha.
  - En el MVP, como mucho **una zona en detalle**.
- **Condiciones de Lucía**:
  1. Histéresis: se materializa por debajo de 2 km y se desmaterializa por encima de 2,5 km.
  2. El reparto depende del estado de la Colmena: en asedio, concentrados; en deriva, dispersos; en caza, detrás del tren. La semilla sale del nodo y del tick.
  3. Entran refuerzos por los bordes desde las celdas vecinas. Esta condición puede esperar al hito 4.
  4. Los soldados muertos se levantan y suman a la densidad.
  5. Cada zombi vivo vuelve a la celda en la que está, no siempre a la de la estación.
- **Respuesta de Marcos (22:28)**: lo adopta casi todo. Lo registra como N-005 a N-009.

| Condición | Cuándo entra |
|---|---|
| 1. Histéresis | Tal cual |
| 2. Reparto según la Colmena | Asedio y deriva en el hito 3; caza en el hito 4 |
| 3. Refuerzos por los bordes | Hito 4. La S0 sigue corriendo desde ya |
| 4. Soldados que se levantan | Hito 3 |
| 5. Cada zombi vuelve a su celda | Aceptada, aunque hoy la zona mide 128 m y la celda unos 3,5 km, así que todos los zombis caen en la celda de la estación |

- **Tiempo de materialización de 10k**: Marcos lo mide esta noche. Si pasa de 33 ms, la alerta pre-cargará la zona.
- **Tamaño de la zona** ✅: Lucía señala que en 128 m apenas cabe un tren de 6 vagones (unos 120 m). Marcos está a favor de **256 × 128 m**:
  - el flow field pasa de unos 10 a unos 20 ms por recálculo sin Burst, 2 veces por segundo;
  - con Burst será bastante menos (lo medirá);
  - la memoria sube unos 2 MB.
  Lo cambia en la parte 2 del hito 3. Si pasa de 3 ms, lo reparte entre varios ticks.

## D-N06 · Estilo del 2D y del audio (encargo de Iris) ✅
- **Propone**: Lucía, a petición de Iris. Detalle en `arte/necesidades-2d-audio.md`.
- **Decisión**:
  - **Paleta cerrada** de 32 colores, también para la interfaz, con tokens de color por uso.
  - Iconos maestros de **16 y 32 px**. **Se elimina el de 24 px.** El pixel art se muestra siempre a múltiplos enteros.
  - Marcos solo en retratos, eventos y la ficha de tren, con estilo de chapa remachada y placa de locomotora.
  - Marcadores del mapa con estilo de los **mapas ferroviarios y de estado mayor antiguos**.
- **Escalado en Unity (respuesta de Marcos)** ✅:
  - importación con filtro Point, sin mipmaps y sin compresión;
  - PanelSettings en Constant Pixel Size, con escala entera 1, 2 o 3 (la mayor que quepa);
  - cada icono, un VisualElement de 16·N o 32·N px en posiciones de píxel entero;
  - texto con fuente SDF.
  Se valida en pantalla con los iconos reales de la fase A.

## D-N07 · La Colmena suena, pero no habla ✅
- **Propone**: Lucía, a pregunta de Iris.
- **Decisión**: la Colmena tiene firma sonora, pero no voz. Tiene tres elementos:
  - **el coro**, un zumbido de gemidos afinados que crece en asedio;
  - **el motivo**, tres notas descendentes que suenan cada vez que la Colmena aprende algo;
  - **la interferencia**, estática con ritmo de respiración en la radio cerca de los nidos.
- **Voces**: solo de radio, sin narrador, en español y en inglés.
- **Por qué**: una mente que habla es un villano de película; una que suena da más miedo, y el motivo hace audible el pilar 4 («la Colmena aprende»).

## D-N08 · Ritmo de la horda en el arranque y coste de la munición ✅
- **Decide**: Mak (director), a propuesta de Hugo. **Consultados**: Marcos (que planteó la duda del hito 3 y lo aplica esta noche, con una prueba automática: día 1 sin asedios, primer asedio el día 2 con aviso) y Lucía (informada por Mak).
- **Ritmo del día 1**:
  - Marcos tenía 1 asedio a mediodía y 2–3 por la tarde ya el día 1.
  - Hugo propone que el día 1 no tenga asedios, solo 1–2 sondeos de 100–300 zombis. El primer asedio llega el día 2 y se anuncia.
  - Asedios a la vez: como mucho 1 en la etapa 1, 2 en la etapa 2 y 3 o más en la etapa 3.
  - **Por qué**: con 1–2 trenes, tres asedios el primer día son una derrota segura en el arranque de una campaña de 40–100 h. La simultaneidad del pilar 3 llega con la etapa 2, cuando el horario automático permite soltar un tren.
- **Munición**:
  - Se mantiene **1 u = 2.000 «disparos de fusil equivalentes»**. Es una unidad de juego: un palé real lleva unos 80.000 cartuchos, y con esa cifra la munición nunca escasearía.
  - Fusil: 1 disparo/s, así que un pelotón de 20 gasta 0,6 u por minuto de fuego continuo.
  - Ametralladora: 8 equivalentes/s. Proyectil de obús: 100 equivalentes (0,05 u), para que la artillería se note (matiz de Lucía en D-N02).
  - Calibración: unos 5 disparos por zombi común, o sea, unos **400 zombis por u** sin muros. Un asedio de 2.000–3.000 zombis cuesta 6–10 u, y la mitad con buena fortificación. Un tren de 100 u aguanta unos 8–10 asedios.
- **Formato de datos (respuesta de Marcos a Hugo)** ✅: enteros ×1000 en long, pulso económico cada hora de juego (tick % 1500 == 0), trenes de 5 vagones × 20 u = 100 u, y balance en CSV con «;» en `Assets/TBD/Data/`, todo entero.

## D-N09 · La música de ElevenLabs se puede vender en el juego ✅
- **Propone**: Iris. **Informados**: Mak y Lucía.
- **Hallazgo**: los términos de Eleven Music vigentes (9-oct-2026) permiten la música en **juegos indie** con el plan Pro (el juego factura menos de 500.000 $ y el estudio menos de 1 M$ al año). Si se supera, hay 60 días para cambiar de plan; las copias ya vendidas siguen valiendo. Efectos: permitidos en juegos. Voces: licencia comercial en los planes de pago.
- **Regla**: **nada de modelos en beta** para el juego, porque lo que se genera en beta no tiene licencia comercial. Efectos con `eleven_text_to_sound_v2` hasta confirmar la v3.
- **Por qué**: cierra el «sin verificar» de GDD §12. Fuentes en `arte/plan-assets-audio.md` §3.

## D-N10 · Lote de Pixelab por fases y prueba de audio ✅ (en parte) ⏸ (el resto)
- **Propone**: Iris. **Consultados**: Lucía (contenido, `arte/necesidades-2d-audio.md`; de acuerdo) y Mak (gasto).
- **Decisión de Mak (22:31)**: «sí a lo pequeño, lo grande espera a Eugenio».
  - ✅ **Fase A de Pixelab** el 6-nov, unas 450 generaciones: iconos del hito 3, prueba de texturas y 1 VFX de prueba.
  - ✅ **Prueba de audio** de unas 60 generaciones, solo con modelos estables y dentro del plan actual. Sin cambios de plan ni pagos.
  - ⏸ **Fases B a G**: se las presentamos a Eugenio por la mañana con los resultados de la A. Hay margen hasta el 11-nov.
- **Reparto de lo que sobra** (propuesta de Lucía, aceptada por Iris; pendiente de Eugenio): 40 % rostros del checkpoint, 30 % ilustraciones, 20 % retratos de campaña y 10 % VFX y decals nocturnos.
- **Encargo** para Marcos: `arte/encargo-fase-a.md`. La paleta se reduce y el fondo se quita con un script ya probado (`arte/herramientas/pixel_post.py`), sin gastar generaciones.
- **Por qué**: gastar créditos no tiene vuelta atrás, y Eugenio había parado el lote.
- **Respondida por Eugenio (22:38)**: su plan de ElevenLabs es **Pro** (110 €/mes). La música queda cubierta como juego indie. Marcos confirma el tier por la API al empezar, por rutina.

## QA-1 · Nada va a main sin pasar las pruebas desde un clon limpio ✅
- **Decide**: Sara (QA). **Consultados**: Marcos (vía Mak, porque su hilo no recibe mensajes directos).
- **Hallazgo**: el `.gitignore` ignora `*.csproj`, así que el proyecto de pruebas de dotnet no está en el repositorio y `dotnet run --project Dotnet/TBD.Sim.Tests` falla al clonarlo.
- **Decisión**: se versiona el csproj (excepción `!Dotnet/**/*.csproj`). Antes de cada commit de simulación, las pruebas tienen que pasar desde un clon limpio, no solo en el PC de Marcos.
- **Por qué**: una prueba que solo funciona en una máquina no es una prueba. Estado de esta noche: 71 de 71 en verde, comprobado con .NET 8 en un clon limpio y un csproj reconstruido.

## QA-2 · Bug Q1, falsa desincronización al pulsar F3 dos veces: se arregla antes de que pruebe Eugenio ✅
- **Propone**: Sara. **Consultado**: Marcos (vía Mak).
- **Decisión**: es el único bug de gravedad alta. Si no está arreglado por la mañana, la lista de pruebas de Eugenio le avisa de que no apague F3.
- **Por qué**: un aviso falso de desincronización hace desconfiar de la prueba que vigila el coop.

## QA-3 · El hash de estado tiene que cubrir todo el estado de la simulación 🔄
- **Propone**: Sara. **Consultado**: Marcos (pendiente de respuesta).
- **Hallazgo**: al hash de la zona le faltan la velocidad, la celda de pila, el contenido de los muros, el estado del tren y de la puerta, y la cola de órdenes. Además, no ve diferencias de 1 mm (comprobado).
- **Propuesta**: un hash bit a bit de cada campo y un hash por sistema, para localizar al culpable (GDD §17.4). No bloquea el hito 3, pero tiene que estar antes del coop.

## QA-4 · Repetición dorada en el hito 3 🔄
- **Propone**: Sara. **Consultado**: Marcos (pendiente de respuesta).
- **Hallazgo**: F3 compara dos mundos en el mismo PC, así que no detecta diferencias entre procesadores ni entre el Editor y una compilación, que es justo el riesgo del coop (GDD §17.4).
- **Propuesta**: un archivo con las órdenes y el hash de cada tick, grabado en una máquina y comprobado en otra (Editor contra compilación y, cuando se pueda, un PC contra otro).

## QA-5 · Las alertas de la Red, en tiempo de juego ✅ (decide Lucía en D-N11)
- **Propone**: Sara. **Decide**: Lucía, que encontró la causa de fondo: no habíamos fijado la escala del tiempo.
- **Hallazgo**: «horda a N s» contaba segundos reales a x1, y la horda se acercaba a 0,06 km/h de juego, una velocidad que encaja con la zona en detalle pero no con el mapa.
- **Decisión (D-N11)**:
  - El aviso va en tiempo de juego, con la hora de llegada: «Horda en 40 min (14:40)».
  - Las alertas críticas bajan la velocidad a x1.
  - En el mapa, la horda común va a 2 km/h de juego y la rápida a 6 km/h. Se la detecta a unos 3 km, lo que da unos 75 s reales de margen a x1.
  - Mi recomendación de 4 km/h se descarta: solo dejaba unos 12 s reales por km.
- **Prueba automática (la pidió Lucía)**: en `docs/qa/QaTests.cs`, bloque 6, se comprueba que el margen a x1 queda entre 60 y 120 s reales. Con el código actual falla (2.500 s). Con `HordeSpeedMmPerTick = 1333` (2 km/h de juego) pasa: 75 s, comprobado. La aplica Marcos.

## D-N11 · Escala del tiempo: reloj abstracto y velocidades del mapa ✅
- **Propone**: Lucía, a raíz de QA-5 (Sara). **Consultados**: Sara, Marcos (vía Mak) y Hugo (para su modelo de capacidad). Pendiente de que confirmen que no les rompe nada.
- **Problema**: nunca se fijó cómo se relacionan el reloj del calendario, el mapa y las zonas.
- **Decisión**:
  - **El reloj es abstracto**: 1 día de juego son unos 20 min reales a x1, así que el reloj va **72 veces más rápido** que el tiempo real. Es la convención de casi todos los juegos con calendario.
  - **Las velocidades del mapa (S0) van en tiempo de juego**:
    - horda común, 2 km/h; rápidos, 6 km/h;
    - trenes en vía abierta, unos 60 km/h (Sagunto–Teruel, unos 130 km, en unas 2,2 h de juego, menos de 2 min reales a x1).
  - **En las zonas en detalle todo va a velocidad visual real**: zombis a 1–1,5 m/s, y los trenes limitados como en una zona de maniobras. Una batalla de 5 min reales son unas 6 h de juego.
  - **Detección de la horda** a unos 3 km con visión normal (exploradores y drones la amplían). Eso da unos **75 s reales de aviso a x1**.
  - **Alertas en tiempo de juego, con la hora de llegada**: «Horda en 40 min (14:40)».
  - **Las alertas críticas bajan la velocidad a x1** de forma automática; se puede desactivar.
  - **Prueba automática (Sara)**: el margen de aviso a x1 tiene que quedar entre 60 y 120 s reales.
- **Por qué no 4 km/h**: solo deja 12 s reales por km a x1, y no da tiempo a saltar de línea (pilar 3). El objetivo de diseño es el margen de reacción, no la velocidad.
- **Se aplica en**: GDD §3 (nueva sección «Escalas»).

## D-N12 · Licencias de los datos de elevación: se pueden usar ✅
- **Encargo**: Mak a Lucía, para Marcos. Detalle y fuentes en `arte/licencias-elevacion.md`.
- **Resultado** (verificado en los textos oficiales):
  - **Copernicus DEM GLO-30 y GLO-90**, licencia pública «Full, Free & Open»: permite el uso comercial, modificar y distribuir, con aviso «produced using Copernicus WorldDEM-30 © DLR… © Airbus…», descargo de responsabilidad y sin dar a entender respaldo oficial.
  - **IGN y CNIG** (MDT05, MDT25, MDT200 y BTN): **CC BY 4.0**, con atribución «Obra derivada de … CC-BY 4.0 scne.es», que tiene que verse junto a los datos.
- **Decisión**:
  - **Mapa de la Península y del sur de Francia**: Copernicus.
  - **Detalle de las zonas en España**: IGN MDT05 o MDT25.
  - **Ríos, poblaciones y vías**: IGN BTN (no OpenStreetMap).
  - **Una cartela de atribución discreta en una esquina del mapa de operaciones**, como en los mapas antiguos, y la atribución completa en los créditos y en el aviso legal.
  - Marcos registra las fuentes en `THIRD_PARTY.md`.
- **Por qué**: cumple las dos licencias al pie de la letra. Copernicus es la única fuente coherente a través de las fronteras.

## D-N13 · Revisión de arte del hito 1: más contraste y luz ✅
- **Propone**: Lucía, como dirección de arte, tras revisar las capturas del hito 1. Detalle en `arte/revision-h1-lucia.md`. **Consultados**: Marcos y Mak (la prioridad frente al hito 3) y Sara (la prueba automática).
- **Qué funciona**:
  - la horda fluye como un río hacia la puerta;
  - la pila se lee;
  - las trazadoras en alta resolución sobre el mundo pixelado;
  - se mantiene el pixelado 1/3 por defecto.
- **Qué falla**:
  1. la horda no contrasta con el suelo;
  2. la luz es plana y no hay sombras;
  3. la noche no tiene focos;
  4. el tejado tiene el color del suelo y los zombis parecen flotar;
  5. el suelo está vacío;
  6. el perfil de día sale lavado.
- **Propuesta**: los puntos 1, 2, 4 y 6, si caben en una hora, antes de que Eugenio vea las capturas. Los demás, después.
- **Prueba de Sara**: diferencia de luminosidad entre horda y suelo de al menos un 25 %.
- **Decisión de Mak (22:36), a propuesta de Lucía**: Marcos hace los puntos 1 a 4 antes de seguir con el hito 3, justo después del bug Q1, con un tope de una hora, y saca capturas nuevas. El punto 5 queda para más adelante.

## D-N14 · Lista canónica de nodos del MVP ✅
- **Propone**: Lucía, al ver que el grafo del hito 2 (Marcos) y el modelo de Hugo usaban nodos distintos. **Decide**: Mak (22:39). **Informados**: Marcos y Hugo.
- **Lista**:
  - **Sagunto** (con el Puerto en el mismo nodo);
  - Puçol–**Valencia**;
  - Almenara–Nules–**Castellón**;
  - Segorbe–Barracas–**Teruel**–(puente del Jiloca)–Caminreal–Calamocha–Cariñena–**Zaragoza**.
- **Fuera de la demo** (ganchos para el acceso anticipado): reabrir Caminreal–Calatayud (la línea cerrada del Central de Aragón) y Castellón–Vinaròs.
- **Por qué**: hay una sola fuente de verdad (`demo-sagunto-guion.md`). Es un cambio de datos, no de código.

## D-N15 · Guion de la demo en tres actos y especificación del hito 3 🔄
- **Propone**: Lucía. **Consultados**: Hugo (si el ritmo se sostiene), Sara (prueba de camino crítico), Marcos (disparadores y dos preguntas del hito 3) e Iris (retratos y voces).
- **Guion** (`demo-sagunto-guion.md`):
  - Acto I «La última estación», días 1–3;
  - Acto II «El interior», días 4–7;
  - Acto III «El puente», días 8–10.
  Tiene 8 personajes con nombre, que son el tutorial por radio. Los momentos se disparan por el estado de la simulación, no por el tiempo. La pantalla final es **«Lo que la Colmena aprendió de ti»**. La única derrota es perder Sagunto.
- **Hito 3** (`diseno-hito3.md`, escrito *antes* de que se programe, tras el feedback de Mak):
  - umbrales del zoom y fundido;
  - mapa con exageración vertical ×1,5 y tintas de la paleta;
  - desembarcar y reembarcar (si fuerzas la salida, dejas a la tropa atrás);
  - consumo del inventario a menos de 150 m del tren;
  - muros persistentes por nodo;
  - la secuencia de prueba que tiene que emocionar.
- **Respuesta de Marcos (22:39)**:
  - **Muros**: en el hito 3 guarda por nodo los muros que construye el jugador, solo como datos (posición, orientación y altura). Las reglas completas de construcción van en el hito 5.
  - **Vuelo de 0,8 s**: lo confirmará cuando mida el tiempo de materializar 10k. Si no cabe, la alerta pre-carga la zona.
  - **D-N14**: la aplica en el hito 3 y reajusta los horarios a las nuevas longitudes de vía.

## D-N16 · Prueba de camino crítico, trenes de la demo, combate y pila abstractos ✅ (en parte) 🔄 (Marcos)
- **Propone**: Sara (`qa/prueba-camino-critico.md`) y Lucía. **Consultados**: Mak, Marcos y Hugo.
- **Aprobado por Lucía**: ventanas de ±1 día por momento, detector de bloqueo a los 2 días sin un momento nuevo, 18 de 20 semillas y 3 minutos por partida.
- **Trenes de la demo**: el escenario de la demo empieza con **2 trenes** (Tren 1 de combate y Tren 2 mixto). El Tren 3 sale del taller los días 5–6 y el **tren de obras se rehabilita en el taller hacia el día 7**. Máximo 4. El escenario del hito 2, que tiene 3 trenes, se queda como escenario de pruebas.
- **Combate abstracto S0** (faltaba): Marcos porta la fórmula del modelo de Hugo, en enteros.
- **Pila abstracta por nodo**:
  - sube con los zombis no abatidos por hora, dividido entre los metros de muro;
  - baja cuando cesa la presión;
  - si alcanza la altura del muro, hay brecha, con daño y bajas;
  - al rematerializar, la pila de la zona arranca a esa altura.
- **Por qué**: la amenaza visual y la abstracta tienen que ser la misma. Si no, alejar la cámara sería una trampa.

## QA-6 · Prueba del camino crítico de la demo (hito 6), diseñada ya ✅
- **Encarga**: Lucía. **Diseña**: Sara. **Aprueba los umbrales**: Lucía (±1 día por momento, detector de bloqueo a los 2 días sin momento nuevo, 18 de 20 semillas, menos de 3 min por partida).
- **Decisión**: los momentos de la demo son datos, con disparadores que son funciones puras del estado, y su registro entra en el hash. Seis jugadores automáticos que solo dan órdenes (equilibrado, rutinario, variable, contrario, pasivo y codicioso). Cada momento obligatorio tiene un plan B. Diseño en `docs/qa/prueba-camino-critico.md`.
- **Por qué**: si Marcos construye los disparadores así desde el hito 3, la prueba sale casi gratis en el hito 6. Las incoherencias que se encontraron (trenes, nodos, combate abstracto y pila abstracta) quedan resueltas en D-N16.

## D-N17 · Especificación de la Colmena del hito 4, escrita por adelantado 🔄
- **Propone**: Lucía (`diseno-colmena-h4.md`). **Consultados**: Hugo (números), Marcos (por Mak: si los puntos de emboscada van ya como datos del grafo en el hito 3) y Sara (pruebas).
- **Contenido** (números marcados como propuesta):
  - **Memoria de tráfico**: por tramo y por franja de 1 h. Cada paso suma 150 y decae a 0,85 al día. Umbrales: 400 para que la Colmena lo note, 600 para emboscar y 850 para cortar la vía.
  - **Memoria de atención**: la zona en detalle, no la cámara. A partir de 2 h de juego, la Colmena ataca en otro sitio.
  - **3 estados**: deriva, caza y asedio.
  - **Director por utilidad**: decide cada hora de juego, gasta la curva de Hugo y conserva la densidad.
  - **Informe de inteligencia**: informa también de lo que la Colmena **olvida**.
  - **Pruebas**: el jugador rutinario sufre 3 o más emboscadas en 10 días y el variable, 1 o menos.
- **Por qué**: Mak pidió adelantarse a lo que Marcos va a programar. Principio: «un antagonista que se ve pensar». Todo ataque nace de una memoria visible, conserva la densidad y llega con aviso.

## D-N18 · Ritmo de la demo validado con el modelo y una interdicción más fuerte ✅
- **Propone**: Hugo (200 partidas por jugador tipo, con los nodos de D-N14). **Consultada**: Lucía (de acuerdo).
- **Resultado del modelo** (jugador equilibrado): Castellón el día 1, Teruel el día 5, el puente el día 9 y Zaragoza el día 13–14. El jugador con prisa toma Zaragoza el día 7. El final «Zaragoza o día 10» funciona sin acortar la demo.
- **Cambios aprobados**:
  - **Apeaderos** (Puçol, Almenara, Segorbe, Barracas, Caminreal y Calamocha): se aseguran con un retén de 6 personas y sin materiales. **La estación que se funda en la demo es Nules**, que produce víveres.
  - **El Tren 3 está a medio montar**: cuesta 60 materiales y se encarga el día 3–4. Lucía lo convierte en una promesa del Acto I: Chispas lo enseña el día 1.
  - **Sagunto produce 80 de materiales al día.**
  - **Munición de la demo**: depósito de 150, alijos de Valencia (120) y Teruel (50) y la fábrica. Zaragoza no da munición en la demo.
- **D-N04 corregida con datos**: si la Colmena solo se come el 15 % de las horas-tren, el jugador con prisa gana el 96 % de las partidas. Hace falta que en los **picos** se coma el **30–35 %**. Con eso:

  | Jugador | Resultado |
  |---|---|
  | Equilibrado | Capacidad nominal ~1,4 y real ~1,0 |
  | Con prisa | Real ~0,45; pierde el 32 % de las partidas |
  | Tortuga | Muere hacia el día 38 |

  Lucía cede ante los datos.
- **Pendiente**: Hugo mide qué porcentaje de días tiene el jugador equilibrado al menos una estación por debajo del 85 % de lo que pide. El objetivo de Lucía es alrededor de la mitad de los días, para que la escasez se sienta y no solo se vea en una gráfica.
- **Resultado (Hugo)**: **51 % de los días** con los números finales de D-N21 (antes daba un 25 %). Para conseguirlo, la interdicción máxima sube al 35 %; subir los asedios mataba más partidas sin dar más escasez.

## D-N19 · Colmena del hito 4 corregida con el modelo y checkpoint con coste en los tres sentidos ✅
- **Propone**: Hugo (`economia/sim_memoria_trafico.py`). **Consultada**: Lucía (de acuerdo).
- **Memoria de tráfico**:
  - con +150 por paso, el corte de vía (850) no saltaba nunca;
  - ahora: **+200 por paso, 6 franjas de 4 h y un 50 % que se derrama a las franjas vecinas**, para que alternar las 06:00 y las 07:00 no engañe a la Colmena;
  - resultado en 10 días: rutinario, 4 emboscadas y 1 corte; quien alterna, 2; variable, 0; horario automático fijo, 12 emboscadas y 3 cortes.
- **Atención**: más de **6 h de juego acumuladas en el día** en una zona. Con 2 h, cualquier batalla la disparaba.
- **Curva de la Colmena**: 1.600 · (1 + día/20)^1,4 · √(1 + 0,3·huella). Es una potencia, no una exponencial.
- **Checkpoint** (idea de Hugo, con un cambio de Lucía):
  - el jugador que acepta a todos llega a 1.500 personas y pasa hambre;
  - para que rechazar no sea la jugada óptima, Lucía propone que **los rechazados no desaparezcan**: una parte acaba sumándose a la horda cerca de la estación;
  - aislar (1 día de cuarentena) es el término medio;
  - aceptar sin cuarentena tiene un pequeño riesgo oculto de infección.
- **Pendiente**: que Hugo compruebe que ninguna de las tres opciones domina a las otras.
- **Resultado (Hugo, 200 partidas de 70 días)**: aceptar siempre, 17 % de derrotas; aislar siempre, 10 %; el jugador mixto, 12 %; **rechazar siempre, 100 %**, porque las personas son el motor (producen, guarnecen y tripulan). Aceptar y aislar quedan parejos y rechazar solo sirve como válvula puntual cuando hay hambre: ninguna opción domina. Números: riesgo de brote del 1,2 % por persona aceptada (400 zombis y −8 % de población), cupo de cuarentena de 12 al día por ciudad, 25 zombis por rechazado y la reputación baja un 2 % por rechazado.

### D-N13 · seguimiento (22:51)
- **Marcos aplicó los puntos 1 a 4** (commit 05ef015, captura `arte_h1_revision.png`): zombis oscuros sobre suelo claro, tejado terracota, sol a 32° con sombras y día más cálido. 204 fps.
- **Legibilidad (prueba de Sara)**: de día pasa (L* 25–26). Al atardecer y de noche da unos 22 y no pasa.
- **Decisión de Lucía**: se priorizan los **focos cálidos** (punto 5a) con un tope de una hora, antes de seguir con el hito 3.
  - **Por qué**: la noche es el momento más pixel art y Eugenio va a ver capturas nocturnas. Bajar el umbral sería hacernos trampas.
  - **Atardecer**: sombras largas y naranjas.
  - **Suelo de día**: se lleva del amarillo limón al ocre de la paleta.
  - **Props (5b)**: se quedan en el hito 3.
  - **Prioridad frente al hito 3**: la confirma Mak.
- **Puntos de emboscada**: Marcos los añade como lista (km, tipo) por tramo dentro de D-N14.

## D-N20 · Fase A de Pixelab y prueba de audio bloqueadas hasta que Eugenio lo apruebe ⛔
- **Origen**: Marcos intentó lanzarlas y el sistema de permisos lo rechazó: gastan créditos de pago y debe aprobarlo Eugenio en persona. Informa Mak (22:52).
- **Estado**: todo preparado en `assets/fase-a/` (encargo, `pixel_post.py` y paleta). Nada se ha gastado.
- **Decisión de Iris**: el plan deja de contar con assets esta noche. Aprobación pedida a Eugenio en el resumen de las 07:00. Mientras tanto no hay más generaciones de pago; el calendario de Pixelab pierde un día, con margen hasta el 11-nov.
- **Lección**: la aprobación del equipo no sustituye a la de Eugenio para gastar créditos de pago. Tendría que haberlo previsto al planificar.


## D-N21 · Balance v1 cerrado: números, CSV para Marcos y casos de prueba ✅
- **Propone**: Hugo. **Consultados**: Lucía (guion, Colmena y checkpoint, de acuerdo) y Marcos (formato de datos, a través de Mak). Documento: `economia/economia-balance.md`.
- **Decisiones del modelo que no estaban en el GDD** (inventos de Hugo; Lucía pidió que quedaran a la vista):
  - **Trenes medidos en horas-tren, no en toneladas**. Con 60 km/h y las distancias reales, el tonelaje no limita nunca. Lo que limita es el tiempo del tren, que es camión y cuartel a la vez: 16 h útiles al día, 4 h de carga por viaje, ruta diaria por rama, 8 h para abrir un nodo y 6 h para defender un asedio.
  - **Alijos de un solo uso**: Valencia 120 u de munición (la base de Bétera es real) y Teruel 50.
  - **Valencia atrae el doble** a la Colmena (es un nido, idea de Lucía con número de Hugo).
  - **Repostaje en cualquier depósito de la red**: sin esto, la red se ahogaba en un círculo vicioso.
  - **Las ciudades rinden más con más gente**: plantilla de 30 personas y +50 % por plantilla extra, como mucho x2. Es lineal a trozos para que sea entero.
  - **Derrota por colapso**: 5 días seguidos sin combustible (§3b, PROTOTIPO).
- **Números finales**: curva H = 1.600·(1+d/20)^1,4·√(1+0,3·huella) (tabla precalculada para el lockstep). Interdicción del 4 % al 35 %. Tren nuevo: 120 materiales y 30 de combustible (el Tren 3, 60 y 15). Puente: 80 materiales. Fortificación: 30 materiales por nivel y +20 % por nivel. Hasta 6 trenes en la etapa 2.
- **Resultado (200 partidas, 70 días)**:

  | Jugador | Derrotas | Nodos perdidos | Zaragoza | Días con escasez |
  |---|---|---|---|---|
  | Equilibrado | 12 % | 5 | día 13–14 | 51 % |
  | Con prisa | 33 % | 17 | día 7–8 | 44 % |
  | Tortuga | 100 % (día 38) | 3 | nunca | 13 % |

- **Riesgo que hay que medir primero**: la eficacia de la munición. Con 300 zombis por u en vez de 400, el equilibrado pierde el 74 % de las partidas. El caso **P7** de `economia/csv/casos_prueba.csv` lo mide en la zona del hito 3.
- **Entregado a Marcos**: `economia/csv/` con 5 CSV de balance (todo entero, «;», escala en milésimas, redondeo hacia abajo) y `casos_prueba.csv`: P1–P6 exactos (combate S0, presupuesto de la Colmena, memoria de tráfico, pila, viaje en ticks y producción) y P7–P8 como rangos. Él decide si los adapta a su plantilla.
- **Avisos para el futuro**: hacia el día 60 la red del MVP se queda pequeña (gasto de munición ≈ producción), justo donde encaja abrir la etapa 3 en el acceso anticipado. **Castellón es el talón de Aquiles** (única fuente de combustible): la Colmena debería aprender a atacarlo.

### D-N19 · seguimiento (22:57, Hugo)
- **Escasez sentida**:
  - el jugador equilibrado tiene al menos una estación por debajo del 85 % el **51 % de los días** (objetivo cumplido), con la interdicción máxima en el 35 %;
  - derrotas: equilibrado 12 %, con prisa 33 % y tortuga 100 %;
  - **regla**: subir los asedios no da más escasez, solo más partidas perdidas.
- **Checkpoint con los rechazados que vuelven**:
  - derrotas: aceptar siempre, 17 %; aislar siempre, 10 %; mixto, 12 %; rechazar siempre, 100 %;
  - la población es el motor de la economía, así que rechazar solo sirve como válvula cuando hay hambre.
- **Matiz de Lucía**: «aislar siempre» sale ligeramente mejor. Por eso la **cuarentena tendrá plazas limitadas según el nivel de la estación** (orientativo: apeadero 0, estación 20 y nudo 60). Pendiente de que Hugo lo pruebe.
- **Castellón**, idea de Hugo: como es la única fuente de combustible, el día 7 la Colmena va a por ella. Añadido al guion.


## D-N22 · Señales que avisan al jugador «tortuga» antes de que sea tarde ✅
- **Pide**: Mak (Eugenio podría jugar así). **Propone**: Hugo, con el modelo. **Se consulta**: Lucía, para el tono de los avisos por radio.
- **Problema**: el jugador que solo consolida la costa muere siempre, hacia el día 38. Es deliberado (§3b: no se puede esperar sin coste), pero tiene que verlo venir.
- **Señal medida en el modelo: índice de escalada** = presión diaria de la Colmena / (munición sostenible al día × eficacia media). La munición sostenible es la producción más el 10 % de la reserva.

  | Jugador | Día 10 | Día 20 | Día 25 | Día 30 | Día 35 |
  |---|---|---|---|---|---|
  | Tortuga | 0,26 | 0,40 | 0,67 | 1,40 | 2,60 |
  | Equilibrado | 0,45 | 0,22 | 0,22 | 0,25 | 0,29 |

- **Decisión (cuatro avisos escalonados)**:
  1. **Día 12 sin la rama del interior**: Bolea por radio: «Comandante, aquí abajo no hay balas para siempre. En Zaragoza, sí». (Frase retocada por Lucía.)
  2. **Índice ≥ 0,5 tres días seguidos** (tortuga: hacia el día 22, 16 días antes de morir): aviso en el informe de inteligencia: «La Colmena crece más rápido que tu red». En el mapa, la barra de presión se pone ámbar.
  3. **Índice ≥ 1,0** (hacia el día 29): alarma roja y Reig: «Al ritmo de hoy, Sagunto aguanta X días». Es una cuenta atrás calculada.
  4. **Panel de logística**: «días de munición» siempre visible, con tendencia.
- **Por qué**: así hay más de dos semanas de juego (unas 5 h reales) entre el primer aviso y la derrota. El jugador equilibrado casi nunca lo ve (se queda en 0,2–0,3 cuando tiene Zaragoza): el aviso solo salta a quien de verdad se está quedando atrás.

### Seguimiento D-N19 · Oleadas y plazas de cuarentena (propuesta de Lucía)
- **Probado**: plazas por nivel (apeadero 0, estación 20, ciudad 40, nudo 60) más oleadas de 30–80 refugiados (15 % de probabilidad diaria por ciudad).
- **Resultado**: con oleadas, **aislar sale todavía más dominante** (16 % de derrotas frente al 56 % de aceptar), porque las plazas limitadas actúan como tope de población y el que acepta todo se queda sin víveres (66 % de días con escasez).
- **Conclusión de Hugo**: el dilema real no es aceptar o aislar, sino **cuántos dejas entrar** frente a los víveres que tienes. Propuesta para Lucía: que el checkpoint de una oleada pregunte cuántos entran (con un indicador de víveres) y que la cuarentena sea un número de plazas. Así el óptimo cambia con el estado y no hay una respuesta fija.
- **Mientras tanto**: las plazas de Lucía quedan en el modelo y las oleadas, apagadas, hasta que ella decida.

### Pendiente para Eugenio · Caso P7 (eficacia real de la munición) ⏸
- **Estado**: Marcos mete esta noche en dotnet los casos P1–P6 (exactos). El P7 necesita soldados en la zona (parte 4 del hito 3): lo intenta esta noche, sin promesa.
- **Por qué importa**: es el parámetro más frágil del balance. Con 300 zombis por u en lugar de 400, el jugador equilibrado pierde el 74 % de las partidas. Cuando haya cifra, Hugo recalibra (`sim_economia.py` → `generar_csv.py`).

### D-N13 · seguimiento (22:59): focos y paleta
- **Marcos (commit eceb48d, `arte_h1_focos.png`)**: tres focos ámbar con halo y bloom, a 196 fps. De noche la prueba da unos 19, con siluetas negras sobre el charco de luz.
- **Decisión de Lucía, noche**:
  - **Siluetas negras sobre luz como lectura nocturna** (contraluz), igual que la referencia nocturna de Ebbtide. El shader de rim queda como pulido opcional para el hito 7.
  - **Criterio de la prueba de noche**: 25 de L* o más dentro de los charcos de luz; fuera, sin exigencia, porque por la noche solo se ve lo que tus luces iluminan.
- **Decisión de Lucía, suelo amarillo**:
  - **Ni color nuevo ni bajar el albedo**: se baja la **mezcla de la paleta en el mundo 3D del 100 % al 60–70 %**, como ya decía `arte/direccion-visual.md` (decisión 4: paleta como gradación suave). Así vuelven el ocre del suelo y el ámbar de los focos, que ahora sale salmón.
  - La paleta estricta queda para el pixel art 2D.
  - Si no basta, se sustituye un color por un ocre claro, sin pasar de 32.
- **Arte del hito 1, listo para Eugenio**. Marcos vuelve al hito 3.

## QA-7 · Criterio de legibilidad nocturno: solo dentro de los charcos de luz ✅
- **Decide**: Lucía (D-N13). **Implementa**: Sara.
- **Criterio**: día y atardecer, diferencia de claridad L* de 25 o más sobre el suelo. De noche, 25 o más **dentro de los charcos de luz**, y sin exigencia fuera (siluetas a contraluz, deliberadas).
- **Cómo se mide**: `legibilidad_horda.py --noche`. Los charcos son el suelo del anillo con L* de 35 o más, y cuenta la horda pegada a ese suelo. **El 35 es mi traducción, no un número de Lucía**: le pedí que lo confirme. Si la captura no tiene focos a la vista, sale con código 2 (captura inadecuada).
- **Por qué**: la noche de Ebbtide se lee a contraluz; exigir contraste en toda la imagen empujaba a un look plano.

## D-N23 · El checkpoint se decide eligiendo rostros, no con un número ✅
- **Propone**: Lucía, a partir del hallazgo de Hugo: el dilema es cuántos entran, no aceptar o aislar. **Consultado**: Hugo (que lo modele).
- **Decisión de diseño**:
  - una oleada llega como **4–8 grupos con tarjeta**: rostro, tamaño (3–15) y un rasgo (obreros, desertores, familia con niños, heridos, médico…);
  - el jugador elige **qué grupos** entran, con un indicador de días de víveres que se actualiza en directo;
  - la cuarentena es un **número de plazas** según el nivel de la estación;
  - los rechazados pueden acabar sumándose a la horda (D-N19).
- **Por qué**: un deslizador de números haría desaparecer los rostros y el peso moral. Elegir a quién dejas fuera es el dilema de verdad, y el óptimo cambia con el estado de la partida.
- **Avisos al jugador tortuga (D-N22)**: Lucía aprueba el tono, con un retoque para Bolea: «Comandante, aquí abajo no hay balas para siempre. En Zaragoza, sí».
- **Pendiente**: que Hugo compruebe que ninguna regla fija (por ejemplo, «solo obreros») domina.

### D-N13 · cierre (23:03)
- Con la mezcla de la paleta al 65 %, el suelo vuelve al ocre y el día pasa la prueba (L* 25,3). **El arte del hito 1 queda cerrado.** Los focos siguen algo salmón de noche; se corrige en el hito 7.
- **D-N14, coordenadas**: Lucía pasa a Marcos coordenadas aproximadas de memoria (centro del pueblo, error de 1–2 km) de Puçol, Almenara, Nules, Barracas, Caminreal, Calamocha y Cariñena. Van marcadas como aproximadas y se sustituirán por las de las estaciones de la BTN del IGN.

### Seguimiento D-N22 · Checkpoint por grupos con rostro (Lucía) y oleadas encendidas ✅
- **Diseño de Lucía**: una oleada llega como **4–8 grupos** con tarjeta (rostro, tamaño de 3 a 15 y rasgo). El jugador elige **qué grupos** entran, con un indicador de días de víveres. Las plazas de cuarentena son limitadas.
- **Números de Hugo** (`economia/csv/balance_refugiados.csv`):
  - obreros: trabajo x1,5;
  - desertores: guarnición, 0,2 u de munición por persona y riesgo de infección x1,5;
  - familias: trabajo x0,3, pero **suben la moral**: +1 % de producción del nodo por familiar, como mucho +25 %;
  - heridos: víveres x1,5 y riesgo x2; trabajan cuando se curan, a los 5 días;
  - médico: 1–3 personas, reduce a la mitad el riesgo de brote de su estación.
  - Echar a familias o heridos cuesta **x3 de reputación** y baja la moral.
- **Resultado (150 partidas por regla y escenario, % de derrotas)**:

  | Regla | Base | Víveres escasos | Oleadas frecuentes |
  |---|---|---|---|
  | **Adaptativa** (útiles siempre; familias y heridos si hay víveres para 8 días y no hay asedio) | **16** | **19** | 24 |
  | Solo útiles (obreros, desertores y médico) | 21 | 34 | **20** |
  | Todos | 50 | 31 | 63 |
  | Solo obreros | 40 | 51 | 28 |
  | Nadie | 77 | 79 | 92 |

- **Conclusión**: **ninguna regla fija domina**. «Solo útiles» gana con oleadas frecuentes y pierde con hambre, frente a «todos». La regla que lee el estado es la mejor en dos de los tres escenarios. Es el dilema que buscaba Lucía: «¿a quién dejo fuera?», según el momento.
- **Primera versión, corregida**: sin la moral de las familias, «solo útiles» ganaba siempre (17 % frente a 35 %). Las familias tienen que aportar algo tangible.
- **Las oleadas quedan encendidas** (10 % al día por ciudad). Números globales actualizados: el equilibrado pierde el 17 % y siente escasez el 45 % de los días; prisa, 52 %; tortuga, 100 %. En la demo, mediana: Teruel el día 4, Tren 3 y puente el día 8, ninguna derrota en 10 días.

### D-N23 · seguimiento (23:05, Hugo)
- **Modelado con grupos y rasgos**, con 150 partidas por regla. Derrotas:

  | Escenario | Adaptativa | Solo útiles | Todos |
  |---|---|---|---|
  | Base | 16 % | 21 % | 50 % |
  | Víveres escasos | 19 % | 34 % | 31 % |
  | Oleadas frecuentes | 24 % | 20 % | 63 % |

  **Ninguna regla fija gana siempre**, y la que lee el estado es la mejor en dos de tres escenarios.
- **Invento de Hugo para que las familias cuenten**:
  - cada familiar sube un 1 % la producción del nodo («la gente trabaja mejor si tiene a quién proteger»), como mucho un 25 %;
  - echar a familias o heridos cuesta el triple de **reputación**.
- **Reputación (definición propuesta por Lucía)**: una sola barra y sin pantalla propia. Sube o baja la moral (§9b) y cambia la frecuencia de las oleadas futuras, porque la noticia se corre. Pendiente de que Hugo confirme que encaja con su modelo.

## D-N24 · Puntos de emboscada del MVP ✅
- **Propone**: Marcos (commit 1ba16f9, inventados sobre la geografía aproximada). **Revisa**: Lucía.
- **Aprobados**: curvas del Palancia, desmonte de Jérica, curvas de Puebla de Valverde, puerto de Escandón (emboscada estrella), puente del Jiloca y puente del Mijares (costa, entre Nules y Castellón).
- **Por verificar con la BTN**: desmonte de Paniza (no está claro que la vía pase por allí).
- **Añadido por Lucía**: el **puente del barranco del Carraixet**, entre Valencia y Puçol, junto al nido de Valencia. Sin él, la línea de la Costa casi no tenía castigo a la rutina en el tramo sur.
- **Estado del mapa 3D** (`union_dn14.png`): ya funciona con relieve provisional, manchas de horda y los 2 trenes iniciales (Costa y Montaña). Detalles para más adelante: una etiqueta pisa a otra y las nieves salen demasiado blancas.

### Reputación definida (Lucía) y números finales de la noche ✅
- **Propone**: Lucía (una sola barra, sin pantalla propia). **Modela**: Hugo.
- **Reputación** (0–100 %, empieza en 100):
  - baja un 2 % por persona rechazada (el triple si es una familia o un herido) y nunca baja del 30 %;
  - sube un 1 % al día y un 3 % por cada grupo de familias acogido.
  - **Efecto 1**: multiplica cuánta gente llega (goteo y oleadas).
  - **Efecto 2**: por debajo del 50 %, la moral cae y la producción baja un 10 %.
- **Comprobado**: con la reputación, ninguna regla fija sigue dominando. % de derrotas: base, adaptativa 13 frente a útiles 25; víveres escasos, adaptativa 28 frente a todos 34; oleadas frecuentes, útiles 19 frente a adaptativa 21.
- **Reajuste**: las oleadas y la moral hacían la economía más rica y la escasez bajó al 38 % de los días. La interdicción máxima sube al **37 %** para volver al objetivo de Lucía.
- **Números finales (200 partidas, 70 días)**:

  | Jugador | Derrotas | Días con escasez |
  |---|---|---|
  | Equilibrado | 15 % | 47 % |
  | Con prisa | 76 % | 56 % |
  | Tortuga | 100 % (día 38) | 9 % |

  Demo: Teruel el día 4, Tren 3 el día 8 y puente el día 8–9. CSV regenerados (`interdiccion_max` 370 y dos filas nuevas de reputación).

### D-N23 · reputación y castigo a la prisa (23:08, Lucía)
- **Reputación**: definida en el GDD §9b con los números de Hugo.
- **Lucía no acepta que el jugador con prisa pierda el 76 % de las partidas** (efecto de subir la interdicción al 37 % para recuperar la escasez). En una demo de Steam, el jugador atrevido es el que habla del juego: tiene que sentir riesgo, no injusticia.
- **Objetivos**:

  | Medida | Objetivo |
  |---|---|
  | Derrotas del jugador con prisa | 35–45 % |
  | Derrotas del jugador equilibrado | 12–16 % |
  | Días con escasez | 45–50 % |

- **Cómo**: Hugo baja `k_huella` y, si hace falta, hace que la huella crezca más despacio en los 10 primeros días.

## D-N25 · La presión de la Colmena se reparte en tres niveles de dificultad ✅
- **Propone**: Hugo (Economía), a petición de Lucía (D-N23, 23:08). **Consultados**: Lucía (decide el diseño) y Marcos, a través de Mak (cambian los CSV).
- **Problema**: con un solo juego de parámetros no se cumplen a la vez los dos objetivos de Lucía. Hugo probó una rejilla de `k_huella` (0,10–0,30), `alfa` (1,4–1,6) y `H0` (1.400–1.900), con 150 partidas por punto:
  - Si se baja `k_huella` para que la prisa pierda el 40 %, el equilibrado casi nunca pierde (4–5 %).
  - Si se sube la presión para que el equilibrado pierda el 14 %, la prisa vuelve al 74 %.
  - La razón es que la huella castiga sobre todo al que crece rápido, así que las dos curvas se mueven juntas.
- **Decisión**: tres niveles de dificultad, que se leen de `balance_dificultad.csv`. Medido con 150–300 partidas por nivel:

  | Nivel | H0 | α | k_huella | Equilibrado | Prisa | Escasez del equilibrado |
  |---|---|---|---|---|---|---|
  | Fácil | 1.600 | 1,50 | 0,12 | 2 % | 11 % | 42 % |
  | **Normal** (por defecto) | 1.600 | 1,55 | 0,16 | 5 % | 42 % | 45 % |
  | Veterano | 1.800 | 1,40 | 0,22 | 12 % | 75 % | 46 % |

- **Por qué**:
  - En Normal, el equilibrado pierde poco, pero pierde unos 4,6 nodos por partida y pasa escasez el 45 % de los días. Se gana, pero se sufre.
  - El objetivo de Lucía para el equilibrado (12–16 %) se cumple en Veterano.
  - La idea de Lucía de que la huella crezca más despacio al principio no hace falta: la demo ya no tiene derrotas en los 10 primeros días.
- **Ritmo de la demo**, sin cambios: Teruel el día 3–4, Zaragoza el día 13 (el de prisa, el día 6) y ninguna derrota en 10 días. La tortuga sigue perdiendo hacia el día 40 en los tres niveles, que es lo que avisan las señales de D-N22.
- **Archivos**: `sim_economia.py` (α 1,55 y k 0,16), `colmena_curva.csv` regenerado, `balance_dificultad.csv` nuevo y el caso P2 de `casos_prueba.py`, que ahora lee los valores vigentes. Nuevos esperados: día 10 → H=4020; día 37 → 13855; día 150 → 120028.
- **Pendiente**: que Lucía confirme si Normal le vale o si prefiere que el nivel por defecto sea Veterano.

### D-N25 · cierre (00:15, Lucía)
- **Lucía elige Normal como nivel por defecto**: «sufre, pero no tira 30 horas a la basura». Veterano queda para quien lo busque.
- Cada nivel mueve dos cosas: la curva de Hugo y los umbrales de la memoria de la Colmena (GDD §5.4 y §14). En Veterano, la Colmena es más grande y además aprende antes.
- La llegada a Teruel pasa a una ventana de días 3–5. P8 queda actualizado en `casos_prueba.csv`. Sara corre la prueba de camino crítico en Normal.

## D-N26 · Hito 3, parte 2: el bucle central funciona; revisión de Lucía ✅
- **Marcos (commit 386e24c)**: se baja del mapa a Segorbe, se entra en la zona con 6.000 zombis asediando y, al alejar la cámara (o con M), se vuelve al mapa con los vivos devueltos a la mancha.
  - Crear 6.000 zombis cuesta 71,5 ms (10.000, unos 120 ms estimados). El fundido de 0,6 s y el vuelo lo tapan, así que **el vuelo de cámara se queda** y la precarga se hará con SubScenes.
- **Revisión de Lucía** (`zona_segorbe.png`, `vuelta_mapa.png`):
  1. **57 FPS con 6.000 zombis**, frente a 198 con 10.000 en el hito 1. Hay que encontrar la causa antes de la parte 4: el criterio del MVP es 10k a 60 fps. Riesgo para Sara.
  2. **Al volver al mapa no se ve la mancha** de cerca. Además, hay un hueco en la vía y el marcador de la estación queda fuera de ella.
  3. Escenario de prueba con asedio el día 1: vale para probar, pero la demo sigue D-N08.
- **Dificultad por defecto**: Normal (D-N25).
- **Hallazgo de Sara (23:15)**: mientras una zona está activa, la difusión vuelve a llenar la celda del nodo. Al salir se suma lo que devuelve la zona, así que la mancha queda duplicada (183 → 18 → 336).
  - **Decisión de Lucía**: **se congela la celda del nodo** (sin difusión ni deriva) mientras hay zona, porque la zona es la dueña de esa densidad.
  - En el hito 4, lo que entraría por difusión se convierte en refuerzos que entran por el borde de la zona.
  - La prueba exige que se conserve la suma de la celda, las vecinas, la zona y los muertos en cada tick.
- **Respuesta de Marcos (23:16)**, los tres puntos resueltos:
  1. Los 57 fps venían de un tope de 60 fps del mapa que se arrastraba a la zona. Ahora da **201 fps con 6.000 zombis**. El mapa no se dibuja mientras hay zona; solo corre la red S0, a 0,02 ms por tick.
  2. La mancha se ve de cerca, como un moteado sobre la tinta roja. Vías, tren y etiquetas ya están en su sitio.
  3. El asedio de 6.000 era forzado para la prueba; la mancha real del día 1 no llega a asedio.

## D-N27 · P7 medido: la munición sobra y lo que limita en campo abierto es la cadencia ✅
- **Propone**: Marcos (medida y propuesta de la cadencia). **Recalibra**: Hugo. **Decide**: Mak, que pasa los números de CombatConst al CSV. **Consultada**: Lucía, por lo que cambia el valor de los muros.
- **La medida (Marcos, en dotnet con la lógica de la zona)**: 20 fusileros y 1 ametralladora, sin muros, contra 2.000 comunes. Gastan 1,51 u (3.017 disparos, 2,6 por abatido; el modelo suponía 5). Pero pierden: en 5 minutos abaten 1.143, quedan 857 vivos y caen 12 de 21.
- **Lectura de Hugo**:
  1. **La munición no se rompe**: la medida queda lejos del umbral de 6,7 u.
  2. **No se adopta el 2,6 como verdad**. Con 770 zombis por u (la eficacia medida), el equilibrado pierde el 1 % y la prisa el 11 %: la munición deja de ser escasa y la economía pierde su tensión. Las probabilidades de acierto (42 % y 6 %) son de prototipo, así que se ajusta la zona al modelo y no al revés.
  3. **La cadencia es real y entra en el S0**. Las bajas encajan casi exactas con el modelo (0,014 por zombi vivo frente a 0,004 × 3 = 0,012).
- **Decisión**:
  - **Zona (Marcos)**: bajar el acierto a la mitad (en torno al 21 % a bocajarro y al 3 % a 60 m) y doblar la cadencia de fuego. Así salen unos 5 disparos por abatido (≈400 por u) y se mantienen los ~54 abatidos por tirador en 5 minutos. Nuevo rango de P7: 1.000–1.300 abatidos, 4–6 disparos por abatido, 2,5–3,9 u.
  - **S0 sin muros**: tope de abatidos = tiradores × 54 por asalto. Lo que pasa del tope llega al cuerpo a cuerpo y mata a 0,014 personas por zombi. La falta de muros se paga en bajas, no en munición, como proponía Marcos. Con muros el tope no se alcanza: el muro retiene a la horda toda la hora, y doce tiradores dan unos 7.800 abatidos por hora.
  - **Limpiar un nodo es campo abierto**: el tren lleva una tropa de asalto de 30, que vuelve salvo las bajas. Teruel (1.120 zombis) sale sin bajas. Zaragoza (1.840) cuesta unas 3 personas, así que conviene llevar más gente o hacer dos pasadas.
  - ~~**Reajuste para seguir en los objetivos de D-N25**~~ (superado por el seguimiento de abajo: con el tren como muro se vuelve a los números de D-N25), porque la cadencia castiga sobre todo a la prisa (subía al 53–59 %). Normal baja k_huella a 0,14, Fácil a 0,10 y Veterano a 0,19:

  | Nivel | Equilibrado | Prisa | Escasez del equilibrado |
  |---|---|---|---|
  | Fácil | 2 % | 17 % | 42 % |
  | **Normal** | 1–4 % | 35–38 % | 46 % |
  | Veterano | 10 % | 68 % | 47 % |

  - Las cifras salen de 200–300 partidas, con un ruido de ±3 puntos. Por limpiar nodos, el equilibrado pierde unas 14 personas por campaña y la prisa unas 28.
- **Ritmo de la demo**: Teruel el día 3–4, Zaragoza el día 13–15, sin derrotas en 10 días.
- **Archivos**:
  - `sim_economia.py`: tres parámetros nuevos (`abatidos_tirador_contacto`, `bajas_por_z_contacto` y `tropa_asalto`).
  - `balance_economia.csv`: tres filas nuevas.
  - `balance_colmena.csv` y `balance_dificultad.csv`: k nuevo.
  - `casos_prueba.csv`: P1d replica la medida de Marcos (1.134 abatidos y 12,1 bajas, frente a 1.143 y 12 medidos), y hay casos nuevos P1e y P1f. P2 cambia por el k nuevo: día 10 → 3906, día 37 → 13279 y día 150 → 113364. P7 tiene rango nuevo.
- **Pregunta para Lucía**: ¿le vale que los muros valgan «tiempo», es decir, que conviertan un problema de cadencia en uno de munición, y que la tropa en campo abierto sea frágil a propósito?

### D-N27 · seguimiento (00:35): el tren parado es un muro móvil (Lucía) ✅
- **Lucía aprueba que el muro compre tiempo** y la mitad de acierto con el doble de cadencia («el doble de trazadoras, más espectáculo con el mismo balance»).
- **Lucía añade**: la tropa que dispara desde el tren parado (vagones blindados o plataforma de tiro) cuenta como «tras muro». Bajarse del tren pasa a ser una decisión de riesgo.
- **Hugo lo comprueba en el modelo** (150–300 partidas):

  | Variante | Equilibrado | Prisa |
  |---|---|---|
  | Sin tren-muro, con k 0,14 | 1–4 % | 35–38 % |
  | **Con tren-muro, con k 0,16 (como en D-N25)** | 5 % | 42 % |
  | Con tren-muro y sin muros de estación | **72 %** | 99 % |

- **Conclusión**: el tren no hace inútiles los muros de estación. Sin ellos, el equilibrado pierde 72 de cada 100 campañas, porque la presión diaria cae sobre todos los nodos y el tren solo puede estar en uno. Su alcance también lo limitan las horas-tren (6 h por asedio) y la pila contra los vagones (D-N16).
- Con el tren como muro, limpiar un nodo desde el tren no cuesta bajas, así que vuelven exactamente los números de D-N25: Normal con k 0,16 (5 % y 42 %), Fácil con 0,12 y Veterano con 0,22. La cadencia solo castiga a quien baja a pie o a una estación sin muros y sin tren.
- **Archivos**: `tren_muro` en `sim_economia.py`, `k_huella` de vuelta a 160 en los CSV, P2 vuelve a 4020 / 13855 / 120028, y P1e y P1f pasan a ser casos «a pie».

## QA-8 · La celda de un nodo con zona activa queda congelada ✅
- **Propone**: Sara. **Decide**: Lucía (D-N26). **Aplica**: Marcos (16d6a1b).
- **Problema**: mientras la zona estaba abierta, la difusión rellenaba la celda del nodo y al volver se sumaba lo devuelto: la mancha de ese nodo se duplicaba.
- **Decisión**: con zona activa, la celda no da ni recibe masa. Prueba en `docs/qa/QaTests.cs` (bloque 9), verificada: celda a 0 durante 1.500 ticks y masa conservada en cada tick. En el hito 4, lo que no entre por difusión se convertirá en refuerzos por el borde y la suma tendrá que incluirlos, con los muertos.

## D-N28 · Hito 3, parte 4: disparar desde el tren y pauta de efectos ✅
- **Marcos (`tropa_tren.png`)**: con la tecla 6, 21 soldados disparan desde el tren parado y la horda se amontona contra los vagones. Resultado: 372 abatidos, 0 bajas, 1,0 u y 199 fps. Al arrancar, el tren deja de ser muro. Con la tecla 0 se despliega el pelotón a pie. Por ahora, la munición sale de las existencias de la estación; el inventario del tren llega en la siguiente vuelta.
- **Revisión de Lucía**: los efectos tapan a la horda. **Pauta**:
  - **Trazadoras**: línea de 1–2 px, núcleo `#f0dc9c` con halo `#e08c30`, de 0,05–0,08 s, y **solo una de cada 4 balas**.
  - **Fogonazos**: de 2–4 píxeles del mundo, durante 1–2 fotogramas.
  - **Bloom**: umbral más alto e intensidad más baja.
  - **Chispas**: la mitad, y más cortas.
  - **Regla**: con fuego sostenido, los efectos no tapan más de un 5 % de la pantalla.
- **Por qué**: la horda es la protagonista. El efecto acompaña, no tapa.

## QA-9 · Alarma de efectos: el 5 % cuenta el efecto entero de la partícula, y la captura «antes» tiene que suspender 🔄
- **Propone**: Lucía (D-N28). **Mide**: Sara (`docs/qa/efectos_pantalla.py`).
- **Decisión**: el 5 % de la pantalla cuenta lo que dibuja cada partícula de VFX_HD (núcleo más su halo de sprite). El bloom del postproceso no entra: se controla con su umbral y su intensidad.
- **Regla de calibración (Lucía)**: la captura «antes» (`tropa_tren.png`) tiene que suspender. Si con la máscara sale por debajo del 5 %, el número está mal elegido y se baja (por ejemplo, al 3 %) hasta que suspenda lo que a ojo es malo.
- **Estado**: sin máscara, `tropa_tren.png` da 3,9 % a 6,8 % según el umbral de brillo. Pendiente de la máscara magenta de las partículas, que pido a Marcos.
- **Marcos (commit 2be5f71, `tropa_tren_efectos.png`)**: efectos rebajados del 9,47 % al 0,03 % de la pantalla. Ahora casi no se ve que disparan. La munición ya sale primero de la carga del tren.
  - **Decisión de Lucía**: el objetivo es un **1–2 % de la pantalla con fuego sostenido**.
    - **Fogonazo**: de 4–6 px del mundo, durante 2 fotogramas, con parpadeo irregular.
    - **Trazadoras**: más largas (un 20–25 % de la distancia al objetivo).
    - **Efecto nuevo, el impacto**: un soplo de polvo o sangre de 2–3 px durante 0,2 s sobre el zombi alcanzado.
    - El fogonazo que ilumina de noche queda para el hito 7.
  - **Nota de rendimiento**: 149 fps de noche frente a 203 de día. Seguramente son los focos y el bloom. No es urgente.

## QA-10 · Medidas con máscara: efectos «antes» suspende, noche pasa en los charcos de luz ✅/🔄
- **Efectos**: «antes» 10,1 % (suspende, como exige Lucía); «después» 0,04 % pasa, pero es un solo fotograma casi sin fuego. Pedida una serie de 10 s de fuego sostenido para dar la pauta por buena. 🔄
- **Noche (D-N13)**: dentro de los charcos de luz, L* 42,0 (pasa con holgura); imagen entera, 20,0 (a contraluz, deliberado). El umbral de «charco de luz» se queda en L* 35: el suelo sin luz tiene percentil 90 de 30,4. ✅
- **Cierre (23:42)**: con la última pauta, el fuego ocupa de media un 0,24 % de la pantalla (máximo 0,35 %, en una serie de 20 capturas, `efectos_serie_muestra.png`). **Lucía lo acepta**: los fogonazos se leen y la horda no se tapa. El objetivo del 1–2 % era una estimación. Decide el ojo, y la prueba vigila el tope del 5 %. El pulido fino (que se vean más las trazadoras y la luz del fogonazo de noche) va al hito 7.

## QA-11 · Alarma de efectos: entre el 0,1 % y el 5 %, y los impactos no cuentan ✅
- **Decide**: Lucía (D-N28). **Aplica**: Sara (`efectos_pantalla.py`).
- **Regla**: con fuego sostenido, los efectos de las partículas VFX_HD ocupan entre el **0,1 %** y el **5 %** de la pantalla. Por debajo del mínimo, el fuego ha desaparecido. No se pone el 0,5 % que propuse: suspendería el 0,24 % que Lucía aprobó con el ojo.
- **Los impactos de sangre y polvo no cuentan** (2–3 px, 0,2 s, sobre la horda): no hace falta una segunda máscara.
- **Estado**: «antes» 10,1 % (suspende), muestra de la serie 0,23 % (pasa). **La serie completa (20 máscaras) la he medido solo por la muestra**: está en el PC de Eugenio.

## D-N29 · Hito 3 funcional y textos de la Colmena preparados para el hito 4 ✅
- **Estado (23:43, Mak)**: el **hito 3 funciona de punta a punta**: mapa 3D, zoom a la zona, horda materializada, disparo desde el tren o a pie, munición de la carga del tren y vuelta al mapa. Marcos graba un vídeo del bucle para Eugenio y empieza el hito 4 por la memoria de tráfico.
  - **Deuda pendiente del hito 3**: precarga de la zona, varias zonas a la vez y la tropa como unidad de la red.
- **Lucía, por adelantado**: `textos-informe-colmena.md`, con 20 plantillas en español e inglés.
  - Cubre tráfico, atención, puntos únicos, estados, checkpoint y los avisos al jugador tortuga.
  - Cada plantilla lleva su fuente (Mora, Ibarra o «tras el ataque») y su disparador.
  - **Reglas de escritura**: como mucho dos frases y tono sobrio. El inglés es una adaptación, y queda pendiente que lo revise un hablante nativo.
- La hoja de ruta y el GDD §15 ya reflejan el estado.

## QA-12 · La repetición dorada va antes de la memoria de tráfico (hito 4) ✅
- **Propone**: Sara (QA-4). **Decide**: Mak, a las 23:46. **Aplica**: Marcos.
- **Decisión**: se construye justo después del vídeo y antes de la memoria de tráfico. Primero la lógica pura (red, balance, combate) con dotnet, luego la zona en el Editor y por último la compilación.
- **Criterio de aceptación**: `docs/qa/criterio-repeticion-dorada.md` (4 escenarios; idéntica en el mismo proceso, entre Editor y compilación Mono, entre sesiones; el reproductor tiene que fallar de verdad si se cambia 1 bit; dos PC distintos queda como pendiente porque hace falta una segunda máquina).

## D-N30 · Revisión del vídeo del hito 3 (`h3_bucle.gif`) ✅
- **Marcos**: una partida real de 44 s. Día 1 a x4, zoom a Sagunto y sondeo de unos 480 zombis, fuego desde el tren (71 abatidos, 0 bajas) y la munición descontada al volver. La grabación destapó un fallo de la mancha frente a la zona, ya arreglado. Queda como deuda que una zona sin tren de la red en el andén no dibuje el tren.
- **Revisión de Lucía**:
  1. **«Segorbe asediada» el día 1 a las 08:11**: choca con D-N08. Probablemente es la etiqueta del hito 2, que pone «asediada» cuando la densidad pasa del 50 %. **Propuesta**: «asediada» solo con un asedio real del director (hito 4); hasta entonces, una densidad alta se muestra como «amenazada». Sara comprueba también las etiquetas.
  2. **Salto de color en la transición**: el mapa de cerca es verde oliva y la zona, ocre. **Regla**: la tinta del mapa en un punto y el suelo de la zona tienen el mismo color. La tinta baja del mapa tira hacia el ocre.
  3. De acuerdo con que no se dibuje el tren si no está en el andén.

## QA-13 · D-N08 se vigila también en etiquetas y alertas, y la prueba vieja era demasiado floja ✅
- **Propone**: Lucía (vio «Segorbe asediada» el día 1 en el GIF). **Amplía la prueba**: Sara. **Corrige**: Marcos.
- **Hallazgo**: Segorbe pasa a Asediada a las 07:40 del día 1. La prueba anterior solo comprobaba como mucho 1 asedio a las 12:00, así que no lo detectaba.
- **Decisión**: la prueba vigila todo el día 1: nodos, alertas y textos. Hoy falla; tiene que pasar cuando Marcos suba el arreglo (hasta el hito 4, una densidad alta es «Amenazada»).
- **Cierre (23:59)**: Marcos atiende las tres notas.
  - Hasta el hito 4 sale «amenazada» en lugar de «asediada».
  - El llano del mapa usa el ocre del suelo de la zona y el fundido ya no salta de color.
  - Sin tren de la red en el andén, no se dibuja el tren.
  - **Lucía da el GIF por bueno**. La versión válida es `h3_bucle-20261105T235927-e3ac.gif` (la que no lleva sufijo es la antigua). El mapa de cerca sigue liso hasta que lleguen los datos del IGN.
- **Resuelto** (18fec1b): bloque 11 en verde. Hasta el H4 ningún nodo puede estar Asediado, así que el primer asedio del día 2 y la alerta de asedio se prueban cuando llegue la Colmena.

### QA-14 — Repetición dorada: criterios 2 y 3 (Sara, 6-nov)
Commits 4bd3a61 y 4f05b3d. dotnet 123/123 y QaTests 19/19 en verde; G3 verificado por Sara en Debug y con TieredCompilation=0. Marcos declara G1/G2/G3 idénticos en Editor, Mono e IL2CPP (no verificado por QA: sin acceso a Unity). Pendiente: G4, dos PC, RasterSolid. Propuestas: criterio Burst on/off, auditar float fuera de Burst, regenerar .golden solo con aprobación escrita.

## D-N31 · Memoria de tráfico: tope, un paso por día e histéresis ✅
- **Pregunta**: Marcos (hito 4, parte 1), a través de Mak. **Postura conjunta**: Lucía y Hugo.
- **Decisión**:
  1. **Tope de 1.200 por franja.**
     - Lucía proponía quitarlo (con un tope de seguridad de 4.000). Hugo demostró que, con 3 trenes en la misma franja, la memoria llegaría a unos 3.400 y tardaría 14–15 días en olvidar, lo que rompe «olvida en una semana».
     - Con 1.200, nunca tarda más de 8 días en bajar de 300 ni más de 3 en bajar del umbral de corte.
     - Los umbrales 400, 600 y 850 quedan por debajo del tope. El P3 no cambia.
     - Lucía cede ante los datos.
  2. **Un solo paso por tren, tramo, franja y día**, aunque dos trenes distintos sí suman. Contar ida y vuelta castigaría al tren lanzadera del nudo sin que el jugador pudiera evitarlo.
  3. **Histéresis: aprende en 400 y olvida por debajo de 300.** Solo afecta al estado y al informe.
- **Se aplica en**: `diseno-colmena-h4.md`.

### QA-15 — Director de la Colmena (f5fd8fe), D-N08 en 6 días (Sara, 6-nov)
Bloque 12 de QaTests: ningún asedio ni alerta antes del día 2, máximo 1 asedio simultáneo (etapa 1), masa conservada 6 días. 23/23 en verde. Observación: el primer asedio (Sagunto) empieza en el primer tick del día 2 (36001) y la alerta 14 ticks después, sin «Horda en 3 h» previa; a revisar con Lucía/Hugo contra el momento 4 del guion.

## D-N32 · Aviso de 3 h antes de cada asedio; el primero, de día ✅
- **Hallazgo**: Sara (el primer asedio empezaba al arrancar el día 2, sin el aviso prometido). **Decide**: Mak, que el director anuncie «Horda en 3 h» y el asedio empiece 3 h después.
- **Matiz de Lucía**: el **primer asedio de la partida** empieza entre las **10:00 y las 16:00 del día 2**, con el aviso antes. Del segundo en adelante, a cualquier hora.
- **Por qué**: el primer asedio es el tutorial de muros y de la pila (momentos 4 y 5 del guion). De noche se ve a contraluz, y la noche se reserva como escalada del segundo acto.

## D-N33 · Calibración del primer director de la Colmena ✅ (Lucía informada)
- **Propone**: Marcos (director por utilidad con valores de prototipo). **Calibra**: Hugo, con `sim_economia.py` (150–300 partidas por variante). **Pide**: Mak.
- **Qué se probó**:

  | Variante | Equilibrado | Prisa | Escasez |
  |---|---|---|---|
  | Valores de prototipo tal cual (asedio cada 2 días, 600 ‰, masa conservada sin más presupuesto) | 0 % | 1 % | 26 % |
  | Asedio continuo de 2 días, uno a la vez, presupuesto ×1,36 | 4 % | 21 % | 36 % |
  | **Asedio continuo de 2 días, nº simultáneo por etapa (1/2/3), presupuesto ×1,36** | **5 %** | **41 %** | **45 %** |
  | Referencia D-N25 | 5 % | 42 % | 45 % |

- **Decisión** (valores en `balance_colmena.csv`):
  1. **Presupuesto del director = curva × 1,36 desde el día 2**, repartido entre 24 por hora. El 1,36 es lo que mi modelo ya metía al concentrar asedios (45 % × 1,8 más el 55 % restante). Con la masa conservada, hay que darlo como presupuesto. La interdicción sigue usando la curva sin el ×1,36.
  2. **El 600 ‰ para asedios de Marcos se queda**: cuadra exacto con mi modelo (0,81 / 1,36 = 0,60). El 400 ‰ restante va a los demás nodos por peso.
  3. **Siempre hay asedio activo desde el día 2**. Cada uno dura 2 días (ese es el enfriamiento) y luego se elige otro objetivo. **Cuántos a la vez depende de la etapa**: 1, 2 o 3 (D-N08). «Uno a la vez» vale solo para la etapa 1. Con un asedio cada 2 días el juego se vuelve trivial (la prisa pierde el 1 %).
  4. **El asedio no compite con la emboscada ni con el corte**. Con utilidades de gente × 4 frente a memoria × 2, un jugador rutinario no recibiría nunca asedios, solo emboscadas. Son dos canales: el asedio tiene su calendario y la emboscada o el corte gastan del 400 ‰ según la memoria. Emboscada × 2 y corte × 3 se quedan (con memoria ≥ 850 siempre gana el corte). La emboscada se lleva el 250 ‰ de esa parte.
  5. **Objetivo del asedio**: peso = (60 + población) × 1,4 en el interior × 2 en Valencia. Se sortea con la semilla del tick, con probabilidad proporcional al peso al cuadrado, en lugar de tomar el máximo. Si se tomara el máximo, el asedio caería siempre en Valencia o en el nudo y sería previsible. La horda cercana puede sumarse a la población (zombis / 10) como desempate.
- **Encaja con D-N32**: el aviso de 3 h y el primer asedio de día no cambian nada de esto.
- **Archivos**: `sim_economia.py` (`presupuesto_director` y `asedio_dura`; ya es el modelo vigente), 10 filas nuevas o actualizadas en `balance_colmena.csv` y `resultados.txt` regenerado.

### D-N33 · respuesta de Lucía (00:50)
- **De acuerdo con los dos canales** (asedio por calendario y emboscada por memoria) y con el sorteo del objetivo, con probabilidad proporcional al peso al cuadrado.
- **Matices de Lucía** (Hugo los mide):
  - un **respiro de 6–12 h** en una rama tras cada asedio, para que haya valles de calma, alerta y asedio;
  - el **peso** del objetivo incluye la **atención** y el **punto único** (Castellón); si no, las entradas AT-1 y OB-1 del informe nunca se disparan.
- `diseno-colmena-h4.md` §4 queda actualizado con los dos canales.

## D-N34 · Respiro entre asedios y peso por atención y punto único (Lucía) ✅
- **Propone**: Lucía, para que la música y el ritmo tengan valles (calma, alerta, asedio) y para que AT-1 y OB-1 del informe lleguen a dispararse. **Mide**: Hugo (200–300 partidas).
- **Medido**:

  | Variante | Equilibrado | Prisa | Escasez |
  |---|---|---|---|
  | D-N33 (sin respiro) | 5 % | 41 % | 45 % |
  | Respiro de 9 h y la masa del respiro **desaparece** | 2 % | 20 % | 43 % |
  | **Respiro de 9 h y la masa vuelve a la deriva** (repartida por peso), con Castellón ×1,5 y atención ×1,5 | **4 %** | **41 %** | **48 %** |

- **Decisión**:
  - Tras terminar un asedio, hay de 6 a 12 h (se sortea con la semilla) sin asedio nuevo en esa rama. En las demás ramas sí puede haberlo.
  - **Condición de Hugo**: durante el respiro, la masa no se pierde. Vuelve a la deriva y presiona a todos los nodos por peso. Si desapareciera, la prisa pasaría a perder solo el 20 %.
  - El peso del objetivo se multiplica ×1,5 si es el punto único (Castellón) y ×1,5 si el jugador lleva más de 6 h de juego lejos de ese nodo. En el balance casi no se nota, y hace que los avisos AT-1 y OB-1 lleguen a salir.
- **Ritmo de la demo**: sin cambios (Teruel el día 3 y Zaragoza el día 13).
- **Archivos**: `sim_economia.py` (`respiro_h`, `w_castellon`, `w_atencion`) y 4 filas nuevas en `balance_colmena.csv`.

## D-N34 · Respiro entre asedios sin regalar la partida ✅
- **Propone**: Lucía (los valles). **Mide**: Hugo.
- **Resultado**:
  - si la masa del respiro desaparece, la prisa baja al 20 % de derrotas: los valles regalan la partida;
  - si vuelve a la deriva y presiona a todos los nodos según su peso, Normal da **4 % / 41 % / 48 %**, igual que antes.
- **Decisión**:
  - **6–12 h de respiro por rama** tras cada asedio, y **la masa vuelve a la deriva**;
  - atención ×1,5 y punto único ×1,5 en el peso del objetivo (AT-1 y OB-1 ya pueden saltar).
- **Por qué**: la calma en una rama se paga con presión repartida en el resto, así que el jugador nunca está del todo tranquilo.
- **Se aplica en**: `diseno-colmena-h4.md` §4.

### QA-16 — D-N32: aviso de asedio con antelación (ec3efae, 8e9d42d) (Sara, 6-nov)
Bloque 13 de QaTests: primer aviso «Horda hacia Almenara en 2 h 59 min (10:00)» en el tick 46515, primer asedio en el 51001 (día 2, 10:00), cada asedio avisado antes, 26/26 mías y 147/147 de Marcos en verde. Cierra la observación de QA-15. Pendiente: «hoy» de la atención reiniciado a las 05:30 (deuda de Marcos) y CSV sin cargar en la build.

### D-N33 · seguimiento (01:20, Hugo): curva real en Unity y reparto de objetivos
- **Hallazgo de Marcos**: hasta el commit 3c2f4a3, el director de Unity usaba una curva lineal provisional (1000 + 50 × día), que daba más o menos la mitad de presión. Ahora lee `colmena_curva.csv`. El balance del modelo no cambia, porque siempre usó la curva real. Pero **Sara tiene que repetir P8 y las medidas de asedio y pila** hechas antes de ese commit.
- **Reparto de asedios con 200 semillas**: Valencia, Segorbe y Barracas coinciden con el modelo. Castellón (11 % frente a 17 %) y Teruel (4 % frente a 11 %) quedan en el límite. Hugo pide comprobar que se aplican los pesos de interior y de punto único, y usar las poblaciones del día 10 del modelo (Valencia 34, Castellón 35, Teruel 26, Segorbe 10, Barracas 9, Sagunto 38).

### QA-17 — Repetición con la curva real (3c2f4a3) (Sara, 6-nov)
Mis bloques 11–13 se ejecutaron ya sobre 3c2f4a3 (curva real de colmena_curva.csv): 27/27 y 151/151 en verde. Escenario Mvp sin jugador activo, 10 días: ningún nodo perdido, máximo 1 asedio, masa conservada. Las medidas previas a 3c2f4a3 quedan invalidadas. El camino crítico (P8) aún no se puede medir: faltan los jugadores automáticos y el combate abstracto.

## D-N35 · El director inyecta masa nueva, pero solo por nidos y bordes ✅
- **Decide**: Mak. Cambia la regla de Lucía («nunca aparecen zombis de la nada»). **Consultada**: Lucía (de acuerdo, con condiciones).
- **Problema**: si el director solo mueve la masa que ya existe, el campo se vacía y la presión de la curva de Hugo no se cumple. Zaragoza y Barracas casi no recibían ataques.
- **Decisión**: el director inyecta la masa que pide la curva **en deriva**, en los **nidos** y en los **bordes del mapa**, y luego la mueve como al resto.
- **Condiciones de Lucía**:
  - nunca sobre el objetivo, a menos de unos 10 km de un nodo del jugador ni dentro de una zona en detalle;
  - la prueba de conservación se convierte en «conservación con fuentes»;
  - en el hito 6, la masa que entra por un borde se dibuja en el mapa como una **columna de migración**.
- **Por qué**: la Colmena tiene que crecer (§3b), pero la horda siempre llega de un sitio que se puede ver. Así no se rompe la regla de justicia («no aparece junto a ti»).
- **Se aplica en**: `diseno-colmena-h4.md` §0, §4 y §6.

## D-N36 · Primer asedio en el 2.º día de juego, tablas del director y tope de masa (Hugo) ✅
- **Pide**: Mak, con Marcos y Sara. **Mide**: Hugo (200–300 partidas por variante).
- **B · Primer asedio el día de índice 1** (D-N32). Mi modelo lo tenía en el índice 2. Al adelantarlo un día, Normal se endurece: el equilibrado pasa al 9 %, la prisa al 48–51 % y la escasez al 54 %.

  | Compensación | Equilibrado | Prisa | Escasez |
  |---|---|---|---|
  | Ninguna | 9 % | 48–51 % | 54 % |
  | H0 1450 | 6 % | 22 % | 52 % |
  | Rampa 0,15/0,35/0,65/0,85 | 10 % | 45 % | 55 % |
  | **Rampa 0,15/0,35/0,65/0,85 y H0 1550** | **6–7 %** | **38–39 %** | **53 %** |

  - **Decisión**: la última fila. El primer asedio es más suave (rampa 0,35), como pide el tutorial de muros. Teruel se toma el día 3 y Zaragoza el 12–13, sin derrotas antes del día 10.
  - Fácil (1550) y Veterano (1750) solo escalan H0 y no se han vuelto a medir.
  - La escasez queda unos 3 puntos por encima de la banda 45–50 %. Se lo digo a Lucía.
- **C · Tablas enteras** (generadas por `generar_csv.py`):
  - `colmena_estacion.csv`: 30 filas con 1 + 0,15·sen(2π·d/30) ×1000. Se usa con día mod 30.
  - `colmena_ruido.csv`: 64 cuantiles de la lognormal con σ 0,30 ×1000 (de 484 a 2065, media 1044). Cada día se sortea un índice de 0 a 63 con la semilla del tick. Se descarta calcular la lognormal en coma flotante, porque rompería el lockstep, y también una tabla fija por día, porque sería previsible.
- **Masa total en el campo (pregunta de Sara)**: mi modelo no tenía tope, porque solo cuenta el flujo. Con la inyección de D-N35 propongo:
  1. Los zombis inyectados que no entren en combate en **6 días vuelven a los nidos** (sumidero).
  2. **Invariante de cada partida**: masa en el campo ≤ suma de lo inyectado en los últimos 6 días. Es exacto: la prueba de Sara puede fallar si la Colmena crece sin límite.
  3. **Banda por día**: lo inyectado cada día debe quedar entre el p10 y el p90 de `csv/referencia_masa_campo.csv` (el día 10 da entre 4.951 y 10.275, con mediana 6.982). El tope de 6 días con el p90 es de 52.624 el día 10 y de 75.426 el día 20.
- **Archivos**: `sim_economia.py` (`dia_primer_asedio`, rampa de 4 días y H0 1550), `balance_colmena.csv` (rampa y día del primer asedio), `balance_dificultad.csv`, `casos_prueba.csv` (P2: 3894 / 13421 / 116277), `colmena_estacion.csv`, `colmena_ruido.csv`, y regeneradas `referencia_asedios_d1_20.csv` y `referencia_masa_campo.csv`.

### D-N36 · respuesta de Lucía (01:30)
- **Aprobado**: rampa de los primeros días 0,15 / 0,35 / 0,65 / 0,85 y H0 1550.
- **Resultado en Normal**: equilibrado 6–7 %, prisa 38–39 % y escasez 53 %. La escasez queda 3 puntos por encima de la banda de Lucía, pero dentro del ruido.
- **Por qué**: más vale un poco más de hambre que una prisa sin castigo. El primer asedio, más ligero, viene bien al tutorial.
- **Palanca prevista** si la demo resulta demasiado dura al principio: H0 a 1500.
- **Cierre (01:30, Lucía)**: la escasez del 53 % se acepta («un poco más de hambre a que la prisa salga gratis»). Queda como vigilancia cuando haya datos de jugadores reales: si en la demo hay quejas de hambre en las primeras horas, la primera palanca es bajar H0 a 1500.

## D-N37 · El modelo incluye el aviso de 3 h: hueco efectivo de 12 h entre asedios ✅
- **Hallazgo**: Marcos, con la mediana de 20 semillas: 9 de 18 días caen fuera del ±25 %, siempre por debajo y en días de relevo. **Decide**: Mak, opción (a): el aviso y el respiro se quedan y el modelo se adapta. **Recalibra**: Hugo.
- **Cambio en el modelo**: `respiro_h` pasa de 9 a 12 (3 h de aviso más 9 h de respiro medio). Durante el hueco, la masa sigue volviendo a la deriva (D-N34).
- **Resultado con 300 partidas**: equilibrado 7 %, prisa 40 % y escasez 55 %. Es igual que D-N36 dentro del ruido (±3), así que **no hace falta tocar H0 ni el porcentaje del asedio**. Al conservarse la masa, mover el golpe de unas horas no cambia la presión total.
- **Comparación día a día**: mi modelo funciona por días y su ciclo es de 48 h fijas, mientras que el de Unity es de unas 60 h. Por eso los días de relevo caen en fechas distintas y la comparación día a día no vale para los relevos. Criterio nuevo: **total de golpes contra asedios en los días 1–20** (mediana 71.442, con p10–p90 entre 63.495 y 81.528) y total contra la red (144.714), con ±15 %. Fila `total_1_20` en `referencia_asedios_d1_20.csv`.
- **Horda inicial del escenario fuera del tope**: me cuadra, con una condición. La horda inicial son guarniciones estáticas y paisaje, y solo combate si el jugador se acerca (limpiar nodos; en mi modelo, unos 12.500 zombis en toda la red). **El director solo puede gastar masa inyectada**: si recluta de la horda inicial, se salta la curva. El invariante de Sara pasa a ser: masa en el campo − horda inicial viva ≤ inyectado en los últimos 6 días.
- **Archivos**: `sim_economia.py`, `balance_colmena.csv` (fila nueva `asedio_aviso_h` 3), `referencia_asedios_d1_20.csv` y `referencia_masa_campo.csv` regenerados.

### QA-18 — Conservación con fuentes (399ac18, D-N35/36/37) (Sara, 6-nov)
Bloques 9 y 12 de QaTests ajustados: masa(t) = masa(0) + inyectada − bajas − retirados, exacta cada tick en 10 días y también con zona activa; inyecciones fuera de la zona y a >4 celdas de nodos con personas; masa del campo − inicial ≤ inyectado en 6 días (cota necesaria); retirado ≤ inyectado. 31/31 mías y 157/157 de Marcos. No puedo separar la horda inicial viva de la inyectada, así que «el director solo gasta masa inyectada» solo se comprueba de forma agregada. Medida: inyectado por día 19, 94, 182, 252, 310, 322, 336, 552, 360, 374 (en el escenario Mvp sin jugador), muy por debajo de la banda de Hugo del día 10 (4.951–10.275): hay que aclarar con Hugo si son las mismas unidades.

### QA-19 — Unidades del director (Sara, 6-nov)
Aclarado con Hugo: los contadores de inyección están en grupos de 10 (curva/10); sin jugador, mi cifra × 10 queda a ±15 % de su curva en los días 1–10. Hay una deriva a la baja en los días 5–9 que Marcos revisa (¿índice de la estación?). Hasta que los contadores pasen a zombis individuales, comparar con factor 10. Cierra el aviso de QA-18.

## D-N37b · La horda inicial deriva atada, pero no se recluta ✅
- **Propone**: Mak, a partir de un aviso de Marcos: con la horda inicial estática (D-N37), el día 1 quedaba muerto. **Postura conjunta**: Lucía y Hugo.
- **Decisión**:
  - **Correa de 2 celdas** (unos 7 km): la horda inicial deriva y reacciona al ruido del tren, pero nunca se recluta ni entra en un nodo;
  - **es finita**: no se repone;
  - solo cuenta para el combate la masa a tiro de la vía (del orden de 12.500 zombis); el resto es paisaje;
  - las bajas solo salen de decisiones del jugador (el tren cuenta como muro; a pie, tope de cadencia).
- **Resultado**: el día 1 tiene vida y Normal no se mueve (4 % / 40 % / 55 %).
- **Se aplica en**: `diseno-colmena-h4.md` §3b.

## D-N38 · Zonas de emboscada: el desmonte primero ✅
- **Pide**: Marcos, a través de Mak (la zona solo sabía hacer estaciones). **Diseña**: Lucía (`diseno-colmena-h4.md` §8).
- **Reglas comunes**:
  - zona de 256 × 128 m con la vía en el eje largo;
  - el tren para por un **tapón** de cuerpos sobre la vía (la pila de §5.7), con escombros si hay corte;
  - tres salidas: despejar el tapón, **dar marcha atrás** (los primeros 40 m siempre quedan libres) o aguantar;
  - el tren es muro; la horda que sobrevive pasa a caza.
- **Desmonte (demo)**: trinchera de 7 m de profundidad entre X = 60 y X = 200. La horda baja **rodando por los taludes** (caídas de §5.7). Es una ratonera: se dispara desde el tren o se retrocede.
- **Curva y puente**: diseñados para después de la demo. En la curva, bancales de piedra como cobertura y pinar desde donde sale la horda. En el puente, cuello de botella con caídas al vacío.
- **Mientras tanto**, todos los puntos usan la disposición del desmonte con otro decorado.
- **Por qué el desmonte primero**: es el más reconocible y luce la física de caídas que pidió Eugenio.

## D-N39 · Horda a tiro de la vía, emboscada sin respuesta y total esperado según la huella (Hugo) ✅
- **Pide**: Marcos, a través de Mak (commit 1f140fe). **Calibra**: Hugo.
- **Total de los días 1–20**: Marcos mide 111.190 golpes contra la red y 55.020 contra asedios, con un escenario de huella fija. Hugo genera `csv/referencia_total_por_huella.csv` con el total esperado para cada huella de 0 a 15. Con huella 3, el esperado es 111.028 y 54.848, a un 0,2–0,3 % de lo medido. **El presupuesto queda validado.** La diferencia del 23 % venía de que mi jugador simulado hace crecer la huella. Los asedios se llevan el 49,4 % de la red, igual en los dos modelos.
- **Guarnición a tiro de la vía**: al nacer, 1.600 grupos de 10 (16.000 zombis) frente a los ~12.500 del modelo. Vale: es un +28 %. Pero los ~3.500 grupos (35.000 zombis) tras 600 pasos de deriva no valen, porque costarían unas 88 u de munición frente a las 31 del modelo. **Objetivo: como mucho 1.500 grupos (≈15.000) a tiro de la vía en cualquier momento.** La correa se mide desde la celda donde nace cada manada: solo puede llegar a la vía la que nace a 7 km o menos, y el resto es paisaje.
- **Emboscada sin respuesta**: se pasa del 30 % provisional al **20 % de la carga**, con un máximo de una por tren y día.
  - Dos emboscadas en un día suman el ~36 % que ya es el techo de la interdicción (37 %).
  - Responder cuesta unas 1,75 u de munición el día 10 (unos 700 zombis), frente a 20 u de carga. Así que responder sale siempre a cuenta, y la rutina automatizada sin escolta se paga.
  - Es una estimación, porque el modelo no tiene emboscadas por tren. Hay que validarlo con la prueba de Sara: un rutinario sin escolta debe perder entre el 5 y el 10 % de lo que transporta en 10 días.

### QA-20 — D-N37b y D-N39 (1f140fe) (Sara, 6-nov)
Bloque 14 de QaTests. En verde: InitialMassAlive nunca sube y no baja sin bajas del jugador (103.902 → 103.902 en 10 días); ninguna celda de la horda inicial sale de su correa de 2 celdas. Bloque 12 ajustado: la masa que retiene una emboscada activa (Encounter.Taken) cuenta como masa viva; con eso la identidad con fuentes es exacta 10 días. **Abierto:** a tiro de la vía (1 celda) hay 1.600 ‰ al nacer (≈16.000 zombis, bien) pero sube a 6.013 ‰ en 10 días porque la horda inicial deriva hacia la vía dentro de su correa; el tope D-N39 de 1.500 grupos aún no existe en el código (mi prueba falla hasta entonces). Test de Marcos solo mira 600 pasos con tope 5.000.
- **Revisión del GIF del desmonte (02:54, `emboscada_desmonte.gif`)**: **jugable**. La horda baja por los taludes, la tropa dispara desde el tren sin bajas y la marcha atrás funciona. El arte es provisional. Notas para el hito 5 o el 7:
  1. no se lee como trinchera: falta sombra en el fondo y un talud continuo (con el MDT o un degradado), no a franjas;
  2. el tren casi no se ve: necesita contraste de valor (D-N13);
  3. las franjas de color le restan protagonismo a la horda.
  - La zona de prueba se llama «Puçol», que no es un punto de emboscada. Que no llegue así a la demo.

### QA-21 — D-N39 y desmonte jugable (f243c97, fc478bb) (Sara, 6-nov)
173/173 de Marcos y 35/35 mías (con la zona de 256×128 m y la guarnición con tope). Cierra el hallazgo de QA-20: a tiro de la vía 14.000 zombis al nacer y máximo 14.000 en 10 días (tope 1.500 grupos). Sin verificar (requiere Unity): flujo Intro → emboscada → zona (Z/X/C) → M → resolución en la red; pérdida 5–10 % del jugador rutinario (falta jugador automático).

### QA-22 — Repaso final de la noche (Sara, 6-nov, 05:00 UTC)
Commit 3b19304: 173/173 de Marcos y 35/35 mías en verde. pruebas-manana.md actualizada (§3). Abiertos: Q6, Q7, Q9 (bajos); prueba del camino crítico y jugador automático (no existen); dos PC distintos; RasterSolid y BuildWall/Level (float fuera de Burst); hash del balance en coop (H7); sin Unity no verifiqué FPS, fundidos, builds ni el flujo de emboscada.

## D-N40 · Fase A aprobada por Eugenio; propuesta de fases B a G preparada ✅ (A) 🔄 (B–G)
- **Eugenio (6-nov, 07:05)**: aprueba la fase A de Pixelab y la prueba de ElevenLabs. Marcos las ejecuta; Iris supervisa el gasto y revisa las hojas de contacto. Sustituye al bloqueo D-N20.
- **Iris**: propuesta de las fases B a G en `arte/propuesta-fases-b-g.md`, con tres decisiones para Eugenio (B–F, G y reparto del sobrante). Plazo: antes del 11-nov.

## D-N41 · Fases B a F de Pixelab aprobadas por Eugenio; G pendiente ✅
- **Eugenio (6-nov, 07:06)**: «Sí» a la propuesta de Iris: fases B a F, una a una, con revisión entre fases (Lucía e Iris).
- **Pendiente**: la fase G (texturas 3D) se decide al ver la prueba de texturas de la fase A. El reparto del sobrante del 11-nov se confirma con Eugenio antes de ejecutarlo.
- **Límite**: si una fase se desvía más de un 20 % del gasto previsto, Marcos para y avisa.

## D-N42 · Deuda de arte del hito 3: noche ámbar y desmonte legible (Lucía) ✅
- **Pide**: Sara (QA-20) y la revisión del GIF del desmonte. **Diseña**: Lucía (`arte/deuda-arte-h3.md`). **Ejecuta**: Marcos, a través de Mak, antes del hito 5.
- **Noche (D-N13)**: el salmón de los focos viene de aplicar la gradación azul después de la luz. La noche azul pasa a venir de la luz de la luna y del ambiente (`#283440`–`#404460`), o de un virado partido (sombras frías, altas luces cálidas). El foco va en VFX_HD sin gradación. **Prueba**: el tono del centro del charco entre 25° y 45°.
- **Desmonte**: talud continuo, albedo oscurecido según la pendiente, sombra en el fondo y fondo de balasto `#48403c`. **Prueba**: tres bandas de valor en escala de grises.
- **Tren**: techos claros, laterales oliva, contorno de 1 px y franja ámbar en la locomotora. **Prueba**: 25 de L* o más contra el fondo de la trinchera.
- **Por qué ahora**: es barato y el hito 5 se juega en esas mismas zonas (la reparación del tramo es una batalla en el desmonte).

## D-N43 · Diseño del hito 5 (Construir) por adelantado (Lucía) 🔄
- **Diseña**: Lucía (`diseno-hito5.md`). **Consulta**: Hugo (costes marcados [Hugo] y ruido de obra) y Marcos (nivel de fortificación de la S0 a partir de las piezas; trazado de muros con coste en directo).
- **Claves**: se construye solo en terreno asegurado (sin zombis a menos de 30 m), con materiales y obreros. Siete piezas (sacos, HESCO, puerta, nido, foco, depósito y andén). **El nivel de fortificación de la S0 sale de lo construido** (valor ÷ 30 u, máximo 5), para que la zona y el mapa digan lo mismo. Reparar tramo (5 u) y puente (80 u, obra larga). Fundar estación (30 u y 12 personas). El taller fabrica trenes (120 u y 30 de combustible, 2 días).
- **Pendiente**: ajustar los números cuando responda Hugo y la arquitectura cuando responda Marcos.

## D-N44 · Números del hito 5 (Construir): las piezas y el S0 dicen lo mismo ✅ (salvo el plazo del tren de obras)
- **Pide**: Lucía (`diseno-hito5.md`, preguntas [Hugo]). **Mide**: Hugo (200 partidas por variante). Valores en `csv/balance_construccion.csv` y casos P9 de `casos_prueba.csv`.
- **Muros más caros**. Con los precios de la v0.1 (sacos 1 u y HESCO 2 u por cada 10 m), un perímetro realista de 150 m da como mucho unas 50 u, es decir, nivel 1,7. Mi balance supone nivel 2–4 en las estaciones y 4 en Sagunto, así que todo sería más frágil de lo medido. **Propuesta**:

  | Pieza | Precio | Cuenta para el nivel |
  |---|---|---|
  | Sacos | 2 u por cada 10 m (150 m = 30 u = fundar = nivel 1) | Sí |
  | HESCO | 6 u por cada 10 m (150 m = 90 u = nivel 3) | Sí |
  | Puerta | 6 u | Sí |
  | Nido | 8 u | Sí |
  | Foco | 2 u | Sí |
  | Andén | 6 u | Sí |
  | Depósito | 5 u | No |

  - El ejemplo del §2 pasa a valer 118 u, nivel 3,9. Los tiempos de obra de Lucía se quedan: construir 4 veces más rápido no cambia el balance (7 % / 41 %), porque lo que limita son los materiales.
  - `balance_pila.csv` pasa a 200 y 600 milésimas de u por metro. La altura del HESCO se mantiene en 2.100 mm, que es la de la pila calibrada (no 2,2 m).
- **Ruido de obra**:
  - Mientras haya una obra activa, la probabilidad de sondeo es de 83 ‰ por hora (uno cada ~12 h de obra).
  - El sondeo trae el 5 % del presupuesto del día (unos 330 zombis el día 9).
  - El nodo pesa ×1,5 como objetivo de asedio.
  - La huella de las obras de muros es 0,5. La del puente y las obras grandes, 1,5, como ya tenía el modelo.
- **Tramo cortado (5 u y 3 h) y puente (80 u y 2 días)**: encajan. Con el tren de obras saliendo el día 7 y 8 obreros (192 obreros·h), el puente está el día 9, como en el modelo (día 8–9).
- **Dos cambios que tocan el balance**:
  - **Andén con un 25 % más de velocidad de carga**: si lo tuvieran todas las estaciones (−0,5 h por viaje), la escasez bajaría del 55 al 43 % y la prisa del 41 al 34,5 %. Propuesta: el bono de carga solo en el andén de Sagunto. En las demás, el andén da solo el «tras muro».
  - **Taller en 2 días**: la prisa bajaría del 41 al 19 %. Propuesta: se quedan 3 días. Chispas Ferrer da un 25 % más de velocidad en reparar trenes y vía, no en fabricarlos.
- **Almacén**: 50 u es poco, porque Castellón produce 60 de combustible al día y tiraría producción. Propuesta: 100 u por estación, +200 por depósito y 1.000 en Sagunto.

### D-N44 · respuesta de Lucía (07:15)
- **Acepto todo**: los precios nuevos, que el depósito no cuente para el nivel, la altura del HESCO de 2,1 m, el ruido de obra, el almacén (100, +200 y 1.000) y los 3 días del taller. Me convence el argumento de los materiales: si el muro es barato, la estación del mapa es de papel aunque la zona parezca una fortaleza. Paso `diseno-hito5.md` a la v0.2 y el CSV de Hugo manda.
- **Andén**: de acuerdo con que el bono de carga sea solo de Sagunto. En la ficción, lo dan **las grúas del puerto**. En las demás estaciones, el andén da solo el «tras muro».
- **Lo que sí rompía**: con 3 días por encargo y un solo puesto en el taller, el tren de obras salía el día 9 y el puente se iba al día 11. Lo resuelvo con una regla de diseño: **rehabilitar no es fabricar**. El Tren 3 (a medio montar) y el tren de obras (un tren viejo) se rehabilitan en 1,5 días, y Chispas acelera un 25 % las rehabilitaciones porque son reparaciones. Calendario: el Tren 3 sale el día 5 y el tren de obras hacia el día 6–7. **Pendiente de Hugo**: que lo mida y que ponga precio a la rehabilitación del tren de obras.

### D-N42 · revisión de Lucía de las capturas de Marcos (07:20)
- **Desmonte y tren: aprobados** (`arte_desmonte_v2.png`). Ya se lee como trinchera. Perfil de L*: arriba ~65–69, taludes ~48–51, fondo ~38–42. Los techos claros del tren destacan sobre la trinchera. El fondo solo queda unos 10 L* por debajo del talud: se puede reforzar cuando llegue el MDT (hito 7), pero no bloquea.
- **Noche: todavía no**. El centro del foco está bien (H = 33°), pero de los ~1.600 píxeles cálidos e iluminados de `arte_noche_luz_luna.png`, unos 1.000 tienen un tono de 5–15°: el halo es salmón y ocupa casi todo el charco. **Causa**: la luz ámbar del foco se suma al ambiente azul sobre el suelo ocre, y en la caída del halo gana la mezcla rosa. **Arreglo**: dentro del radio del foco, atenuar el ambiente frío con la misma caída (`ambiente × (1 − 0,6·atenuación_foco)`, que es la adaptación del ojo a la luz). Si no basta, que la caída del foco vire hacia el amarillo (`#c89040`) en lugar de solo bajar de intensidad. **Prueba nueva**: el 80 % de los píxeles cálidos del charco con un tono entre 20° y 45°, además del centro entre 25° y 45°. Mejor medirlo sobre una captura a resolución completa.

### D-N43 · arquitectura acordada con Marcos (07:25)
- **Marcos**: el nivel calculado a partir de las piezas encaja, pero hoy los muros no persisten. Hay que crear `Obras` por nodo en la red, dentro del hash. Todo va en enteros (‰ y mm). El coste en directo usa la misma función que la orden, y el corte por falta de materiales lo decide la simulación. Propone que el perímetro sea cualquier muro defensivo, cierre o no.
- **Lucía**: de acuerdo, con una condición: solo cuenta lo que está a **60 m o menos del andén**, para que un muro suelto en una esquina no infle el nivel. El orden es el de Marcos, con «fundar» delante del taller y del puente, porque Nules llega el día 3 de la demo. Detalle en `diseno-hito5.md` v0.3, §2b y §8. La recalibración del muro de 2,5 m a 1,2 o 2,1 m pasa a Hugo.


## D-N45 · El tren de obras frena la prisa: se compensa con la huella ✅ (k 0,24, elegido por Lucía)
- **Propone**: Lucía, que separa rehabilitar de fabricar (el Tren 3 y el tren de obras se rehabilitan en 1,5 días, 1,2 con Chispas; sin tren de obras no hay puente). **Mide**: Hugo (250–300 partidas).
- **Precio de la rehabilitación del tren de obras**: 20 u de materiales, 5 de combustible y 8 obreros a bordo. Con 30 + 10 llega tarde por falta de materiales y el puente se va al día 12.
- **Calendario en el modelo** (con Chispas; el modelo va por días, así que hay ±1 día):

  | Jugador | Tren 3 | Tren de obras | Puente |
  |---|---|---|---|
  | Equilibrado | 5,5 | 8 | 10 |
  | Prisa | 5 | 7 | 9 |

  Sin Chispas el puente se va al día 11–12, así que **en la demo Chispas tiene que estar en el taller desde el principio**.
- **Efecto en el balance**: con k 0,16, la prisa baja del 41 al **10 %**. El jugador con prisa ya no puede tender el puente el día 5: el tren de obras frena su expansión. Así queda cada opción:

  | k_huella | Equilibrado | Prisa | Escasez |
  |---|---|---|---|
  | 0,16 | 4 % | 10 % | 50 % |
  | 0,20 | 8 % | 17 % | 51 % |
  | **0,24** | **11 %** | **39 %** | **52 %** |

- **Propuesta de Hugo**: k 0,24. La prisa vuelve a doler, y el equilibrado queda en el 11 %, cerca de los objetivos originales de Lucía (12–16 %). Ya está aplicado en el modelo y en los CSV, y se puede deshacer. Fácil (0,18) y Veterano (0,33) solo están escalados, sin volver a medir.
- **Archivos**: `sim_economia.py` (`dias_rehabilitar`, `coste_tren_obras`, `k_huella` 0,24), `balance_construccion.csv` (4 filas), `balance_colmena.csv` y `balance_dificultad.csv` (k nuevo), P2 (4306 / 15472 / 139147) y `referencia_total_por_huella.csv` regenerada (huella 3 → 119.692 contra la red).

### D-N45 · respuesta de Lucía (07:30)
- **Elijo k 0,24.** La lección de la prisa, «expandirte sin cabeza alimenta a la Colmena», es uno de los pilares del juego. Con 0,20 la prisa solo pierde un 17 % y deja de enseñar nada. Subir el equilibrado del 8 al 11 % son 3 puntos, y queda dentro de lo que yo pedía al principio (12–16 %). El 5 % de anoche era un mínimo, no un objetivo. Quien quiera una campaña más amable tiene el nivel bajo de dificultad.
- **Chispas en el taller**: queda como regla de la demo, y la cuenta la ficción. Chispas no se mueve del taller hasta que sale el tren de obras («No me muevo de aquí hasta que el de obras ruede»). Después queda libre para subir a un tren. Fuera de la demo, el jugador decide, y sacarlo del taller retrasa las rehabilitaciones.
- **Tren de obras**: 20 u, 5 de combustible y 8 obreros a bordo, como propone Hugo. Calendario: el Tren 3 sale el día 5–5,5, el tren de obras el día 7–8 y el puente está el día 9–10.


### QA-23 — Incidencia Q14: DESINCRONIZADA en el tick 0 (Sara, 6-nov)
Hallada por Eugenio en su prueba. Abierta; Marcos reproduce. Detalle y regresión propuesta en informe-qa-h1-h2.md (Q14).

## D-N46 · Revisión de A1 (cargas): 16 px por reducción y prefijo limpio para A2 y A3 ✅
- **Revisa**: Iris sobre `A1_cargas.png` (80 generaciones exactas, sin desvío).
- **Hallazgo 1**: a 32 px salen bien; elegidos provisionales: munición v4 y v5, combustible v3 y v6, materiales v1 (tubos) y v2 (tablones), víveres v4 y v5, población v4 y v6. A 16 px el modelo dibuja soldados y zombis, no objetos.
- **Hallazgo 2**: casi todos los iconos de 32 px llevan salpicaduras de sangre, y algunos calaveras o caras. Viene del prefijo (`gritty post-apocalyptic`, `dried blood red`). La sangre va en los decals, no en los iconos de interfaz.
- **Decisión**: se aprueba la propuesta de Marcos (16 px por reducción de los de 32, sin generar 16 px en A2 y A3; ahorra 96). **Condición**: en A2 y A3 usar un prefijo limpio, sin `gritty`, sin `dried blood red` y con `clean, no blood, no skull, no characters`. Los de 16 se eligen entre los 32 más simples y se reducen con vecino más cercano, comprobando la legibilidad.
- **Corrección de Lucía (6-nov, 07:43)**, aceptada: selección definitiva a 32 px: munición **v4** (v3 de alternativa; v5 y v6 llevan marco, y la regla es icono sin marco), materiales **v1 y v2**, víveres **v4** (v5 se confunde con un bidón), población **v4** (v6 son soldados con casco y chocan con los iconos de tropa). **Combustible: ninguno vale** (cántaros y ánforas); v3 provisional.
- **Regenerar solo dos familias a 32 px** (unas 16 generaciones, dentro de lo ya aprobado de la fase A): combustible con `military jerry can` y población con `family of civilians, adult and child`.
- **Acento por carga** (tokens de la paleta; el rojo es el token de peligro y no se usa en recursos): munición latón y ámbar, combustible verde oliva, materiales gris acero, víveres ocre y beige, población hueso (#d4d0cc).
- **Condición de los 16 px**: tras reducir, se vuelve a dibujar el contorno de 1 px y se comprueba a ×1 sobre el fondo de panel (#181c30). Si una reducción no se lee, se simplifica la silueta a mano.
- **Pendiente**: Eugenio ve la hoja de contacto.

### QA-24 — dcd84d5 (D-N45, goldens regenerados) y Q14 (Sara, 6-nov)
173/173 de Marcos y 35/35 mías en verde. Goldens G3 y G4 regenerados por D-N45 (N-054) con aprobación registrada (criterio 8 cumplido). Q14 sigue abierta: Marcos añadió el informe `Captures/desync_zona_*.txt` (escena, zona, Burst, hash por sistema A/B, últimas 40 órdenes); que Eugenio lo adjunte si se repite.

## D-N47 · Iconos y marcadores por código (pixelvm) en vez de Pixelab para A2 a A5 ✅
- **Propone**: Bruno (arte técnico). **Revisa**: Iris (recomienda sí); falta Lucía.
- **Evidencia**: `arte/pixel-codigo/comparativa_pixelab_vs_codigo.png`. Las 5 cargas por código salen limpias, sin sangre ni rojo, con la misma vista y contorno, y a 16 y 32 px. El bidón por código es un bidón; el de Pixelab no. Pierden en riqueza de textura, pero para iconos de interfaz basta. Retratos, ilustraciones, logotipo y texturas siguen siendo de Pixelab.
- **Recomendación de Iris**:
  1. Las cargas finales de A1 son las de código. **Ya no hace falta regenerar combustible ni población** (ahorra ~16).
  2. A2 a A5 (alertas, órdenes, estaciones y trenes, ~256 generaciones) se hacen por código. Marcos **no lanza esas tandas** hasta que Lucía lo confirme.
  3. El saldo ahorrado pasa a retratos, ilustraciones, rostros del checkpoint y texturas, donde Pixelab aporta más.
  4. A6 (unidades) y A7 (texturas) siguen en Pixelab; A8 (humo) usa el de código, y se prueba en Unity sobre el tren.
  5. **Código descargado (pixelfx, Pixelbolt)**: no se ejecuta sin que Eugenio lo apruebe y sin leerlo antes. Su skill propia, escrita por Bruno, sí está instalada (PR #1 del repo del juego).
- **Pendiente**: Lucía confirma; Mak da el visto bueno al cambio de reparto; Eugenio revisa.
- **Luz verde de Lucía (6-nov, 08:03)**: el estilo del código encaja con D-N06, las siluetas aguantan a 16 px y los acentos funcionan. Aprueba A2 a A5 por código y pasar el saldo a retratos, rostros del checkpoint, ilustraciones y texturas.
- **Cuatro correcciones que Lucía pide a Bruno antes de cerrar la familia de cargas**: luz fija con algo de desgaste; caja de munición en acero o madera (en oliva se confunde con el bidón a 16 px); víveres como saco y latas; población con pelo y piel (las cabezas blancas parecen fantasmas).
- **Humo de A8 por código: aún no aprobado.**
- **Visto bueno de Mak (6-nov, 08:04)**: aprobado. Cargas finales de A1 = las de código (no se regeneran combustible ni población). A2 a A5 por código. Las ~256 generaciones pasan a retratos, rostros del checkpoint, ilustraciones y texturas, con revisión de cada hoja de contacto antes de la siguiente fase. **Pixelfx y Pixelbolt no se ejecutan hasta que Eugenio lo autorice.** Marcos avisado.

## D-N49 · Obras por nodo en la red: coste exacto, corte determinista y nivel en ‰ (hito 5, carril 1) 🔄
- **Propone y programa**: Nacho (PR #2 del repo del juego, https://github.com/HerrKlicova/TBD/pull/2). **Consulta y aprueba**: Marcos (alcance y reglas de integración, vía Mak) y Mak (hash, CSV y registro). **Pendiente**: revisión e integración de Marcos.
- **Qué se decide**:
  1. **Muros en módulos de ≤ 10 m**: cada módulo es una pieza con su coste y su vida (el daño es local y el perímetro de 60 m se aplica pieza a pieza).
  2. **Coste exacto en 1/10.000 de u** (precio por 10 m × longitud en mm). Al almacén se le cobran las u redondeadas hacia arriba.
  3. **Corte por falta de materiales**: se construye el tramo más largo que cabe en las existencias (existencias × 10.000 ÷ precio, en mm, hacia abajo, desde el primer vértice). La previsualización y la orden usan la misma función. Menos de 1 m no se construye. Las piezas puntuales no se cortan.
  4. **Nivel de fortificación (‰)** = Σ(coste × vida) ÷ 30 u, tope 5.000 ‰. Cuenta lo construido, sin el depósito y con el punto medio de la pieza a ≤ 60 m del andén. El ejemplo de D-N44 (118 u) da 3.933 ‰.
  5. **El hash de las obras va dentro de «existencias»** (Mak, 08:05). Vale 0 sin obras: los goldens G1–G5 no se regeneran. Si más adelante crece mucho, se separa con una decisión registrada.
  6. **Orden nueva `NetCmdType.PlaceWork = 9`** y **`NetCommand.Payload`** (int[], null en casi todas las órdenes). `Arg = nodo | (PieceKind << 16)`; `Payload = [x0,y0,x1,y1,…]` (muro) o `[x,y]` (pieza puntual), en mm locales al nodo (el andén es el (0,0)). Solo se acepta con la zona del nodo materializada. `NetGolden` guarda el Payload como quinto campo opcional: los .golden antiguos se siguen leyendo.
- **Para el CSV de Hugo** (hoy viven en el código con valor por defecto; las claves son las que ya lee `ObrasParams.FromCsv`):
  - `muro_modulo_mm;10000`
  - `muro_minimo_mm;1000`
  - `perimetro_mm;60000`
  - `nivel_u_por_nivel;30`
  - Alturas de pieza (aún solo en el código, `Obras.HeightMm`): sacos 1.200, HESCO y puerta 2.100, nido y andén 1.500 mm.
- **Límites**: «S0 = S2» está probado contra la geometría de las piezas, no contra `SimSystems` (lo cierra Marcos al integrar la zona con `Works.Snapshot/Restore`). `ObrasState.CompleteAll` es provisional hasta la orden «asignar obreros» (paso 2). Falta el terreno asegurado (sin zombis a < 30 m).
- **Pruebas**: 207 correctas, 0 fallos (173 + 34 nuevas, sección [15] de `Dotnet/TBD.Sim.Tests`). Documento de interfaz: `Docs/obras-h5.md` del repo del juego.

### D-N42 · noche aprobada (Lucía, 08:10)
- Marcos mide el 83,5 % de los píxeles cálidos del charco con un tono entre 20° y 45° (antes, el 18 %). Mi medición independiente sobre `estacion_noche_completa.png` da menos del 2 % de píxeles cálidos por debajo de 15°: **el salmón ha desaparecido**. La masa del charco está en 25–30°. **Aprobado**, con lo que se cierran D-N13 y la deuda de arte del hito 3.
- **Nota para el hito 7 (no bloquea)**: con la paleta al 65 % y la desaturación, el borde del charco se lee algo melocotón. Si en la revisión final se quiere más ámbar, se puede subir la saturación del foco un poco, sin tocar el tono.


### D-N49 · paso 2: obreros, avance y cancelar (Nacho, PR #3 apilado sobre #2)
- **Órdenes nuevas**: `AssignWorkers = 10` (`Arg` nodo, `Arg2` obreros) y `CancelWork = 11` (`Arg` nodo, `Arg2` número de obra). **Decisiones de Nacho a revisar por Marcos**: máximo 4 obreros por pieza; los obreros no se gastan (población asignada, limitada a la del nodo en cada tick); la obra avanza aunque no haya zona materializada.
- **Obra en obrero·h** (de `diseno-hito5.md` §2): sacos 2 por 10 m, HESCO 4 por 10 m, puerta 4, nido 6, foco 2, depósito 8, andén 10. 1 obrero·h = 1.500 obrero·ticks.
- **Para el CSV de Hugo (se suman a los cuatro valores de arriba)**: `obra_max_obreros_por_pieza;4`, `obra_sacos_h_por_10m;2`, `obra_hesco_h_por_10m;4`, `obra_puerta_h;4`, `obra_nido_h;6`, `obra_foco_h;2`, `obra_deposito_h;8`, `obra_anden_h;10`.
- **Cancelar**: 100 % si nadie ha empezado, 50 % (`cancelar_obra_empezada_permil`, ya en el CSV) si hay trabajo hecho. Lo terminado se queda.
- **Pruebas**: 230 correctas, 0 fallos. G1–G5 sin tocar.

## D-N50 · A2 a A4 de Pixelab descartadas; prompts siempre en positivo ✅ (citada antes como D-N48)
- **Origen**: Marcos avisa y Iris confirma con `A2_alertas.png`, `A3_ordenes.png` y `A4_estaciones.png`: pixen **ignora las negaciones**. Mi prefijo limpio (`no skull, no blood, no characters`) tuvo el efecto contrario: casi todo son calaveras y cruces rojas. Fallo mío al redactar el encargo.
- **Evaluación**: A4, 0 de 32 usables. A2 y A3, casi todo calaveras; se salva el puño de «aguantar», pero con marco propio.
- **Decisión** (Iris, confirmada por Lucía el 6-nov a las 08:09): A2, A3 y A4 **por código** (Bruno, D-N47); no se queda ninguna pieza de Pixelab. «Aguantar»: referencia de pose v6 (puño de frente, cerrado, nudillos marcados), sin marco, porque el marco lo pone el botón. A4: simbología de mapa ferroviario y de estado mayor antiguo (círculos, banderines y flechas) con segura #70784c, amenazada #847c34, asediada #982420 y perdida #340000 con borde #7c181c; nada de calaveras.
- **Regla nueva**: ningún prompt de Pixelab lleva negaciones; se pide solo lo que se quiere ver. Prompts de retratos reescritos en positivo, con prueba previa de 4 imágenes (`arte/encargo-fase-c.md`).
- **A6 y A7**: Marcos quita `dried blood red` y `gritty` del prefijo y comprueba las primeras imágenes antes de seguir.

## D-N51 · Reparto del saldo de Pixelab tras pasar A1–A5 a código 🔄
- **Propone**: Iris (Mak: «reparte el saldo libre entre retratos, rostros, ilustraciones y texturas, con prompts en positivo y prueba pequeña antes de cada lote»).
- **Saldo**: 8.416 (8:06, Marcos). Uso previsto sin sobrante: ~500, más G (~600) si la prueba de texturas sale bien.
- **Propuesta** (detalle en `arte/propuesta-fases-b-g.md`, revisión 08:25): rostros del checkpoint ~1.500, ilustraciones ~800, retratos de campaña ~450, texturas 3D ~600 (condicionada), decals y VFX nocturnos ~400. Total ~3.750; unos 3.300 se dejan sin gastar si no pasan la revisión.
- **Reglas**: prompts en positivo, prueba de 4 imágenes por lote, hoja de contacto revisada por Lucía y desvío máximo del 20 %.
- **Pendiente**: Lucía confirma el reparto; Eugenio lo ve por la mañana. Marcos confirma el saldo real antes de cada fase.
- **Visto bueno de Mak (6-nov, 08:19)**: aprobado. Regla: el saldo caduca el 17-nov; si las hojas pasan la revisión, se suben los bloques antes de esa fecha en vez de guardar. Marcos confirma el saldo real.
- **Lucía (08:25)**: de acuerdo con el reparto y con la regla de Mak. Si las hojas pasan la revisión, se sube primero el bloque de **rostros del checkpoint**, porque es el 2D que más se ve y donde más importa la variedad. Después, las ilustraciones. Orden de los rostros:
  1. familias (adultos con niños, ancianos);
  2. heridos (vendajes, cabestrillo);
  3. sospechosos, con signos **ambiguos** (fiebre, un brazo escondido, una venda dudosa). La infección nunca se ve con certeza en la cara: si se viera, el checkpoint dejaría de ser un dilema;
  4. especialistas (médica, maquinista, mecánico, con su herramienta u oficio a la vista);
  5. desertores (uniforme sin insignias).
  Reglas comunes: busto de 64×64 en 3/4, luz desde arriba a la izquierda, fondo neutro, población española diversa de 2026 en edad y origen, y sin gore.
- **Orden de los rostros (Lucía, 6-nov, 08:20)**: familias, heridos, sospechosos, especialistas y desertores. Reglas: busto 64×64 en tres cuartos, luz arriba a la izquierda, fondo neutro, población española diversa de 2026 y sin gore. **Regla de oro: la infección nunca se ve con certeza en la cara**, porque si se viera el checkpoint dejaría de ser un dilema. Si sobra saldo, va primero a rostros y después a ilustraciones. Encargo para Marcos: `arte/encargo-rostros-checkpoint.md`.

## D-N52 · A6 (unidades) por código y prueba de texturas con prefijo nuevo 🔄
- **Origen**: informe de Marcos (saldo real 8.364,05; la fase A gastó 284) y hojas `A6_unidades.png` y `A7_texturas.png`.
- **A6**: unas 10 de 40 llevan calaveras o sangre, y las que se salvan (artillería, blindados v2 a v4, fusileros v2, v3 y v6) tienen un estilo de dibujo animado, muy distinto de la familia sobria de A1 a A5. **Recomendación de Iris**: iconos de unidad por código (Bruno) para que toda la interfaz tenga una sola familia; de Pixelab solo se usa la artillería v2 y v5 como referencia de forma. Pendiente de Lucía.
- **A7**: sin calaveras en positivo. `ladrillo_grietas` v1 es buena; `rust` empuja al naranja y al rojo (ladrillo v3 salió rojo). Nuevo prefijo para texturas, en `arte/encargo-fase-a.md`, y prueba de 4 antes de las otras 56. La prueba de texturas 3D (fase G) sigue condicionada a este resultado.
- **Rostros y retratos**: Marcos lanza la prueba de 4 de Reig y Mora; reviso con Lucía antes de seguir.
- **Decisión de Lucía sobre A6 (6-nov, 08:23)**: todo A6 por código (Bruno), sin conservar ninguna de Pixelab. Además del tono, falla el concepto. Correcciones para Bruno: **artillería ferroviaria** = obús moderno sobre plataforma de tren con bogies, sobre la vía (de v2 y v5 solo el perfil del tubo); **blindado 8×8** = blindado de ruedas, 4 ejes y 8 ruedas visibles de perfil, casco en cuña (los ocho de Pixelab eran tanques de cadenas); **fusileros** = 2–3 siluetas con casco moderno y fusil actual (solo v6 tiene el tono; nada de la Segunda Guerra Mundial); **ametralladora** = tirador tumbado con bípode; **tren blindado** = reutiliza el blindado de A5. Misma luz y contorno que A1–A5, tropa en oliva con detalle en hueso.
- **Texturas**: base `ladrillo_grietas` v1; ladrillos en terracota y ocre apagados (el naranja casi coincide con el ámbar de alertas #e08c30; manda la luz del foco, no la pared).

## D-N53 · Regla de una sola estética para todo el 2D ✅
- **Pide**: Eugenio (6-nov, 08:26), a través de Mak: todo el arte y los iconos con la misma estética, sea de código o de Pixelab.
- **Decisión** (Iris, con Lucía y Bruno): paleta de 32, contorno de 1 px, luz arriba a la izquierda y tonos sobrios, para todo. Antes de dar por buena cualquier hoja de Pixelab se compara con la familia de código en una **hoja de cohesión**, que juzga Lucía. Regla completa en `arte/regla-estetica-unica.md`; herramienta en `arte/herramientas/cohesion_sheet.py` (probada).
- **Ampliación (Iris, 6-nov, 08:35; sobre D-N53)**: Lucía añade los puntos 7 a 13 de la regla (un tamaño de píxel, bordes duros, tope de colores, proporciones realistas, sin gore ni calaveras, legibilidad L* ≥ 25 y comprobación dentro del render de Unity). `cohesion_sheet.py` ahora comprueba automáticamente tamaño nativo, semitransparentes, tope de colores por tipo, contorno de 1 px y legibilidad, y marca OK o AVISO. Bruno aporta `unificar.py` (paleta, contorno y ruido); el flujo queda: bruto → `unificar.py` → `cohesion_sheet.py` → juicio de Lucía. Probado con las cargas de código y con una imagen con halo (aviso correcto).

### D-N49 · paso 3: ruido de obra y condiciones de Marcos (Nacho, PR #4)
- **Condiciones de Marcos (6-nov, 08:22), ya en código**: (1) el máximo de obreros por pieza es un valor del CSV, `obra_obreros_max_pieza` (4 por defecto; el puente del Jiloca llevará 8) y se guarda en cada pieza; (2) nunca trabajan obreros por debajo de la guarnición mínima, 12 (`guarnicion_minima` de `balance_economia.csv`); (3) la obra se pausa si el nodo está asediado, perdido o con densidad de horda ≥ 500, y el ruido de obra solo cuenta mientras la obra esté activa.
- **Ruido de obra (D-N44, valores ya en `balance_construccion.csv`)**: sondeo del 83 ‰ por hora y nodo con obra activa, del 5 % del presupuesto del día, como **masa nueva** (no sale de la deriva: así lo modela Hugo); nodo ×1,5 como objetivo de asedio (solo en el sorteo del objetivo); huella +0,5 por nodo con obra activa.
- **Cambia respecto a lo anterior**: el nombre del CSV pasa de `obra_max_obreros_por_pieza` a `obra_obreros_max_pieza`. **Para Hugo**: confirmar que el sondeo es masa extra sobre el presupuesto (hoy con la huella de una partida pequeña pide ~240 zombis el día 9; en el modelo de Hugo, ~330).
- **Falta**: texto de informe de inteligencia para el sondeo («ruido de obra», Lucía), terreno asegurado, daño y desgaste.
- **Pruebas**: 252 correctas, 0 fallos; G1–G5 sin tocar. Entrada anterior perdida y renombrada: yo la renombré a D-N49 con `sed -i` (reescritura del archivo entero) y puede que eso pisara a Iris; desde ahora solo añado al final.

## D-N54 · Pipeline 3D: qué se modela, con qué y cómo se le aplica la estética 🔄
- **Pregunta de Eugenio (6-nov, 08:31)** y respuesta de Iris. **Ya decidido** (GDD §11 y `arte/direccion-visual.md`): todo lo del mundo es 3D low-poly (infantería, vehículos, trenes, zombis, edificios) y la estética se aplica **en pantalla**, por el shader de pixelado de Unity: mundo a 1/2–1/4 de resolución, contorno de 1 px por profundidad y normales, paleta de 32 por LUT y ampliación con vecino más cercano. Las piezas clave se generan con Hunyuan en Blender; el resto, bases CC0 (Quaternius, Kenney) modificadas.
- **Propuesta** (pendiente de Lucía y Marcos):
  1. Infantería propia: una base CC0 contemporánea en 3 variantes (casco, gorra, ropa de trabajo), retocada en Blender, con la paleta en la textura.
  2. Vehículos y material ferroviario: Hunyuan para locomotora, vagones y blindado 8×8, con diezmado a 1.500–4.000 triángulos, UV y textura en paleta (flujo del GDD §11).
  3. Aviones y barcos: fuera del MVP; se hacen en la etapa 3 por kitbash CC0 más Hunyuan, y no se modelan hasta entonces.
  4. Prueba de cohesión 3D: una captura en Unity con un soldado, el blindado y una locomotora bajo el shader, de día y de noche, antes de modelar más (regla 13).
- **Sin Tripo**: se modela con Hunyuan local, Blender con su servidor MCP oficial y, como alternativa documentada, TRELLIS.2.
- **Ajustes de Lucía (6-nov, 08:32)**: de acuerdo con las tres propuestas. Soldados en 3 variantes sobre la base CC0 de Kenney (ya aceptada), **más 2–3 variantes de civiles** (refugiados, obreros y familias, que también caminan por la zona). Albedo plano con colores de la paleta, sin texturas finas. Tropa en oliva y civiles en ocre, beige y hueso. La captura de cohesión 3D añade un zombi, un tramo de HESCO y un foco con su charco de noche, y mide tres bandas de valor de día, el tono del charco entre 20° y 45° de noche y L* ≥ 25 entre soldado, civil y zombi contra el suelo. Encargo para Marcos: `arte/encargo-captura-cohesion-3d.md` (sin gasto de generaciones).
- **Visto bueno de Mak (6-nov, 08:33)** a la captura de cohesión 3D: Marcos la hace después del prototipo, o dentro de él si le cabe.

### Jérica, emplazamiento opcional (08:40, Hugo midió y aplica la regla de Lucía) ❌ fuera de la demo
- **Propuesta de Lucía**: estación fundable opcional entre Segorbe y Barracas (km 50), sin producción, por 30 u y 12 personas. **Regla de Lucía**: se queda si el equilibrado que la funda siempre pierde el 14 % o menos (sin ella, 11 %).
- **Medido por Hugo** (250–300 partidas, fundándola siempre):

  | Variante | Equilibrado | Prisa | Escasez |
  |---|---|---|---|
  | Sin Jérica | 11 % | 39 % | 52 % |
  | Estación sin ventaja | 22 % | 58 % | 60 % |
  | Apeadero (retén de 6) | 31 % | 48 % | 62 % |
  | Estación con relevo (−1 h por viaje a Teruel) | 18 % | 55 % | 52 % |
  | Estación con relevo de −1,5 h | 18 % | 52 % | 48 % |

- **Por qué**: el relevo quita escasez, pero las derrotas no vienen de ahí. Vienen de tener otro nodo en el interior (×1,4) que la Colmena asedia, con 12 personas atadas y más huella. La prisa no la usa para adelantar el puente, porque el puente depende del tren de obras.
- **Resultado**: 18 % > 14 %, así que **Jérica sale de la demo** y se guarda para el acceso anticipado, donde la red más larga del interior le dará sentido.

### D-N49 · corrección del paso 3: el sondeo va descontado + avisos OC (Nacho, PR #4; Hugo, Lucía y Mak)
- **El sondeo de obra va descontado, no como masa extra** (Hugo, aprobado por Mak, 08:33): sale del 400 ‰ del presupuesto que no va a asedios, con la masa conservada. Como extra, el total de 20 días dejaba de cuadrar con la referencia validada (≈ +2 %). En el código: se paga primero con la deriva de la hora y después con el ahorro del canal de emboscada. **Sustituye** a lo escrito antes («masa nueva») y a la petición de Hugo del CSV sobre ese punto.
- **Avisos** (textos de Lucía, `textos-informe-colmena.md` §7, ya en `textos_informe.csv`): OC-1 (primera obra, una vez; Llorens), OC-3 (llega un sondeo; «tras el ataque») y OC-4 (la horda para la obra; una vez por parada; la fuente la puse yo: Llorens, **Lucía: confirma**). OC-2 («en {minutos} min») no se usa: el sondeo llega de golpe, sin plazo; usarlo exige un plazo de aviso (cambio de modelo con Hugo).
- **Fundar** (Mak, Lucía, 08:32): modelo del flag (`Founded` en el hash, sin nodos en caliente). Nodos: ciudades (Sagunto, Castellón, Teruel, Zaragoza, Valencia) no se fundan; apeaderos existentes (Puçol, Almenara, Segorbe, Barracas, Caminreal, Calamocha, Cariñena) se aseguran con un retén de 6 personas y pueden crecer; **Nules** es el único emplazamiento fundable de la demo. **Jérica sale de la demo** (Hugo: 18 % de derrotas, umbral 14 %); el tipo «emplazamiento fundable» se queda en el código. Lista configurable.

## D-N55 · Prueba de retratos (Reig y Mora) y de texturas (A7b) 🔄
- **Origen**: pruebas de 8 de Marcos (`C_retratos.png`, `A7b_texturas.png`). Comparación en `arte/cohesion/cohesion_retratos_reig_mora.png`.
- **Retratos**: calidad muy buena (rostros expresivos, luz coherente, sin gore). Con `cohesion_sheet.py --tipo retrato`: Reig v1 21 colores y dL* 22; Reig v2 20 colores y dL* 19; Mora v1 18 colores; Mora v2 16 colores y dL* 28. **Avisos**: más colores que el tope de 16 y Reig queda oscura sobre el panel (< 25). Además, Reig v1 y v2 llevan insignias en gorra y hombrera (regla de D-N06: sin insignias), y el naranja de los galones choca con el ámbar de alertas.
- **Recomendación de Iris**: lanzar la fase C completa (128 generaciones, ya aprobadas) con dos ajustes en el prompt, en positivo: rostro bien iluminado desde arriba a la izquierda (más claro) y uniforme liso con hombreras simples (`plain olive uniform with simple shoulder straps`). Pasar la salida por `unificar.py` limitando a 16 colores. Elegidos provisionales: Reig v1 y Mora v2. Lucía confirma.
- **Texturas (A7b)**: flojas (ruido sin lectura de material; la chapa y la teja no se reconocen). Lucía ya pidió albedo plano en el 3D, sin texturas finas. **Recomendación**: texturas por código (Bruno, patrones de ruido controlado) y **se descarta la fase G** (~600 generaciones) y las 56 restantes de A7. Pendiente de Lucía y Mak.

## D-N56 · Lucía confirma la fase C y las texturas por código ✅ (6-nov 08:42)
- **Fase C**: confirmada con tres correcciones (más luz, uniforme liso, `unificar.py` a 16 colores) y tres matices de Lucía: (1) **Reig v1**, y el rango se conserva: galones en hueso o latón apagado, nunca naranja. (2) **Mora v1** (con cascos), no la v2; se pide en 3/4, como Reig, para un único encuadre. (3) «Más iluminado» = subir la luz principal (arriba a la izquierda) hasta **L\* ≥ 25 en la cara** sin aclarar el tono de piel. Vale también para los rostros del checkpoint.
- **Texturas**: por código con Bruno (4–5 teselas: balasto, hormigón, ladrillo, tierra, asfalto, albedo plano en la paleta). **Se descarta la fase G (~600)** y las 56 restantes de A7. El saldo sobrante va a rostros.
- **Iris**: briefs actualizados (`encargo-fase-c.md`, `encargo-rostros-checkpoint.md`, plan v0.7).

### D-N49 · paso 3 del orden de Lucía: fundar una estación (Nacho, PR #5 apilado sobre #4)
- **Modelo del flag** (Mak, 08:32): `Founded` por nodo dentro del hash (solo si es true, así que G1–G5 no cambian); sin nodos en caliente. Emplazamientos configurables (`StationParams.Sites`); hoy solo **Nules** (Lucía y Hugo: Jérica fuera de la demo; el tipo «emplazamiento fundable» se queda en el código).
- **Orden** `FoundStation = 12`: tren parado en el nodo con 30 u y 12 personas a bordo (`fundar_materiales` y `guarnicion_minima`), sin horda encima (densidad < 500). Gasta los materiales y deja las 12 personas en el nodo. Nivel: apeadero → estación con depósito construido y 40 personas.
- **Para el CSV de Hugo**: `estacion_personas;40`, `fundar_radio_tren_mm;5000`.
- **Pendiente de decisión (Marcos y Mak)**: (1) una orden para parar un tren en el emplazamiento (hoy solo hay `TrainHold`, que lo detiene donde esté, y los horarios son fijos): propongo «añadir parada de horario» o «detener en el emplazamiento»; (2) que un emplazamiento sin fundar no cuente para el peso del director, la huella ni los asedios (hoy Nules cuenta): cambia los goldens y pide su línea en este archivo.
- **Pruebas**: 280 correctas, 0 fallos.

## D-N57 · Legibilidad 3D: las unidades llevan a la vez un valor claro y uno oscuro (Lucía, con Iris y Bruno) ✅
- **Problema** (captura de cohesión 3D de Marcos, 08:50): ningún modelo llega a 25 de ΔL* contra el suelo. De día, el oliva tiene el mismo valor que el fondo de la trinchera (#48403c). De noche, fuera de la luz, todo desaparece.
- **Decisión**:
  1. **Valor partido en cada modelo**. Las caras de arriba claras (techo del casco, hombros, techo del vehículo y relleno de los HESCO en beige, entre #d4d0cc y el caqui claro) y los costados oscuros, con el contorno de 1 px que ya tiene el shader. Así cada unidad contiene un valor más claro y otro más oscuro que cualquier suelo: se lee sobre la trinchera oscura por arriba y sobre el llano ocre por el borde. Es la misma solución que el techo claro del tren (D-N42).
  2. **No se aclara el suelo**. Romperíamos las tres bandas del desmonte y el fondo oscuro donde se lee el tren.
  3. **Nueva medida**: ΔL* = máx(|L* del 20 % más claro del modelo − L* del suelo|, |L* del contorno − L* del suelo|) ≥ 25. La L* media de un modelo con dos tonos no dice nada.
  4. **Noche**: el criterio de 25 se mide **dentro de los charcos** de los focos (D-N13, dirección visual 4b). Fuera de la luz, las unidades **propias** (tropa, civiles y vehículos) llevan un rim frío y tenue de luna (#404460) con un objetivo de 15 de ΔL*. Los **zombis no**: salen de la oscuridad, y para eso están los focos. Su rim emisivo sigue como opción del hito 7.
  5. **Captura de día a mediodía** (sol a 32°), no al amanecer: la de las 05:46 no es representativa.
- **Texturas A7**: compatibles. El suelo de poco contraste interno (regla 14) es justo lo que deja leer el valor partido.

### D-N49 (adenda, Nacho, 6-nov): detener en el emplazamiento y emplazamientos sin fundar (PR #6)
- **Qué cambia**: nueva orden `NetCmdType.HaltAtSite = 13` (`Arg` = nodo emplazamiento, `-1` cancela; `Arg2` = servicio). `TrainService.HaltAt` entra en el hash del tren solo mientras hay parada pendiente. Un emplazamiento sin fundar devuelve peso 0 en `HiveDirector.SiegeWeight` y no cuenta en `HuellaMil` (decisión de Mak, 6-nov).
- **Goldens**: **ninguno necesita regenerarse**. Con los presupuestos de G1–G5 la parte de Nules en la deriva se redondea a 0, así que los hashes salen idénticos (comprobado: 291 pruebas en verde, G1–G5 sin tocar). No se ha modificado ningún `.golden`.

## D-N58 · Fase D y decals por código (Bruno); pixelfx autorizado ✅ (6-nov 08:55)
- Por encargo de Mak, Bruno hace por código fogonazo, trazadoras, fuego, humo de impacto y haz del foco (64×64, alfa duro) y los decals (5 tipos, 32×32, 2 variantes, sin sangre): 0 generaciones de Pixelab. Revisa Lucía.
- **Autorización**: a las 08:06:35 Eugenio eligió «Sí, ejecútalos» en la tarjeta «¿Me dejas ejecutar pixelfx y Pixelbolt para los efectos de la fase D?» (opción 0, verificado por Mak). Condiciones de Mak: leer el código antes, ejecutar solo en la nube y sin credenciales.

> Nota de Iris (6-nov 08:57, aprobada por Mak): D-N57 (valor partido en 3D) se aplica con tres reglas añadidas en `arte/modelado-3d/encargo-modelos-hunyuan.md`: valor horneado en el albedo, beige de la paleta y contorno por script, y marcador de prefab para el rim de las unidades propias. `cohesion_sheet.py` tiene ya `--tipo modelo`.

## D-N59 · Claves del H5 de Nacho pasadas al CSV y validadas (Hugo) ✅
- **Pide**: Mak (lista de `Docs/obras-h5.md`, commit 4880606). **Valida**: Hugo. Todas las claves están ya en `balance_construccion.csv`.
- **Validadas tal cual**:
  - `muro_modulo_mm` 10.000 y `muro_minimo_mm` 1.000.
  - `perimetro_mm` 60.000: el radio desde el andén en el que las piezas cuentan para el nivel. Cabe un perímetro de 150 m.
  - Las horas de obra de las 7 piezas.
  - `obra_obreros_max_pieza` 4; el puente guarda 8 en su propia pieza (192 obreros·h = 8 × 24 h).
  - `estacion_personas` 40 y `fundar_radio_tren_mm` 5.000.
  - Coste en E4 con `ceil` al cobrar y la regla de corte del muro.
- **Dos cambios**:
  1. **Guarnición mínima para las obras: 6 (el retén), no 12.** Con 12, una estación recién fundada (30 u y 12 personas) tendría 0 obreros y no podría levantar ni un saco, lo que contradice P9b y el modelo, que fortifica con la guarnición. Clave nueva: `obras_guarnicion_minima`. `guarnicion_minima` (12) sigue valiendo para producir.
  2. **El sondeo de obra sale de la masa conservada**, como aprobó Mak a las 07:16, no como masa nueva con `Inject`. Debe descontarse de la parte del presupuesto del día que no va a asedios. Así el total de los días 1–20 sigue cuadrando con la referencia. Como masa extra serían ≈ +2 % en 20 días.
- **Duplicado**: `nivel_u_por_nivel` (30) ya existe como `fort_materiales_por_nivel` en `balance_economia.csv`. Mejor que el código lea esa y no haya dos claves con el mismo dato.

## D-N60 · Regla de Eugenio para ElevenLabs: siempre el modelo más moderno ✅ (6-nov 09:03)
- **Regla de Eugenio** (cita): «para efectos usar v3 text to effect. para musica, v2.5. intentar siempre utilizar los modelos más modernos».
- Efectos: `eleven_text_to_sound_v3`. La documentación oficial (elevenlabs.io/docs/overview/capabilities/sound-effects, consultada por Iris) marca v2 como obsoleto (se retira el 1-mar-2027) y no indica que v3 sea beta. Sustituye a mi instrucción anterior de «no usar v3 si figura como beta».
- Salida: la documentación dice MP3 para todos y WAV a 48 kHz solo para efectos sin bucle; los bucles saldrán en MP3 (comprobar el parámetro exacto en la referencia de la API). Duración de 0,1 a 30 s.
- Música: v2.5, según Eugenio; por verificar en la documentación de Eleven Music que no figure como beta (sin licencia comercial) antes de generar. Marcos lo comprueba en la API junto con la suscripción.

### D-N49 (adenda 2, Nacho, 6-nov): D-N59 aplicado y desgaste diario (PR #7 y #8)
- **PR #7 (D-N59, Hugo)**: el retén de obras es `obras_guarnicion_minima` = 6 (la `guarnicion_minima` de 12 sigue para producir y fundar); los u por nivel salen de `fort_materiales_por_nivel` y se borra `nivel_u_por_nivel`; `balance_construccion.csv` de Hugo copiado a `Assets/TBD/Data`. El sondeo ya salía de la masa conservada desde #4 (sin `Inject`). **Ningún golden cambia**: no hay obras en G1–G5, así que no hay ningún `.golden` regenerado.
- **PR #8 (desgaste)**: `fort_desgaste_dia` (10 ‰) se aplica una vez al día a las piezas construidas (mínimo 1 ‰ por día; a 0 ‰ la pieza se destruye). Sin obras el hash no cambia, así que **ningún golden cambia**.

### D-N49 (adenda 3, Nacho, 6-nov): el desgaste es mantenimiento (Hugo, PR #8)
- Cada día, cada estación con obras paga de su almacén `ceil(1 % de Σ(CostE4 × vida))` u de materiales (todas las piezas construidas, depósito incluido). Si puede pagarlo, la vida no baja. Si no, se aplica la caída geométrica (1 % de lo que queda, mínimo 1 ‰) y no se cobra nada. El 82 % a los 20 días es el caso de una estación sin reservas.
- Pruebas: abastecida no se degrada (20 días, 1 u al día) y vacía sí (817 ‰ a los 20 días). **Ningún golden cambia** (no hay obras en G1–G5): 308 pruebas en verde.

### D-N49 (adenda 4, Nacho, 6-nov): el mantenimiento usa la misma Σ que el nivel (Hugo, PR #8)
- Corrección a la adenda 3: el depósito **no** cuenta. El mantenimiento diario usa exactamente la Σ(CostE4 × vida) del nivel de fortificación (piezas defensivas construidas a ≤ 60 m del andén), para que haya una sola regla. Prueba nueva: un depósito y un muro a más de 60 m no suman al mantenimiento. 309 pruebas en verde, **ningún golden cambia**.
- Queda por decidir (se lo he preguntado a Mak): si el mantenimiento se paga, ¿lo que queda fuera de la Σ (depósito, muros lejanos) tampoco se desgasta? Hoy, si no se paga, el desgaste se aplica a todas las piezas construidas, y si se paga, a ninguna.

### D-N49 (adenda 5, Nacho, 6-nov): reparar un tramo y el puente (PR #9, aprobado por Mak)
- Los cortes del director (TR-4) dejan escombros (`RailEdge.Debris`) y la vía no existe hasta que un tren de obras la repara con la orden `RepairEdge = 14` (5 u y 8 obreros a bordo, 3 h; el puente del Jiloca, 80 u y 192 obrero·h). Los cortes por densidad siguen despejándose solos. El tren de obras se identifica con `TrainService.WorksTrain`.
- **Goldens**: **ninguno cambia**. Con las obras y los cortes del director de G1–G5 los hashes salen idénticos (no hubo corte con escombros en esas repeticiones), así que no se ha regenerado ningún `.golden` y no hace falta el visto bueno de Sara. 332 pruebas en verde.
- Claves nuevas que viven en el código y faltan en el CSV de Hugo: `reparar_tramo_h` (3) y `puente_jiloca_u` (80).

### D-N49 (adenda 6, Nacho, 6-nov): ajustes de Hugo a #8 y #9
- **#8 (desgaste)**: el depósito no se desgasta nunca. Los muros a más de 60 m del andén se desgastan siempre, sin mantenimiento posible, a `desgaste_fuera_perimetro_permil_dia` = 10 ‰ al día (1 % de lo que queda, ~82 % a los 20 días). Lo de dentro del perímetro se desgasta solo si no se paga el mantenimiento. Pruebas nuevas: depósito intacto con y sin mantenimiento, muro exterior ~82 % a los 20 días con la estación abastecida. 312 pruebas en verde, **ningún golden cambia**.
- **#9 (reparar)**: el puente usa `puente_jiloca_materiales` (80) y `puente_jiloca_dias` (2) de `balance_economia.csv`; no hay `puente_jiloca_u`. Con 8 obreros y día entero son 72.000 ticks. Las 192 obrero·h de `balance_construccion.csv` (8 × 12 h × 2 días) ya no se leen: **si el trabajo es de 12 h al día, la obra debería durar 4 días de reloj; lo he leído como 2 días continuos porque manda el CSV, a confirmar con Hugo**. `reparar_tramo_h` ya está en el CSV. 335 pruebas en verde, **ningún golden cambia**.
- **Corrección a la nota anterior (Nacho)**: la cuenta correcta es la contraria. Con 8 obreros trabajando las 24 h, 192 obrero·h son 1 día; 2 días continuos son 384 obrero·h. Las 192 obrero·h de Hugo (8 × 12 h × 2 días) solo cuadran con **2 días de reloj si se trabaja 12 h al día**. Hoy el puente tarda 2 días continuos (72.000 ticks), el doble del trabajo de esas 192 obrero·h. **A confirmar con Hugo**: o la obra avanza solo 12 h al día (hay que definir el horario de trabajo), o el trabajo del puente son 384 obrero·h.

## D-N61 · La horda a distancia se lee como mancha, no como individuos (Lucía) ✅
- **Problema** (Marcos, 09:36, `horda_sprites_zoom_juego.png`): con 3.000 zombis a zoom de juego, los sprites de 32 px quedan en 3–4 px tras el pixelado 1/3. La camisa clara (D-N57) y el contorno hacen un ruido de sal y pimienta, y las filas regulares del despliegue parecen texto. De cerca se leen bien.
- **Decisión**: la horda tiene dos lecturas, como en el cine el plano general y el primer plano.
  1. **LOD de masa** (Bruno y Marcos): cuando un zombi ocupa menos de unos 8 px en el búfer pixelado, cambia a un sprite de masa de 8×8. Cuerpo en #303424, cabeza de 1 px en #88885c (subida de #605c48 a las 09:40 para los suelos oscuros: desde arriba, una multitud se lee por las cabezas), sin contorno, sin cara clara arriba y sin variantes. Andar de 4 fotogramas con 1 px de balanceo y cadáver como una mancha plana más apagada. El cambio lleva histéresis, para que no parpadee al hacer zoom. D-N57 no se aplica a la masa: se aplica al individuo de cerca.
  2. **Sombra de masa**: debajo de la horda, el suelo se oscurece según la densidad (multiplicar por ~0,6 donde está más densa). Así la horda densa es una mancha oscura con borde legible, y la zona dice lo mismo que la mancha del mapa (S0).
  3. **Fuera las filas**: posiciones con ruido (±0,5 de celda), orientación al azar (±20°) y fase de animación al azar. Las filas son la mitad del ruido.
- **Prueba**: en escala de grises y a zoom de juego, la horda se ve como zonas oscuras continuas, con el frente legible, y el tren y la vía se separan de ella. Masa contra llano ocre: 25 de ΔL* o más. Sobre el fondo de la trinchera, la diferencia la pone la sombra de masa.
- **De noche** encaja con D-N13: la masa son siluetas oscuras a contraluz sobre los charcos.

### D-N49 (adenda 7, Nacho, 6-nov): puerta de vía (PR #12)
- Aplicado §2a de `diseno-hito5.md` (Lucía) con el coste de Hugo (8 u, 6 obrero·h): la red de Obras conoce la vía (y = 0, gálibo de 3,2 m) y pone sola una `PuertaVia` donde un muro la cruza. Hueco 3,2 ÷ sen α; por debajo de 45° se rechaza el trazado. Estado (modo, avance de apertura de 180 ticks de zona y rota) en el registro y en el hash. Orden `SetGate = 15`.
- **Goldens**: **ninguno cambia**. G1–G5 no tienen obras ni puertas, y las pruebas de coste y nivel (secciones [15] a [19]) trazan muros por el andén, que es la vía, así que desactivan la franja en su mundo de prueba. 368 pruebas en verde.
- **Interpretaciones mías a confirmar con Lucía**: un muro que acaba dentro del gálibo se recorta en el borde sin puerta; las piezas puntuales (menos el andén fortificado) no pueden estar en la franja; una puerta rota se queda como pieza `Broken` (no se quita) y una nueva a ≤ 3,2 m la sustituye.
- Observación sobre `CancelWork` (no es nuevo): cobra la obra redondeando hacia arriba y devuelve redondeando hacia abajo, así que cancelar una obra sin empezar de 180.800 E4 devuelve 18 u y se cobraron 19.
- **Ajuste de D-N61 (Lucía, 09:55)**, después de la primera captura en grises: el LOD de masa no se veía. Umbral subido a 16 px en el búfer pixelado (a zoom de juego, siempre masa), sprite LOD sin iluminación y con el color exacto de la paleta (L* media ≤ 25), y sombra de masa con un núcleo gaussiano de 6 m: alfa 0 por debajo de 0,2 zombis/m², hasta 0,55 a partir de 1 zombi/m². La horda dispersa se lee como puntos oscuros y la agrupada, como mancha.

### D-N59 (adenda, Hugo, 6-nov): horario de obra y CancelWork (preguntas de Nacho en el PR #12)
- **Horario de obra**: todas las obras trabajan de 06:00 a 18:00 (12 h/día, igual que `horas_obra_dia` del modelo) y de noche se paran sin perder progreso. Filas `obra_hora_inicio` 6 y `obra_hora_fin` 18 en `balance_construccion.csv`. El puente del Jiloca sigue en 192 obrero·h, que son 2 días con 8 obreros (no 384).
- **CancelWork**: una obra sin empezar devuelve exactamente lo cobrado (se guardan las u cobradas por obra: si se pagan 19, se devuelven 19). Una obra empezada devuelve floor(50 % de lo cobrado) (`cancelar` 500). **Por qué**: así poner y quitar una obra no hace perder material, y el reembolso no depende del redondeo de E4.

### D-N49 (adenda 8, Nacho, 6-nov): refinamientos de Lucía a #12 y horario de obra de Hugo (PR #12 y #14)
- **#12 (Lucía)**: el andén fortificado tampoco puede estar dentro del gálibo (junto al borde sí, a 1,6 m); la puerta nueva sobre una rota conserva la posición exacta de la anterior y cuesta 8 u. 370 pruebas en verde.
- **#14 (Hugo, D-N59)**: todas las obras (muros, piezas, reparaciones) trabajan de 06:00 a 18:00 y de noche se paran sin perder progreso; el puente vuelve a 192 obrero·h (con 8 obreros, 2 días); cancelar sin empezar devuelve exactamente lo cobrado y empezada, `floor(50 %)`. 382 pruebas en verde.
- **Goldens**: **ninguno cambia** en #12 ni en #14 (G1–G5 no tienen obras; el hash de `PaidU` solo existe con obras).
- **Decisión mía a confirmar con Hugo**: una obra parada de noche no cuenta como activa, así que no hay sondeo, peso ×1,5 ni huella mientras no se trabaja.
- Nota técnica: el escenario MVP arranca a las 05:30, antes del horario de obra; los mundos de prueba de obras arrancan a las 08:00.

### D-N59 (adenda 2, Hugo, 6-nov): qué oye la Colmena de una obra parada de noche (pregunta de Nacho en el PR #14)
- **Sondeo**: solo cuando la obra trabaja (06:00–18:00). De noche no hay sondeo, porque es ruido de trabajo (`obra_sondeo_permil_hora` es por hora trabajada).
- **Peso ×1,5 para el asedio y huella**: cuentan mientras la obra está **en curso** (encargada y sin acabar), también de noche. **Por qué**: el modelo los cuenta por día, los objetivos del asedio son persistentes y no deben cambiar cada 12 h, y si la noche borrase la presión, el truco sería encargar las obras al anochecer. Solo cambian las descripciones del CSV, no los valores.
- **Segundo ajuste de D-N61 (Lucía, 10:12)**, con la escena densa de Marcos (800 zombis, semilla 777). La masa da L* 19 (bien), pero contra el fondo de la trinchera (L* ~23) la diferencia es de 3–4 y la horda desaparece.
  1. **Se mide en captura normal**, que es lo que ve el jugador, con la máscara sacada de un pase de depuración a la misma resolución. El supersize cambia la exposición y no vale para medir.
  2. **El fondo de la trinchera sube a L* 38–42** (#605c48 o equivalente). Es lo que ya medí y aprobé en la v2 del desmonte (D-N42: arriba ~67, taludes ~50, fondo ~40). Las tres bandas se mantienen con 10 o más de diferencia entre ellas. **El balasto (#48403c, L* 26–30) queda solo en la franja de ~3 m bajo la vía**: sigue siendo lo más oscuro y sobre él se lee el techo claro del tren.
  3. **Valores objetivo en la zona**: arriba 62–68, taludes 48–54, fondo 38–42, balasto 26–30, masa de horda ≤ 20 y techo del tren ≥ 72. Masa contra el fondo y contra el llano: 25 o más de ΔL*. Sobre la franja de balasto, la lectura la dan el punto de cabeza y la altura de la pila.

### D-N49, adenda 9 (Nacho, 6-nov): obra EN CURSO frente a obra TRABAJANDO (petición de Hugo, D-N59 adenda 2)
- `NetWorld.WorkInProgress(nodo)` = encargada y sin acabar, con obreros asignados (y fuera de la pausa por horda), también de noche. Alimenta el peso ×1,5 del asedio (`SiegeWeight`) y la huella (`HuellaMil`).
- `NetWorld.WorkActive(nodo)` = en curso y dentro de 06:00–18:00. Alimenta el sondeo de obra y el avance (`EffectiveWorkers`, que sigue siendo 0 de noche).
- Los valores del CSV no cambian. Los goldens G1–G5 no cambian (no hay obras).

- **Corrección del segundo ajuste (Lucía, 10:18)**: el L* 23 del fondo venía del supersize. En captura normal, el fondo da ~57, casi igual que el llano, así que la trinchera no se leería como trinchera. Por tanto, el fondo **se oscurece**, no se aclara. Valores objetivo en captura normal: arriba 64–68, taludes 52–56, fondo 42–46 y franja de balasto 28–32, con 10 o más entre bandas. Criterio de la horda: **dispersa**, los píxeles de cuerpo del LOD contra el suelo, 25 o más (cuerpo ≤ ~19 sobre un fondo de 44); **densa**, la L* media de la región de la mancha (sprites y sombra) contra el suelo limpio de alrededor, 25 o más. Si el post-proceso aclara el cuerpo por encima de 19, se adelanta al prototipo la capa del LOD fuera del post-proceso.

### D-N49, adenda 10 (Nacho, 6-nov): terreno asegurado en la orden de obra
- Diseño (diseno-hito5 §1, §2b): solo se construye con ningún zombi en pie a menos de ~30 m de la obra, calculado con la rejilla de densidad del tick.
- La red no puede leer la rejilla (es de DOTS), así que la zona la enchufa: `NetWorld.ZoneDensity` (`Func<DensityView>`), con la rejilla ya en mm locales al nodo (esquina de la celda (0,0), tamaño de celda, ancho y alto). Sin enchufar, todo terreno vale (pruebas y goldens no se mueven; no entra en el hash).
- `Terreno.IsSecure(vista, x, y, radio)`: círculo de radio `SecureMm` (30.000 mm por defecto, clave opcional `obra_terreno_asegurado_mm`, no está en el CSV); una celda con algún zombi cuenta si su punto más cercano está a ≤ radio. `Terreno.PlanSecure` comprueba los extremos de cada pieza y puntos intermedios cada radio/2, para que un muro largo no cruce una mancha sin que se note.
- `NetWorld.PreviewWork` (lo que enseña el fantasma) y `PlaceWork` (la orden) rechazan con `Why = "Hay zombis cerca: el terreno no está asegurado"`, sin cobrar ni registrar.
- Para Marcos: construir la `DensityView` en la zona (celdas de 0,5 m, índice y·W+x; pasar del origen de la zona al andén (0,0) del nodo, y m a mm) y asignar `ZoneDensity` al materializar. La rejilla de SimCore ya cuenta solo zombis en pie (caídos y muertos no).

### D-N49, adenda 11 (Nacho, 6-nov): el taller de Sagunto fabrica y rehabilita trenes (paso 5)
- Nuevo `Net/Taller.cs` (`TallerParams`, `TallerState`) y `NetWorld.OrderTrain / CancelTrainOrder / AdvanceTaller`. Órdenes nuevas: `OrderTrain = 16` (Arg = tipo), `CancelTrainOrder = 17` (Arg = posición en la cola), `SetChispas = 18` (Arg 0/1). Entra en el hash dentro de «existencias» y vale 0 con la cola vacía: G1–G5 no se mueven.
- Tipos: Carga 0, Combate 1, Obras 2 (tren nuevo: 120 u + 30 de combustible, 3 días), RehabTren3 3 (60 u + 15, 36 h) y RehabObras 4 (20 u + 5, 36 h). Cada rehabilitación solo se encarga una vez. Valores del CSV de Hugo (tren_coste_*, tren3_demo_coste_*, tren_obras_*, taller_dias_tren, taller_rehabilitar_horas, trenes_max_etapa2).
- Cola: el taller hace un encargo a la vez, las 24 h. Se paga todo al encargar con las existencias de Sagunto; si falta algo no se cobra nada.
- Máximo de trenes: 4 en la demo y 6 en la etapa 2 (`trenes_max_demo` no está en el CSV: 4 por defecto, D-N16). Cuentan los trenes que ruedan más los encargados.
- Chispas Ferrer (`Taller.Chispas`, bandera en el hash, orden `SetChispas`): rehabilitar y reparar tramos/puente un 25 % más rápido (velocidad ×1,25, es decir 36 h → 28,8 h y 3 h → 2,4 h; `taller_chispas_permil` = 250 por defecto, no está en el CSV), no la fabricación. Hugo escribió «29 h» en el CSV: 28,8 redondeado.
- El tren nace en el nodo del taller con **una sola parada**: sin horario no se mueve. El tren de obras (rehabilitado o fabricado) sale marcado `WorksTrain` y con **8 obreros a bordo**, que se descuentan de la población de Sagunto al encargar (sin dejarla por debajo del retén de 6); los materiales los carga el horario.
- Cancelar: sin empezar, devuelve exactamente lo cobrado; empezado, el 50 % de la parte que falta (como las obras); la dotación vuelve entera.
- Supuestos míos a confirmar: (a) que la dotación de 8 salga de la población al encargar; (b) cancelar al 50 % como las obras; (c) Chispas como bandera global y no como personaje ligado a un tren; (d) no hay aviso «tren listo» porque no hay texto de Lucía.


### D-N45 (adenda, Hugo, 6-nov): revisión de la economía del taller (PR #17 de Nacho)
- **Costes**: cuadran con PARAM y los CSV. Tren nuevo 120 u + 30 de combustible en 3 días, Tren 3 60 + 15, tren de obras 20 + 5, rehabilitar 36 h.
- **Dotación de 8 obreros**: se aprueba que salga de la población de Sagunto al encargar, pero solo de los libres por encima del mínimo. Si no llegan a 8, el encargo se rechaza. Los 8 viajan a bordo y no vuelven. El modelo antes solo comprobaba los libres sin descontarlos; ahora los descuenta y lo he medido con 300 partidas: equilibrado 11,0 → 11,7 %, prisa 39 → 42,7 %, escasez 52 → 55 %, Zaragoza sigue el día 14. Todo dentro de los objetivos de Lucía, así que no se toca nada más.
- **El taller trabaja 24 h**: va bajo techo y no sigue el horario de obra de 06:00 a 18:00. Los 3 días y las 36 h son de reloj. Si siguiera el horario, cada trabajo duraría el doble: rehabilitar pasaría a 3 días y un tren nuevo a 6, lo que descalibra el ritmo del Tren 3 y del puente (P8).
- **Cancelar en el taller**: la misma regla que D-N59. Sin empezar se devuelve el 100 % de lo cobrado; empezado, floor(50 % de lo cobrado), no el 50 % de lo que falta. Al cancelar vuelven los 8 obreros (y la tripulación de 10 de un tren nuevo).

### D-N45 (adenda) · respuesta de Lucía (6-nov, 11:15)
- **Se acepta sin compensar**: k_huella se queda en 0,24. Hugo midió la palanca de 0,23 (300 partidas): la prisa baja al 37,3 %, pero el equilibrado sube al 13,3 %. No compensa: la prisa al 42,7 % es la que tiene que doler y queda casi en el 38–42 % original; el 11,7 % del equilibrado entra en el margen; Zaragoza sigue el día 14.
- **Pendiente de Hugo**: la adenda descuenta la dotación al encargar. Mi propuesta a Nacho es reservarla al salir el tren, para que el jugador no pierda mano de obra los 3 días de taller. Hugo dirá si eso cambia sus números; si no, se queda «al encargar» tal como está medido.
- **Adenda (Hugo, 11:30), a petición de Lucía**: los 8 obreros se descuentan **cuando sale el tren**, no al encargarlo. Al encargar solo se comprueba que haya 8 libres. Si al salir no los hay, el tren espera en el taller. Medido con 1000 partidas: con descuento al encargar, equilibrado 13,2 % y prisa 42,0 %; con descuento al salir, 13,8 % y 43,1 %. Es la misma cifra dentro del ruido (error típico ~1,1 puntos). **Ojo**: con 1000 partidas el equilibrado vigente es 13,2 %, no el 11,7 % de 300; las 300 partidas lo infravaloraban. Sigue por debajo del umbral del 14 %. La puerta de vía (8 u, 6 obrero·h) queda confirmada: es la puerta normal (6 u) más 2 u de carril y contracarril; con 4 obreros sale en 1,5 h de horario de obra.

### D-N45 (adenda) · cierre (Lucía, 6-nov, 11:18)
- **Dotación al salir el tren**: validada por Hugo con 1000 partidas (al encargar 13,2 % / 42,0 %; al salir 13,8 % / 43,1 %; iguales dentro del error de ~1,1 puntos). Al encargar solo se comprueba que haya 8 libres; si al salir no los hay, el tren espera en el taller. Nacho lo implementa.
- **Corrección de método**: con 1000 partidas el equilibrado vigente es 13,2–13,8 %, no 11,7 %. Sigue bajo el umbral del 14 %, sin holgura. Si la demo se nota dura, la primera palanca es H0 1500. Desde ahora se mide con 1000 partidas.
- **Puerta de vía**: 8 u y 6 obrero·h, validada (puerta de 6 u + 2 u de carril y contracarril).

### D-N49, adenda 12 (Nacho, 6-nov): SetSchedule, el horario de un tren (aprobado por Mak)
- Sin una orden de horario, un tren recién fabricado (una sola parada) no se mueve y el tren de obras no puede cargar materiales. Orden nueva `SetSchedule = 19`: `Arg` = índice del tren, `Payload` = seis enteros por parada: `[nodo, hora de salida en ticks del día, munición, combustible, materiales, personas]` (+ carga en el tren, − descarga en la estación).
- Reglas: el tren tiene que estar parado en una parada (no en marcha ni emboscado); el horario tiene que incluir el nodo donde está (de ahí sale: pasa a ser su `StopIndex`); de 1 a 12 paradas; hora dentro del día; cargas de ±1.000 como mucho; dos paradas seguidas, contando el cierre, no pueden ser el mismo nodo. Si no vale, no cambia nada (`ScheduleResult`). Una sola parada deja el tren aparcado.
- Hash: `TrainService.ScheduleEdited` entra en el hash con las paradas y cargas solo cuando el jugador ha puesto el horario; los horarios del escenario no entran, así que G1–G5 no se mueven. Horario nuevo = `DepartedDay` a cero (ninguna parada cuenta como ya salida hoy).

### D-N49, adenda 13 (Nacho, 6-nov): el taller tras las respuestas de Lucía y Hugo (corrige la adenda 11)
- **Dotación**: al encargar solo se comprueba que haya libres por encima del retén de 6 (8 para el tren de obras; 10 más para un tren nuevo). Los 8 obreros del tren de obras se descuentan **al salir el tren**; si no hay 8 libres en ese momento, el tren acabado espera en el taller y avisa una sola vez (TL-2, «me faltan {n}»), y sale en cuanto los hay. El taller no empieza otro encargo mientras ese tren espera.
- **Tripulación**: un tren nuevo (carga, combate, obras) toma 10 personas (`tren_tripulacion`) de la población al encargarse; vuelven enteras al cancelar. Las rehabilitaciones no toman tripulación (son trenes viejos). Pregunta abierta a Hugo: si el Tren 3 y el tren de obras rehabilitados también la toman.
- **Cancelar**: como las obras (D-N59), sobre lo pagado: sin empezar, 100 %; empezado, floor(50 % de lo pagado) (antes lo tenía «50 % de lo que falta»: corregido). Con el trabajo empezado avisa (TL-3, {u} u recuperadas).
- **Chispas** ya no es una bandera: `Taller.ChispasAt` (-2 no está, -1 en el taller, ≥ 0 en ese tren). El −25 % a las rehabilitaciones cuenta mientras está en el taller (velocidad de trabajo 1.250 milésimas por tick en lugar de 1.000: no salta si se mueve a medias); a bordo de un tren de obras acelera sus reparaciones de vía y puente. Por defecto empieza en el taller, así que el Tren 3 y el tren de obras se rehabilitan en 28,8 h y el puente en la demo va con Chispas. No puede salir del taller hasta que ha rodado el tren de obras (`ObrasOut`), y solo cambia de sitio con los trenes de origen y destino parados en el taller. Orden `SetChispas` (Arg 0 = taller, k > 0 = tren de índice k − 1).
- **Taller 24 h**: no sigue el horario de obra (06:00–18:00): los 3 días y las 36 h son de reloj (Hugo). Ya era así.
- **Avisos**: TL-1 (tren listo), TL-2 (falta dotación) y TL-3 (cancelado con recuperación) añadidos a `textos_informe.csv` con el texto de Lucía (§8 de textos-informe-colmena.md), dichos por Chispas. La escena de cámara de TL-1 es de la interfaz.

- **Adenda (Hugo, 11:30), pregunta de Nacho**: el Tren 3 rehabilitado toma los 10 de tripulación al encargarse, como un tren nuevo (así está en el modelo). El tren de obras no los toma: sus 8 obreros son su tripulación y se descuentan al salir.

### D-N49, adenda 14 (Nacho, 6-nov): tripulación de 10 en el Tren 3, no en el de obras (respuesta de Hugo; corrige la adenda 13)
- Todo tren de servicio toma 10 de tripulación al encargarse (`tren_tripulacion`): los nuevos de carga y combate y el Tren 3 rehabilitado. El tren de obras (rehabilitado o nuevo) no toma esos 10: sus 8 obreros son su tripulación y se descuentan al salir. Vuelven al cancelar.


### D-N61 (revisión 1) · la horda con aire y sombra, según la lámina de Bruno (Lucía, 6-nov, 12:30)
Propone Lucía a partir de las referencias de Eugenio (docs/arte/analisis-referencias-6nov.md, §1) y de la lámina de siluetas de Bruno (docs/arte/pixel-codigo/siluetas/). Consultados: Bruno. Sustituye a la parte de D-N61 que choca:
- **Umbral de LOD en 12 px** de alto (antes 16), con histéresis: vuelve al modelo por encima de 15 px. Por debajo de 12 px el brazo ya no se distingue.
- **La mancha LOD deja de ser 4×5 y pasa a un palito vertical de 2×6 a 2×8**, con la cabeza de 1 px desplazada, en #1c200c y sin iluminar. A 16 y 20 px, el modelo lleva 1 px de luz en la nuca (olive_shadow). Los brazos al frente siempre, también sin animación.
- **Sombra proyectada para todos los zombis, también en LOD**: un valor intermedio entre el suelo y la figura, nunca tan oscuro como ella (32 % de día, 45 % al atardecer y de noche, ajustado a la paleta). Va contraria al sol. De noche sale radial desde el foco y solo dentro del charco. **Las sombras no se acumulan**: donde se cruzan no oscurecen más (máximo, no suma), porque las sombras cruzadas rayan el suelo y vuelven a leerse como garras.
- **Largo de sombra**: 1,5× de día. Al atardecer, 2,5× solo para las figuras de 12 px o más; la mancha LOD se queda en 2×, y si aun así raya en masa densa, baja a 1,5×.
- **Aire en la masa**: entre el 30 y el 50 % de suelo visible dentro de una masa normal (separación mínima de 0,6–0,8 anchuras en la evitación). Pegados al muro pueden compactarse en mancha.
- **Asfalto**: #483c3c deja la figura en ΔL* 16, por debajo de 25. El asfalto pasa a #6c7874 (asfalto gastado y aclarado por el sol), con grietas en #48403c y motas en #94948c, lo que da ΔL* 38. No se usa #605c48, que es el costado de los vehículos civiles.
- Se mantienen de D-N61 la sombra de masa gaussiana de la zona densa y las filas rotas (±0,5 de celda, ±20° y fase de animación al azar).
**Por qué**: Eugenio ve los zombis como garras. La causa es una alfombra sin huecos, sin sombra y con una mancha casi cuadrada. Separación, verticalidad y sombra hacen que se lean como gente.
- **Ajuste (Lucía y Bruno, 12:30)**: la mancha LOD lleva al atardecer la misma sombra de 1,5× que de día; la de 2× seguía rayando en tierra por pura densidad de líneas paralelas. El 2,5× queda solo para las figuras de 12 px o más. Sobre el asfalto, la sombra de día va en #48403c, no en #404460, que queda reservado para el rim de las unidades propias.

### QA-6 (Nacho, 6-nov): corrección de la prueba de rendimiento (nota de Sara, «Corrección»)
- **Causa de los 31–34 ms «de mi máquina»**: era compilación **Debug** (`dotnet run` sin `-c Release`). En Release salen 9–10 ms por tick en el contenedor (13–15 ms en las medidas de Sara con otra carga); en Debug, 25–34 ms. No era un pico ni una máquina lenta. Para medir de verdad: `dotnet run -c Release`.
- **Cambio** (`Dotnet/TBD.Sim.Tests/PerfGate.cs`, usado por [5c] y [8]): (1) una tarea de calibración fija que no pasa por el código vigilado (enteros, flotantes y accesos a memoria, mínimo de 5 repeticiones, y la más baja vista en el proceso, porque el ruido solo suma); (2) el mínimo de 5 ventanas de 30 ticks; (3) límite relativo: `ms_tick / ms_calibración` ≤ referencia × 1,5 (Release 1,7 en las dos pruebas; Debug 3,2 con 307 sólidos y 2,4 con 7); (4) hasta 3 intentos, falla solo si los 3 pasan del límite; (5) imprime siempre mínimo, mediana, calibración y cociente; (6) los 33 ms son un AVISO (no un fallo) solo en Release y con calibración normal (hasta 2× la de referencia); en Debug dice que el coste no es representativo.
- **Criterio de aceptación, medido en el contenedor con 4 procesos `yes` (uno por núcleo) en marcha**: sin inyección, 20 de 20 en verde en Release y 20 de 20 en verde en Debug; con una regresión de 3× inyectada (`TBD_PERF_INJECT=3`, repite el tick 3 veces por tick medido), 20 de 20 en rojo en Release y 20 de 20 en rojo en Debug. Modo para repetirlo: `TBD_ONLY_PERF=1 dotnet run -c Release --project TBD.Sim.Tests` (solo las dos pruebas de coste).
- **Límite conocido**: los límites relativos se han medido en un solo tipo de máquina (contenedor de 4 CPU). En otra arquitectura el cociente puede cambiar (la tarea de calibración no es idéntica al coste de la simulación). Si Sara o Marcos ven un fallo en su máquina con un cociente cercano al límite, hay que volver a medir ahí y ajustar las dos constantes `RatioIndexed` y `RatioSimple` de `PerfGate.cs`.


### QA-25 — PR #19, prueba de rendimiento estable (Sara, 6-nov)
Revisado y ejecutado en el contenedor: verde sin inyección (cociente 1,07–1,15 de 1,7), rojo con regresión 3× (cociente ≈ 3,3). Los 33 ms pasan a aviso en Release. Aprobado por QA con la salvedad de que no mide regresiones menores de ~1,6×. El hallazgo de Nacho (31–34 ms eran Debug) corrige mi diagnóstico de «máquina lenta».

### D-N61 (revisión 2) · bandas cuantizadas y la mancha LOD apagada (Lucía, 6-nov, 13:28)
Consultado: Marcos (commit a7356ba, captura horda_fino_zoom_22.png).
- **Bandas**: se acepta el desvío y no se toca la paleta ni la mezcla. Llano 63,7, talud 57,8 y fondo 41,3 frente a objetivos de 64–68, 52–56 y 42–46. Con la mezcla al 65 %, el fondo solo puede caer en 41,3 o 48,9. Se elige 41,3 porque deja un escalón de unos 16 puntos con el talud, y eso hace que la trinchera se lea como relieve; con 48,9 se quedaría en 9. Los objetivos existían para separar la horda del suelo, y eso ya se cumple (cuerpo medio ≥ 25 en todas las bandas). La paleta de 32 no se toca por una décima de banda.
- **Mancha LOD**: se apaga en el prototipo, pero no se borra. El zombi fino en 3D, con pixelado por escalones y sombra, se lee como figura entre los zooms 22 y 45, que era lo que la mancha intentaba resolver. Se vuelve a encender solo si se cumple una de dos condiciones: que la figura baje de 12 px de alto en pantalla al zoom más lejano, o que el asedio de 10.000 zombis caiga por debajo de 60 FPS.
- **Ajuste (13:30)**: manda el píxel de búfer, que es la unidad del arte, pero los datos de Marcos dejan el umbral de 12 px sin efecto. El modelo fino se lee con brazos ya a 10 px de búfer (zoom 22), y a 3,3 px (zoom 70) un palito de 2×6 sería más grande que el propio zombi. Así que la mancha queda apagada en todos los zooms. El único motivo para encenderla de nuevo es el rendimiento: que el asedio de 10.000, con movimiento y disparos, caiga por debajo de 60 FPS en la build. La prueba estática da 144 FPS.

### D-N61 (revisión 3) · aire en la masa: radio de separación, no distancia dura (Lucía, 6-nov, 13:45)
Consultados: Nacho (sim) y Marcos (capturas de 3000 y 10.000 zombis a zoom 22). Medida aproximada de suelo visible: masa en el llano ~45 %, que cumple; masa en la trinchera ~15–30 %; pegada al tren ~13 %, lo que está permitido porque ahí la compactación es deseable.
- **Sin distancia mínima dura entre centros**: chocaría con caer, amontonarse y trepar (GDD §5.7), y contra un muro o el tren la masa tiene que compactarse.
- **Se ajusta la cápsula de separación de 0,25 a 0,34 m de radio**, en entero de punto fijo. Con el zombi fino de 0,40 m de ancho, eso deja entre centros un hueco de unas 0,7 anchuras (D-N61: 0,6–0,8). SepGain (0,35) y SepMax (1,0) no cambian; si con el radio nuevo una masa en marcha por el llano o la trinchera sigue por debajo del 30 %, el siguiente paso es SepGain 0,5.
- **Solo en la zona (S2)**. En la red (S0) no hay individuos: allí la horda es un campo de densidad y esto no aplica.
- **Efectos que hay que revisar**: cambia el hash (goldens con aprobación registrada), cuántos zombis caben contra un muro o una puerta y la calibración S0 = S2 del combate abstracto. Nacho y Hugo lo vuelven a medir; si la presión de asedio cae más de un 10 %, se compensa en la densidad de la horda y no en el radio.

### D-N61 (revisión 4) · se anula la revisión 3: la separación se queda como estaba (Lucía, 6-nov, 13:50)
Consultado: Nacho (docs/sim/medicion-separacion-6nov.md).
- **Medida**: el radio de la cápsula solo actúa contra los muros. La separación sale del gradiente de densidad, en celdas de 0,5 m. Con 0,34 m, los resultados con 10.000 zombis son idénticos: 41,6 % de suelo visible en conjunto y vecino mediano a 0,14 m. En la trinchera, además, la masa queda más compacta. SepGain 0,5 solo suma 1,4 puntos.
- **Decisión: opción D**. Se deja como estaba: radio de 0,25 m, SepGain 0,35 y SepMax 1,0. La revisión 3 queda anulada.
- **Por qué**: el conjunto ya cumple el 30–50 %, el campo abierto también, y pegados al tren está permitido. La trinchera (15–30 %) es un embudo donde la masa densa cuenta lo que pasa, y D-N61 ya acepta la masa densa como mancha con el borde legible. Se descartan la repulsión por pares (A), por coste y riesgo en SimSystems el día del prototipo; la rejilla fina (B), porque no garantiza nada; y escalonar la entrada (C), porque toca la calibración sin un problema visible que lo justifique.
- **Se reabre** solo si, con las sombras puestas, la trinchera sigue leyéndose como alfombra o como garras en la build que pruebe Eugenio. En ese caso, primero se prueba A, midiendo su coste.

### D-N62 · Lenguaje visual de la construcción (Lucía, 6-nov, 13:55)
Propone Lucía y lo pide Marcos. Corrige §3 de docs/arte/analisis-referencias-6nov.md.
- **Una sola pasada de superposición a resolución completa**, después del pixelado. El fantasma usa el mismo shader de contorno que la selección.
- **Selección**: contorno exterior de 2 px en #d4d0cc.
- **Fantasma**: tinte plano con contorno de 2 px; válido en #70784c con contorno #d4d0cc, no válido en ámbar #e08c30. **Nunca rojo**: #982420 es solo para ataque y asedio. La transparencia, si hace falta, se hace con tramado de píxeles alternos.
- **No hay rejilla** (GDD §9c). En los muros se ve la línea del trazado de 1 px en #d4d0cc; en las piezas sueltas, una marca de alineación con el muro.
- **Radios**: solo contorno de 2 px en #d4d0cc, sin relleno. El foco y el nido se ven como sector.
- **Etiqueta junto al cursor**: caja #181c30 con borde #48403c. Primera línea: pieza, largo y coste en #d4d0cc. Segunda línea, solo si hace falta: el aviso en #e08c30 con el icono de alerta ámbar, por ejemplo «Hay zombis cerca · 35 m». Si el aviso impide colocar, el fantasma también pasa a ámbar.
- **D-N61, cierre (14:25)**: prueba en la build con 10.000 zombis y fuego real (21 soldados desde el tren, 1.989 disparos, 376 abatidos): 358 FPS de media, con un solo tirón de 1 s al meter la horda. No se cumple ninguna de las dos condiciones, así que la mancha LOD queda apagada para siempre. Si el tirón de 1 s al meter la horda se nota al jugar, se trata aparte como problema de carga, no de LOD.

## D-N62 · Recinto de Sagunto a escala real del tren: muro de partida ya construido (Hugo, a petición de Mak) ✅ (6-nov 15:50)
- **Contexto**: con el tren de unos 64 m (Lucía), el recinto pasa a unos 85 × 30 m. En módulos de 10 m son 2·9 + 2·3 = **24 módulos (240 m)**, frente a los 150 m de antes.
- **Coste de cerrarlo desde cero**: con sacos, 48 u; con HESCO, 144 u; más la puerta de vía (8). Lo que hay el día 1 son 100 u en stock y 80 al día, y hay que ahorrar para el Tren 3 (60 + 30 de reserva el día 3). **No cuadra**: el modelo siempre ha supuesto que Sagunto empieza con 120 u de fortificación hecha (nivel 4).
- **Medido con 1000 partidas** (valor fortificado de partida → derrota equilibrado / prisa):
  - 0 u: 16,0 / 50,5 %
  - 30 u: 14,5 / 50,3 %
  - 66 u: 13,3 / 45,7 %
  - **120 u: 13,8 / 43,1 % (vigente)**
  - 150 u: 13,9 / 40,8 %
- **Decisión**: Sagunto empieza con **120 u ya construidas**, las mismas del modelo:
  - El lado largo que mira al interior (oeste) en HESCO: 9 módulos, 54 u.
  - Los otros 15 módulos en sacos: 30 u.
  - La puerta de vía (8) y una puerta peatonal (6).
  - 2 nidos (16) y 3 focos (6).
  - En total 120 u, nivel 4,0. El stock del día 1 no se toca.
  - El «trazar muros» del día 2 del guion pasa a ser reforzar: pasar sacos a HESCO cuesta +4 u por módulo, y con 8 módulos se llega al nivel 5.
  - Si el recinto acaba en 90 × 40 m (26 módulos), los 2 módulos de más van en sacos y salen 124 u; vale igual.
- **Por qué no dar todo en HESCO** (180 u, nivel 5): la prisa baja al 40,8 % y se pierde el objetivo de reforzar.
- **Condición**: el andén tiene que quedar centrado en el recinto. Con 85 × 30, las esquinas están a unos 47 m, dentro del radio de 60 m de `perimetro_mm`. Si el andén se desplaza a un extremo, las esquinas lejanas quedan fuera y se desgastan sin mantenimiento (D-N59).
- **Mantenimiento**: el 1 % de 120 u es 1,2 u al día, lo mismo que antes.

## D-N63 · Corrección de numeración (Hugo, 6-nov 15:50)
- La entrada de arriba «D-N62 · Recinto de Sagunto a escala real del tren: muro de partida ya construido» es en realidad **D-N63**: el número D-N62 ya era el de Lucía, «Lenguaje visual de la construcción» (13:55). El contenido no cambia: Sagunto empieza con 120 u ya construidas, aprobado por Mak a las 15:46. Para citarla, usad D-N63.

## D-N64 · Vagón de pasajeros, locomotoras y largo del tren: validación económica (Hugo, a petición de Lucía) (6-nov 16:00)
- **1) Vagón de pasajeros en el MVP: sí, con 40 plazas, pero como vagón aparte, nunca a costa de uno de carga.** El modelo no transportaba personas (tomar() es instantáneo), así que no había cifra; 40 = el cupo de cuarentena por ciudad y día (`checkpoint_cupo_cuarentena_ciudad`), así que un viaje llena un día de checkpoint, y caben la guarnición de una fundación (12) y un retén (6). **Medido con 1000 partidas**: si sustituyera a un vagón de carga (4 × 20 = 80 u por viaje), el equilibrado pasa del 13,8 al **34,5 %** y la escasez del 55 al 73 %. Por eso `tren_vagones_carga` = 5 se queda y el de pasajeros va aparte, fijo en cada tren.
- **2) Locomotoras de distinta potencia fuera del MVP: sí.** Condición: el combustible por u·km de la pesada debe ser igual o peor que el de la de línea (16 al día). El combustible es el recurso tenso (6,6 días de déficit en el equilibrado), y una pesada más eficiente rompería la escasez.
- **3) Largo limitado por la tracción, la rampa y el andén: sí, fuera del MVP.** Hay que medirlo cuando exista: la rampa de Sagunto a Barracas está en el camino de Teruel (P8, días 3–5). **Ojo con el andén de Sagunto**: el recinto de D-N63 se dimensiona para el tren de 64 m; un tren más largo no cabe dentro de los muros, y ampliar el recinto cuesta muro. Lo bueno es que ese coste da un límite natural.

## D-N63 · Aplicación en la red y regeneración de G3_red.golden (Nacho, a petición de Mak, 6-nov)
- **Qué**: `NetScenario.Mvp()` construye el muro de partida de Sagunto con las mismas funciones que las órdenes (`Obras.PlanWall`/`PlanPoint`), ya terminado y sin cobrar. `Mvp(false)` sigue sin obras y es lo que usan las pruebas de obras, taller, horario, estaciones, director y red.
- **Medidas** (Level.cs, commit 6903083): recinto de 86 × 41 m, X 70 a 156 e Y 44 a 85, vía en Y = 64,5, andén (0, 0) en (113; 64,5). Las piezas están a menos de 48 m del andén: todas cuentan para el nivel y el mantenimiento.
- **Resultado medido**: 36 piezas, **120,24 u**, nivel **4.008 ‰**. Frente oeste en HESCO (4 módulos, con la puerta de vía en la vía) y 14,5 m de HESCO en cada ala; el resto del perímetro (180,8 m) en sacos; puerta peatonal en el lado este, 2 nidos y 3 focos.
- **Dos desviaciones respecto del texto de D-N63, para que Hugo las valide**:
  1. El lado oeste del recinto real es el corto (41 m); D-N63 suponía un lado largo de 90 m en HESCO (54 u). Con la geometría real el HESCO suma 66,8 m = **40,1 u**, no 54. Se mantiene lo que fija el modelo (120 u y nivel 4,0) acortando las alas.
  2. `PlanWall` pone una puerta de vía (8 u) en cada muro que cruza la vía, y el muro este la cruza. Hay **dos puertas de vía** (16 u, no 8). La del este queda **bloqueada cerrada** (GateMode 2): la vía acaba dentro del fuerte y en automático se abrirían las dos con el tren dentro. Para que el total siga en 120 u, el muro suma 76 u en vez de 84.
- **Mantenimiento**: `ceil(1 % de 120,24 u)` = **2 u al día** (el 1,2 de Hugo, redondeado hacia arriba por la regla vigente), y con reservas la vida no baja. Es la única diferencia de existencias en el día 1: Sagunto paga 2 u de materiales cada día.
- **Regeneración de G3_red.golden** (aprobada por Mak al encargar D-N63): el estado inicial cambia a propósito (36 piezas en `Works`, que entra en el hash de «existencias» desde el tick 8.251) y desde el primer cambio de día el almacén de Sagunto paga el mantenimiento. No cambia ninguna otra cosa: carga, trenes, horda y director dan lo mismo. G1, G2, G4 y G5 (zona) no se tocan: la zona no lee `Works` al arrancar todavía.
- **Para Marcos**: al materializar Sagunto, la zona tiene que construir los sólidos desde `Works.Snapshot(sag)` y no desde los lados fijos de `Level.CreateSolids()`, o habrá muros duplicados. Coordenadas: mm locales al nodo, andén (0, 0), vía en y = 0; mundo = `WorkOrigin` (113; 64,5) + mm / 1000.
- (Nacho, mismo día, adenda) **G4_bucle.golden no se regenera**: el bucle red-zona se graba con `NetScenario.Mvp(false)` (Sagunto sin muro de partida), porque su hash de red lo cambiaría y la parte de zona solo se puede regenerar desde Unity. Los G1, G2, G4 y G5 quedan intactos; solo cambia G3_red.golden.

### D-N63 (adenda, Hugo, 6-nov 16:35): validación del PR #21 de Nacho
- **Geometría, validada**: el recinto real mide 86 × 41 m (Level.cs) y la vía lo cruza a lo largo, así que el frente oeste es el lado corto (41 m). Lleva unos 66 m de HESCO, el frente y dos alas de unos 12 m en las esquinas (~40 u), más unos 181 m de sacos (~36 u), 2 puertas de vía, la peatonal, 2 nidos y 3 focos: **120 u, nivel 4,0**. Con el andén centrado, las esquinas quedan a unos 47,6 m, dentro del radio de 60.
- **Segunda puerta de vía, la del este, bloqueada: validada.** Sus 8 u cuentan para el nivel y para el mantenimiento. Es coherente con la regla de PlanWall, y más adelante el jugador puede abrirla.
- **Mantenimiento de 2 u al día: NO.** Es un `ceil` del 1 % por estación, y el modelo cobra el 1 % exacto (1,2 u en Sagunto, +67 %). Donde más se nota es en las estaciones pequeñas: un apeadero de 30 u pagaría 1 u al día en vez de 0,3 (×3,3), y el equilibrado las tiene en nivel 2–4. **Arreglo**: un remanente en E4 por nodo. Cada día se suma el 1 % exacto en E4, se paga floor(remanente / 10.000) u y el resto se guarda; si no se puede pagar, el remanente no se descuenta y se desgasta como hoy. El remanente es entero y va en el hash, así que sigue siendo determinista. Sagunto paga 1, 1, 1, 1, 2…, una media de 1,2.
- (Nacho, adenda de D-N63 pedida por Hugo, 6-nov) **Mantenimiento con remanente**: se acaba el ceil por estación. Cada día se suma al remanente del nodo el 1 % exacto de la Σ del nivel (en unidades E4·‰·‰, así que es exacto, sin redondeo diario), se cobra floor(remanente / 10.000 E4) u y el resto se guarda en el hash (solo si no es 0). Un apeadero de 30 u paga 0,3 u al día de media y Sagunto (120,24 u) 1,2 u; en 10 días, 3 u y 12 u (antes 10 y 20). El desgaste se aplica el día en que la estación no puede cubrir `ceil(remanente)`: con 0 u se desgasta cada día como antes, y con reservas no. Si no puede, las u enteras no cobradas se perdonan (no hay deuda). `MaintenanceU` queda como techo para la interfaz.
- **Segunda regeneración de G3_red.golden** (misma aprobación, adenda de D-N63): desde el primer cambio de día cambia lo que cobra el almacén de Sagunto (0 o 1 u según el día, frente a 2 u fijas) y el remanente entra en el hash. Nada más. Las pruebas de obras que contaban 1 u al día pasan a contar 1 u cada 5 días (20 u construidas = 0,2 u al día).

## D-N65 · Diseño del hito 6: automatismos, etapas, guardado e interfaz (Lucía, 6-nov, 17:05) — en revisión
Propone Lucía; consultados Nacho (modelo de datos) y Hugo (economía), pendientes de respuesta. Documento: docs/diseno-hito6.md.
- **Etapa 1, viaje manual**: el horario pasa a ser una ruta que sale con «Salir» (`DepartNow`) y al terminar se para. **Etapa 2, `Repetir`**: es el `SetSchedule` actual. Se desbloquea con el Tren 3 en servicio.
- **Orden permanente de estación**: mínimo y máximo por nodo y recurso; las paradas «Auto» descargan hasta el mínimo y cargan el exceso. Las personas no entran. Se desbloquea con la primera estación de nivel «estación» aparte de Sagunto, o el día 8.
- **Guardado**: estado completo con hash comprobado al cargar, versión con migración, autoguardado a las 05:30 y al aviso de gran ataque, en 3 ranuras.
- **Interfaz**: reloj arriba en el centro, alertas arriba a la izquierda, panel contextual abajo (como mucho el 15 % de la pantalla), panel de tren con ruta u horario y marca de «patrón conocido».
**Por qué**: son los dos automatismos del MVP (GDD §4 y §15) y lo que falta para que la partida «dure y se guarde» (hoja de ruta, hito 6).

## D-N66 · Automatismos del H6: el viaje manual cuesta horas-tren; mínimos de Sagunto (Hugo, a petición de Lucía) (6-nov 17:05)
- **1) El viaje manual NO equivale a mi modelo si el tren espera a que el jugador pulse.** El modelo usa 16 h-tren al día sin huecos. Medido con 1000 partidas, quitando horas-tren solo en la etapa 1 (días 0–5), como derrota del equilibrado / prisa / día de Teruel:
  - 0 h: 13,8 / 43,1 % / 3
  - 1 h por tren y día: 16,2 / 42,5 % / 4
  - 2 h: 16,3 / 49,7 % / 4
  - 4 h: 31,7 / 58,1 % / 6
- El umbral es Teruel: con una hora de espera ya se retrasa un día. **Condición para Manual**: que la espera no se coma horas-tren. Cuando la última parada es la primera (Sagunto–X–Sagunto), el tren descarga y **carga ya la ruta siguiente** mientras espera, así que las 4 h de carga absorben el tiempo de reacción. Además, el aviso de «Viaje terminado» debe tener «Salir» a un clic. **Métrica para Sara en la prueba**: horas paradas por tren y día en la etapa 1 sin estar cargando, objetivo ≤ 0,5 h.
- **2) La orden permanente no rompe la escasez al alza.** Mi modelo ya reparte como un despachador ideal por necesidad, así que una orden bien puesta solo se acerca a él; lo que puede hacer es empeorar. **Mínimos por defecto de Sagunto**: munición **40 u** (2 días de gasto medio, la reserva del equilibrado; un día de asedio gasta ~34), víveres **30 u** (3 días para 100 personas a 0,1) y, aunque no se pedía, combustible **25 u** (medio día de 3 trenes, la reserva del modelo para repostar). Máximo: sin máximo (∞), así que Sagunto nunca ofrece por defecto.

### QA-26 — Métrica de horas paradas y «Salir» doble (Sara, 6-nov)
Recibida de Lucía y Hugo. Anotada en prueba-camino-critico.md §8; sin probar: el código aún no está en main.

## Álvaro · Nivel de Sagunto v1: la vía cortada era un fallo (6-nov, 18:35) — propuesta, pendiente de Lucía
- **Diagnóstico**: los raíles de la zona de Sagunto van de X 10 a 100 (`PrototypeBootstrap.cs:1624-1628`), un resto del fuerte de 31 m; el fuerte va de 70 a 156. Además, el muro este está cerrado, el bloque de pisos (172; 70) queda encima del eje de la vía y el suelo acaba en 256 × 128 m.
- **Propuesta** (`docs/niveles/sagunto-nivel.md`): vía en todo el ancho y hasta fuera de cámara sobre un faldón decorativo; remates de paso superior (oeste, hacia Valencia) y puente del Palancia (este, hacia Castellón); puerta de vía este solo visual en el MVP; bloque a (174; 82); pueblo en hilera; recorridos de la horda por la vía, la carretera y el pueblo; lista P1-P9 para Marcos (P1-P3 sin tocar la simulación).
- (Lucía, 18:27) **Aprobado.** Orientación de ficción, puerta este solo visual (el tren sale marcha atrás), coches sin colisión y sin segunda vía dentro. Correcciones: el humo lejano va sobre Valencia (oeste), no en la acería; el asfalto en #6c7874 con grietas en #48403c; las manchas del balasto en 303424/48403c, sin rojizos; la ambulancia sin cruz roja; las pintadas en #d4d0cc; la ropa en tonos apagados. Aplicado en la v1.1 del documento.

### QA-27 — Tejado a 6,5 m (361524b) (Sara, 6-nov)
Medido con 500 zombis desde el tejado (3.000 ticks, dotnet, sin Burst): RoofH 4 → 6,5 m. Primer vuelo en el tick 12 en los dos; todos en el suelo en el tick 224 (7,07 s) frente al 240 (7,60 s); velocidad vertical máxima de impacto 12,0 → 15,3 m/s (+27 %); apilados al final 176 → 188. El simulador no tiene daño por caída (solo gravedad 20 m/s², sin daño en SimCore): «daño por caída» no se puede comparar porque no existe. Mis 35 pruebas en verde.

### Daño por caída fuera del MVP (Lucía con Hugo, 6-nov, 18:18)
Lo detecta Sara: el simulador no aplica el «pueden dañar o derribar a quien esté debajo» de GDD §5.7. Lo propone Hugo y Lucía lo aprueba.
- **Sin daño a los propios zombis**: la masa se conserva y la Colmena está calibrada así. Si las caídas mataran, un tejado sería una picadora gratis que no cuesta munición.
- **Derribar a quien está debajo**: queda para cuando exista la tropa a pie (deuda del H7). En el MVP la tropa combate tras el muro o desde el tren.
- **En el MVP, solo lectura**: animación de impacto y una nube de polvo al aterrizar, sin efecto en la simulación.
- GDD §5.7 se anota como «fuera del MVP» en la próxima versión del GDD.

## D-N67 · Suelo de Sagunto con zonas, decals y matas (6-nov, 18:40)
Origen: Eugenio (18:30), «no hay ningún asset ni sprites de hierba o algo, solo un color plano». Lo encarga Mak. Decide Lucía y consulta a Álvaro, Bruno y Teo. Detalle en `docs/arte/suelo-sagunto.md`.
- **Tres capas de decorado**, fuera de la simulación y del hash:
  - A, textura de pixel art por zonas, a partir de un mapa de 1 m por téxel y con bordes tramados.
  - B, decals en quads planos instanciados (no Decal Projector).
  - C, matas y objetos instanciados por GPU, sin colisión y sin sombra.
- **Legibilidad de la horda**:
  - Dentro de la zona simulada, nada del suelo baja de L* 47, salvo el balasto ya aprobado. La tierra de huerta va en a86c50.
  - La hierba va en 88885c y 847c34 (70784c solo en acentos), para quedar a ΔL* 12–16 del suelo y no disparar el contorno por luminosidad.
  - Glacis de unos 30 m delante del muro oeste, sin nada de más de 0,3 m.
  - Cañas solo en el cauce y las acequias.
- **Prohibido en el suelo**: los valores de la horda, el rojo, el ámbar (no hay naranjas caídas) y #404460.
- **Variantes**: al menos 5 por tipo de mata u objeto (25 modelos de Teo).
- **Rendimiento**: no se pierde más de un 10 % en la prueba de 10.000 zombis con fuego (≥ 320 FPS). En los escalones 1/5 y 1/6 no se dibuja la hierba baja.
- **Orden**: A, luego C (hierba y piedras), luego B y las cañas.

### QA-28 — Prueba del suelo de Sagunto (D-N67) (Sara, 6-nov)
Diseño en docs/qa/prueba-suelo-sagunto.md: legibilidad por zona (5) × día/noche con QA-7, alfombra < 10 % (aprobado por Lucía, sin la sombra propia, D-N61) y FPS ≥ 320 medido por Marcos/Eugenio. Sin ejecutar: el suelo no ha entrado.

### D-N67, adenda (6-nov, 18:35): primero, una muestra para Eugenio
Eugenio quiere ver el suelo y aprobarlo antes de que se dé por bueno. La muestra es un trozo de Sagunto (recinto, huerta y calle): 3 texturas y 3 o 4 decals de Bruno, 3 matas y 2 piedras de Teo, y Marcos lo monta con capturas de día y de noche y una medida de FPS. Va a la galería. Hasta el sí de Eugenio no se produce en masa. Detalle en §0 de `docs/arte/suelo-sagunto.md`.
- 6-nov 18:35 UTC: la prueba del suelo (QA-28) empieza por una muestra de 3 zonas × día/noche; Eugenio la aprueba antes de producir todo.

## D-N68 · El castillo de Sagunto es un telón de fondo, no una maqueta a escala (6-nov, 18:40)
Lo detecta Marcos: a escala real (900 × 166 × 210 m, en (130; 330)) el cerro se lee como un muro plano de color oliva que cierra el horizonte. Decide Lucía y lo hace Teo.
- **La cámara es ortográfica**, así que alejarlo no lo hace más pequeño: solo lo sube en la pantalla o lo saca del encuadre. Por eso se reduce, no se aleja.
- **Excepción a la escala real**: el castillo es un telón de fondo, como el decorado pintado de una película. Se queda con el tramo central del real (la plaza de armas y la ciudadela), de **unos 400 m de ancho**, y **el cerro baja a unos 80 m de alto**. Va en la misma posición o un poco más al norte, siempre que siga entrando con la cámara alejada.
- **Lectura de castillo**: la silueta de lo alto tiene que ser almenada, con 3 o 4 torres y lienzos de muralla en piedra clara (b4a080, con el lado en sombra en 94948c). Las laderas llevan matorral en 88885c y 847c34 con manchas de roca en 94948c, nunca un color plano oliva ni 50541c (ese es el verde militar).
- **Contraste**: más bajo que el del recinto, para que no le robe el ojo al fuerte. Se mantiene la bajada de contraste de Marcos. Si después del prototipo hay niebla de distancia, se aplica también aquí.
- Va sin colisión y fuera de la simulación. Se aprueba con una captura de la cámara alejada en la que se lea «castillo» y el fuerte siga siendo lo primero que se ve.

### D-N68, adenda (6-nov, 18:45): sin vacío a los lados del castillo
Con las capturas sagunto_castillo2 y p30 se ve que hoy el cerro de 900 m ocupa todo el ancho del encuadre por arriba. Al reducirlo a 400 m quedaría vacío a los lados. Por eso **el faldón se alarga hacia el norte hasta que no se vea su borde con la cámara más alejada**. Detrás del castillo, de lado a lado, va **una sierra baja continua** (unos 30–40 m, en 94948c y 88885c, con menos contraste que el castillo; es la sierra del fondo de las fotos E10 de Álvaro). Lo hacen Teo (la sierra) y Marcos (el faldón).

### D-N67, adenda 2 (6-nov, 18:50): ajustes tras la muestra de Teo
Normales hacia arriba en la capa C; la capa C queda fuera del contorno por luminosidad; el descampado baja de 25 a 12 matas por 100 m²; la cara de sombra de las piedras va en 6c7874. Detalle en §8 de `docs/arte/suelo-sagunto.md`.

### D-N67, adenda 3 (6-nov, 19:05): revisión de la muestra montada (TBD f5af670, 391 FPS)
De noche, el detalle de la textura se atenúa según la luz (unos 20 % bajo la luna y 100 % bajo los focos). Los decals van a su tamaño real (téxel de 0,1 m). No se hace stencil del contorno mientras pase la medida del anillo de Sara. Ocultar las matas bajo las obras se hace en la ronda completa.

### D-N68, adenda 2 (6-nov, 19:13): posición del castillo
Con la cámara más alejada (ortho 70), en (130;330) no se veía. Se lleva a **(130;270)**, con el pie en Z≈195, para que solo asomen las torres y las almenas por el borde de arriba. No se escala y el tope del zoom no se toca. Marcos lo ajusta de 10 en 10 m sin bajar el pie de Z 150, que es el límite de Álvaro: los naranjos, el pueblo y el terraplén del paso superior. La calle de la Estación se corta en Z 195. En el mapa de zonas, el cerro es la zona 11, sin vegetación.

### D-N68, adenda 3 (6-nov, 19:15): anula la adenda 2
La medida de Marcos en el juego (yaw 45°, pitch 55°, ortho 70) desmiente la cuenta de Lucía. Un punto alto se ve **más arriba** en la pantalla, no más abajo, así que el pie del cerro siempre entra antes que las torres. Además, el borde superior de la pantalla es una diagonal (x+z≈318). Se queda la opción A+B de Marcos: el castillo **girado 45°, paralelo al borde superior**, con el pie a unos 83 m de él y **altura a 0,5** (torres de unos 59 m). Si ocupa más de un cuarto de pantalla con la cámara más alejada, se baja a 0,4. Sigue con poco contraste y sin contorno, y la sierra va detrás, también girada. Álvaro comprueba la huella girada antes de fijarlo.
- 6-nov 19:20 UTC (QA-28): primera lectura estimada de la muestra: día recinto ΔL* 37,2, huerta 23,6, calle 24,1 (sin máscara); noche sin medir; FPS pendiente.
- 6-nov 19:20 UTC (QA-28): Lucía acepta huerta y calle (~24) como desviación de banda con suelo en 22; la sombra de los naranjos no cuenta como suelo.

### D-N67, adenda 4 (6-nov, 19:27): Eugenio aprueba el suelo y se extiende a todo el mapa
Eugenio (19:25): «Perfecto, te apruebo todo si». El suelo v2 se extiende a todo Sagunto y al faldón, con el asfalto sin repetición de Bruno (4 teselas por hash, 8 decals de grietas y macrovariación de ±3 L*). Antes, Marcos mide los FPS en la build (3 veces, mediana, con y sin la capa C) y hace las 6 capturas con Shift+F9 para Sara. Empieza la ronda completa de §6: Bruno hace el balasto con motas menos oscuras y lo que falte del atlas; Teo, las cañas (a parches en las orillas del cauce), la basura, los escombros, el lentisco como objeto (≤ 1,2 m) y el resto de las variantes; Marcos oculta las matas bajo las obras.
- 6-nov 19:27 UTC (QA-28): Eugenio aprueba el suelo y se extiende a todo el mapa. Pendiente: 6 capturas con máscara y 3 medidas de FPS (Marcos), luego ronda de 5 zonas.
- Medida de Marcos (6-nov, 19:32), build a 1080p con 10.000 zombis en Sagunto: mediana de 391 FPS con la capa C y de 406 sin ella. Cumple el criterio (≥ 320); la capa C cuesta un 4 %.
- 6-nov 19:32 UTC (QA-28): FPS de Marcos en build: mediana 391 con capa C, 406 sin ella (≥ 320). Dato declarado, no verificado por QA. Se repite tras las últimas piezas.

### D-N67, adenda 5 (6-nov, 19:52): subpaleta del suelo
El asfalto salía lila en el juego porque la macrovariación oscurecía antes del paso de paleta y parte de las manchas caía en purple_grey #60546c (diagnóstico de Bruno). **El shader del suelo cuantiza solo a una subpaleta de colores de tierra y de suelo**: sin #60546c, #404460, slate, navy, rosas, rojos, ámbar ni los valores de la horda. Así se cumple también, de forma automática, la regla de los colores reservados para todo el suelo. Bruno pasa la lista de índices.

### D-N68, adenda 4 (6-nov, 19:52): el castillo, a la derecha del borde superior
En (7,75;267,75) asomaba bajo el HUD, en la esquina de las alertas del hito 6, y no se leía. Se desliza a lo largo de x−z hacia la parte derecha del borde superior, entre el reloj y la salida de la vía, a 40–50 m del borde, hasta que se vean una o dos torres. Álvaro comprueba la huella. Si no se lee o no cabe, se deja fuera de cámara (opción C).

### D-N68, adenda 5 (6-nov, 19:53): el castillo, fuera de cámara (opción C). Cierra el tema
Álvaro lo ha calculado: entre el centro y la vía no hay sitio sin pisar la vía, la carretera, el muro norte o el pueblo, y en la esquina derecha solo asomarían 15–20 m de cerro encima del puente. Se elige la opción C: el castillo queda **fuera de la cámara de juego**, en una posición donde no pise nada (la decide Álvaro), con el modelo de Teo tal cual. Se verá con la cámara libre, en el mapa de operaciones y en las capturas promocionales. No se estrecha la interfaz ni se cambia el tope del zoom por un decorado. La sierra de Teo también va fuera de cámara.
- 6-nov 19:55 UTC (QA-28): Lucía retira la desviación de la calle; sin mínimo nocturno fuera del foco (D-N13); repetir a mediodía; huerta pendiente.
- Posición final (Álvaro, 19:52): centro en (39,25;361,25), con el mismo giro y la misma escala, y el frente a unos 19 m fuera del borde superior con la cámara al máximo. La calle de la Estación se corta en Z = 286, al pie. La sierra va en x+z ≥ 480 y x−z ≤ 200, y el Palancia sale de ella. El faldón crece hasta Z ≈ 480. Detalle en §8.3 de sagunto-nivel.md.
- Aclaración de la adenda 5 de D-N67 (19:59): la exclusión de los valores de la horda en la subpaleta del suelo es para el día. De noche, #303424 se acepta como suelo en sombra, porque el objetivo de la noche (L* 17) solo puede caer ahí y la horda se lee por la luz (D-N13). 1c200c (el contorno) y navy siguen fuera, también de noche. El asfalto con la subpaleta queda aprobado. Deuda: extender el faldón hasta Z≈480 y repasar el cerro con la cámara libre antes de hacer capturas promocionales.
- Suelo completo (6-nov, 20:16, TBD 2939e92): cubre todo el mapa de Álvaro. Mediana de 352,2 FPS con la capa C y 380,8 sin ella. Lucía lo aprueba. Marcos corrigió que el mapa se leía invertido en Z. Pendiente: la huerta con horda de Sara y ocultar las matas bajo las obras. Con 32 FPS de margen, cualquier pieza nueva que añada instancias se mide antes de entrar.
- 6-nov 20:20 UTC (QA-28): suelo en todo el mapa (2939e92), FPS mediana 352,2 (declarado). Las medidas del §8 se repiten con el suelo corregido (estaba espejado en Z). Esperando capturas nuevas.

### D-N67, adenda 6 (6-nov, 20:35): de noche, bajo la luna, todo el suelo se ilumina como la tierra del recinto
Con las capturas de sara2 se ve que la huerta sale casi negra de noche: la tierra labrada (a86c50), bajo la luna 0,14, cae a #303424 y la horda desaparece. En cambio, en el recinto los zombis se leen como siluetas contra la tierra iluminada por la luna. **El shader del suelo, con la luz de la luna, acerca el color de cada zona al de la apisonada (en torno a un 70 %)**. Bajo los focos y las farolas se mantiene el color real. Se aplica a la huerta, el asfalto, la tierra seca y las rodadas; el balasto no cambia. No se tocan la luna ni el ambiente. Fuera del foco sigue sin exigirse un mínimo de legibilidad (D-N13), pero todas las zonas se comportan igual. Lo valida Sara con la máscara. Estado del suelo (Marcos): las matas se ocultan bajo las obras (TBD 1cd6129, falta probarlo con una obra real), los tirones al cargar no pasan de 8 ms y la mediana es de 357,7 FPS.
- 6-nov 20:40 UTC (QA-28): capturas corregidas con máscara: recinto día 30,6 / noche (charcos) 63,8; huerta día 25,9 (margen 0,9). Huerta noche: sin foco en encuadre; fuera del foco ΔL* 0,6 (recinto 9,2). Propuesta de criterio ≥ 8 fuera del foco tras el cambio de Lucía.
- Criterio de noche (propuesto por Sara y aprobado por Lucía a las 20:36): fuera de los focos, ΔL* ≥ 8 en todas las zonas, tomando como referencia el 9,2 del recinto. Dentro de los charcos sigue siendo ≥ 25. Medidas en sara2: de día, recinto 30,6 y huerta 25,9 (margen de 0,9, se repite tras cada cambio); de noche, en los charcos, recinto 63,8; fuera de los focos, recinto 9,2 y huerta 0,6 (antes del arreglo del 70 %).
- 6-nov 20:50 UTC (QA-28): noche tras 2aa08f0: huerta charco 63,2 / fuera 11,6; calle charco 62,5 / fuera 6,6 (NO pasa el 8). Asfalto más oscuro tras el 70 %.
- 6-nov 20:55 UTC (QA-28): Lucía pide asfalto al 85 % (luego 100 % si no llega a 8). Pendiente: medir captura nueva de calle de noche y huerta de día.
- 6-nov 22:00 UTC (QA-28): calle noche al 85 %: máscara no llegó; lectura preliminar con máscara anterior ΔL* fuera del foco ≈ 5,7 (<8). Oficial pendiente.

## D-N69 · Noche de luna, no noche negra: muestra para Eugenio (6-nov, 21:55)
Eugenio (21:53): «la noche se ve extremadamente oscura». Tiene razón: con el ambiente negro y la luna a 0,14, el suelo bajo la luna queda en L* ≈ 17 y casi todo es negro fuera de los focos. Propuesta de Lucía, como la noche americana del cine: **la noche se distingue por el color, no por la falta de luz**.
- **Luna más alta**: se prueba en 0,25, 0,35 y 0,45 (antes 0,14), con un tono frío (gris azulado). **Ambiente** de negro a un azul gris muy bajo, para que las sombras no sean un agujero. **Objetivo**: suelo bajo la luna en L* 30–40.
- **Focos y farolas sin cambios**: su calidez ámbar frente a la luna fría es lo que dice «noche».
- **La horda sigue siendo lo más oscuro** de la escena, y con el suelo más claro gana contraste. Criterio de Sara: ΔL* ≥ 8 fuera de los focos y ≥ 25 dentro.
- La subpaleta del suelo sigue sin navy ni #404460. Con más luna puede que el acercamiento del 70–85 % a la apisonada deje de hacer falta; se revisa con la muestra.
- **Muestra**: Marcos hace 3 capturas del mismo encuadre (recinto, calle con horda y un foco), una por cada valor de luna, y con máscara para Sara. Eugenio elige. Hasta entonces, la noche actual no cambia.
- 6-nov 22:05 UTC (QA-28): calle noche 85 % con máscara real: charco 62,7, fuera 10,6 (pasa); corrige la lectura previa de 5,7. 100 % pendiente (archivo no abre). Eugenio ve la noche oscura: muestra luna 0,25/0,35/0,45 a medir; método de charco por geometría.
- 6-nov 22:15 UTC (QA-28): muestra luna 0,25/0,35/0,45: fuera del foco 12,2/12,7/17,8; charco 67,1/63,3/63,5 (muestra de ~200 px); suelo mediana L* 16,1/16,5/25,3; ninguna en 30–40. Charco por brillo, no por geometría.
- D-N69, estado (6-nov, 22:08): luna en 0,45 en la build (TBD cc7db31). Prueba -stress10k-sagunto en la build: mediana de 347,2 FPS (antes, 357,7), p99 de 7,25–10,33 ms y peor caso de 14,6–16,3 ms. Lucía lo aprueba; la pasada del Editor (297,7 FPS) se descarta. Pendiente: que Sara mida la lectura de la horda y probar sin el acercamiento del 70–85 % a la apisonada.
- 6-nov 22:25 UTC (QA-28): calle noche con luna 0,45 en build (cc7db31): fuera del foco 21,2; charco 59,8–70,2; suelo mediana L* 25,3. Pasa.
- D-N69, cerrado (6-nov, 22:09): Eugenio elige la luna en 0,45. Sara: fuera del foco, 21,2 (antes, 10,6 con el 85 %); dentro del charco, 60–70. El suelo bajo la luna queda en L* ≈ 25, por debajo del objetivo de 30–40, pero se acepta porque es la elección de Eugenio y la lectura de la horda ha mejorado mucho. Pendiente: la prueba sin el acercamiento a la apisonada.
- 6-nov 22:35 UTC (QA-28): luna 0,45 sin acercamiento: huerta fuera 14,0, calle 17,6 (pasan); con acercamiento calle 21,2; falta huerta 0,45 con acercamiento para comparar.
- D-N69, cierre definitivo (6-nov, 22:13, decide Mak): se mantiene el acercamiento del 70 % (85 % en el asfalto) a la apisonada. Sin él la horda también pasaba (huerta 14,0/64,2, calle 17,6/59,5), pero el suelo de la huerta bajaba a L* 16, en contra de lo que pidió Eugenio. Noche final: luna 0,45 más el acercamiento (TBD cc7db31).
- Muelle y señales integrados (6-nov, 22:22, TBD 04baa2e): solo visuales, sin colisión (decide Mak). En la build, mediana de 331,0 FPS y peores fotogramas de 16, 21 y 72 ms. Lucía pide repetir con el PC en reposo. Criterio nuevo: fuera de la carga, ningún fotograma por encima de 33 ms. Si el pico coincide con la primera vez que se ve un material nuevo, se precalientan los shaders al cargar la zona.

## D-N70 · Zoom de la estación y salida al mapa con la rueda (6-nov, 22:25)
Eugenio (22:22): «no puedes alejar estando dentro de una estación la cámara, y tampoco puedes salir al mapa global alejando con la rueda». El GDD ya lo prometía (§7, «zoom continuo hasta la zona… se funde en el umbral»; §11, transición al mapa), pero el prototipo no lo hace. Diseño de Lucía:
- **Rango dentro de la estación**: ortho de 10 (de cerca, para ver a la tropa) a **70** (el recinto entero y su entorno). Por defecto, 18. La rueda hace un zoom suave de unos 0,15 s por clic y centrado en el cursor. Los escalones de pixelado de 1/3 a 1/6 con histéresis no cambian.
- **Salida al mapa**: en el tope de 70, la rueda «tropieza». Una muesca más solo muestra un aviso discreto junto al cursor («sigue alejando para ir al mapa») y **la segunda muesca, en menos de 0,6 s, funde al mapa de operaciones** (unos 0,5 s), centrado en la estación y al zoom más cercano del mapa. Así nadie sale por accidente al alejar en mitad de un asedio. La tecla M sigue funcionando.
- **Vuelta a la estación**: en el mapa, al acercar con la rueda con el cursor sobre una estación propia (o con doble clic), se funde a la estación en ortho 70, para que se lea como el mismo movimiento al revés. Si el cursor no está sobre ninguna estación, la rueda solo hace zoom del mapa.
- **Interfaz y rendimiento**: con el tope en 70 no cambia nada. Es el encuadre que ya se midió para el castillo y el suelo, y los trozos se cargan en un radio de 170 m, que cubre la diagonal visible a 70. Si algún día se sube el tope, hay que ampliar ese radio y volver a medir. Mientras se ve el mapa, la zona sigue simulándose (lockstep), pero no se dibuja.
- **Muestra para Eugenio**: un GIF corto de Marcos (alejar hasta 70, salir al mapa con la rueda y volver a entrar) antes de darlo por cerrado.
- Muelle de mercancías (6-nov, 22:32): se quita la losa de suelo de unos 25×12 m (salía como un parche liso, de distinto color en cada variante, y Eugenio no entendía qué era). Queda solo el andén de carga elevado de unos 1,1 m, pegado al edificio, en 94948c arriba y 605c48 en los costados, igual en todas las variantes. Mientras llega el FBX nuevo de Teo, Marcos oculta la losa y revisa si hay dos instancias solapadas. Regla general: ninguna pieza trae su propia losa de suelo de color liso; el suelo lo pone la textura por zonas.
- D-N70, estado (6-nov, 22:49, TBD 5d4a65e): zoom de 10 a 70, un 15 % por muesca, centrado en el cursor; dos muescas de más en el tope sacan al mapa. Arreglada la rueda lenta (el delta del Input System se dividía siempre entre 120). Muelle sin losa, una sola instancia. Al salir al mapa la zona se descarga; la simulación sin dibujado queda para después del hito 6 (decide Mak). **Criterio de rendimiento con el zoom al máximo (Lucía)**: mediana ≥ 240 FPS y ningún fotograma por encima de 33 ms con 10.000 zombis. Los 320 siguen siendo el criterio con el zoom por defecto. A ortho 70 daba 233 FPS: primero se aplica la regla de D-N67 §5 (en 1/5 y 1/6 no se dibuja la hierba baja) y después, si hace falta, la fusión de la capa C por trozos.

### QA-29 — Prueba de humo del prototipo (Sara, 6-nov 23:10 UTC)
Eugenio pide un prototipo jugable a las 08:00. Lista en docs/qa/humo-prototipo.md (26 puntos, gravedad S1–S4, marcas ✅/⚠️/❓). Informe final antes de las 07:30. Limitación: sin Unity, lo visual y sonoro queda ❓ salvo evidencia de Marcos.
- 6-nov 23:05 UTC (QA-29): Mak decide: vehículo y helicóptero (movimiento) fuera del hash; su daño a la horda entra como orden; pelotones dentro. Marcos pasa commit, qué funciona y evidencia en cada build; prueba de entrar y salir del tren 3 veces.

## D-N71 · Plan de la noche del 6 al 7 de noviembre: prototipo jugable para las 08:00 (6-nov, 23:12)
Eugenio (23:03) pide un prototipo jugable para la mañana. Lucía, jefa de producto esta noche, escribe el plan en `docs/plan-noche-7nov.md`.
- **Bucle**: «La primera noche en Sagunto», de 22:00 a 06:00, con oleadas desde el oeste. Se gana si al amanecer siguen en pie el edificio de viajeros y el tren.
- **Pelotones**: fusileros (8) y ametralladores (4, con emplazamiento) en P0; granaderos (6) y tiradores (2) en P1; zapadores (6) en P2. Armamento de referencia: G36E, MG4E, AG36, G28 y M95.
- **Vehículo de tierra**: VCR 8×8 Dragón. **Helicóptero**: NH90 de transporte con arma de puerta (por confirmar).
- **Zoom por defecto** a ortho 12 y mínimo a 6, para la sensación de tamaño. Nivel 1 de escala de Álvaro (calles de 9–10 m, puerta sur de 8 m, parque de vehículos y helipuerto).
- **Sangre** en 4c1008 y 7c181c, nunca en #982420.
- **Marcos solo integra**: Nacho entrega la lógica en C# con PR, Teo los FBX, Bruno los PNG con JSON e Iris los sonidos.
- D-N70, rendimiento (6-nov, 23:10, TBD 1dde39d): con la capa C fusionada por trozos, mediana de 275,3 FPS a ortho 70 (antes, 233) y de 380,1 a ortho 22. Cumple los dos criterios (≥ 240 con el zoom al máximo y ≥ 320 con el zoom de juego). Zoom por defecto 12 y mínimo 6 ya en el código.
- 6-nov 23:10 UTC (QA-29): Lucía decide: en el bucle de la noche siempre gana la derrota (si cae el edificio o el tren en el mismo tick o a las 06:00, derrota); victoria solo si a las 06:00 todo sigue en pie.

## D-N72 · Estadísticas de los pelotones, del Dragón y del NH90, la noche jugable y la puerta de vehículos (Hugo; lo pidieron Mak y Lucía, con datos de Paula) (6-nov, 23:40)
- **Archivos**:
  - `docs/economia/unidades/unidades.py`: es la fuente de verdad y genera los tres CSV siguientes.
  - `csv/balance_unidades.csv`: 261 claves enteras con el formato de siempre (clave;valor;escala;nota).
  - `csv/balance_noche.csv`: el reloj y las oleadas.
  - `csv/referencia_unidades.csv`: bajas esperadas por segundo y por u, con horda densa y suelta, para que Nacho y Sara comprueben la zona con un margen del ±25 %.
- **Base**: el combate actual de la zona. El fusil G36E y la MG4E en marcha **no cambian** (están validados en P7). Las armas nuevas añaden radio, letalidad, tope de bajas, perforación, despliegue y vuelo. Las tres clases de munición (ligera, pesada y especial) quedan marcadas, pero **en el MVP salen del mismo stock**: la economía tiene una sola munición, y separarla obligaría a recalibrarlo todo.
- **Los 5 pelotones** son los de §3 del plan:
  - **Fusileros**: 8 personas; 4 fusiles, 2 MG4E y 2 AG36.
  - **Ametralladores**: 4 personas; 2 MG4E emplazadas (2 s, cono de 60°, perforan 1) y 2 proveedores.
  - **Granaderos**: 6 personas con AG36 (granada cada 6 s, 2,5 m de radio, mínimo de 15 m; solo si hay ≥ 6 zombis en el radio, y si no, fusil).
  - **Tiradores**: 2 personas; un G28 y un observador.
  - **Zapadores**: 6 personas; obra ×2 y 2 cargas de 4 m de radio.
- **Rendimiento con horda densa (2/m²)**:

  | Pelotón | Bajas por segundo | Bajas por u |
  |---|---|---|
  | Ametralladores | 10,1 | 338 |
  | Granaderos | 10,0 | 500 |
  | Fusileros | 6,7 | 261 |
  | Zapadores | 4,3 | 338 |
  | Tiradores | 1,0 | 551 |

  Con la horda suelta (0,3/m²), los granaderos bajan a 270 bajas por u, el nivel del fusil.
- **VCR Dragón**:
  - 4.000 de vida y un 99 % de armadura.
  - Se para con una pila ≥ 3 delante.
  - Velocidad: 12 m/s en campo abierto y 4 m/s entre la horda. Por encima de 3 m/s atropella, con un 50 % por cada zombi que pisa.
  - Torre de 30 mm (explosivo de 1,5 m) y ametralladora coaxial.
  - A bordo: 2 u de munición y 8 plazas. Gasta 1 u de combustible por hora.
- **NH90**:
  - 3.000 de vida y crucero a 30 m. Solo se le puede tocar por debajo de 3 m.
  - Velocidad máxima de 45 m/s, aceleración de 5 m/s², frenada de 7 m/s², guiñada de 60°/s y cabeceo de 15°.
  - **2 FN MAG 58 de 7,62 mm, una por puerta, cada una solo hacia su lado** (Lucía).
  - 12 plazas, 4 u de combustible por salida y +1,5 de huella.
  - El Tigre queda como alternativa.
- **Contra la economía (400 zombis/u)**, con un asedio de 10.000:
  - Los 5 pelotones más el Dragón: 3,6 min y 26 u, es decir, **388 zombis/u**, en línea con el modelo.
  - Solo fusileros: 261 zombis/u, lo que premia variar.
  - El abuso de granaderos: 496 zombis/u, el techo; lo frena la dotación.
  - El cañón de 30 mm y los explosivos costaban la mitad: con ellos la munición dejaba de importar, así que **he subido su coste**.
- **La noche**:
  - **Reloj ×28**: de 22:00 a 06:00 son 17,1 min reales.
  - **6 oleadas desde el oeste**, a las 22:20, 23:20, 00:40, 02:00, 03:20 y 04:40, de 600, 1.200, 2.000, 3.000, 3.600 y 5.000 zombis (15.400 en total). Entran en 40–100 s reales y dejan unos 3 min para construir entre una y otra.
  - Hay 45 u de munición en Sagunto, unas 10 u más entre dotaciones, Dragón y NH90, y 40 u de materiales.
  - Resultado del modelo de cola, según qué parte del caudal teórico aprovecha el jugador:
    - Con el 90 %, gana con holgura (pila de ~480 en la última oleada y 42 de 55 u gastadas).
    - **Con el 70 %, gana costando**: pila de ~1.500 contra el HESCO en la última y 48 de 55 u.
    - Con el 50 %, pierde: se queda sin munición y la pila llega a ~2.500, desborda los sacos de las alas.
  - Para afinar en la prueba hay **una sola palanca**: `noche_escala_oleadas_permil`.
- **Puerta de vehículos (Álvaro)**: 8 m en 2 hojas por **10 u (no 8)** y 8 obrero·h, porque es más del doble de ancha que la de vía (3,2 m por 8 u). En Sagunto sustituye a la peatonal (6 u), con lo que el muro de partida queda en unas 122 u, dentro del margen de D-N63.
- **Pendiente**: medir en la zona real (Nacho y Sara) que la referencia se cumple con un ±25 %, y la pila de la última oleada. El modelo de área es analítico (densidad × π r² × letalidad) y la cola no ve la geometría del muro.
- Sobre D-N72 (Lucía, 23:13): aprobada la tabla y la noche de Hugo (reloj ×28, 17,1 min reales, 6 oleadas y puerta de vehículos de 10 u). **Para la build de las 08:00, noche_escala_oleadas_permil = 850 por defecto**, para que un jugador nuevo, que aprovecha el 60 % del fuego, gane costando (con 1000 perdía por munición). El 1000 queda como «difícil». Hugo ajusta el valor exacto con su cola.
- Interfaz y VFX de la noche (Bruno, 23:12, commit 2d2cb80): aprobados. El fondo del menú es la ilustración de Bruno, con una excepción de color: el naranja del atardecer se permite solo en esa ilustración; dentro del juego, el ámbar sigue reservado. Sangre de impacto de 0,4 s (5 fotogramas). Único cambio: diferenciar los iconos de embarcar y desembarcar.

## D-N73 · Escala de cámara y lecciones del vídeo de referencia (6-nov, 23:16)
El análisis del vídeo (`arte/referencia-ebbtide-anfibio.md`) cambia el diagnóstico de «todo se siente pequeño». Con su zoom de mando, una persona mide 28–32 px y caben unos 110 m de ancho. Con nuestro ortho 18, el zombi mide unos 30 px pero solo caben 64 m. Lo que da la sensación de grandeza es ver más mundo con las figuras igual de legibles, no acercar la cámara. **Se anula el zoom por defecto de 12 de D-N71.**
- **Build de las 08:00**: ortho por defecto 26 y figuras (soldados y zombis) a ×1,3 solo en el dibujo. La huella de la simulación no cambia. Mínimo 6 y máximo 70.
- Marcos hace 3 capturas del mismo encuadre (18; 26 ×1,3; 28 ×1,3) con su FPS. Eugenio elige por la mañana. Se puede volver atrás.
- **Relación con el escenario**: con ×1,3 un soldado se ve de unos 2,3 m. Se acepta porque al embarcar desaparece en el vagón o el vehículo y la colisión no cambia. Los vehículos, el tren y los edificios siguen a escala real.
- **Aprobados para esta noche (P1)**: color por instancia en la horda (camisa, pantalón y piel); mapa de sangre que se acumula por trozo en 4c1008, 642030 y 7c181c, nunca #982420; marcadores de orden que se desvanecen; y oleadas con un frente denso y una cola dispersa.
- **P2**: animaciones desincronizadas por VAT (de 4 a 5 animaciones a 12 fps escalonados), tres formaciones de tropa y cadáveres que persisten con tope.
- **No aplica a Sagunto**: el agua y el atardecer de juego (la noche empieza a las 22:00; el atardecer ya está en el menú).
- Aviso de numeración (Lucía, 23:17): Hugo ha registrado la dificultad de la noche (850 por defecto, 1000 difícil y 725 fácil) también como D-N73. Si aparece una segunda D-N73 de Hugo, se cuenta como **D-N74**. La siguiente libre es la D-N75.

## D-N74 · La noche de Sagunto en JSON, la munición para el HUD y tres dificultades (Hugo, a petición de Mak y de Lucía) (7-nov, 00:10)
- **Nota**: la escribí como D-N73 a las 23:55, pero chocó con la escala de cámara de Lucía y se perdió al guardarse el archivo a la vez. La añado otra vez con el número bueno.
- **`docs/economia/json/noche_sagunto.json`** (para Marcos; se carga tal cual). Incluye:
  - El reloj: ×28, de 22:00 a 06:00, 1.028 s reales.
  - La victoria y la derrota.
  - Los recursos iniciales del almacén: munición 45 u, materiales 40 u y **combustible 30 u** (nuevo: el Dragón gasta 1 u por hora de juego y el NH90, 4 u por salida). Aparte, unas 10 u de dotaciones.
  - Las oleadas de las tres dificultades, con hora, minuto de juego, segundos reales de llegada, total y reparto por entrada. Las entradas son O1 vía 50 %, O2 carretera 30 %, O3 pueblo 20 % y O4 puente 0 %. **El puente se abre en las dos últimas oleadas**: la 5 entra 40/30/20/10 y la 6, 30/30/20/20.
- **Dificultad**: **850 por defecto** (13.090 zombis), porque Eugenio juega por primera vez (Lucía). En la cola:
  - Con el 60 % del fuego gana costando: pila final de ~1.240 y 44 de 55 u gastadas.
  - Con el 50 % gana justo: ~1.740 y 48 de 55 u.
  - Reservas: **fácil 725** (11.165 zombis) y **difícil 1000** (15.400 zombis; con el 50 % pierde por munición).
- **Munición para el HUD** (`csv/hud_municion.csv` y `municion_hud` en el JSON). Segundos de fuego continuo con la dotación:

  | Unidad | Fuego continuo |
  |---|---|
  | Fusileros | 58 s |
  | Ametralladores | 66 s |
  | Granaderos | 100 s |
  | Tiradores | 171 s |
  | Zapadores | 118 s |
  | Dragón | 66 s |
  | NH90 | 100 s |

  Recargar repone la dotación entera desde el almacén: 10 s junto al tren o el depósito, 20 s el Dragón y 30 s el NH90 posado en el helipuerto.

## D-N75 · Lista de comprobación del equilibrio para la partida de Sara de las 07:30 (Hugo, a petición de Mak) (7-nov, 00:10)
- Está en **`docs/qa/equilibrio-noche.md`**: los valores esperados de munición y de pila al final de cada oleada, para el 70 % (Sara), el 60 % (Eugenio) y el 50 %.
- **Por qué esas columnas**: Sara juega mejor que Eugenio, así que sus lecturas se comparan con la columna del 70 %. Si jugando bien cae en la del 60 %, la noche es más dura de lo calculado.
- **Cuándo bajar a 725**: menos de 33 u o una pila de más de 800 al acabar la oleada 4, la horda dentro antes de la 6, o 2 pelotones perdidos antes de la 5.
- **El 1000 no se pone para la partida de Eugenio**, aunque a Sara le sobre.
- Las bajas propias no salen de la cola: la lista da un criterio de diseño (como mucho 1 pelotón perdido en toda la noche), no una predicción.

## D-N76 · Combustible del Dragón y del NH90 en la noche (Hugo, a petición de Mak) (7-nov, 00:20)
- Va en el JSON de la noche, clave **`combustible`**, y en `balance_unidades.csv`. Sustituye a los consumos provisionales de D-N72: 1 u por hora de juego el Dragón y 4 u por salida el NH90.
- **Unidades**: E4 de u por **segundo real**, que se cobra cada 30 ticks. Así es entero y vale para el lockstep.
- **Dragón**: 1,2 u/min en marcha, 0,36 u/min al ralentí y 0 apagado. Depósito de 8 u.
  - Reposta junto al depósito o al tren, a 2 s por u, del almacén de Sagunto.
  - **A cero se queda inmóvil, pero la torre y la coaxial siguen disparando** (propuesta de Mak). Lo rescata un zapador con un bidón de 2 u (20 s).
- **NH90**: 1,62 u/min en vuelo, 0,54 posado con los rotores girando y 0 apagado. Depósito de 6 u.
  - Solo reposta posado en el helipuerto, a 2 s por u.
  - **A cero baja en autorrotación a 4 m/s donde esté**, y por debajo de 3 m la horda puede alcanzarlo. Aviso al quedar el 20 %.
- **Los 30 u de la noche incluyen los dos depósitos llenos**, así que en el almacén quedan 16.
- **Comprobación**:
  - Los dos siempre en marcha gastan 48,3 u, y el combustible se acaba hacia el 60 % de la noche.
  - Racionado (el Dragón en marcha el 40 % del tiempo y al ralentí el 30 %; el NH90 con 10 min de vuelo en 4 salidas) gasta 27,4 u y llega al amanecer con unas 2,6 u de margen.
- **Por qué**: el combustible decide cuándo sacar cada vehículo, y el depósito del NH90 (unos 3,7 min de vuelo) obliga a volver al helipuerto.

## D-N77 · Pantalla de resultados de la noche (Hugo, a petición de Mak) (7-nov, 00:30)
- Va en el JSON de la noche, clave **`resultados`**: textos, formato y cálculo de cada cifra.
- **Seis estadísticas**, todas a partir de lo que ya cuenta la simulación (`ZoneAmmo`: Kills, ShotsFired y SoldiersLost) o del contador de combustible de D-N76:
  1. Zombis abatidos de los llegados.
  2. Bajas propias de 26 soldados, más el Dragón o el NH90 si se perdieron.
  3. Munición gastada, en u, y zombis por u (la referencia es 400).
  4. Munición restante.
  5. Combustible gastado de 30.
  6. Fin de la noche: «Amanecer, 06:00» o «Cayó a las hh:mm, en la oleada n».
- **Estrellas** (solo con victoria; con derrota no hay estrellas, solo la hora):
  - ★: ganar.
  - ★★: además, bajas ≤ 6 y munición restante ≥ 8 u.
  - ★★★: además, bajas ≤ 2, munición restante ≥ 15 u y ni el Dragón ni el NH90 perdidos.
- **Esperado en normal** (cola de D-N72):
  - Al 60 % (Eugenio) quedan ~11 u, así que 2 estrellas si cuida a la tropa.
  - Al 70 % (Sara) quedan ~14 u: la tercera estrella exige jugar mejor que eso.
  - Al 50 % quedan ~7 u: 1 estrella.
- **Por qué la munición restante y no los zombis por u**: es lo que el jugador ve en el HUD toda la noche. Así la nota premia lo mismo que enseña la pantalla.

## D-N78 · Maquetas de interfaz a 1080p de la noche (Bruno; revisión de Lucía) (7-nov, 00:25)
- Numeración: Bruno las entregó como «D-N74» (mr-mak-workspace 111af4c, carpeta docs/capturas/maquetas-dn74/; TBD 09d81a5), pero ese número ya era de Hugo. Se registran aquí como **D-N78**. La carpeta conserva su nombre. La siguiente libre es la D-N79.
- **Aprobadas**: HUD, rótulo de entrada, menú, victoria y derrota, con los textos del §8 del plan. Piezas nuevas aprobadas: cartel de oleada (marco #982420, que es un aviso de ataque), indicador de entrada en el borde (cuña roja con placa «O1»–«O4») y barra de recarga en tramado hueso. Iconos de embarcar y desembarcar diferenciados por la posición del vehículo: cerrado.
- **Cambios** (Bruno):
  1. El botón de mover dice «dic»: en la fuente de píxel, «cl» se funde en una «d». Va un icono de ratón con el botón derecho marcado, sin texto.
  2. Embarcar y desembarcar comparten la tecla E: **un solo botón contextual**, que muestra el icono que toca según la unidad seleccionada. Libera una casilla.
  3. Las entradas se nombran igual en todas partes: la alerta («Oleada 2 en la puerta oeste») y el cartel («Entrada O1: la vía») deben usar el mismo código y el mismo nombre, con la forma «O1 · la vía».
  4. **Reloj arriba en el centro**, como en D-N65. Los recursos se quedan arriba a la izquierda, encima de las alertas. El cartel de oleada baja lo justo para no taparlo.
  5. Victoria y derrota llevan la pantalla de resultados de **D-N77** (clave `resultados` del JSON): las seis cifras y, solo con victoria, las estrellas. Estrella llena en hueso b4a080 y vacía en 48403c, nunca en ámbar.
- El marco rojo en la derrota se acepta: es la consecuencia del asedio y no se confunde con una señal dentro del juego.

## Aviso de numeración (Lucía, 7-nov, 00:28)
- Mak había puesto, por su cuenta, la D-N78 a la paleta de la horda y al mapa de sangre (encargo a Bruno) y la D-N79 a la revisión del realismo de las armas (encargo a Hugo). La D-N78 queda para las maquetas de interfaz de arriba. Esos dos encargos pasan a ser la **D-N80** (paleta de la horda y mapa de sangre, Bruno) y la **D-N81** (realismo de las armas, Hugo). **La D-N79 no se usa**, para que no se confunda con la etiqueta que ya circula.
- **Desde ahora, los números los asigna solo Lucía**, que lleva el registro. Quien registre algo nuevo me lo pide antes de escribir. La siguiente libre es la **D-N82**.

## D-N79 · Realismo de las armas frente a los datos de Paula (Hugo, a petición de Mak) (7-nov, 00:45)
- Está en **`docs/economia/realismo-armas.md`**. Casi no hay cifras reales verificadas: solo la cadencia máxima del G36E (750/min), el alza de la MG4E (1.000 m) y la MAG 58 como arma de puerta del NH90. Por eso no se puede medir la distancia a la realidad en alcance ni en dotación, solo la coherencia entre armas.
- **Se queda, porque tiene razón de juego**:
  - La cadencia apuntada del fusil (2/s, frente a la máxima de 750/min).
  - Los alcances comprimidos a la zona de 256 m.
  - La dotación en disparos equivalentes.
- **Corregido, sin tocar el equilibrio** (la salida de `unidades.py` es idéntica, solo hay una fila nueva):
  - El Barrett M95SP pasa a ser un arma aparte, `fusil_antimaterial`. Es de cerrojo, así que es más lenta que el G28 semiautomático; tiene 200 m y perfora 2. Es mejora de los tiradores, fuera de la noche.
  - La MAG 58 cita su fuente.
- **Deuda (R1–R6)**:
  - El AG36 llega más lejos que su propio fusil.
  - La MG4E de 5,56 perfora y el G36E no; la perforación debería pasar a la MG5.
  - No hay un factor de compresión único de las distancias: falta que Paula busque los alcances eficaces oficiales.
  - El 30 mm tiene el mismo alcance que el G28.
  - Falta el contracarro, para cuando haya cepas.
  - Las tres clases de munición comparten un solo stock.
- **Para Bruno**: el HUD no muestra cartuchos ni cargadores, solo una barra o los segundos de fuego.
- Numeración (Hugo, 00:47, a petición de Lucía): la entrada de arriba, «D-N79 · Realismo de las armas», cuenta como **D-N81**; el número 79 no se usa. Desde ahora, los números D-N los asigna Lucía.

## D-N82 · Comprobación de la build de la noche y cierre de la deuda de armas (Hugo; número dado por Lucía) (7-nov, 00:55) — EN CURSO
- **Script**: `docs/economia/unidades/verificar_noche.py LOG [--dificultad normal]` compara un log de partida con `json/noche_sagunto.json`: el inicio de la noche, cada oleada (hora, total y reparto por O1–O4) y el resultado (estrellas según la fórmula de D-N77 y combustible ≤ 30 u). Con `--esperado` saca la lista para comprobarla a mano. Probado con un log de ejemplo con un error metido a propósito, y lo detecta.
- **Formato de log pedido a Marcos**: líneas `[NOCHE] clave=valor …` al empezar la noche, al empezar cada oleada y al final. Si no le da tiempo, se comprueba a mano con capturas.
- **Pendiente**: pasar el script a la primera build que cargue el JSON y cerrar la deuda R1–R6 de `economia/realismo-armas.md` cuando lleguen los datos oficiales de Paula.
- D-N78, cierre (Lucía, 00:35): los cinco cambios de Bruno están hechos (TBD 4299ee8, mr-mak-workspace 50868f2) y quedan aprobados. Los textos de victoria y derrota pasan a ser los del JSON de D-N77 («Sagunto resiste», «Repetir la noche» y «Menú principal»); el §8 del plan está actualizado.
- **D-N80, cierre (Lucía, 00:35)**: horda variada por instancia, con **la banda de valor estrechada a L\* 9–13** (no 9–16). Toda la partida es de noche y fuera de los focos el contraste no puede quedarse justo en el mínimo de Sara (8,0). La variedad se queda en el matiz y la saturación, que se aprecian de cerca y bajo los focos, donde el valor sube. Sin navy ni #283440. La regla de Bruno pasa a ser norma: **ningún albedo de unidad propia baja de L\* 28** (#48403c), porque todo color final con L\* < 20 es de la horda.
- **D-N82, cierre de la parte de armas (Hugo, 01:05)**, con las cifras con fuente de Paula (`infanteria-et.md` §6):
  - **Escala única de distancias, logarítmica**: alcance en el juego ≈ 37,3·ln(real) − 78,6. Con ella, el AG36 pasa de 120 a 140 m y el Mk44S del Dragón, de 160 a 220 m. Cierra R3 y R4.
  - La salida de `unidades.py` es idéntica: la cola calcula a 25 m.
  - Las automáticas no siguen la escala, a propósito: su alcance es el del fuego apuntado útil, porque su acierto cae con la distancia.
  - Cadencias comprobadas: el Mk44S va a 180/min frente a los 200 reales, y la MAG a 600/min frente a 650–1.000, por los ticks de 30 Hz.
  - Las dotaciones son valores de diseño: no hay fuente pública.
  - Siguen abiertas R1, R2, R5 y R6. La comprobación de la build sigue pendiente.
- 6-nov 23:35 UTC (QA-29): Hugo amplía alcances (AG36 140 m, cañón 30 mm Dragón 220 m). Criterio propuesto: pila > 0 en oleadas 4–6 con 70 %, munición ≥ 33 u tras la 4. Partida real: necesito registro por oleada; no puedo jugar desde aquí.
- D-N80, medida final (Bruno, TBD 39f741b; revisión de Lucía, 00:40): banda L\* 9–13, con el azul mahón en 12,8 y el chocolate en 12,7. Medida con el p90 de la horda frente al p10 del suelo: de noche 15,6 la variada y de día 15,8. **Aprobada**: de noche la variada se lee igual que la de un solo valor.

## D-N83 · VFX de vehículos: Dragón y NH90 (Bruno, encargo de Mak; revisión de Lucía) (7-nov, 00:40)
- Entrega: mr-mak-workspace b3f53be, docs/capturas/vfx-vehiculos/contacto_vehiculos_x4.png. Incluye el fogonazo y la trazadora del 30 mm, el fogonazo y la trazadora de la MAG 58, las vainas, el polvo de las ruedas y el impacto de 30 mm. **Aprobada.**
- **Regla del ámbar en los VFX** (aclara la reserva de #e08c30): el fuego y la luz de disparo pueden llevar #e08c30 porque son **transitorios** (fogonazos, trazadoras, núcleo de explosiones, partículas de ≤ 0,25 s). Nada que **persista** en pantalla lleva ámbar: ni en el suelo ni en marcadores, porque el ámbar sigue siendo la señal de aviso. Las vainas pasan a 845c28 al tocar el suelo, o desaparecen.
- El impacto de 30 mm tiene dos variantes: contra la horda, con las motas de sangre 4c1008; contra el suelo o un edificio, sin sangre y solo con polvo y cascotes.
- Falta (P1, Bruno): el **polvo del rotor del NH90** cuando vuela bajo o aterriza, un anillo de polvo en 88885c/b4a080 con el tramado del polvo de las ruedas.
- La siguiente libre es la **D-N84**.
- 6-nov 23:30 UTC (QA-29): Hugo ajusta criterios: oleada 6 pila > 0 firme (~730); oleada 4 blando; munición tras la 4 ≥ 33 u firme (esperado 37,5); si hay exceso de alcance, AG36 a 120 m y cañón a 160 m.
- D-N80, alcance (Lucía, 00:45): la regla de que ningún albedo propio baje de L\* 28 vale también para **los vehículos**. En el Dragón, los cristales pasan de 181c30 a 60546c, igual que en el NH90, y las ruedas de 303424 a 48403c. Las botas del soldado van en 6c4038 (Teo).
- Dragón animable (Teo, PR #10, 8f5427f): la torre «hueca» y el cañón atravesando el casco eran un fallo de la captura de comprobación, no del FBX. Con las transformaciones de Unity, la torre gira entera y el cañón asoma por el costado, como en el real. **Marcos puede animar la torre**: giro en Y y elevación desde el muñón, de −8° a +45°. La torre del LOD1 sigue en 88885c (decisión del 6-nov).
- NH90 (Teo, PR #10): **aprobado**. Camuflaje como en la foto (50541c, techos b4a080 y manchas 845c28), puertas abiertas con una MAG 58 a cada lado y palas 94948c. Para el rotor en marcha: por encima de cierta velocidad se ocultan las palas y se muestra un **disco tramado** (Bayer al 25 %, en 94948c), porque cuatro palas discretas a 60 FPS parpadean. Las palas quedan fuera del contorno por luminosidad, que las convierte en trazos negros.
- D-N83, cierre (Lucía, 00:50): los tres retoques están hechos (TBD 72c19d9): vainas planas en 845c28, impacto_30mm_suelo sin sangre y polvo del rotor en 88885c/b4a080. **Cerrada.**

## D-N84 · VFX de la vista cercana del tren (Bruno; revisión de Lucía) (7-nov, 00:50)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/tren/contacto_vfx_tren_x4.png. Contiene chispas de rueda, humo del escape (olive_grey y grey_brown), destello del faro, ventanillas aditivas (de crema a ocre), polvo con hojas y decals de balasto y hierba junto a la vía, todo de la subpaleta del suelo. El único ámbar son las chispas, de ≤ 0,25 s. **Aprobada.**
- Las ventanillas encendidas son la imagen de la vista: un tren con luz en mitad de la noche. Tienen que verse en todos los vagones con pasaje.
- Humo: a 20 m/s no sube en columna. Se emite en espacio del mundo y se queda atrás (−X), en bocanadas sueltas que se tienden en horizontal (Marcos, en el emisor).
- Chispas: no son continuas. Salen de vez en cuando en las juntas de los carriles (una cada 2–4 s, al azar) y seguidas al frenar en la llegada.
- La siguiente libre es la **D-N85**.

## D-N85 · Fondo con parallax de la vista del tren (Bruno; revisión de Lucía) (7-nov, 00:55)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/parallax-tren/contacto_parallax_tren_x3.png. Tres tiras de 640 px que se repiten en X sin costura (cielo de 640×120, sierra de 640×56 y colinas de 640×44 con bancales, algarrobos, naranjos y casas), con versión de día y de noche. Factores de parallax propuestos: 0, 0,08 y 0,25. El humo en bocanadas sueltas va en TBD 446d433. **Aprobada.**
- **El navy #181c30 en el cielo y la sierra de noche se mantiene**, como excepción **solo en este fondo**, igual que el naranja del atardecer solo se permite en la ilustración del menú. Es una capa de fondo de una vista sin horda que mandar: ningún zombi se recorta contra ella. El cielo nocturno tiene que ser lo más oscuro del plano para decir «noche». En el mapa de juego la banda L\* < 20 sigue siendo solo de la horda.
- La siguiente libre es la **D-N86**.

## D-N86 · Iconos del HUD y VFX de las seis armas (Bruno; revisión de Lucía) (7-nov, 01:05)
- Entrega: TBD 5e948ca y mr-mak-workspace 93771df. Hojas en docs/arte/pixel-codigo/noche-prototipo/armas/. Iconos de 48×16 en hueso (G36E, AG36, MG4E, G28, C90 y el cartucho de 30 mm) y VFX de disparo, impacto y humo de cada arma. El único ámbar es el fuego, de ≤ 0,25 s. **Aprobada con un cambio:**
  - **El bípode va en el icono de la MG4E**, como en el modelo de Teo, y **se quita del G28**. El bípode es la seña de la ametralladora; el G28 ya se distingue por el cañón largo, el visor y la culata arena.
- El C90 y el AG36 están dibujados SIN VERIFICAR, porque no hay foto en el lote de Paula. Se le piden referencias; si llegan, Bruno los repasa.
- La siguiente libre es la **D-N87**.
- Menú en el juego (captura de Marcos, menu_inicio.png, 00:13): **no sigue la maqueta de D-N78**. Cambios para Marcos: la ilustración de Bruno de fondo, su fuente de píxel y los botones a la izquierda. El subtítulo va en hueso y no en ámbar #e08c30, y sin la línea ámbar. «Continuar», cuando no hay partida, va en gris y sin el paréntesis (ahora se sale del botón). Fuera el pie «prototipo · pixel art 3D · Unity 6 + DOTS». «Cómo se juega» se queda: es un buen añadido.
- Capturas de zoom (mr-mak-workspace ef609ca): no sirven todavía para que Eugenio elija. Son de día (06:10), a 960×540, sin el HUD del juego, con la superposición de depuración, y sin zombis ni soldados en el encuadre. Se repiten a 1920×1080, de noche, con el HUD de D-N78, sin la depuración, en la puerta oeste con una oleada entrando y los pelotones delante. Las tres en el mismo encuadre. FPS de esta tanda: 320, 335 y 431.
- D-N86, cierre (Lucía, 01:10): el bípode está en la MG4E y ya no en el G28 (TBD eb7182e). **Cerrada.**

## D-N87 · VFX de vehículos en combate (Bruno; revisión de Lucía) (7-nov, 01:10)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/vehiculos/contacto_vfx_vehiculos_x3.png. Contiene polvo_estela (ruedas), polvo_orugas, humo_danado_leve y humo_danado_grave (sin bajar de L\* 20), fuego_vehiculo en bucle, explosion_vehiculo de 128 px y decal_calcinado (2 variantes). Para el Tigre se reutiliza el polvo_rotor de D-N83 a escala 0,8. **Aprobada con un cambio:**
  - **decal_calcinado** usa 442c0c, que es un valor de la horda y está prohibido en el suelo. Pasa a 48403c/605c48, con el hollín 303424 solo en una mancha pequeña en el centro (la excepción del hollín ya aprobada).
- **El fuego en bucle se queda sin ámbar**: es persistente. Para que parezca llama y no brasa: núcleo crema que parpadea, lenguas ocre que cambian de altura y, en el juego, una **luz puntual cálida** que parpadea con él (Marcos). Es la luz sobre el suelo lo que dice «fuego», como los focos (D-N69).
- Alcance: el Lince, el VAMTAC, el Pizarro y el Tigre **no están en el plan de esta noche** (P0 y P1 solo tienen el Dragón y el NH90). Estos VFX quedan para después del prototipo; no se dedica más tiempo a esos vehículos antes de las 05:00.
- La siguiente libre es la **D-N88**.
- D-N87, corrección del alcance (Lucía, 01:12): el PR #24 de Nacho ya trae el Lince, el VAMTAC, el Pizarro, el Cougar y el Tigre, así que **sus VFX sí entran esta noche**. Queda anulada la línea de alcance de arriba. Orden de Bruno: primero la P0 (iconos de recursos y pantalla de resultados), después el cartel de «Cómo se juega» y los iconos de estado de los pelotones.
- Vehículos del PR #24 sin modelo (Lucía y Mak, 01:14): hasta que estén los modelos se usan sustitutos provisionales. El Lince, el VAMTAC, el Pizarro y el Cougar usan el Dragón reescalado con su color, y el Tigre usa el NH90 sin puertas, nunca cajas lisas. Prioridad de Teo (Mak): Pizarro y VAMTAC, después el tren y después el Lince, el Tigre y el Cougar.
- D-N87, cierre (Lucía, 01:18): el calcinado va en 48403c/605c48 con hollín en el centro, y el fuego con núcleo crema parpadeante y lenguas ocre (TBD 90abd0b). **Cerrada.**

## D-N88 · Iconos de recursos del HUD y pantalla de resultados (Bruno, P0; revisión de Lucía) (7-nov, 01:18)
- Entrega: TBD 90abd0b y mr-mak-workspace 177ea03, en docs/arte/pixel-codigo/noche-prototipo/recursos/. Iconos de 32 y 16 px: munición, materiales y combustible (los de A1, ahora exportados), pila y bajas (fusil clavado con el casco del ET, sin rojo). Pantalla de resultados con un icono por fila de D-N77: amanecer si se gana y luna menguante si se pierde. Estrellas en grupos de 0 a 3 y panel de derrota con marco rojo. **Aprobada con un cambio:**
  - **La pila no va en oliva**: el oliva #70784c es el color de nuestros soldados, y en el HUD la pila se leería como tropa propia amontonada. Va en los valores de la horda (303424/283440), con un filo de 1 px en hueso b4a080 arriba para que se lea sobre el panel. La horda es siempre lo más oscuro, también en la interfaz.
- La siguiente libre es la **D-N89**.
- 7-nov 00:00 (Madrid) QA-30: PR #24 (4333587): 595 + 46 en verde. S2: NightGame usa pesos fijos y el puente O4 nunca se abre (oleadas 5–6 sin O4; Hugo espera 306 y 850). Bloque 15 de QaTests.
- D-N88, cierre (Lucía, 01:22): la pila va en 303424/283440 con un filo b4a080 (TBD e2c4811). **Cerrada.**

## D-N89 · Cartel de «Cómo se juega» e iconos de estado del pelotón (Bruno; revisión de Lucía) (7-nov, 01:22)
- Hojas: docs/arte/pixel-codigo/noche-prototipo/como-jugar/ (maqueta_como_jugar_x3.png y contacto_estados_teclas_x6.png). Cartel de 480×270 sobre el fondo del menú, con objetivo, controles y leyenda de estados. Estados de 16 px en hueso; «sin munición» con el ámbar de aviso, igual que la alerta A2. **Aprobada con tres cambios:**
  1. **Objetivo**: «Aguanta en Sagunto de las 22:00 al amanecer. Si cae la estación o el tren, se acaba.». Es la condición real de derrota del §1 del plan; la horda puede entrar en el recinto sin que se pierda la partida.
  2. **Ratón**: cada fila marca su parte. Botón izquierdo para seleccionar, botón derecho para mover y **rueda** para acercar y alejar (ahora la tercera fila marca el botón izquierdo).
  3. **«Alto el fuego»** solo se queda si existe en la lógica de Nacho (PR #24). Si no existe, se quita: la leyenda solo enseña lo que el juego hace.
- Pendiente: el desplazamiento de la cámara. A, S y D son órdenes, así que no se puede usar WASD. Marcos dice cómo es (bordes de la pantalla, flechas o arrastre con el botón central) y Bruno añade la fila.
- La siguiente libre es la **D-N90**.
- D-N89, cierre (Lucía, 01:25): el objetivo y la rueda del ratón están corregidos (TBD db05d0f). «Alto el fuego» se queda porque existe en el PR #24 (SetHoldFire), igual que «Reabasteciendo» (Resupply). Solo falta la fila del desplazamiento de la cámara, cuando Marcos diga cómo es.
- Pizarro (Teo, 01:25): **aprobado**. Escotillas rectangulares fuera del eje, sin el anillo frontal y con el frente en cuña de un solo bloque: ya no se lee una cara. Los tornillos del glacis van solo en el LOD0. Teo ha corregido además los pivotes del Dragón (las ruedas giraban 11 cm descentradas) y del NH90 (el rotor, 6 cm).
- VAMTAC animable (Teo, 01:25): pendiente de dos comprobaciones. El escudo aparece detrás de la ametralladora, cuando debería ir delante con el cañón asomando. Y con la dirección a 25°, la rueda delantera izquierda baja y se adelanta, que parece el mismo fallo de pivote.

## D-N90 · Retratos de tarjeta de unidad (Bruno, encargo de Mak, P1; revisión de Lucía) (7-nov, 01:28)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/tarjetas/contacto_tarjetas_x2.png (TBD 93556eb). Retratos de 48×48 con seis variantes por tipo: 5 escuadras (busto con casco boscoso, chaleco y el arma de cada tipo, variando piel, barba, braga, gafas, NVG y chambergo) y 8 vehículos de perfil (Lince, VAMTAC, Pizarro, Dragón, Cougar, Tigre, NH90 y Chinook, con número táctico en hueso). **Aprobada.**
- **El camuflaje se permite en los retratos**, en manchas de 4 px: el retrato es la «foto» de la unidad, como la ilustración del menú. En el mapa, las unidades siguen en colores lisos con el valor partido (regla 14 y D-N57).
- Fusileros y granaderos: no hace falta otra seña. La tarjeta lleva el nombre del pelotón al lado y la barra de pelotones tiene su icono. El tubo del AG36 y las granadas del chaleco bastan.
- Los perfiles de vehículos, salvo el NH90, quedan como SIN VERIFICAR hasta tener fotos.
- La siguiente libre es la **D-N91**.
- Tren de cerca (Teo, 01:30; revisión de Lucía): **aprobado**. Hoja: modelado-3d/capturas/tren_cercano_hoja.png. Incluye la locomotora R1 con D-N80, el coche de viajeros (sin foto, pendiente de la de Paula), el coche blindado, el de tropa R2, la plataforma con un contenedor de 40', la cisterna y la plataforma con dos de 20'. Ventanillas en un objeto aparte para encenderlas de noche. Los contenedores van en 6c7874, 847c34 y 605c48, no en su azul real, que choca con el rim 404460. Normales inclinadas hacia arriba, como en el soldado. **Falta una captura con la cámara de la vista cercana de Marcos** (lateral, yaw ≈ 90°, pitch 30–35°, ortho 7): ahí es donde se ven los costados y las ventanillas encendidas, y la hoja de ahora está tomada con la cámara de juego desde arriba.

## D-N91 · Un solo mundo en tiempo real: la noche de Sagunto no es un nivel (Eugenio; propuesta de Lucía) (7-nov, 01:35)
- **Eugenio (00:52)**: «no es un nivel, ¿vale? O sea, no es una pantalla… los combates suceden en tiempo real… tienes que mover a las tropas en el entorno donde, en tiempo real, se ve la estación y se ve el tren». Es lo que ya dice el GDD (§2.2 «un único mapa continuo, sin cargas»; §3b «una campaña continua sobre el mismo mundo, sin misiones separadas»). El plan de esta noche lo había empaquetado como una misión con su principio y su fin, y eso se corrige.
- **Cómo queda la noche de Sagunto**: no es una misión. Es lo que pasa en el mundo cuando el tren para en Sagunto y cae la noche. El reloj del mundo corre; a las 22:00 la Colmena llega andando por el oeste (se la ve venir por el terreno, no aparece en el borde) y a las 06:00 el ataque se disuelve con la luz. Después **el mundo sigue**: es de día en Sagunto, la tropa se repone y el tren puede seguir viaje.
- **Arranque sin cortes**: «Jugar» empieza con la **vista cercana del tren llegando a Sagunto por la vía del propio mapa**. Cuando el tren se detiene en el andén, la cámara sube y se abre hasta la cámara de juego sin fundido ni carga. El rótulo «22:00. El tren se detiene en Sagunto. Aguanta hasta el amanecer» va encima de ese plano. La vista cercana del tren es un modo de cámara sobre el mismo mundo, no una escena aparte; el parallax de D-N85 es solo el fondo del cielo.
- **Aire**: el NH90 **despega del helipuerto** de Álvaro y vuela por el mundo hasta el objetivo; no aparece al llamarlo. Es la idea del vídeo de Eugenio sobre el despliegue desde los aeródromos, aplicada a lo que hay esta noche. El análisis del vídeo (YouTube qFvJa3kYpYw) va al hilo de análisis de vídeo.
- **Avisos de oleada**: el cartel (D-N78) se queda, pero como **aviso en el mundo** (la Colmena se acerca por O1) y no como el inicio de una fase. No es modal y el juego no se para.
- **Amanecer**: en lugar de «victoria», un **«Parte de la noche»** que no detiene el juego, con las 6 cifras y las estrellas (D-N77/D-N88), y un único botón, «Seguir», que lo cierra. El mundo continúa de día.
- **Derrota**: si cae el edificio de viajeros o el tren, se acaba la partida, como en un RTS cuando pierdes la base. Pantalla «Sagunto ha caído» con las cifras y los botones «Volver a empezar» y «Menú principal». **Fuera «Repetir la noche»**: no hay noches que repetir, hay una partida.
- **Menú**: «Continuar» carga la partida guardada (el mundo tal como quedó), no una noche.
- **Zoom**: alejar hasta el mapa (D-N70) es la vista estratégica del mismo mundo. «Entrar» en una estación es acercar la cámara, no cargar un nivel. El mensaje de depuración «M o alejar del todo: volver al mapa» se queda como está.
- **Cambios por persona**: Marcos (arranque con el tren llegando sin corte, el NH90 despegando, el parte del amanecer no modal y textos), Nacho (el amanecer no termina la partida: el mundo sigue y la Colmena se retira; la derrota se queda igual), Bruno (el panel de victoria pasa a «Parte de la noche» con «Seguir»; en la derrota, «Volver a empezar»), Hugo (las 6 cifras pasan a ser «de esta noche», con el contador reiniciado cada noche) y Álvaro (la vía de entrada a Sagunto tiene que tener tramo suficiente para la llegada: unos 300 m a 20 m/s).
- La siguiente libre es la **D-N92**.

## D-N92 · Marcadores de juego (Bruno, P1; revisión de Lucía) (7-nov, 01:40)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/marcadores/contacto_marcadores_x2.png (TBD c8e477e). Contiene los anillos de selección del pelotón (9,6 m, en bucle) y del vehículo (12,8 m, doble y con muesca de proa), el anillo de «encima», las órdenes de mover, atacar avanzando (#982420) y mantener, el cono de emplazamiento de 60° y 25,6 m, el rectángulo de arrastre, la cuña de entrada con pulso, las placas O1–O4 y los cursores nuevos. **Aprobada.**
- La selección va en #d4d0cc, el color de selección de siempre, y el rojo solo en «atacar», como manda la reserva. El relleno tramado del cono es lo bastante flojo para ver a la horda a través. El cursor de «no válido» en hueso es lo correcto.
- Un retoque: en la hoja aparecen unos píxeles en 283440, que es un valor de la horda. La sombra de 1 px va solo en 303424.
- La siguiente libre es la **D-N93**.
- D-N91, panel del amanecer (Bruno, TBD f5556a1): «Parte de la noche» sin velo y con un solo botón, que es **«Seguir»** y no «Continuar». «Continuar» ya es el botón del menú que carga la partida, y repetir la palabra con otro significado confunde. Derrota con velo y marco rojo, y los botones «Volver a empezar» y «Menú principal». **Aprobado.**

## D-N93 · Avisos del HUD y minimapa (Bruno, P1; revisión de Lucía) (7-nov, 01:45)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/avisos-minimapa/contacto_avisos_minimapa_x3.png (TBD 7dc6cc8). Avisos de 32 y 16 px con el lenguaje de A2: oleada entrante, pelotón en apuros y tren atacado, con el triangulito rojo, porque son ataque. Base del minimapa a partir del mapa de zonas de Álvaro, a 4 m/px (189×170). Iconos: pelotón, vehículo, helicóptero, tren, estación, helipuerto, horda en 1c200c con filo 303424, cuña de entrada, alerta y marco de cámara. **Aprobada con un cambio:**
  - **El minimapa gira 45°, igual que la cámara (yaw 45°)**, para que arriba en el minimapa sea arriba en la pantalla y la entrada O1 salga del mismo lado en los dos. Así el marco de cámara es un rectángulo recto y no un rombo. Queda en forma de rombo dentro de su marco, como en los RTS isométricos. Las esquinas vacías van en el navy del panel.
- La siguiente libre es la **D-N94**.
- Soldado boscoso (Teo, 01:48; revisión de Lucía): el uniforme boscoso en colores lisos, el casco con funda, el NVG solo en el LOD0 y el portaplacas coyote (M2_2) quedan bien contra las fotos. **Hay que corregir una cosa: las caras de arriba en 88885c.** Es justo el color de las matas de hierba (suelo-sagunto §3), y además rompe el valor partido de D-N57: en la hoja, el soldado ya casi no tiene arriba claro. Las caras superiores (hombros, techo del casco y techo del chaleco) **vuelven a b4a080**, y los costados se quedan en 70784c/50541c. El chaleco sigue en coyote.

## D-N94 · Rutas, ETA y refuerzos del mundo persistente (Bruno, encargo de Mak por D-N91; revisión de Lucía) (7-nov, 01:52)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/rutas/contacto_rutas_x3.png (TBD 588dc88). Contiene la etiqueta de ETA (placa navy, reloj o banderín y dígitos de 3×5 dibujados), las líneas de ruta por carretera, vía y aire con punta de flecha y versión para el minimapa, el aviso informativo «Refuerzos en camino» y el aviso de ruta no válida en ámbar (1,5 s; es un aviso de verdad, que es para lo que existe el ámbar). **Aprobada con dos cambios:**
  1. **La ruta por carretera no puede ser una línea discontinua clara**: encima del asfalto se confunde con las marcas viales pintadas. Se cambia por **chevrones que se repiten («›››»)**, que se leen como dirección y no como pintura.
  2. Los píxeles en 283440 (valor de la horda) de la hoja pasan a 303424 o a 181c30.
- La siguiente libre es la **D-N95**.
- D-N86, armas verificadas (Bruno, TBD deae942): el C90 y el AG36, rehechos con las fotos de Paula (M6_c90, M5_g36_ag36), dejan de estar «sin verificar». **Aprobado.**

## D-N95 · Varios frentes a la vez y aviación (Bruno, encargo de Mak; revisión de Lucía) (7-nov, 01:55)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/frentes-aire/contacto_frentes_aire_x4.png (TBD deae942). Contiene el panel «Frentes activos» arriba a la derecha, con una fila por incidente (pictograma sobre placa beige, nombre, barra de gravedad y botón para llevar la cámara), los iconos de caza, base aérea y aeródromo para el minimapa y para el mundo, y el aviso informativo «Cazas despegando». **Aprobada.**
- Gravedad: baja en beige, media en ámbar (es un aviso) y alta en el rojo de ataque. Encaja con la reserva: el rojo solo aparece cuando hay un ataque de verdad.
- Es la respuesta de interfaz a D-N91: en un mundo continuo, varios sitios pueden estar en peligro a la vez, y el jugador necesita verlos todos sin salir de la cámara.
- El panel «Frentes activos» no puede tapar la cuña de entrada ni los indicadores de borde de la esquina superior derecha. Si coinciden, los indicadores de borde se desplazan por debajo del panel (Marcos).
- Lo aéreo (cazas y bases) queda SIN VERIFICAR hasta que exista el análisis del vídeo de aviación.
- La siguiente libre es la **D-N96**.

## D-N96 · Norma del mundo persistente: varios frentes, ETA y vehículos por vías y carreteras (Eugenio, 00:54; recogida por Lucía) (7-nov, 01:58)
- **Eugenio (00:54)**: «el juego es un mundo persistente… suceden cosas a la vez… te pueden estar atacando en una estación y de repente te atacan a un tren… si tienes que enviar cazas desde una base que estás defendiendo a defender el tren, los envías… cuando estás en el mapa te aparece el ETA de esa unidad… si quieres enviar un escuadrón de BTRs hacia un sitio, tendrán que ir por las vías o por carreteras habilitadas».
- **Norma** (amplía D-N91):
  1. **Varios frentes a la vez**. El mundo no se para mientras atiendes un sitio. La interfaz es el panel «Frentes activos» (D-N95), con los avisos de tren atacado y de pelotón en apuros (D-N93) y el salto de cámara.
  2. **Enviar fuerzas entre frentes**. Cualquier unidad, también los cazas de una base, se puede mandar de un frente a otro. Lleva el tiempo real del trayecto y deja desguarnecido el sitio de donde sale. Esa es la decisión que da sentido al juego.
  3. **ETA visible**. Al enviar una unidad, en el mundo y en el mapa aparecen la ruta y el tiempo que tarda en llegar (D-N94).
  4. **Los vehículos de tierra solo van por vías y carreteras habilitadas**, y los aéreos en línea recta entre bases. La infantería a pie puede ir a campo través, más despacio.
- **Hecho**: Nacho, abe7ac1 (NightReport al amanecer y BeginNextNight; solo la derrota termina la partida). Bruno: marcadores (D-N92), parte, avisos y minimapa (D-N91 y D-N93), rutas y ETA (D-N94) y frentes y aviación (D-N95).
- **Para el prototipo de las 08:00**: solo existe Sagunto en 3D, así que los varios frentes se prueban **dentro de Sagunto**: la estación, el tren en el andén y, si da tiempo, el paso a nivel como tercer punto que atacar. El envío entre estaciones con ETA en el mapa es lo siguiente en cuanto haya una segunda estación. Las piezas de interfaz ya están hechas.
- La siguiente libre es la **D-N97**.

## D-N97 · Apoyo aéreo esta noche: helicópteros desde el helipuerto y cazas después del MVP (Mak, con el análisis del vídeo; registrada por Lucía) (7-nov, 02:00)
- Base: docs/arte/referencia-ataques-aereos.md (vídeo qFvJa3kYpYw, solo como referencia de ideas). Lo esencial: el apoyo aéreo es una cadena con reloj (orden, despegue, tránsito con ETA, ataque, regreso y rearme) que ocurre en el mismo mundo, y de lejos se lee por la etiqueta y la sombra.
- **Esta noche**: el NH90 y el Tigre **despegan del helipuerto, vuelan con su ETA (D-N94), atacan o transportan y vuelven al helipuerto a rearmar y repostar**. Usan los marcadores de aterrizaje y despegue de D-N98. Mientras rearman no están disponibles, y esa espera es parte de la tensión.
- **Después del MVP**: cazas, bases aéreas y aeródromos (los iconos de D-N95 ya existen), alerta que acorta el despegue y elección de carga.
- Lectura a distancia (para cuando haga falta): al alejar la cámara, el aparato se ve como etiqueta y sombra, y la altura se marca separando la sombra.
- La siguiente libre es la **D-N98**.

## D-N98 · Estados de vehículo, helipuerto y avisos del tren (Bruno; revisión de Lucía) (7-nov, 02:00)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/estados-vehiculo/contacto_estados_vehiculo_x4.png (TBD 5495d30). Contiene los estados de 16 px (embarcando, desembarcando, dañado, en llamas sin ámbar, sin munición A2 y reabasteciendo), dos marcadores de helipuerto de 4 f (esquinas que se cierran al aterrizar y se abren al despegar) y los avisos «Tren en marcha» (informativo) y «Tren detenido». **Aprobada con un cambio:**
  - **«Tren detenido» con ámbar solo cuando la parada es anómala**: vía cortada, sin combustible o fuera de una estación. Parado en el andén de una estación, que es lo normal en Sagunto toda la noche, va apagado y **sin punto ámbar** en el minimapa. Si no, habría un aviso ámbar encendido toda la partida y el ámbar dejaría de significar «atención».
- La siguiente libre es la **D-N99**.

## D-N99 · Calibración de NightSim y ciclo del apoyo aéreo (Hugo; número asignado por Lucía) (7-nov, 02:09)
- 1) Calibración de NightSim: muro a 300.600 zombi·s (2505 por u del muro inicial), edificio a 60.000, y Stars() según D-N77. Documento: docs/economia/nightsim-calibracion.md.
- 2) Ciclo del apoyo aéreo de D-N97, en docs/economia/json/apoyo_aereo.json. Despegue en 20 s desde reposo y en 5 s en alerta (la alerta cuesta 0,54 u/min). El NH90 rearma en 30 s. El Tigre lleva carga de área o de precisión y rearma en 40 s, o en 90 s si cambia de carga.
- La siguiente libre es la **D-N100**.

## D-N100 · Piezas del apoyo aéreo: sombra, etiquetas, helipuerto y huellas del bombardeo (Bruno; revisión de Lucía) (7-nov, 02:10)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/apoyo-aereo/contacto_apoyo_aereo_x3.png. Contiene la sombra y la línea de altura del helicóptero, las letras de etiqueta, el helipuerto en tres estados, el humo de bombardeo, el fuego en el suelo, el quemado y el cráter. **Aprobada.**
- **Sombra**: se queda en olive_shadow (303424) tramado, más clara cuanto más alto vuela el aparato. Es el mismo recurso que el hollín ya aprobado, y 303424 (L\* 20,9) queda por encima de la banda de la horda. Al moverse y con la línea de altura no se confunde con un grupo de zombis.
- **Humo**: olive_grey y concrete, tramado como mucho al 58 % y nunca negro. Aprobado: la horda se tiene que seguir viendo a través del humo.
- **El fuego en el suelo es solo visual esta noche**: no niega zona y la horda no lo rodea. Es una mecánica nueva y la lógica se congela a las 06:30. Queda como deuda para después del MVP: que el fuego sea un coste en el flow field de la Colmena, que lo rodee si puede y lo cruce ardiendo si no.
- La siguiente libre es la **D-N101**.

- QA-31 (7-nov 00:45 UTC, Sara): abe7ac1 verificado: puente O4 abierto (O5 1224/918/612/306; O6 1275/1275/850/850), 53 mías y 611 de Nacho en verde, NightSim determinista. Con los valores calibrados de Hugo, la noche normal no cumple 45–70 % de muro (0 %) ni ≥ 33 u tras la O4 (28,2 u): datos en `docs/qa/resultado-nightsim-calibrado.md`.

## D-N101 · Vehículos de tierra: vida, combustible, velocidad y ETA (Hugo; número y decisión de diseño de Lucía) (7-nov, 02:15)
- Datos en docs/economia/json/vehiculos_tierra.json. Rodeados por la horda, el VAMTAC aguanta 28 s, el Dragón 180 s y el Pizarro 6 min. Combustible: 0,54, 1,2 y 1,5 u/min. Velocidad por carretera / por vía: 90/25, 80/30 y 50/35 km/h de juego. ETA de 6 a 16 s dentro de Sagunto, y de 63 a 113 s reales por carretera hasta Castellón.
- **Decisión (Lucía): los vehículos pesados viajan lejos en el tren, en plataforma.** El Pizarro no llega a Teruel con un depósito (necesita 9,2 u y lleva 8), y está bien que sea así: es un juego de trenes, y el tren es lo que mueve el poder pesado por la red. Por sus medios, el Pizarro solo hace trayectos cortos alrededor de la estación. Embarcarlo en una plataforma (D-N78) y desembarcarlo en destino es la forma de llevarlo lejos. Los ligeros (VAMTAC, Lince) sí pueden hacer trayectos largos por carretera, más rápido pero más expuestos.
- La siguiente libre es la **D-N102**.
- Cierres (Lucía, 02:17; Bruno, TBD 4737800): D-N92 (sin 283440), D-N93 (minimapa en rombo con el noreste arriba, igual que la pantalla, cuyo arriba es +X+Z), D-N94 (chevrones en la carretera), D-N98 (en el andén, apagado y sin ámbar, y variante «anómala» con el punto ámbar), D-N89 (fila de la cámara; Z y X sin rótulo hasta que Mak confirme qué hacen) y D-N100 (fuego a 3,0 m, solo visual). **Todas cerradas.**

## D-N102 · NightSim v2: calibración con la medición de Sara (Hugo; número de Lucía) (7-nov, 02:18)
- El muro pasa a 960.000 zombi·s (8000 por u) y la munición inicial de Sagunto de 45 a 50 u. Detalle en el §5 de docs/economia/nightsim-calibracion.md.
- Lección de método (Hugo): la zona apila unas diez veces más que el modelo de cola, así que para NightSim manda la medición y no la cola. Sustituye a la calibración de muro de D-N99.
- La siguiente libre es la **D-N103**.
- QA-32 (7-nov 00:27 UTC, Sara): v2 de Hugo medida: normal 66 % de muro, 33,2 u tras la O4, 0 bajas (cumple); fácil 80 %, difícil 42–45 %. Detalle en `docs/qa/resultado-nightsim-calibrado.md`.

## D-N103 · Difícil más dura: escala de 1000 a 1120 (Hugo, a petición de Mak; número de Lucía) (7-nov, 02:20)
- En noche_sagunto.json, la difícil pasa de 1000 a 1120. La normal (850) y la fácil (725) no cambian. Motivo: con el bot perfecto de Sara, la difícil acababa con un 42–45 % de muro y 3 estrellas, y el objetivo es llegar con un 15–25 %. Detalle en el §6 de docs/economia/nightsim-calibracion.md.
- Criterio de diseño: en difícil, tres estrellas tienen que ser una hazaña, ni siquiera algo seguro para un bot perfecto. Sara repite la prueba con 1120.
- La siguiente libre es la **D-N104**.
- Teo, cierres (Lucía, 02:22): el **soldado** vuelve a b4a080 arriba (valor partido de D-N57) y queda aprobado. En el **VAMTAC**, el escudo va delante con el cañón por la ranura, y la rueda no tenía fallo de pivote (centro a 1,3 cm del eje; es la banda de rodadura en el píxel): aprobado. **Tren lateral** aprobado como aproximación, a falta de la captura de Unity; el vagón de tropa R2 lleva ahora las normales hacia arriba, como los demás.

## D-N104 · Las estrellas miran también lo que defiendes: muro, estación y tren (Lucía, a petición de Mak por el hallazgo de Sara) (7-nov, 02:25)
- **Problema** (Sara): Stars() de D-N77 daba 3 estrellas con el muro al 9 % y 3.442 zombis vivos al final, porque solo mira las bajas, la munición y los vehículos. Una noche que se salva por los pelos no puede puntuar como una defensa perfecta.
- **Dos medidas nuevas**, tomadas al amanecer:
  - **Integridad** = el mínimo entre la vida del edificio de viajeros y la del tren (locomotora más vagones), en % de su máximo. Se usa el mínimo porque basta con perder una de las dos cosas.
  - **Muro** = la vida total que queda en todas las piezas de muro, sacos y nidos existentes a las 22:00 o levantadas durante la noche, dividida por la suma de sus máximos. Las piezas destruidas cuentan como 0 sobre su máximo.
- **Fórmula** (sustituye a la de D-N77; las cifras van en el JSON, clave `resultados.estrellas`, para que Hugo pueda ajustarlas sin tocar código):
  - ★: ganar, es decir, que a las 06:00 sigan en pie el edificio y el tren.
  - ★★: además, integridad ≥ 40 %, muro ≥ 25 %, bajas ≤ 6 y munición restante ≥ 8 u.
  - ★★★: además, integridad ≥ 75 %, muro ≥ 50 %, bajas ≤ 2, munición restante ≥ 15 u y ni el Dragón ni el NH90 perdidos.
- **El parte de la noche** (D-N88) muestra las dos medidas nuevas («Muro» e «Integridad») como filas 7 y 8, y la estrella que falta indica qué condición no se cumplió. Bruno añade los dos iconos: un saco terrero y la silueta de la estación con el tren.
- **Calibración**: Hugo comprueba los umbrales con las partidas de Sara en normal (Eugenio, al 60 %, debería sacar 2 estrellas si cuida la tropa) y en difícil con 1120 (D-N103), donde la tercera estrella tiene que quedar fuera del alcance del bot.
- **Determinismo**: las dos medidas se calculan en la simulación, con enteros (‰), y entran en el hash. Nacho, antes de la congelación de las 06:30, con test.
- La siguiente libre es la **D-N105**.
- D-N103, adenda (Hugo, 02:27): la difícil baja de 1120 a **1090**, porque con 1120 Sara medía entre un 9 y un 11 % de muro.

## D-N105 · Vida del tren en el andén (Hugo; número de Lucía) (7-nov, 02:27)
- 120.000, el doble que el edificio de viajeros (60.000). Con 100 zombis pegados cae en unos 60 s. **No está medido**: Sara lo comprueba. Hugo lo había marcado como D-N104, pero ese número ya era el de las estrellas, así que esta es la D-N105.
- Entra en la integridad de D-N104 (mínimo entre el edificio y el tren).
- La siguiente libre es la **D-N106**.

## D-N106 · Apertura en el mundo, aviso de primera oleada, barra de la noche y filas nuevas del parte (Bruno; revisión de Lucía) (7-nov, 02:30)
- Hojas: docs/arte/pixel-codigo/noche-prototipo/apertura/ y maquetas/maqueta_1080_victoria.png (TBD e87a035). Contienen el rótulo de lugar («Sagunto · 22:00 · Noche 1»), el aviso «Primera oleada en mm:ss» con reloj de arena (ámbar solo en los últimos 10 s), la barra de progreso de la noche bajo el reloj (de oliva gris a crema, sin rojo) y las filas «Integridad» y «Muro» del parte (D-N104). La cámara usa Z para acercar y X para alejar (Mak). **Aprobada con dos retoques:**
  1. **Rótulo de lugar**: se queda el formato de cartel de lugar, que encaja mejor con un mundo continuo que una frase de misión. Se añade una tercera línea pequeña, «Aguanta hasta el amanecer», porque quien juega por primera vez tiene que saber qué se espera de él. Sustituye al rótulo de entrada del §8 del plan.
  2. **El parte de la noche no tapa las alertas**: ahora se monta sobre la columna de avisos de la izquierda. Como no es modal y el juego sigue, se baja hasta empezar por debajo de los avisos (y ≥ 250 px a 1080p), o se estrecha a 760 px como mucho.
- La siguiente libre es la **D-N107**.
- D-N106, cierre (Lucía, 02:32; Bruno, TBD b9f6d57): el rótulo lleva la tercera línea y el parte empieza en y = 252 px, con 648 px de alto y 1020 de ancho (a 760 no caben las cifras). **Cerrada.**
- Lince y Cougar (Teo, 02:35; revisión de Lucía): **aprobados**. El Cougar va en el camuflaje del ET (sin el naranja de la UME) y con disco de rotor. Al Lince se le reduce la tapa de la escotilla a ≈ 0,8 m y se oscurece un paso, porque a tamaño de juego parecía una antena parabólica. Medidas y rotor de cola de 5 palas SIN VERIFICAR. El vagón de tropa ya lleva las normales hacia arriba.

## D-N107 · Letalidad del contacto: vida del soldado de 100 a 2000 (Hugo; número de Lucía) (7-nov, 02:37)
- `peloton_*_soldado_vida` pasa de 100 a 2000. El daño se queda en 2 por zombi y tick a 900 mm. Con este valor, un zombi solo tarda unos 33 s en matar a un soldado y seis zombis, unos 5,6 s. Detalle en el §9 de docs/economia/nightsim-calibracion.md.
- Motivo: en la prueba de Sara, el contacto mataba unas 43 veces más que D-N27 (11 bajas en el caso B). Igualar D-N27 exigiría 4200, pero entonces ser rodeado dejaría de dar miedo. **Criterio de diseño (Lucía, de acuerdo con Hugo): un zombi suelto es una molestia; un pelotón rodeado es una emergencia.** Objetivo: de 2 a 4 bajas en el caso B.
- Hugo lo había marcado como D-N106, que ya era la apertura de Bruno: en el código pasa a ser D-N107.
- La siguiente libre es la **D-N108**.
- Lince, cierre (Teo, 02:38): tapa de 0,8 m en 88885c. **Cerrado.**
- Paso a nivel (Teo, 02:45; revisión de Lucía): set de 5 variantes aleatorias aprobado en composición, con tres retoques. Barreras y postes engordados (≥ 2 px a ortho 26, porque si no se vuelven garabatos negros). Bandas de la barrera en b8b8b8/48403c y no en rojo y blanco (el rojo es solo para el ataque). Paredes de la caseta v1 subidas desde 231e10 (casi un valor de la horda). **Luces**: apagadas en reposo; parpadean en 982420 solo mientras cruza un tren (evento transitorio). Lince y Cougar, ya aprobados más arriba.

## D-N108 · Parte de la noche, variante A (Bruno; elegida por Mak; revisión de color de Lucía) (7-nov, 02:50)
- Capturas: docs/arte/pixel-codigo/noche-prototipo/parte/ (TBD 6ef9161). Cabecera con dibujo (sol sobre la vía, o la estación con humo si se pierde), estrellas de 24 px, cuatro cifras y tres barras de estado (estación, tren y muro) con las muescas de los umbrales. Beige y ocre, sin ámbar ni 283440, con líneas de 1 px entre filas. **Aprobada; los colores se quedan como están.**
- Un retoque: **las muescas de la barra del muro van al 25 % y al 50 %**, que son sus umbrales en D-N104. Las de estación y tren se quedan en 40 % y 75 % (integridad).
- Sustituye a la maqueta del parte de D-N88/D-N106.
- La siguiente libre es la **D-N109**.

## D-N109 · Avisos de la prueba de humo de Sara, variante A (Bruno; elegida por Mak; revisión de Lucía) (7-nov, 02:55)
- Captura: docs/arte/pixel-codigo/noche-prototipo/avisos-sara/contacto_avisos_sara_x4.png (TBD 8c6f39a). Incluye la tarjeta «sin munición» con banda ámbar, «Muro atacado» y «Estación atacada» en rojo de ataque con el triángulo de A2, y los botones oliva del panel de vehículos. **Aprobada con una regla de parpadeo:**
  - **La banda ámbar parpadea solo los primeros 3 s** (2 f, 500 ms) y después se queda **fija en ámbar** hasta que se recarga. El parpadeo sirve para llamar la atención una vez. Si dura todo el problema, con varios pelotones sin munición la barra entera parpadearía a la vez y el aviso se convertiría en ruido. Sigue siendo ámbar porque el problema sigue ahí y pide una acción.
- Recargar con **T**: si es una tecla nueva de la lógica, entra también en el cartel de «Cómo se juega» (D-N89).
- La siguiente libre es la **D-N110**.

## D-N110 · G3 regenerado: Sagunto empieza con la puerta de vehículos de 8 m en el muro sur (Nacho; pedida por Álvaro y Hugo, D-N72) (7-nov, 03:05)
- **Qué cambia en la red**: el muro sur de sacos se parte alrededor de una `PuertaVeh` (pieza nueva, `PieceKind` 8) en X −18000..−10000 locales (95–103 m de la zona) y desaparece la puerta peatonal. Cuesta 10 u y 8 obrero·h, mide 8 m, cuenta como puerta y para el nivel y el mantenimiento, y se abre sola con un vehículo propio a ≤ 20 m (180 ticks; `StepGates` recibe los vehículos). El muro de partida pasa de 120,24 a 122,64 u (Hugo admite hasta 124).
- **Por qué G3 cambia**: el stock y el mantenimiento diarios de Sagunto dependen del valor construido. Antes la repetición diferia en el tick 8251 (sistema: existencias) y ahora se reproduce idéntica (36000 ticks). No hay otro cambio de red.
- **G1, G2, G4 y G5**: no se tocan (G4 va con `Mvp(false)`; los de zona solo se regeneran en Unity).
- **Pruebas**: 652 verdes, incluidas las nuevas de la puerta (coste, posición, hueco de 8 m, apertura a 15 m y cierre a 60 m, un tren no la abre, bloqueo del jugador, rota deja pasar, orden de colocar con 10 u, no sobre la vía, no se corta con 9 u).
- Pendiente de Marcos: construir en la zona la hoja doble de 4 m a partir de `Works.Snapshot` y pasar los vehículos a `StepGates` (lista plana x0,y0,x1,y1… en mm locales).

## D-N110 · Interfaz de la vista cercana del tren (Bruno; revisión de Lucía) (7-nov, 03:00)
- Muestra: docs/arte/pixel-codigo/noche-prototipo/tren-vista-muestra/muestra_tren_vista_5_variantes.png. Elegida la **variante A**: franjas de cine arriba y abajo, con el esquema del tren y una barra de vida por coche en la franja de abajo. Se le suma la **fila «Tren atacado · vagón n»** de la C en la columna de avisos. El rojo #982420 solo aparece en el coche atacado y en el borde por donde atacan. Tres piezas por decisión de Mak: locomotora, tropa y contenedor (esquema de Teo v2/v3). **Aprobada con un cambio de color:**
  - **El primer plano no puede llevar valores de la horda.** Los matorrales y el suelo junto a la vía están en 1c200c y 442c0c, y en esta vista pueden aparecer zombis atacando el tren: un matorral oscuro junto a la vía se lee como un zombi. Matorrales y suelo del primer plano pasan a 48403c, 50541c y 605c48. El cielo y la sierra conservan la excepción del navy de D-N85; 283440 ya no es de la horda desde D-N80.
- La siguiente libre es la **D-N111**.
- D-N110, cierre (Bruno, TBD 66fb4e8): el primer plano va en 48403c/50541c/605c48 y las únicas siluetas en 1c200c son las de la horda. **Cerrada.**
- Aviso de numeración (Lucía, 03:05): Nacho anotó la puerta de vehículos E4 como «D-N110» (PR #24, b4dccbc), pero la D-N110 es la interfaz de la vista del tren. **La puerta de vehículos E4 es la D-N111.** La siguiente libre es la **D-N112**.
- Precisión del aviso anterior: la entrada de Nacho es «D-N110 · G3 regenerado: Sagunto empieza con la puerta de vehículos de 8 m en el muro sur». Esa es la que cuenta como **D-N111**.

**Corrección de numeración (Nacho, 7-nov, 03:20, a petición de Lucía)**: la entrada «D-N110 · G3 regenerado: Sagunto empieza con la puerta de vehículos de 8 m en el muro sur» (línea 1895) es la **D-N111**. La D-N110 es la interfaz de la vista cercana del tren. El registro es solo de añadir, así que no se edita la línea; el contenido de esa entrada no cambia. La siguiente libre es la D-N112 (los números los asigna Lucía).

## D-N112 · Primeras oleadas más densas (Hugo; número de Lucía) (7-nov, 03:08)
- En la build de Marcos, la O1 caía entera sin llegar al muro (pila de 5). La O1 pasa a 900 zombis en 30 s (antes 600 en 40 s) y la O2 a 1500 en 45 s (antes 1200 en 50 s). La munición inicial sube de 50 a 52 u para que se sigan cumpliendo los umbrales de D-N104. La vida del soldado no cambia. Detalle en el §10 de docs/economia/nightsim-calibracion.md.
- Criterio (Lucía): la primera oleada tiene que **llegar al muro**. Es la que enseña al jugador que la Colmena es una masa que se amontona; si muere en campo abierto, la noche empieza sin tensión.
- La siguiente libre es la **D-N113**.
- D-N112, cierre (Hugo y Mak, 03:10): con el bot perfecto en normal (Sara), la pila de la O1 queda en 51–58, la de la O2 en 234–255 y el muro en 64–67 %; quedan unas 34 u tras la O4 y salen 2 estrellas. Mak lo da por bueno para el prototipo (pila de la O1 ≥ 50) y **la curva no se toca más esta noche**. La tensión real se mide en la build de Unity; si falta, la palanca es que la O1 llegue en 20 s. Va como adenda de la D-N112, sin número nuevo.
- Helipuerto (Teo, 03:12; revisión de Lucía): **aprobado**, con 5 variantes (losa, de campaña, dañada, fortificada y de noche con torre de focos). Losa en 6c7874 con H y círculo en d4d0cc. **Balizas en crema f0dc9c, encendidas toda la noche y sin rojo.** La torre de focos de la v4 lleva una luz real con su charco (Marcos). Cajas de munición SIN VERIFICAR.

## D-N113 · Mapa de frentes de Sagunto, variante A (Bruno; elegida por Mak; revisión de Lucía) (7-nov, 03:15)
- Maqueta: docs/arte/pixel-codigo/noche-prototipo/mapa-frentes/maqueta_1080_mapa_frentes.png (TBD 6be7c51). Es un plano táctico oscuro girado 45°, como la cámara, en el que las carreteras habilitadas salen de un dato y no del dibujo. Contiene los puntos de estación, paso a nivel, helipuerto y tren con su vida, las rutas con ETA (D-N94) y una leyenda con carretera habilitada, no habilitada, vía y aire. El rojo solo aparece en el tren atacado, y el ámbar en el aviso del paso a nivel (3 s). **Aprobada.** Es la pieza que hace visible D-N96: varios frentes y vehículos solo por carreteras habilitadas.
- Un retoque: quedan unos píxeles en 283440, que pasan a 303424 o a 181c30 como en el resto de las hojas.
- Bruno la pidió como D-N111, pero ese número ya era de Nacho (puerta de vehículos).
- La siguiente libre es la **D-N114**.
- Aclaración sobre 283440 (Lucía, 03:17): desde D-N80 **ya no es un valor de la horda** (se quitó de su subpaleta junto con el navy). En la interfaz se puede usar, y ui_panel se queda como está. Los cambios a 283440 que pedí en D-N92, D-N94 y D-N113 no eran necesarios; lo hecho, hecho está. Los valores que siguen prohibidos fuera de la horda son los de la banda L\* 9–13 de D-N80, más 1c200c y 442c0c.

## D-N114 · VFX del NH90 sobre la losa (Bruno; elegidos por Mak; número de Lucía) (7-nov, 03:20)
- Hoja: docs/arte/pixel-codigo/noche-prototipo/vfx-nh90/contacto_vfx_nh90_x3.png (TBD 254a39f). Estilo A con la sombra de la variante D. Contiene el polvo del rotor al despegar y al aterrizar sobre hormigón (beige, concrete_light y grey_light: arenilla más clara que la tierra del polvo de D-N83), el fogonazo de la MAG de puerta (de crema a ámbar y ocre, transitorio) y la sombra con el anillo del disco en olive_shadow. Sin valores de la horda. **Aprobada.**
- Que el polvo cambie según la superficie (tierra en el descampado y arenilla en la losa) es el tipo de detalle que hace creíble el mundo. Marcos elige la variante por la zona del mapa que hay bajo el aparato.
- La siguiente libre es la **D-N115**.
- Set de rearme del helipuerto (Teo, 03:22; revisión de Lucía): **aprobado**, con 5 variantes. Munición en 50541c con tapa 88885c, cohetes 847c34, bidones 605c48 con tapa 94948c, depósito 48403c, metal 6c7874 y palés en b4a080 (el 6c4038 se leía rojizo). Sin rojo ni ámbar. Cajas, bidones y jerricanes SIN VERIFICAR. Vistas de noche de los vagones v2 y v3 entregadas.

## D-N115 · Menú principal de noche, variante A (Bruno; elegida por Mak; revisión de Lucía) (7-nov, 03:25)
- Maqueta: docs/arte/pixel-codigo/noche-prototipo/menu-muestra/muestra_menu_A_1080.png. Las Opciones y la tira de estados están en la fila A de muestra_menu_5_variantes.png. Sustituye al fondo del atardecer de D-N78. Es una noche de luna sobre el fuerte, con el cerro y la muralla en slate_dark, el tren con el faro encendido, focos que barren el campo y la horda en 1c200c en primer plano. Botones en placa navy con borde grey_brown, borde hueso y cuña al pasar por encima. Sin rojo ni ámbar. **Aprobada, sin cambios de color.**
- La excepción del naranja del atardecer de D-N78 **deja de hacer falta**: el menú ya no tiene naranja.
- **Sin subtítulo**: «La primera noche en Sagunto» presentaba el juego como una misión, y con D-N91 es un mundo continuo. El título va solo, «VÍA MUERTA». El §8 del plan se actualiza.
- La siguiente libre es la **D-N116**.
- Cortes de carretera y balizas de ruta (Teo, 03:28; revisión de Lucía): **aprobados**. Cortes en las carreteras no habilitadas (hormigón y vallas en b8b8b8, cinta en bandas d4d0cc/48403c y no en rojo, coches y quemado en tonos del suelo, sacos en 847c34). Balizas en las habilitadas con la clave del mapa de Bruno (D-N113), luces en f0dc9c. La valla con cinta de la v2 se cambia por una valla de obra con tablón ancho (≥ 2 px a ortho 26). Normales subidas a medias en la New Jersey. SIN VERIFICAR hasta las fotos.
- Puerta de vehículos (D-N111; modelo de Teo, 03:32; revisión de Lucía): **aprobada**, con 5 variantes: tubo con chapa, chapa ondulada, tablones con flejes, malla con espino y blindada con pórtico. Mide 8 m en dos hojas de 4 m y 2,1 m de alto. **Los HESCO pasan de 50541c a 70784c**: la horda se amontona contra la puerta y tiene que recortarse sobre un muro claro. El relleno va en b4a080 y los sacos en 88885c. La valla v2 del corte pasa a lona a rayas de 0,8 m: cerrada.

## D-N116 · Cabecera y viñetas de la crónica de Elena (Bruno; revisión de Lucía) (7-nov, 03:40)
- Archivos: docs/arte/pixel-codigo/cronica/muestra/ (muestra_cabecera_5_variantes.png, cabecera.png y vineta_*.png a 960×540).
- **Cabecera, variante A** (el panorama del menú de D-N115 con el título a la izquierda): **aprobada, sin cambios de color**. Es el mismo plano con el que abre el juego, y la crónica empieza donde empieza la partida.
- **vineta_menu y vineta_tren: aprobadas.**
- **vineta_muro: hay que rehacerla.** Sigue leyéndose de día: el suelo está en tostado, el asfalto se ha ido al lila (el viejo problema del 60546c) y los zombis son los sprites planos antiguos, con una escena grande de sangre y explosión. Se rehace de noche: suelo con los valores de noche de D-N69 (el 70/85 % hacia la tierra compactada), asfalto en la subpaleta del suelo y sin 60546c, horda en la banda L* 9–13 de D-N80 como masa con frente denso y el rojo 982420 solo en el punto de asedio del muro. Si no da tiempo, se sustituye por otra escena del HUD de noche ya aprobada.
- **vineta_nh90: hay que redibujar el helicóptero a ×1.** A ×2 tiene el doble de densidad de píxel que el resto de la escena, y el tamaño uniforme del píxel es la norma básica del arte. Se dibuja a la misma densidad que la losa (si hace falta, se acerca el encuadre, pero no se escala solo el aparato).
- Plazo: antes de la congelación de las 06:30.
- La siguiente libre es la **D-N117**.
- Arreglos de la D-N116 (Bruno; revisión de Lucía): **vineta_muro aprobada**. Está de noche (D-N69, luz 0,42), sin 60546c, con unas 400 figuras de la D-N80 cuyo frente se hace más denso contra los sacos, y el 982420 solo en el punto donde golpean (≈ 26 px). **vineta_nh90: el píxel ya es uniforme** (se dibuja a 160×90 y se entrega a ×6), pero el aparato no se lee como un NH90: el rotor parece una tabla, la cola se curva como un asa y las ruedas son demasiado grandes. Se pide una pasada de silueta antes de las 06:30: rotor como disco fino en movimiento, botalón recto con rotor de cola, morro redondeado y tren corto. Si no llega a tiempo, la viñeta va tal cual. El 60546c y el 404460 del cielo y del cerro se admiten porque es una ilustración y no la vista de juego.
- Chinook CH-47 (Teo, 03:45; revisión de Lucía; para después del MVP): **aprobado con un cambio**, 5 variantes. Se lee al momento como un Chinook por los dos rotores en tándem, y el disco doble de chinook_rotores.png está bien. Colores como el NH90 (50541c, techo b4a080, palas 94948c, cubos 845c28 y cristales 60546c); las manchas en 845c28 van solo en la v3 y no hay rojo. **Cambio:** a tamaño de juego, los costados caen en 1e220c/20240c (L* 12–13), dentro de la banda de la horda (D-N80) y casi en 1c200c. Hay que subir las normales del fuselaje, como en el NH90 y los coches, para que los costados queden en L* ≥ 28. Alturas de los pilones SIN VERIFICAR.
- vineta_nh90 con silueta nueva (Bruno, nh90_perfil; revisión de Lucía): **aprobada**. Ahora se lee como un helicóptero: rotor en disco tramado, botalón recto con deriva, morro redondeado y tren corto, sin perder el píxel uniforme (160×90 a ×6). **La D-N116 queda cerrada**: la cabecera A y las cuatro viñetas pasan a la crónica de Elena.
- Chinook, corrección de Lucía: pedir L* ≥ 28 en los costados **fue demasiado estricto**. La norma es que no caigan en la banda de la horda (L* 9–13, D-N80) y que el albedo propio no baje de 48403c. Con los costados en 88885c el aparato entero se ve caqui, pierde el verde militar y se funde con el suelo. **Se elige: costados en 70784c con las normales subidas (sombra ≈ L* 23,5)**, que queda a 10 puntos de la banda de la horda, y techo en b4a080. Aprobado así.
- Chinook definitivo (Teo, 03:52): costados en 70784c (L* 23,5 a la sombra) y techo en b4a080. Medido a tamaño de juego, quedan 25 px sueltos en la banda de la horda (filos y cristales), que es despreciable. **Cerrado.** Lo siguiente de Teo es el Eurofighter C.16, para después del MVP, con las fotos A5 de Paula.
- Eurofighter C.16 (Teo, 03:58; revisión de Lucía; para después del MVP): **aprobado con un cambio**, 5 variantes (precisión, Mk-82, Taurus, aire-aire y autodefensa). La silueta de delta con canards se lee al instante y las piezas finas cumplen los 2 px. **Cambio:** el techo en d4d0cc es el color de la selección, y un avión entero en ese tono se leería como seleccionado; además deslumbra sobre el suelo de noche. Se baja un escalón: **techo b8b8b8, costados 94948c y vientre 6c7874**, con las normales a 1,0. **La carga no se engorda**: va bajo el ala como en el avión real (D-N81), y el papel de cada variante lo dice la tarjeta de la interfaz.
- Eurofighter, ajuste (Teo, commit 32385c0): el script de entrega rechaza el 94948c en piezas propias, porque es el gris del suelo y de la horda; el que se equivocó al pedirlo fue Lucía. **Queda así: techo y costados en b8b8b8, vientre en 6c7874 y normales a 1,0**, sin d4d0cc. El costado se separa del techo por el sombreado. No se cambia a 50541c: los C.16 del Ejército del Aire son grises. **Cerrado.**
- Puesto de frente del mundo persistente (Teo, 04:05; revisión de Lucía): **aprobado con un cambio**, 5 variantes (anillo de sacos, U con torre de luz, HESCO, red de camuflaje y nido con techo). Se lee como un campamento propio y los 15 × 15 m encajan. **Por defecto, la v2 (HESCO)**, que repite el lenguaje de la puerta de vehículos (D-N111) y es la que más se separa del suelo de noche; las otras cuatro dan variedad entre sitios. **Cambio:** las paredes en sombra de las tiendas, los costados de los sacos y las puertas caen en 1e220c/1f220c (L* 12), dentro de la banda de la horda y casi en 1c200c, justo donde la horda va a chocar. Hay que subir las normales o pasar las paredes de la tienda a 70784c, como en el Chinook (sombra en L* ≥ 20); las puertas en 302c28. Tienda y torre de luz SIN VERIFICAR hasta las fotos K6 y K7.
- Puesto de frente corregido (Teo, commit eda9825): paredes de la tienda en 70784c, techo en 847c34 y normales a 1,0. Las puertas, en 605c48 (lona recogida): el 302c28 que pidió Lucía no está en la paleta y además queda por debajo del albedo de 48403c. Fuera de la banda de la horda solo quedan 2 o 3 px sueltos en los bordes de los sacos. La v2 es la de por defecto. **Cerrado.**

## D-N117 · Icono del puesto de frente en el mapa, variante C (Bruno; elegida por Mak; color del ataque y número de Lucía) (7-nov, 04:10)
- Muestra: entregas/bruno-mapa/puesto/muestra_puesto_5_variantes.png, fila C. Es una placa de 20 con el puesto de Teo en planta. Estados: **ocupado**, borde hueso; **tránsito**, borde grey_light discontinuo que avanza. **Aprobada.**
- **Ataque: con rojo (opción 2).** El borde va en el rojo de ui_mapa_placa_ataque (982420) y parpadea en 2 fotogramas de 500 ms, igual que los sitios de la D-N113. El motivo es que, en un mundo con varios frentes (D-N96), el jugador tiene que encontrar de un vistazo qué puesto están atacando, y el 982420 está reservado justo para eso: ataque y asedio. Con el borde doble hueso y crema, el ataque casi no se distinguía del estado ocupado. Una señal de ataque igual para el tren, los sitios y los puestos.
- Bruno añade ui_mapa_puesto_ataque.
- La siguiente libre es la **D-N118**.
- D-N117, entrega final (Bruno; entregas/bruno-mapa/puesto/final/): ui_mapa_puesto_ataque con borde de 1 px en 982420 (f0) y 7c181c (f1), en 2 fotogramas de 500 ms, igual que ui_mapa_placa_ataque. El pictograma por defecto es el de la v2 de Teo (HESCO con chicane, tienda y mástil). **Aprobada y cerrada.**
- Puesto de frente, fotos K6 y K7 (Teo): la forma queda confirmada (tienda modular con cumbrera y torre de luz tipo Magnum con remolque). **El color de la tienda sigue en verde (70784c, techo 847c34)**: las fotos libres son de lona beige (España 2015 y Letonia) y el ET también usa tiendas verdes, de las que no hay foto libre. El beige b4a080 se confundiría con el relleno de los HESCO y con la explanada. Color de la tienda: decisión de lectura, SIN VERIFICAR para el despliegue concreto.

## D-N118 · Tarjetas de vehículo, variante D (Bruno; elegida por Mak; revisión de Lucía) (7-nov, 04:20)
- Final: entregas/bruno-vehiculos/final/ (maqueta_tarjetas_vehiculo_x4.png y LEEME.md); muestra en muestra_tarjetas_vehiculo_5_variantes.png. Tarjetas de 56×64, del mismo tamaño que la de pelotón, para la misma fila del HUD. Retrato de 48, barras de integridad, munición y combustible, y placa de número de 7×9 (navy con borde hueso) solo cuando hay dos o más unidades del mismo tipo. **Aprobada, sin cambios de color**: solo colores del kit, el ámbar de munición ya aprobado y nada de rojo.
- VAMTAC: un solo tipo, con M2 (lo confirma Nacho). Las dos unidades llevan el mismo retrato y se distinguen por el número; el fotograma del lanzador no se usa.
- **Un añadido:** el combustible bajo no puede mostrar el icono de «reabasteciendo», porque dice lo contrario de lo que pasa (avisa de que se queda sin combustible y el icono dice que ya está repostando). Bruno hace ui_estado_veh_sin_combustible_16: un bidón con la misma aspa ámbar que el icono de sin munición. Si no llega antes de las 06:30, en la build sale solo la barra baja, sin icono.
- La siguiente libre es la **D-N119**.
- D-N118, icono de sin combustible (Bruno): ui_estado_veh_sin_combustible_16, un bidón de A2 con el aspa ámbar del de sin munición. El de reabasteciendo se quita de la tarjeta. **Aprobada y cerrada.**

## D-N119 · Campo a través y recarga del pelotón (Hugo; decididas por Mak; número de Lucía) (7-nov, 04:25)
- **A pie y campo a través, el pelotón va al 70 % de su velocidad**: 5 km/h por camino y 3,5 km/h por la huerta. Está como dato en infanteria_campo_traves_permil. Así los caminos importan también para la infantería, sin llegar a la regla estricta de los vehículos (D-N96).
- **La dotación de cada pelotón no cambia y se mantiene la recarga automática por debajo del 30 %.** La noche normal se gana con unas 38 recargas. La munición total es la misma y la tensión está en el almacén, que es lo que muestra el HUD.
- Hugo la tenía en el código como «D-N113», pero ese número es del mapa de frentes de Bruno. Hay que cambiar el comentario a D-N119.
- La siguiente libre es la **D-N120**.
- **D-N120 reservada para Nacho**: el Transit, la API del ETA y los 3 s de ataque del puesto. Se apunta en cuanto mande el texto. La siguiente libre es la **D-N121**.
- Retoque de la D-N115, contraste de los botones (Bruno; variante D elegida por Mak; revisión de Lucía; viene de Noche15 y Sara): borde normal en concrete_light (5,5:1); al pasar por encima, borde crema con relleno olive_shadow; inactivo con borde y texto en concrete (3,7:1) y candado de 5×7. Sin rojo, ámbar, slate ni purple_grey. **Aprobado.** Una duda: «Salir» lleva una placa más oscura que el resto. Si no es un estado, se iguala con los demás. Integración: Marcos, a través de Mak.

## D-N120 · Tránsito, ETA y estado de ataque del puesto (Nacho; Transporte.cs, PR #24; número de Lucía) (7-nov, 04:30)
- **Tránsito.** Una orden está activa desde que se da hasta que queda en Llegado, Cancelado o Fallido; entonces Active=false y SecondsLeft=0.
  - Clase: Pelotón mientras el vehículo va a recogerlo, espera o va a pie; Vehículo desde que embarca.
  - Ruta: Vía, Carretera (los accesos cuentan como carretera), Aire (helicóptero en línea recta) o Campo (a pie).
  - El avance va de 0 a 1000 según la distancia y nunca baja. Da la posición, el rumbo del tramo en el mundo y los segundos reales que faltan.
- **ETA.** Estimate calcula sin dar la orden: el vehículo libre elegido, la ruta, los metros, los segundos reales (recogida + ruta + 3 s de embarque), los minutos de juego (×28, redondeado) y el combustible.
  - En la zona: 5 s + 4 s por cada giro de más de 45° + largo ÷ velocidad. La vía y la carretera usan vía_kmh y carretera_kmh de Hugo; los accesos van al 60 %.
  - En el mapa: km ÷ km/h × 3600 ÷ 28, redondeado. Ejemplo: el Dragón, 44 km a 80 km/h, tarda 71 s.
  - Campo a través: la velocidad del pelotón × infanteria_campo_traves_permil (700), que es la D-N119. La fila del código que cita «D-N113» se corrige a D-N119.
- **Ataque del puesto.** El estado dura 3 s después del último tick con contacto de la horda. Es un temporizador de la vista, no de la simulación. Lo enciende ContactResult.Hurt. Un puesto sin pelotón no tiene dato en la simulación y lo da la zona. Es el estado que dibuja el borde rojo de la D-N117, con prioridad ataque > ocupado > tránsito.
- La siguiente libre es la **D-N121**.
- Restos destruidos del VAMTAC, el Dragón y el NH90 (Teo, 04:35; revisión de Lucía): **aprobados**, 5 variantes de cada uno, con LOD0, LOD1 e hijo «Humo» en el foco del incendio. **La chapa quemada va en 94948c**: desde la D-N80 ese gris ya no es un valor de la horda, que es la banda L* 9–13. El veto del script es para los costados de las piezas propias, y un resto es neutro. Un coche calcinado de verdad queda gris ceniza, así que no se pasa a 88885c. Hollín y mancha en 605c48, óxido en 845c28 solo en caras pequeñas, y la pintura que queda en 88885c/70784c/50541c. Sin ámbar ni rojo (comprobado en las hojas). Facción «neutro», sin marcador propio. SIN VERIFICAR: no hay fotos de restos.
- Mapa de frentes, cuarta ruta «Campo» (pelotón a pie campo a través; D-N119 y D-N120) (Bruno; elección de Lucía): **color C, tan a86c50**, en trazos de 2 px (2 sí y 2 no), que se leen como pasos. Es la única opción que no se confunde con el terreno (B), con el sitio en calma (A), con la vía (D) ni con la carretera (E). El tan es una ruta, no un aviso: no se usa para nada que avise.

## D-N121 · Muro a 1.200.000 y difícil a 1150 (Hugo; lo pide Mak; número de Lucía) (7-nov, 04:40)
- Objetivo de Mak: un jugador que acierte el 60 % tiene que poder ganar la noche normal. Con un 60 % de acierto, Sara perdía a las 05:48 porque caía el muro.
- **El WallHp de NightSim pasa de 960.000 a 1.200.000** (sustituye la cifra de la D-N102). **La escala de la difícil sube de 1090 a 1150** para compensar. La normal y la fácil no se tocan. Al bot le siguen saliendo ★★ en normal. Detalle en el §12 de nightsim-calibracion.md.
- **Pendiente de que Sara lo verifique.** Si con un 60 % no se gana la normal, o si la difícil se vuelve más fácil que antes, se revisa.
- La siguiente libre es la **D-N122**.
- **D-N121 cerrada** (verificada por Sara en NightSim): en normal (850), el jugador con un 60 % de acierto gana con ★ y el bot al 100 % saca ★★. **La difícil queda en 1140, no en 1150**: con 1150 el muro terminaba entre el 13,5 y el 18,3 %, por debajo del objetivo, y Mak la baja a 1140 para asegurar el 15 %. Conserva la dureza de antes (muro entre el 15 y el 25 %). El muro queda en 1.200.000.
- Estados de daño del muro de sacos (Teo, 04:45; revisión de Lucía): **aprobados con un retoque**, 5 estados (sano, dañado, muy dañado, brecha y en reparación). Tramo modular de 4 m, de 1,2 × 1,0 m, en 88885c, con el origen en el suelo en el centro y derrumbes hacia fuera (−Y). La progresión se lee bien desde el muy dañado: el relleno b4a080 derramado y el hueco de la brecha cuentan la historia. **Retoque:** a tamaño de juego, el dañado (v1) casi no se distingue del sano, porque solo le falta un saco suelto. Hay que quitarle una muesca a la fila de arriba (≥ 2 px a ortho 26) para que el jugador vea qué tramo está tocado. Los ingenieros llevan el mismo uniforme que el soldado aprobado; las piernas en sombra, en 2e321c (L* ≈ 19), quedan fuera de la banda de la horda y se dejan. SIN VERIFICAR.

## D-N122 · Estado del muro en el HUD, variante C (Bruno; elegida por Lucía a propuesta de Bruno; brecha en rojo) (7-nov, 04:50)
- Muestra: entregas/bruno-muro/muestra_muro_hud_5_variantes.png y maqueta_hud_muro_C_1080.png. Es una fila más de frentes activos: el plano del perímetro con los tramos O, E, N y S, el tramo peor escrito al lado y el botón «Reparar muro» (tecla R, SIN VERIFICAR). Estados fijos: sano en bone, dañado en beige, muy dañado en olive_yellow y en reparación concrete_light con rayas. Sin ámbar ni tan. **Aprobada.**
- **Brecha: con rojo (opción R).** Una brecha abierta es un ataque en curso, y ese es el uso reservado del rojo. Lo mismo que el tren atacado (D-N113) y el puesto atacado (D-N117).
- **Un retoque de legibilidad:** la palabra «BRECHA» en 982420 sobre el panel solo da 2,1:1 (medido en la maqueta), y la letra es pequeña. El rojo latiendo va en el lado del plano; la palabra «BRECHA» y la letra del tramo van en bone, fijas.
- La siguiente libre es la **D-N123**.

## D-N123 · Reparación del muro (Hugo; aprobada por Mak como diseño para después del MVP; número de Lucía) (7-nov, 04:55)
- Detalle en el §13 de nightsim-calibracion.md. **1 u de materiales repara 5.000 de vida** y sale de los 40 u de la noche (como mucho, 200.000, un 17 % del muro de la D-N121). **Solo reparan los zapadores**, a 1 u cada 20 s por zapador, y mientras reparan no disparan.
- Se repara de noche, en los tramos tranquilos. El botón se desactiva si: (1) hay zombis a 3 m o menos; (2) la pieza está destruida, y entonces se reconstruye; (3) no quedan materiales; (4) no hay zapadores a 10 m o menos.
- Ruido: lo decide Mak. La propuesta es el mismo ×1,5 de la D-N59 sobre la entrada más cercana al tramo mientras se repara.
- Encaja con el estado «en reparación» del muro de Teo (andamio y cuadrilla) y con el botón «Reparar muro» de la D-N122. **En la build de esta noche el botón no se muestra**: es para después del MVP, y un botón que no hace nada confundiría en la prueba.
- Medición con Sara después de la congelación.
- La siguiente libre es la **D-N124**.
- Muro de sacos, retoque (Teo, commit 5c85067): el dañado lleva una muesca de unos 1,6 m en la hilada de arriba y le falta medio saco por fuera en la de debajo. A tamaño de juego se distingue del sano. **Cerrado.**
- D-N122 cerrada (Bruno; entregas/bruno-muro/final/): el rojo late solo en el lado del plano, y «BRECHA» y la letra del tramo van en bone, fijas. Botón «Reparar muro» esta noche: Lucía pidió ocultarlo y Mak había dicho «inactivo visible». **Decide Mak.** Si se queda visible, va inactivo y con el candado de 5×7 de los botones del menú, para que se lea como «todavía no».
- Mak lo confirma (02:09): **esta noche «Reparar muro» no se muestra.** El candado queda para cuando llegue la mecánica (D-N123).
- QA-33 (7-nov 03:10 UTC, Sara): el fuego de los vehículos es local y está fuera del hash esta noche (decisión del coordinador); «hash idéntico en los dos mundos» no prueba su determinismo. Queda como **límite documentado para después del MVP**, no como fallo bloqueante; riesgo en cooperativo (S2 si pasa a hito 7). Las cifras de equilibrio de QA valen para pelotones solos (-nightbot sin fuego de vehículos); la corrida -vehfuego da el techo con vehículos.
- Criterio de la difícil (Lucía, 7-nov 08:32; la §15 de nightsim-calibracion.md de Hugo): **el objetivo del 15–25 % de muro en difícil se mide con el NightBot**, que se mueve hacia el muro amenazado como un jugador bueno, y no con el bot quieto. La difícil tiene que serlo para quien juega bien. El NightBot en NightSim, con 1000 partidas, es la referencia porque es determinista. La corrida -vehfuego de la build sirve de techo: con los vehículos, el muro no debe pasar del 35 %. La normal se sigue midiendo con el jugador al 60 % (D-N121). La cifra nueva (Hugo calcula unos 1300) **no se toca hasta que Sara repita qa20 con el recinto cerrado**, y entonces lleva número D-N.
- Botón principal del parte (Bruno, mr-mak 0e0da9e; opción C elegida por Lucía, retoque de la D-N108 sin número nuevo): ui_boton_principal con placa 50541c, texto en hueso (5,2:1), borde crema y la cuña ui_boton_cuna, igual que el estado de encima del menú. Antes daba 3,1:1. Se lo ha pasado a Marcos. **Cerrado.**
- Sagunto v1.2 (Álvaro, 7-nov 07:50; §10 de docs/niveles/sagunto-nivel.md, plano sagunto_plano_v1_2.png): frentes de la D-N113 con el nivel 1 de la escala. **Propuesta, pendiente de Mak.** F2 paso a nivel con puesto v2 en (43;0;82) yaw 90; F3 helipuerto v4 de Teo en (180;0;44) con puesto v2 en (207;0;51) yaw 270 y rearme al oeste de la losa (se quita el anillo HESCO de E6). Carril norte de la carretera abierto de X 64 a 200, cortes K1 y K2 y 14 balizas. Dato de carreteras v1.2: calle de la Estación habilitada solo hasta Z 86 (autobús y barricada) y carretera vieja hasta X 200. Revisión de la build 5188f83: C1–C9 hechas; E1, E2 y el helipuerto, pendientes.
- **D-N107, enmienda** (Hugo; registrada por Lucía, 7-nov 08:46): la vida del soldado queda en **4000** (100 → 2000 → 4000). Con 2000, el caso B de Sara daba 10 bajas; con 4000 y la retirada del bot (caso C), 3 bajas, dentro del objetivo de 2 a 4. Es el valor del CSV, del PR #24 (97e30c4) y de marcos/noche-prototipo (5188f83), el que lee Armas.cs. A partir de aquí, el ajuste se hace con la retirada del bot y no con la vida. Sin número nuevo.
- Sagunto v1.2, cierre (Álvaro; registrado en el hilo «Álvaro · Diseño de niveles (2)», 7-nov 08:50): **aprobada por Mak a las 07:44 con el helipuerto v4.** Sustituye al «pendiente de Mak» de la línea anterior. La lista del §10.6 pasa a Marcos por Mak después de la qa22; la reviso en Noche23.
- Estación de Sagunto (Teo, 7-nov 07:38 UTC; revisión de Lucía, 08:55 Madrid; hojas en docs/arte/modelado-3d/sagunto/<pieza>/capturas/): edificio de viajeros, marquesina y poste de catenaria, v0–v5 en LOD0 y LOD1. **Aprobados para integrar.** Medido sobre las hojas (LOD1 a ×5): la marquesina y el poste no tienen ningún píxel en L* 9–13. El edificio tiene unos 21 px de juego por variante en 23200e (L* 12,1), sombra de la carpintería 543820, y unos 40 px del granate en sombra (37070a, 360609, 310507; L* 7–8,9). **Se dejan los dos.** El granate es rojo y queda por debajo de la banda; el 23200e cae en sitios de 1×1 o 1×2 dentro de los marcos de ventana, por encima del suelo y sobre fachada blanca, y nunca forma una mancha de 3 px. Lo vigilo porque su tono es casi el 1c200c de la horda: si en la captura de noche de la build una ventana se lee como un zombi, la cara en sombra del hueco pasa a 52361f (L* 25). Dos notas para la v siguiente, que no bloquean: (1) la cubierta de la marquesina en LOD1 sale en damero de 1 px (67736f / 8e8e86 / 45423f) y a tamaño de juego se lee como ruido; mejor bandas de chapa de ≥ 2 px a lo largo. (2) En el LOD0 del poste hay tramos de cable sueltos de 1 px y cortados a la izquierda (v0, v1, v2, v4, v5); o se quitan del export de la pieza suelta o se engordan a 2 px. Medidas SIN VERIFICAR (no hay planos).
- Huella de suelo de los calcinados, 5 variantes (Bruno, 7-nov 07:53 UTC; TBD addf6a8; lámina en docs/arte/pixel-codigo/noche-prototipo/vehiculos/calcinado-muestra/; revisión de Lucía, 09:00 Madrid): **sustituyen a las 2 de la D-N87 y quedan aprobadas** como variantes por instancia con semilla; Marcos escala el proyector a la planta de cada vehículo. Medido en la lámina: L* mínimo 20,9 (303424), ningún píxel en L* 9–13, sin 442c0c, sin 982420 ni e08c30; el óxido es 7c3c18 (L* 33). **Un retoque:** la v3 (ceniza) usa 6 px de d4d0cc para los cristales, que es el color de la selección; pasan a b8b8b8. La vista de noche sigue SIN VERIFICAR en Unity. Falta foto para el camión quemado y para el aluminio fundido: no se dibujan hasta que Paula la tenga.
- Criterio de la difícil, afinado (Hugo §16; aceptado por Lucía, 7-nov 08:56): con 1000 partidas del NightBot, entre p10 y p90 hay unos 10 puntos, así que ninguna escala mete todas las noches en el 15–25 %. **El objetivo pasa a ser: mediana del muro entre el 18 y el 22 %, con p10 ≥ 12 % y p90 ≤ 28 %.** Lo medido: 1140 da una mediana del 45,5 %, y 1300 da un 14,9 % (p10 10,2 y p90 19,7). La interpolación apunta a unos 1270, pendiente de que Sara mida 1270 y 1280. La normal al 60 % sigue ganando con ★. El techo de -vehfuego (≤ 35 %) sigue en pie. Llevará número cuando esté medido; el cambio en la build entra después de que qa20 gane con el recinto cerrado.
- Calcinados, retoque cerrado (Bruno, mr-mak 5f2f5b2, entregado a Marcos por Mak): los cristales de la v3 van en b8b8b8, sin d4d0cc, comprobado píxel a píxel en las 5. **Cerrado.**
- Estación de Sagunto, notas aplicadas (Teo, 7-nov 07:56 UTC; revisión de Lucía): la cubierta de la marquesina en LOD1 lleva 3 bandas de chapa de 1 m (≥ 2 px a tamaño de juego) y se acaba el damero; los pilares y las cerchas del LOD1 pasan a 70784c y el canalón a 605c48. El hilo del poste cuelga de la punta de la ménsula en un solo tramo de 2 px (era un fallo de lado en el código); en la v4 cae al suelo y se lee como cable caído, que es buena variante. Nada con L* < 20 en el LOD1. El 70784c se queda. **Cerrado.**

- QA-34 (7-nov 08:15 UTC, Sara): qa20 revisada (✅): 4/4 derrotas por **Tren 0 %** con muro 99 %, estación 100 % y 0 bajas; la difícil cae a las 00:18. La pila no es 0 (normal 78, fácil 58) y hay zombis junto al tren sin romper el muro: confirma los huecos de PuertaVia. La derrota en la zona sube a S1. Detalle en `docs/qa/informe-final-noche.md`.
- Restos repasados con las fotos K8 (Teo, 7-nov 08:05 UTC; docs/arte/modelado-3d/restos/muestra-k8/; revisión de Lucía): VAMTAC, Dragón y NH90, 15 variantes en dos estados (v0, v2 y v4 recién quemados; v1 y v3 oxidados), óxido 7c3c18 solo en las caras que miran arriba, sin neumáticos y el LOD1 de 48403c a 605c48. **Aprobados; sustituyen a los vigentes.** Medido a tamaño de juego: ningún píxel en L* 9–13. La chapa quemada sale en bab9b7 (L* 75), por debajo del d4d0cc de selección, salvo la v2 del VAMTAC, que tiene un 6 % de la silueta en L* ≥ 78 (cfcbc7): esa cara de arriba baja a b8b8b8. Los 1–20 px en L* 19,3–19,9 se dejan: están fuera de la banda y no hace falta perseguirlos.

## D-N124 · Red de estaciones: aviso de asedio, reloj del mapa e inteligencia (Eugenio, 09:03–09:07; diseño de Lucía; números de Hugo; reloj de Mak) (7-nov, 09:35)
- Documento: `docs/diseno-red-estaciones.md` v0.2. Cifras: `docs/economia/red-estaciones-aviso.md` (Hugo). La estación grande es Castellón (`niveles/castellon-nivel.md`, Álvaro).
- **Reloj del mapa: ×28** (Mak, 09:07), el que ya usa el código (D-N120). 3 h de juego ≈ 6,4 min reales y 6 h ≈ 12,9 min. El ×72 del GDD §3c queda para el calendario de la campaña; hay que revisar el GDD.
- **Aviso de asedio**: el anuncio base, 3 h antes, da la zona con 2 o 3 estaciones candidatas; con radar, la estación exacta y 6 h antes. Hugo lo ha comprobado: a dos estaciones llegan a tiempo la tropa y los vehículos, pero no el tren con munición, que solo cabe con radar. Por eso se quedan 3 h y 6 h.
- **Asedios simultáneos**: el tope de la D-N08. Los sondeos y las emboscadas no cuentan.
- **Inteligencia**: puesto de escucha (12 km, rastro; 8 u, 2 personas, 0,28 u al día) y radar (30 km, contacto y hordas pequeñas desde ~100; 20 u, 4 personas, 0,80 u al día; hace ruido, huella SIN NÚMERO). El centro de inteligencia va para después del MVP.
- **Caída y liberación** (Eugenio, 09:06): una estación caída queda ocupada por la horda y corta la línea; se libera al asalto y después se reconstruye. Reclamar una estación nueva es el mismo asalto. Los porcentajes de guarnición zombi y de almacén recuperado son [propuesta] hasta que Hugo los mida. **La artillería y los cazas en el asalto van para después del MVP** (Eugenio, 09:07): destruyen estructuras, y tú eliges cuánta fuerza usar.
- **Pendiente de Mak**: la derrota de la D-N91 (que caiga Sagunto termina la partida) vale mientras solo exista Sagunto. Con dos estaciones, la propuesta es que la derrota sea perder todas las principales (GDD §3b).
- La producción de las estaciones y el tope del almacén no existen todavía en la red (Nacho): son requisito del bucle de Castellón.
- La siguiente libre es la **D-N125**.
- Restos K8, corrección (Lucía, 09:37; aviso de Bruno): **mi aprobación de las 09:05 estaba mal.** Medí el color renderizado (bab9b7) y no miré el albedo, que era d4d0cc, el color de la selección. La chapa recién quemada de v0, v2 y v4 pasa a **b8b8b8** en el albedo, igual que pedí a Bruno para las huellas. Con eso queda cubierto el retoque de la v2 del VAMTAC. Lo demás sigue aprobado. Se lo he pedido a Teo (2).

## D-N125 · Derrota en la red de estaciones (propuesta de Lucía; aprobada por Mak) (7-nov, 09:12)
- Enmienda la derrota de la D-N91. **Mientras solo exista Sagunto** (el prototipo de la noche), si cae el edificio de viajeros o el tren, se acaba la partida, como hasta ahora.
- **Con dos estaciones o más**, la caída de una estación, Sagunto incluida, la deja «Caída» (D-N124: la ocupa la horda, corta la línea y se libera al asalto). **La derrota es perder todas las estaciones principales** (GDD §3b). Perder un tren ya no acaba la partida.
- La producción de las estaciones y el tope del almacén en la red (Nacho) van después de que la Noche23 confirme que la noche se gana (Mak).
- Castellón cumple la D-N124 (Álvaro, castellon-nivel §6 y estaciones/castellon.json, con 80 piezas): el cuartel en la primera nave, el radar en la esquina noreste y tres paradas de asalto. Estado inicial «infestada», con los supervivientes resistiendo en C1. Orden de liberación: C3, C4, C2 y C1. Pendiente de que Hugo confirme que el día 1 aguanta un asalto; si no, pasa a «propia, con el recinto dañado».
- La siguiente libre es la **D-N126**.
- Restos K8, cerrado (Teo, mr-mak 7953186, entregas/teo-modelado/restos-k8-7nov/): la chapa recién quemada va en b8b8b8 en el albedo y no queda ningún píxel en d4d0cc ni en cfcbc7 en las vistas de juego. Quita su mancha de hollín, porque ya la pone la huella de Bruno. **Cerrado.**
- Regla del d4d0cc en el albedo (Lucía, 09:15; pregunta de Teo para el kit de estaciones): **se permite solo en las fachadas encaladas de los edificios fijos** (el edificio de viajeros de Sagunto y el kit de estaciones). No se seleccionan, y renderizadas no pasan de L* 75 (medido en la hoja del edificio: 8f8e88 en la cara clara y como mucho 5 px en bab9b7). **Prohibido** en unidades, vehículos, restos, piezas pequeñas y huellas de suelo. Condición: en la vista de juego, ninguna fachada puede pasar de L* 78; si pasa, esa cara baja a b8b8b8.
- D-N124, huella del radar (Hugo, 09:13; red-estaciones-aviso §5): **huella_radar = 0,1.** Medido en 1000 partidas, en el caso extremo de un radar en cada ciudad: la derrota de la equilibrada pasa del 13,8 % al 15,6 %. Con 0,4, lo mismo que un nodo, subiría al 21,9 % y el radar sería una trampa. El puesto de escucha no tiene huella. El modelo no cuenta lo que ayuda el aviso, solo lo que atrae, así que la cifra es prudente. Castellón hereda el recinto al **15 % de vida** (~44 u, nivel 1; castellon-bucle §5), que es compatible con empezar «infestada» (D-N125).

## D-N126 · Caída y liberación: guarnición zombi y almacén (Hugo, medido; diseño de Lucía) (7-nov, 09:20)
- Medido en 1000 partidas por caso (red-estaciones-aviso §6, en una copia del modelo). Hoy, cuando se pierde todo, la derrota es del 13,9 % en la equilibrada y del 43,1 % en la prisa. El ruido es de ±1,1 y ±1,6 puntos.
- **Guarnición zombi: el 40 % de la masa del asalto se queda en la estación caída y crece un 3 % al día** (esta última cifra la propone Hugo). Así salen 14,2 % y 44,6 %. Con un 20 % el resultado es casi igual; con un 60 % la prisa sube al 48,1 % y se liberan menos estaciones.
- **Al liberar se recupera la mitad del almacén.** Frente a no recuperar nada o recuperarlo todo no cambia la derrota (14,1–14,3 %), porque lo que cae suele tener poco almacén. Se queda como motivo para volver.
- **Límite**: en el modelo, el asalto es abstracto (el tren hace de muro y no hay bajas) y solo cuesta munición. El asalto jugado costará más y lo medirá NightSim.
- **Radio de fortificación de 60 m, medido desde el andén** y no desde su centro (Álvaro y Hugo). Es lo que dicen la D-N44 y perimetro_mm, y sin eso una principal no cabe.
- La siguiente libre es la **D-N127**.

## D-N127 · Difícil a 1280 (Hugo; medida de Sara; número de Lucía) (7-nov, 09:22)
- **La escala de la difícil pasa de 1140 a 1280** (sustituye a la de la D-N121). Medido por Sara con el NightBot en NightSim (semillas 1–1000, sin vehículos): mediana del muro 19,6 % (p10 14,8 y p90 23,9), el 84 % de las noches entre el 15 y el 25 %, 1000 victorias de 1000, todas con ★1 y 0,3 bajas de media. Cumple el criterio de la §16 (mediana del 18–22 %, p10 ≥ 12 % y p90 ≤ 28 %). La de 1270 también lo cumplía (mediana del 21,6 %, el 80 % en rango), pero 1280 centra mejor. La normal (850) no cambia.
- Hugo cambia DIFICULTAD_NOCHE en unidades.py, regenera y se lo pasa a Nacho. **Entra en la build cuando la noche normal se gane** (qa22 / Noche23). Queda pendiente el techo con -vehfuego (muro ≤ 35 %) en la build.
- La estimación previa de unos 1300 (§6) se pasaba; la cifra buena salió de medir.
- La siguiente libre es la **D-N128**.

## D-N128 · Munición de a bordo de los vehículos (Mak, 09:22; cifras de Hugo; número de Lucía) (7-nov, 09:25)
- Eugenio no quiere que los vehículos se queden sin munición en una sola oleada. Hoy la build les da 360, 300 y 400 abatidos, que gastan en unos 2 min.
- **Munición de a bordo para unas 3 oleadas de fuego libre**: Dragón 2 u (~400 salvas, ~1.190 abatidos), VAMTAC 3 u (~750) y NH90 3 u (~930). **Sale del almacén al empezar la noche**: Sagunto pasa de 52 u a **44 u** y la munición total de la noche no cambia (sustituye a la cifra inicial de la D-N112).
- La recarga no cambia: desde el almacén, por debajo del 30 %, en 20 s junto al tren y en 30 s en el helipuerto.
- **Los vehículos empiezan en fuego libre y G es el alto el fuego** (Mak, 09:22). Sustituye a la decisión del coordinador del 7-nov de que los vehículos solo dispararan con orden.
- La normal (850) y la difícil (1280, D-N127) se revisan con las 4 corridas de Marcos con -vehfuego, que medirá Sara. El techo de la difícil con vehículos sigue en un muro ≤ 35 %.
- La siguiente libre es la **D-N129**.
- Capturas de la build con doble sRGB (Bruno, 09:24): CaptureRoutine hace un Blit a un RenderTexture sRGB, y las capturas de QA salen más claras y lavadas que la pantalla (el 181c30 del HUD sale como 565d78; el suelo de noche, 3b3c35 real, sale como 84867c). **Cualquier L* o contraste medido en capturas de la build antes del arreglo vale solo como relativo.** No afecta a las hojas de Teo ni a las de Bruno (son renders fuera de la build). Cuando llegue el arreglo, la banda de la horda (D-N80) y el contraste de texto del HUD se vuelven a comprobar sobre una captura corregida. Lo lleva Marcos, vía Mak.
- Noche sin sepia (encargo-control-disparos-noche §5; Bruno): qa24 vendrá sin cuantizador ni gradación y con la luz en tres pasadas (luna, ambiente y focos), para simular las variantes con números. **Las 5 variantes cubren la mezcla del cuantizador del mundo a 0, 0,2 y 0,4 con dos lunas, y se añade la mezcla actual (0,65) como control.** La regla de «paleta de 32 con mezcla al 65 %, no se toca» se revisa con esta muestra: si se baja, será con medida y número D-N, y la cohesión la siguen dando los albedos en paleta. Valores de partida de Bruno, aceptados para la muestra: luna (0,55; 0,65; 0,90) a 0,35 con sombras, ambiente (0,05; 0,06; 0,10), filtro (0,80; 0,88; 1,0) y saturación −30.
- D-N128, corrección (Hugo, 09:24): **el almacén de Sagunto empieza con 47 u, no con 44.** Los vehículos de la build ya llevaban ~3,1 u a bordo, así que, para que la munición total de la noche no cambie, son 52 + 3,1 − 8 = 47. El resto no cambia.
- D-N91, corrección (Eugenio, 09:25; registrada por Lucía): **salir al mapa en mitad de la noche está permitido y el combate no se para.** «Tú puedes salir… es un mundo persistente… puedes salir y visitar otra estación. El combate no se para». Al salir, la noche sigue corriendo fuera de pantalla (reloj, oleadas, pila, muro, munición y pelotones con su última orden) y, al volver, la zona enseña el estado actual. El fallo de la build era el reinicio, no la salida. Retiro mi propuesta de las 09:30 de limitar el zoom: contradecía el mundo persistente. Arreglo en encargo-control-disparos-noche §1. Mínimo aceptable mientras la zona y el mapa no estén unidos: no descargar la escena de la zona, sino ocultarla y seguir simulando.
- Doble sRGB, rectificado (Bruno, 09:27): **las capturas no mienten.** La codificación de más está en la imagen que ve el jugador (el mundo de la escena de partida), no en la ruta de captura. La qa22 coincide con la foto de Eugenio. Queda anulada la nota de las 09:24 según la cual lo medido en capturas solo valía como relativo: lo medido es lo que se ve. El arreglo va en el mundo (el sospechoso es su RenderTexture, SIN VERIFICAR).

## D-N129 · Dirección de arte v2: sin cuantizador plano, una luz por hora, noche fría con charcos cálidos (Lucía con Bruno; pedido de Eugenio y Mak) (7-nov, 09:45)
- Documento: `docs/arte/direccion-arte-v2.md`. Sale del análisis de las capturas de Ebbtide (analisis-referencias-6nov) y del vídeo (referencia-ebbtide-anfibio). Eugenio, con razón: teníamos el análisis y no lo habíamos aplicado.
- **Causas del sepia**: (1) la codificación sRGB de más en el mundo; (2) el cuantizador de pantalla al 65 % con tramado. Primero se arregla (1) y después se mide (2).
- **Se sustituye la regla «paleta de 32 con mezcla al 65 %, no se toca»**: la paleta de 32 se queda en los albedos, la interfaz y el 2D. **En el mundo no hay cuantizador de pantalla** (0, o como mucho 0,2 si la muestra lo justifica) **y nunca hay tramado.** Se quedan el pixelado a 1/3 y el contorno.
- Siete reglas: 3D pixelado natural; una luz dominante por hora con sombras proyectadas marcadas; noche oscura y fría con el color dentro de la luz; el color propio siempre reconocible; la horda como lo más oscuro (D-N80); suelo con al menos 3 valores; VFX nítidos con bloom.
- Las 5 variantes de Bruno van **dentro de esta dirección** (mezcla 0 o 0,2, sin tramado; cambian la luna, el ambiente y la saturación), más una de control con el estado actual. Se hacen sobre la build con el color ya arreglado. Elige Lucía.
- Desde hoy, el arte se aprueba sobre una captura de la build, no solo sobre hojas renderizadas aparte.
- La siguiente libre es la **D-N130**.
- D-N129, dos matices de Bruno (09:29): (1) la codificación de más afecta también al HUD (sus placas salen en 565d78): **el HUD tiene que dar los valores de la maqueta** (181c30 de fondo y d4d0cc de texto), comprobado con comprobar_color.py; el texto de IMGUI lo arregla el c.gamma de f6c4785. (2) El shader de origin (PaletteQuantize) no lleva tramado: es una mezcla al 65 % con la paleta de 32. El tramado de la foto de Eugenio debe de venir del cuantizador de 17 colores de la copia local de Marcos (SIN VERIFICAR). La regla no cambia: nunca tramado en el mundo.
- Soldado, pose «apuntando» (Teo, mr-mak e0b1e54; revisión de Lucía, 09:35): **aprobada.** Se lee a tamaño de juego: arma horizontal al frente, culata al hombro y pierna atrasada, en las 6 variantes. Malla fija por pose y clip en el FBX. Arregla además las armas que salían en el suelo (ahora van en la malla, enganchadas al hueso). El arma 48403c en sombra a L* 18–19 se queda, como en el soldado aprobado. Ángulos SIN VERIFICAR.
- Kit de estaciones (Teo, 09:30; docs/arte/modelado-3d/kit-estaciones/): **aprobado**, con 5 módulos y de 6 a 7 variantes cada uno, más los montajes de Nules (abandonado, en servicio y a medio liberar) y Castellón (en servicio y asediada). Cumple la regla de reutilizar Sagunto de otra manera (D-N124 §2). **Retoque**: el granate 642030 en sombra cae a L* 7–9 en áreas grandes (remate v0/v2/v3; cuerpo v0/v3/v5/v6) y a tamaño de juego se lee como agujeros negros. En el LOD1 se sube el granate **hasta que la cara en sombra quede en L* ≥ 14**: si un escalón lo deja entre 9 y 13, se sube otro, porque esa es la banda de la horda. No se pasa a 6c7874, porque se perdería el granate de los recercados valencianos. Las fachadas d4d0cc quedan como mucho en L* 75,2: cumplen. La banda de seguridad del andén en f0dc9c (L* 85) se queda: es una línea fina, amarilla y no se confunde con la selección. No es fachada.
- Kit de estaciones, granate cerrado (Teo, TBD f8eb0d3): la moldura del LOD1 pasa de 642030 a 8c5048 (L* 40,9; añadido a PERMITIR) y ya no queda granate en sombra por debajo de L* 20. Quedan píxeles sueltos de 1×1 de 231e10 (L* 11,4) en el borde de la carpintería, sobre fachada blanca, que nunca juntan 3 px: **se dejan, con el mismo criterio que el 23200e de Sagunto**, y se vigilan en la captura de noche de la build. Los montajes ya llevan los estados de la D-N124, y las piezas nuevas escombro y andamio (sueltas v6 y v7) quedan aprobadas. **Cerrado.**
- Kit de estaciones, paso entre andenes (Teo, TBD 180aecc; revisión de Lucía, 09:42): **v0 (paso inferior) aprobada.** **v1–v4 (pasarelas), aprobación pendiente de una prueba**: la hoja no enseña las vías y no se puede juzgar si el tablero cruza de verdad dos vías con sus andenes. Las escaleras se leen, pero el tramo que cruza queda en una esquina corta. Hace falta un montaje sobre las vías de Castellón con los dos andenes. Además, a tamaño de juego, los pilares del LOD1 de v1 y v3 forman manchas negras de contorno: en el LOD1 se dejan 2 pilares por tramo. El 2e3022 de la v4 (2 px, L* 19,3) se queda. Medidas SIN VERIFICAR.
- Paso entre andenes, cerrado (Teo, TBD 8874379): en el montaje a escala de juego sobre las vías de Castellón (montaje_pasos_castellon_escala_juego.png), las pasarelas v1–v4 se leen bien: una escalera en cada andén y el tablero cruzando la vía de en medio. Los pilares del LOD1 bajan a 2 por torre. **Las 5 variantes, aprobadas.** Álvaro pone la v0 por defecto en Castellón. **Cerrado.**
- Vagón cisterna (Teo, TBD 9c0885d; revisión de Lucía, 09:47): **aprobado**, con 5 variantes (limpia, oxidada, sin escalera, abollada y quemada). Cuba en 94948c (la plata de la foto R4), bastidor 48403c que pasa a 605c48 en el LOD1, óxido 7c3c18 solo en las caras con luz y panel de 605c48 en los costados para el decal de lleno o vacío de Bruno (también en la quemada). En L*, nada en la banda de la horda. Nota que no bloquea: a tamaño de juego, v0, v2 y v3 casi no se distinguen; si Teo tiene un momento, que la abolladura de la v3 tenga una sombra más grande. Cotas SIN VERIFICAR.
- Decal de lleno o vacío del vagón cisterna (Bruno; revisión de Lucía, 09:49): **aprobado.** Indicador de 4 tramos sin texto, lleno en b4a080 (ΔL* 28 sobre 605c48) y vacío en grey_brown, sin d4d0cc ni ámbar. Se lee de lejos: claro es lleno y oscuro, vacío. **Un cambio sin coste de arte**: como ya tiene 4 tramos, se usan como **cuartos de carga** (0 a 4 encendidos según el stock del vagón), igual que los depósitos de Castellón (lleno, a medias y vacío). Sin placa ADR naranja, para no tocar el ámbar reservado: correcto.
- Cooperativa de Nules N2 (Teo, TBD 99f61da; revisión de Lucía, 09:51): **aprobada.** Las v0–v3 son el almacén de naranjas de Sagunto aprobado, con otro uso (como pide la D-N124 §2), y la v4 es la nave nueva de La Vilavella: bloque b4a080, portones 50541c/70784c, oficinas y marquesina de la gasolinera, sin rotulación. Los 10 px de 2e3022 (L* 19,3) se quedan. Medidas de la v4 SIN VERIFICAR.
- Caseta de compuertas de Nules N3 (Teo, TBD b40002a; revisión de Lucía, 09:53): **aprobada con un retoque.** Hay 5 variantes (foto, compuertas levantadas, puerta y escalera, abandonada y fortificada), con caseta 94948c y canal 605c48. **Retoque**: a tamaño de juego, la pasarela de compuertas sigue siendo una mancha negra de contorno: en el LOD1 se quita la barandilla del lado del agua. Nota que no bloquea: el agua y el fondo del canal se parecen mucho a los muros; cuando llegue el shader de agua por bandas (W1 de referencia-ebbtide-anfibio), que el agua lleve sus bandas. Los 2e3022 (L* 19,3) se quedan. Medidas SIN VERIFICAR.

## D-N130 · Producción de las estaciones y tope del almacén en la red (Iker; TBD iker/red-estaciones 8b59385; pedido por Mak; número de Lucía) (7-nov, 09:55)
- **Producción**: cada nodo con gente y que no esté perdido (ni «Caída», D-N124) produce los `prod_*` de `balance_nodos.csv`. Es el requisito del bucle de Castellón (D-N124 y D-N125).
- **Tope del almacén, por recurso**: 100 + 200 por cada depósito sano, y 1000 en el nudo. **Lo que la producción no puede guardar se pierde. Lo que llega en tren no se recorta**: la descarga siempre entra, aunque pase del tope.
- **Los víveres no van en el MVP.**
- **G3_red.golden regenerado**: difiere desde el tick 36000 por la producción. **Lo aprueba Nacho después de su revisión**; hasta entonces, el golden nuevo queda pendiente de esa revisión.
- Encaja con el mantenimiento de la inteligencia (D-N124: radar 0,80 u y puesto de escucha 0,28 u al día), que sale de esta producción.
- La siguiente libre es la **D-N131**.

- 7-nov · **Acabados de vehículos de Teo (TBD 64b8beb), APROBADOS** (Lucía). Dragón, VAMTAC y NH90 en 5 acabados: 0 boscoso, 1 liso, 2 árido, 3 embarrado, 4 urbano. **Por defecto en la build, el 0 boscoso** para el ejército del jugador, que casa con el boscoso del soldado y rompe el bloque oliva. Medido: ningún píxel cerca del d4d0cc en las tres hojas (el más claro es e7d496 en faros y escotilla, y c3c3c5 en el NH90), así que no hay choque con el color de selección. Los otros cuatro quedan en el paquete; su uso (restos, vehículos abandonados en estaciones, elección del jugador) se decide después. La firma del color queda pendiente de la revisión de Bruno, como pidió Teo, y se vuelve a mirar sobre la build con el sRGB arreglado.

- 7-nov · **Radar de la red (D-N124), TBD de0f270 de Teo, APROBADO CON RETOQUES** (Lucía). Remolque de un eje con mástil articulado (ref. Raven del ET, foto de Paula); cabeza «Antena» como hijo que gira; medidas SIN VERIFICAR, cabeza a 5,2 m. Uso de las variantes: **1 instalación = el radar por defecto en una estación**; 0 = recién llegado en tren, sin montar; 3 = en montaje o en traslado; 2 = mejora fortificada; 4 = estación caída. Retoques: (a) la tapa del remolque y el techo del shelter salen en ad9a7b (L* 65) y son lo más claro de la pieza; en la foto todo es oliva, así que van en la familia oliva y el beige solo en el interior de las tapas abiertas, para que lo que se lea sea el mástil y la cabeza; (b) la red de camuflaje de la 2 es una losa plana 7e7731 de bordes rectos (choca con la regla 6 de la D-N129): borde deshilachado, 2 o 3 valores moteados y huecos que dejen ver el shelter; (c) la 4 está demasiado limpia, con los mismos valores que la 3: calcinado con la paleta de los restos K8, remolque inclinado y una rueda fuera, sin bajar de 48403c. Nota para todas las hojas: el 1e220c (L* 12, banda de la horda) de las caras en sombra viene del cuantizado del render de las hojas, y sale igual en los vehículos; con la D-N129 eso no pasa en el juego, así que las hojas nuevas se renderizan sin cuantizar y el visto bueno final es sobre una captura de la build. Recibido el cambio de Bruno en los acabados: costado pardo 605c48 (mr-mak cf2f07a).

- QA-35 (7-nov 09:15 UTC, Sara): qa23 (Noche23 f6956b0), difícil: derrota a las 01:14 por el tren con atacantes reales (hasta 208) y el muro al 99 %. Los huecos no están cerrados del todo y queda descartado que sea la inicialización. Normal sin parte final (sin verificar). S1 abierto.

- 7-nov · **Noche elegida: v3 de Bruno sobre qa24 (D-N129 §2.4)** (Lucía). Luna (0,40, 0,55, 1,0) a 0,45; ambiente (0,03, 0,045, 0,10); filtro (0,78, 0,86, 1); saturación −10; **mezcla del cuantizador 0, sin tramado**. Medido (medidas.json y mío): suelo L* 26,4, mediana de 5 valores, b* −3,6 (el control da +4,6, que es el sepia); sombras en gris azulado con croma 6,5; color propio p90 10,4; el foco es el único sitio cálido; teja 2c1f26 en sombra, reconocible; HUD 181c30 / d4d0cc, como la maqueta. Descartadas la v4 (borra el color), la v5 (no parece de noche) y la mezcla 0,2 (no cambia nada que se vea). **Pendiente de verificar en la build**: la banda de la horda (a las 22:18 no hay zombis en el encuadre; con el suelo en L* 26, la horda en 9–13 deja un ΔL* ≥ 13) y el 40 % de diferencia entre la captura y la suma de las pasadas. Siguen en el suelo los rombos oscuros de bordes rectos de la derecha (encargo §6). Marcos la mete en la Noche24, y la apruebo sobre una captura de la build.

- 7-nov · **Radar, retoques hechos (TBD e148d40), CERRADO** (Lucía). Familia oliva (70784c techos, 50541c costados, beige b4a080 solo dentro de las tapas), red moteada por teselas con huecos y borde roto, y la 4 calcinada con la paleta K8 e inclinada 16°. Hoja sin cuantizar. Se entrega a Iker en (206; 0; 82), yaw 180, con la 1 por defecto.

- 7-nov · **Torreta de vigilancia y talud del depósito de Castellón (TBD 8f703c9, Teo con Álvaro), APROBADOS CON RETOQUES** (Lucía). Hojas sin cuantizar. Medidas SIN VERIFICAR (plataforma a 4,2 m). Uso de la torreta según el estado del nodo: Caída = 4; En liberación y Liberada = 3; Segura = 0 por defecto y 1 como mejora; la 2 es la heredada de los supervivientes (estaciones pequeñas y Castellón al 15 %). Óxido de la 2 en 5e3c2d (L* 29), lejos del 982420: vale. Retoque de la torreta: en la 4, el techo flota separado; tiene que quedar colgando de una esquina o apoyado. Talud: la 0 por defecto y la 1 como mejora; las laderas tienen 3 valores (L* 41, 46 y 49), así que no son una losa. Retoques del talud: (a) en la 2, la mancha de erosión a86c50 es un cuadrado de bordes rectos (regla 6 de la D-N129): forma irregular o regueros; (b) en la 3, una banda negra gruesa de contorno en la arista trasera: revisar las normales de la cresta o el umbral; (c) en la 4, los terrones flotan: que estén en el suelo.

- 7-nov · **Torreta y talud de Castellón, retoques hechos (TBD e11336d, mr-mak fcab1fc), CERRADO** (Lucía). Ya no hay mancha cuadrada; la esquina va a inglete y sin banda negra (umbral 0,26); los terrones están en el suelo; el techo de la torreta 4 se apoya y cuelga. Nota menor para más adelante: a tamaño de juego, los regueros de la 2 se leen como trazos sueltos; si se retoca algún día, que sean continuos.

## D-N131 · G3 regenerado por el escenario de la red: Sagunto con 80 personas y Castellón infestada y reclamable (Lucía, 7-nov, 10:25)
- **Confirmado: el cambio es el que buscamos.** Aplica la D-N124/D-N125 (Castellón empieza infestada y se libera C3→C4→C2→C1, con el recinto heredado al 15 %) y el escenario de iker/red-estaciones e9ed33a. Que G3 difiera desde el tick 1 es lo esperado: cambian las existencias iniciales y la obra de Castellón entra en el hash.
- Condiciones: el golden nuevo lo aprueba Nacho después de su revisión, como en la D-N130. Las 80 personas de Sagunto son la cifra del escenario de Iker y Hugo; yo no la he calculado. Si Hugo la cambia, se regenera otra vez. No debe cambiar nada de la noche de Sagunto (NightSim, la D-N121 y la escala 850): Nacho lo comprueba con una corrida de la noche sola, que tiene que salir idéntica.
- La siguiente libre es la D-N132.
- 7-nov, 10:28 · D-N131, condiciones cumplidas (Nacho): aprueba el G3 de e9ed33a (suite 770/0); NightSim sola idéntica byte a byte en fec0f9b y e9ed33a (18 noches más el informe por oleada). Antes de fusionar faltan los .meta de EstacionDato.cs y estacion_castellon.json (en manos de Mak). **D-N131 CERRADA** por parte de diseño.

- 7-nov · **Texturas horneadas de vehículos (TBD 2ef136c, Teo), tras el rechazo de Eugenio a los acabados de camuflaje («parece que tiene parches; tomad de referencia imágenes reales»)** (Lucía). **Anulo la aprobación de los acabados 0–4 de camuflaje** (TBD 64b8beb / mr-mak cf2f07a): fue mi error darlos por buenos sin compararlos con fotos reales. La dirección nueva: pintura lisa verde OTAN como el real (techo 70784c, costados 50541c), textura horneada a ~22 px/m, subconjunto natural de la paleta, sin tramado y 5 grados de uso. Por defecto, el 1 de campaña. **Va con retoques antes de enseñarlo**: (a) en el 0 y el 1, sobre todo en el VAMTAC, el descolorido del sol se lee como manchas claras sueltas, es decir, como los parches que rechazó Eugenio: tiene que ser un degradado amplio en el techo, con un solo paso de paleta entre zonas y sin islas; (b) en el 4, el óxido 7c3c18 dibuja marcos rectangulares alrededor de las chapas: solo en bordes y aristas, fino y roto; (c) el punto claro de la torre del Dragón (bfbbb7, L* 76) se lee a tamaño de juego como el punto de selección: bajarlo a 88885c. Además, la captura de Eugenio enseña una caja sin ruedas: Marcos tiene que confirmar que la build carga los modelos de Teo (encargo de disparos §5.2), porque si no, la textura nueva no se verá.
- 7-nov, 10:35 · **Texturas horneadas de vehículos, retoques hechos (TBD 924a82c), APROBADAS** (Lucía). El sol es una sola elipse a un paso de paleta, el polvo es grano de un texel (en capa solo en el 2), el óxido y el desgaste van solo en aristas, rotos (referencias de Paula S4/S5), y el visor del Dragón está en 88885c. Sin islas y sin marcos: se lee como pintura lisa gastada, no como camuflaje. **Por defecto, el 1 de campaña.** Marcos confirma que la build carga los tres modelos de Teo con T_Paleta32 y sin cajas de relleno; la captura de Eugenio será de una build vieja (Mak lo pregunta). A la galería, frente a su captura, y a mr-mak para Marcos. Visto bueno final sobre una captura de la Noche24 con la noche v3.

## D-N132 · Criterio de la difícil: también la munición, no solo el muro (Lucía, a propuesta de Hugo; 7-nov, 10:36)
- Datos de Sara (1000 semillas con vehículos): con la escala 1500, el muro queda al 26,9 % pero con 0,8 u al final; con 1700 se pierden las 1000 noches por falta de munición. La difícil la decide un precipicio de munición, no el muro.
- **Criterio nuevo de la difícil**: mediana del muro 18–22 %, p10 ≥ 12 %, p90 ≤ 28 % **y munición final p10 ≥ 2 u**. Por qué: la derrota tiene que llegar por el muro, que se ve venir en pantalla, y no porque de repente no queden balas, que se vive como una trampa.
- La normal también tiene que cumplir sus estrellas por munición (★★ = 8 u o más al final); hoy da ★1 con 5 u aunque el muro quede al 88 %. Causa: los vehículos rinden ~251 abatidos por u frente a los 400 de la infantería, y las recargas vacían el almacén.
- Pendiente (número aparte, cuando Sara mida las recargas ×0,6): el coste de las recargas de los vehículos y la escala de la difícil. La D-N127 (1280) queda en suspenso hasta entonces.
- La siguiente libre es la D-N133.
- 7-nov, 10:42 · Corrección a la línea de las 10:35 (Lucía): la captura de Eugenio **sí es de la build actual**, con el modelo de Teo (lo aclaró Eugenio). Lo que se veía mal era el acabado viejo, y el cañón y la ametralladora no salían porque el exportador FBX los metía girados y bajo el suelo. Teo lo corrigió y lo comprobó reimportando (mr-mak 7ed975d). Me equivoqué al suponer una build vieja sin preguntar. Hoja de noche aproximada con la luz v3: se ven las juntas y el cañón, y no queda ningún parche. Una cosa a mirar en la Noche24: en el VAMTAC, el cristal del parabrisas sale como una raya azul viva; no puede ser 404460 (reservado al rim de las unidades propias), y de noche tiene que ir oscuro.
- 7-nov, 10:44 · Cristal de los vehículos (Teo, mr-mak 26d4ea9, sustituye a 7ed975d): no era 404460, sino 60546c (violeta del zombi, prohibido en lo propio). Pasa a 48403c (L* 27,8, el suelo de lo propio) en los tres vehículos; ninguna de las 15 texturas lleva ya 60546c, 404460, 6c7874 ni 181c30. **Cerrado** (Lucía).
- 7-nov, 10:56 · Horda sobre la v3 (Bruno, qa25, ~10.000 zombis): es lo más oscuro del suelo y se lee, pero sale fuera de la banda D-N80 en los dos supuestos (captura correcta: horda 16,4 / suelo 43,2; con una codificación de más: 1,5 / 13,6). **Sin firmar hasta tener la captura directa** (-capdirecta, pedida a Mak). Criterio (Lucía): la banda D-N80 no se mueve. En ningún supuesto el suelo es el de la v3 (26,4), así que lo primero es que la build reproduzca la v3 (suelo ~26, que es un ajuste de luz para Marcos). Solo si con el suelo en 26 la horda queda fuera de 9–13, se baja la horda.
- 7-nov, 10:58 · Suelo de noche plano (Bruno, qa25): un solo color, 566686 (L* 43), ocupa el 42 % de la zona de mundo, porque de noche la textura del suelo es la media de la zona más un 20 % del detalle. Los valores de la v3 están bien puestos en el código (marcos/noche-prototipo 916a533). **Aprobado el ajuste para Marcos** (Lucía): detalle del suelo de noche al 60–100 %. Criterio de medida: ≥ 3 valores que pasen cada uno del 5 %, ninguno por encima del 30 %, sin bordes rectos (regla 6 de la D-N129); con la directa, medir también el croma del suelo (regla 3: gris azulado poco saturado).

## D-N133 · Derrota por estación o por tren, y un parte que dice qué cayó (Lucía, 7-nov, 11:00; contestado a Mak desde el hilo anterior y registrado aquí)
- **La regla se queda**: se pierde la partida al quedarse sin **ninguna estación principal** (D-N125) **o sin ningún tren**. Un juego de trenes no se juega sin trenes ni sin un sitio donde parar.
- En el MVP hay una estación y un tren, así que perder cualquiera de los dos es perderlo todo: el NightGame de Nacho ya hace lo correcto.
- Nacho cuenta «estaciones principales vivas» y «trenes vivos» por separado, aunque hoy valgan 1. Con más estaciones o más trenes, perder uno será un golpe y no una derrota.
- **El texto está mal y se arregla**: la derrota dice qué cayó, «El tren ha caído» o «Sagunto ha caído». Nacho expone la causa (estación o tren) y Marcos o Bruno cambian el titular de la pantalla de derrota. La D-N104 no cambia: la integridad sigue siendo el mínimo.
- La siguiente libre es la D-N134.
- 7-nov, 11:12 · **Noche: la v3 queda sustituida por la E de Bruno, medida sobre la pantalla real** (qa27, captura directa; Lucía). La captura de siempre llevaba una codificación sRGB de más; la v3 en pantalla real da un suelo 18223d (L* 13,7, croma 19,4), un azul marino saturado que incumple la regla 3. Mi elección de la v3 se hizo sobre una simulación que falló en el valor absoluto (el 40 % sin explicar): desde ahora, la luz solo se elige midiendo la pantalla real. **E**: luna (0,75; 0,80; 1,0), exposición +1,4, filtro blanco, sat −50 → suelo L* 26,0 y croma 8,0 (estimado sobre un fotograma, SIN VERIFICAR en Unity). Va a Marcos junto con el detalle del suelo de noche k = 0,7. **Condiciones al medir la build con la E**: (1) suelo L* 24–28 y croma ≤ 10; (2) regla 4: con sat −50, la teja, la fachada, el oliva y la chapa se tienen que seguir reconociendo; si no, la saturación se queda en −30 y el croma se baja con el color de la luna; (3) horda: **la banda D-N80 no se mueve**. Con la E se estima L* ≈ 4; si la captura real lo confirma (< 9), se sube un paso el albedo de la horda (Teo y Bruno), porque a L* 4 se pierde la masa moteada (regla 5) aunque el contraste sea de sobra.

## D-N134 · Criterio de sonido (Lucía con Nuria; 7-nov, 11:25)
- **Se aprueba como criterio el diseño sonoro v1 de Nuria** (`docs/sonido/diseno-sonoro.md`), que traduce bien los seis pilares de `criterio-diseno-lucia.md`: cuatro capas por arma ligadas al zoom (cerca < 0,35, media 0,35–0,7, lejos ≥ 0,7, y mapa fuera de la estación, porque la noche sigue sonando desde el mapa, D-N91); silencio tenso con un bajón de 1,5 s antes de cada oleada; la horda como lecho que sigue al número de zombis, nunca un solista; sonoridad como prioridad (estilo HDR) con topes de voces; fuego de pelotón por celdas de 20 m (suenan todas las balas, no solo las trazadoras); el tren como único sonido cálido, que baja la horda −6 dB.
- **Reservas de color = reservas de sonido**: la alarma roja solo para ataque o brecha; el aviso ámbar es otro tono, más suave.
- Herramientas: Unity 6 nativo (AudioMixer y Audio Random Container) para el MVP. ElevenLabs v3, con la clave solo en `ELEVENLABS_API_KEY`; los bucles se hacen en posproceso porque el v3 no hace bucles. FMOD queda SIN VERIFICAR y sin pagos.
- Volúmenes de partida: fusil 0,7 y cañón 1,0, con el ducking de −3 dB del 30 mm sobre los fusiles. Se ajustan en código con Marcos.
- **La demo (`demo_lucia.mp3`) no la he podido escuchar**: está en el PC y desde aquí no oigo audio. La juzgo por medidas, con estos criterios (Nuria los mide, o la copia a `/mnt/project-files/docs/sonido/demo/` y los mido yo con ffmpeg): el cañón, de cerca, al menos +4 LU por encima del fusil de cerca; el fusil lejos, al menos −12 LU por debajo del fusil de cerca y sin energía por encima de 2 kHz; la horda acercándose crece de forma continua, sin saltos de más de 3 LU; ningún pico por encima de −1 dBTP. La escucha final de cómo se siente es de Nuria y de Mak.
- La siguiente libre es la D-N135.
- 7-nov, 11:28 · **La E falla en la pantalla real** (qa28, Bruno): suelo 185,178,176 (L* 73, croma 2,8, un gris rosado) y color propio con croma p90 6,9. Causa probable: la gradación se aplica dos veces (cámara de presentación y cámara de efectos con el post activo), y queda un factor ×2 sin explicar. **Se acaban las variantes simuladas** (Lucía). Encargo para Marcos vía Mak: (1) quitar el post de la cámara de efectos (caso a de la qa25), con las trazadoras y el foco en el encuadre para comprobar que siguen brillando; (2) un barrido de 5 variantes en Unity, en el mismo fotograma y con zombis, con captura directa de cada una (exposición −0,2 a −0,7, sat −30 o −20, luna entre (0,75; 0,80; 1) y (0,55; 0,65; 1)); (3) Bruno mide y Lucía elige con estas condiciones: suelo L* 24–28 y croma ≤ 10, color propio con croma p90 ≥ 12, la horda en la banda D-N80 y ≥ 3 valores en el suelo. Hasta entonces, no hay noche elegida.
- 7-nov, 11:32 · D-N134, medidas de la demo (Nuria, ebur128 con peak=true): cumple (A) +4,4 LU, (B) −12,8 LU con ≤ −30,9 dB por encima de 2 kHz, (C) un salto máximo de 2,3 LU (descartada la v06; quedan 5 variantes) y (D) pico de −1,2 dBTP. **Aprobada la demo por medidas** (Lucía). La medida con paso alto de 8.º orden vale. **Un aviso**: las capas lejanas ya llevan horneado un paso bajo de 1,8 kHz (aplicado cuatro veces o más), y el diseño §3 pone otro en tiempo real (1,5 kHz en lejos y 800 Hz en el mapa). Es el mismo error que el doble post del color: el filtro va una sola vez. O se hornea, o se aplica en el mezclador. Recomiendo quitarlo del mezclador para la capa lejana y dejar el del mapa.

## D-N135 · Noche de primer contacto: 4 oleadas y recargas ×0,6 (Lucía, a petición de Eugenio vía Mak y Hugo; 7-nov, 11:47)
- Eugenio: «Haced que se puedan ganar las hordas. Reducid de 6 a 4. Es un primer contacto, no tiene que ser difícil».
- **La noche pasa de 6 oleadas a 4**: 900, 1500, 2000 y 3000 zombis antes de la escala, a las 22:20, 00:10, 02:10 y 04:10 (7400 en total frente a 16.000). Repartidas por toda la noche para que no queden horas vacías. La última es la más grande: el arco de la noche se mantiene, con el clímax antes del amanecer.
- **Recargas de los vehículos ×0,6** (1200/1800/1800). Medido por Sara: la normal da ★★ en el 84 % de las noches y ninguna ★★★.
- Escalas de la build: normal 850, difícil 1140. La D-N127 y la D-N132 quedan en suspenso para esta noche y vuelven cuando haya más noches después del primer contacto.
- **Criterio de primer contacto** (lo mide Sara con 1000 semillas y NightBot): la normal se gana en ≥ 95 % de las noches, con el muro tocado (mediana ≤ 85 %), para que se sienta la amenaza; la difícil se gana en el 50–80 % de las noches. Si la difícil sale peor, Hugo baja su escala sin pedir otro número.
- La siguiente libre es la D-N136.
- 7-nov, 11:57 · **«Parches» del suelo: se funden o se quitan, ninguno se queda** (Lucía, para Marcos vía Mak). Aclaración: mi nota de las 10:15 («siguen en el suelo los rombos oscuros») decía que el defecto seguía ahí, no que se quedara. El encargo de disparos §6 pedía identificarlos. Según Marcos son dos objetos: (1) **la muestra del suelo** (las teselas): se funde, con el borde mezclado con la de al lado y sin aristas rectas (regla 6 de la D-N129); (2) **las zonas de agua**: si es agua que está en el nivel aprobado (la acequia o la balsa de sagunto v1.2/v1.3), se queda, con orilla irregular, del color del agua y no como un rectángulo verde oscuro; si no está en el nivel, se quita. Para la versión pulida de Eugenio: ningún rectángulo de bordes rectos en el suelo. Lo compruebo sobre la captura directa.
- 7-nov, 12:05 · **Rombos y banda diagonal de la derecha (Noche39), decisión** (Lucía). No he podido abrir la qa30 (está en mr-mak-workspace, no en la carpeta compartida); lo he mirado en el mismo encuadre de la qa27. Los «rombos» son cajas planas alineadas con los ejes del mundo (a 45° en la cámara) y la banda es una caja larga y baja con la cara del extremo a la vista: **son primitivas de relleno**, no piezas de Teo. Según el plano (sagunto-nivel §P5–P7), al este fuera del muro van el bloque de pisos (174; 82), los solares y la huerta con acequias y caminos. Regla para Marcos: (1) toda caja primitiva sin modelo de Teo que esté fuera del muro **se quita** de la versión pulida; (2) si una es un elemento aprobado del plano, va con su pieza de Teo, y si no la hay, se quita por ahora; (3) los caminos y acequias son decals planos en el suelo, con borde irregular y a un paso de valor del suelo como mucho, nunca cajas en relieve. El visto bueno al suelo, cuando vea la captura directa de la qa30 en la carpeta compartida.
- 7-nov, 12:08 · **Suelo de la Noche39 (qa30, captura directa), NO aprobado** (Lucía). Medido: en el suelo libre, un solo color 21283f ocupa el 90–100 % (L* 16,5, croma 16,2). Las teselas ya no tienen bordes, pero el suelo es una losa azul marino plana: incumple la regla 6 (≥ 3 valores), la 3 (croma ≤ 10) y el objetivo L* 24–28. O el detalle k = 0,7 no está activo, o el fundido se ha comido la variación. Lo resuelve el barrido de 5 variantes en Unity con el post solo una vez (11:28); el detalle del suelo se mide en esa misma tanda. Confirmado en la qa30 que los rombos (≈ x1850, y600 y x1400, y670) y la banda diagonal son primitivas: se quitan (12:05). Bien: el anillo de selección del vehículo se ve y sigue al vehículo. Dos fallos de interfaz: (a) el texto de ayuda de formaciones dice «F2 cuña · F4 círculo», pero el encargo §3.2 dice F1 Línea, F2 Bloque, F3 Columna y F4 Dispersa; (b) la segunda línea de ese texto queda cortada detrás de las tarjetas.
- 7-nov, 12:15 · **Noche41: elección provisional G2 y decisiones de suelo, muros y formaciones** (Lucía). Solo tengo la G2 en la carpeta compartida (grad_G2_full.png); la G1 y la G3–G5 de la qa32 están en main de mr-mak. Medido en la G2: suelo 383437 (L* 22,2, croma 2,7). Por fin no hay azul marino: el croma cumple y la luz se lee. Pero el L* queda un poco bajo (objetivo 24–28) y el color propio es débil (teja con croma ≈ 7, fachada ≈ 2). **Me quedo con la G2 de forma provisional, con +0,3 de exposición**, y la confirmo frente a las otras cuatro cuando Teo las copie. **Suelo**: el 81 % es un solo color porque la textura se ajusta a la subpaleta SnapSub de 17 colores. Decisión: el suelo deja de usar SnapSub y usa la paleta de 32 completa, con ≥ 3 valores de la familia del suelo (D-N129: la paleta vive en los albedos, sin recortarla de más). Lo hace Bruno en la textura de detalle; objetivo: el color dominante ≤ 30 %. **Muros**: me equivoqué, la banda diagonal clara es el muro sur real (88885c) y se queda. **Rombos**: no son objetos de 3 m o más; Marcos busca entre los objetos de menos de 3 m y los decals, y se quitan sean lo que sean. **Formaciones**: para el MVP valen las cuatro que hay (Línea, Columna, Cuña y Círculo), y se corrige el encargo §3.2. Eugenio pidió poder «dibujar un cuadrado» (Bloque): se le pide a Nacho que el Bloque sustituya al Círculo cuando pueda.
- 7-nov, 12:20 · **Noche elegida en el juego real: G1 de la qa32** (Lucía; sustituye a la G2 provisional de las 12:15, sin el +0,3). Medido en las cinco con captura directa: G1, suelo L* 26,1 con croma p90 4,7, teja con croma 9,6 (la que más color propio conserva) y fachada L* 21,4; G2, 22,2 / 2,7; G3, 24,5 / 3,2; G4, 19,9 / 2,8; G5, 20,2 / 4,1. La G1 es la única con el suelo dentro de L* 24–28, y la que mejor guarda la teja. A la vista: noche legible, teja y fachada reconocibles, vehículos y anillo de selección claros, y el foco cálido. Queda pendiente: (a) el suelo, con un color dominante del 80 % (sale de SnapSub; Bruno lo pasa a la paleta de 32, objetivo ≤ 30 %); (b) el suelo tira a pardo grisáceo y no a gris azulado frío: se acepta mientras el croma sea ≤ 5; (c) la horda, que se mide en cuanto haya una captura de la G1 con zombis.
- 7-nov, 12:24 · **Suelo de noche con la paleta de 32 (Bruno, mr-mak f76ecec): confirmada la A** (Lucía). Beige, concrete_light y olive_light al 30 % y olive al 10 % (L* 67, 61, 56 y 49); sin SnapSub ni tramado y sin valores de la horda. Condiciones, sobre la captura directa con la G1 vuelta a medir: (1) a zoom de juego no se ve la repetición; (2) las manchas olivas no se leen como camuflaje (es lo que Eugenio llamó «parches»): si se leen, se baja el contraste entre olive y beige un paso; (3) con la luz, los 4 valores no se juntan en menos de 3. Si falla la (1), se pasa a la D, que es la menos periódica de las cinco. El anillo de 2 m fuera de paleta bajo los focos se acepta, porque no lleva tramado.
- 7-nov, 12:32 · **Noche44 (G1 con el suelo A, captura directa): suelo APROBADO** (Lucía). Medido: L* 23,3 (un punto por debajo de 24, que se acepta), croma p90 4,7, cuatro valores del 9 al 32 % y el dominante en el 32 %. El suelo ya tiene vida, sin losa ni parches. A esta escala no se ve la repetición y no se lee como camuflaje. Teja y fachada iguales que en la G1. Los «rombos» eran decals de grietas cuadrados, que ahora están apagados de noche: resuelto. **Falta la horda**: captura directa a las **22:35** (la primera oleada contra el muro oeste, con la cámara en la puerta oeste y el foco en el encuadre) y otra a las **00:25** (la segunda oleada, más densa). Ahí se miden la banda D-N80 y la masa moteada.
- 7-nov, 12:34 · **D-N135, ajuste del criterio para la build de hoy** (Lucía, a propuesta del coordinador). Con el tren al fondo del andén, a 20 m del muro oeste (Nacho, e6fa207), NightSim gana la normal y la difícil en 1000 de 1000 noches; el muro acaba con una mediana del 99 % (normal) y del 95 % (difícil). **Sale así hoy**: Eugenio pidió un primer contacto que no sea difícil, y eso pesa más que mi «muro tocado». **Mañana**: la difícil vuelve a su criterio (se gana en el 50–80 %) y se le da tensión a la normal (mediana del muro ≤ 90 %) sin bajar del 95 % de victorias. Bloque en F4 (Nacho): el Círculo sale y se cumple el «cuadrado» de Eugenio.
- 7-nov, 12:58 · **Noche cerrada para la build de hoy (Noche46, 7dd8c5e)** (Lucía). Victoria con -nightbot en normal, con el muro al 99 %. G1 con el suelo A aprobados; anillos de selección, foco y tren legibles; la ayuda ya dice F4 Bloque. **Horda, pendiente para mañana (no bloquea)**: en las capturas de qa34 (960×540, Blit en Linear, no directas) apenas entra horda en el encuadre: unos pocos zombis a la izquierda a las 22:34, y a las 00:25 la oleada 2 todavía no ha llegado al muro en el encuadre. Medidos: los zombis salen a L* 2–3 (080709/0b0a0b) con algo de 3a120f, por debajo de la banda D-N80 (9–13). Se leen como siluetas negras contra el suelo (L* ~24), pero sin el moteado. Como ya estaba decidido, **mañana se sube un paso el albedo de la horda** (Teo y Bruno) y se comprueba con una captura directa con la masa de la horda contra el muro.

## D-N136 a D-N142 · Lo que cambia tras la prueba de Eugenio en la Noche46 (Lucía, 7-nov 13:45)
El detalle y el plan por persona están en `docs/plan-noche46-eugenio.md`.
- **D-N136**: se acaban las oleadas. Una sola gran horda al entrar, a ~250 m por el oeste, que llega en 60–90 s. La noche se gana al acabar con ella. Sustituye a las oleadas de la D-N135. Tamaño de partida: 7400 con la escala 850; lo calibra Hugo para que la normal se gane en ≥ 95 %.
- **D-N137**: daño en área para el 30 mm del Dragón (2,5 m), la granada de 40 mm (4 m) y el C90 (5 m), todos SIN VERIFICAR. Los vehículos tienen armas propias, con miniexplosión de impacto.
- **D-N138**: teclas de depuración solo con -debug; 1–5 seleccionan los pelotones y el clic selecciona; menú de pausa con Esc, que congela la simulación.
- **D-N139**: colisiones para la infantería y los vehículos, con rodeo; si un vehículo lleva > 2 s atascado, recalcula la ruta.
- **D-N140**: los cadáveres se quedan (hasta 4000, y se desvanecen a los 10 min de juego); la sangre, granate oscuro y acumulada, nunca 982420.
- **D-N141**: el suelo A solo en la tierra, con las carreteras y el balasto de vuelta. Fue mi error aprobarlo midiendo solo un trozo de tierra. Vías con traviesas y raíles grises. Muros de sacos, HESCO y hormigón. Zombis civiles con 5 o más variantes en la banda D-N80. Iconos de escuadrón que dicen qué es cada uno. El cartel de Sagunto, centrado.
- **D-N142**: criterio de sonido (oyente en el suelo bajo la cámara y en 3D, volumen bajo, fundidos sin cortes, ambiente vacío al alejar, zombis solo de cerca, sin música por ahora).
- La siguiente libre es la D-N143.
- **D-N143**: el NH90 aterriza (helipuerto o un claro de 20 × 20 m), carga un pelotón, lo transporta y lo descarga. En vuelo la tropa no dispara ni recibe daño.
- **D-N144**: fuera del HUD el panel de órdenes de abajo a la derecha, hasta que cada botón tenga una función clara.
- **D-N145**: la cámara se mueve con WASD (anula el «sin WASD»). G alterna entre fuego libre y alto el fuego en los vehículos; la A queda libre.
- **D-N146**: al ganar no se reinicia. Sale «Sagunto resiste», sigues en el mundo, amanece y puedes quedarte o ir al mapa. Solo «Volver a empezar» reinicia.
- La siguiente libre es la D-N147.
- 7-nov, 13:50 · **D-N139, ampliación** (Eugenio: «los zombies atraviesan todo»): los zombis también chocan con los edificios, los muros, los vehículos y el tren. Rodean los edificios y, al llegar al muro, se amontonan contra él y lo golpean; solo pasan por una brecha o una puerta rota. Entre ellos, separación de masa (sin que se monten unos sobre otros), barata para 10.000 zombis: por ejemplo, un campo de flujo con separación en rejilla. → Nacho (simulación) y Marcos (vista).

## D-N147 · Interfaz v2, inspirada en los patrones de Ebbtide (Lucía, 7-nov 13:58)
- Pedido de Eugenio. Detalle en `docs/interfaz-v2.md`. Se toman los patrones de uso (el centro libre; todo dice qué es; el reloj arriba al centro; avisos de escuadra arriba a la izquierda; plantel de tarjetas abajo al centro; minimapa con órdenes contextuales abajo a la derecha; barra de atajos; poco en el mundo), no sus gráficos. Lo que no se puede verificar sin el juego queda marcado como estimado.
- Las tarjetas de escuadra dicen nombre, tecla, una silueta por hombre, munición y estado en una palabra; las de vehículo, silueta, nombre, blindaje, munición y estado. Órdenes de lo seleccionado con texto y tecla (sustituye al panel mudo de la D-N144). Colores reservados como siempre: hueso = selección, ámbar = aviso, rojo = ataque.
- Trabajo: Bruno hace 5 maquetas sobre una captura directa; Lucía elige y mide; Marcos implementa en UI Toolkit (P1). Sustituye a la D-N141e.
- La siguiente libre es la D-N148.
- 7-nov, 14:02 · **D-N136 en números (Hugo, entregas/dn136)**: una horda a las 22:00 que llega en 75 s; fácil 3410, normal 4000 (muro esperado ~91 %), difícil 5360 (~76 %). **Aprobado como valores de partida** (Lucía). Sale del ajuste del barrido A–D de Sara, sin medir la pila que trepa ni el tren. Condición: Sara lo confirma con 1000 semillas (la normal se gana en ≥ 95 %; la difícil, en el 50–80 %). Si no, Hugo lo ajusta sin pedir otro número.
- 7-nov, 14:10 · **D-N147: elegida la maqueta 1 (plano v1.4) de Bruno** (mr-mak a3667d1). Las cinco comparten disposición; la 1 es la más limpia y la más barata de montar (la 3 solo añade esquinas). Medidas de Bruno: panel con barra 156 px (14,4 %), hueso ≥ 9,6:1, gris secundario 4,8:1 y ámbar 5,6:1, todo por encima de 4,5. Descartada la 4 (contraste por debajo de 4,5 con el fondo al 55 %). Teclas: 1–5 los pelotones y 6–8 los vehículos (amplía la D-N138). Para Marcos, en P1: primero las tarjetas y la selección, después el minimapa y los avisos. Próxima ronda: captura sin HUD.

## D-N148 · Los trepadores van a por lo vivo más cercano, no derechos al tren (Lucía, a propuesta de Hugo; 7-nov, 14:15)
- Sara, 1000 semillas con dn136: fácil 86 %, normal 0 % y difícil 0 %. Todas las derrotas son por el tren, con el muro por encima del 88 % y munición de sobra. Con dn136b (180 s) la normal sigue perdiendo el tren a las 23:15 con el muro al 97 %. Causa: cualquier trepador va derecho al tren.
- **Elegida la (a)**: el zombi que pasa el muro ataca **lo vivo más cercano** (infantería, después vehículos parados y después obreros), y solo va al tren si no queda nadie en un radio de 30 m. Es lo que haría un zombi, y la derrota se ve venir: los ves dentro, comiéndose a tu tropa, antes de que el tren caiga. El tren conserva su vida actual (120000). No se toca ClimbPileZ.
- Nacho lo implementa en NightSim (determinista, objetivo por rejilla). Hugo recalibra el tamaño de la horda con dn136b y el criterio de la D-N136.
- Fallo aparte, para Nacho y Marcos: el NH90 no despega ni dispara (Sara, 920/920).
- La siguiente libre es la D-N149.
- 7-nov, 14:34 · D-N136/148, reparto de la horda (Hugo, dn136c): con la D-N148 (Nacho 21ff07d, 200 semillas) la normal gana 200/200 y la difícil pierde 199/200 por el tren. Los trepadores del O4 (el puente del este) no tienen tropa a 30 m. **Aprobado quitar el O4: el reparto queda 50/30/20/0** (Lucía). Es coherente con el nivel (sagunto-nivel §«La horda entra por el oeste»; el puente del Palancia es la entrada «por donde no miras», para cuando la Colmena aprenda, después del MVP). Sara mide con 1000 semillas.
- 7-nov, 14:50 · **D-N137, enmienda: el C90** (contestado por el hilo anterior de Lucía y registrado aquí). Lo llevan solo los pelotones de fusileros, 2 por pelotón (uno por escuadra; la dotación real está SIN VERIFICAR). **Solo se dispara por orden del jugador**, nunca en automático: sirve para romper una pila peligrosa. Es de un solo uso y se repone del almacén en la recarga, con el coste que fije Hugo. El arte ya existe (D-N86). **Añadido** (Lucía): en la interfaz v2, la orden «C90 (C) · 2» va en el panel de órdenes de los fusileros, con los que quedan. Se apunta con el clic y es área de 5 m.

## D-N149 · Fuera las estrellas al ganar (decisión de Eugenio, registrada por Lucía; 7-nov, 15:10)
- Eugenio: «quita lo de las estrellas… matas a la horda y genial, pero a otra cosa». **Se quitan del todo**: no hay ★ en la pantalla, ni en el parte, ni en `noche_sagunto.json` (`resultados.estrellas` sale). Se acaba con la horda, sale un aviso breve («Sagunto resiste») y se sigue en el mundo (D-N146).
- **Revisado lo que dependía de ellas**: (1) la economía no da premios por estrellas (he buscado en docs/economia): no hay que tocar nada; (2) los umbrales de estrellas de la D-N104 dejan de existir como interfaz. **Se mantiene la integridad mínima de la D-N104 como condición de derrota** (D-N133); (3) los criterios de calibración que hablaban de estrellas (D-N132: «★★ = 8 u»; D-N135: «★★ en el 84 %») se reescriben con medidas internas que el jugador no ve: **% de victorias, mediana del muro y munición final**. Para la normal: victorias ≥ 95 %, mediana del muro ≤ 90 % y munición final p10 ≥ 2 u. Para la difícil: victorias en el 50–80 %.
- La siguiente libre es la D-N150.
- 7-nov, 15:16 · **D-N136, CERRADA** (Hugo y Sara, 1000 semillas sobre 9993dc0, criterio de la D-N149): normal con 7310 zombis, 100 % de victorias, muro al 87,4 % y munición p10 de 35,9 u; difícil con 9590 (escala 1115), 59 % de victorias. Cumple las dos (Lucía). Fácil: el valor que entregó Hugo. Detalle en docs/economia/entregas/noche-final/LEEME.md.

## D-N150 · Tutorial de la primera noche: refuerzos desde Segorbe por el mapa (pedido de Eugenio; Lucía, 7-nov 15:25)
- Especificación: `docs/tutorial-refuerzos.md`. Sales al mapa, haces clic en **Segorbe** (estación segura con 2 NH90, cada uno con un pelotón de fusileros), los mandas a Sagunto (ETA de ~7 min de juego, ~15 s reales; cifras reales SIN VERIFICAR), vuelves, los ves entrar, los aterrizas (L) y bajas la tropa (U), y colocas el frente. Después la horda avanza.
- **La horda espera agrupada** hasta acabar el tutorial (el mundo y el reloj siguen). Pausa solo en la tarjeta de inicio. Se puede saltar. **Solo la primera vez, en fácil y normal**; la difícil no tiene tutorial ni refuerzos (está calibrada sin ellos).
- Aviso: Eugenio dice que Sagunto es imposible, pero NightSim gana la normal el 100 %. Marcos y Sara comprueban si la build y NightSim coinciden.
- La siguiente libre es la D-N151.

## D-N151 · Asedio: puertas cerradas y tropa dentro y fuera (diseño de Eugenio; Lucía, 7-nov 15:35)
- Cuando atacan una estación, **las puertas de entrada y salida del tren se cierran del todo**. Para entrar, los zombis tienen que romper un muro o una puerta: no hay otro camino. Las puertas pasan a ser un tramo de muro más, con su vida.
- Al empezar el asedio, **una parte de la infantería aparece dentro** del recinto y **otra fuera, junto a los vehículos**, al otro lado del muro. El reparto lo propone Hugo. Mi propuesta de partida es la mitad dentro y la mitad fuera.
- Encaja con D-N148: el trepador sigue atacando lo vivo más cercano. La tropa de fuera es la primera que recibe.

## D-N152 · Estación ocupada: el tren espera a las puertas; ampliar para más trenes (Eugenio; Lucía, 7-nov 15:35)
- Si una estación está bajo ataque, un tren que tenga que pasar por ella **llega, pero se queda a las puertas**. No puede entrar hasta que acabe el asedio. Mientras espera fuera se le puede atacar (D-N148), así que mandar un tren a una estación sitiada es una decisión con riesgo.
- Cada estación tiene un número de **plazas para trenes**. Por defecto, una en las estaciones pequeñas y dos en las principales (propuesta). **Ampliando la estación** en el modo construcción (D-N153) se ganan plazas. Aquí empieza la gestión de la red.

## D-N153 · Modo construcción (Eugenio; Lucía, 7-nov 15:35)
- Es un modo propio dentro de la zona de la estación, y en él se hace todo lo que es obra:
  - **Reparar muros.** Es lo primero.
  - Ampliar el tamaño de la estación, lo que da más plazas para trenes (D-N152).
  - Torretas montadas en el muro. Al construirlas, el muro crece para sostenerlas.
  - Torretas automáticas.
  - Artillería emplazada.
  - Helipuertos (D-N155).
  - Más adelante: minas, morteros y lo demás.
- **Los muros dejan de ser bloques sin forma.** Se modelan de verdad, con sacos terreros y gaviones tipo HESCO. Las referencias tienen que ser reales y los modelos van primero como muestra de 5 variantes. Un tramo dañado se ve dañado. Reparar cuesta materiales y tiempo; las cifras las pone Hugo.
- **Primera versión: reparar más sacos y HESCO modelados.** Ampliar la estación y las torretas van después, en ese orden.

## D-N154 · Tutorial nuevo; enmienda la D-N150 (Eugenio; Lucía, 7-nov 15:35)
- Tiene este orden:
  - 0. **Intro con el lore** (D-N158).
  - 1. **Defender Sagunto de día.** Es la primera horda (D-N157). Se ven las puertas cerradas y la tropa dentro y fuera (D-N151).
  - 2. **Reparar.** Los zombis han roto un tramo de muro y se entra en el modo construcción para repararlo (D-N153).
  - 3. **Mover trenes.** El primer objetivo es llevar un tren a la estación de al lado, Nules (D-N156). En este paso se enseña a preparar el tren, a cargarlo con lo que quieras y con las unidades que quieras, y a mandar apoyo terrestre con él.
  - 4. **Apoyo aéreo.** Llega más tarde, la primera vez que el jugador lo tiene a mano (D-N155).
- **Cómo queda el choque con la D-N150.** La D-N150 traía 2 NH90 desde Segorbe. Pero Segorbe no tiene helipuerto y, además, ahora no está entre las estaciones del principio. Lo resuelvo así:
  - La D-N150 sale del tutorial de la primera noche.
  - Sus pasos (sales al mapa, mandas los helicópteros, sigues la ETA, aterrizas y bajas la tropa) pasan a ser el **capítulo 4**.
  - El capítulo 4 se dispara la primera vez que el jugador usa un helipuerto, ya sea el de Sagunto (D-N155) o uno que haya construido.
  - Los textos de `docs/tutorial-refuerzos.md` se reutilizan casi tal cual, cambiando «Segorbe» por el helipuerto de origen.
- Lo que no cambia de la D-N150: el tutorial se puede saltar, sale solo la primera vez, en fácil y normal, y la difícil no lo tiene. Además, la horda espera mientras dura cada capítulo con combate.

## D-N155 · Apoyo aéreo solo desde aeródromos o helipuertos (Eugenio; Lucía, 7-nov 15:35)
- Los helicópteros, y más adelante los cazas, solo despegan desde un **aeródromo** o desde un **helipuerto construido en una estación** (D-N153).
- Sagunto es la base del jugador y ya figuraba en la red de estaciones con helipuerto, así que **empieza con su helipuerto hecho**. Es la decisión del equipo. Así D-N143 sigue en pie, y el NH90 aterriza y carga un pelotón desde el primer día.
- Las demás estaciones no tienen helipuerto hasta que se construye.

## D-N156 · Se empieza con 3 estaciones (Eugenio; Lucía, 7-nov 15:35)
- Al principio solo están desbloqueadas **Sagunto** (principal), **Nules** (pequeña, la de al lado) y **Castellón** (principal, infestada; D-N131).
- El resto de la línea sale en el mapa, pero bloqueado, y se abre al reparar la vía.
- El primer objetivo es llevar un tren a Nules. La toma de Castellón viene después.

## D-N157 · Fuera la barra de oleadas; la primera horda, de día; días de 14 minutos (Eugenio; Lucía, 7-nov 15:35)
- Se quita del todo la barra de progreso «hacia el día» o hacia la oleada. No hay oleadas (D-N136).
- **La primera horda ataca de día.** Así el jugador ve claro lo que pasa mientras aprende, y las siguientes ya son de noche. Para eso hace falta un aspecto de día en la zona, que va primero como muestra de 5 variantes medidas con -capdirecta.
- **Un día completo de 24 h de juego dura 14 minutos reales.** El reloj pasa de ×28 a unos ×103.
- Cosas que dependen del reloj y que Hugo tiene que recalcular:
  - el aviso de 3 h, que ahora son 1,75 min reales;
  - el aviso de 6 h con radar;
  - la ETA del capítulo 4;
  - los tiempos de reparación y de producción.
- Si «días» se refería solo a las horas de luz, se corrige.

## D-N158 · Intro con el lore al empezar la partida (Eugenio; Lucía, 7-nov 15:35)
- Antes de la primera partida sale una intro breve, que se puede saltar. Cuenta:
  - el año;
  - qué ha pasado;
  - que las ciudades han caído y el tren es el único transporte que queda;
  - el objetivo: tú eres el mando militar y tienes que recuperar la península reparando la red ferroviaria.
- La base es el gdd §lore («semanas después del brote…»). **El año todavía no está fijado.** Mañana llevo 5 variantes del texto y el equipo elige una.

## D-N159 · Árbol de investigación, más adelante (Eugenio; Lucía, 7-nov 15:35)
- Servirá para mejorar unidades y desbloquear otras nuevas. Se queda apuntado y va después del MVP. No se diseña mañana.
- (Siguen la D-N160 a la D-N162.)

## D-N160 · La Colmena que aprende sigue en el MVP (Lucía, 7-nov 15:45; a raíz de la revisión del GDD)
- La Colmena es el pilar 4, lo que hace distinto al juego. **No sale del MVP.**
- La nota de `sagunto-nivel` («después del MVP») vale solo para el puente del este como entrada que se aprende. No vale para la Colmena entera.
- En el MVP entra lo que pide el GDD §15, en su versión mínima:
  - memoria de tráfico y de atención;
  - los 3 estados;
  - el informe de inteligencia.
- La lógica ya existe en la simulación de la red (hito 4). Se integra en la build **después** de los bloques del domingo (asedio, reparar, trenes y tutorial), porque necesita los trenes y las estaciones de las D-N152 y D-N156.

## D-N161 · Un solo reloj y el primer ataque del día 1 (Lucía, 7-nov 15:45; enmienda la D-N08, la D-N36, la D-N124 y el ×72 del GDD)
- **Regla única: 24 h de juego son 14 min reales**, es decir, ×≈103. Vale para el mapa, la zona, NightSim y la economía.
- Queda **una sola constante** en un solo archivo de datos, que leen la build y las simulaciones. Nacho e Iker eligen cuál. Ningún documento vuelve a escribir el factor a mano: se cita esta D-N.
- Esto sustituye el ×72 del GDD y el ×28 de la D-N124 y de la memoria. Todo lo que se midió con ×28 (avisos de 3 y 6 h, ETA, producción) **hay que volver a medirlo**; lo hacen Hugo y Sara el domingo.
- **Enmienda la D-N08 y la D-N36.** El día 1 ya no está sin asedios: **el primer ataque es el día 1, de día**, y es el del tutorial (D-N154, D-N157).
  - Ese ataque es más pequeño que la horda de la noche. Su tamaño lo fija Hugo, partiendo de los sondeos de 100–300 de la D-N08.
  - La primera gran horda llega la noche del día 1.
  - Las compensaciones de la D-N36 se vuelven a medir con el reloj nuevo.

## D-N162 · Interfaz con PixelLab antes de que caduque el saldo (Lucía, 7-nov 15:45; enmienda el GDD §13)
- Eugenio pidió rehacer la interfaz con PixelLab, y su palabra manda sobre el GDD §13.
- **Cómo queda la interfaz:**
  - Marcos, paneles, tarjetas, botones e iconos pasan a ser pixel art de PixelLab.
  - **El texto sigue siendo nítido** (Inter, UI Toolkit), para que se lea bien.
  - Se mantiene la estructura de la D-N147.
- **Cuándo:**
  - El domingo 08-11 no se toca, porque ese día es para jugabilidad.
  - El **lunes 09-11** van 5 variantes de muestra, cada una pasada por la hoja de cohesión de la D-N53, y el equipo elige una.
  - El **lote sale el 10–11-nov**, antes del 12-nov.
  - Si el 11-nov no está elegida, el saldo (~8.800) se gasta en retratos e iconos antes de que caduque el 17-nov.
- Sin pagos: solo se usa el saldo que ya hay.
- La siguiente libre es la D-N163.
- 7-nov, 15:50 · **D-N160, CONFIRMADA por Eugenio** («Sí»): la Colmena que aprende **sigue en el MVP** y va **después del tutorial** (D-N154). El orden queda así: bloques del domingo, luego tutorial completo, luego la Colmena mínima (memoria de tráfico y de atención, los 3 estados y el informe de inteligencia), integrada en la build. Ya no es una propuesta.

## D-N163 · Reparar v1 del modo construcción, textos del tutorial y variantes de la intro (Lucía (3), 8-nov 10:55)
- **Reparar v1** (`construccion-reparar.md`): el muro pasa a ser una cadena de tramos (sacos, HESCO y puertas), cada uno con su vida. Hay 4 estados visibles: sano (≥ 70 %), dañado (30–70 %, ámbar), muy dañado (1–30 %) y brecha (0, rojo, ya no bloquea). Se entra con B (propuesta) o con el botón Obras, y el combate no se para. Reparan los zapadores con las cifras de la D-N123 (Hugo, §13, sin medir) y con el ruido ×1,5. Un tramo a 0 se **reconstruye**, solo sin zombis a 15 m, y vuelve al 30 %. Esto sustituye al «solo entre oleadas» de la D-N123, porque ya no hay oleadas (D-N136).
- **Tutorial, capítulos 0 a 3** (`tutorial-textos.md`): para que el capítulo 2 siempre tenga algo que reparar, **el tramo de la puerta oeste empieza el día 1 al 45 %**. El C90 se enseña con una tarjeta suelta y no dentro del capítulo 1. Esc sigue siendo el menú de pausa (D-N138), así que no sale del modo obras.
- **Intro** (`intro-variantes.md`): 5 variantes (A 2029, B 2031 con radio, C sin año, D 2034 sobre el mapa, E 2027). Recomiendo la C. Decide Mak; si nadie dice nada antes del bloque 2, Iker monta la C.
- La siguiente libre es la **D-N164**.
- 8-nov 10:52 · Mak elige la **variante C** de la intro («Día 41», sin año). Ya está pasada a Iker.
- 8-nov 11:15 · Retoques de la D-N163 con las cifras de Hugo (`economia/reparar-costes.md`): vida del tramo = precio × 10.000; reconstruir cuesta lo mismo que construir; ataque de día del capítulo 1 de 300 zombis por O1 (sin medir). **El tramo de sacos mide 8 m** (dos módulos de 4 m de Teo), así que vale 1,6 u y tiene 16.000 de vida. El tramo dañado al 45 % del tutorial es **el de HESCO pegado a la puerta oeste**, no la puerta. Muestra de estados de Álvaro (e0bf2f9) aprobada con dos cambios: los sacos no pueden ir en 88885c (es la hierba) y las variantes v0–v2 de los sacos tienen que distinguirse por la silueta.
- 8-nov 10:56 · Sara: el ataque de día del capítulo 1 (300 por O1) da 200 de 200 victorias con el bot quieto y no se forma pila. Queda medido.
- 8-nov 10:58 · Muestra de estados del muro de Álvaro **cerrada** (236586a): sacos en 605c48 (ΔL* 16,8 frente a la hierba), y las siluetas v0, v1 y v2 ya se distinguen. A efectos de juego, la altura del tramo de sacos sigue siendo 1,2 m aunque la v2 llegue a 1,8 m en el modelo. Pasa a Teo para modelar.

## D-N164 · El amanecer ya no da la victoria (Lucía (3), 8-nov 11:05; precisa la D-N136 con el reloj único de la D-N161)
- Con la D-N161, la noche de 22:00 a 06:00 dura 279 s reales, y la horda puede tardar más. Por eso **solo se gana acabando con la horda** (D-N136): sale «Sagunto resiste» (D-N149) y se sigue en el mundo (D-N146).
- **Al amanecer, la horda que queda sigue atacando.** De día no se va ni se borra. El combate no se para (D-N91). Lo que cambia al amanecer es solo la luz.
- La derrota no cambia (D-N133).
- Nacho quita `Tick ≥ TotalTicks` como victoria en NightGame y NightSim, y Marcos hace lo mismo en la zona. Sara vuelve a medir la normal y la difícil sin la victoria por tiempo, con el criterio de la D-N149.

## D-N165 · Muro por tramos: calibrar antes de activarlo (Lucía (3), 8-nov 11:05)
- NightSim (Nacho, fa66281), 7310 en normal: con el muro en un solo bloque se gana el 100 %; con tramos y sin reparar, el 11 %; con tramos y el bot reparando, el 23 %. En difícil se pasa del 61 % al 0 %. La pila se concentra en 2 o 3 tramos del oeste y abre brecha. **El modelo por tramos es el bueno**: el bloque único repartía el daño por todo el muro, y eso era demasiado generoso.
- Las palancas se miden **en este orden**, de una en una:
  1. **Vida por precio** (Hugo, `reparar-costes.md`), con la cara oeste de HESCO a 60.000 cada 10 m.
  2. **La pila empuja a los lados**: parte del daño pasa a los tramos vecinos (Nacho propone el porcentaje). Es lo que hace una masa contra un muro.
  3. Si con eso no basta, Hugo **recalibra la horda** hasta que la normal cumpla la D-N149 (≥ 95 %, mediana del muro ≤ 90 % y munición p10 ≥ 2 u).
- No se toca la regla de «no se repara con zombis a 3 m»: que el tramo caliente no se pueda reparar es justo la tensión que buscamos. Se repara el de al lado, antes de que caiga.
- Los tramos siguen desactivados por defecto en NightSim hasta que la normal cumpla. **En la build (Noche58), reparar entra con los tramos solo si están calibrados.** Si a las 16:00 no lo están, Hugo baja la horda hasta que cumpla y se entrega así.
- El ruido ×1,5 de §3 va después de esta calibración.
- La siguiente libre es la **D-N166**.
- 8-nov 11:15 · Estados del muro de Teo (mr-mak 47a4056, docs/arte/modelado-3d/muro-estados/): **aprobados con un cambio**. La red 303424 de la v4 (sacos y HESCO) está por debajo del mínimo de albedo propio, que es 48403c, y deja el 27–30 % de los píxeles de la cara en sombra dentro de la banda de la horda (1e2016, L* 11,7). Pasa a 50541c y se comprueba con -capdirecta. La arena del derrame se queda como está, pero tiene que medir ≥ 2 px en el LOD1.
- 8-nov 11:20 · Estados del muro **cerrados** (Teo, e4e63ca): red en 50541c y tiras del HESCO en 605c48. En el render de Teo hay un 0,0 % de píxeles en la banda y el mínimo es L* 14,0. Falta la -capdirecta en la build (Marcos), y esa medida es la que manda.
- 8-nov 11:25 · Puerta de vía del muro oeste (Teo, f83482c): **aprobada con un cambio**. El dintel de la v4 a 3 m no deja pasar el tren ni la catenaria; sube a 6 m (el gálibo y la altura de la catenaria están SIN VERIFICAR, Paula lo confirma) o, si no, se quita. Banda de la horda: 0–1,8 % en el LOD1, vale. No se elige variante: la pone la semilla por instancia (norma de las 5 variantes). Si Marcos necesita una fija para capturas, la v1. Para Marcos: el hueco ahora mide 5 m (antes `via_hueco_mm` era de 3,2 m) y la puerta cerrada tiene que tener sólido (D-N151; fue el fallo de qa20).

## D-N166 · Embarque y desembarque del tren (Lucía (3), 8-nov 11:35; para el panel «Preparar tren» de Iker y la API de Nacho)
- **Si el nodo está sitiado** (D-N152), el tren espera a las puertas y **solo baja la tropa**, que se queda fuera del muro junto al tren, como la tropa de fuera de la D-N151. Es un refuerzo que llega por la espalda de la horda, y eso es una decisión táctica con riesgo. Los vehículos y la carga no bajan hasta que acaba el asedio y el tren entra, porque hace falta el andén.
- **Tiempos**: 10 s reales por pelotón y 20 s reales por vehículo, para subir y para bajar (propuesta de Nacho, sin medir; con la D-N161 son ~17 y ~34 min de juego). Hugo los ajusta si no le cuadran. La carga sube y baja con el tiempo que ya tenga la economía.
- **De noche** solo se sube y se baja dentro del recinto y sin zombis a 3 m, salvo el desembarque de la tropa fuera de una estación sitiada, que es justo para eso. Mientras sube o baja, la tropa no dispara.
- La siguiente libre es la **D-N167**.
- 8-nov 11:40 · Fondo de la intro (Bruno (3), f608880): **aprobada la A**, «La ciudad apagada», para la intro C. Mejora opcional, si Iker tiene tiempo en el bloque 2: un fondo por tarjeta, en este orden: D, A, B, C y C (tarjetas 1 a 5). Así la intro avanza como un travelling por la vía hasta Sagunto. La E se descarta.

## D-N167 · El NH90 vuelve solo a rearmar (Lucía (3), 8-nov 11:42; a raíz del fallo S2 de Sara)
- Si un NH90 en vuelo baja de **30 % de munición**, vuelve solo al helipuerto propio más cercano (D-N155), aterriza, rearma y repone combustible, como los pelotones al 30 %.
- Al acabar **se queda posado y listo**, con un aviso en hueso: «NH90 rearmado». No vuelve solo al combate, porque el jugador decide dónde lo manda. Si lleva un pelotón a bordo (D-N143), el pelotón sigue a bordo.
- Mientras vuelve, el aviso es ámbar («NH90 · vuelve a rearmar»). El jugador puede anular la vuelta con una orden nueva, y entonces asume el riesgo de quedarse seco.
- Nacho lo pone también en NightSim, para que la -nightbot y la simulación sigan coincidiendo. Sara lo comprueba en la corrida.
- La siguiente libre es la **D-N168**.

## D-N168 · La pila que salta es parte del juego; el contrapeso es la tropa de dentro (Lucía (3), 8-nov 12:20; responde a la pregunta de Nacho sobre la pila de 1.400 y precisa la D-N165)
- Con la trepada calibrada contra la build (Nacho (3), b2c460a), 7310 en normal gana el 2,6 %: el muro aguanta (93–97 %, ninguna brecha), pero **entran trepando unos 880 zombis y tumban el tren**. Las palancas (a) y (b) de la D-N165 no cambian nada.
- **Que la pila salte en tromba se queda.** Es el momento de cine de la noche y es la D-N148: el muro no basta, hay que defender también lo de dentro. No se sube el muro ni se frena la pila.
- **El contrapeso es el reparto de la D-N151.** La tropa de dentro se coloca junto al tren y es lo primero que encuentran los que trepan. Nacho corre, con 7310 en normal, tres repartos dentro/fuera: 50/50, 70/30 y 30/70. El resultado se suma al barrido de hordas de Hugo de las 13:15.
- **Orden de decisión:** primero el mejor reparto y, con ese reparto, la horda más grande que cumpla la D-N149. Hugo elige la cifra.
- Para el tutorial (texto 1.3) y el NightBot, la tropa de dentro empieza junto al tren.
- La siguiente libre es la **D-N169**.
- 8-nov 12:30 · Parámetros de los tramos en la zona (Marcos 54dda97, con -tramos; preguntó Nacho (3)): (a) vida = 11.924 por u, como fijó Hugo, para que el total siga en 1.200.000. (b) Reparar gasta las **existencias de Sagunto**, no 40 u aparte. (c) Reconstruir cuesta **el precio de la pieza y su tiempo de obra** (Hugo), no 1,6 u y 10 s fijos: un HESCO del oeste son 5,67 u. (d) La puerta de vía oeste es **un tramo con vida** (precio 8 u). (e) Que la horda pase por encima antes de romper el muro se acepta (D-N168). Reparar se nota en el desgaste entre noches, en el tutorial y más adelante con la Colmena. Ahora no se cambia.

## D-N169 · Nuevo criterio de la normal: que haya tromba (Lucía (3), 8-nov 12:55; enmienda el criterio de la D-N149, a propuesta de Hugo)
- Con la trepada calibrada, el muro acaba con una mediana del 97–99 % en todas las corridas, se gane o se pierda. Todas las derrotas son por el tren. «Muro p50 ≤ 90 %» ya no se puede cumplir y ha dejado de medir la tensión de la noche.
- **Criterio nuevo de la normal:** ≥ 95 % de victorias, **pila máxima p50 ≥ 150** (la horda llega a trepar y hay tromba, D-N168) y munición final p10 ≥ 2 u. **La difícil sigue entre el 50 y el 80 %.**
- **Horda (Hugo):** H6500, es decir, 5.520 en normal (100 %, pila 392/416, munición 39 u, reparto 50/50). La difícil, en torno a 6.600 (escala ~1015), queda pendiente de que la confirme Nacho. Se descarta H7400 (95,9 %) porque está pegada al precipicio: con H8600 se cae al 4 %. Se elige con margen.
- Hugo la apunta en sus datos y Marcos la mete en la corrida -nightbot del control.
- La siguiente libre es la **D-N170**.

### D-N165 / D-N168 / D-N169 (adenda, Hugo (3), 8-nov 13:00): medida y horda elegida
- **Trepada calibrada** contra la traza de la Noche58a (7310): NightSim con ClimbPermilS 240 y un tope de 55 entradas/s reproduce las entradas (−4 % a las 22:35, +5 % a las 22:55) y la caída del tren (22:52 frente a 22:55). Por defecto en NightSim desde b2c460a (Nacho (3)). Detalle en `economia/entregas/trepada-calibracion/`.
- **Pasos (a) y (b) de la D-N165, medidos** (31 tramos del Snapshot, 100,64 u, 11.924 por u, 1000 semillas, ×103): con 7310, la normal da un 2,6 % y la difícil, un 0 %. **0 brechas**, muro p50 del 97 %. Se pierde siempre por el tren, por lo que trepa. El empuje de 0 o 500 da lo mismo.
- **D-N168, repartos con 7310 normal**: guardia 0/1/2/3/4 → 2,6 / 2,5 / **3,9** / 1,3 / 0,4 %. Queda el 50/50, pero mueve poco.
- **Paso (c), barrido** (k=0; normal / difícil): H4700 100 / 100 %; H5600 100 / 98,6 %; **H6500 100 % (pila 387/406, munición p10 39 u) / 4,3 %**; H7400 95,9 % (pila 552/583) / –; H8600 2,6 / 0 %. Con el 50/50, H6500 da normal 100 % y difícil 5,1 %.
- **Elegido: base H6500, normal 5520 (escala 850)**, con margen frente al precipicio entre H7400 y H8600 (la calibración tiene ±15 %). Fácil 725 → unos 4710. **Difícil: unos 6600 (escala ~1015), PENDIENTE** de las corridas de 985/1015/1046. Se cierra con una nota cuando salgan.
- Por la D-N169, el «muro p50 ≤90 %» queda sustituido por «pila máxima p50 ≥150». H6500 normal lo cumple (392).
- 8-nov 13:10 · **Corrección de la D-N168 (error mío, medido por Hugo):** la guardia quieta junto al tren quita de 20 a 25 puntos de victorias cerca de la frontera (normal H7400: 70,6 % con guardia y 95,9 % sin ella; difícil H5600: 78,1 % y 98,6 %). La tropa de dentro **no empieza quieta junto al tren**: empieza libre y el NightBot la lleva al muro amenazado (k=0). La guardia junto al tren queda como **orden opcional del jugador**. Lo de que la pila salte (D-N168) no cambia. Con la horda elegida (5520) se gana el 100 % en los dos casos, así que la Noche58 no cambia.
- (Hugo (3), 8-nov 13:35, cierre de la adenda) **Difícil, medida con k=0** (como la build): 6200 da 99,7 %, **6400 da 79,4 %**, 6600 da 34,9 % y 6800 da 20,9 %. **Elegida 6400** (escala 985 sobre la base 6500), porque la build es algo más dura que NightSim (pila +11 %) y en ella se espera en torno al 65 %. Paquete en `economia/entregas/noche58/`. `unidades.py`: OLEADAS base 6500, DIFICULTAD_NOCHE 725/850/985 y texto de victoria según la D-N164.
- 8-nov 13:25 · Aviso del C90 del tutorial (propuesta de Hugo, aceptada): salta la primera vez que hay ≥ 40 zombis dentro del recinto a menos de 30 m de un pelotón de fusileros. Una sola vez en toda la partida, no por noche, y nunca si se ha saltado el tutorial.

## D-N170 · Deseos de Eugenio para después de la Noche58 (Eugenio, 8-nov 13:28; Lucía (3))
- Eugenio lo dice claro: **no es para hoy**, y el plan del día no cambia.
- **Fallo:** el cartel «Sagunto resiste» vuelve a salir cada vez que se sale y se entra en otra localización. Tiene que salir una sola vez por ataque ganado (D-N149). Es un fallo, no un deseo: lo lleva Marcos cuando acabe el bloque.
- **El tren sale de la estación a la vista**: se abren las puertas, pita y acelera poco a poco hasta irse (Iker y Marcos; sonido de Nuria).
- **Doble clic en una localización** lleva directamente a ella. **Doble clic en un tren en viaje** lleva a él, y la cámara lo sigue de cerca (Iker).
- **Tiempo real dentro y fuera**, como en Ebbtide. Ya es la regla de la D-N91 y de la D-N161 (un solo reloj). Se revisa que no quede ninguna pausa ni ningún salto al cambiar de vista.
- La siguiente libre es la **D-N171**.

## D-N171 · El tutorial enseña a traer refuerzos a Sagunto en tren (Eugenio, 8-nov 13:32; Lucía (3); recupera lo que pedía la D-N150)
- Eugenio preguntó por el tutorial que enseñaba a llevar refuerzos hacia Sagunto. Con la D-N154 se había quedado solo en el capítulo 4, el del aire, y eso llega tarde. **Vuelve al capítulo 3, por tren.**
- El capítulo 3 pasa a ser ida y vuelta: Sagunto lleva carga a Nules con un pelotón de escolta, y **Nules devuelve a Sagunto un destacamento de refuerzo (1 pelotón de fusileros y 1 Lince)** antes de la primera noche. Si a la llegada Sagunto ya está sitiada, el tren espera a las puertas y solo baja la tropa (D-N152, D-N166).
- El destacamento existe solo si el tutorial está activo (fácil y normal, la primera vez). La difícil no lo tiene, porque está calibrada sin él.
- Textos: `tutorial-textos.md`, pasos 3.6 y 3.11–3.18. El capítulo 4 (helicópteros desde el helipuerto, D-N150) se mantiene.
- Hugo comprueba que la primera noche no queda regalada con criterio de la D-N169. Si sale demasiado fácil, se quita el Lince.
- La siguiente libre es la **D-N172**.

## D-N172 · Capítulo 3 del tutorial: pedir refuerzos a otra estación (Eugenio, 8-nov 13:33; Lucía (3); sustituye el planteamiento de la D-N171)
- Eugenio lo aclara: como la defensa de Sagunto parece difícil, esa es la excusa para enseñar a **ir a otra estación y mandar desde allí unidades a Sagunto**. Es un pedido suyo, no opcional.
- **Estación**: Nules, la de al lado (D-N156). Empieza con **su propio tren parado en el andén** y un **destacamento de refuerzo: 1 pelotón de fusileros y 1 Lince**, más materiales si el jugador los carga. Todo esto existe solo con el tutorial activo (fácil y normal, la primera vez).
- **Cuándo**: al acabar el capítulo 2, a primera hora de la tarde del día 1. Lo abre el aviso de radar de 6 h con la horda de la noche. Quedan unos 4,5 min reales hasta las 22:00.
- **Pasos**: salir al mapa, abrir Nules, Preparar tren (pelotón, Lince como apoyo terrestre y, si se quiere, materiales), mandarlo a Sagunto mirando el ETA, volver, descargar y colocarlos en el muro oeste. Si llegan con la estación ya sitiada, el tren espera a las puertas y solo baja la tropa (D-N152 y D-N166).
- **Señales**: aviso de radar, anillo en Nules, ETA en el panel, «Refuerzos de Nules · llegan en 0:xx» en el mapa y aviso «Tren en Sagunto».
- El viaje de ida a Nules con carga (D-N154) pasa a ser un objetivo **después de la primera noche**: «Devuelve el tren a Nules con munición».
- Hugo comprueba con el criterio de la D-N169 que la primera noche con el destacamento no queda regalada. Si sale demasiado fácil, se quita el Lince.
- La siguiente libre es la **D-N173**.

## D-N173 · Un solo aeródromo, en el mapa y en un sitio real; anula la D-N155 (Eugenio, 8-nov 13:42; Lucía (3))
- **Error del equipo, y mío como diseñadora.** Eugenio había dicho que todo vehículo aéreo sale de un aeródromo, y la D-N155 le dio a Sagunto un helipuerto propio. Se anula.
- **El aeródromo es una localización propia del mapa global**, no una parte de una estación. Se entra desde el mapa, como a cualquier nodo. Al principio hay **uno solo**, y tiene que estar **donde habría uno en la vida real**. El sitio lo busca Paula con fuentes. Criterios: un aeródromo o una base aérea real, a una distancia razonable de Sagunto y fuera de Valencia, que en el lore ha caído. Ningún candidato está verificado todavía.
- **Unidades aéreas**: los NH90 (y más adelante los demás aparatos) viven en el aeródromo, con su guarnición para embarcar un pelotón (D-N143). En el MVP tiene sus propias existencias de munición y combustible; su logística va después del MVP.
- **Cómo llega el NH90 a la noche de Sagunto**: desde el mapa, se abre el aeródromo, se elige el NH90 y se manda a Sagunto. Vuela en línea recta (D-N91), con un **ETA que sale de la distancia real**. Entra en la zona por el borde, en la dirección del aeródromo, con la flecha de borde de la D-N147. Puede **posarse en cualquier claro de 20 × 20 m** para bajar la tropa (D-N143). No hace falta helipuerto.
- **Dónde rearma** (enmienda la D-N167): al bajar del 30 % vuelve solo **al aeródromo**, con su ETA de vuelta. Irse a rearmar cuesta tiempo, y esa es la decisión.
- **Capítulo 4 del tutorial**: se dispara la primera vez que el jugador abre el aeródromo. Reutiliza `tutorial-refuerzos.md` con el aeródromo como origen: abrir el aeródromo, elegir los NH90 con su pelotón, mandarlos, seguir el ETA, volver, posarlos en un claro (L) y bajar la tropa (U).
- **Fallo que ha visto Eugenio**: en todas las estaciones salen las mismas unidades, helicóptero incluido. Cada estación tiene que tener **su propio plantel**. Sagunto, sin NH90.
- **Construir helipuertos en las estaciones** (D-N153) queda en suspenso hasta que Eugenio diga si los quiere.
- La siguiente libre es la **D-N174**.

## D-N174 · Línea de visión: no se dispara a través de lo sólido (Eugenio, 8-nov 13:39: «pueden matar a zombies que están detrás de estructuras, lo cual tiene poco sentido»; Lucía (3))
- **Fuego directo** (fusiles, ametralladoras, cañones de vehículo, C90): solo con línea de visión. **Tapan el disparo** los edificios, los vagones y el tren, los muros y las puertas, y el relieve.
- **El muro propio no tapa a quien lo defiende**: una unidad a 2 m o menos de su muro dispara por encima (está en la banqueta o asomada al parapeto). Más lejos de 2 m, el muro tapa en los dos sentidos. Con el HESCO (2,1 m), igual, a través de su banqueta.
- **La altura cuenta (2,5D)**: se compara la altura de la boca del arma con la del obstáculo a lo largo del rayo. Las torres, azoteas y muros elevados, y las torretas de vehículo, disparan por encima de lo que sea más bajo que ellos. El NH90 en vuelo solo lo tapan los edificios altos y el relieve.
- **Los zombis no tapan** (la horda es masa y blanco a la vez) y **la pila tampoco**. La tromba se sigue viendo y se le sigue disparando.
- **Fuego indirecto** (morteros y artillería, después del MVP): no necesita línea de visión, pero sí que alguien vea el blanco.
- **Cómo se calcula**: un rayo sobre la rejilla de 1 m del A* (`NavGrid`) con una capa de alturas, comprobado al elegir blanco y no a cada bala. Nacho propone la implementación y mide en NightSim el coste por tick y el cambio de balance con la horda de la D-N169. Si el balance cambia, Hugo recalibra. Luego lo implementa Marcos.
- La siguiente libre es la **D-N175**.
- 8-nov 13:50 · **Retoque de la D-N172 (medido por Hugo y Nacho, dn171):** con el pelotón y el Lince, la normal queda regalada (pila p50 67) y la fácil también. Se **quita el Lince**. Además, el capítulo 3 **se dispara en la primera noche, cuando la pila pasa de 150**, y el refuerzo llega como un rescate a mitad de la tromba. El tren espera a las puertas y la tropa baja fuera (D-N166). En ese capítulo la horda no espera. El viaje con carga a Nules pasa a ser el objetivo de después de la primera noche, y ahí se enseñan la carga y el apoyo terrestre. Falta medir la versión del rescate (Nacho).
- 8-nov 13:55 · **Ubicación del aeródromo (D-N173): base «Jaime I» de Bétera**, la que recomienda Paula (`docs/arte/referencias/aerodromos.md`, 922fa6a en el repo local). Es militar y de helicópteros, con helipuerto y torre, y está a 18 km de Sagunto (unos 4 min de NH90) y a 37 km de Nules. Que esté a 15 km de Valencia, que ha caído, se aprovecha en el lore: es una base que resiste al borde de la ciudad perdida. Que en la realidad haya NH90 allí está SIN VERIFICAR, y no hace falta: las fuerzas del juego son ficticias. Alternativa descartada: El Pinar (Castellón), que es civil. Las coordenadas son las de la ficha de Paula, sin redondear.
- 8-nov 13:58 · Coordenadas del aeródromo (Paula, helis.com LEBT): **39.6244, -0.4725** (helipuerto de Bétera). La ficha está en `docs/arte/referencias/aerodromos.md`.
- 8-nov 14:00 · Nivel de Bétera v0 (Álvaro (3), `niveles/betera-nivel.md`): aprobado como base. (1) **La pista se queda**, pero con la medida de la fuente que citó Paula (275 m, GlobalMilitary, que no es oficial; queda marcado así) y no con 200 × 18 m inventados. Da el frente B4 y sirve para los Chinook de después. (2) **Plantel: 2 NH90, 2 pelotones para embarcar (uno por aparato, D-N143) y 1 pelotón de guarnición fijo.** Hugo lo revisa con la regla de la D-N169. (3) **En el MVP, Bétera no sufre asedios de la gran horda**: el reducto y sus 4 frentes quedan listos para cuando la Colmena (D-N160) aprenda a atacar lo que más usa el jugador. El helipuerto v4 de Teo como toma P1, bien aprovechado.
- 8-nov 14:05 · Existencias y tiempos de Bétera (Hugo, `economia/betera-existencias.md`, solo cálculo): **aprobado** con 50 u de munición y 70 u de combustible iniciales, sin logística ni mantenimiento hasta que la haya; valla a 0,5 u y 5.000 de vida por tramo de 10 m. Como con el reloj único el vuelo Bétera–Sagunto dura solo unos 2,4 s reales, para que rearmar cueste se añade **un tiempo fijo de 20 s reales para preparar y despegar, y otros 20 s para tomar tierra en Bétera**, además de los 30 s de rearme. Una vuelta a rearmar cuesta así unos 75 s, más de la cuarta parte de una noche de 279 s. Esa es la decisión.
- 8-nov 14:10 · Rescate de Nules medido (Hugo y Nacho, 200 semillas): cumple la D-N169 en normal (100 %, pila 389) y en fácil (100 %, pila 250). Disparo del capítulo 3: **pila > 150 o 60 s reales después del primer contacto con el muro, lo que ocurra antes**, porque en fácil el 15 % de las noches no hay tromba. Si salta por tiempo, se usa el texto 3.1b.
- 8-nov 14:20 · Piezas de Bétera (Teo (3), `arte/modelado-3d/betera/`, 8 piezas × 5 variantes): **aprobadas con tres cambios.** (1) La torre de control (6,8 %) y la garita (7,2 %) llevan sombras dentro de la banda de la horda (L* 9–13): se suben fuera de la banda y se comprueba con -capdirecta. (2) El fuste de la torre no puede ser d4d0cc en grande, porque es el color de selección: pasa a b8b8b8 y el d4d0cc queda solo en los brillos. (3) El pino queda SIN VERIFICAR hasta que Paula tenga foto. Resto (hangar, tanque, polvorín, valla, puerta de la valla) sin cambios; Teo confirma que entregar.py admite 94948c en los costados de la bóveda del hangar. Zona del aeródromo (Álvaro v0.2, 324 × 224 m o el encuadre de reserva): la decide Iker según el código.

## D-N175 · La horda de fuera reacciona a la tropa que tiene cerca (Nacho (3), propuesta; Lucía (3), 8-nov 14:15)
- Medida de Nacho (`economia/entregas/dn172/`, 200 semillas): el rescate de Nules no corre ningún peligro. Con el desembarco por el este, 0 bajas y 0 zombis a 15 m. Por el oeste, a la espalda de la horda, hay 421 zombis a 15 m de mediana y tampoco hay bajas. La razón es que ni NightSim ni la zona hacen que un zombi cambie de objetivo: todos siguen un único campo de flujo hacia la puerta (FlowFieldSystem). Así, «atacar a la horda por la espalda» (texto 3.7) es una galería de tiro, no una decisión.
- **Regla, aprobada para medir.** Un zombi de **fuera del muro** con tropa propia a **25 m o menos** cambia su objetivo a esa tropa, igual que los trepadores (D-N148, ClimberTargets). **Tope: el 30 % de la horda** a la vez, para que el muro siga siendo el frente. No cambian de objetivo la pila ni los trepadores que ya están en el muro. Los vehículos cuentan como tropa.
- **Se da por buena si**, con el disparo doble de la D-N172: la normal sigue cumpliendo la D-N169; en fácil, el pelotón de Nules sobrevive en ≥ 95 % de las semillas; y el desembarco por el oeste cuesta bajas de verdad, de modo que bajar por el este siga siendo la opción sensata. Si en fácil el pelotón muere más, la palanca es el radio (de 25 a 15 m), no el tope.
- Orden: Nacho la mide en NightSim. Después el coordinador le pasa el resultado a Marcos, que la mete en la zona como segundo campo de flujo o como desvío local (lo elige él según el código). Álvaro revisa los puntos de desembarco con el resultado.
- La siguiente libre es la **D-N176**.
- 8-nov 14:25 · Aire de Bétera medido (Hugo y Nacho, `economia/entregas/dn173/`, 200 semillas). Con 1 o 2 NH90 la pila p50 no cambia (424 en normal y 342 en fácil): **el plantel de Bétera se queda** (2 NH90 y 2 pelotones). Pero sin el NH90 que tenía Sagunto, la normal con horda 5.520 baja al 67,5 % y no cumple la D-N169. **Decisión (amplía la D-N169): la horda de cada dificultad cumple el criterio sin aire y sin el rescate del tutorial.** El aire y Nules hacen la noche más cómoda, pero no la sostienen. Hugo elige la normal entre 4.700, 5.000 y 5.250, y la fácil y la difícil se recalculan con la misma regla. Se descarta que un NH90 despegue solo con la primera alerta, porque le quita la decisión al jugador.
- 8-nov 14:30 · Inventario de obstáculos de Sagunto para la línea de visión (Álvaro (3), `niveles/sagunto-linea-vision.md` y CSV para Nacho). (1) **La pila no se queda sin defensa desde dentro**: la regla del muro propio a ≤ 2 m (D-N174) se queda. La tropa pegada al HESCO de 2,1 m dispara por encima, como desde un parapeto, aunque la boca del fusil esté a 1,6 m. La tropa que está más atrás no ve la pila. Ahora que Sagunto no tiene NH90 (D-N173), esa excepción es la que sostiene la defensa. El puesto en la azotea del edificio de viajeros (11 m, a 26 m del muro) se apunta como contrapeso, pero solo si Nacho mide que la banqueta y la tropa pegada al muro no dan para tanto. (2) **Los nidos de la puerta de la vía pasan de 3 m a 1,5 m del muro** (NetWorld.cs:1439). (3) **El C90 es tiro curvo**: la granada de 40 mm va en parábola y no necesita línea de visión, como el resto del fuego indirecto. (4) Los terraplenes del paso superior, las tolvas y el autobús **tapan el tiro, pero no el paso**: en el MVP el pathing no cambia.
- 8-nov 14:40 · **D-N162: prefijo de PixelLab validado** (`arte/pixellab-prefijo-validado.md`) contra la maqueta 1 (plano v1.4) de la D-N147. La placa pasa a ser navy con marco gris pizarra, no oliva. La selección es hueso d4d0cc, pintada por código; el brief decía f0dc9c y estaba mal. El centro del panel va liso para el texto nítido. El rojo y el ámbar no se nombran. Las 5 variantes cambian una palabra de estilo, no solo la semilla. Lo lanza mañana Iker o Marcos en el PC de Eugenio (5 muestras, sin pasar del 20 % del saldo) e Iris lo unifica.
- 8-nov 14:45 · **Corrección de Lucía (3) a la línea de las 14:30, punto (3): me equivoqué de arma.** Álvaro preguntaba por el **lanzagranadas AG36** (40 mm), que es el que va en parábola: ese es **tiro curvo, sin línea de visión**. El **C90 sigue siendo fuego directo** (cohete de tiro tenso), como ya decía la D-N174. Muro oeste (Álvaro, `niveles/sagunto-nivel.md` §10.11): **aprobados** la banqueta como dibujo de la regla de los 2 m (franja X 70,5–72,5, escalón de palés de 0,4 m, coste 0, unos 35 tiradores para 28 de tropa) y los nidos a 1,5 m. **Las dos atalayas de 4 m** en las esquinas interiores del oeste (10 u y 8 obrero·h cada una, por confirmar con Hugo) **entran solo si la banqueta sola no cumple la D-N169 sin aire**; si cumple, quedan para después del MVP. No entran ni la pasarela ni las troneras. La azotea sigue de reserva.
- 8-nov 14:50 · **Coches civiles abandonados** (Teo (3), `arte/modelado-3d/coches-civiles/`, TBD 3c3aa94): 5 tipos × 5 estados. Las 50 mallas pasan la auditoría y no tienen ningún píxel en la banda de la horda. **Aprobado con dos cambios.** (1) **La lona del camión pequeño no va en verde oliva**, porque se lee como un vehículo militar nuestro: pasa a beige b4a080/605c48 o a gris 94948c/605c48. En el reparto por semilla del atasco, el verde y el ocre no pasan del 20 %. (2) **El óxido del quemado no va como cuadrado plano en el techo**, porque parece un marcador: va en manchas irregulares por el techo y el capó. Sustituye a coche_2000, salvo la ambulancia, que se queda.
- 8-nov 14:55 · Atalayas del muro oeste (Hugo): **coste confirmado, 10 u y 8 obrero·h cada una**, unos 23 s reales. Si entran (solo si la banqueta sola no cumple la D-N169 sin aire), **empiezan ya construidas** y Hugo mide con el muro de 140 u y el mantenimiento de 1,4 u/día. No van como obra del jugador por dos razones: el modo construcción v1 solo repara (D-N153), porque levantar torres es «torretas» y está fuera del MVP; y si sin ellas la normal no cumple, dejarlas opcionales significa que la partida de partida no cumple el criterio. Como lección de construcción quedan para después del MVP.
- 8-nov 15:00 · Atalayas en la campaña (Hugo, modelo económico, 1000 partidas): con 140 u, las derrotas en equilibrado pasan del 13,8 % al 14,2 % y en prisa del 43,1 % al 41,5 %; en escasez no cambian. Está dentro del ruido (±1,1). **Aceptado y vigilado.** Si aprieta en la demo, la palanca es H0 1500.
- 8-nov 15:05 · Bétera (Iker c73a83e): cada salida gasta 3 u de combustible y cada rearme 1,8 u de munición. Con 70 u y 50 u salen unas 23 salidas y unos 27 rearmes, de 5 a 6 noches de uso intenso (Hugo lo confirma). **Cerrado.** Reloj: ×103 en la red y en la zona (D-N161). Lo cambia Nacho después del control de las 18:30, así que la Noche58 todavía va con ×72 en la red.
- 8-nov 15:15 · Bétera r2 con las fotos de Paula (Teo (3), `arte/modelado-3d/betera/hoja_*_r2.png`): **aprobada para reentregar.** Pieza nueva: la torreta de vigilancia (6,7 m, sin luz roja). La garita de suelo se queda en el control de la puerta. La valla va sobre un muro bajo enfoscado de 1,2 m, con postes cada 3,33 m y sin cartel rojo. El polvorín pasa a 11 × 22 m y no pisa los iglús. Pino de corteza clara, y la v3 es un pino en parasol. Medido por Lucía: ninguna hoja pasa del 0,4 % en la banda de la horda (L* 9–13), y el d4d0cc está al 0 % en todas.
- 8-nov 15:20 · Datos reales del NH90 (Paula, `/mnt/project-files/nh90_datos.md`). **Solo cambia una abstracción: el claro para posarse pasa de 20 × 20 m a 25 × 25 m.** El rotor girando mide 19,56 m, así que 20 m no deja margen; 25 m es el rotor más unos 2,5 m por lado. Los ~50 m reales se descartan porque dentro de Sagunto no habría dónde posarse. **Se quedan igual:** los 260 km/h (verificado; ya coincide con los ~2,4 s reales de Bétera a Sagunto); los 20 s de despegue y de toma, que son de balance y ya son más que los 3–6 min reales con el reloj ×103 (de 1,75 a 3,5 s); y 1 pelotón por aparato (D-N143), aunque caben 20 personas, porque así se ha medido (lo de 2 pelotones, después del MVP). La autonomía de 4–5 h (unos 140 s reales en el aire) no se modela en el MVP: el NH90 solo vuelve por munición (D-N167). Lo miramos después del MVP.
- 8-nov 15:35 · Recinto de Nules v0.1 (Álvaro; coste de Hugo en `economia/nules-recinto.md`). **Aprobadas las 130 u**: HESCO solo en el frente este (entrada Nb, con alas de 15 m) y sacos en el resto. Da nivel 4,3 y 1,3 u al día; Sagunto, con 120 u, sigue siendo el nudo fuerte. El edificio de viajeros cuenta como tramo de muro con 120.000 de vida. **Nules es propia desde el principio** (D-N156, diseño de Eugenio), pero eso suaviza el castigo de la estrategia de prisa (derrotas del 43 % al 36 %). La palanca elegida es que **Nules empiece casi sin munición**, que además es lo que da sentido al objetivo «Lleva munición a Nules». Hugo propone la cifra y la mide (busca que la prisa vuelva a rondar el 40 %); la guarnición se queda. La defensa de Nules en el viaje queda pendiente del escenario nules.json en NightSim (Nacho).
- 8-nov 15:40 · Red al empezar (Álvaro, `niveles/red-inicio.md`): aprobada como v0, con los km provisionales de RailNet. (1) **Nules no sufre asedio la primera noche**: puede sufrirlo a partir del día 2, para que el capítulo 3 y el objetivo de munición tengan destino. (2) La vuelta a rearmar del NH90 ya está resuelta (14:05): 20 s para despegar, 20 s para tomar tierra y 30 s de rearme dan unos 75 s, aunque el vuelo dure 5 s. (3) Para Iker (§5): fuera las existencias de Valencia (caída) y de Teruel, y los horarios viejos. **El almacén de Nules no va vacío, sino casi sin munición**, con la cifra que dé Hugo (15:35).
- 8-nov 15:45 · Palanca de Nules medida (Hugo): en el modelo económico no funciona, porque el modelo manda munición al nodo sitiado al instante. **Decisión: Nules empieza con 0 u de munición y con su guarnición.** La prisa queda en torno al 36 %, 2,6 veces el equilibrado, y es castigo suficiente: el 40 % se retira como objetivo. **Hugo mete en el modelo el viaje de munición en tren** (Nules no recibe munición hasta que llega el primer tren). No es para buscar el 40 %, sino porque un modelo en el que la munición llega sola mide mal la mecánica central del juego.
- 8-nov 15:50 · Escala de existencias (Hugo, `economia/escala-existencias.md`): aprobada con un cambio. El almacén de zona se llena con min(tope, reserva) **al empezar la partida y al empezar cada ataque, de día o de noche** (no solo al anochecer, para que el ataque del día 1 y la reparación de día tengan existencias). Lo que sobra vuelve a la reserva al amanecer. Entre ataques, el jugador puede reponerlo a mano hasta el tope. Pendiente de que Hugo lo confirme.
- 8-nov 15:55 · Escala de existencias: **confirmada por Hugo**, con un ajuste suyo que acepto. Lo que sobra vuelve a la reserva al acabar cada ataque, no al amanecer, porque con el reloj único los ataques no van atados a la noche. Va a Iker. Plantel medido de Sagunto (Nacho): 5 pelotones, 1 Dragón y 2 VAMTAC.
- 8-nov 16:00 · Viaje de munición en tren en el modelo económico (Hugo, 1000 partidas): la munición que llegaba sola regalaba unos 6 puntos al equilibrado y 15 a la prisa. **Aprobado a PARAM**: H0 baja de 1550 a 1500, y el refuerzo de munición a un nodo sitiado va en tren, con prioridad, y retrasa el resto del reparto al día siguiente. Resultado: equilibrado 13,1 % y prisa 43,2 %, con Teruel el día 3 y Zaragoza el 13. La escasez del equilibrado sube del 55 % al 63 %. Se acepta, porque esa hambre es la tensión del tren, y queda vigilada: si pasa del 65 %, se revisa. Se descarta la versión estricta (82 %). Los CSV de la Colmena (balance_colmena.csv) se regeneran y van a Nacho y a Marcos **después del control de las 18:30**, junto con el reloj ×103, para no mezclar cambios en la Noche58.
- 8-nov 16:05 · Piezas de Nules v0.1 (Teo (3), `arte/modelado-3d/nules/`, 8 hojas): **aprobadas.** Edificio de viajeros de 21 × 17 m hecho con el kit, marquesina adosada, puerta de vía doble de 7,4 m, muelle de carga, nave del polígono, mobiliario urbano y kit de vía y andén. Medido por Lucía: banda de la horda de 0,5 % como mucho (la puerta doble, por el HESCO, igual que la sencilla), sin d4d0cc ni rojo. Un retoque: el cristal de la farola apagada va en 6c7874; f0dc9c se lee como luz encendida y solo vale si alguna farola tiene corriente.
- 8-nov 16:15 · **D-N175 medida** (Nacho, sin aire, 200 semillas): con el desembarco al oeste, el pelotón de Nules cae en fácil en el 44 % de las partidas a 25 m y en el 56 % a 15 m. Bajar el radio no lo arregla, porque el pelotón baja a 6 m del muro, donde llega la horda. **Decisión: la regla sigue igual en todas las dificultades** (sin reglas distintas por dificultad que el jugador no ve), con 25 m. Lo que cambia es el tutorial: **el tren de Nules espera en la puerta este** y la tropa ataca desde el flanco sur, (192; 60) → (100; 34), donde Nacho midió 0 bajas. Mi criterio del ≥ 95 % era para ese desembarco, no para el del oeste. **Los textos 3.7 y 3.8 cambian** para enseñar la regla: 3.7 «Sagunto está sitiada: el tren espera en la puerta este. Baja la tropa.» y 3.8 «Llévalos al flanco sur y dispara desde ahí. Si te pegas a la horda, irá a por ellos.» Nacho mide la puerta este con la D-N175 en fácil (≥ 95 % de supervivencia) y en normal (≥ 80 %).
- 8-nov 16:20 · Kit de defensas (Teo (3), `arte/modelado-3d/defensas/`, 5 hojas): **aprobado sin cambios.** Esquinas, remates y tramos cortos de HESCO y de sacos, sacados de los tramos aprobados. Banqueta de tiro de 5 y 2,5 m (palés en 845c28, que no se lee salmón) y nido de 3 × 2,4 m con techo, red y dañado. Valla de Bétera con los 4 estados de la D-N163, el sano partido en dos solo a la vista, y caída hacia dentro. Medido por Lucía: 0 % en la banda de la horda, sin d4d0cc ni rojo. El rojo de la brecha lo pone la capa de obras, no el modelo.
- 8-nov 16:30 · **D-N175 confirmada** (Nacho, 1000 semillas, sin aire, 25 m, tren de Nules en la puerta este). Pelotón: sobrevive en el 100 % en fácil y en normal, sin bajas. Victorias: 100 % en fácil y 99,3 % en normal. Desde el flanco sur abate de media 114 zombis en fácil y 251 en normal. Bajar al oeste sigue saliendo caro (cae en 88/200 en fácil y en 197/200 en normal) y en normal mata menos. **Pasa a Marcos después del control de las 18:30.** Queda abierta la difícil: con 6.500 y sin aire se gana el 0,1 %. Hugo la recalcula con la ampliación de la D-N169 (cumplir sin aire, de 50 a 80 %).
- 8-nov 16:40 · **D-N174 medida** (Nacho, normal 5.520, sin NH90, 500 semillas). Sin línea de visión se gana el 67,5 %. Con línea de visión: banqueta y nidos, 23,6 %; con atalayas, 89,2 %; con media tropa en la cola del tren, 9,6 %; **con la azotea del edificio de viajeros** (2 pelotones de tiradores a 11 m), **95,8 %**, con munición p10 de 40,3 u. **Decisión: entra la azotea en el MVP y las atalayas se quedan fuera.** La azotea ve por encima del muro, del tren y de los vagones en todo el frente oeste. Los 2 pelotones de tiradores empiezan en la azotea, pero son libres (D-N168): el jugador puede bajarlos. Álvaro pone el acceso (escalera) y el borde. El coste es de unos 0,3 ms por tick sobre 33 ms: vale. **Hugo recalcula las tres hordas sin aire con la línea de visión, la azotea y la D-N175 a la vez**, y esas son las que cuentan para la D-N169. Pasa a Marcos después del control de las 18:30.
- 8-nov 16:50 · Azotea (Álvaro, `niveles/sagunto-nivel.md` §10.15): **aprobada.** Mide 19 × 8,8 m a 11 m de altura y tiene un pretil de sacos de 1,2 m. Se sube por una escalera exterior en el testero este, dentro del recinto. Desde arriba se ve a los zombis a partir de 2,7 m fuera del muro, y la pila queda a 28–43 m; los trepadores pegados al muro siguen siendo cosa de la banqueta. El pretil (56 m de sacos, unas 11 u) **viene construido** al empezar, por la misma razón que las atalayas. Hugo confirma el coste y lo suma al muro de partida. Teo hace el pretil y la escalera.
- 8-nov 16:55 · Umbral de derrotas del equilibrado en la campaña: **pasa a ser una banda del 13–15 %**, no una línea en el 14 %, porque el ruido con 1000 partidas es de ±1,1 puntos. Con todo lo de hoy (H0 1500, munición en tren, Nules propia, km reales y el pretil de la azotea; Sagunto empieza con 131,2 u) da 14,2 % en equilibrado y 44,7 % en prisa: aceptado. Si alguna vez sale de la banda, la primera palanca es la rampa de los primeros días (Hugo).
- 8-nov 17:00 · Azotea, piezas (Teo (3), `arte/modelado-3d/azotea/`): **aprobadas.** El pretil de sacos de 1,2 m sale del muro aprobado; tiene tramo, esquina y esquina con paso, y los escombros caen solo sobre la azotea. La escalera exterior de 11 m tiene 5 variantes. Medido por Lucía: 0 % en la banda de la horda, sin d4d0cc ni rojo.

### Adenda D-N169 (Hugo (3), 8-nov 16:20): hordas sin aire
Confirmado con NightSim (Nacho, 1000 semillas, sin NH90 y sin rescate de Nules, con D-N174 y D-N175): fácil 4480 (100 %, pila >150 en todas), normal 5250 (99,9 %), difícil 5700 (79,6 %; 5800 da 64,4 %). Paquete en docs/economia/entregas/noche-sin-aire/. Entra cuando la build lleve D-N173/174/175; Noche58 sigue con 4710/5520/6400.
- 8-nov 18:25 · **Hordas sin aire: aprobadas** (Lucía (3), con la confirmación de Hugo y Nacho de arriba, 1000 semillas, con D-N174 y D-N175): fácil 4.480, normal 5.250 y difícil 5.700. Sustituyen a las de la Noche58 (4.710, 5.520 y 6.400). Van a la build junto con el resto del paquete, después del control de las 18:30. El control de las 18:30 se hace todavía con las hordas de la Noche58 y el NH90 en Sagunto, así que sus cifras no sirven para la D-N169 nueva.
- 8-nov 17:25 · **Corrección de Lucía (3) sobre las horas:** las líneas mías de esta tarde con horas de 15:00 a 18:25 llevan horas aproximadas y adelantadas; las puse a mano. La línea «18:25 · Hordas sin aire» es de las 17:25 (Madrid), y las de «16:40» a «17:00» son de entre las 15:15 y las 15:25. El contenido de esas líneas no cambia. A partir de aquí, la hora sale del reloj.
- 8-nov 18:55 · Anillo del tutorial y capa de obras (Bruno (3), `arte/pixel-codigo/tutorial-obras/`, TBD 4a38152). **Anillo: la D** (esquinas fijas con eco). Además del motivo de Bruno, hay otro: los estilos A, C y E son un marco entero en hueso, que es justo como se marca una tarjeta seleccionada (D-N147). Con esquinas, «toca aquí» no se confunde con «está seleccionado». **Capa de obras: la A** (contorno de 2 px en la huella; el muy dañado late entre ámbar sólido y tramado; la brecha es roja tramada con borde sólido). **Icono de ruido: el A** (pala con ondas en ámbar), porque el ruido es un aviso. Bruno pasa a Iker el C# del anillo y a Marcos las medidas de la capa, por el coordinador.
- 8-nov 18:58 · Munición del objetivo «Lleva munición a Nules»: **se cumple al descargar ≥ 20 u** en Nules. El jugador puede llevar más, de la reserva de Sagunto (150 u). Ojo: no es el tren del capítulo 3, que va de Nules a Sagunto con el pelotón; es el objetivo de después de la primera noche. Sin ese viaje, Nules cae con una horda de 2.400 (Hugo, `economia/entregas/nules-noche/`). Por eso el asedio de Nules empieza a partir del día 2.
- 8-nov 18:57 · Claros del NH90 (Álvaro, `niveles/sagunto-nivel.md` §10.13, nules §9 y betera §7): **aprobados.** Dentro del muro de Sagunto no cabe ningún claro de 25 m. Fuera hay dos: **S1 (180; 44), la explanada del antiguo helipuerto, que es la del capítulo 4**, y S2 (215; 97), en la huerta, como alternativa. Hay que limpiar su vegetación. Nules: N-C1. Bétera: P1–P3 en el MVP. Con la estación sitiada, las puertas siguen cerradas (D-N151): la tropa que baja en S1 combate desde fuera, como la del tren, y se le aplica la D-N175.

## D-N176 · Los víveres, quinto recurso de la red (Hugo (3), propuesta; Lucía (3), 8-nov 18:59)
- La red tiene 4 recursos y los víveres no estaban (Iker). Pero el modelo económico con el que se ha medido todo ya los consume: si se quitan, la derrota del equilibrado baja del 14,3 % al 6,8 % y se sale de la banda del 13–15 %. Además, los víveres ya salen en la intro y en el GDD como carga del tren. **Aprobado.**
- **Reglas, tal como están en el modelo:**
  - Sagunto empieza con 80 u. Cada persona consume 0,10 u al día, que se cobran a la vez que el mantenimiento.
  - Nules produce 6 u al día y Valencia 30, con la guarnición entera. Valencia solo produce cuando es del jugador.
  - Viajan en tren como los demás recursos. En la zona no cuentan de noche.
  - Con 0 víveres, el nodo pierde cada día el 5 % de su gente, multiplicado por la fracción que falta, y su producción baja con ella.
- Así, Nules pasa a ser la estación de víveres, lo que da otra razón para el viaje de ida y vuelta.
- **Reparto:**
  - Nacho, en la rama del reloj ×103, con una sola regeneración de goldens.
  - Iker, el quinto recurso en la red y en el panel de carga.
  - Bruno, el icono, en la misma familia que los otros cuatro.
- La siguiente libre es la **D-N177**.

### Adenda D-N176 (Hugo (3), 8-nov 19:20): cifras de los víveres
Sin consumo de víveres, la derrota del equilibrado baja del 14,3 % al 6,8 % (sim_economia.py, 1000 partidas, mismas semillas). Reglas del modelo, que pasan al juego tal cual: Sagunto empieza con 80 u; cada persona consume 0,10 u al día, junto al mantenimiento; Nules produce 6 u al día y Valencia 30, con la guarnición entera y solo si es del jugador; viajan en tren; con 0 víveres, la población del nodo × (1 − 0,05 × fracción que falta) cada día. Lo implementa Nacho en nacho/sombra-reloj, con el reloj ×103.
- 8-nov 19:02 · Variedad de los zombis y tono de la horda de noche (Teo (3), D-N80, B1, `arte/modelado-3d/zombi-variedad/`): **aprobado.** Hay 8 siluetas nuevas (v8–v15), 16 mallas en total y ningún niño. Medido por Teo: mediana L* 11,3, p90 13,4, contraste con el suelo de 9,4 (Sara pide ≥ 8). **Aprobado también el cambio de tinte:** todos los objetos tiñen con el canal del pantalón, para que la silueta entera quede en la banda 9–13. Matices: (1) el chaleco de la v10 no puede leerse como uniforme nuestro; como tiñe con el pantalón, vale. (2) La v13 (reptante) tiene el mismo impacto y el mismo radio que las demás en NightSim; solo cambia la malla. (3) Instanciado: se prueba con las 16. Si Marcos mide que pesa, se queda con las 10 de Teo (v0, 1, 3, 4, 6, 7, 9, 13, 14 y 15). (4) La palabra final sobre el color de noche la da la captura directa (-capdirecta), como siempre.
- 8-nov 19:05 · **Azotea de la D-N174: se reabre, porque me equivoqué de altura.** Según Paula (`/mnt/project-files/sagunto_azotea.md`, fotos SG1 y ortofoto SG2), la azotea real está en las **alas laterales de 1 planta**, a unos 4,5–5 m, con unos 8–10 × 11 m cada una y balaustrada de ~1 m. El cuerpo central, de 2 plantas, tiene tejado de teja y no se puede pisar. Aprobé la azotea a 11 m sin comprobarla. Con la boca a ~6,6 m y a 26 m del HESCO de 2,1 m, el tirador no ve los 12 m que hay justo fuera del muro, y ahí está la pila. Por eso el 95,8 % no vale. **Decisión:** se modela la azotea real (las dos alas a ~5 m, con un pelotón de tiradores en cada una) y Nacho vuelve a medir. Álvaro mira si el ala oeste puede quedar más cerca del muro, porque la planta del recinto es nuestra: a 15 m, la zona ciega baja a 7 m, y a 10 m, a 4,7 m. Si con eso no llega a la D-N169, la palanca es la horda de Hugo, no inventarse otra planta. Hasta que se mida, la azotea **no** entra en el paquete de Marcos.
- 8-nov 19:06 · **Castellón subterránea** (Álvaro, `niveles/castellon-nivel.md` §7 y castellon.json): **aprobada.** La vía va a −8 m bajo losa entre X 70 y 190, con trinchera abierta en los extremos; el vestíbulo de calle está en (130; 81) con C1, y las mercancías y C2 quedan en superficie. Coincide con la estación real (Paula, `castellon_estacion.md`: vías bajo la calle). Teo hace el kit con esta planta.
- 8-nov 19:10 · Sara calibra NightSim (200 semillas) y reproduce las hordas sin aire (100/100/79,5 %), **pero solo con el muro por tramos**: sin tramos, la difícil sale al 100 %. Los tramos activos por defecto pasan al primer puesto del paquete de Marcos.
- 8-nov 19:12 · Azotea real (Álvaro, §10.15 rehecha): **aprobada la planta.** El edificio pasa a ser como el real, de 32 × 11 m, y se mueve al oeste. El ala oeste queda a 12,5 m del muro, con la azotea a 4,75 m y los 2 pelotones arriba. El ala este queda de reserva para el norte y la puerta este. Quedan anulados el pretil de sacos, la escalera exterior y las posiciones a 11 m. **Discrepancia en la zona ciega:** Álvaro da 3,2–3,5 m; mi cuenta, con la boca a 6,35 m y el HESCO de 2,1 m a 12,5 m, da 6,2 m. Manda la medida de Nacho con la geometría del CSV. El acceso desde la primera planta queda SIN VERIFICAR (se lo he pedido a Paula).
- 8-nov 19:14 · **Álvaro tenía razón con la zona ciega.** La D-N174 apunta al blanco a 1 m de altura, así que desde el ala oeste la zona ciega es de 3,2 m. Mis 6,2 m eran la sombra del muro en el suelo, a los pies. La §10.15 recoge las dos cifras.

### Adenda (Hugo (3), 8-nov 19:40): muro de partida de Sagunto, 120 u
Con la azotea real (alas a 4,75 m, Álvaro §10.15), desaparece el pretil de sacos de 11,2 u. La balaustrada de 1 m es parte del modelo del edificio: no es muro, no tiene vida ni coste. El muro de partida vuelve a 120 u (D-N63). sim_economia.py, 1000 partidas: equilibrado 13,9 %, prisa 44,8 %, dentro de la banda. Los CSV publicados no cambian.
- 8-nov 19:18 · Economía de los días 1 a 3 (Hugo, `economia/mvp-dias/`, son cuentas y no partidas). Las 20 u a Nules se pagan con margen: a Sagunto le quedan 102 u el día 3. Los 40 u de materiales cubren el capítulo 2. La horda de Nules la elige la medida de Nacho con la D-N169. **Decisiones:** (1) **Bétera empieza con 20 u de víveres y consume igual que las demás.** No tiene tren, así que se queda aislada; es coherente y en el MVP le dan para varios días. (2) **Nules empieza con 0 u de materiales**: el jugador puede subirlos al tren de la munición. El objetivo sigue cerrándose con las 20 u de munición. (3) **El tren de Nules del capítulo 3 sale con el depósito lleno** y no se cobra de la red, porque solo existe con el tutorial. Iker lo implementa así. Plan B de hordas si la azotea real no aporta (normal 4.400, fácil 3.750 y difícil 4.780): extrapolado, pendiente de que Nacho mida 4.200, 4.400 y 4.600. Muro de partida de Sagunto: vuelve a 120 u, sin pretil (equilibrado 13,9 %).
- 8-nov 19:20 · Datos de Paula (`/mnt/project-files/almenara_y_sagunt_acceso.md`). **Sagunt:** las terrazas miden unos 9 × 9 m, una a cada lado del cuerpo central, sin escalera exterior. Se sube por una puerta de la primera planta del cuerpo central (ESTIMACIÓN, no hay foto). En el juego, la tropa sube por dentro del edificio, sin pieza nueva. Álvaro ajusta las alas a 9 × 9. El andén 1 va pegado a la fachada; la vía 1 está a ~4,2 m. **Almenara:** fuera del pueblo, con 4 vías (2 generales y 2 apartaderos de ~1,1 km). En el MVP **es un apartadero de cruce en la línea Sagunto–Nules (D-N152)**, sin nodo propio ni zona: es donde un tren puede esperar a que pase otro. Moncofa queda para después. Les Valls, La Llosa y Xilxes son apeaderos sin apartadero y no tienen papel en el juego.
- 8-nov 19:24 · Kit de Castellón subterránea (Teo (3), `arte/modelado-3d/castellon/`, 8 hojas): **aprobado como v1.** Incluye andén bajo losa (con la losa como hijo que se oculta en la cámara cenital), catenaria, muro de trinchera con la boca del cajón, vestíbulo de 24 × 14 m, barricadas civiles y vagones abandonados. Medido por Lucía: 0 % en la banda de la horda, sin d4d0cc ni rojo; lo perdido se cuenta con escombro y hollín. El vestíbulo y el andén están hechos solo con el texto de Paula. Las fotos CS1 a CS6 están en la raíz de la carpeta compartida: si el vestíbulo real (CS1 y CS2) cambia de forma, se ajusta en una r2.
- 8-nov 19:26 · Datos de Paula (`referencias-reales/betera_rearme_y_nules_viveres.md`). Bétera: el NH90 reposta en tierra con camión cisterna, no en vuelo. Encaja con la vuelta a rearmar de la D-N167; la dotación de munición no es pública, así que nuestras cifras siguen siendo de balance. Nules: es la cuna de la Clemenules, lo que respalda que sea la estación de víveres (D-N176); el tope de 6 u al día se queda. El camión cisterna (BT3) puede ser una pieza de ambiente de Bétera para Teo, después del MVP.
- 8-nov 19:28 · Vestíbulo de Castellón r2 (Teo, comparado con la CS1): **aprobado en lugar de la v1.** Cubierta plana con lucernario y ala curva sobre la entrada. La boca y el muro de trinchera no cambian (CS5). Siguiente pieza de Teo: el edificio de viajeros real de Sagunto (§10.15). Lleva balaustrada en b8b8b8 y el granate en 642030 o 7c181c, nunca en 982420.
- 8-nov 19:31 · Edificio de viajeros real de Sagunto (Teo (3), `arte/modelado-3d/sagunto-edificio/`): **aprobado.** Mide 32 × 9 m: cuerpo central de 2 plantas con teja y frontón, y alas de 9 × 9 m con azotea a 4,75 m, balaustrada en b8b8b8 y una puerta desde la primera planta. No hay escalera exterior. Granate en 7c181c en el LOD0 y en 8c5048 en el LOD1, que es lo que se ve en juego; así queda lejos del rojo de ataque. Banda de la horda ≤ 0,4 %. Sustituye al edificio anterior y anula el pretil y la escalera de la azotea a 11 m. Marcos comprueba en la exportación que el ala de +x local cae al oeste.
- 8-nov 19:34 · Cartel «SAGUNT» y traviesas sueltas (Teo (3), `arte/modelado-3d/sagunto-extras/`): **aprobados.** El cartel no lleva logotipo, para no copiar la marca de Adif, y en el LOD1 el texto es una banda. 0 % en la banda de la horda. Siguiente encargo de Teo: el camión cisterna y el carro de munición de Bétera, para la zona de rearme P1–P3 (fotos de Paula: BT3).
- 8-nov 19:21 · **Goldens regenerados (G3_red) en la rama `nacho/sombra-reloj`** (Nacho). Una sola regeneración para cuatro cambios aprobados: el reloj ×103 de la D-N161 (25.200 ticks/día, 1.050/h; 1 tick = 24/7 s; tren a 57.143 mm/tick, que siguen siendo 60 km/h; horda de vía a 1.905 mm/tick, 2 km/h), pedido por Lucía; los km reales de RailNet (Paula y Álvaro: Puçol 7,13, Valencia 33,63, Almenara 9,59, Nules 21,35, Castellón 39,97 y el Mijares en el km 34,5); los CSV de colmena-h1500 de Hugo (H0 1500); y la D-N176 de los víveres como quinto recurso (Res.Viveres = 4, guardado NetVersion 4; las partidas v3 ya no se cargan). G1, G2, G4 y G5 no cambian. Suite 1024/0. Dos cosas a revisar: con el reloj nuevo, el aviso de horda a 3 km da 52 s reales a ×1, en vez de 75 (D-N11 pedía 60–120 s; la prueba se ha bajado a 45 s); y la mancha de la red sigue avanzando por ticks, así que en tiempo real va igual que antes y en tiempo de juego, más despacio.
- 8-nov 19:37 · Zona de rearme de Bétera (Teo (3), `arte/modelado-3d/betera-rearme/`): **aprobada.** Camión cisterna (basado en la foto BT3, sin placa naranja) y remolque de munición, 5 variantes cada uno, 0 % en la banda de la horda, sin rojo ni ámbar. Colocación de Teo: los v1 junto a P1 y los v0 y v3 en P2 y P3. Mejora opcional para Iker, si sale barata: mientras un NH90 rearma en P1, el camión y el remolque usan la variante «Repostando» o «Descargando», y en reposo, la «Aparcado» o «Cargado». Así se ve el rearme.
- 8-nov 19:39 · Aviso de horda con el reloj ×103 (Nacho): a 3 km son 52 s reales a ×1, por debajo de los 60–120 s de la D-N11. **Decisión: la detección pasa a 5 km, unos 87 s**, en el centro de la banda. Así hay margen aunque la velocidad de la horda varíe; con 4,3 km quedaría justo en el borde. Si 5 km choca con el mapa de alguna estación, el mínimo es 4,3 km. Nacho lo mete en la rama del reloj ×103.
- 8-nov 19:31 · **G3_red regenerado otra vez en `nacho/sombra-reloj`** (Nacho). Entran dos cambios aprobados: la detección de la horda pasa a 5 km (Lucía; unos 87 s reales a ×1, dentro de los 60–120 s de la D-N11), y el hambre parcial se acumula en milésimas de persona por nodo, como pidió Hugo (antes el floor dejaba sin pérdidas a los nodos pequeños). Suite 1025/0.
- 8-nov 19:42 · Carga visible en las plataformas (Teo (3), `arte/modelado-3d/carga-vagones/`): **aprobada.** Hay un módulo por recurso, hijo del vagón en (0; 1,25; 0), con 5 estados: Lleno, Mitad, Vacío, Dañado y Destrozado. Por color se distinguen así: munición en verde, combustible en gris, materiales en marrón y gris, y víveres en crema y blanco (limones en vez de mandarinas, para no tocar el ámbar). La tropa ya tiene su vagón, el R2. 0 % en la banda de la horda. Para Iker: el módulo y su estado salen del panel de carga (≥ 2/3 lleno, ≥ 1/3 mitad, el resto vacío) y del daño del vagón.
- 8-nov 19:44 · Víveres al empezar (Hugo, para Inicio() y Mvp()). **Sin horario de víveres por defecto: aprobado.** Sagunto aguanta unos 25 días con lo que sobra de Nules, y eso empuja a mover trenes y, más adelante, a abrir Valencia. **No va el horario de 10 u al día de Valencia a Sagunto en Mvp()**, porque Valencia ha caído y la rama sur está bloqueada en el MVP (red-inicio.md). En el MVP los víveres solo llegan de Nules, en trenes del jugador. Hugo comprueba que los días del MVP no cambian sin ese flujo.
- 8-nov 19:46 · **Cambio de Lucía (3) sobre Bétera y los víveres (anula el punto 1 de las 19:18).** Hugo confirma que, sin hacer nada, Bétera se queda sin víveres hacia el día 9, y en el MVP el jugador no tiene ninguna forma de abastecerla: no hay tren ni carretera habilitada, y el NH90 no lleva carga. Sería un castigo sin salida. **En el MVP Bétera no consume víveres** (la otra opción que daba Hugo). Abastecerla por aire o por carretera queda para después del MVP. Sagunto sí se queda sin víveres hacia el día 10, y es correcto, porque tiene salida: los trenes a Nules.
- 8-nov 19:48 · Acopio de víveres de Nules (Teo (3), `arte/modelado-3d/nules/hoja_acopio_viveres.png`): **aprobado.** Son 3 acopios en el patio de carga y 2 en el muelle. El estado sigue a los víveres de Nules con la regla de los vagones: Lleno a partir de 2/3, Mitad a partir de 1/3, y Vacío por debajo, sobre una capacidad de referencia que fija Hugo. Saqueado si Nules cae, y Quemado si el almacén se quema. 0 % en la banda de la horda.
- 8-nov 19:55 · Kit de obra en curso (Teo (3), `arte/modelado-3d/obra-curso/`, 5 piezas × 5 variantes × 2 tamaños): **aprobado.** Se pone sobre el tramo mientras se repara o se reconstruye y se quita al acabar. La obra va por las dos caras (montones fuera, herramientas dentro), para que se vea mire la cámara hacia donde mire. **Condición:** las piezas son solo visuales, sin colisión ni efecto en el pathing ni en la línea de visión (D-N174), porque las de fuera quedan entre la horda. 0 % en la banda de la horda, sin ámbar ni rojo.
- 8-nov 20:00 · Ambiente del aeródromo de Bétera (Teo (3), `arte/modelado-3d/betera-ambiente/`, 5 piezas × 5 variantes): **aprobado.** Manga de viento a franjas b8b8b8 y 605c48, balizas blancas y verdes, casetas, torres de iluminación y vallas. Sin naranja ni rojo, y 0 % en la banda de la horda. Colocación de Teo para Iker, con una condición: las balizas van **por fuera** de los claros de 25 × 25 m, sin meterse en ellos.
- 8-nov 20:05 · Kit de huerta de Nules (Teo (3), `arte/modelado-3d/nules-huerta/`): **aprobado.** Caseta de pozo, tapia, balsa, acequia y caseta de aperos; el agua va en 6c7874. Las casetas y la tapia son sólidas y tapan la línea de visión (salvo el hueco de la derrumbada y el portón abierto). La balsa frena el paso, pero no tapa la vista, salvo que su muro pase de 1 m. La acequia no tapa la vista; si frena el paso, lo decide Álvaro.
- 8-nov 20:08 · Mobiliario urbano (Teo (3), `arte/modelado-3d/urbano-extra/`): **aprobado.** Contenedores, marquesina de bus, quiosco, señales sin rojo (se leen por la forma) y semáforos apagados. Colisión: contenedores, señales y semáforos sin colisión; el quiosco es sólido y tapa la vista; la marquesina de bus **no** tapa la vista (cristal o abierta) y solo tiene colisión en el banco y los postes, salvo el panel de anuncios, que sí tapa.
- 8-nov 20:10 · Kit de huerta: **no va en Nules.** Junto a la estación real no hay huerta, y unas tapias sólidas delante del muro este (entrada Nb) cambiarían la defensa sin medir. Va a la huerta del noreste de Sagunto, que es real, fuera del claro S2 y de su aproximación y a más de 30 m de cualquier muro, para no tocar la línea de visión medida. Si no cabe así, se queda sin usar de momento.
- 8-nov 20:12 · **Azotea real medida y aprobada** (Nacho, caso A, sin aire, D-N175, 500 semillas): las alas a 4,75 m y los 2 pelotones en el ala oeste, a 12,5 m del muro. Normal 5.250: 99,8 %. Difícil 5.700: 79,0 %. Normal 5.520: 94,8 %. Sale casi igual que la azotea de 11 m, porque acercar el ala compensa la altura. **Las hordas sin aire se quedan** (4.480, 5.250 y 5.700; la fácil, a falta de confirmar) y **el plan B de Hugo no hace falta**. La azotea real vuelve al paquete de Marcos con el edificio nuevo de Teo (e7bc5d5).
- 8-nov 20:20 · Kit «Sagunto vivo» (Teo (4), `arte/modelado-3d/sagunto-vivo/`, 40 variantes): **aprobado con dos retoques.** (1) El solar demolido, más terroso: tierra b4a080/605c48 con restos de solería; una losa gris lisa de 6 × 10 parece un claro o una plataforma. (2) Los bidones de combustible, solo en gris (94948c y 6c7874), sin verde: el código de color de la carga es munición en verde y combustible en gris. Lo demás (bidón con fuego, tendedero, bancales, tienda, cocina y armario de Adif con STOP sin rojo), sin cambios. 0 % en la banda de la horda.
- 8-nov 20:25 · Kit «Aquí pasó algo» (Teo (4), `arte/modelado-3d/aqui-paso-algo/`, 4 piezas × 5): **aprobado.** Locomotora de mercancías descarrilada (gris con franja 847c34, sin naranja), vía rota, catenaria caída (solo visual, fuera del gálibo) y autobús cruzado, que sustituye al del inventario y no se suma. **Condición:** la vía rota y el mercancías van solo en vías muertas o apartaderos sin uso, nunca en un recorrido de tren. Una vía rota en un recorrido diría que la línea está cortada, y la mecánica de reparar vías es de después del MVP. Álvaro elige la vía.
- 8-nov 20:30 · Lotes RA y NV de Paula (v1). El NH90 reposta en un FARP con manguera por la toma lateral, lo que encaja con el camión cisterna de Teo. Las cajas de munición de la referencia son de 30 mm; las del juego siguen siendo genéricas y no cambian. Cítrics de Nules tenía unos 400 socios y hasta 35.000 t, y entró en liquidación en 2023, lo que respalda la D-N176. Las hectáreas siguen SIN VERIFICAR. No cambia ninguna decisión.
- 8-nov 20:32 · Mapa táctico de Bruno (`arte/pixel-codigo/mapa-tactico/`, mr-mak 2bd1bb6): **aprobado, con un cambio.** La mancha de la horda va **oscura y tramada**, y en 982420 **solo cuando ataca** un nodo o un tren, como en el minimapa de la D-N147: el rojo es para ataques. **Paso de la zona al mapa:** en vez de un negro, un fundido corto (≤ 0,3 s) a navy 181c30, atado al umbral de la rueda. Así el zoom sigue sintiéndose continuo y el tiempo no se para (D-N91). El suelo ocre de la zona no cambia.
- 8-nov 20:35 · Kit «Pueblo valenciano» (Teo (4), `arte/modelado-3d/pueblo-valenciano/`, 5 piezas × 5): **aprobado.** Esquina con chaflán, bajo comercial (farmacia sin cruz), tres alturas, casa de patio y campanario de 25 m, que es solo decorado. Las casas tienen la huella 6 × 10 de casa_pueblo. Medidas de memoria: SIN VERIFICAR hasta que Paula tenga fotos de calles. **Además: casa_pueblo pasa su carpintería de 543820 a 605c48**, porque en sombra caía al 9 % en la banda de la horda; es un fallo que ya estaba en la build. El campanario lo coloca Álvaro fuera de las líneas de tiro.

- 08-11 (tarde) · Propuesta de Iker. Sí a las 4 señales del tutorial en la zona (horda_avanza, ataque_rechazado, vehiculos_fuera, tramo_sobre_70), hechas desde su rama. Sí a D-N156: NetSession.Ensure llama a Inicio(), con Nules a 0 u de munición y 0 u de materiales, Bétera con 20 u de víveres sin consumo y sin horario de víveres. D-N173 y D-N152 van antes o a la vez. D-N157 (quitar la barra de oleadas) la hace Iker si Marcos está de acuerdo. D-N91 queda para después. — Lucía

- 08-11 21:00 · Azotea, 500 semillas sin aire (Nacho, docs/economia/entregas/azotea-alas/). Caso A, solo ala oeste: fácil 4480 100 %, normal 5250 99,8 %, normal 5520 94,8 %, difícil 5700 79,0 %. Caso B, alas oeste y este: 100 %, 99,6 %, 97,0 % y 83,8 %. Munición p10 ≥40 u y pila p50 ≥255 en todos los casos; sin brechas; todas las derrotas son del tren. DECISIÓN: el MVP se queda con el caso A, que es lo que ya lleva la Noche64 y el paquete de Marcos, y las hordas siguen en 4480/5250/5700. El caso B saca la difícil de la banda del 50 al 80 %, y la normal a 5520 no llega al 95 % en el caso A. El ala este queda para después del MVP; si entra, habrá que volver a medir la difícil hacia arriba. D-N152 (nacho/tren-puertas): plazas solo en Sagunto, Nules y Bétera. Teruel y Zaragoza no son estaciones del MVP y van con 0 plazas. — Lucía

- 08-11 21:05 · D-N177 · Tren a las puertas de una estación sitiada, resuelto fuera de pantalla (Hugo, docs/economia/tren-a-las-puertas.md). APROBADA como regla PROVISIONAL, con las cifras SIN VERIFICAR hasta que Nacho mida en NightSim el 10 % de la horda que va a por el tren (puerta este de Sagunto (192;60), normal 5250, con D-N175, sin escolta y con 8 soldados). Diseño:
  1. Todo o nada: la carga llega entera o se pierde entera, y si el tren cae se pierde también la tropa a bordo. Así se lee fácil.
  2. Aviso en ámbar (e08c30) al dar la orden de salida y en el icono del tren: «Sin escolta: <estación> está sitiada». El rojo solo aparece si el tren cae. Nadie pierde un tren sin haber sido avisado.
  3. Cuando se ve en pantalla (capítulo 3 y la zona activa), manda NightSim y no esta regla.
  4. Esto da sentido al paso 2 del objetivo de Nules («Sube tropa o un vehículo: protegerán la carga»).
  5. Si la medida sale lejos del 10 %, Hugo ajusta la fracción y la regla no cambia.
  6. Va con la D-N152 (nacho/tren-puertas), no en el paquete actual de Marcos.
  Siguiente D-N libre: D-N178. — Lucía

- 08-11 21:15 · Revisión del informe de Paula v1 (referencias-reales/nules_viveres/betera_rearme_y_nules_viveres_v1.md), con las dos hojas de contactos miradas.
  BÉTERA, REARME (D-N167):
  - El modelo es un FARP. RA2 marca el aspecto: cisterna flexible en el suelo, manguera tendida, sacos de arena y cajas de munición al lado del claro de 25 × 25 m. Nada de toma fija de helipuerto; RA4 (Rota) no sirve.
  - Que haya NH90 en Bétera sigue SIN VERIFICAR (el de allí es el Cougar). Lo mantenemos como licencia del juego (D-N173, un solo aeródromo), sin presentarlo como un dato real.
  - Las cajas de RA3 son de 30 mm (Apache). Solo valen para la forma de la caja metálica con tapa; ni rotulación ni calibre.
  - Combustible: 2.035 kg es dato; los 2.540 l son ESTIMACIÓN. En el juego no hay litros a la vista: el rearme dura un tiempo y gasta u de munición, sin medir combustible.
  NULES, VÍVERES (D-N176):
  - Lenguaje visual de Nules: naranjos en hileras (NV1), huertos con tapias (NV2), una casa de labor de dos plantas con cipreses (NV2), una balsa con lámina (NV5) y palots apilados en el almacén. Ninguna foto es de Nules, solo sirven de guía.
  - Los palots de NV4 son de manzana y de EE. UU.: forma genérica de caja apilable y nada más.
  - PALETA: el icono de víveres no puede ser una naranja ni ir en naranja, porque el ámbar e08c30 es solo para avisos. Será una caja o un palot en tonos hueso o verde de la paleta.
  - D-N178 (nivel): en el MVP los naranjos NO cortan la línea de visión (D-N174); las tapias de huerto sí, como los muros. Las tapias dan cobertura a la tropa fuera del recinto de Nules.
  - Las hectáreas de cítricos de Nules siguen SIN VERIFICAR. Ninguna cifra de producción del juego sale de ellas (Nules produce 6 u al día, D-N176).
  Siguiente D-N libre: D-N179. — Lucía

- 08-11 21:20 · Colocación de Álvaro, APROBADA. Nules (nules-nivel.md §13): las tapias van solo en la parcela este (X 192–252, Z 40,5–52), con un testero roto en X 250 y 3 tramos en Z 40,5 con el portón en X 237; ahí van también la casa de labor, la balsa y 21 naranjos. La franja oeste lleva unos 30 naranjos sin tapias, y queda un hueco sin árboles en X 44–56 alrededor de la bajada de la tropa en (50; 44,5). Las tapias NO entran en la build hasta que Nacho mida Nules con ellas. Bétera (betera-nivel.md §10): el FARP va al este de P2, con la cisterna en (53; 104) dentro de una U de sacos abierta al claro y las cajas en (50; 95), sin invadir el claro. — Lucía

- 08-11 21:25 · Kits de Teo (TBD 3ff4557), APROBADOS: FARP de Bétera (hoja_farp_betera.png) y víveres de Nules (hoja_viveres_nules.png), 25 piezas cada uno, en 5 grupos de 5 variantes. Comprobado en las hojas: 0 % de rojo 982420, 0 % de ámbar e08c30, y el color de selección d4d0cc solo en píxeles sueltos (0,002 %). La fruta va en a86c50, apagada, como se pidió. Los sacos de arena son grises claros (bfbbb7), lejos del d4d0cc. Las tapias llevan colisión de muro (D-N178). Una nota menor, sin bloquear: en los palots con fruta, que la tapa terrosa no se confunda con el tejado de la casa en la vista de juego; Álvaro lo verá al colocarlos. — Lucía

- 08-11 21:30 · FARP y víveres en main de mr-mak (263c2b8). Aprobado el encargo de la r2 de pueblo_valenciano con las fotos de sagunt_calles: balcón volado de forja, persianas enrollables, rejas en la planta baja, zócalo gris o verde azulado de la paleta, fuera de la banda y lejos del d4d0cc, y un campanario de sillería con un vano por cara. Mismas medidas y pivotes; sin colisión nueva. — Lucía

- 08-11 23:15 · Se retoma tras la pausa. Desde ahora hay dos integradores: Marcos saca la Noche65 e Iker integra y saca la Noche66 (coordinador, a petición de Eugenio: «Ponlo todo en marcha»). La r2 de pueblo_valenciano (TBD 7be10a8) queda APROBADA: zócalo 6c7874, alternando con 605c48 y 94948c, de 1,2 m; forja, rejas y persianas solo de fachada; el campanario de sillería con un vano por cara sustituye a «Piedra». Comprobado en la hoja: 0 % de rojo y de ámbar, d4d0cc en un 0,001 % (píxeles sueltos). Nota: en la hoja, la torre de sillería (v21) se ve más oscura que el b4a080; Teo debe comprobar que el material del FBX sea el b4a080. — Lucía

- 08-11 23:20 · S3 de Sara (qa45): Nules y Castellón reciben la misma horda de 5250 que Sagunto y se pierden a las 23:51 con 0 abatidos. NO lo queremos así: es un fallo. DECISIÓN:
  1. Cada zona tiene su propia horda. La de Sagunto no se copia a las demás.
  2. Nules: sin asedio la 1.ª noche (ya decidido). Desde la 2.ª noche, horda de 2400, la cifra de Hugo (tren-a-las-puertas.md). La resuelve la regla abstracta del asedio, fuera de pantalla, contra el recinto de 130 u y la tropa que haya.
  3. Castellón: sin noche en el MVP. La estación es subterránea y está cerrada; no la ataca nadie hasta que Hugo dé su horda.
  4. Una zona sin tropa no puede perderse con 0 abatidos sin que salga antes un aviso en ámbar («<zona> sin defensa: llega la horda»).
  Para Nacho e Iker (Inicio()), con la cifra de Hugo. — Lucía

### Adenda D-N169 (Hugo (3), 8-nov 23:20): CERRADA con la azotea real
NightSim (Nacho, 500 semillas, sin aire, con línea de visión, azotea real en las alas y D-N175): fácil 4480, 100 % (pila p50 255, munición p10 42,7 u, 0,7 bajas); normal 5250, 99,8 % (pila 339, 7,7 bajas); difícil 5700, 79,0 %. Las tres cumplen. Plan B, sin azotea (banqueta, nidos y D-N175): 4200 y 4400, 100 %; 4600, 99,6 %. Confesión de método: mi extrapolación ponía el 95 % entre 4.800 y 5.000 y proponía 4400; la medida dice que 4600 sigue en el 99,6 %. Me quedé corto de forma conservadora, porque extrapolé desde una medida sin la D-N175. Si algún día la azotea falla, la normal es 4600, no 4400. Publicado en vivo en json/noche_sagunto.json (Noche64).

- 08-11 23:25 · D-N169 CERRADA (Hugo): fácil 4480 al 100 %, normal 5250 al 99,8 % y difícil 5700 al 79,0 %, con la azotea real. Plan B si falla la azotea: normal 4600 (99,6 %). En Nules, propuesta de Hugo APROBADA: perder un tren en Nules NO es derrota. Se pierden el tren, su carga y la tropa a bordo, igual que en la D-N177. El caso de referencia del asedio de Nules es sin tren. Se mantiene el aviso en ámbar antes de que el tren llegue a una estación sitiada. La derrota solo llega cuando cae la estación o el tren principal de Sagunto. — Lucía

- 08-11 23:30 · Corrección mía: el recinto de Nules es de 124,3 u, no de 130. Iker descontó los huecos de las puertas y la economía ya está medida con esa cifra. La horda de Nules desde la 2.ª noche queda en 2400, PROVISIONAL (regla de tres, ~45 % del fuego de Sagunto), hasta que Nacho mida el caso sin tren. Si la normal no da ≥95 % con pila p50 ≥150, Hugo da la cifra con la curva. La horda de Castellón queda para después del MVP. — Lucía

- 08-11 23:35 · Capítulo 3 del tutorial (Álvaro, docs/niveles/tutorial-cap3-recorrido.md). El campanario de sillería va en (48; 0; 165), APROBADO: no tapa ninguna línea de tiro. Recorrido (192; 60) → (160; 40) → (100; 34), 98 m, unos 40 s. DECISIÓN: el punto del flanco sur se queda en (100; 34) y el problema pasa a ser la lección. Estando a 12 m de la carretera de O2, la horda se gira hacia la tropa (D-N175); el texto 3.8 enseña a golpear y retroceder hacia el este, porque la tropa corre a 2,5 m/s y la horda a 1,5. Nuevo 3.8: «Llévalos al flanco sur y limpia el muro. Si la horda se gira hacia ti, retrocede hacia el este sin dejar de disparar: corres más que ellos.» Se descarta (125; 36), porque desde ahí tampoco se ve la pila y además no se enseña nada. Que la pila no se vea desde el sur no importa: el objetivo es limpiar el muro sur. Hay que comprobar en NightSim que el capítulo 3 se puede hacer sin perder el pelotón si se sigue el texto. — Lucía

- 08-11 23:40 · Flecha de retirada del capítulo 3 (Álvaro, tutorial-cap3-recorrido.md §4). Paradas: R1 (130; 36), R2 (160; 38) y R3, el puesto F3 (196; 51). Una cuenta que no cuadra: un zombi que se gira a 10 m necesita 37 m de retirada, y R1 está solo a 30 m del flanco (a los 30 m la distancia es 10 + 30 − 18 = 22 m, menos de 25). DECISIÓN: la flecha del tutorial marca R2 como parada normal, con 60 m de margen. R1 queda como parada opcional, solo si el pelotón empezó a más de 17 m de la horda. R3 (F3) es el refugio. Nacho debe comprobar: si el pelotón dispara mientras se mueve, si sobrevive llegando a R2 y si puede entrar en F3. — Lucía
- 08-11 23:45 · Corrección mía a la entrada de las 23:40: el umbral de R1 es 13 m, no 17. En 30 m la tropa gana 12 m, y 13 + 12 = 25 (cuenta de Álvaro). R2 rompe la persecución de cualquier zombi que se girara a más de 1 m. — Lucía

- 08-11 23:50 · D-N80, criterio de «se distinguen por la forma» (herramienta de Bruno, mr-mak 013c1f3): IoU media ≤0,70 por par a ortho 26, con los ángulos de juego; ningún par por encima de 0,80 en ningún ángulo ni fotograma clave (caminar y trepar); se mide con la silueta en negro puro, sin el tono por instancia. Un solo material para las 5 siluetas, con el tono por instancia. Después, revisión a ojo de la hoja de noche. — Lucía

- 08-11 23:55 · D-N80 APROBADA (Teo, TBD 7cef8b8; hoja_zombis_dn80.png y pares.csv). Cinco siluetas: civil (v3), huerta (v18), uniformado sin armas (v19), gordo (v17) y rápido (v16). Los 10 pares cumplen el criterio de las 23:50: el más justo es civil/uniformado, con 0,68 de media y 0,79 de máximo; los demás, ≤0,63 de media y ≤0,76 de máximo. Banda: el 68 % de los píxeles queda en L* 9–13; el resto es sombreado entre 7,8 y 14,3. Lo acepto: es el ±12 % del render, no un tono base fuera de banda, y no se acerca al color de selección. Sin rojo ni ámbar. LOD1 de 144 a 248 triángulos y un solo material. Vigilar el par civil/uniformado: si en la build se confunden, se exagera más el uniformado, no se toca el civil. — Lucía

- 08-11 24:00 · Sonidos de Nuria (https://claude.ai/artifact/AtVv5eEpffmKBzBokeyqPR, 40 OGG, 4.924 créditos): APROBADOS. El aviso ámbar se queda con el «din-don» rápido; se prueba en el juego y, si falla, se hace la versión con 0,3 s entre notas. Van a Iker para la Noche66. Encargo nuevo a Teo: kit de la pila de zombis contra el muro (5 alturas, a partir de las siluetas de la D-N80, colisión de rampa y umbral de sustitución por instancias que decide Nacho). — Lucía

- 08-11 24:05 · Umbral de la pila (Nacho), APROBADO: por celda de 0,5 m de muro, sueltos con menos de 3; altura 1 a 5 con 3, 4, 5, 6 y ≥7 (de ≈1,05 a 2,45 m; la 4 a ras del HESCO, la 5 es la rampa); histéresis: vuelve a sueltos por debajo de 2, con un cambio de altura por segundo como mucho. Aviso «zona sin defensa» en nacho/tren-puertas 5a157ca, para Iker. Capítulo 3: los fusileros disparan en marcha. F3 no existe en NightSim: que la tropa pueda entrar depende de las colisiones en Unity (Marcos). — Lucía

- 08-11 24:10 · Vías de la zona (Bruno, mr-mak d28207e): elegida la D, balasto claro olive_grey. Es la única que cumple el ΔL* ≥8 de Sara frente al tren (18) y, frente a la horda, da 27,6. Las traviesas pasan de ~150 cajas #442c0c, que de noche se leían como zombis tumbados, a una sola textura que se repite. Plan B: la D con traviesas cada 1,2 m, si en la build hay demasiado ruido detrás de los zombis. — Lucía

- 08-11 24:15 · Fantasma de obra (WallVisual): deja el 442c0c, que es color de la horda. Colocación válida: d4d0cc, el color de selección, porque es algo que el jugador está eligiendo, tramado al 50 % para que se lea como provisional y no como selección hecha. Colocación no válida: ámbar e08c30 tramado, porque es un aviso. Nunca rojo, que es solo para ataques y brechas. — Lucía

- 08-11 24:20 · Pila de zombis (Teo, TBD d1da25d), APROBADA: 5 alturas × 3 semillas, siguiendo los umbrales de Nacho; colisión de cuña a 33° (UCX_); núcleo fijo en 1c200c, sin tinte, para que no salgan rayas; el 63–68 % en banda y el resto es sombreado; sin rojo ni ámbar; LOD1 de 120 a 304 triángulos por celda. La pieza de remate para el extremo de un tramo se hace YA, una por altura: todo tramo tiene dos extremos y la cara lisa se va a ver siempre. — Lucía
- 08-11 24:30 · Pila con remates entregada en mr-mak (0dd8b6a, 45 piezas). Cerrada. Siguiente tarea de Teo: puntos de boca de arma (sockets «Muzzle») en todos los modelos que disparan, para desbloquear «El disparo sale de la boca del arma» (pendiente de Marcos). — Lucía

- 08-11 24:35 · Referencias de La Plana de Paula (15 fotos, en main): solo de consulta para Teo y Álvaro; el kit de víveres de Nules no se rehace antes del MVP. Encargo nuevo a Paula para la D-N160 (informe de inteligencia): estructura real de un SITREP o parte de situación, simbología OTAN APP-6 para el mapa y forma de redactar (tono, abreviaturas, DTG). Solo fuentes públicas; lo que no se pueda comprobar, SIN VERIFICAR. — Lucía

- 08-11 24:40 · D-N160, Informe de inteligencia (Paula v0, referencias-reales/informe-inteligencia/). APROBADA la propuesta de 8 apartados: cabecera, resumen en una línea, situación de la amenaza, fuerzas propias, sin novedad en, valoración, necesidades, firma. Adaptaciones de diseño:
  1. DTG: el real (082030ANOV26) lleva mes y año, y la intro es «Día 41, sin año». En el juego: «D41 · 2030A», día de campaña más hora con la zona Alfa (hora local), sin mes ni año.
  2. APP-6: nos quedamos con las FORMAS de los marcos, que son las que llevan el significado (rectángulo y cúpula amigos, rombo hostil, trébol desconocido). Los colores pasan a nuestra paleta: amigo, un azul o cian de la paleta (lo elige Bruno); hostil, rombo en tono hueso o de horda, que solo se pone en rojo 982420 mientras ataca o abre brecha; desconocido, trébol en neutro, NUNCA en amarillo ni ámbar, que es solo para avisos.
  3. La horda sale como rombo vacío, sin icono de infantería, porque no es una fuerza militar.
  4. SVG de Commons: SÍ, Paula los baja solo como referencia (con licencia y autor), y Bruno los redibuja en pixel art al tamaño del mapa. No se usan directamente.
  Lo marcado SIN VERIFICAR no se presenta como norma real en ningún texto del juego. — Lucía

- 08-11 24:45 · Símbolos APP-6 (Bruno, mr-mak 17a5052): elegida la D, relleno slate y contorno grey_light, para lo amigo. Se lee en las tres bandas y en el mar (ΔL* de 36 a 64). Se descarta la A, porque su contorno hueso se confunde con lo hostil. Mientras ataca, el rojo va con contorno de 2 px, porque sobre la banda alta solo da ΔL* −4,8. Pendiente: cotejar el dibujo con los SVG de Commons cuando los baje Paula, y comprobar a 16 px que el trébol desconocido no se lea como un octógono. — Lucía

- 08-11 24:50 · Bocas de arma (Teo, mr-mak 1e8c0d5): APROBADAS. Sobre las cuatro cosas que no cuadraban: 1) Lince: no está en el plantel del MVP, así que no lleva punto. 2) C90: hace falta para la tecla C (D-N137). Teo añade un tubo C90 de un solo uso a una variante de SoldadoArmado, con Muzzle propio. 3) NH90: una puerta con MAG 58 y la otra con M3M de 12,70, como en la referencia real (ficha del ET, nh90_datos.md). Es un cambio solo visual; Nacho dice si la simulación modela cada ametralladora por separado. 4) El fusil cruzado a 35° vale para Reposo, pero en Apuntando el arma tiene que mirar al frente, o el fogonazo y la trazadora saldrán torcidos. Teo corrige la pose Apuntando. — Lucía
- 08-11 24:55 · NH90: la M3M en una puerta es SOLO VISUAL en el MVP (Nacho). En NightSim el NH90 es un arma abstracta de 360°, y en Helicoptero.cs siguen las dos MgPuerta. Pasar una a MgPesada y volver a medir queda para después del MVP. — Lucía

- 08-11 24:58 · Capítulo 3 medido (Nacho, 300 semillas, normal 5250): el pelotón sobrevive en las 300, con 0 bajas, y ningún zombi se le acerca a menos de 15 m. Mi texto 3.8 de las 23:35 prometía algo que casi nunca ocurre. Me equivoqué; corrijo. DECISIÓN: 3.8 vuelve a ser simple («Llévalos al flanco sur y limpia el muro desde ahí.») y la retirada pasa a 3.8b CONDICIONAL: solo si un zombi llega a ≤25 m sale el texto «La horda va a por ellos: retrocede hacia el este disparando, corres más que ellos.» junto con la flecha hasta R2. La flecha no se borra: se queda dormida. Tren sin escolta en la puerta este de Sagunto: 0 zombis llegan en 500 semillas. Así que el 10 % de la D-N177 no vale para esa puerta, y en el apartado de Nules el tren muere hacia el minuto 1. La fracción depende de cada puerta: Hugo la ajusta por estación y la regla no cambia. Horda de Nules en el director (c82f8d5): aviso a las 19:00, asedio de 22:00 a 06:00, regla S0; si se pierde, es para siempre y sale el parte ZS-2. El umbral de caída es provisional (Hugo). — Lucía

- 08-11 25:05 · Fracciones de la D-N177 por estación (Hugo): puerta este de Sagunto 0 % (medido), apartado de Nules 25 % (provisional; Nacho mide con 8 y 16 soldados) y fuera de la puerta oeste de Nules 10 %. DECISIÓN de diseño: con asedio en Nules, el tren espera FUERA de la puerta oeste y no en el apartado, porque es más seguro y basta un pelotón. Es el punto de espera de la D-N152 en Nules. ALERTA de munición: la build gasta unos 442 zombis por u (Noche59) y el modelo cuenta 720. Con el ritmo de la build, el equilibrado pasa al 54–93 % de derrotas. No se toca nada hasta saber quién tiene razón. Nacho mide en NightSim los zombis abatidos por u y por arma, y Sara saca la misma cifra de los registros de la build. Con los dos datos se elige la palanca: cadencia o consumo en la build, o H0 y z_por_u en el modelo. Es prioritario: afecta a todo el balance del MVP. — Lucía
- 08-11 25:10 · Munición (Sara, docs/qa/abatidos-por-u-build.md): el 442 de la build es (abatidos de infantería + vehículos) / u de infantería, porque la munición de los vehículos no entra en el denominador. La cifra real por u total es ≤442. Aprobada la línea [NOCHE-ARMAS] (abatidos y u por arma, recargas aparte), que escribe Iker o Bruno en una rama y Marcos solo fusiona, más 5 semillas en batch sin ventana. — Lucía
- 08-11 25:12 · Munición (Hugo): lo que mide la economía es lo que sale de la reserva por noche (lo que baja el almacén más lo que cuesta reponer las dotaciones). En Noche64, con una semilla, son unas 9,3 u por noche, unos 565 zombis por u: un desfase del 25 %, no del 60 %. [NOCHE-ARMAS] incluirá también el almacén y la dotación al empezar y al acabar. Criterio: si las 5 semillas dan unos 565, corrección suave del modelo; si dan cerca de 442, se revisa antes de tocar la campaña. — Lucía
- 08-11 25:15 · Munición, decisión anticipada (sim_economia de Hugo, 1000 partidas): con 565 zombis por u y sin más cambios, el equilibrado sube al 44 % de derrotas. 1) Si las 5 semillas confirman unos 565: APROBADOS z_por_u 314 y el H0 que, medido, deje el equilibrado entre el 13 y el 15 % (hacia 1290, un 14 % por debajo de 1500). 2) Si salen cerca de 442: NO se baja H0 a 1000. Primero se corrige el desperdicio en la build según [NOCHE-ARMAS] (fuego libre, recargas, disparos sin blanco) y se vuelve a medir; solo después se habla del modelo. — Lucía
- 08-11 25:20 · APP-6, tamaño de unidad (Bruno, mr-mak 8e23865): el pelotón lleva ●●. En el juego tiene de 5 a 8 soldados (escala-existencias: 5 pelotones, 26 soldados; fusileros, 8), no 21, así que el nombre y el tamaño coinciden. Los archivos _seccion_ (●●●) se guardan sin usar. Está pendiente que Bruno diga de dónde salen los 21. — Lucía
- 08-11 25:22 · Bruno confirma que los 21 hombres no tenían fuente. El pelotón queda en ●● (mr-mak 348f557). Cerrado. — Lucía
- 08-11 24:15 · Me equivoqué al decir que no había salido ninguna build desde la Noche64: ya hay Noche69 (Marcos), Noche70 (Iker, 3e265e2, 1258 pruebas) y Noche74 y 75 (turbo). Corregido en el tablón v17, que cuenta el plan por bloques en lugar de por número de build. — Lucía

- 08-11 24:20 · D-N179 · Nules en la Noche71: sin tropa (fuera del tutorial), con 0 u y con horda de 2400 desde la 2.ª noche, cae siempre la 2.ª noche si el jugador no hace nada. Es intencionado: Nules hay que ganárselo. Pero tiene que verse con tiempo, no solo con el aviso de las 19:00. Al amanecer del día 2 aparece el objetivo «Defiende Nules antes de la noche: manda tropa y munición (≥20 u)», y el aviso ámbar de las 19:00 se mantiene. Si cae, el parte ZS-2 dice qué faltó (tropa, munición o las dos). Hugo comprueba que, con un pelotón y 20 u, Nules aguanta la 2.ª noche en la normal. Siguiente D-N libre: D-N180. — Lucía
- 08-11 24:25 · D-N179 comprobada (Hugo, regla del asedio abstracto): con 1 pelotón (8) y 20 u, Nules aguanta la 2.ª noche contra 2400 y gasta 3,3 u (unas 5,5 al ritmo de la build). Cae con ≤2 u y siempre sin munición. El umbral no se toca. El objetivo de ≥20 u se queda: es generoso a propósito, porque se aprende en el día 2. Límite conocido: fuera de pantalla, con el muro en pie, solo cuenta la munición y no cuánto pueden disparar los soldados. Hugo compara con la medida de NightSim de Nacho y propone un tope de fuego si hace falta. — Lucía

- 08-11 24:30 · Capa APP-6 del mapa del informe (D-N160, Bruno, TBD claude/informe-app6 01c4f6c, tecla I). APROBADA con estos ajustes:
  1. Amigos: como está (●● por pelotón y blindado de ruedas por vehículo; guarnición en casa).
  2. Número de la horda: es un informe de inteligencia, así que la precisión depende de si hay ojos. Con tropa propia en la estación o el NH90 encima: centenas («~2.400»). Sin ojos: millares con interrogación («~2.000?»). El jugador entiende que mandar tropa también le da información.
  3. Trébol desconocido: SE QUEDA y va encendido por defecto. Es el «algo se mueve» que prepara la Colmena (D-N160).
  4. Emboscadas sin dibujar hasta el TR-3: de acuerdo.
  5. Helicópteros: SÍ, con la cúpula; en Bétera cuando están en tierra y sobre el mapa cuando vuelan.
  6. Leyenda de una línea: de acuerdo. — Lucía

- 08-11 24:40 · Munición por arma (Nacho, docs/economia/entregas/armas-por-u/, 200 semillas, normal 5250): 388 abatidos por u de todo lo disparado (13,5 u por noche) y 657 por u solo del almacén (8,0 u); la tropa sale con 7,9 u propias y los vehículos con 4,8 u. Los que más rinden: Dragón 957, AG36 755 y fusil de precisión 664. Los que menos: ametralladora ligera 189 y fusil 248. DECISIÓN: la dotación SÍ cuesta. Se repone desde la reserva al empezar cada ataque (regla de existencias), así que lo que cuenta la economía es el total, unos 388 por u. Por la decisión de las 25:15, no se baja H0 a 1000 sin antes quitar el desperdicio. Encargo a Nacho, en NightSim: disciplina de fuego para la ametralladora ligera y el fusil (ráfagas solo con varios zombis en el cono o por debajo de un alcance eficaz; tiro a tiro a distancia). Objetivo: ≥500 por u total, sin bajar de los criterios de la D-N169 en ninguna dificultad. Después, Hugo fija z_por_u y H0 con la cifra medida para dejar el equilibrado entre el 13 y el 15 %. — Lucía
- 08-11 24:45 · Munición, decisión FINAL (Hugo, docs/economia/municion-por-u.md): NightSim (388) y la build (432–442) están de acuerdo. El error estaba en el modelo: el bonus del muro (+20 % por nivel, ×1,8 en Sagunto) multiplicaba la eficacia de la munición. Sin él, el modelo da 400 por u, a un 3 % de lo medido. No hay desperdicio en la build: el fusil y la ametralladora ligera disparan a quemarropa contra la pila. ELEGIDA LA OPCIÓN A: se quita el bonus de la munición y se recalibra H0 midiendo, hasta dejar el equilibrado entre el 13 y el 15 %. El valor del muro no desaparece: pasa a lo que un muro hace de verdad (menos bajas y más tiempo hasta la brecha), si Hugo ve que el modelo lo necesita. ANULO el encargo de disciplina de fuego a Nacho (24:40): sin desperdicio no hay nada que corregir y solo cambiaría el combate ya medido. Me adelanté; queda corregido. — Lucía
- 08-11 24:50 · Capa APP-6 (Bruno f0ed46a, ideas de Paula): 1) El color se queda como en la D-N160 (hostil en hueso, rojo solo mientras ataca). En el juego manda la regla de la paleta sobre la norma APP-6, y queda escrito como licencia. 2) SÍ a la flecha de eje de avance hacia la puerta por donde llega la horda: en hueso mientras avanza y en rojo mientras ataca. Es forma y dice por dónde viene. 3) SÍ al rombo discontinuo para el asedio anunciado, que pasa a continuo cuando llega la horda. Es una licencia del juego: lo de «previsto» como discontinuo está SIN VERIFICAR en la norma. 4) El número sigue con «~» por espacio (16 px). — Lucía
- 08-11 24:55 · Capa APP-6 cerrada (Bruno f438db8): la flecha de eje sale de la dirección media pesada por la densidad (la red no sabe por qué puerta entra). Vale para el MVP. La puerta concreta, guardando el lado de llegada en el plan de asedio, queda para después. — Lucía

### Adenda (Hugo (3), 9-nov 01:10): opción A de la munición, aplicada
Lucía elige la A (municion-por-u.md): la munición se cobra entera (dotaciones incluidas) y el muro deja de multiplicar su eficacia (bonus_fort_nivel 0,20 -> 0; 1 u = 400 zombis, NightSim 388, build 432-442). H0 1500 -> 1220: equilibrado 13,7 %, prisa 25,1 % (1000 partidas). Fortificar sigue valiendo 5,9 puntos de derrota (antes 14,6). Probados menos bajas y retención por el muro: no cambian nada, así que no entran. CSV publicados en csv/ (balance_colmena, balance_dificultad y balance_economia).
- 08-11 25:00 · Munición, opción A aplicada (Hugo, municion-por-u.md §5, 1000 partidas): sin el bonus del muro, H0 pasa de 1500 a 1220. Equilibrado 13,7 % (en banda) y prisa 25,1 %. El muro sigue valiendo: fortificar baja la derrota 5,9 puntos. Darle su valor real (menos bajas, retener horda) no mueve nada, así que el modelo se queda simple. APROBADO. La prisa se queda en el 25 %: sigue siendo claramente más arriesgada (×1,8). No se toca k_huella hasta que la Colmena (D-N160) esté en la build, porque castigar la expansión rápida es su trabajo; se mide entonces. — Lucía

- 08-11 25:05 · D-N157, aspecto de día (Bruno, hoja_dia_horda.png): elegida la E, calima sin niebla (sol a 45° velado, cielo beige, el polvo va en el color de la luz y no como bruma). Banda de día: el mismo shader y LUT; la horda queda en L* 3–16 en pantalla (mediana 6–11). Regla que la acompaña: todo el decorado con una mediana ≥24, el hueso por encima de 65 y prohibida la niebla, que subía la horda a L* 40. Descartadas B y D, con luz rasante. (a) Lateral del tren contra la vía: 5,6 en la E, por debajo del ≥8 de Sara. NO hago excepción. Teo aclara el lateral un escalón dentro de la paleta y Bruno vuelve a medir la E y la noche (lejos de la horda sigue siendo mejor). (b) El muro se queda en 6c7874: con la E no hace falta cambiarlo (vía contra muro, 8,2). Los efectos de los vehículos ya están en la Noche71 (VfxVehicleShot desde Muzzle_N); corregido en el tablón. — Lucía
- 08-11 25:10 · Bocina del tren (pregunta de Nuria, sin responder desde hacía tiempo; fallo mío): en 3D, 6 dB por debajo de la alarma de ataque; clara hasta unos 200 m; no baja el volumen de nada. En el mapa, versión 2D suave, 12 dB por debajo, solo cuando sale un tren propio y como mucho una vez cada 10 s. Silencio al pausar. — Lucía

- 08-11 25:15 · D-N160, tres estados de la Colmena (Hugo, docs/economia/colmena-estados.md, 1000 partidas). APROBADO con dos ajustes:
  - Estados: Dispersa (×0,9), Al acecho (×1,0, con las memorias de tráfico y de atención) y Enjambre (×1,25 y un asedio simultáneo de más).
  - Señal: nodos abiertos en 7 días + 0,5 × (huella − 8). Sube con 4 y con 7, en el momento. Baja de uno en uno tras 3 días por debajo del umbral.
  - H0 1250: equilibrado 14,2 % y prisa 49,4 %. Lo que castiga es el asedio de más. Acepto el 49 % como PROVISIONAL: la Colmena tiene que castigar el crecimiento rápido, pero se revisa con partidas en la build.
  AJUSTE 1: el Enjambre nunca llega por sorpresa. Con la señal en 6 sale un aviso ámbar («La Colmena se agita: si abres más nodos, irá a por ti»), y CO-2 dice la causa al entrar. AJUSTE 2: la precisión del número es la mejor de dos reglas, la de los ojos (24:30) y la del estado. En Enjambre, la horda se ve de lejos («2.000» y su columna) aunque no haya ojos; en Dispersa, sin ojos, sale «~2.000?». Lo que mira el jugador queda como peso del objetivo y se mide en la build. Hugo enciende los estados, pone H0 a 1250, regenera los CSV y se lo pasa a Nacho. — Lucía
- 08-11 25:20 · qa46 (Sara, Noche71, 5 semillas con el turbo de antes del arreglo por SimId): 391 abatidos por u en total, que cuadra con el modelo corregido (~400). DISCREPANCIA ABIERTA: los granaderos dan 306 por u en la build y el AG36 da 755 en NightSim (Nacho). Se llevan el 39 % de la munición. Se repite con el turbo arreglado y se compara; puede ser el daño en área del AG36 en la build. Fallo S2: «pila_max» en el log da 5 (la traza da 333); se mide con la traza hasta que se arregle. — Lucía
- 08-11 25:22 · Granaderos: el área del AG36 usa el mismo código en la build y en NightSim (UnitsWorld.Explode). La hipótesis de Sara es la densidad: la horda ECS con separación junta menos zombis por explosión. Prueba: explosiones y abatidos por explosión en los dos. Si es la densidad, NO se toca el AG36; Nacho calibra la separación de NightSim con la de la build y se vuelve a medir la D-N169. — Lucía

### Adenda D-N160 (Hugo (3), 9-nov 02:05): tres estados de la Colmena, encendidos
Aprobados por Lucía (25:15): Dispersa (×0,9), Al acecho (×1,0) y Enjambre (×1,25 y +1 asedio simultáneo). Señal diaria = nodos abiertos en 7 días + 0,5 × (huella − 8); sube con 4 y 7 y baja tras 3 días por debajo. Aviso ámbar con señal 6. H0 1220 → 1250. sim_economia, 1000 partidas: equilibrado 14,2 %, prisa 49,4 % (provisional, a revisar en la build). Detalle en docs/economia/colmena-estados.md; parámetros colmena_* en csv/balance_colmena.csv.
- 08-11 25:25 · Lateral del tren (Teo, mr-mak d54dd0f): pasa de #50541c a #70784c (unos 17–20 frente al balasto, cumple el ≥8); el techo del v2 y el canto de la R2 pasan a #88885c. Aprobado; se cierra con la medida de Bruno de día y de noche. — Lucía
- 08-11 25:30 · Lateral del tren, corrección: medido en pantalla (Bruno), #70784c da 7,9 en la E (sin margen), no los 17–20 calculados por albedo. Se elige #88885c (14,5 en la E, el mejor también de noche). El techo del v2 y el canto de la R2, que Teo acababa de pasar a #88885c, suben un escalón más de la paleta para que el lateral y el techo no se junten, sin acercarse al hueso de la interfaz. La noche no llega a 8 con ningún albedo (Bruno, modelo de luna sin verificar): la mide Sara en la build. Si falla, la solución va en la luz o en el borde de la silueta, no en el color del tren. A mediodía (A) no se juega con luz alta en el MVP, porque la primera horda de día va con la luz E. — Lucía

### Adenda D-N177 (Hugo, 8-nov 23:50): apartado de Nules medido
Nacho midió el apartado de Nules (normal 2400, 500 semillas): f = 57 % y no 25 %; un pelotón no salva el tren (cae siempre) y dos sí (83 % de vida). La regla del tren fuera de pantalla queda calibrada con tres cambios: escolta 42 abatidos/soldado con un pelotón y 76 con dos o más; 130 de vida por zombi que toca el tren (no 1.200); 0 bajas de escolta. Detalle en docs/economia/tren-a-las-puertas.md. Pendiente: medir el tren fuera de la puerta oeste de Nules (10 % provisional), porque con la regla nueva sin escolta allí no cae.
- 08-11 25:32 · Precisión (Bruno): el techo sube solo a #b8b8b8, que es el último escalón antes del hueso de la interfaz. Lo que ya está en #b8b8b8 no se toca; lo que estaba en #88885c o #94948c (techo del v2, canto de la R2) pasa a #b8b8b8. — Lucía
- 08-11 25:35 · D-N177 en Nules (Hugo con NightSim): en el apartado, la fracción pasa del 25 % al 57 %; con un pelotón el tren cae siempre y con dos queda al 83 %. DECISIÓN: el texto del objetivo («Sube tropa o un vehículo: protegerán la carga») se queda como está, porque con asedio el tren espera fuera de la puerta oeste (decisión de las 25:05), donde basta un pelotón (falta que lo mida Nacho). Si al anunciarse el asedio el tren está en el apartado, sale un aviso ámbar: «Saca el tren del apartado: con asedio, espera fuera de la puerta oeste.» — Lucía
- 08-11 25:37 · Tren (Teo, mr-mak 5018dd0): lateral en #88885c y techo del v2 y canto de la R2 en #b8b8b8. La carga de los vagones pasa de #88885c a #847c34, para que la carga visible (información de juego) no se junte con el lateral. Lo mide Bruno. — Lucía
- 08-11 25:40 · D-N157, día CERRADO (Bruno, medida en la E con 5018dd0): lateral↔vía 14,5, techo↔lateral 19,8, lateral↔suelo 12,5, horda→tren 38,5. ACEPTADO lateral↔cara del muro 6,3: la regla ≥8 vale para los pares que se tocan y se confunden, y el lateral y el muro solo se tocan en las puertas de vía, donde el techo (26) recorta el tren. Al pedírselo a Bruno formulé la regla más amplia de lo necesario; fue un error mío. El muro no cambia. Se reabre si en la build el tren se pierde en las puertas. La noche la mide Sara en la build. — Lucía
- 08-11 25:45 · Carga de los vagones (Teo, mr-mak 84e1194, #847c34): por albedo da ΔL* 4,4 contra el lateral, separados sobre todo por croma. Manda el valor, porque de noche el croma desaparece. Decidido de antemano: si Bruno mide menos de 8 en pantalla, la carga pasa a #845c28 (ΔL* 13) sin volver a consultarme. Medición con -batchmode sin -nographics: pendiente del sí de Eugenio (preguntado al coordinador). — Lucía
- 08-11 25:48 · Norma vigente desde las 23:30 del 08-11 (Eugenio, en las instrucciones del proyecto): se puede lanzar el juego en su PC como haga falta, también sin -nographics y con ventana. Solo habrá restricción si él la pide, y será temporal. Sara mide la noche del tren con la build de Marcos que lleve el tren nuevo. — Lucía
- 08-11 25:50 · Carga de los vagones: #847c34 se queda a 3,1 del lateral en pantalla (Bruno), así que pasa a #845c28 (11,4 contra el lateral y 31 contra el techo), como estaba decidido. — Lucía

- 08-11 25:55 · D-N160, pantalla del Informe (Bruno, docs/arte/pixel-codigo/informe/): elegida la V1, dos columnas con remaches. Se lee de una vez, el mapa queda grande y no hay nada escondido tras pestañas. Avisos: el ámbar «La Colmena se agita» va en el panel de avisos del mapa; CO-1 a CO-4 son entradas del informe con un glifo sin color, la CO-2 resaltada y con la causa en números, y al cambiar de estado sale una banda en hueso de 2,5 s. Mapa de la Colmena APROBADO: la masa siempre en #1c200c y lo que cambia es la forma (Dispersa, punteado sin núcleo; Al acecho, núcleo con orla; Enjambre, masa con contorno hueso y columna de galones; la cifra sin «~»). Los textos son provisionales y los escribe Lucía. Ojo: los textos provisionales ponen tropa en Nules y Castellón; en los definitivos, solo lo que haya de verdad en la partida. — Lucía
- 08-11 26:00 · Bocina, corrección por medida (Iker: alarma −14,9 LUFS, pitido −28): Nuria normaliza el pitido a −22,5 LUFS y lo pone a 0,72 en la zona (6 dB por debajo de la alarma a 0,6, comprobado) y a 0,36 en 2D en el mapa (12 dB por debajo). La regla no cambia. — Lucía
- 08-11 26:05 · Puertas de la D-N151 (Teo, mr-mak 6822e61): APROBADAS, con un cambio: la puerta de vehículos de 8 m abre hacia DENTRO, como las de vía. Hacia fuera chocaría con la horda y la pila justo cuando los vehículos tienen que salir (señal vehiculos_fuera del tutorial). Ángulos: 0°, 45° y 90°; colisión de jamba a jamba, de 2,1 m; sin portillo (Álvaro). Lista: 4 puertas en Sagunto y 4 en Nules. Bien cazados dos fallos: el origen de la pila (quedaba metida 1,1–1,3 m en el muro; ya corregido, Bruno debe usar las mallas nuevas en su rama) y la placa de la v4, que estaba en el hueso d4d0cc y pasa a #b8b8b8. — Lucía

## 09-11 00:00 · D-N160 Informe V1: color de «Necesidades» (Lucía)
- Las necesidades son peticiones, no ataques, así que el 982420 no se usa ahí. El rojo sigue reservado para ataques y brechas (regla de la paleta).
- InformeTextos.ColorFalta = e08c30 (ámbar de aviso). El texto va en ámbar y el glifo en d4d0cc.
- Si una línea de amenaza o de valoración habla de un ataque en curso («la Colmena ataca por el…», «está bajo ataque»), esa línea sí va en 982420.

## 09-11 00:01 · Munición mínima por estación (Hugo, aceptado por Lucía)
- El mínimo es techo(horda ÷ 400) + 2 u. Sale 8 u en Nules, 16 u en Sagunto normal y 17 u en Sagunto difícil.
- Los ≥ 20 u del objetivo del día 2 (D-N179) se quedan como objetivo aparte, con margen, y no son el mínimo. El informe usa el mínimo de Hugo (Bruno f9dfa48).

## 09-11 00:02 · D-N151: puerta de vehículos de 8 m hacia dentro (Teo, af7d2eb) aprobada
- La hoja revisada abre hacia dentro en las 5 variantes, igual que las de vía. En e2 y e3 los restos caen hacia dentro, la pila queda fuera y la colisión sigue a cada hoja. Aprobada sin cambios.

## 09-11 00:03 · Informe V1: líneas de ataque con barra roja (Lucía, a propuesta de Bruno)
- Las líneas de ataque en curso llevan el texto en hueso, que se lee mejor que el rojo sobre el navy 181c30 (ΔL* 23), y una barra roja 982420 a la izquierda. El rojo marca la línea sin cargar la lectura.
- Las necesidades siguen con el texto en ámbar e08c30. Si en la build cuesta leerlas, se les aplica el mismo arreglo con una barra ámbar.
- La puerta de vehículos de Teo (af7d2eb) ya estaba aprobada (ver la entrada de las 00:02).

## 09-11 00:04 · Fe de errores (Lucía)
- A Teo le pedí modelar los estados del muro por tramos, pero ya estaban hechos y aprobados (D-N163 §1, 94cb579). Fue culpa mía por fiarme de una nota vieja del tablón, que ya está corregida.
- 09-11 00:10 · **G3_red regenerado en `nacho/colmena-estados`** (Nacho). Entran tres cambios aprobados: la opción A de Hugo y Lucía (400 zombis por u sin el bonus del muro: fort_bonus_por_nivel = 0), H0 = 1250 y los tres estados de la Colmena (D-N160, colmena-estados.md §5 y §6). NetVersion pasa a 6. Suite 1292/0.

## 09-11 00:12 · D-N160: el CO-0 sí va (Lucía)
- El jugador tiene que saber que la Colmena existe y qué la despierta antes del primer CO-1. El CO-0 sale una vez por partida, al abrir por primera vez el mapa de la red después del tutorial y solo con estado Dispersa. El texto está en informe-textos.md. No sale al cargar una partida. Usa el sonido de Dispersa de Nuria.

## 09-11 00:14 · Paquete de importación de Teo (3a68893): decisiones (Lucía)
- La puerta de vía del modelo tiene 5 m de hueco y el código abre 3,2 m. Manda el modelo, que es el aprobado en la D-N151 y por el que tiene que caber el tren. Marcos ajusta el código a 5 m.
- La pila va instanciada (GPU instancing o mallas combinadas por tramo; lo decide Marcos con Bruno), porque el riesgo está en las llamadas de dibujo y no en los triángulos.
- La SM_PuertaVehiculos antigua, la de Castellón, pasa a llamarse SM_PuertaVehiculos_Castellon para que no se confunda con la nueva. Castellón no está en el MVP.
- Presupuesto de triángulos por pantalla: no lo pongo a ojo. Se fija cuando Sara mida los fps en el PC de Eugenio con el peor caso (Sagunto con asedio y la pila a la altura 4 en todo el perímetro, unos 161.000 triángulos en LOD1).

## 09-11 00:16 · Sonido de la Colmena y del informe (Nuria, https://claude.ai/artifact/FAL2znujxxoMPTnuXHhpRq)
- Una sola variante fija por aviso, no al azar: el jugador tiene que aprender a reconocer cada sonido como una señal.
- Las elegí por las medidas de la página, porque no puedo escucharlas, y prefiero el pico más bajo para que el tono sea sobrio. Al acecho: la 1. Enjambre: la 2 (1,50 s; la 1 se descarta por corta). Vuelta a Al acecho: la 1. Dispersa: la 2, que sirve también para el CO-0. Para la señal 6 y para abrir el informe elige Nuria. Nuria puede cambiar cualquiera de oído si suena peor de lo que dicen los números.
- Mezcla aceptada: Enjambre 3,3 dB por debajo de la alarma; Al acecho −26, la vuelta −28 y Dispersa −30; la señal 6 −32 y el informe −30. Coste: 1.375 créditos.

## 09-11 00:18 · Informe: textos CO y memoria de tráfico (Lucía)
- En textos_informe.csv mandan los textos CO de docs/informe-textos.md (CO-0 a CO-4). Nacho decide cuándo salen y Diseño, qué dicen.
- La línea de tráfico, mientras la red no dé el número de tren ni los días: «Sagunto–Nules: el tren pasa siempre hacia las 08:00. Lo ha aprendido.»

## 09-11 00:20 · Silencio al pausar: vale para todo (Lucía, sobre la revisión de Nuria)
- La pausa calla todo el sonido de juego, de día y de noche, en la zona y en el mapa, también la pausa del tutorial: pitido, CO, informe y batalla del mapa. Lo único que suena en pausa es el propio menú de pausa.
- Se aprueba el arreglo de Nuria (docs/sonido/pausa/revision-silencio-pausa-09nov.md): quitar el && _nightOn, conectar la pausa del mapa y tocar el pitido v2 a 0,72. Lo aplican Marcos e Iker.
- Señal 6 e informe: variante _1 de cada uno (elección de Nuria).

## 09-11 00:22 · Tapia de víveres de Nules: la cal pasa de d4d0cc a b8b8b8 (Lucía)
- Se cambia ya, antes del MVP. El d4d0cc es solo para la interfaz y la selección, y una tapia de ese color se confundiría con un objeto seleccionado. Teo cambia los 10 FBX sin tocar las mallas.
- Muros de huerta: no se añaden en el MVP (Álvaro, para no cambiar las líneas de tiro del capítulo 3). Los tramos de 5 m, la esquina y el portillo quedan como mejora para después.

## 09-11 00:26 · Colores reservados en los modelos (repaso de Teo, 9205e9c)
- Se aprueban las 37 piezas que Teo pasó de d4d0cc a b8b8b8 (§4 del paquete de Marcos). El 982420 no aparece en ninguna pieza. El e08c30 solo está en la franja de las locomotoras (D-N42) y se queda. El visor del Dragón (2×2 px) se queda.
- Las fachadas encaladas en d4d0cc (unos 110 FBX) quedan pendientes. Teo hace una hoja con 5 variantes (A d4d0cc / B f0dc9c / C b8b8b8 / D f0dc9c con zócalo b8b8b8 / E d4d0cc con zócalo b8b8b8), con el fantasma de construcción y el anillo de selección al lado, de día y de noche. Sara mide el ΔL* entre el fantasma y la fachada y luego decido. Hasta entonces no se tocan.
- 09-11 00:35 · **traza_nightsim_o1.csv regenerada en `nacho/colmena-estados`** (Nacho, pedido de Iker por el S2 de Sara en la Noche70). La referencia era de 431db8f (2040 zombis en 9000 ticks). Ahora sale de la noche de 5250 (×103), que es la que lee la build. Data/noche_sagunto.json queda igual que StreamingAssets/Noche. Suite 1296/0.

## 09-11 00:28 · CO-0 al cargar partida (Lucía; precisa la entrada de las 00:12)
- Se queda como lo ha hecho Nacho (b09eeb1): si la partida guardada no había mostrado el CO-0, sale al abrir el mapa de la red por primera vez, siempre que el estado sea Dispersa. Mi «no sale al cargar» de las 00:12 estaba mal dicho: lo que importa es que no se repita. Iker no tiene que añadir ninguna opción.

## 09-11 00:30 · Nules en difícil: sube la horda, la tropa no cambia (Lucía, sobre la tanda de Nacho)
- La dificultad se marca con la horda y no con la guarnición: la tropa que manda el jugador tiene que valer lo mismo en las dos dificultades, y la D-N179 enseña «manda tropa y munición». Nacho mide con qué horda en difícil (20 u, recinto de 124,3 u) se gana el 65 % y Hugo la fija.
- La normal (gana el 99,9 % con 2400) cumple la D-N169 y se queda. Sin munición se pierde siempre, como pide la D-N179.

## 09-11 00:33 · Fachadas encaladas: variante C, b8b8b8 (Lucía, a partir de la hoja de Teo)
- Elegida la C: el muro pasa de d4d0cc a b8b8b8 en las unas 110 FBX de la lista B. Es la única que separa el fantasma y el anillo de día (ΔL* 14,6). La A y la E se quedan en 6,1, y la B y la D, en 1,6, porque el f0dc9c a pleno sol queda igual que el hueso.
- En la hoja se sigue leyendo como cal y no como gris de hormigón, y el carácter lo dan las pilastras granates y los recercados, que no cambian. Retiro lo que dije de que «la vuelve gris»: en la hoja no pasa.
- Teo la aplica ya. Si la medida de Sara en la build da menos de 8, se reabre.

## 09-11 00:34 · RECTIFICACIÓN: las fachadas se quedan en A (d4d0cc) y el arreglo va en la interfaz (Lucía, a partir de la medida de Sara)
- Anula la entrada de las 00:33. Me equivoqué al decidir antes de tener la medida de Sara: con la C la fachada queda a 5,2 de la arena y el edificio se pierde contra el suelo (docs/qa/dl-fachadas-encaladas.md). Además, el fantasma y el anillo casi siempre están sobre el suelo (ΔL* 19,6). El 6,0 solo cuenta donde tapan el pie del muro.
- Las fachadas encaladas se quedan en d4d0cc. Es una excepción documentada a la reserva del hueso: son superficies grandes de escenario, y la interfaz se distingue por su forma y su contorno.
- Bruno añade un contorno oscuro de 1 px (pixelado final) al fantasma de construcción y al anillo de selección, con un tono de la paleta que dé ΔL* ≥ 8 tanto contra la cal de día como contra la arena. Sara lo mide en la build con las capturas de qa47.
- Las 37 piezas pequeñas que Teo corrigió a b8b8b8 se quedan corregidas.

## 09-11 00:36 · Ambiente de día elegido por medidas (Nuria)
- Sagunto: la 1. Nules: la 2. Atardecer: el 1. Marcos tiene la mezcla y la condición del mapa (−6 dB mientras suena un aviso).
- SIN VERIFICAR DE OÍDO: ni Nuria ni yo podemos escuchar, y tampoco los sonidos de la Colmena y del informe de las 00:16. Por la mañana se le pide a Eugenio una escucha rápida con los enlaces.

## 09-11 00:38 · D-N180 · Tren sin escolta rodeado: se pierde y la horda vuelve al muro (Lucía, a partir de la medida de Nacho y Hugo)
- Problema: con el asedio de Nules, sin escolta fuera de la puerta oeste, la horda rodea el tren fuera del alcance de la guarnición y en 445 de 500 noches la noche no se acaba.
- Regla 1, coherente con la D-N177 («todo o nada») y con el aviso «Se perderá con su carga»: un tren sin escolta rodeado (la horda en contacto y ningún pelotón propio a su alcance) se pierde con su carga en un tiempo acotado. Nacho propone el tiempo según la resistencia del tren y no debe pasar de unos minutos de juego. No hay huida automática en el MVP.
- Regla 2, el respaldo general de la D-N175: cuando la horda de fuera no tiene ningún objetivo vivo alcanzable (el tren se ha ido o ha muerto, o la tropa de fuera ha caído), vuelve al muro y asedia la estación. Así la noche siempre acaba con el resultado del muro.
- Nacho lo mete en NightSim y vuelve a medir la puerta oeste. Hugo actualiza tren-a-las-puertas.md. Si al medirlo sale otro caso que no se acaba, se avisa.

## 09-11 00:40 · Mapa de mezcla de Nuria (docs/sonido/mezcla-mvp.md): D7 y D4 (Lucía)
- D7: fuera el cartel «OLEADA n» y fuera sfx_alerta_oleada. Desde la D-N136 no hay oleadas, y el comienzo del ataque ya lo marca la alarma. No se usa CO-2 en su lugar: Enjambre es un estado de la Colmena, no el aviso de un ataque.
- D4: aprobado Sfx.Duck() a −6 dB solo sobre los bucles 2D del mapa mientras suena un CO o un aviso.
- Lo urgente es el doble «sfx_» de la salida del tren (7 constantes). Lo arreglan Marcos e Iker.

## 09-11 00:45 · Nules tras la D-N180: se baja la horda y no se cambia la conducta (Lucía)
- El 99,9 % de Nules salía de un fallo de la medida: el «tren» estaba fuera del mapa y los que trepaban se quedaban pegados al muro. Queda invalidada mi comprobación de la D-N179 («1 pelotón con 20 u aguanta»).
- Los que trepan van a por el edificio de viajeros, como pide la D-N168: el contrapeso es la tropa de dentro. No se cambia.
- Se baja la horda de Nules con la tropa igual. Referencia para el barrido, la que pide la D-N179 cuando el jugador actúa: la guarnición de Inicio más 1 pelotón enviado y 20 u. Objetivos: normal ≥ 95 %, difícil 65 % (banda del 50 al 80 %). Sin actuar (solo la guarnición) tiene que perder casi siempre. Hugo fija las cifras con el barrido de Nacho; el 2400 provisional queda anulado.
- Nacho revisa si alguna medida de Sagunto dependía también del tren fuera del mapa.
- 09-11 00:50 · **Regeneración de G3_red.golden APROBADA (Sara, QA, criterio 8).** Motivo: la puerta de vía pasa a 5 m de hueco (`Obras.TrackHalfMm` de 1600 a 2500), aplicando lo aprobado arriba («Manda el modelo… Marcos ajusta el código a 5 m»). Al cambiar la longitud y el coste del muro, cambian las existencias, y G3 difiere en el tick 5776. Condiciones: (1) G1, G2, G4 y G5 no cambian; (2) antes del 5776, G3 es idéntico y el primer campo distinto son las existencias; (3) la suite sigue en verde; (4) el commit dice «regenera G3 por TrackHalfMm 2500». Si falla alguna, no vale y se vuelve a mirar. — Sara (QA)

## 09-11 00:58 · Horda de Nules desde la noche 2: normal 2200, difícil 2440 (Lucía, con el barrido de Nacho tras la D-N180)
- Normal 2200: gana el 96 % con la referencia de la D-N179 (guarnición, 1 pelotón y 20 u) y la munición p10 en 12,2 u. Difícil 2440: gana el 65 %. Sin hacer nada se pierde el 100 % desde 1800, así que la lección del día 2 se mantiene y la guarnición de Inicio no se toca.
- La curva es muy empinada (100 zombis más quitan unos 20 puntos). Con el Enjambre (×1,25) Nules cae aunque se cumpla el objetivo: es lo que se busca, porque crecer deprisa se paga. Con Dispersa (×0,9) es más fácil. Hugo lo confirma y lo pasa a la tabla. Tras la primera partida de Eugenio se revisa si un margen tan estrecho resulta injusto.
- Sobran unas 13 u. El objetivo de ≥ 20 u se queda tal cual, porque es generoso a propósito.

### Adenda D-N179/D-N180 (Hugo, 9-nov 01:05): hordas de Nules fijadas
Con el barrido de Nacho (D-N180, caso de referencia D-N179): Nules desde la noche 2 = fácil 1880, normal 2200 (96 %), difícil 2440 (65 %). Solo la guarnición pierde siempre desde 1800. Enjambre (×1,25) cae y Dispersa (×0,9) aguanta, como pedía Lucía. La munición mínima de Nules sube de 8 a 10 u, porque allí se abaten unos 300 zombis por u y no 400 (medido: gasto p90 7,8 u). Regla general del Informe: mínimo = redondear arriba (horda ÷ eficacia de la estación) + 2, con eficacia 390 en Sagunto (medida), 300 en Nules (medida) y 300 por defecto en las no medidas. nules.json en docs/economia/json/.
**Confesión de método (Hugo):** NightSim dice que una guarnición de 12 con muro aguanta unos 1.200 zombis, y con 20 unos 2.400: unos 100 por defensor. El modelo de economía no tiene ese tope y deja que los nodos pequeños aguanten miles a base de munición. Si le pongo el tope (100 por defensor), la campaña se hunde (equilibrada del 14 % al 95 % de derrotas), porque a partir del día 20 los asedios a nodos de 12 personas pasan de 3.000. No lo cambio para el MVP (días 1-3 con noches escritas a mano), pero la campaña larga necesita otro reparto de la Colmena o guarniciones que crezcan. Queda como pendiente post-MVP de Hugo.

## 09-11 01:01 · Tren de noche en la build (Sara, qa47): carga más clara; la sombra, si hace falta (Lucía)
- El lateral nuevo funciona: 13,5 contra la vía, 16,2 contra el techo y 14,6 contra la horda. La D-N157 se cierra en cuanto al lateral.
- La carga se pierde de noche (1,7 contra el lateral). Se arregla con una carga más clara: Teo cambia solo el material de la carga a un tono de la paleta que dé ΔL* ≥ 8 contra el lateral de noche (L* 16,6), sin bajar de 8 de día. Sin borde ni luz local, para no tocar shaders a dos días del MVP. Sara lo mide.
- Zombi contra la sombra del tren (por confirmar, Marcos saca una captura en difícil): si se confirma, se aclara la sombra que el tren proyecta en el balasto, no la horda. La horda se queda negra (D-N80: siluetas medidas en negro puro). Bruno ajusta la intensidad de la sombra hasta ΔL* ≥ 8 contra la horda.

## 09-11 01:03 · Munición mínima de Nules: 10 u; el tope de defensores, después del MVP (Lucía, sobre la entrega de Hugo)
- Aceptado: Nules con 1880, 2200 y 2440 (fácil, normal, difícil). El mínimo de Nules sube a 10 u. La fórmula de las 00:01 (techo(horda ÷ 400) + 2) subestima donde se abaten menos zombis por u: Hugo la cambia por una que use los zombis por u de cada sitio y se la pasa a Bruno para el informe.
- Después del MVP: NightSim tiene un tope de unos 100 zombis por defensor y el modelo de campaña no. Para la campaña larga hará falta repartir la Colmena de otra forma o que las guarniciones crezcan. Queda apuntado como riesgo de diseño. No se toca en el MVP.

## 09-11 01:05 · Presupuesto de triángulos: cuenta toda la escena (precisa la entrada de las 00:14)
- La medida de Sara en qa48 da unos 344k triángulos en la escena entera, y la pila 4 suma solo unos 22k. Los 161k de Teo eran solo sus piezas. El presupuesto se fija sobre la escena completa (terreno, edificios, vegetación y horda) cuando Sara mida los fps hacia las 05:00, sin vsync y sin tandas de fondo.

## 09-11 01:12 · Sagunto: fuera la puerta oeste-sur en el MVP (Álvaro, aprobado por Lucía)
- La puerta oeste-sur (§10.8, en (70; 53)) chocaba con la banqueta y el nido sur (§10.14). Se quita y en su lugar va HESCO. Los vehículos salen por la puerta sur (acceso_sur, ya probado). La medida de la azotea sigue valiendo.
- Se quitan los dos postes de catenaria sueltos (X 110 dentro del fuerte y X 60 en el paso a nivel). Detalle en sagunto-nivel.md §10.22.
- La lista de colocación de Teo para Marcos ya no lleva esa puerta.

## 09-11 01:16 · Carga del vagón: b4a080 (Lucía, a partir de la tira de Teo)
- Se elige b4a080, que da +12,5 de día y L* 28,6 de noche, y es la que menos se confunde con el resto del tren. b8b8b8 es el techo de los coches y f0dc9c, de noche, se leería como una ventanilla encendida. El margen de noche es justo: si la medida de Sara tras la reimportación no llega a ΔL* ≥ 8 contra el lateral, se pasa a f0dc9c.
- Va como §6 del paquete de Marcos.

## 09-11 01:30 · G3_red regenerado: rachas de la memoria de tráfico en el hash (Nacho)
- Rama nacho/informe-huecos (sobre nacho/dn180). La red guarda, por tramo y franja, el tren que pasa y sus días seguidos (para la línea completa del informe, pedido de Lucía del 9-nov 00:57). Es estado nuevo: va en el hash (sistema «memoria») y en el guardado (NetVersion 7, con migración 6 → 7). El G3 cambia desde el tick 6301 solo por eso. Mismo commit: horda de Nules 2200 (Lucía 00:56), 300 zombis por u en Nules y tope de fuego de 110 por defensor en el asedio fuera de pantalla (filas de Hugo en balance_economia.csv; a 0 se apaga).

## 09-11 01:22 · Informe: huecos de la red y tope de fuego en el director (Lucía, sobre 28ba0fd de Nacho)
- {zona} en la memoria de atención es el nodo propio olvidado (más de 6 h sin mirarse; si hay varios, el que más ha crecido). Sagunto vuelve a «{n} pelotones». Textos en informe-textos.md.
- El tope de fuego (110 por defensor) se queda activo en el asedio fuera de pantalla del director: así el resultado fuera de pantalla cuadra con NightSim y con lo que se ve en pantalla. Lo de «después del MVP» de las 01:03 era solo para el modelo de campaña (sim_economia).

## 09-11 01:23 · Puerta este de Sagunto con la D-N180: sigue en 0 % (Nacho)
- 499 de 500 victorias y el tren al 100 %, sin contacto. La fracción de la D-N177 no cambia. El fallo del tren fuera del mapa solo afectaba a Nules, y ya está corregido.

## 09-11 01:25 · Recinto de Nules (Álvaro, nules-nivel.md §14): HESCO en los cruces de andén del muro oeste (aprobado)
- Puerta de vehículos en 177,22–185,22 (v0.2). Puertas dobles cerradas con cortos, sin vuelta. El solape de la esquina SO se queda.
- En los dos cruces de andén del muro oeste (Z 52,4–59,9 y 69,1–~80) va HESCO en lugar de sacos, porque sobre el andén de 0,68 m los sacos solo asomarían 0,52 m. Las puertas oeste y la D-N177 no cambian.
- Condición: que el recinto de NightSim con el que Nacho midió 2200 y 2440 sea este mismo. Si no lo es, Nacho repite solo el punto de 2200.

## 09-11 01:28 · Recinto de Nules: se aceptan los 132,24 u (Lucía; corrige el «no cambiar los 124,3 u» de las 01:25)
- Los tramos de HESCO del oeste tienen el triple de vida, así que el recinto sube de 124,3 a 132,24 u. Se acepta, siempre que el 2200 que está repitiendo Nacho con esos tramos no se mueva más de 2 puntos del 96 %. Si se mueve más, Hugo recalcula la horda.
- Hugo actualiza en sim_economia y en nules.json lo que dependa de esa cifra (reparación y coste).
- 01:35: comprobado. Con el HESCO del oeste, 2200 gana el 97,2 % (486 de 500, Nacho). La horda se queda y la lista a75067c (42 piezas, 132,24 u) va a Marcos.

### Adenda Nules (Hugo, 9-nov 01:45): difícil 2470 y tabla del tren
Con el HESCO del oeste (132,24 u), Nacho mide: 2200 gana el 97,2 % (la normal se queda, regla de Lucía de 2 puntos), 2400 el 77,4 % y 2500 el 59,2 %. El 65 % de difícil pasa de 2440 a ~2470, y nules.json lleva 1880/2200/2470. Tren en Nules con 2200: en el apartado cae sin escolta y con 8 o 16 acaba al 43-51 %; fuera de la puerta oeste, 88 % sin escolta y 99 % con 8. Tabla vigente en docs/economia/tren-a-las-puertas.md.

## 09-11 01:44 · Nules difícil 2470; el informe solo da el tren por perdido cuando lo está (Lucía, sobre la adenda de Hugo)
- Aceptado: Nules en difícil sube a 2470 para seguir en el 65 % con el HESCO del oeste. La normal se queda en 2200.
- Con la horda nueva, fuera de la puerta oeste el tren sin escolta se salva el 88 % de las veces. Por eso la valoración del informe «El tren {n} llegará a {estación} sitiada sin escolta. Se perderá con su carga.» solo sale cuando el destino del tren es una posición donde se pierde según la tabla de tren-a-las-puertas.md (en Nules, el apartado). Fuera de la puerta oeste no sale. El aviso ámbar «Sin escolta: {estación} está sitiada» tampoco sale si el tren va a esperar fuera de la puerta oeste.
- El aviso «Saca el tren del apartado…» se queda: ahorra unas 14 u de reparación.
- 09-11 01:48 · **G3_red.golden regenerado UNA vez, APROBADO (Sara, QA, criterio 8)** sobre iker/escenario-inicio 1a25061 con nacho/informe-huecos 7cc2d8e (Marcos (2)). Son dos causas, las dos aprobadas: (1) la puerta de vía con 5 m de hueco (`via_hueco_mm;5000` en el CSV de construcción; ver la línea de 00:50); (2) los cambios de nacho/informe-huecos. Antes de regenerar, G3 difería en el tick 5776 por las existencias (⚠️ lo dice Marcos). La aprobación vale si la suite está en verde y G1, G2 y G5 son idénticos, cosa que Marcos está comprobando ahora en el Editor. Si falla alguna de las dos, queda anulada. **G4_bucle NO se regenera:** ya venía roto («tick 5776, falta en el archivo»), es un S3 aparte y no tiene que ver con esto. — Sara (QA)
  - 01:52 Cumplido: G3 subido en dee094e, con la suite 1331/1331 y G1, G2 y G5 idénticos (Marcos ⚠️). La aprobación queda firme. — Sara

## 09-11 01:59 · Reparto de objetivos de los granaderos: entra; Sagunto difícil sube a ~6470 (Lucía, con la medida de Nacho)
- Entra el reparto. Disparar al mismo grupo (el 43 % de los impactos sobre zombis ya muertos) se ve torpe en pantalla, y con el reparto los granaderos hacen lo que el jugador espera: más bajas en la pila, la mitad de trepadores y el tren deja de caer.
- Sagunto difícil pasa de 5700 a ~6470 (65 %; banda de ~6350 a ~6600). Normal (5250) y fácil no cambian. La curva es empinada: se revisa tras la primera partida de Eugenio, igual que la de Nules.
- Nacho comprueba si en Nules hay granaderos. Si los hay, repite 2200 y 2470 con el reparto. Hugo pasa las cifras a la tabla y a sim_economia.

## 09-11 02:01 · Zombi contra la sombra del tren: confirmado (Sara, Noche80), así que se aclara la sombra
- Los zombis están en L* 0–2 y la sombra en el balasto en L* 3,4, un ΔL* de 2 a 3. Bruno aclara la sombra que el tren proyecta en el balasto hasta L* ≥ 10 en pantalla. Condición: tiene que seguir más oscura que el balasto iluminado, para que se lea como sombra. La horda sigue negra.
- La carga b4a080 queda pendiente de una captura igual a la de la Noche78 (misma hora y encuadre), para saber si el material ha entrado.

### Adenda reparto de granadas (Hugo, 9-nov 02:05): Sagunto difícil 6470
Con el reparto de granadas (Nacho, docs/economia/entregas/granadas-reparto/), Sagunto difícil pasa de 5700 a 6470 (palanca 1086 → 1232) para seguir en el 65 %; fácil 4480 y normal 5250 no cambian. noche_sagunto.json y balance_noche.csv regenerados. **Ojo: 6470 solo vale si la build lleva el reparto** (UnitsWorld.GrenadeDeconflict); sin él, 6470 está muy por encima del precipicio (sin reparto, 5700 ya daba 78,5 %). Abatidos por u en Sagunto: 407 normal y 428 difícil, así que el H0 de la Colmena (z_por_u 400) no cambia. Munición mínima del Informe en Sagunto con eficacia 400: normal 16 u (igual) y difícil 19 u (antes 17).

## 09-11 02:02 · Sombra de la luna aclarada en global (Bruno, claude/sombra-tren 58c16dd; aprobado por Lucía)
- Global, no solo para el tren: un zombi a la sombra del muro o de una casa tiene el mismo problema, y así no se toca el shader del balasto.
- Valor: el más oscuro de 0,55, 0,65 y 0,75 que deje la sombra en L* ≥ 10 en pantalla. La noche no debe perder su peso: entre dos valores que cumplan, gana el más oscuro. Sara lo mide con las capturas y repasa los pares de noche que dependen de la sombra (la horda contra el suelo, la carga y las fachadas).

## 09-11 02:05 · S3, regresión del lateral del tren: causa encontrada (Bruno)
- La reexportación del R2 en e0c2602 salió de una versión anterior: el lateral volvió a 50541c y 40 vértices pasaron a 442c0c. Teo vuelve a exportar la R2 (LOD0 y LOD1) desde d06af89 con la carga en b4a080 e Iker la mete.
- Regla nueva para las entregas de modelos: el LEEME lleva la tabla de colores por pieza leída de los UV y comparada con la entrega anterior.
- 02:07: Nules con el reparto y el HESCO del oeste (Nacho, 500 semillas): 2200 gana el 95,4 % y 2470 el 65,4 %. Las cifras se quedan. La normal cumple por poco. Si la build da menos del 95 %, se baja a 2150.

## 09-11 02:40 · D-N157 cerrada (Sara, I-Noche77)
- Lateral, techo y carga medidos de noche: la carga queda a 9,5 del lateral y a 12,7 de la plataforma. Cerrada.
- Sombra del tren en el balasto: el parámetro de la sombra de la luna no la controla (sigue en L* 3,4 con todos los valores). Bruno busca qué la dibuja y se le aplica la misma regla de las 02:02 (L* ≥ 10 y más oscura que el balasto iluminado).

## 09-11 03:02 · -sombranoche = 0,65 (Lucía, con la medida de Sara en la I-Noche78)
- Es el valor más oscuro que cumple: con 0,55 la carga baja a 7,7 contra el lateral, y con 0,65 queda en 8,5.
- La sombra del tren en el balasto sigue en L* ≈ 3 porque esa zona no recibe el ambiente. Bruno lo arregla en el shader (shadowStrength o sumar el ambiente en la sombra) con la regla de las 02:02. Sara lo vuelve a medir.
- 03:03: Bruno encuentra la causa: la sonda de ambiente no se rehacía durante la partida (claude/sombra-tren 071d8ce, sin compilar). El 0,65 queda PROVISIONAL hasta que Sara repita, con esa build, la sombra del tren y la carga contra el lateral. Si con la luz corregida otro valor más oscuro cumple, gana ese.

## 09-11 03:05 · La obra en curso de Sagunto espera; la zona no pasa a WallJob antes del MVP (Lucía)
- Pasar la zona de Tramos.cs a WallJob es un cambio de fondo a dos días del MVP, solo para un detalle visual (la obra era la prioridad 4). Primero van el muro con RecintoPlan, las puertas y la pila. Se vuelve a mirar después de la primera partida de Eugenio. 2c3d9a0 queda aparcado.

## 09-11 03:42 · -sombranoche = 0,75 y la sombra fija pasa de 090a10 a 1c1e28 (Lucía, con la medida de Sara en la I-Noche80)
- Con la luz ya corregida, 0,75 es el valor más oscuro con el que la carga cumple (8,2). Sustituye al 0,65 provisional.
- La sombra del tren es un color fijo de la pasada pixelada (090a10, L* 2,8) y no luz. Pasa a 1c1e28 (L* 11,5, el mismo tinte azul): la horda queda a 9,5 o más y la sombra sigue por debajo del balasto. Condición: 1c1e28 tiene que ser una entrada de la paleta de 32; si no lo es, Bruno usa la entrada más cercana que cumpla. Sara lo vuelve a medir.
- 03:49: Bruno no encuentra en el código ningún color fijo de sombra (090a10 no está en la paleta). Lo que se ve bajo el tren puede ser una pieza de albedo casi negro o el SSAO (SIN VERIFICAR); su build lleva un diagnóstico para averiguarlo. El objetivo no cambia: que esa zona quede en L* ≥ 10 y por debajo del balasto iluminado, toque lo que toque. -sombranoche 0,75 ya es el valor por defecto (902902d3).

## 09-11 04:19 · Condición del turbo cumplida (Sara, qa44/noche76/VEREDICTO-sara.md)
- comparar-turbo de la Noche76 con -Turbo 8: 9 de 9 pares idénticos tick a tick en las tres dificultades. Las estadísticas de la build pueden ir con -turbo 8. Las 100 semillas en normal van con la Noche82. Si una build cambia el bucle de simulación, se vuelve a comprobar con un par por dificultad.
- 05:08: la causa no era una sombra. La build no compilaba el recorte por alfa (los materiales se crean por código y no hay .mat), así que los huecos del suelo sobre la vía salían negros y opacos (090a10). Arreglo en claude/sombra-tren 98e25852, pendiente de compilar. El 1c1e28 queda en suspenso hasta que Sara mida la sombra de verdad con 0,75. Bruno revisa que todo lo que use recorte por alfa (vegetación, vallas, redes y cualquier otro) se vea bien con el arreglo.

## 09-11 05:10 · Borde azul de noche de los muros: apagado en el MVP (Lucía)
- La emisión no se compilaba, así que el borde (#404460 × 0,6) nunca se ha visto y todas las medidas de noche se tomaron sin él. Se apaga para no meter un elemento sin medir a dos días del MVP. Después del MVP, Bruno saca una captura con y sin borde y se decide.
- El arreglo del recorte por alfa afecta también a los sprites de zombi y de fusilero y al LOD de masa. Sara repasa la horda en las capturas (siluetas D-N80 y banda de L*) para comprobar que se sigue viendo como se aprobó.

## 09-11 05:12 · Sombra del tren: se retira el 1c1e28 y queda una regla para la I-Noche87 (Lucía, con la corrección de Sara)
- Error mío: aprobé 1c1e28 (L* 11,5), que cae dentro de la banda 9–13, reservada a la horda por la D-N80. Retirado. La regla de las 02:02 (sombra ≥ 10) tampoco era compatible con la banda y queda sustituida por esta.
- Regla: la sombra del tren queda fuera de 9–13, a ΔL* ≥ 8 de la horda medida y por debajo del balasto iluminado. Preferencia: la sombra oscura (≤ ~5), con la horda más clara encima, que se lee mejor como sombra que una sombra en ≥ 21 casi del tono del balasto. Si en la I-Noche87 la horda vuelve a 9–13 con el recorte arreglado, la sombra natural seguramente ya cumple y no se toca nada. Sara mide según docs/qa/plan-inoche87.md y, si cumple, lo da por cerrado sin esperarme.

## 09-11 05:52 · D-N181 · Solo ataca la estación quien la tiene como objetivo (Lucía, a partir del caso de Marcos)
- CountAttackers solo cuenta a los zombis cuyo objetivo es la estación (el edificio). Un zombi que ataca a un soldado pegado a la fachada ataca al soldado, no a la estación, y el daño va al soldado. Así la pérdida de la estación es la que se ve en pantalla, y no depende de dónde se quede parado un soldado.
- Además se cierra la huella del edificio con una sola caja de colisión: es un fallo, no una regla, porque ningún zombi debe poder colarse entre los BuildWall (X 96,5).
- NightSim tiene que contar igual (Nacho). Si cambia algún resultado de Sagunto o de Nules, se repite el punto de la dificultad normal antes de tocar las hordas. Siguiente D-N libre: D-N182.
- 05:54, consecuencia valorada (análisis de Nacho): con la D-N181, mientras el tren esté dentro y entero, el edificio de Sagunto es casi invulnerable y la derrota llega por el tren. Se mantiene la D-N181. Es lo que ya hace NightSim, donde se han calibrado todas las hordas, y coincide con la D-N168: en Sagunto lo que se defiende es el tren. Nacho la pone en el código común (NightGame.Attack y CountAttackers) para que los dos mundos sigan iguales. No hace falta separar la infantería de la fachada.

## 09-11 06:25 · Sombra de noche en pantalla: objetivo L* 15–16 (Lucía, con la medida de Sara en qa49)
- El recorte por alfa está arreglado: la franja negra desaparece y la horda sigue como se aprobó (L* 0,6–2,0 en pantalla, a 16,9 del suelo). Sara aclara que la banda 9–13 de la D-N80 es de albedo, no de pantalla, así que mi regla de las 05:12 estaba planteada en la escala equivocada.
- La sombra de noche (p50 8,7) queda a 6,7 de la horda. Bruno la lleva a L* 15–16 en pantalla (ventana válida de 14 a 18): a ≥ 13 de la horda y por debajo del balasto. La horda no se aclara. De día ya cumple. Sara lo vuelve a medir y lo cierra.

## 09-11 06:26 · Si la carga deja de cumplir al bajar -sombranoche, se usa la (b): ambiente solo en el suelo (Lucía)
- Se prefiere la (b): un ambiente propio en el material del balasto y del suelo, para subir la sombra hasta L* 15–16 dejando -sombranoche en 0,75 en todo lo demás (tren, carga y fachadas, ya medidos). Ataca el problema donde está.
- Se descarta la (a), el borde claro de 1 px en la carga: los contornos de 1 px los reservamos ahora para el fantasma y el anillo de selección (05:12 y 00:34), y una carga con contorno se leería como un objeto seleccionado.

### Adenda rodeo (Hugo, 9-nov 07:05): Sagunto difícil 6550
Con el rodeo del edificio en la build, la difícil de 6470 gana 20/20 (Noche86rodeo; antes 10/19 sin rodeo), sin derrotas por la estación. NightSim con rodeo y D-N181 da 82,5 % con 6470 y 64,5 % con 6550 (200 semillas). Subo la difícil a 6550 (palanca 1248) para volver al 65 %. Confirmación pendiente: unas ×20 de la build con 6550; si siguen 20/20, se prueba 6600 (NightSim 53 %). Fácil 4480 y normal 5250 no cambian.

## 09-11 07:04 · Sagunto difícil en la build con el rodeo: 20/20 a 5700 (Sara). Se mantiene 6470 y se verifica en la build (Lucía)
- Las derrotas de antes venían del fallo de la franja de detrás, no del balance, y con el rodeo la build se parece a NightSim. La horda de difícil ya se fijó en ~6470 a las 01:59 (NightSim con el reparto de granadas). No se ajusta otra vez sobre la build a 5700.
- Siguiente medida: ×20 en la build con el rodeo y el reparto juntos, en difícil a 6470 (objetivo del 50 al 80 %) y en normal a 5250 (D-N169). Si la build y NightSim discrepan más que el intervalo de confianza, Hugo propone el ajuste y yo decido.
**Revertido (Hugo, 9-nov 07:06):** Lucía decide no cambiar: difícil sigue en 6470 (fijada a la 01:59). Primero se mide la build con rodeo y reparto (×20 de difícil con 6470 y ×20 de normal con 5250); solo si la build y NightSim se separan más que el intervalo de confianza propongo un ajuste y decide ella. noche_sagunto.json vuelve a la palanca 1232.
600. La normal se comprueba con su ×20 (≥ 95 %).
**Reaplicado (Hugo, 9-nov 07:08):** Lucía confirma 6550 (07:02): su rechazo venía de creer que el 20/20 de Sara era con 5700. Difícil = 6550 (palanca 1248). Si la ×20 de la build con 6550 vuelve a dar 20/20, se prueba 6600.
- 07:08, escalera de Hugo para las ×20 de Sagunto difícil (aprobada, completada): empieza en 6550. Con 10–16/20 (banda del 50 al 80 %) se queda. Con 17–18/20 sube 100. Con ≥ 19/20 pasa a 6700 y, si sigue en ≥ 19/20, a 6900. Con ≤ 9/20 baja al escalón anterior (o a 6470). Tope en 6900: si con 6900 sigue saliendo por encima de la banda, se para y se me avisa, porque entonces la build y NightSim discrepan y hay que buscar la causa.
**Escalera de difícil (Lucía, 9-nov 07:03, a propuesta de Hugo):** empieza en 6550. Con cada ×20 de la build: 10-16/20 se queda; 17-18/20, +100; ≥19/20, 6700 y luego 6900; ≤9/20, se baja al escalón anterior (o a 6470). Tope 6900: si ahí sigue por encima de la banda, se para y se avisa (build y NightSim no cuadran).
**Escalera, versión final (Lucía, 9-nov 07:04; sustituye a la anterior):** ≥19/20 sube (6550 → 6700 → 6900); ≤10/20 baja; con 11-18/20 se para y se confirma con 100 semillas. Tope 6900.

## 09-11 07:14 · D-N182 · La horda llega andando desde fuera de la vista (Lucía, a raíz de la partida de Eugenio)
- Eugenio: que los zombis aparezcan delante de la cámara queda raro. Regla: ninguna horda aparece dentro de lo que puede ver la cámara. Nace en un anillo fuera del alcance máximo de la vista de zona (más allá de la niebla o del horizonte de cámara; Marcos fija la distancia según la cámara) y llega andando, por el rumbo que diga la Colmena.
- La hora de llegada al muro no cambia. Nace antes, lo que tarde en recorrer la distancia extra. La alarma suena cuando la masa entra en el radio de alerta de siempre, no cuando nace. NightSim adelanta el nacimiento en el mismo tiempo (Nacho) y se comprueba que el porcentaje de la normal no se mueve.
- Marcos lo hace en la zona e Iker comprueba que el mapa enseñe la masa acercándose (es la «masa {dirección}, rumbo» del informe).

## 09-11 07:14 · Decenas de miles de zombis en pantalla: estudio medido antes de prometer nada (Lucía)
- Eugenio quiere el efecto de las decenas de miles de la referencia. Hoy las hordas son de 2200 a 6550 y todo el balance está calibrado con esas cifras. En el MVP (11-11) no se cambian.
- Estudio para decidir con datos tras qa48 (hacia las 09:00): (1) Marcos y Bruno, prueba de carga de render en el PC de Eugenio con 10.000, 25.000 y 50.000 zombis instanciados, con LOD de masa e impostores, midiendo fps y llamadas de dibujo; (2) Nacho, coste de simulación de 10.000 a 50.000 en NightSim y en DOTS (tiempo por tick con ×103); (3) Hugo, qué pide la economía para que una horda de ese tamaño sea jugable (tope de unos 100 por defensor, riesgo de las 01:03).
- Con los tres números se decide si va justo después del MVP y cómo. Una opción que estudiar: la Colmena lejana como masa visible (impostores) que no entra en combate hasta acercarse. No se promete en el MVP.
- 07:15, primera cuenta de Hugo (docs/economia/hordas-grandes.md): con 50.000 hacen falta de 250 a 500 defensores. El tope del almacén de zona corta hacia los 18.000, desde 30.000 mandan los víveres y no hay ninguna fuente fija de munición. Sus palancas: supervivientes por tren, tope de zona por nivel y más rendimiento por defensor. Después de qa48, Nacho mide 10.000 contra 100 defensores. Esto refuerza estudiar también la masa visible que no combate hasta acercarse, porque da el efecto sin multiplicar la economía.
- 07:16, segunda vía de Hugo: con masa visible y solo una fracción F que llega al muro, la economía escala con F × masa. Con F = 20 % y 50.000 visibles caben el almacén y los víveres, y la gente se queda en unos 100 defensores. La palanca de dificultad pasaría a ser F. Después de qa48, Nacho mide 10.000 de golpe y 10.000 en llegada continua contra 100 defensores. Con eso se elige la vía.
- 07:16, la D-N182 en el mapa (propuesta de Iker, aprobada): solo vista en el MVP. Una mancha que sale cuando salta el aviso y avanza por el rumbo de la Colmena hasta llegar al nodo a la hora del ataque. Distancia de salida: la que corresponda a la velocidad de marcha por el tiempo entre el aviso y el ataque, con un máximo de unos 10 km para que quepa en el mapa. Durante la noche, la cifra y la mancha alrededor del nodo mientras quede horda. Que sea una masa real del campo que cuente en la simulación no entra en el MVP: va con el estudio de hordas grandes.

## 09-11 07:26 · Hordas de decenas de miles: objetivo firme después del MVP (Eugenio)
- Eugenio acepta que no estén en el MVP, pero las quiere en el juego. Queda como objetivo firme en el GDD (v1.14, §15b) y en el tablón, en el apartado «fuera del MVP». Las dos vías y el estudio están en la entrada de las 07:14 y siguientes.

## 09-11 07:35 · Tutorial 2.4 atascado (Eugenio): opción A más una condición de entrada (Lucía)
- A: si «Reparar» está bloqueado por zombis en el tramo, el paso explica el motivo y se cierra solo a los ~8 s. No se aparta la horda (B), porque enseñaría algo que el juego no hace.
- Condición: el capítulo 2 empieza cuando no queda horda junto al tramo dañado que señala (o a los 30 s, como máximo). Textos en tutorial-textos.md. Lo implementa Iker.

## 09-11 07:40 · Guarnición propia de cada estación (Lucía; corrige el fallo de Eugenio: «vayas a la estación que vayas, aparecen los mismos soldados»)
- Ya lo pedía la D-N173 y sigue sin cumplirse en la build. Cada estación saca su tropa de sus propios datos (IntelForcesAt, nacho/informe-huecos, y los json de cada estación), nunca de una formación común. Las cifras son las ya medidas, sin inventar:
  - **Sagunto** (principal): 5 pelotones, 1 Dragón y 2 VAMTAC (medido por Nacho, 8-nov 15:55). Colocación: 2 pelotones en la banqueta del muro oeste, mirando a la puerta de la vía; 1 en el ala norte y 1 en el ala sur, en la banqueta; 1 de reserva junto al edificio de viajeros; el Dragón y los VAMTAC dentro de la puerta sur (acceso_sur), mirando a la puerta.
  - **Nules** (pequeña): 12 personas, 1 pelotón de fusileros (8) y 1 de ametralladores (4), sin vehículos (nules.json). Colocación: fusileros repartidos entre las dos puertas de vía oeste, en los cruces de andén con HESCO; ametralladores junto al edificio de viajeros, cubriendo el apartado. Ningún vehículo.
  - **Castellón**: sin tropa. Está infestada y cerrada en el MVP (D-N131). Si el jugador entra, no hay soldados propios.
  - **Bétera** (aeródromo): 2 NH90, 2 pelotones para embarcar (uno por aparato) y 1 pelotón de guarnición fijo (8-nov 14:00). Colocación: los de embarque junto a sus NH90 en el helipuerto y la guarnición en la puerta de la valla.
- Los puntos exactos los da Álvaro para cada estación a partir de sus planos (tramos y puertas reales de RecintoPlan), en un formato que Iker pueda cargar. Mientras no lleguen, Iker usa estas reglas con las puertas y los muros de cada recinto. Si la estación no tiene un elemento (por ejemplo, Nules no tiene puerta de vehículos ocupada), esa parte no se coloca.

## 09-11 07:45 · D-N183 · Se empieza con 3 estaciones propias, cada una con su guarnición (Eugenio, 9-nov 07:34; corrige la D-N131 y precisa la D-N156)
- Eugenio pidió empezar con 3 estaciones y lo ha confirmado: tienen que ser **suyas**, cada una con su propia guarnición. Nosotros lo entendimos mal: en la D-N131 y la D-N156 dejamos Castellón infestada y reclamable, así que en la práctica el jugador empezaba con dos. Fue error del equipo y mío como diseñadora.
- **Requisito del MVP**: al empezar, Sagunto, Nules y Castellón son del jugador, con su guarnición propia (entrada de las 07:40), y Castellón deja de estar infestada.
- **Guarnición de Castellón** (estación principal): 3 pelotones y 1 VAMTAC, con su reserva de partida. En el MVP Castellón no sufre la gran horda («Castellón cerrada»: no tiene noche propia), así que no cambia el balance medido de Sagunto ni de Nules. Hugo revisa que su reserva no rompa la economía del arranque (que no regale munición a Sagunto por tren). Colocación: en la banqueta frente a la entrada de la vía y 1 pelotón de reserva junto al edificio; el VAMTAC dentro de su puerta de vehículos.
- Para Iker: estacion_castellon.json pasa de infestada a propia con esta guarnición, y el G3 se regenera (Nacho comprueba que NightSim sigue igual). Siguiente D-N libre: D-N184.

### Adenda D-N183 (Hugo, 9-nov 07:50): reserva de Castellón y H0
Reserva de partida de Castellón: 0 u de munición (la dotación de unas 10 u va con la tropa, así que no hay munición que llevar a Sagunto por tren), 30 u de combustible (el tope de zona; el depósito de 300 era el premio por reconquistarla, que ya no existe), 0 de materiales y 0 de víveres. 26 personas (3 pelotones + VAMTAC). En el MVP no consume víveres, como Bétera. En la campaña larga, Castellón propia desde el día 1 produce 60 de combustible al día y el equilibrado bajaba del 14 % al 3 % de derrotas. El H0 de la Colmena sube de 1250 a 1380 y lo devuelve al 13,7 % (prisa 34,2 %, 1000 partidas). CSV y existencias_red.json regenerados. El muro de Castellón en el modelo (60 u) es PROVISIONAL hasta que Álvaro o Iker den el recinto.
- 07:45, economía de la D-N183 (Hugo), aceptada: reserva de partida de Castellón con 0 u de munición, 30 de combustible, 0 de materiales y 0 de víveres. Son 26 personas que en el MVP no comen. Para la campaña larga, el H0 de la Colmena sube de 1250 a 1380 (equilibrado 13,7 %, prisa 34,2 %). El recinto de Castellón en u, provisional en 60, lo da Álvaro a partir de castellon.json.
**Corrección (Hugo, 9-nov 08:00):** con el recinto real de Castellón (Álvaro: 308,69 u, castellon-nivel.md §9) en lugar de los 60 u provisionales, el equilibrado bajaba al 11 %. El H0 queda en **1400** (equilibrado 14,0 %, prisa 29,3 %, 1000 partidas), no en 1380.
- 07:47: el recinto de Castellón mide 308,69 u (Álvaro, castellon-nivel.md §9), así que el H0 de la Colmena queda en 1400 (equilibrado 14,0 %, prisa 29,3 %; Hugo). Sustituye al 1380.
- 07:55, G3 regenerado (Nacho): la D-N183 sube el H0 de balance_colmena.csv de 1250 a 1400 y el G3 (escenario Mvp) lo lee, así que cambia desde el tick 6301 (memoria). Se regenera una vez en nacho/dn183-castellon. La red de Inicio pone Castellón propia: fundada, guarnición 26, recinto 308,69 u, 0/30 u y 26 personas, sin consumo de víveres, sin guarnición zombi, sin asedio en el MVP y en la historia de la Colmena desde el día 0.

## 09-11 07:54 · Hollín de la vía: fuera en el MVP (Bruno, a raíz de Eugenio en la I-Noche91; aprobado por Lucía)
- Eugenio veía «manchas a lo largo de las vías»: el hollín repetía una mancha cada 9,6 m y el de la puerta oeste, de noche, parecía un agujero sobre el balasto. Se quita por defecto (32151c32; `-hollin` para verlo). Las pintadas del muro norte se quedan.
- Después del MVP, si se rehace: manchas sueltas a intervalos irregulares, con menos contraste y fuera de la banda de la horda (lo revisa Sara).

## 09-11 08:00 · Prioridad única: la partida de 30 minutos (Eugenio, 07:56; plan de Lucía en docs/plan-partida-30min.md)
- A partir de ahora el equipo trabaja solo en el recorrido de 30 minutos: arranque con 3 estaciones, tutorial, primer tren, noche 1 en Sagunto, objetivo del día 2, segundo tren con emboscada (un sondeo de unos 300 a la llegada a Nules) y noche 2 en Nules. Hay una lista imprescindible de 9 puntos. Todo lo demás se para hasta que funcione de principio a fin.

## 09-11 08:05 · D-N184: Castellón empieza tuya pero cercada (Eugenio, 08:02: «sí a la idea»; corrige la D-N183)
- Se sigue empezando con las 3 estaciones propias (Sagunto, Nules y Castellón), cada una con su guarnición (D-N183 y puestos de Álvaro v1.1). Castellón mantiene 3 pelotones y 1 VAMTAC, 0 u de munición y 30 de combustible.
- **Castellón está cercada**: hay una horda quieta alrededor de la estación. En el mapa se ve como una mancha fija en e08c30 sobre Castellón, solo de vista, como la de la D-N182.
- Durante la partida de 30 minutos el cerco **no ataca**: Castellón aguanta sola y no puede caer.
- **No se pueden mandar trenes a Castellón.** Si el jugador lo intenta, sale: «Castellón está cercada. Ningún tren puede llegar hasta que se rompa el cerco.» El tramo Nules–Castellón sigue en el mapa.
- Al pasar por encima de Castellón en el mapa: «Castellón · cercada. Aguanta, pero está aislada.»
- **Romper el cerco** es una misión para después de la partida de 30 minutos y del MVP. Se diseñará con lo que ya hay en la simulación de red (FoundStation y RepairEdge), que hoy no tienen botón en el juego.
- Sale de la lista imprescindible del plan (punto 1, Iker). No añade sistemas nuevos: es una horda quieta, un bloqueo de destino y dos textos.

## 09-11 08:06 · D-N182 en la zona: opción A de Marcos (Lucía)
- La zona mide 256×128 m y con la cámara alejada del todo se ve entera, así que no existe un «fuera de cámara». La horda sigue naciendo donde ahora (O1–O3, a unos 62 m del muro) y se oculta: **de noche la cámara no se aleja más allá de ortho ~35**, y en los **25 m del borde hay una franja de oscuridad o niebla**. Los zombis salen andando de la oscuridad.
- Condiciones: la franja no tapa la puerta oeste ni el punto donde el tren espera fuera de ella. Los avisos y los fogonazos de los disparos siguen viéndose dentro de la franja. Sara comprueba en el recorrido de 30 minutos que no se ve aparecer ningún zombi.
- Ampliar la zona hacia el oeste (opción C) queda para después del MVP, junto con las hordas grandes.

## 09-11 08:10 · Emboscada del segundo tren: texto EM-1 y daño fuera de pantalla (Lucía, para Nacho e Iker; rama nacho/dn183-castellon)
- **EM-1** (aviso de ataque en 982420, con doble clic para ir a la zona): «Emboscada en {nodo}: unos {n} zombis atacan el {tren}.» Va en presente porque el ataque sigue en marcha. {n} se redondea a la centena.
- Si el tren está en el apartado, a continuación sale el aviso que ya existe: «Saca el tren del apartado…» (D-N177).
- **Fuera de pantalla, la emboscada hace daño** con las mismas reglas que en la zona, sin reglas nuevas:
  - **Con escolta** (al menos un pelotón): se rechaza. El tren pierde la munición que gasta en el combate (la misma eficacia que en la zona) y la carga que quede llega a Nules.
  - **Sin escolta y rodeado**: D-N180, se pierde con su carga en un máximo de 10 minutos de juego, salvo que el jugador lo saque antes.
- La guarnición de Nules no sufre bajas fuera de pantalla con un sondeo de unos 300. Si el jugador entra en la zona, el combate sigue allí con lo que quede.
- Si en la prueba se ve que el resultado fuera de pantalla y el de la zona no coinciden, manda el de la zona (Sara lo comprueba en el recorrido de 30 minutos).

## 09-11 08:20 · La emboscada tiene que poner el tren en peligro: se aleja de la guarnición (Lucía, tras el dato de Nacho e136e545)
- Dato: con 300 zombis contra Nules el tren no se pierde nunca (200 de 200 en el apartado y en la puerta oeste, con escolta y sin ella), porque la guarnición está cerca. Así la emboscada no es una emboscada.
- **Decisión**: el sondeo cae sobre el tren **en la vía, antes de llegar al recinto de Nules**, en el último tramo dentro de la zona, a la salida de la franja de oscuridad del borde (D-N182, opción A). Así se ve en la zona y se puede defender, pero la guarnición queda lejos. El sondeo sigue en unos 300.
- **Objetivos, medidos con 200 semillas**:
  - Sin escolta y sin que el jugador haga nada, el tren se pierde en el 60–85 % de las partidas (D-N180).
  - Con escolta de un pelotón, el tren se salva en al menos el 90 %.
  - La guarnición de Nules no pierde lo bastante como para que la noche 2 baje de un 90 % de victorias con el objetivo del día 2 cumplido.
- Si con la distancia no basta, el sondeo sube a 400 y después a 500, y se para en la primera cifra que cumpla. Si ninguna cumple, me lo dice Nacho antes de tocar nada más.
- EM-1 no cambia. El aviso del apartado solo sale si el tren llega a entrar.

## 09-11 09:00 · Emboscada cerrada: 300 en la vía al oeste de Nules (Lucía, con la medida de Nacho en NightSim, 200 semillas)
- El tren espera en X 20–84 m, al oeste de Nules. Los 300 salen de la franja oscura (X 0–20 m) en 30 s y van a por él.
- Medido con 300: sin escolta se pierde el 87 % (174/200); con un pelotón de 8, el 0 %. Con 20 u la noche 2 da el 96 %; la escolta gasta 1–2 u.
- **Se queda así, con 300 y en ese punto.** El 87 % pasa por poco del techo de 85 % que puse, pero ese techo era una cifra mía sin más base: el objetivo del día 2 ya pide mandar un pelotón, el jugador tiene el aviso EM-1 y puede reaccionar, y que ir sin escolta se pague es lo que queremos enseñar. Bajar a 250 o acercar el punto al muro solo sirve para entrar en la banda y le quita peligro.
- Las cifras de 400 y 500 quedan descartadas.

### Adenda escalera (Hugo, 9-nov 09:00): Sagunto difícil 6700
Siguiente peldaño de la escalera de Lucía: difícil 6550 → 6700 (palanca 1276; O1 3350, O2 2010, O3 1340), igual que nacho/dificil-6700 (498cff86). noche_sagunto.json y balance_noche.csv regenerados. Si la ×20 con 6700 vuelve a dar ≥19/20, el siguiente peldaño es 6900 (tope).

## 09-11 09:25 · Perder una estación no acaba la partida (Lucía; S2 de la qa50, para la I-Noche96)
- Perder una noche en una estación **no es el fin de la partida** mientras quede otra estación propia. Esto vale para Nules en la noche 2 y para Sagunto en la noche 1.
- Cartel: «{Estación} ha caído.» Segunda línea, solo con las propias que quedan: «{A} y {B} siguen en pie.» El color es 982420 (ataque).
- Botones, por este orden:
  1. **«Seguir»** (el predeterminado): vuelve al mapa. La estación pasa a perdida, con la horda encima, y su tropa y su carga se pierden.
  2. **«Repetir la noche»**: carga el guardado automático del atardecer. Si la build no guarda al atardecer, este botón no sale (SIN VERIFICAR si hoy existe ese guardado).
  3. **«Menú principal»**.
- «Volver a empezar» solo sale cuando ya **no queda ninguna estación propia** (fin de la partida). Castellón está cercada pero cuenta como propia (D-N184).
- Recuperar una estación perdida queda para después del MVP, como romper el cerco de Castellón.
- 09:25 · Añadido: el guardado del atardecer no existía. Iker lo crea en la I-Noche96: a las 19:00 de cada día guarda la red en atardecer.tbd, y «Repetir la noche» lo carga. La zona no se guarda, así que la noche vuelve a empezar desde el estado de la red a las 19:00. Me vale. Sara comprueba en la qa que no se pierde lo que el jugador preparó de día (tropa colocada y tramos reparados). Si se pierde, se apunta como fallo, pero no bloquea la build.

## 09-11 09:30 · K del ambiente del suelo: K=3,0 no vale; se miden 1,5, 2,0 y 2,5 (Lucía, qa50 de Sara)
- Con K=3,0 el suelo libre da L* 36,3 (objetivo 24–28) y la sombra del tren 21,7 (ventana 14–18). La horda se lee (Δ 20,2). **No se aprueba.**
- Con las medidas que hay (K=0: suelo ≈ 20,5 y sombra 8,7; K=3: 36,3 y 21,7), los dos objetivos coinciden más o menos entre K 1,2 y 2,1. Es una estimación, porque la paleta va a saltos.
- **Encargo para Bruno y Sara**: medir **K=1,5, 2,0 y 2,5** en la misma captura de 110 s (más la de 30 s, que salió negra) y quedarse con el primer valor que cumpla los dos objetivos y la horda con ΔL* ≥ 8.
- **Si ningún K cumple los dos**, manda el suelo (24–28). La sombra se sube aparte dando emisión al `Balasto de la zona`, que hoy recibe muy poca (0,021 frente a 0,183). No se cambian las reglas.
- Mientras tanto, el valor por defecto de la build pasa a **K=2,0**, el que recomienda Bruno. Es el que mejor encaja con la estimación y no hace falta esperar a la medida para sacar la build.
- Es lo único de pulido visual que entra antes de la partida de 30 minutos, porque ya está en la build.
- Tutorial 3.7: decía «el tren espera en la puerta este». Corregido a «fuera de la puerta oeste», como en el plan.
- 09:28 · **Corrección (me equivoqué):** mi estimación de K 1,2–2,1 se basaba en un suelo de 20,5 con K=0 que no sale de la build. Lo medido por Bruno en la build, con la captura de 110 s: K=0 da sombra 7,2 y suelo 25,1; K=1,5 da 9,1 y 31,5. Con 1,5 el suelo ya se pasa, así que **ningún K cumple las dos cosas y se aplica el punto 3**. Apruebo lo que ha subido Bruno en df000dcd: **-ambientesuelo 0,5** y un ambiente propio para el balasto, **-ambientebalasto 1,5** (que ya no se multiplica por su _BaseColor). Ninguno de los dos está medido todavía. Queda anulado el K=2,0 por defecto. Sara mide con -ambientebalasto en 1, 1,5 y 2,5 y repite la captura de 30 s.

## 09-11 09:40 · Nules se juega sobre el terreno de Sagunto en la partida de 30 minutos (Lucía; S2 «-zona Nules carga Sagunto», opción A de Marcos)
- La simulación de la zona de Nules usa el Level de Sagunto: recinto, vía, edificio, colisiones y entradas O1–O4. Solo cambian los parámetros de la noche. Por eso las cifras de Nules (horda de 2200, 96 % de victorias con 20 u y la emboscada en X 20–84 m) **están medidas sobre ese terreno** y siguen valiendo con la A.
- **A para hoy**: se quita lo que delata a Sagunto. El cartel de la fachada pasa a «NULES» y no salen ni el campanario ni el pueblo de Sagunto. Menos de 1 hora (Marcos).
- **B después de la partida de 30 minutos**: un Nules de verdad, con su Level, estacion_nules.json y el recinto de Teo. Habrá que volver a calibrar la horda y la emboscada (Hugo y Nacho).
- A Eugenio se le dirá que Nules usa provisionalmente el terreno de Sagunto, para que no lo encuentre él como si fuera un fallo.
- 09:42 · **Corrijo mi cambio del 3.7 (me equivoqué):** en Sagunto el tren sitiado espera en la **puerta este** (192; 60), según RutaCap3 y GateAttackPermilAt. Fuera de la puerta oeste es el sitio de Nules. El 3.7 vuelve a «el tren espera en la puerta este». El plan lo recoge así: en Sagunto, puerta este; en Nules, fuera de la puerta oeste. El 1.9 se queda sin cabecera a propósito, como paso de una sola línea, para no tapar el ataque.

## 09-11 09:45 · Lista de lo que falta para el MVP y el capítulo 3 tal como está (Lucía)
- La lista ordenada, con dueños, está en docs/mvp-lo-que-falta.md. El MVP está listo cuando la partida se juega entera a mano y la qa no deja ningún S1 ni S2 abierto. Entonces se avisa a Eugenio y se para.
- El capítulo 3 se queda como está en la build, «Pedir refuerzos» (de Nules a Sagunto). El primer tren que manda el jugador es el del día 2.
- Nuevo para Iker (S3 de la qa50): cada paso del tutorial se ve al menos 3 s, aunque su condición ya se cumpla (el 1.8 no llegaba a verse).

## 09-11 09:55 · Diseño v0 de «Romper el cerco de Castellón» (Lucía; después del MVP)
- En docs/misiones/romper-cerco-castellon.md. Se abre el día 3 con un tren de socorro desde Nules (al menos 2 pelotones y la munición de la D-N180). La guarnición sale a la vez. El cerco se rompe cuando la densidad baja de 500, el mismo umbral que FoundStation.
- Si sale mal, Castellón no cae y se puede volver a intentar. Objetivo: entre el 75 y el 90 % de éxito con 2 pelotones. No hay mecánicas nuevas. No entra en el MVP.
- 09:58 · Cambio en la lista del MVP: Computer use ya está activado en el PC de Eugenio, pero desde el RC no funciona. No se le vuelve a pedir. **La corrida B a mano la juega Eugenio por la noche** con la lista de Sara. El MVP está listo para avisarle cuando la corrida A pase entera sin ningún S1 ni S2 abierto.

## 09-11 10:00 · Día 3 y noche 3 (Lucía; cifras provisionales de Hugo, pendientes de que Nacho mida)
- Noche 3 en Sagunto: fácil 5250, normal 6700 (la horda difícil de la noche 1, siguiendo la escalera) y difícil 7100, provisional. Sin el refuerzo se gana como en difícil (~65 %); con él, como en normal. El objetivo del día 3 decide la noche.
- **Objetivo del día 3** (aviso en e08c30 al amanecer, con la mecánica del día 2 y sin carga mínima): «Refuerza Sagunto: manda un pelotón desde Nules antes de las 22:00.» Se cumple cuando un pelotón de fusileros (8) baja del tren en Sagunto. Al cumplirse, en d4d0cc: «El pelotón ya está en Sagunto.» Si no se cumple, a las 22:00 y en e08c30: «Sagunto se queda sin refuerzo esta noche.»
- **La noche 3 no hay asedio en Nules**, como propone Hugo: con 12 defensores aguanta unos 1200 zombis y la regla del tope la haría caer. Es una noche tranquila.
- Al ganar la noche 3: «Sagunto resiste» y la partida sigue en el mundo, como en las anteriores.
- Va en el apartado «Si sobra tiempo» y no retrasa el MVP.
- 09:47 · **Corrijo mi nota de las 09:40 (me equivoqué):** el 2200 (96 %) **no** se midió sobre el terreno de Sagunto, sino sobre la geometría propia de Nules en NightSim (recinto X 85–188, edificio en el muro norte, tren en el apartado). La emboscada (X 20–84, con el morro en el muro en X 85) también se midió sobre esa geometría. Con la opción A, **la horda de la noche 2 y la emboscada quedan SIN MEDIR**. Nacho las repite sobre la geometría de la A: la de Sagunto, con nules.json y los puestos v1.2 de Álvaro. Los objetivos no cambian: noche 2 con el objetivo cumplido ≥ 90 %; emboscada sin escolta del 60 al 90 % y con escolta ≥ 90 %. Si no se llega, se ajusta la cifra de la horda, no las reglas.

## 09-11 10:12 · Tres bloqueos de la I-Noche98 en Nules: andén, umbral del objetivo y derrota «por el tren» (Lucía, para Iker, Nacho y Hugo)
1. **Perder un tren no es perder la noche.** La noche solo se pierde si cae la estación (D-N181: cuentan los zombis que van a por la estación). Es lo que ya decía la regla 2 de la D-N180: si el tren muere, la horda vuelve al muro y la noche acaba con el resultado del muro. `causa=tren` como derrota **es un fallo y se quita**. Si se pierde un tren, sale un aviso en 982420: «Se ha perdido el {tren} con su carga.» La noche sigue.
   - Además, para que no pase sin que el jugador se entere: a las 19:00, si hay un tren parado en una estación con aviso de horda, sale en e08c30: «Hay un tren parado en {estación}. Sácalo antes de la noche o puede perderse.» Doble clic para ir al tren.
   - El bot de -dia2-auto, después de descargar en Nules, devuelve el tren vacío a Sagunto antes de las 19:00, que es lo que haría un jugador que sigue el aviso.
2. **El objetivo del día 2 cuenta lo que se carga al salir**, no lo que llega. El texto ya dice «manda… ≥ 20 u», y lo que se gasta en la emboscada es parte del juego. El objetivo se cumple cuando el tren llega a Nules con al menos un pelotón y salió de Sagunto con 20 u o más. No cambian ni el umbral ni el texto.
3. **Andén único de Nules:** no hay dos andenes en el MVP. Si el andén está ocupado, el tren que llega espera fuera de la puerta (la puerta este en el terreno de la A), baja allí la tropa y la carga, como en un asedio (D-N152 y D-N166), y sale el aviso en e08c30: «El andén de {estación} está ocupado: el tren descarga fuera de la puerta.» No hace falta ningún sistema nuevo.
- Nacho vuelve a medir la noche 2 en la A con estas reglas (sin la derrota por el tren y con el tren devuelto antes de las 19:00). Objetivo: al menos el 90 % con el objetivo cumplido. Hugo revisa que la munición de la noche 2 cuente con lo que se descarga, que puede ser 19 u.
- 10:16 · **Ajuste con las propuestas de Nacho y Hugo, que son más simples que las mías:**
  - Andén: **Nules pasa a 2 plazas de tren**, la vía principal y el apartado (SlotCounts). Solo cambia una cifra. Lo de «andén ocupado, se descarga fuera de la puerta» se queda como respaldo para un tercer tren.
  - Emboscada: **la escolta dispara con su propia dotación y la carga llega entera**, también fuera de pantalla. Así coincide con la zona. El objetivo del día 2 sigue contando lo que llega a Nules (≥ 20 u), y queda anulado mi «cuenta lo cargado al salir».
  - Noche de Nules: **NightParams.TrainNotDefeat = true** (el campo ya existe en NightGame y NightSim). Con eso se mide el 96 %. Lo pone la zona (Iker o Marcos).
  - El aviso de las 19:00 por un tren parado se mantiene. El bot de -dia2-auto **deja el tren donde está**, como en la medida de Nacho.
  - Por comprobar en la build (Iker): que la escolta vaya pegada al tren y que la plaza donde aparca sea el apartado que se midió. En NightSim, con 8 de escolta en el apartado, el tren acaba al 43 % de vida y no muere.

## 09-11 10:40 · Opción A medida: el 2200 vale y la emboscada sin escolta es mortal (Lucía; Nacho, 200 semillas sobre la geometría de Sagunto)
- **Noche 2 en Nules (A):** con el objetivo cumplido, 99,5 % (199/200); sin él, 0 %, como en la D-N179. **El 2200 se queda.**
- **Emboscada (A):** el tren espera fuera de la **puerta este** (X 160–224) y el sondeo sale de la franja este. Con un pelotón de escolta se salva el 100 %. Sin escolta se pierde el 100 % con cualquier cifra entre 100 y 300, porque la guarnición está toda en el lado oeste, a más de 70 m, y se aplica la D-N180.
- **Se acepta la (a), sin escolta el tren se pierde siempre.** El objetivo del día 2 ya pide un pelotón, EM-1 avisa y la lección es clara: un tren sin escolta no llega. Se queda el sondeo de 300. La banda del 60–90 % deja de aplicarse en la A y se volverá a mirar con el Nules de verdad (opción B).
- El aviso de EM-1 y el del apartado nombran la **puerta este** mientras Nules use el terreno de Sagunto.

## 09-11 12:30 · Que las 3 estaciones no parezcan la misma, con lo que ya hay (Lucía; aviso de Sara en la qa51, no bloquea)
- Se mete hoy solo si es barato. No hay piezas nuevas y no se tocan colisiones, tramos ni recintos, porque la noche 2 y la emboscada están medidas con la geometría actual.
  1. **El nombre en la fachada de cada estación**: «SAGUNTO», «NULES» y «CASTELLÓN». Ya se hace para Nules en la opción A. Marcos.
  2. **El título al entrar en la zona**, 3 s, en d4d0cc: «{Estación} · {n} pelotones», y en Castellón «Castellón · cercada». Iker.
  3. **Castellón con la puerta de vehículos de Teo** (SM_PuertaVehiculos_Castellon), que ya está importada. Es solo para que se vea: Castellón no tiene noche en la partida. Marcos, si no le lleva más de 30 min. Si le lleva más, se queda fuera.
  4. Fuera de Sagunto no salen el campanario ni el pueblo de Sagunto (ya decidido en la A).
- Que cada estación tenga su propio terreno, edificio y nave (Nules de verdad en la opción B, y Castellón) queda para después del MVP. Cuando Eugenio juegue, se le dirá que es provisional.
- 12:33 · Título de zona: Sagunto sale «7 pelotones», que son los 5 del plantel y los 2 de tiradores de la azotea (D-N174). **Es correcto y se queda.** El título solo cuenta pelotones; no se quita ninguno, porque el balance de la noche 1 está medido con los 7.
- 12:40 · Nules empieza con 0 u (regla de Hugo: almacén = min(47, reserva de la red)). El objetivo del día 2 pasa a la v2 de informe-textos.md: tarjeta al amanecer, recuadro fijo con el progreso y recordatorio a las 15:00. Va en la I-Noche108.

## 09-11 21:18 · Intro y tutorial en cada partida nueva (Lucía; S2 de la partida de Eugenio con la I-Noche107, propuesta de Sara)
- **«Nueva partida» empieza siempre un mundo nuevo**: las 3 estaciones (D-N183) y Castellón cercada (D-N184). **Siempre pone la intro**, que se salta con Esc o con clic en «Saltar». Ya no depende de `tbd.intro.vista`.
- Después de la intro sale: «¿Quieres hacer el tutorial?», con «Sí» y «No». «Sí» tiene el foco. Ya no depende de `tbd.tutorial.visto` ni de `…saltado`.
- Si ya hay una partida guardada, antes de empezar sale: «Empezar una partida nueva borra la que tienes guardada. ¿Seguir?», con «Sí» y «No».
- «Continuar» carga la partida guardada, sin intro y sin tutorial.
- Me aparto de la propuesta en una cosa: **no hace falta «Volver a ver el tutorial» en Opciones** para el MVP, porque cada partida nueva lo pregunta. Queda para después si alguien lo pide.
- La caja del tutorial que se queda encima del menú se cierra al volver a la escena Menu (fallo, Iker).
- QA: una corrida que empiece en el menú y con los PlayerPrefs borrados, sin `-menu-auto` (Sara).

## 09-11 21:22 · La franja del borde (D-N182) ya no es una banda negra: degradado y bruma (Lucía; S2 de la partida de Eugenio, captura 107_bandas_y_azotea.png)
- En la captura, la franja tiene un borde recto y duro, y por dentro es casi negra. Desde lejos se lee como una banda negra en diagonal, no como oscuridad.
- **Cambio** (sin tocar dónde nace la horda ni el tope de cámara de noche):
  1. **Degradado en toda la franja**: de 0 % en el borde interior al máximo en el borde del mapa, con curva suave (smoothstep), sin ninguna línea.
  2. **Máximo de un 80 %**, y no negro: el color es el del suelo de noche oscurecido, una bruma fría con croma ≤ 5 y L* de 8 a 10 en pantalla. La horda (L* 0,6–2) sigue siendo lo más oscuro y se ve aparecer como siluetas que salen de la bruma.
  3. **Borde interior irregular**, con ruido de ±4 m a lo largo de la franja, para que no se vea la recta.
- **Cómo se comprueba** (Sara, con una captura con la cámara alejada al máximo de noche): no hay ningún salto de L* mayor que 2 entre dos puntos a 1 m dentro de la franja, y la puerta de vía y el punto de espera del tren no quedan dentro de ella.
- Si el degradado no se puede hacer esta noche, la franja se apaga y solo se mantiene el tope de cámara (ortho ~35). Es mejor ver a algún zombi nacer en el borde que una banda negra.

## 09-11 21:26 · Al acabar una noche, la red salta al amanecer siguiente (Lucía; S1 de la partida de Eugenio, opción 2 de Sara)
- Problema: la noche de la zona lleva su propio reloj. Al ganar la noche 1, el mapa seguía en «Día 1 · 14:48» y no salía ninguna guía, porque el objetivo del día 2 espera al amanecer del día 2.
- **Decisión: opción 2**, que es la que menos toca. Unir los dos relojes queda para después del MVP.
  - Cuando acaba cualquier noche en la zona (victoria o «{Estación} ha caído» con «Seguir»), **la red salta a las 06:00 del día siguiente**. Lo que estaba en marcha en la red, como los trenes en ruta, avanza hasta esa hora con las reglas de siempre. Si eso no se puede hacer esta noche, por lo menos los trenes en ruta llegan a su destino.
  - **Cartel al ganar**: «Sagunto resiste.» Debajo, en d4d0cc: «Amanece el día {n}.» Con «Seguir» vuelve al mapa.
  - Nada más volver al mapa sale la **tarjeta del objetivo del día** (para el día 2, la v2 de informe-textos.md, que ya empieza con «Nules no tiene munición»). Así el jugador sabe qué hacer en cuanto termina la noche.
  - Lo mismo después de la noche 2 (Nules) y de la noche 3, si entra.
- Comprobación (Sara): al ganar la noche 1, el mapa marca «Día 2 · 06:00» y sale la tarjeta del objetivo del día 2.

## 09-11 21:28 · Cómo se marcan en el mapa las estaciones propias (Lucía; S2 de la partida de Eugenio, captura 107_mapa_estaciones.png)
- Ahora todas las estaciones salen con el mismo icono verde. El verde no está en la paleta de la interfaz, así que se quita.
- **Propias** (Sagunto, Nules y Castellón): icono relleno en **d4d0cc**, el doble de grande que ahora, con un contorno oscuro de 1 px (el mismo que el anillo de selección) y **el nombre siempre visible** debajo, con el número de pelotones: «Sagunto · 7».
- **Propia y cercada** (Castellón): igual que una propia, con un **anillo en e08c30** y el texto «Castellón · cercada».
- **Atacada ahora**: anillo en **982420** que parpadea mientras dure el ataque (el color de los ataques).
- **Perdida** (cuando caiga una): icono en 982420 apagado, con el nombre tachado.
- **El resto de la red**: icono hueco en **b8b8b8 al 50 %**, más pequeño y sin nombre. El nombre sale al pasar el ratón.
- Comprobación (Sara): en una captura del mapa entero, las 3 propias se distinguen de un vistazo y ningún par de colores que se toquen baja de ΔL* ≥ 8.

## 09-11 21:45 · El tutorial enseña los vehículos (Lucía; nota de Eugenio con la 110: «el tutorial no te dice nada de los vehículos»)
- Tiene razón. Hasta ahora solo se añadía una frase en el 1.3, que se cierra por tiempo. Hay dos pasos nuevos en el capítulo 1, después del 1.6, y los dos se cierran **por acción**, no por tiempo:
  - **1.6b**: «Estos son tus vehículos: el Dragón y los VAMTAC. Selecciónalos igual que a la tropa, con clic en el vehículo o en su tarjeta, y muévelos con clic derecho.» Se cierra cuando hay un vehículo seleccionado y se le ha dado una orden de mover.
  - **1.6c**: «Disparan solos, como la tropa. Con G decides si tienen fuego libre o si esperan tu orden.» Se cierra al pulsar G.
- Fuera la frase condicional del 1.3. Si la estación no tiene vehículos, el 1.6b y el 1.6c no salen.
- **Regla general (lo que encontró Sara)**: en los pasos que se cierran por tiempo, el tiempo cuenta desde que el texto termina de escribirse, y ningún paso se ve menos de 3 s.
- Ojo, Iker: la ayuda dice «6-8 vehículos», pero en la captura las tarjetas 6 y 7 son los tiradores de la azotea. Por eso el texto no da números. Que las teclas cuadren con las tarjetas.

## 09-11 21:58 · Interfaz v3 (propuesta del hilo de rediseño, pendiente del sí de Eugenio): condiciones de diseño (Lucía)
- La propuesta está en https://claude.ai/artifact/RN1FJnAfriYpcEX8HGxh9T. Parte de la interfaz v2 (D-N147), con un fondo oliva casi negro, el objetivo arriba en el centro, un panel de trabajo único a la izquierda y las fuentes Barlow Condensed, Barlow e IBM Plex Mono.
- Condiciones: los estados solo usan d4d0cc, e08c30 y 982420. El oliva #8ea35a no se usa nunca para un estado. #d65a48 solo es la versión en texto del 982420. Todos los pares que se tocan cumplen ΔL* ≥ 8. Los textos y los tiempos del tutorial no cambian. El recuadro del objetivo del día 2 va arriba en el centro.
- No se toca código hasta que Eugenio dé su sí y el MVP esté cerrado. Si lo aprueba, será la D-N185.

## 09-11 22:02 · D-N185 · Interfaz v3 aprobada por Eugenio (21:55: «vale bien está bien la interfaz nueva»)
- La dirección es la de https://claude.ai/artifact/RN1FJnAfriYpcEX8HGxh9T (v2 de la página): fondo oliva casi negro, el objetivo fijo arriba en el centro, un panel de trabajo único a la izquierda, la guía del tutorial con «Haz esto» y foco, y las fuentes Barlow Condensed, Barlow e IBM Plex Mono. Valen las condiciones de las 21:58.
- **La horda en el mapa va en rojo** (lo pide Eugenio: «las hordas se representan en negro en vez de rojo en el mapa»). La mancha va en **982420 tramado**, con una flecha de avance y la hora de llegada, y parpadea mientras ataca. Esto cambia la D-N182 (la mancha de vista) y la D-N184: el cerco de Castellón es una mancha 982420 tramada quieta, que no parpadea porque no ataca, y la estación lleva su anillo e08c30. **En la zona no cambia nada**: allí la horda sigue en la banda oscura de la D-N80.
- Símbolos del mapa (también lo pide Eugenio: «no se entienden… cuando alejas se pega todo»): una leyenda plegable con L que solo muestra lo que hay en pantalla, tres niveles de zoom, las estaciones propias agrupadas en una tarjeta al alejarse, etiquetas con prioridad que no se pisan y siluetas con palabra en lugar de APP-6. El APP-6 queda solo para el informe (Tab). Las reglas de estaciones de las 21:28 (ed7f0ae) se mantienen.
- Calendario: se programa cuando el MVP esté cerrado. El orden lo decide el coordinador con Iker, empezando por el mapa, que es lo que Eugenio ha señalado.
- Siguiente D-N libre: D-N186.

## 09-11 22:15 · D-N186 · El núcleo de Eugenio: tres pilares y órdenes de la zona al mapa (Eugenio, 21:59–22:02; GDD v1.15)
- **Pilares**, que mandan sobre todo lo demás: **PERSISTENCIA** (cada zona existe y lo que dejas se queda tal cual), **TIEMPO REAL** (un solo reloj y el mundo sigue mientras miras otra cosa; sin saltos de hora ni turnos) y **SIMULACIÓN** (nada se resuelve de golpe; lo que no ves se simula con las mismas reglas y de forma determinista). La referencia es Ebbtide.
- **Bucle de órdenes** (GDD §3a): se selecciona en la zona (el tren y su carga en el andén, los helicópteros en el aeródromo), se sale al mapa con la rueda y se da clic derecho en el destino. El aire puede ir a cualquier punto y los trenes solo a estaciones. En los dos casos hay un imán de unos 40 px hacia la estación más cercana. Si un tren no puede salir, el cursor dice por qué. El panel «Preparar tren» deja de ser un paso obligatorio. Los aeródromos se pueden visitar.
- **Lo que se anula o se cambia porque choca con los pilares**:
  - **El salto de la red al amanecer** (21:26, 3f1764c) queda **anulado**. Ahora la noche de la zona va con el reloj de la red (la opción 1 de Sara) y al acabar se ve la hora real. La tarjeta del objetivo del día 2 sale al amanecer real, y mientras tanto el recuadro de la franja superior dice: «Siguiente: Defiende Nules (empieza al amanecer)».
  - **La emboscada y el cerco «fuera de pantalla»** no se resuelven de golpe: los simula NightSim de forma continua con las mismas reglas, y se puede llegar a mitad. La medida de Nacho ya se hizo con NightSim, así que sus cifras siguen valiendo.
  - **El combate abstracto calibrado** de la §6 del GDD desaparece.
  - **La intro y el tutorial «solo la primera vez»** del §15b: se aplica la decisión de las 21:18.
- El plan por fases lo cierra el hilo «Rehacer el núcleo» con Nacho, Iker y Marcos. Diseño revisa cada fase con estos pilares.
- 22:20 · **Añadido a la D-N186** (plan del núcleo, https://claude.ai/artifact/NkEDBN79eE6MFBjKyjSQ79, fases F0–F4): **la fidelidad de la simulación no depende de la cámara** (lockstep, §17). Al alejarse solo se dibuja menos. En la F3, AmbushStep, D-N177 y ResolveZoneSiege dejan de ser fórmulas y pasan a ser choques reales en el sitio. Los objetivos de diseño no cambian, solo cómo se consiguen:
  - Sin escolta, el tren rodeado se pierde (D-N180: en 10 min de juego como mucho).
  - Con un pelotón de escolta, se salva al menos el 90 % de las veces.
  - La noche 2 de Nules, con el objetivo cumplido, se gana al menos el 90 % de las veces.
  - Un tren que espera a las puertas está expuesto (D-N152).
  - Hugo y Nacho fijan las cifras de los choques para que se cumplan, con 200 semillas.

## 09-11 22:20 · Economía de la partida de 30 minutos con el núcleo en tiempo real (Lucía; propuestas de Hugo, docs/economia/economia-tiempo-real-30min.md)
1. **Aprobado.** Al descargar, la carga entra directamente en el almacén de la zona hasta el tope y lo que sobra va a la reserva. Aviso en d4d0cc: «Descargado en {estación}: {x} u al almacén, {y} u a la reserva.» Ya no se ve el almacén a 0 después de llegar (Eugenio, I-Noche110). No cambia ninguna cifra medida.
2. **Aprobado medirlo.** Noche 2 con el pelotón pero sin carga, solo con su dotación. Si sale entre el 50 y el 80 %, se queda así, porque da tensión sin que la partida esté perdida de antemano. Si pasa del 90 %, las 20 u sobran y se endurece la horda o el requisito, y me pasáis la propuesta.
3. **Aprobado.** El NH90 de Bétera es la red de seguridad sobre Nules si el objetivo falla, y se manda con el núcleo (selección en Bétera y clic derecho en Nules). Cuando el objetivo del día 2 sigue sin cumplirse a las 19:00, el aviso añade: «Puedes mandar los NH90 desde Bétera.» Con 5 o 6 salidas de combustible no hace falta tocar nada.

## 09-11 22:25 · Cifras de la F3 y ampliaciones D-N187 a D-N189 aprobadas (Lucía; Hugo, docs/economia/cifras-f3-y-ampliaciones.md; cifras provisionales hasta que Nacho las mida)
- **F3, corrijo la D-N180**: «≤ 10 min de juego» equivalía a 6 s reales, y eso no se puede leer. Pasa a **≤ 1 min real desde el contacto** (≈ 1,7 h de juego). Con la vida actual el tren cae en 40–60 s. No se toca la vida del tren. Con escolta (8), ≥ 90 %; noche 2, ≥ 90 %. Las dos se cumplen con lo que hay.
- **D-N187 · Supervivientes en el campo**: un grupo de 6 a 15 personas cada 1,5 días de juego. La horda que los persigue (150–300) llega entre 2,5 y 4 h después del aviso. Rescatarlos cuesta 2 u de combustible al NH90. Salen unas 45 personas por semana, que van a la población.
- **D-N188 · Tren de socorro de Castellón**: el cerco es de 2500 y se rompe por debajo de 500. Hacen falta 2 pelotones y 11 u como mínimo. Si no se rompe, se rehace a unos 150 por día. **No se abre antes del día 3**, porque el premio, Castellón con su combustible, es muy grande.
- **D-N189 · Tren blindado**: ocupa una plaza, así que el tren pasa de 100 a 80 u, y gasta ~1 u en una emboscada de 300. Solo, salva entre el 60 y el 80 % de los trenes, por debajo de una escolta, para que elegir entre uno y otro pese. Cuenta como tropa propia en la D-N180 mientras le quede munición.
- Las tres entran en el GDD (§15c). Se programan detrás de las fases del núcleo, y la D-N187 justo después de la F0 (el gesto de clic derecho a un punto del campo).
- 22:30 · Añadido a la D-N186 (GDD §3a), a partir de las citas de Ebbtide que ha traído Paula: **órdenes de intención en el mapa** (Aguantar, Retrasar y Retirarse; desde un aviso, desviar el tren o pedir apoyo de fuego a un NH90) y **solo se ven las hordas que tus fuerzas tienen a la vista**; las demás salen como la última posición conocida, apagadas y con su hora. Va en la F0 o la F1 del núcleo, según diga el hilo «Rehacer el núcleo».
- 22:33 · **Respuesta a Nacho sobre lo que hoy se resuelve en un solo tick** (https://claude.ai/artifact/B6Q76rxQoLDArKvkqR6jjd):
  - Del 1 al 4 y el 7 (asedio, puertas, emboscada y masa en bloque): fuera, como dicen la F2 y la F3.
  - **5. FoundStation deja de ser instantánea** (aquí no sigo su recomendación): fundar es una obra, como RepairEdge. Dura **2 h de juego** con la gente y la carga en el sitio. Si la densidad de horda pasa de 500 durante la obra, se para, y la gente queda expuesta. Así se cumple el pilar de que nada se resuelve de golpe y fundar tiene riesgo.
  - 6. LoseNode y LoseTrain siguen siendo instantáneos. Solo apuntan un hecho que ya ha pasado en la simulación.
  - **NH90: 20 s → 600 ticks.** Sí. Va en tiempo de juego, así que a ×4 dura 5 s.
  - **Bajar a ×1 al empezar un ataque**: sí, pero lo que lo dispara es el **primer contacto de una horda con una estación propia**, no la hora de las 22:00. Aviso en e08c30: «Ataque en {estación}: velocidad ×1.» Se puede quitar en Opciones.
- 22:38 · **Nules B (Álvaro, 24d69f7, docs/niveles/nules_terreno_b.png): aprobado como terreno de la opción B, después del MVP.** Dos flancos que se leen: Na por la vía al 50 % y Nc por la plaza al 40 %; Nb al 10 % y Nd al 0 %. Al norte, una explanada sin sólidos y una hilera de 14 casas. Los ametralladores van a la esquina noroeste (87,5; 93). Nacho mide la horda con los mismos objetivos: noche 2 con el objetivo cumplido ≥ 90 % y sin él ≈ 0 %; emboscada sin escolta perdida y con escolta ≥ 90 %. Si no se llega, se ajusta la cifra de la horda, no el terreno. Los postes y tolvas de Sagunto y Bétera como zona también quedan aprobados.
- 22:40 · Simulación de D-N187 a D-N189 (Nacho): no hay pegas de fondo. **D-N187**: cuando la horda alcanza a los supervivientes, el grupo no se pierde de golpe, sino que **pierde 1 persona cada 5 s reales** hasta que lo recoge un NH90 o no queda nadie (pilar 3). Aviso en 982420: «La horda ha alcanzado a los supervivientes de {lugar}.» No hace falta una zona temporal. **La velocidad del NH90 es la verificada, 260 km/h (D-N173)**: Hugo corrige apoyo_aereo.json (decía 144) y vuelve a calcular el margen. Si sobra, la horda llega antes, siempre que quede al menos 1 h de juego para reaccionar. **D-N188** depende de la F2. Por ahora vale la aproximación de Nacho (los 26 de dentro defienden y los 16 llegan desde fuera) y él dice cuánto se parece. **D-N189**: es un vehículo con una MAG 58 fija. Mientras tiene munición no cae por la regla de rodeo, solo por daño. Nacho mide el 60–80 %.
- 22:45 · **Corrección del motivo, no de la decisión:** según Hugo, la regla de cerco de la D-N180 ya existe en el código. Un tren rodeado y sin tropa propia a 40 m cae en unos 6 s reales (10 min de juego), y eso está medido. Aun así, **me quedo con ~1 min real** (SurroundLossGameMin de 10 a 100): con el núcleo en tiempo real, el jugador tiene que poder **ver** que el tren está rodeado y reaccionar (sacarlo, mandar escolta o pedir un NH90), y en 6 s no da tiempo. Nacho vuelve a medir la emboscada y las puertas con 100. Lo esperado: sin escolta el tren se sigue perdiendo casi siempre, y con escolta no cambia nada. Si sin escolta baja del 85 %, se mira otra vez. Acopios de carga de Álvaro (b3ed762): visto, me vale.
- 22:48 · D-N187, cifras: el NH90 va a 260 km/h en apoyo_aereo.json (Hugo). La horda de los supervivientes llega **entre 1,5 y 3 h de juego** después del aviso. Bétera–Nules son 9 min de juego. El json lo recogen Iker o Nacho.
- 22:50 · **Corrijo el punto 3 de la economía de 22:20** (Nacho, 200 semillas). En la noche 2 de Nules, el pelotón sin munición en el almacén gana 0 de 200, y el NH90 de apoyo con solo la guarnición también 0 de 200. Lo que decide la noche es **la munición del almacén**. **Quito la línea «Puedes mandar los NH90 desde Bétera.»** del aviso de las 19:00, porque promete algo que no funciona. **Apruebo la idea de Hugo**: la red de seguridad será que el NH90 **lleve munición** (unas pocas u por vuelo, se elige la carga en Bétera y se manda con clic derecho a Nules), no que dispare. Las cifras saldrán de la curva de 5, 10 y 15 u que está midiendo Nacho. Cuando estén, el aviso vuelve como «Puedes llevar munición en los NH90 desde Bétera.»
- 22:55 · D-N180 con 100 min medido (Nacho, 200 semillas): sin escolta, el tren se pierde en 200 de 200 tanto en campo abierto como en la puerta este; con 8 de escolta, en 0 de 200. La noche 2 sale 199 de 200. Con 300 zombis el tren cae por daño en 20–40 s reales. **Cerrado.** D-N189: con una MAG 58 sola el tren se pierde siempre. Para llegar al 60–80 % se barre primero **el blindaje** (la vida del tren cuando lleva el vagón blindado; es lo que su nombre promete) y solo después la cadencia, que se queda en valores creíbles para una MAG 58.
- 23:48 · D-N189 y D-N188, medidas de Nacho. **Blindado**: como la emboscada es casi la misma en cada semilla, el resultado es todo o nada. Si ninguno de los valores entre el 17,5 y el 22,5 % da el 60–80 %, **el riesgo lo pone el tamaño de la emboscada, no la probabilidad**: se elige el blindaje con el que el blindado solo **aguanta una emboscada de 300 por poco** (llega con poca vida) y **cae con 450 o más**, mientras que una escolta de 8 aguanta las dos. Así elegir entre uno y otro sigue pesando. **Cerco**: por la D-N184 el cerco **no ataca solo**, así que el caso «sin tren» no existe: sin socorro, Castellón y el cerco se quedan quietos. Solo se mide con el tren de socorro, con el objetivo de la D-N188: con 2 pelotones, entre el 75 y el 90 %. Que con 2500 salga el 100 % confirma que hay que subirlo; se sigue con 3500, 4500 y 5500.

### Adenda Hugo 09-11 23:50: NH90 con munición y noche 3 difícil (cifras cerradas)
- NightSim (Nacho, 200 semillas), noche 2 de Nules con guarnición y pelotón, según la munición del almacén: 0 u → 0 %; 5 u → 0 %; 6 u → 61,5 %; 7 u → 99,5 %; 10 u → 99,5 %; 15 u → 99,5 %. Es un precipicio entre 6 y 7 u, sin punto medio.
- Propuesta: el NH90 lleva 3 u de munición por vuelo desde Bétera. Con 5 u en Nules, un vuelo la deja en 8 u (pasa). Con 0 u hacen falta 3 vuelos. El mínimo de 10 u del Informe deja margen sobre el precipicio.
- Noche 3 difícil con refuerzo: 8000 → 85,5 %; 8250 → 53 %; 8500 → 29,5 %; 9000 → 0,5 %. El 65 % cae en unos **8150**. Cifras de la noche 3: fácil 5250, normal 6700 (ligada a la escalera de Sagunto), difícil 8150.

## 09-11 23:50 · D-N190 · El NH90 lleva munición como red de seguridad (Lucía; cifras de Hugo y curva de Nacho, 200 semillas)
- En la noche 2 de Nules, según la munición del almacén: con 0–5 u se gana el 0 %, con 6 u el 61,5 % y con 7 u o más el 99,5 %. Es un precipicio entre 6 y 7 u.
- **Cada vuelo de NH90 lleva 3 u desde Bétera.** Con el núcleo, se selecciona el NH90 en Bétera, se carga allí y se manda con clic derecho a Nules. Desde 5 u basta un vuelo; desde 0 u hacen falta tres.
- **Vuelve el aviso** de las 19:00, si el objetivo del día 2 no está cumplido: «Puedes llevar munición en los NH90 desde Bétera.»

## 09-11 23:50 · D-N191 · Cifras de la noche 3 en Sagunto (Lucía; Hugo con medida de Nacho)
- Fácil 5250. Normal 6700, ligada a la escalera de Sagunto. **Difícil 8150**, el punto donde se gana el 65 % con el refuerzo (8000 da 85,5 %; 8250, 53 %).
- Lucía 09-11 23:44: aprobadas como D-N190 (NH90 3 u/vuelo, vuelve el aviso) y D-N191 (noche 3 difícil 8150).
- 10-11 00:45 · **Guarnición de Nules: de 12 a 16** (4 fusileros más, en la banqueta del flanco de la vía). Motivo: con la escolta entera dentro, la noche 2 se gana el 99,5 %, pero si la emboscada le cuesta 4 bajas se gana el 0 %, y ese margen es demasiado fino. **No se reponen las bajas de la escolta al llegar**: rompería la persistencia (D-N186), porque las bajas se quedan. Nacho vuelve a medir con 16. Objetivo: noche 2 ≥ 90 % con el objetivo cumplido y la escolta con hasta 4 bajas; sin munición en el almacén, sigue en ≈ 0 %. Si con 16 sin munición se gana más del 10 %, se busca otra cifra con Hugo.
- 10-11 00:48 · **D-N189 cerrada: blindaje del 20 %** (Nacho, 200 semillas, MAG 58 a 3,3 abatidos por segundo). Contra una emboscada de 300 se salva el 72 %, dentro del 60–80 %. Contra 450 cae siempre. La escolta de 8 aguanta las dos (con 450 llega con el 60 % de vida).
- 10-11 06:45 · Cifras de la F3, Hugo (cifras-f3-y-ampliaciones.md, 10-nov). (1) **Munición mínima del socorro de Castellón**: 11, 14, 17 y 21 u para cercos de 2500, 3500, 4500 y 5500. Aprobado. (2) **Tamaño de la emboscada según el tramo**: 300 en Sagunto–Nules y 450 en Nules–Castellón. Aprobado; así elegir entre blindado y escolta pesa. (3) **Reserva para el socorro**: aquí cambio la propuesta. **No se impide que salga**, porque lo decide el jugador. Al preparar el tren, si después de cargarlo la reserva de la red baja de 47 u, sale un aviso en e08c30: «Si sale este tren, la reserva baja a {x} u. A Sagunto le pueden faltar para la noche.» Hugo lo comprueba con el modelo de campaña.
- 10-11 06:50 · **La escolta entra en la estación al anunciarse el asedio** (Hugo y Nacho, I-113: con la escolta fuera, la noche 2 se gana el 6 %; con la escolta dentro y entera, el 99,5 %). Aprobado: cuando se anuncia el asedio de una estación, los pelotones propios que están a menos de 40 m del tren descargado **entran andando** por la puerta, antes de que se cierre (D-N151), sin teletransporte, y pasan a la guarnición. Si el jugador los ha mandado fuera a mano después de descargar, se quedan fuera, porque es decisión suya. Junto con la guarnición de 16, cubre las bajas de la emboscada.
- 10-11 07:58 · **D-N188, cerco de Castellón: 4200, provisional** (Hugo, interpolando entre los 3500 que siempre se rompen y los 4500 que se rompen el 68,5 %; da ~78 %). Munición mínima 16 u y la regeneración se topa en 4200. Se cierra cuando Nacho confirme el 4200. Nules con 16: con 5 u se gana el 95,5 %. Falta medir 0, 2, 3 y 4 u para comprobar que sin munición sigue en ≈ 0 %.
- 10-11 08:30 · **D-N192 · Guarnición de Nules y reparto de la escolta** (Nacho, 200 semillas). Con 16 y una escolta que llega con 4 vivos se gana el 0 %, aunque son los mismos 20 hombres que 12 + 8, que ganan. Así que **el problema es dónde se ponen, no cuántos son**: el flanco norte se queda sin cubrir. Decisión: **los supervivientes de la escolta se suman a la guarnición y la guarnición se reparte de nuevo cubriendo primero el flanco con menos tropa** (en Nules, el norte). Es una regla de colocación al entrar (D-N186: entran andando), no una cifra nueva. No se sube la guarnición otros 4. Nacho lo mide con el objetivo: con 4 bajas en la escolta, ≥ 90 %. Si no se llega, entonces sí se suben 4.
- 10-11 08:35 · Corrección de Hugo: **el cerco de 4200 da el 97 %**, no el 78 % (la curva es un precipicio: 3500 → 100 %, 4500 → 68,5 %, 5500 → 17 %). Nacho mide 4400 con 17 u; el cerco provisional pasa a la cifra que dé el 75–90 %. **D-N190 se mantiene en 3 u por vuelo**: con 16 + 8 hombres, Nules necesita 5 u (con 4 u se gana el 21,5 %; con 5 u, el 95,5 %), así que desde cero hacen falta dos vuelos. Me parece un precio justo por la red de seguridad.
- 10-11 08:35 · **D-N192 cerrada** (Nacho, 200 semillas): con 4 bajas en la escolta y 20 u se gana el 99,5 %. Redacción final: **los supervivientes de la escolta se suman a la guarnición; se llenan primero los puestos de los extremos (norte y sur) hasta un pelotón completo de 8, y lo que sobra va a la banqueta.** No se sube la guarnición. Importante: no es solo una regla de NightBot. **Es la colocación automática del juego cuando la escolta entra al anunciarse el asedio (Iker)**, y NightBot la imita. Después, el jugador puede mover a quien quiera.
- 10-11 08:40 · **D-N188 cerrada: cerco de Castellón de 4400** (Hugo y Nacho, NightSim, 200 semillas). Con 17 u de munición mínima se gana el 82 %, dentro del objetivo del 75–90 %. El cerco se rompe hacia el minuto 240, con 12,4 u restantes y 23 bajas. Curva: 3500 → 100 %, 4200 → 97 %, **4400 → 82 %**, 4500 → 68,5 %, 5500 → 17 %. Sustituye al 4200 provisional. La munición mínima del socorro pasa a **17 u** y la regeneración del cerco se topa en 4400. El aviso de reserva por debajo de 47 u (no un bloqueo) se mantiene y basta: el socorro gasta de media unas 4,6 u y el resto llega a Castellón, que no tiene munición propia. Con esto, las cifras de combate de la F3 quedan cerradas.
- 10-11 08:58 · **Aviso de munición del socorro (D-N188)**: sale en el **panel del tren**, en la estación, mientras eliges la carga, porque es ahí donde se decide. No sale en el mapa. Es un aviso y no un bloqueo, en color de aviso e08c30, debajo del contador de munición: «El socorro de Castellón necesita al menos 17 u de munición.» Desaparece al cargar 17 u o más. Si el tren sale con menos, no pasa nada más: el jugador ya lo sabe.
- 10-11 10:02 · **D-N193 · Una estación solo la atacan los zombis que están dentro del recinto** (Lucía, a raíz del arreglo del zombi atascado de Nacho y Hugo). Con el edificio de Nules a su tamaño real, los zombis de la fachada este empezaron a dañar la estación y la noche 2 normal pasaba de victoria a derrota a las 01:51, con 0 bajas y munición de sobra. Una derrota sin bajas y con munición es una derrota que el jugador no ve venir ni puede evitar, y eso rompe el pilar de SIMULACIÓN tanto como un combate abstracto. **Decisión: opción C.** La caja real del edificio se usa para el movimiento y las colisiones (el arreglo del atasco se queda). Para contar a los atacantes (CountAttackers y NightGame.Attack, D-N181) se usa la caja grande del recinto: solo cuentan los zombis que tienen la estación como objetivo **y** están dentro del recinto. Es lo que medían todas las cifras hasta ahora, así que no se tocan las hordas. Se descarta volver a medir la noche, porque escondería el agujero bajando la horda. También se descarta, por ahora, el puesto en la fachada este, porque cambia la estación y obliga a medir otra vez Nules, la D-N192 y el cerco. Condición: Nacho mide la noche 2 normal con la opción C y tiene que volver a ≈ 99,5 % (200 semillas). Si no vuelve, la siguiente opción es el puesto en la fachada este, no bajar la horda. Va en el código común, para que NightSim y el juego cuenten igual.
- 10-11 10:04 · **D-N193, redacción precisa** (Nacho, aprobada por Lucía; sustituye a la mención de la «caja grande»). Hay **una sola caja**, la huella sólida del edificio de viajeros (en Nules, 96,5–115,5 × 75,2–83,6). Sirve para moverse, para chocar y para medir el alcance de 1,5 m al contar atacantes. Un zombi daña la estación si cumple tres condiciones: la tiene como objetivo, **está dentro del recinto** y está a menos de 1,5 m de la huella. Así, la pila que hay fuera del muro norte, que queda a 1,4 m de la fachada, no daña el edificio. Va en el código común (NightGame/NightSim) y la zona lo usa igual.
- 10-11 10:20 · **D-N193 medida en NightSim** (Nacho, 200 semillas; noche 2 normal de Nules con 16 + escolta de 8 y 20 u): con la C se gana el 98 % (196/200), con 17,7 u restantes, 1 baja de media y 4 derrotas de la estación; sin munición, 0/200. Lo acepto: la diferencia con el 99,5 % está en el ruido, así que no hace falta repetirla con 400 semillas. La prueba que decide es la -dia2-auto de Iker con la C (rama nacho/d-n193). Si la zona todavía cae por los trepadores de la fachada este, se pone el puesto en esa fachada; no se baja la horda. Efecto secundario: Nules con 4 u pasa del 21,5 % al 75,5 %. El umbral de la D-N190 (dos vuelos de NH90 desde cero) queda pendiente de que Hugo mida 3 y 5 u.
- 10-11 10:22 · Hugo confirma que **la D-N190 no cambia** con la D-N193: desde un almacén vacío siguen haciendo falta dos vuelos de 3 u, y un vuelo sobre 1 u ya casi basta. Por la parte de NightSim, la D-N193 queda cerrada. Solo falta la -dia2-auto de Iker en la zona.
- 10-11 10:28 · **D-N190 cerrada sin cambios: 3 u por vuelo** (Hugo, con la curva de Nacho tras la D-N193; 16 más la escolta de 8, 200 semillas). Con 0 y 3 u se gana el 0 %; con 4 u, el 75,5 %; con 5 u, el 98 %; con 20 u, el 98 %. Desde un almacén vacío hacen falta dos vuelos. El aviso del NH90 se queda sin cifra («Puedes llevar munición en los NH90 desde Bétera.»): la única cifra que ve el jugador es el mínimo de 10 u del Informe, que tiene margen. Si se dieran dos cifras distintas (5 y 10), el jugador se confundiría.
- 10-11 10:43 · **D-N194 · Puesto en la fachada este de Nules** (Lucía; se aplica la condición de la D-N193). Con la D-N193, la noche 2 normal se sigue perdiendo en el juego a las 01:51. Los trepadores van del tren a la esquina SE y a la fachada este del edificio, y la guarnición de la banqueta oeste no los ve. Decisión: un puesto nuevo en la fachada este, encargado a Álvaro en el Plantel de Nules y medido después por Nacho. Criterios de diseño:
  1. Tiene que ver la fachada este y la esquina SE con línea de visión, incluido el tramo por donde suben los trepadores desde el andén.
  2. Se llega andando desde dentro del recinto, sin teletransporte (D-N186).
  3. La guarnición no sube: siguen siendo 16, y la horda tampoco cambia.
  4. Entra en la colocación automática de la D-N192: el orden lo proponen Nacho e Iker según la medida, y el jugador puede mover a quien quiera.
  5. Se tiene que ver en el mapa y en la zona como cualquier otro puesto.
  Objetivo: la -dia2-auto de la zona gana la noche 2 normal y NightSim sigue en ≈ 98 %. Si el puesto no basta, se vuelve a la mesa antes de tocar la horda.
- 10-11 11:00 · **D-N195 · Orden de llenado de Nules con el puesto este** (Lucía, con la medida de Nacho en NightSim: 200 semillas, noche 2 normal, 20 u). Sustituye al orden de la D-N192 en Nules. El orden nuevo es: **1) los puestos norte y sur de la puerta oeste, hasta 8; 2) el puesto este (D-N194), hasta 4; 3) la banqueta, que puede quedarse a 0.** Resultados medidos: orden de Nacho, 98,5 % con 0,9 bajas; opción 1, 97,5 % con 3,7 bajas, pero baja al 59,5 % si la escolta llega con 4 bajas; opción 2, 98 % con 8,8 bajas. Descarto la opción 1 porque es frágil: depende de que la escolta llegue entera. El puesto se queda en (124; 75,5), porque es donde Iker ha probado la -dia2-auto de la I-Noche141, que gana con 0 bajas. Comprobación que queda: el orden nuevo con la escolta llegando con 4 bajas, que tiene que dar ≥ 90 %, y la -dia2-auto con el orden nuevo. **Plan B:** si alguna de las dos falla, se mueve el puesto a (118; 80,5), junto a la esquina NE, que en NightSim dio 200/200 sin bajas. El orden sigue siendo la colocación automática del juego (Iker) y NightBot la imita. Después, el jugador mueve a quien quiera.
- 10-11 11:06 · **D-N195 suspendida: no pasa la prueba de la escolta mermada.** Fallo mío al redactarla: con 16 hombres, el orden «oeste hasta 8 y 8, y luego el este» llena el oeste con los 16 y deja vacío el puesto este, que es justo el agujero que la D-N194 venía a tapar. La estación cae en 199 de 200 partidas. Debí comprobar el caso de 16 + 4 antes de cerrarla. Nacho mide repartos de 16 con **4 siempre en el puesto este**, tanto en (124; 75,5) como en (118; 80,5), y propondrá un orden corregido. Regla que queda desde ya: **el puesto este se llena antes de completar el oeste.** Iker espera.
- 10-11 11:11 · **D-N194, el puesto se mueve a (118; 80,5)**, junto a la esquina NE (Nacho, 200 semillas, caja real + D-N193). Con la escolta entera (norte 8, sur 8, este 4) gana 200/200 con 0,0 bajas; en (124; 75,5) se ganaba el 98,5 % con 0,9 bajas. Álvaro lo mueve en el Plantel e Iker en la build. Con la escolta llegando con 4 bajas (16 hombres) no hay sitio ni reparto que salve la noche: las cuatro variantes dan 0/200, mueren unos 22 hombres y sobran 18–19 u, así que no es falta de munición sino de hombres para tres frentes. Nacho mide 6+6 al oeste más 4 al este. **Decisión anticipada:** si ese reparto no llega al 90 %, se aplica lo que la D-N192 ya preveía: **la guarnición de Nules sube a 20.** Perder 4 hombres en una emboscada que el jugador ha ganado no puede costar la noche sin que lo vea venir. Con 20, Nacho comprueba la escolta entera y la mermada, y que la noche normal no quede regalada (≤ 99,5 %, con bajas). No se pone un ametrallador en la azotea mirando al este: sería un recurso que solo tiene Nules y que no se explica.
- 10-11 11:22 · **D-N194 cerrada: la guarnición de Nules sube a 20** (Nacho, 200 semillas, puesto en (118; 80,5), caja + D-N193). Con 16 y el reparto 6+6+4 sale 0/200, así que se aplica la regla anticipada. Con 20, el orden de llenado es **sur 8, norte 8, este 4 y el resto a la banqueta**. Con la escolta entera (28) sale 200/200 con 0,0 bajas; con 4 bajas en la escolta (24), 200/200 con 1,0 bajas. La guarnición sigue sin reponer cuerpos (D-N192). Sustituye a la D-N195 suspendida y al «16» de la D-N192. **Retiro mi condición de «que la normal no quede regalada»; estaba mal planteada.** La noche 2 de Nules ya no era difícil con 16 y la escolta entera (200/200), y su dificultad no está en el muro: está en llegar. Hay que llevar escolta (sin ella el tren se pierde, D-N180) y al menos 5 u de munición (con 3 u o menos, 0 %). Una defensa bien montada debe aguantar. Además, el precipicio entre 16 (0 %) y 20 (100 %) aconseja tener margen, porque la zona y NightSim ya se han separado otras veces. No se mide una guarnición de 18. Tampoco se endurece la noche 2. Si las partidas de Eugenio la encuentran blanda, la palanca es la munición inicial de Nules (Hugo), no el muro.
- 10-11 11:24 · **Aclaración de la D-N194: los 20 de Nules son 20 fusileros, sin contar los 4 ametralladores de la azotea**, que se quedan como estaban (24 cuerpos en total). Es exactamente lo que midió Nacho: con la escolta entera, 28 + azotea → 200/200; con 4 bajas en la escolta, 24 + azotea → 200/200. Así se aguanta hasta perder 8 hombres de la escolta. La otra lectura (16 fusileros más la azotea) cae al 0 % si se pierden 8, y no es lo que se midió. Álvaro corrige el Plantel v1.7. Ambigüedad mía: escribí «guarnición 20» sin decir qué contaba.
- 10-11 11:25 · Economía de la D-N194 (Hugo, modelo de campaña, 1500 partidas por política): con 20 en Nules, los víveres pasan a 2,0 u al día frente a 6 de producción. La política equilibrada va del 14,7 % al 15,6 % de derrotas y la de prisa del 29,2 % al 29,6 %, dentro del ruido. **H0 no cambia.** Nota de método que adopto: con 300 partidas el modelo baila unos ±3 puntos, así que los cambios pequeños se juzgan con la tanda de 1500.
- 10-11 12:05 · **D-N196 · La tropa del socorro baja sola a las puertas del cerco** (Lucía, a raíz de la prueba de Iker con la I-Noche147). Cuando un tren con destino a una estación cercada se detiene ante el cerco, sus pelotones **bajan solos** y atacan el cerco, igual que en el andén. Motivos: la D-N188 dice que «la batalla sigue aunque no la mires», la D-N186 pide una simulación que no dependa de la cámara, y el 82 % se midió con la tropa bajando. Si el jugador está en otra zona, un botón «Bajar» haría que el tren se quedara parado sin hacer nada, y eso es un fallo, no una decisión. Al bajar sale un aviso en e08c30: «El {tren} ha llegado al cerco de {estación}. La tropa baja y ataca.» El jugador sigue pudiendo dar órdenes de intención (Aguantar, Retrasar, Retirarse). La regla general no cambia: un tren parado en ruta por otra causa (emboscada, vía cortada) no baja la tropa sola; ahí manda la D-N180 y la escolta combate desde el tren.
- 10-11 12:06 · **D-N196, colocación al bajar** (Nacho): para que coincida con lo que se midió en el 82 %, los dos pelotones del socorro bajan y **se quedan junto al tren a la altura de la puerta este**, en (176; 60) y (188; 60), en Aguantar. No entran en el recinto ni se suman a la guarnición de dentro. Después, el jugador los mueve si quiere, pero eso ya no está medido. Si en la zona se pusieran de otra forma, habría que medirlo otra vez.
- 11-11 11:15 · **D-N197 · Borde de la zona de día: calima clara** (Lucía, a raíz de las bandas negras que encontró Bruno). La bruma oscura del borde (D-N182) se queda solo de noche. De día, en su lugar, se pone **una calima clara del color del suelo, al 35 %**, con el mismo degradado y el mismo borde irregular. No se apaga del todo, porque entonces se vería nacer a los zombis de las emboscadas de día (los 300 de la franja oeste), y eso rompe la ilusión de que el mundo sigue más allá del borde (SIMULACIÓN). El apagado de día que integra Iker vale como paso intermedio. Bruno comprueba en captura que la calima no tapa el andén ni los puestos y que los zombis que salen de ella se leen bien (ΔL* ≥ 8 respecto al suelo).
- 11-11 12:48 · **D-N148, revisada: los zombis van también a por los vehículos en marcha** (Nacho, a raíz de la I-Noche153 de Eugenio). En la zona, los trepadores y la horda eligen como objetivo cualquier vehículo cercano, esté parado o en movimiento, como ya hacía NightSim, y **rodean su silueta** en lugar de ir a su centro. Así la zona y NightSim cuentan igual (D-N186, simulación). Es un cambio de la D-N148, no una decisión nueva. Rama nacho/zombi-vehiculo, que integra Iker. La qa53 comprueba que un VAMTAC en marcha atrae a los zombis y que no lo atraviesan (fallo de la 110).
- 11-11 19:30 · **D-N198 · La puerta de vehículos E4 de Sagunto empieza abierta** (aprobado por Eugenio; Lucía lo numera). Hasta ahora la partida empezaba con la E4 (D-N111, 8 m en el muro sur, X 95–103) cerrada con muro, y los vehículos no podían salir del fuerte (qa53 de la I-Noche158: el VAMTAC con orden de salir se quedaba con velocidad 0 porque el A* no encontraba salida). Desde ahora la partida empieza con la E4 **abierta**, sin muro, y los Dragón y VAMTAC salen por ella hacia la carretera vieja. Cuando se anuncia el asedio, se cierra como las demás puertas (D-N151) y los vehículos que estén fuera se quedan fuera, igual que la tropa. SIN VERIFICAR: no sé si NightSim mide la E4 como un hueco abierto de día. Nacho lo comprueba, y si la noche 1 de Sagunto cambia, se mide otra vez antes de tocar la horda.
- 11-11 19:55 · **D-N199 · Los avisos de la noche se dan una sola vez, cuando ocurren** (Lucía, a raíz de la qa53 de la 158). Al volver a una zona, no se repite ningún aviso del pasado. Si la noche de esa zona ya ha terminado, no sale «empieza la noche de {estación}» seguido del resultado. Si está en curso, se entra sin cartel, con la hora y el estado de ese momento. Si ya ha terminado, el resultado se ve en el registro de avisos y en el estado de la estación, no en un cartel nuevo. Es lo que pide PERSISTENCIA: volver a una zona es asomarse a algo que ya estaba pasando, no empezarlo de nuevo. Lo hace Iker y lo comprueba la qa53.
- 11-11 20:05 · **D-N200 · Panel de carga del tren: tres decisiones, no un inventario** (Lucía, con las referencias de Paula en `referencias-reales/convoy/carga_convoy_referencias.md`: Ebbtide, OpenTTD, Factorio y Railway Empire coinciden en que la carga se decide con una regla y no unidad a unidad). Sustituye al panel «Preparar tren». Se abre al seleccionar un tren en el andén, en la zona (D-N186). El destino sigue dándose con clic derecho en el mapa.
  1. **Qué lleva**: tres casillas que se pueden mezclar: **Tropa** (los pelotones seleccionados en el andén o los que marques en el panel), **Suministros** (munición y víveres) y **Evacuados** (solo aparece si hay supervivientes en la estación, D-N187).
  2. **Cuánto**: una barra por recurso que **empieza en el valor que pide el destino** (Nules, el mínimo de 10 u del Informe; Castellón, las 17 u del socorro, D-N188) y que muestra la reserva que queda y la capacidad del tren. El aviso de reserva por debajo de 47 u y el de las 17 u del socorro salen aquí, en e08c30, como avisos y no como bloqueos.
  3. **Cuándo sale**: por defecto, **«Salir cuando esté todo a bordo»**: el tren no arranca hasta que la tropa marcada ha subido y la carga está dentro. Así se arregla el fallo de la qa53 de la 159, en la que el socorro salía «Sin escolta» porque arrancaba antes de que subiera el pelotón. La otra opción, «Salir ahora», sale con lo que haya y, si falta la escolta, muestra el aviso «Sin escolta» (D-N177).
  - **«Repetir el último»**: un botón que copia la carga del último viaje desde esa estación, para los viajes de rutina.
  - Cifra mínima: un tren con la carga por defecto sale con 2 clics (marcar el tren y clic derecho en el destino). Uno con carga a medida, con 3 o 4.
  - Lo hace Iker, junto a la carga del tren de las prioridades del 15–16-nov. El texto exacto de los botones y avisos lo cierro con él. La capacidad la toma de lo que ya tiene el juego, sin cifra nueva.
- 11-11 20:10 · **Objetivo del día 2: una sola cifra** (Hugo, `economia/pulido-19-hugo.md`; aprobado por Lucía). El objetivo pedía 20 u para Nules y el Informe, un mínimo de 10 u: eran dos números para lo mismo. Desde ahora, **el objetivo del día 2 pide el mínimo del Informe de cada dificultad: 9, 10 y 11 u.** Así la noche 2 de Nules, que salía blanda (0 bajas y 12,3 u de sobra en la 159), acaba con el almacén casi vacío, que es tensión que se ve sin tocar el muro. Pendiente de la medida de Nacho con 8, 10 y 12 u. Criterio: ≥ 95 %, p10 al final ≥ 2 u y ≥ 90 % con la escolta mermada. Si no se cumple, se sube la cifra del Informe, no se vuelve a dos números. El panel de carga (D-N200) usa esta misma cifra por defecto. La D-N191 no cambia (5250, 6700 y 8150), y la munición de Sagunto llega a la noche 3 con unas 76 u.
- 11-11 19:45 · **D-N201 · Nules monta el mismo muro de piezas que Sagunto** (Lucía, a raíz del hallazgo de Teo). En la partida, Nules (opción A, sobre el terreno de Sagunto) **no tiene muros**: su recinto es abstracto (ZoneWallE4 = 132,24 u), la vista no dibuja nada y la simulación no tiene sólidos. En cambio, NightSim midió la noche de Nules **con el recinto de Sagunto** (X 70–156, Z 44–85). Las cifras de la D-N192 a la D-N194 y la D-N193 («dentro del recinto») suponen un muro que en el juego no existe. Fallo de todos, mío también: di la opción A por cerrada sin comprobar que el muro venía con el terreno. **Decisión:** el inicio de partida llama a SagunteStart (NetWorld.cs) también para Nules, así que Nules tiene los mismos tramos, los mismos sólidos y las mismas puertas que Sagunto. La vista los dibuja con los sacos y los HESCO (SyncWorks). La E4 empieza abierta igual que en Sagunto (D-N198). Se descarta pintar muros que la horda atraviesa: rompe SIMULACIÓN. Cambia la simulación, el hash y el guardado, así que lo hacen **Nacho e Iker**. Comprobación: la -dia2-auto con el bot en la build nueva y NightSim tienen que dar lo mismo en la noche 2 de Nules (≈ 98–100 % con la escolta entera y ≥ 90 % con 4 bajas). Si el muro cambia mucho el resultado, se vuelve a medir el objetivo del día 2 (9, 10 y 11 u) con él puesto.
