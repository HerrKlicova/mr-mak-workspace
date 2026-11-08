# Sagunto · diseño del nivel (v1.2: frentes de la D-N113 con el nivel 1 de la escala; la v1.1 la aprobó Lucía)

Autor: Álvaro (Niveles) · 6-nov-2026 · Origen: Eugenio, 17:20: «¿es normal que la vía esté cortada? […] que tenga sentido, que sea realista, que se sienta vivo».
Revisión de cohesión: **Lucía** (última palabra). **Aprobado el 6-nov a las 18:27** con las correcciones de color y contenido de la v1.1 (abajo). Modelos: **Teo**. Integración: **Marcos** (vía Mak).
Plano: `docs/niveles/sagunto_plano_v1.png` (vista cenital de la zona de 256 × 128 m con lo que hay hoy y lo que propongo).
**Plano vigente (v1.2, 7-nov): `docs/niveles/sagunto_plano_v1_2.png`**, con los frentes, las calles de 10 m, la puerta sur, el parque y el helipuerto. Lo nuevo está en el **§10**, al final.

> Regla de la casa: cada vía, calle y muro tiene que tener una razón de existir. Si no sabemos contar por qué está ahí, sobra o está mal puesto.

---

## 0. La vía cortada: es un fallo, no el borde del mapa

**Diagnóstico** (repo TBD, commit 05936b1, `Assets/TBD/Scripts/View/PrototypeBootstrap.cs`, líneas 1622-1628):

- En la zona de Sagunto los raíles se dibujan con `railX = 55`, `railLen = 90`, es decir, de **X = 10 a X = 100**, y las traviesas de 12 a 100. Es un resto de cuando el fuerte medía 31 m (muros en X = 70 y 101; el propio comentario de `Level.TrainMinX` en `SimTypes.cs:363` todavía lo dice).
- Cuando el fuerte se alargó hasta X = 156 para el tren a escala real (Lucía, 6-nov), los raíles no se tocaron. Resultado: **la vía se acaba en X = 100, dentro del fuerte**, y la locomotora, que para entre X ≈ 74 y 154, tiene sus últimos ~37-54 m sobre la tierra.
- Al este no hay vía, pero los postes de catenaria sí siguen hasta X = 256 (línea 1232): postes que no sujetan nada.
- La zona de emboscada del desmonte sí dibuja la vía en todo el ancho (`railLen = WorldW`); solo falla Sagunto.

**Hay otros dos problemas en el mismo sitio:**

1. **El muro este (X = 156) está cerrado** (`Level.CreateSolids`, tramo «este»). Aunque se alargue la vía, chocaría con el muro. Sagunto es una estación de paso, no un fondo de saco: la vía tiene que poder salir.
2. **El bloque de pisos está encima de la vía.** Está centrado en (172; 70) y girado, así que ocupa Z de 63 a 77, y su colisión (5 segmentos de Z 64 a Z 76) cruza el eje de la vía (Z = 64,5). Hoy no se nota porque allí no hay raíles. En cuanto se alarguen, el tren atravesaría el edificio.

**Y uno más de cámara**: el suelo mide exactamente 256 × 128 m (línea 1602). Más allá no hay nada, y al alejar la cámara se ve el vacío azul oscuro en las esquinas (captura `sagunto_pueblo_v1.png`).

## 1. La lógica del lugar

### De dónde viene y adónde va la vía

En la red del juego (GDD §15) Sagunto es un nudo: pasa la **línea costera Valencia–Sagunto–Castellón** y de ahí sale la **línea a Teruel y Zaragoza**. En la realidad, la línea a Teruel se separa en una bifurcación propia fuera de la estación (en OpenStreetMap aparece un tramo de Adif llamado «Sagunt - Bifurcación Teruel»).

Convención de la zona (los ejes del código: +X es el este de la pantalla y +Z, el norte):

| Lado de la zona | Hacia dónde va en la ficción | Por qué |
|---|---|---|
| **Oeste (X < 0)** | **Valencia** | De ahí viene el tren y de ahí viene el desastre: la ciudad grande cayó primero |
| **Este (X > 256)** | **Castellón** y, pasado el río, la **bifurcación de Teruel** | Por ahí salen los trenes a las etapas 1 y 2 |
| **Norte (+Z)** | El **pueblo** viejo y, al fondo, el **cerro del castillo** | Yendo hacia Castellón, el casco y el castillo quedan a la izquierda |
| **Sur (−Z)** | La **huerta** y, lejos, el **Puerto de Sagunto** y el mar | Yendo hacia Castellón, el mar queda a la derecha |

La línea real va casi de sur a norte (SSO–NNE). Girarla 90° en la zona no se nota y deja intacta la orientación relativa: pueblo y castillo a un lado, huerta y mar al otro. Esto es una convención de juego, **no cartografía exacta**: no he verificado la posición del castillo respecto a la estación en un mapa oficial, solo que están cerca.

### Cómo terminan los extremos de la vía (fuera de cámara)

La vía tiene que salir por los dos lados y perderse fuera de lo que enseña la cámara. Propongo un remate en cada extremo que además cuente algo:

- **Oeste, hacia Valencia: un paso superior de carretera** que cruza por encima de la vía en X ≈ 18-26, con **coches abandonados encima** (el atasco de los que huían). Tapa el horizonte de la vía al alejar la cámara y es la «puerta» por la que entra la horda. Debajo, en la vía 2 (paralela, al sur, sin uso), un **tren de mercancías descarrilado** de 3-4 vagones tolva volcados: es la razón de que la vía 2 esté muerta y la primera huella del desastre que se ve al llegar.
- **Este, hacia Castellón: el puente sobre el río Palancia** (X ≈ 222-250). Un tablero metálico o de hormigón sobre un cauce casi seco, con cañas. Es geográficamente lógico (el Palancia pasa al norte de Sagunto y la línea a Castellón lo cruza) y deja preparado un punto de asedio para más adelante: el puente es un embudo.
- **Más allá de los 256 m**: la vía sigue sobre un «faldón» de suelo decorativo (ver P3) hasta que sale de la cámara a cualquier zoom de la zona. No hace falta un túnel: la costa de Sagunto es llana y un túnel no tendría razón de existir.

### La estación y el fuerte

- El fuerte es lo que el Mando levantó **alrededor de la estación**: el muro corta la plaza de la estación. Por eso el edificio de viajeros queda pegado al muro norte, con su fachada principal (la de la calle) mirando al muro. Detalle: la puerta principal **tapiada con sacos** por dentro.
- **Puerta de vía oeste** (la de hoy): por donde entra el tren desde Valencia.
- **Puerta de vía este** (nueva): por donde sale hacia Castellón y Teruel. En el MVP basta con que **se vea** (la misma puerta, cerrada, sobre el muro este, con la vía pasando por debajo). Que funcione cambia la simulación y el balance (8 u más de puerta de vía, D-N63): lo decide Lucía con Hugo y Nacho.
- **Almacén con muelle** al sur de la vía: se carga desde el tren. Lo mismo que hoy.

### El pueblo, la huerta y los caminos

- **Calle de la Estación** (nueva, de norte a sur) en X ≈ 56-62, entre el tejado de pruebas y el muro oeste. Cruza la vía con un **paso a nivel** (barreras rotas, una caseta). Une el pueblo con la carretera y la huerta. Es el único cruce de la vía en la zona, así que la horda y los obreros lo usan.
- **Carretera vieja** (nueva, de oeste a este) al sur, en Z ≈ 20-26, paralela a la vía, como la antigua nacional de la costa. Lleva el **atasco**: coches abandonados apuntando al este, todos huyendo de Valencia. Esa dirección cuenta la historia sin un texto.
- **El pueblo** (al norte): las casas valencianas de pueblo no son cajas sueltas en cuadrícula; van **entre medianeras, en hilera, con fachada a la calle**. Propongo dos hileras a lo largo de una calle paralela al muro norte (Z ≈ 97 y Z ≈ 109, como ahora, pero pegadas entre sí con 1-2 huecos), y **dos solares con escombros** junto al muro: casas que el Mando demolió para despejar el campo de tiro (de nuevo, una razón).
- **El bloque de pisos** se queda al este, fuera del muro, pero se aparta de la vía a (174; 82): fachada larga mirando a la vía, como tantos bloques de los 70 junto a las estaciones. **Lo mueve Marcos con su colisión** (P2).
- **El tejado de pruebas** (X 40-51, Z 30-51, el edificio de las caídas) se viste como **almacén de naranjas** (cooperativa o magatzem): nave baja con cubierta a dos aguas. Explica por qué hay un edificio grande en mitad de la huerta.
- **La huerta** (sur y este): naranjos en hileras (lo de hoy, más), separados por **acequias** y caminos de tierra. Al norte, detrás del pueblo, las hileras actuales.
- **Fondo**: la silueta del cerro del castillo en el borde norte del faldón, sin simulación. Se ve al alejar la cámara.

## 2. Recorridos

### La horda

La horda entra por el oeste (`SimWorldSetup.SpawnInitialHorde`: el asedio se concentra contra el muro oeste; la deriva, en el oeste de la zona). El espacio tiene que explicar ese flujo y darle tres caminos con carácter distinto:

1. **La vía (el río principal)**: el balasto es el camino más recto y despejado. Sale por debajo del paso superior y va directa a la **puerta oeste**. Por eso la puerta oeste es el punto débil, y el jugador lo entiende sin que se lo digan.
2. **La carretera y el atasco (sur)**: un flujo más lento que se cuela entre los coches y llega al **muro sur**. Si los coches tienen colisión, forman callejones; si no, son solo decorado. **Recomiendo que en el MVP no la tengan** (cambiaría el flujo y el balance de Hugo); se puede probar después.
3. **El pueblo (norte)**: las casas tienen colisión, así que las calles son embudos. La horda que se desvía al norte llega en goteo al **muro norte** a través de los callejones. Aquí se lucen las ametralladoras en las esquinas.

Para más adelante, cuando la Colmena aprenda: **el puente del Palancia (este)** es la entrada «por donde no miras». Un asedio que llegue por el este obliga a defender la puerta de vía este.

### El jugador

- **El tren**: entra por la puerta oeste, para en el andén (cola en X ≈ 74, locomotora en X ≈ 154) y sale por el este. Hoy sale marcha atrás por el oeste; con la puerta este cerrada, que sea así en el MVP es aceptable.
- **La tropa a pie**: sale por la puerta oeste hacia el paso a nivel, que es el cruce natural, y desde ahí al pueblo o a la carretera.
- **Campo de tiro**: entre el muro y lo primero construido tiene que haber 12-15 m libres. Hoy, al norte, entre el muro (Z = 85) y las casas (Z = 97) hay 12 m: vale. Al sur y al oeste no hay nada: vale. Nada nuevo puede meterse en esa franja.
- **Obreros y obras**: el paso a nivel y la calle de la Estación son el camino de los obreros al pueblo y a la huerta (para cuando haya trabajo fuera del muro).

## 3. La vida y las huellas del desastre

Nada de esto tiene colisión ni toca la simulación (salvo que se diga). Todo con la paleta de 32 y sin rojos de alerta en la decoración (`ambientacion-sagunto.md`).

**Lo que dice «aquí vive gente»** (dentro del fuerte y en el pueblo):
- **Humo** de una chimenea del edificio de viajeros (la cocina de los supervivientes) y de un **bidón con fuego** junto al almacén (de noche es luz cálida).
- **Ropa tendida** en las terrazas del bloque de pisos y en un patio del pueblo, en tonos apagados (sin ámbar ni rojo). Detalle valenciano y muy legible desde arriba.
- **Farolas del andén** encendidas de noche (ya previsto) y bancos.
- **Sacos, cajas y palés** en el muelle del almacén. Bidones de combustible junto a la vía.
- Un **huerto improvisado** dentro del fuerte, entre el almacén y el muro sur (bancales con tablones).

**Lo que dice «aquí pasó algo»** (fuera del muro):
- **El atasco** de la carretera vieja: 10-15 coches apuntando al este, puertas abiertas, uno quemado, una ambulancia (**sin cruz roja**, que es un emblema protegido: estrella de la vida o solo el rótulo, con el damero en tonos de la paleta).
- **El mercancías descarrilado** en la vía 2, al oeste.
- **Barricadas civiles** rotas a la entrada del pueblo: muebles, colchones, un autobús cruzado. El pueblo intentó defenderse y no pudo; el fuerte es la segunda línea.
- **Los solares** de las casas demolidas junto al muro.
- **Catenaria caída**: los cables cortados y colgando de los postes (ya previsto).
- **Columna de humo lejana** al **oeste**, sobre Valencia, que cayó primero (Lucía: la acería del Puerto no puede arder, porque produce los 80 u de materiales de Sagunto). Refuerza que el desastre viene del oeste y sirve de referencia visual a cualquier zoom.
- **Pintadas** en el muro y en el paso superior: «AQUÍ HAY VIVOS», una flecha a la estación. En **#d4d0cc** (espray blanco), nunca rojas. Las hace Bruno como decal.
- **Huellas en el suelo**: manchas de hollín en el balasto junto a la puerta oeste, donde siempre se rompe la horda (decal de Bruno, en **#303424 y #48403c**). Nada rojizo: se lee como suciedad, nunca como sangre.

## 3b. Lo que dicen las fotos de Paula (`referencias-reales/ambientacion/`, hoja `contacto_ambientacion.jpg`)

- **E4, casas encaladas**: son **alquerías**, casas sueltas en mitad de la huerta, no casas de pueblo. Encaja con la propuesta: el modelo `casa_baja` sirve para **2 o 3 alquerías dispersas en la huerta del sur**, solas entre naranjos, y el pueblo del norte va en hilera entre medianeras (para esto conviene una variante de fachada estrecha de Teo, de 6 m de frente).
- **E5, bloques**: de 6 a 8 plantas, con balcones corridos, toldos y **bajos comerciales**. Ahí van la ropa tendida y los toldos rotos. No está verificado que sean de los 70 (Paula ya lo avisa).
- **E10_4 y E10_5, huerta del Camp de Morvedre**: parcelas de naranjos en bancales con caminos de tierra entre ellas y **sierra al fondo**. Para el faldón: bancales con lindes y una línea de sierra baja en el horizonte oeste y norte, además del cerro del castillo.
- **E3_3, Almenara**: doble vía con andén ancho y catenaria a ambos lados. Confirma la vía 2 fuera del fuerte; dentro seguimos con una sola vía (decidido con Lucía).
- **E1_2, Sagunt**: la estación real es de ladrillo rojo con remates claros y balaustrada. El edificio de Teo es una lectura genérica de estación de pueblo, y la cohesión la decide Lucía; lo apunto por si se quiere un guiño.

## 3c. Lo que dicen las fotos de entorno de Paula (`referencias-reales/entorno/`, 6-nov 19:56)

- **F2_3, el Palancia en Sagunto**: el cauce es **ancho y seco**, con hierba rala, matorral suelto y grava, y escollera o muros en las orillas. **No es un cañar**: las cañas de H2 son del Palancia aguas arriba (Soneja). Además, **el puente de carretera va paralelo al ferroviario y muy cerca**, con pilas bajas parecidas, que es justo lo que pasa con la carretera vieja (Z 23) y la vía (Z 64,5) en nuestro faldón. Cambio en §8.2: el cauce es **hierba seca y matorral con densidad 20 y parches de cañas solo al pie de las orillas**, no «cañas, muchas».
- **F5_1, el castillo desde la llanura**: no es una torre sobre un cerro. Es una **cresta larga y baja**, de cientos de metros, con la muralla recorriendo todo el lomo, y el pueblo a sus pies con bloques de pisos. Para la silueta de Teo: un lomo alargado con la muralla almenada siguiendo la cresta y, detrás (F2_3), la sierra más alta y oscura de pinar. Va en el borde norte del faldón, paralela a la vía.
- **F5_1 también confirma el pueblo**: delante del cerro hay bloques de 5-8 plantas y solares con hierba seca alta y farolas. Encaja con el bloque de pisos y con el descampado.
- **F1, paso superior de la CV-32**: tablero de hormigón con pilas y estribos de escollera. Ya está en el modelo de Teo (sin pila central, §7d).

## 4. Lista priorizada para Marcos

Ordenada por lo que más cambia la lectura con menos trabajo. **P1 a P3 se pueden hacer ya y no tocan la simulación.**

| # | Qué | Dónde | Toca sim / hash | Esfuerzo |
|---|---|---|---|---|
| **P1** | **Vía en todo el ancho de la zona**: raíles y traviesas de X = 0 a 256, igual que en el desmonte. Añadir una franja de **balasto** (#48403c, 4 m de ancho) debajo | `PrototypeBootstrap.cs:1624-1628` (`railX = WorldW / 2`, `railLen = WorldW`, traviesas de 2 a WorldW) | No | 10 min |
| **P2** | **Apartar el bloque de pisos de la vía**: de (172; 70) a (174; 82), y su colisión con él | `BuildSaguntoAmbience`, `blk` | Sí, la colisión de la zona (si algún golden de zona incluye la ambientación, se regenera) | 10 min |
| **P3** | **Faldón y vía hasta fuera de cámara**: suelo decorativo del mismo color de X −250 a 506 y de Z −200 a 328 (sin simulación), y la vía sobre él hasta los extremos. Comprobar con el zoom más alejado de la zona que no se ve el vacío | Línea 1602 (suelo) y P1 | No | 30 min |
| **P4** | **Puerta de vía este** en el muro este, cerrada y solo visual (la vía pasa por debajo). Si Lucía decide que funcione, es un cambio de simulación aparte | `CreateSolids` (visual) | No (visual) | 20 min |
| **P5** | **Remates de los extremos**: paso superior de carretera al oeste (X ≈ 18-26) y puente del Palancia al este (X ≈ 222-250). Mientras Teo los modela, cajas de primitivas con la paleta | Ambientación | No | 1 h con cajas |
| **P6** | **Calle de la Estación con paso a nivel** (X ≈ 56-62) y **carretera vieja** (Z ≈ 20-26): franjas de asfalto en **#6c7874 con grietas en #48403c** (D-N61, textura A7 de Bruno) y caminos de tierra | Ambientación | No | 30 min |
| **P7** | **Pueblo en hilera**: casas pegadas entre medianeras a lo largo de las dos calles, con 1-2 huecos, y dos solares con escombros junto al muro. Usar las 5 variantes de casa con semilla (norma de variantes) | `houses` en `BuildSaguntoAmbience` | Sí (colisión de las casas) | 30 min |
| **P8** | **Vida**: coches del atasco, mercancías descarrilado, barricada civil, ropa tendida, humo (chimenea, bidón, columna lejana), palés y bidones | Ambientación + partículas | No | Por piezas, según lleguen de Teo y Bruno |
| **P9** | **Tejado de pruebas vestido de almacén de naranjas** y **silueta del castillo** al fondo | Ambientación | No | Cuando haya modelo |

**Reglas que no cambian** (de `ambientacion-sagunto.md`): solo tienen colisión los edificios (viajeros, almacén, casas, bloque y el tejado). Nada tapa la vía, el hueco de las puertas ni la franja de 12-15 m del campo de tiro.

## 5. Encargos para los demás

- **Teo**: paso superior de carretera (tablero de hormigón sobre dos estribos, con pretil), puente ferroviario sobre el Palancia (tablero metálico de celosía o de hormigón, 25-30 m), vagón tolva volcado, coche de los 2000 (2-3 variantes) y una ambulancia, caseta y barreras de paso a nivel, almacén de naranjas (nave de 11 × 21 m, a dos aguas), y una silueta baja del castillo para el fondo. Todo a escala real y con las fotos de Paula.
- **Paula**: fotos de un paso superior de carretera sobre la vía en la costa valenciana, del puente de la línea sobre el Palancia (o uno parecido), de un paso a nivel español con barreras, de un almacén de naranjas (magatzem) y del castillo de Sagunto visto desde la llanura. Las 32 fotos ya reunidas (`docs/arte/referencias/catalogo.md`, E1-E10) cubren el resto.
- **Bruno**: decales de pintadas, manchas en el balasto, marcas de neumáticos y escombros.
- **Hugo**: si los coches del atasco o la puerta de vía este llegan a tener efecto en la simulación, cuánto cambia el asedio.

## 6. Preguntas (resueltas por Lucía, 6-nov 18:27: sí a las tres recomendaciones)

1. **¿La puerta de vía este funciona en el MVP?** Recomiendo que no: solo visual. El tren sale marcha atrás por el oeste, como ahora. Funcional en el hito 7, con Hugo.
2. **¿Los coches del atasco tienen colisión?** Recomiendo que no en el MVP. Probarlo después como forma de dar callejones a la horda.
3. **¿Una segunda vía dentro del fuerte (vía de muelle junto al almacén)?** Recomiendo que no por ahora: la puerta tiene 5 m y una segunda vía obliga a ensanchar el muro. La vía 2 solo existe fuera, muerta, con el mercancías descarrilado.

## 7. Revisión de la build 8e567cc (Marcos, 6-nov 18:36)

Capturas: `sagunto_nivel_zoom_max.png` y `sagunto_nivel_oeste.png`. **Lo gordo está resuelto**: la vía va de borde a borde, no se ve el vacío al alejar, el bloque ya no pisa la vía y el pueblo está en hilera. Correcciones, por orden:

| # | Qué se ve | Por qué falla | Corrección |
|---|---|---|---|
| C1 | **La vía 2 vuelve a estar cortada**: raíles de X 10 a 100 en Z ≈ 59,5 | Mismo fallo que la vía 1: empieza en mitad del campo y entra en el fuerte atravesando el muro oeste (la puerta está en Z 62-67) | Vía 2 de X −250 a 50 y, de 50 a 64, un **desvío** en diagonal que se une a la vía 1 antes de la puerta. El paso a nivel cubre las dos vías (Z 58-67) |
| C2 | **Las tolvas parecen planchas o rampas** | Están giradas sobre Z (`Euler(0, yaw, ±28)`), así que levantan una punta. Un vagón volcado cae sobre su costado | Girarlas sobre su eje largo: `Euler(±75…90, yaw, 0)`, con los bogies (cajas oscuras) a la vista. Moverlas a X 30, 40 y 50: la tercera (X 51,5-60,5) tapa ahora la calle de la Estación |
| C3 | **El paso superior es una carretera que no va a ninguna parte** | El tablero acaba en el aire por los dos lados | Rampas de tierra (terraplenes en #b4a080 con asfalto encima) que bajan de 6 m a 0 en ~25 m: al sur se unen a la carretera vieja (Z 23) y al norte siguen como camino hacia el pueblo |
| C4 | **La carretera vieja cruza el Palancia sin puente** | El cauce (X 222-250) corta la carretera en Z 23 | Un tablero sencillo de hormigón para la carretera, como el de la vía. Y que la **cabeza del atasco** esté ahí: un camión cruzado en la entrada del puente que explica por qué se paró todo |
| C5 | **El atasco parece un aparcamiento** | 13 coches en fila con 9 m exactos de separación y casi rectos | Más juntos hacia la cabeza (el puente) y sueltos hacia la cola. Giros de ±25°, dos en el carril contrario, dos fuera del asfalto, en la huerta, y alguno con la puerta abierta (una caja fina a 60°) |
| C6 | **El cauce del Palancia es tierra plana** y el puente parece una tarima | El tablero está a 1 m sobre un suelo al mismo nivel | Motas (caballones de tierra de 1,5 m) a los dos lados del cauce, el lecho en #605c48 y matas de cañas (cajas finas en #506030 o el verde que diga Lucía) |
| C7 | **Las dos hileras de casas miran en la misma dirección** y quedan a 7,5 m del muro | Todas giradas 180°: la de atrás da la espalda a la de delante, y no hay calle entre ellas. Al muro le faltan 12 m de campo de tiro | La hilera de delante, a Z 101 y girada 0° (mira al norte); la de atrás, a Z 115 y girada 180° (mira al sur). Entre las dos queda una **calle** de tierra o asfalto (Z 104,5-111,5). Los patios traseros de la de delante dan al fuerte: ahí irá la ropa tendida. Naranjos a Z 124 y 128 |
| C8 | **Las hileras parecen naves o barracones** | La misma casa repetida con el mismo tejado | Mientras llega la casa de 6 m de Teo: usar sus 6 variantes por hash y que cada casa suba o baje 0,3-0,8 m de alero (alturas distintas entre medianeras) |
| C9 | **Los postes de catenaria se acaban en X 251** y la vía sigue hasta 506 | El bucle de los postes no se amplió | Postes de X −240 a 500 |

### 7b. Modelos de Teo y nueva posición de los remates (6-nov, 18:40)

Teo ha entregado el **paso superior** y el **puente del Palancia** (en el PC: `C:\Dev\mr-mak-workspace\herramientas\modelado-3d\sagunto\paso_superior` y `\puente_palancia`, LOD0 y LOD1 en `lod1\`). Medidas típicas, **SIN VERIFICAR** hasta que lleguen las fotos de Paula:
- **Paso superior**: vía a lo largo de X y carretera a lo largo de Z en Unity. Luz de 26 m entre estribos (33,8 m en total), gálibo de 7 m y rasante a 8,3 m. Origen en el centro de la base.
- **Puente**: vía a lo largo de X. Celosía de 28 m (42 m con estribos), 10 m entre vigas (vía doble). Carril a cota 0 y estribos que bajan 7 m.

**Cambio de plan: los dos remates salen de la zona simulada** y van al faldón. Con las medidas reales no caben bien dentro: el cauce necesita 7 m de hondo y los terraplenes del paso superior, unos 70 m de rampa por lado. Dentro de la zona, ni la simulación tiene ese relieve ni los terraplenes tienen colisión, así que los zombis los atravesarían. Fuera son solo decorado, no tocan nada y siguen tapando los extremos de la vía.
- **Paso superior** centrado en **X = −20**, Z = 64,5. Terraplenes con una pendiente del 12 %, que en juego se lee bien: el del norte llega hasta Z ≈ 150 y el del sur hasta Z ≈ −22. La carretera vieja (Z 23) pasa por debajo del terraplén sur por un paso inferior: un hueco de 10 m con una losa encima, a unos 5,3 m de altura.
- **Puente del Palancia** centrado en **X = 280**. Cauce de 28 m de ancho (X 266-294) y 7 m de hondo, abierto en el faldón: el faldón se parte en dos piezas y se rellena con un lecho en #605c48, taludes y cañas.
- La carretera vieja cruza el río por su propio tablero en X 266-294, y ahí está la **cabeza del atasco** (el camión cruzado). La cola del atasco entra en la zona.
- Esto **sustituye** a C3, C4 y C6 en su parte de posición. Lo demás de esas filas (rampas, cabeza del atasco, motas y cañas) sigue valiendo. Las primitivas que hay ahora en X 18-26 y 222-250 se quitan.
- La horda «por el puente» de más adelante sigue igual: entra en la zona por el borde este.

### 7c. Casa de pueblo de Teo (6-nov, 18:42; pendiente del visto bueno de Lucía)

`sagunto\casa_pueblo` (base y v1–v5), de 6 × 10 m, sin vuelo lateral y con la fachada a +Z en Unity. Sustituye a `casa_baja` en el pueblo; la `casa_baja` pasa a las alquerías de la huerta (§3b). Esto actualiza C7 y C8:
- **Hilera de delante**: Z = 103, girada 0° (fachada al norte, a la calle; espalda y patios al fuerte, a 12 m de la cara exterior del muro). 12 casas con paso de 6 m, X de 75 a 141, y huecos en la 5.ª y la 9.ª para los solares con escombros.
- **Calle del pueblo** entre Z 108 y Z 115 (7 m).
- **Hilera de atrás**: Z = 120, girada 180° (fachada al sur, a la calle). 12 casas, X de 75 a 141, con un hueco en la 4.ª que hace de callejón hacia la huerta.
- Variante por hash de posición entre las 6, con el alero subiendo o bajando de 0,3 a 0,8 m por casa. Colisión: una caja de 6 × 10 m por casa.
- **Naranjos** a Z 131 y 135 (ya en el faldón, sin colisión).

Siguen pendientes de la lista original: humo, ropa tendida y columna de humo sobre Valencia (P8), almacén de naranjas y castillo (P9) y la huerta con bancales y alquerías (§3b). **C1-C6 y C9 no tocan la simulación; C7 sí** (la colisión de las casas).

## 8. Mapa de zonas del suelo (para D-N67, `docs/arte/suelo-sagunto.md`)

Encargo de Lucía (6-nov, 18:32) a raíz de Eugenio (18:30): «no hay ningún asset ni sprites de hierba o algo, solo un color plano».

### 8.0 Trozo de muestra para Eugenio (prioridad, 6-nov 18:36)

Eugenio quiere ver el resultado y aprobarlo antes de producir nada en masa (D-N67 §0). Elijo **la esquina suroeste del fuerte: X de 20 a 95, Z de 5 a 70** (75 × 65 m). Es la escena que más cuenta del nivel: la puerta oeste por donde entra el tren y rompe la horda.
- **Encuadre de cámara**: foco en **(57; 0; 38)**, cámara de juego normal, con un zoom que abarque unos 75 m de ancho.
- **Archivos**: `sagunto_muestra_zonas_1m.png` (75 × 65 px, mismos ids que §8.2; la fila 0 es Z = 70) y `sagunto_muestra_vista.png` (vista previa).
- **Qué sale**, en m²: glacis 846, descampado pisado 951 (la entrada de la horda), huerta 881, calle y carretera 773, recinto 550, vía 448, descampado 272 y acequia 154. Además, el almacén de naranjas, la puerta oeste, el paso a nivel y el cruce de la calle con la carretera vieja.

| Zona en la muestra | Textura (de las 3 de Bruno) | Matas de Teo (3 + 2 piedras) | Densidad /100 m² |
|---|---|---|---|
| Recinto | Tierra apisonada con gravilla | Hierba seca, solo a menos de 2 m del pie de los muros | 4 en esa franja |
| Glacis | Tierra apisonada + decal de rodadas | Solo las 2 piedras, ≤ 0,3 m | 3 |
| Descampado pisado y descampado | Tierra apisonada (en la muestra no hay tierra seca) | Hierba seca y cardo | 8 y 25 |
| Huerta | Tierra labrada siguiendo las hileras | Hierba verde en las lindes y hojarasca (decal) bajo los naranjos | 10 |
| Calle y carretera | Asfalto agrietado | Hierba verde en las grietas, charco y aceite (decals) | 3 |
| Acequia | Agua: #6c7874 con borde de 1 px en #94948c, como los charcos (Lucía: el #605c48 daba L* 38,9) | Hierba verde en los bordes, sin cañas | 12 |
| Vía | Balasto (ya existe) | Ninguna (máscara: es la zona de la puerta) | 0 |

Con estas cifras salen unas 300 instancias en el trozo. Si en la captura el suelo se ve vacío, lo primero que hay que subir es la huerta y el descampado.

(19:25) **Eugenio aprueba la muestra y que se extienda a todo Sagunto** con el mapa completo. Densidades finales: las de §8.2, con el descampado a 20 y el recinto a 8 al pie del muro.

### 8.1 Archivos
| Archivo | Qué es |
|---|---|
| `sagunto_zonas_1m.png` | **Mapa de zonas**: 756 × 680 px en escala de grises, donde **cada valor es un id de zona** (0-11). 1 px = 1 m. Cubre el faldón entero, ampliado al norte para el castillo: X de −250 a 506 y Z de −200 a 480. La fila 0 es el norte (Z = 480) |
| `sagunto_sin_vegetacion_1m.png` | **Máscara**, en la misma rejilla: 255 = sin vegetación, 128 = glacis (nada de más de 0,3 m), 0 = libre |
| `sagunto_zonas.json` | Leyenda, ejes y conversión a UV de Unity: `u = (X + 250) / 756`, `v = (Z + 200) / 680` |
| `sagunto_zonas_vista.png` | Vista previa en color para personas (×2) |

Se generan con un script (`zonas.py`, copiado en `docs/niveles/herramientas/`). Si cambia una posición, se cambia allí y se vuelve a generar.

### 8.2 Zonas, textura y densidad
Densidad = matas u objetos de la capa C por cada 100 m² (orientativa: Marcos la ajusta con el criterio de FPS de §5 de D-N67). En el faldón, fuera de la zona simulada, se multiplica por 0,5, salvo en el cauce.

| Id | Zona | Dónde | Textura (Bruno) | Capa C | Densidad /100 m² | m² en la zona simulada |
|---|---|---|---|---|---|---|
| 1 | Recinto | Dentro del fuerte | Tierra apisonada con gravilla | Hierba rala solo a menos de 2 m del pie de los muros | **8** en esa franja (Lucía, tras la muestra); 0 en el resto | 3.182 |
| 2 | Glacis | 30 m al oeste (X 40-70) y 12 m al norte, al sur y al este | Tierra pisada con rodadas | Solo piedras y escombros sueltos, **≤ 0,3 m** | 3 | 4.026 |
| 3 | Vía | Franja de 4 m: vía 1, vía 2 y desvío | Balasto #48403c | Hierbajos entre traviesas solo fuera del recinto y lejos de las puertas | 6 | 1.252 |
| 4 | Calle | Carretera vieja, calle de la Estación, calle del pueblo, carretera del paso superior | Asfalto agrietado #6c7874 | Hierba en las grietas y los bordes, basura | 3 | 2.783 |
| 5 | Huerta | Sur (Z < 20), norte (Z ≥ 125) y este (X 180-262, Z 70-125) | Tierra labrada #a86c50 siguiendo las hileras | Hojarasca bajo los naranjos, hierba en las lindes | 10 | 9.304 |
| 6 | Descampado pisado | Oeste (X < 40, Z 26-125): la entrada de la horda, y la planta del almacén de naranjas | Tierra seca | Hierba seca baja, pisoteada | 8 | 3.871 |
| 0 | Descampado | El resto (sobre todo el este, entre la vía y la carretera) | Tierra seca | Hierba seca, cardos y matorral | **20** (Lucía, tras la muestra) | 6.164 |
| 7 | Pueblo | Patios y entorno de las casas (X 72-150, Z 98-125) | Tierra apisonada | Hierba en las esquinas y basura | 8 | 1.440 |
| 10 | Solar | Las dos casas demolidas (5.ª y 9.ª de la hilera de delante) | Tierra apisonada | Escombros y hierba crecida | 20 | 120 |
| 9 | Acequia | Madre a Z 9-11 por la huerta sur y ramales de norte a sur cada 40 m al sur de ella | **Agua: #6c7874 con borde de 1 px en #94948c** (el #605c48 baja de L* 47) | Hierba en los bordes; **cañas solo en el faldón (Z < 0)** | 12 | 626 |
| 11 | Cerro del castillo | Z ≥ 195 en todo el faldón (modelo de fondo de Teo) | — (el modelo lo tapa) | Ninguna (máscara a 255) | 0 | 0 |
| 8 | Cauce | Palancia, X 265,6-340,8 (fuera de la zona) | Lecho #605c48 con grava | Hierba seca y matorral suelto; cañas solo en parches al pie de las orillas (F2_3, §3c) | 20 | 0 |

Estimación: dentro de la zona simulada salen **unas 3.000 instancias** con estas densidades, más las del faldón que se vean. Queda muy por debajo del tope de 15.000 de D-N67, así que hay margen para subir la huerta o el descampado si Sara confirma que la horda se sigue leyendo.

### 8.3 Sin vegetación (máscara a 255)
(19:12) **Castillo**: el pie del cerro va en Z ≈ 195 y la cresta en Z ≈ 270, centrado en X = 130 (propuesta de Lucía). La calle de la Estación termina al pie del cerro (Z 195). Si Marcos necesita bajarlo, **puede llegar hasta Z = 150 sin pisar nada**: la hilera de atrás del pueblo acaba en Z 125, los naranjos en 135 y el terraplén norte del paso superior en Z ≈ 150 (en X ≈ −20). Por debajo de 150, el cerro se come la huerta y el terraplén. El mapa de zonas se ha regenerado con el cerro como zona 11.
La vía dentro del recinto · el paso a nivel, el desvío y la entrada de la puerta oeste (X 52-76, Z 54-73) · la puerta este (X 150-162, Z 58-71) · el andén · las huellas del edificio de viajeros, del almacén con su muelle, del almacén de naranjas, del bloque de pisos y de las casas · el paso superior con sus terraplenes · los muros.

**Las obras no van en la máscara fija**: el jugador construye donde quiere, así que una máscara no puede saber dónde. Regla para Marcos: **al terminar una pieza de `Works` (y al materializar la zona con las 120 u de D-N63), se ocultan las instancias de la capa C que caigan dentro de su huella más 0,5 m**. Es lo mismo que con los muros de partida, pero dinámico. La textura de la capa A no cambia.


**(19:16) Castillo girado 45°, sustituye a lo anterior.** La cámara está girada 45°: en pantalla, arriba es +(x + z) y a la derecha, +(x − z). La huella que propuso Marcos (400 × 80 m, con el frente en x + z = 219 y el fondo en 332) pisaba la vía desde la puerta este hasta X ≈ 267, la carretera vieja, la esquina NE del fuerte, el pueblo, el bloque y los naranjos: todo lo que tiene x − z > −55. **Arreglo: la misma huella, desplazada hacia la izquierda de la pantalla**, con la misma profundidad y la misma distancia al borde, de modo que se ve igual de alto:
- x + z entre **219 y 332** (lo de Marcos) y x − z entre **−460 y −60** (antes, entre −255 y 311).
- **Esquinas (X; Z)**: frente derecha (79,5; 139,5), fondo derecha (136; 196), fondo izquierda (−64; 396) y frente izquierda (−120,5; 339,5). **Centro (7,75; 267,75)**, mismo giro de 225° y escala Y de 0,5.
- **Comprobado**: queda entera fuera de la zona simulada (no necesita colisión) y a ≥ 5 m del pueblo y de los naranjos (que tienen x − z ≥ −55). No toca la vía, la carretera, el fuerte, el bloque, el puente ni el terraplén del paso superior (x + z ≤ 134).
- **La calle de la Estación se corta en Z ≈ 160** (donde x + z = 219).
- En pantalla, el cerro asoma por la **esquina superior izquierda**, encima del pueblo, en vez de en el centro. En la ficción es donde debe estar: detrás del pueblo, al otro lado de la vía.
- Mapa de zonas regenerado (zona 11 con esta huella).


**(19:51) Castillo a la derecha del borde: no cabe.** En (7,75; 267,75) queda bajo el HUD de alertas. Con la huella a 40-50 m del borde (x + z de ≈ 197 a 310), no pisar la vía exige x − z < 68 o x − z > 181, y no pisar la carretera vieja, x − z < 151 o x − z > 264. Con x − z < 68 caen el muro norte del fuerte, el pueblo y los naranjos, así que solo queda x − z > 264, la esquina superior derecha, encima del puente, con unos 15-20 m visibles. **Recomendación: fuera de cámara.** La alternativa es volver arriba a la izquierda, siempre que se estreche el HUD o que la cámara al máximo enseñe más hacia el norte.


**(19:53) Posición final, fuera de cámara (Lucía, opción C, adenda 5 de D-N68).** Ojo: (7,75; 267,75) **no** está fuera de cámara, es la que asomaba bajo el HUD.
- **Cerro del castillo**: girado 225° como antes, con escala Y de 0,5 y huella de 400 × 80 m, pero retirado detrás del borde superior: x + z entre **345 y 458**, x − z entre **−480 y −40**. **Centro (39,25; 361,25)**. Esquinas (X; Z): (152,5; 192,5), (209; 249), (−11; 469) y (−67,5; 412,5). El frente queda a ~19 m por detrás del borde superior de la cámara al máximo (x + z ≈ 318), y el ángulo de la cámara empuja la altura hacia arriba, así que no asoma.
- **Sentido para el pueblo**: queda justo detrás del pueblo, y **la calle de la Estación sube hasta su pie (se corta en Z = 286)**: es la calle que lleva del tren al casco viejo y al castillo, como en cualquier pueblo con estación al pie del cerro.
- **Sierra de pinar** detrás: banda de x + z ≥ 480 y x − z ≤ 200 (esquinas de referencia (340; 140), (−110; 590), (410; 210) y (−40; 660)). No toca la vía, la carretera ni el puente (todos tienen x + z ≤ 415 en esa franja). **El cauce del Palancia sale de la sierra**: el modelo de la sierra deja un valle en X 265-341 o el cauce termina al pie.
- **El faldón tiene que crecer hacia el norte** hasta Z ≈ 480 para que haya suelo bajo el cerro con la cámara libre.
- Se ve con la cámara libre y desde el mapa. Mapa de zonas regenerado.

### 8.4 Respuestas a Lucía
- **Glacis de 30 m al oeste: sí.** La capa C no tiene colisión, así que la anchura no cambia el flujo de la horda: es solo lectura, y 30 m dicen «campo de tiro» con claridad. Lo único que lo limita es lo ya construido. El almacén de naranjas (X 40-51, Z 30-51) se queda fuera del glacis; al norte de él, el glacis sí llega a los 30 m (X 40-70). La calle de la Estación y el paso a nivel lo cruzan con su propia zona. En el resto del perímetro le he dado 12 m, que es lo que hay hasta las casas por el norte.
- **Acequias**: la madre va **paralela a la carretera vieja, en Z 9-11, al sur**, y los ramales **bajan hacia el sur** cada 40 m. Ninguna cruza la carretera, la vía, la calle de la Estación ni los tres caminos de la horda. **Cañas solo en los tramos del faldón (Z < 0)**: dentro de la zona, una caña de 3 m a 10 m de la carretera taparía a los zombis que van por ella con la cámara mirando al norte.

## 9. Escala: «se siente todo muy pequeño» (Eugenio, 6-nov 23:55)

### 9.1 Diagnóstico (con el código de main, f5af670)
1. **La zona entera cabe en una pantalla.** La zona mide 256 × 128 m (`SimConst`: 512 × 256 celdas de 0,5 m). Con el zoom máximo (`_orthoSize` 90, es decir, 180 m de alto y unos 320 m de ancho en 16:9) se ve todo a la vez: el mundo se acaba donde se acaba la pantalla. Esa es la causa principal de la sensación.
2. **Calles de un solo carril.** La calle de la Estación y la carretera vieja miden 6 m y la calle del pueblo, 7 m. Un VCR 8x8 Dragón mide 3 m de ancho (V1_dragon_dimensiones.md); un VAMTAC, unos 2,2 m (SIN VERIFICAR). En 6 m no se cruzan dos blindados y un pelotón solo puede ir en columna.
3. **El fuerte no tiene dónde maniobrar.** El interior mide 84 × 39 m. La vía, el andén, el edificio y el almacén dejan una franja libre de unos 17 m al sur de la vía, en la que un 8x8 no puede dar la vuelta, y no hay ningún hueco donde aterrice un helicóptero.
4. **El helicóptero cruza la zona en segundos.** A unos 150 km/h (≈ 42 m/s) recorre los 256 m en ~6 s. No hay vuelo que sentir.

### 9.2 Medidas de referencia
- Helicópteros del Ejército: NH90 (HT-29), con rotor de 16,3 m; Cougar (HU-27), de 15,6 m; Tigre (HA-28), de 13 m. Son cifras de memoria y quedan **SIN VERIFICAR** hasta que Paula las confirme.
- Zona de toma: el manual de pathfinders del Ejército de EE. UU. (FM 3-21.38) da 50 m de diámetro despejado para un helicóptero medio (tamaño 3). También **SIN VERIFICAR** en la edición actual. Para el juego propongo un **mínimo de 30 × 30 m despejados** y una senda de aproximación libre de postes y tejados.
- Calzada real: una carretera nacional tiene unos 7 m de calzada y arcenes de ~1,5 m (orden de magnitud, sin fuente aquí).

### 9.3 Propuesta, en dos niveles
**Nivel 1: esta noche, sin tocar el tamaño de la zona** (todo visual salvo la puerta, que va marcada):
| # | Cambio | Ahora | Propuesta |
|---|---|---|---|
| E1 | Carretera vieja | 6 m (Z 20-26) | **10 m (Z 18-28)**: 7 m de calzada con **línea central discontinua en #b8b8b8** (nunca #d4d0cc, que es la selección) y arcenes de 1,5 m en #94948c. El atasco ocupa los dos carriles |
| E2 | Calle de la Estación | 6 m (X 56-62) | **10 m (X 54-64)**: 7 m de calzada y aceras de 1,5 m. El paso a nivel se ensancha igual |
| E3 | Calle del pueblo | 7 m | **9 m**: la hilera de delante se queda en Z 103 (12 m de campo de tiro), la calle pasa a Z 108-117 y la de atrás a Z 122 |
| E4 | **Puerta de vehículos** en el muro sur | No hay | **8 m de hueco en X 95-103**, con un camino de 8 m hasta la carretera vieja. Hoy los vehículos no pueden salir del fuerte, salvo por la vía. **Toca la simulación** (sólidos del muro y `Works`): Nacho/Marcos, y el coste, Hugo (como la puerta de vía, 8 u) |
| E5 | **Parque de vehículos** dentro del fuerte | No hay | **X 72-124, Z 46-60** (52 × 14 m), al sur de la vía, frente a la puerta nueva: 3 Dragón y 4 VAMTAC en batería, que salen de frente por E4. Nada de decorado en esa franja |
| E6 | **Helipuerto anexo** | No hay | **30 × 30 m despejados en X 165-195, Z 29-59** (centro en (180; 44)), con un anillo de HESCO bajo (1,2 m, como el del muro) y una **H en #b8b8b8 dentro de un círculo** (nunca ámbar). Está fuera del muro, al sureste, como la zona de toma anexa de una base avanzada. Queda a 5 m del poste de catenaria de X = 160 y la aproximación entra por el sureste, sobre la huerta. **Cabe un helicóptero medio** |

**Nivel 2: agrandar la zona de Sagunto (es lo que de verdad lo arregla).** Recomiendo **512 × 256 m**: el doble por lado, cuatro veces la superficie. Así la cámara al máximo deja de ver el nivel entero, hay sitio para un fuerte de ~120 × 70 m con patio de armas y helipuerto dentro, un pueblo con plaza, una huerta en la que se pueda luchar y unos 200 m de carrera de la horda hasta el muro (más tiempo para disparar). Con celdas de 0,5 m son 1024 × 512 celdas (×4); si el FPS no lo aguanta, con celdas de 0,75 m la zona sería de 384 × 192 m. **Lo deciden Marcos y Nacho midiendo el FPS** (ZombieGrid: 361 FPS con 10.000 zombis en la zona actual), y obliga a regenerar los goldens de zona. Si sale adelante, rehago la distribución completa (v2) sobre la zona nueva.

### 9.5 Entradas de las oleadas y posición inicial de los vehículos (zona actual de 256 × 128 m con el nivel 1; Lucía, 7-nov)
Nivel 1 aprobado por Lucía (P0, punto 6 de `docs/plan-noche-7nov.md`). Nivel 2 en P2: solo si cuesta menos de 1 h y el FPS aguanta.

**Entradas de las oleadas** (rectángulos de aparición en el borde oeste, uno por cada camino de §2):
| Id | Camino | Rectángulo (X; Z) | Peso inicial | Por qué |
|---|---|---|---|---|
| O1 | La vía | X 0-8, Z 56-73 | 50 % | Sale de debajo del paso superior y va recta a la puerta oeste |
| O2 | La carretera vieja | X 0-8, Z 14-31 | 30 % | Entre los coches del atasco, hacia el muro sur y la puerta de vehículos |
| O3 | El pueblo | X 0-8, Z 92-124 | 20 % | Por el descampado hacia la barricada y las calles del pueblo, hasta el muro norte |
| O4 (más adelante) | El puente | X 248-256, Z 56-73 | 0 % al principio | La Colmena aprende y entra por el este, «por donde no miras» |

**Vehículos al empezar** (en Unity, yaw 0 = mirando a +Z):
- **VCR 8x8 Dragón**: en el parque de vehículos, en **(99; 0; 53)**, yaw 180° (mirando al sur, hacia la puerta de vehículos de X 95-103). Sale de frente.
- **VAMTAC** (si los hay): (88; 0; 53) y (80; 0; 53), con el mismo yaw.
- **NH90**: en el centro del helipuerto anexo, **(180; 0; 44)**, con el rotor parado y yaw 270° (morro al oeste, hacia el fuerte). Despega hacia el sureste, sobre la huerta, sin pasar por la catenaria.

### 9.4 Boceto del nivel 2 sobre 512 × 256 m (7-nov; no entra esta noche, se decide con las medidas)
Plano: `sagunto_plano_v2_boceto.png` (script en `herramientas/plano_v2.py`). Misma lógica que la v1, con sitio de verdad:
- **Vía en Z = 128**, en el centro. Los remates (paso superior y puente) siguen fuera de la zona. La horda tiene **176 m de carrera** desde el borde oeste hasta la puerta oeste (hoy, 70).
- **Fuerte de 140 × 80 m** (X 176-316, Z 96-176), que sigue cabiendo con el tren de 64 m y sus 70 m de andén. Al sur de la vía: **parque de vehículos de 80 × 20 m** con la **puerta de vehículos** de 8 m en el muro sur y el almacén. Al norte: andén, edificio de viajeros pegado al muro y **patio de armas con helipuerto de 44 × 38 m dentro del recinto**.
- **Glacis** de 30 m al oeste y de 12 m en el resto.
- **Pueblo** al norte (Z 188-236): tres hileras de casas de 6 m con dos calles de 9 m y una **plaza mayor de 36 × 48 m con su iglesia**. La plaza es la zona de toma alternativa y el sitio para que maniobren los pelotones. Las calles llegan hasta la calle de la Estación.
- **Calle de la Estación** de 10 m (X 130-140) y **carretera vieja** de 10 m (Z 50-60) con el atasco.
- **Huerta** al sur con su acequia madre, ramales y 3 alquerías sueltas, y **huerta este** detrás del bloque de pisos.
- Para el tamaño del perímetro (440 m frente a los 254 de hoy) habría que recalcular el muro de partida de D-N63 con Hugo.


### 7d. Puente real del Palancia (6-nov, 18:45)
Las fotos F2 de Paula muestran que el puente ferroviario sobre el Palancia es un **viaducto de vigas de hormigón con pilas bajas y muchos vanos**, no una celosía. Decisión (Álvaro, a falta del visto bueno de Lucía a la v3 de Teo): viaducto fiel a la foto, de 4 o 5 vanos de unos 15 m, con el **estribo oeste en X = 262** y creciendo hacia el este por el faldón. La profundidad del cauce la fija Teo según las pilas de la foto. El paso superior se queda **sin pila central** (las vías están a 5 m entre ejes); como mucho, con pilas laterales.
- **v3 de Teo** (18:45, pendiente de Lucía): 75,2 m entre las caras de los estribos, 81,2 m hasta su trasera y 86,2 m con las aletas. El origen está en el centro, con el carril a z = 0. **Centro en X = 302,6** (la trasera del estribo oeste queda en X = 262, el puente llega a X ≈ 343). **Cauce de X ≈ 265,6 a 340,8, con el lecho a −4,5 m.** El tablero de la carretera vieja (Z 23) salva el mismo cauce, de unos 75 m. La cabeza del atasco, el camión cruzado, queda en X ≈ 258, a la entrada de ese tablero.

### 7e. Tolvas de Teo (6-nov, 18:51, aprobadas por Lucía)
`sagunto\tolva_volcada` (de v0 a v5). El vuelco ya viene en la malla y el origen está en el suelo, bajo el centro. Cada vagón mide 14 m entre topes, así que las X 30, 40 y 50 de C2 se solapan. **Nueva colocación** sobre la vía 2, en Z ≈ 59,5, de este a oeste: **X = 35, v0** (de pie y descarrilada: la cabeza del accidente, la primera en salirse); **X = 20, v2** (recostada a 75°, yaw +8°); **X = 5, v3** (sobre el costado con la grava derramada, yaw −12°). Así quedan entre X −2 y 42, lejos del desvío (X 50-64), de la calle (X 56-62) y del paso superior (X ≈ −20).

### 7f. Paso a nivel y almacén de naranjas de Teo (6-nov, 18:57)
- **Paso a nivel** (`sagunto\paso_a_nivel`, v0-v5, aprobado por Lucía): origen en el cruce de la calzada con el eje de las vías. Va en **X = 59, Z ≈ 63,6**, a medio camino entre la vía 1 y el desvío de la vía 2, que en X = 59 ya casi se han unido. Las barreras, a ±6,5 m, cubren Z 57-70. **La caseta tiene que quedar al oeste de la calle y al norte de la vía (X ≈ 51, Z ≈ 72,6)**: al este quedaría a 3 m del muro y de la puerta oeste. Se gira lo que haga falta para que caiga ahí. Mejor la variante con una barrera rota o levantada, si la hay. Se quitan las primitivas (caseta y barrera rota).
- **Almacén de naranjas** (`sagunto\almacen_naranjas`, v0-v5, pendiente de Lucía): 11 × 21 m, justo la planta del tejado de pruebas (X 40-51, Z 30-51). Centro en **(45,5; 40,5)**, con la fachada al sur, hacia la carretera vieja (girado 180°). **Ojo con la simulación**: el sólido del tejado es plano a 4 m (`Level.RoofH`) y ahí aparecen los zombis del «1 tejado». Hace falta el alero a ~4 m y la variante de cubierta más plana, o los zombis flotarán sobre los faldones. Marcos decide si se ajusta el sólido o se elige la variante.
- (18:58) Altura: la colisión del tejado es una caja plana de **4,0 m** (`Level.RoofH`). Lucía pidió alero a 5,5 m y cumbrera a 7,5 m, y he recomendado a Teo **ajustar el modelo**: alero a 4,0 m, cubierta de ≤ 5° o azotea con pretil, y cumbrera a ≤ 4,5 m. Cambiar RoofH obliga a recalibrar las caídas y los goldens de zona. Si Lucía prefiere la cubierta a dos aguas de verdad, Marcos sube RoofH a 5,5 m y vuelve a pasar las pruebas de caídas.
- (19:01) **Decisión de Marcos**: el sólido del tejado sube a 6,5 m y el almacén se queda a dos aguas. Por tanto, hay que recalibrar las caídas y regenerar los goldens de zona. Aviso de nivel: un sólido plano a 6,5 m bajo una cubierta de 5,5 a 7,5 m hace que los zombis floten 1 m sobre el alero y se hundan 1 m junto a la cumbrera. Desde arriba y en pixelado apenas se nota, pero conviene mirarlo en la captura. Si no convence, Teo tiene preparada una variante con azotea a 4,0 m que cuadra con RoofH = 4.

---

## 10. v1.2: los frentes de la D-N113 dentro de Sagunto, con el nivel 1 de la escala (Álvaro, 7-nov)

Encargo (plan-dia-7nov.md): llevar el nivel 1 de §9 (calles de 10 m, puerta de vehículos sur, parque y helipuerto anexo) a los frentes de la D-N113 (estación, paso a nivel y helipuerto dentro de Sagunto) y revisar C1–C9 en la build de Marcos.
Plano: **`sagunto_plano_v1_2.png`** (script `herramientas/plano_v1_2.py`). Mapa de zonas y máscara regenerados con la v1.2 (`zonas.py`). Dato de carreteras propuesto: **`mapa_sagunto_carreteras_v1_2.json`**.

**En una frase**: cada frente tiene ya un sitio con razón de ser, un puesto que lo defiende, un camino de vehículos que se puede contar («el ejército abrió un carril a empujones») y un corte visible donde el dato dice «no habilitada».

### 10.1 Revisión de la build de Marcos (rama `marcos/noche-prototipo`, 5188f83, leída en el código, sin Unity)
| # | Estado | Qué hay (archivo de `Assets/TBD/Scripts/`) |
|---|---|---|
| C1 | ✅ | Vía 2 de X −250 a 50 y desvío de 50 a 64 (`View/PrototypeBootstrap.cs:1450`) |
| C2 | ✅ | Tolvas de Teo v0, v2 y v3 en X 35, 20 y 5, con yaw 0, +8 y −12 (`:1459`) |
| C3 | ✅ ⚠️ | Paso superior con terraplenes al 12 % y losa sobre la carretera (`:1394`). **Pero** el dato lo da por no habilitado con «coches abandonados encima» y encima no hay ningún coche: ver 10.6, punto 8 |
| C4 | ✅ | Tablero de la carretera sobre el cauce y camión cruzado en X 258 (`:1409`) |
| C5 | ✅ | Atasco irregular (`:1437`). Con la carretera de 10 m hay que mover los carriles: ver 10.4 |
| C6 | ✅ | Cauce a −4,5 m con orillas y cañas (v1.3) |
| C7 | ✅ | Hileras en Z 103 (0°) y Z 120 (180°) (`:1345`). E3 pide la trasera en Z 122 |
| C8 | ✅ | Variantes de casa por hash y alero de distinta altura |
| C9 | ✅ | Postes de X −240 a 500 (`:1340`) |
| E1 | ❌ | Carretera vieja todavía de 6 m, Z 20-26 (`:1435`) |
| E2 | ❌ | Calle de la Estación todavía de 6 m, X 56-62 (`:1423`), y el paso a nivel igual (`:1425`) |
| E3 | ⚠️ | Calle del pueblo de 7 m (falta mover la hilera trasera a Z 122) |
| E4 | ✅ sim · ❓ vista | La simulación ya tiene la puerta de 8 m (D-N111, G3) y los vehículos cruzan el muro sur por X 95-103 (`View/PrototypeBootstrap.Vehicles.cs:106`). No encuentro dónde se dibuja la hoja doble, y el modelo de Teo (`SM_PuertaVehiculos`) no está en `Resources/Models` |
| E5 | ✅ | Dragón en (99; 53) y VAMTAC en (88; 53) y (80; 53), yaw 180 (`Vehicles.cs:56`) |
| E6 | ⚠️ | El NH90 está en (180; 44) con yaw 270, pero **el helipuerto de Teo no está importado**: hoy el helicóptero se posa sobre la tierra, sin losa ni balizas |

Además, el dato `StreamingAssets/Noche/mapa_sagunto_carreteras.json` tiene dos incoherencias de lugar: (1) la calle de la Estación está habilitada hasta Z 160 y atraviesa el autobús cruzado y la barricada de Z 88-97, y (2) la carretera vieja se corta en X 222, donde no hay nada que lo explique (el camión está en 258). Las corrijo en 10.3.

Lo visual (colores con la luz de noche y lectura a ortho 12) queda ❓ hasta las capturas de Marcos.

### 10.2 Los frentes
Todo dentro de la zona simulada (0–256 × 0–128 m), así que todo se ve desde la cámara de juego. Las ETA son **cuentas mías** con la fórmula de la D-N120 (5 s + 4 s por giro + metros ÷ velocidad; Dragón a 80 km/h y accesos al 60 %), **no medidas**.

| Frente | Sitio del dato | Qué se defiende y por qué ahí | Puesto | Camino desde el parque | Le amenaza |
|---|---|---|---|---|---|
| **F1 Estación** | (112; 78) | El edificio de viajeros y el tren en el andén: es lo que pierde la noche (D-N104) | El recinto entero; no lleva puesto | Dentro del recinto, en línea recta | O1 por la puerta oeste, O2 por el muro sur y la puerta de vehículos, O3 por el muro norte |
| **F2 Paso a nivel** | (59; 62) | El cruce de la calle con las vías, a 11 m de la puerta oeste. Es donde se juntan O1 (la vía) y O3 (el pueblo) antes del muro. Si cae, la horda llega a la puerta de vía y los vehículos pierden la calle | **v2 HESCO en (43; 0; 82), yaw 90**: en el glacis, al noroeste del cruce, con la entrada al este, hacia la calle. Ve la vía hacia el oeste (35 m hasta O1) y la calle hacia el pueblo | Puerta sur, carretera hacia el oeste y calle hacia el norte: **109 m, ≈ 19 s** | O1 y O3 desde el principio |
| **F3 Helipuerto** | (180; 44) | El NH90 y su rearme. Al principio es retaguardia; cuando se abre O4 (la Colmena entra por el puente, «por donde no miras»), pasa a ser frente. Es el frente que cambia a lo largo de la noche | **v2 HESCO en (207; 0; 51), yaw 270**: al este del helipuerto, entre la losa y el puente, con la entrada al oeste, hacia la losa. Ve la vía y el puente (O4, a 41 m) | Puerta sur, carretera hacia el este y acceso al norte: **132 m, ≈ 21 s** | O4; O2 si rebasa el muro sur |
| **F4 Tren** | (−68; 64,5) | El tren llegando por la vía 1 hasta el andén (D-N91, unos 320 m de vía de entrada) | No lleva: es un muro móvil (D-N27) | Por la vía | O1 mientras llega |

Sobre F4: en el dato es un punto fijo, pero el tren se mueve. Lo lógico es que el sitio siga al tren y se quede en el andén al parar (X 135-151,5). Lo decide Nacho; no lo he tocado.

Medidas de los puestos (sacadas de los FBX de Teo): la v2 ocupa 14,3 × 16,4 m con la chicane, y su entrada mira a +Z con yaw 0. F2 queda en X 35,9-52,2 y Z 74,9-89,1: a 1,8 m de la calle de 10 m, a 1 m de la caseta del paso a nivel y fuera del autobús y la barricada. F3 queda en X 197,8-214,1 y Z 43,9-58,1: a 1,2 m de la losa del helipuerto v4 (que sobresale hasta X 196,6), a 2,8 m del poste de catenaria de X 210 y fuera de la senda de aproximación (sureste).

### 10.3 Carreteras habilitadas y cómo se ven
El dato manda (D-N113), pero en el suelo tiene que verse lo mismo que en el mapa. Propuesta de dato en `mapa_sagunto_carreteras_v1_2.json`, con los sitios igual que ahora:
- **`calle_estacion`**: habilitada de Z 20 a **86**. Nuevo **`calle_estacion_norte`**, de Z 86 a 160, **no habilitada**: «autobús cruzado y barricada a la entrada del pueblo».
- **`carretera_vieja`**: habilitada de X −250 a **200**. **`carretera_vieja_este`**, de 200 a 320, no habilitada: «atasco cerrado hasta el camión cruzado en el puente».
- `paso_superior`: sin cambios (no habilitado). Aviso para cuando se habilite: el grafo cruza tramos perpendiculares, así que crearía un cruce falso con la vía en (−20; 64,5) y con la carretera en (−20; 23), y los dos son a distinto nivel. Hará falta una marca de «sin cruce».

**Cortes de carretera de Teo** (aprobados, 03:28) donde el dato dice «no habilitada»:
- **K1**: `SM_CorteCarretera` en **(201,5; 0; 23), yaw 90**, atravesado en la carretera (8,8 m de 10).
- **K2**: en **(59; 0; 86), yaw 0**, delante de la barricada civil: el ejército cerró la calle detrás de lo que dejaron los vecinos.

**Balizas de ruta de Teo** en lo habilitado (14, luces f0dc9c; el modelo mide 4,2 m a lo largo de su Z):
- Borde norte de la carretera, Z 28,8, yaw 90: X 70, 86, 110, 126, 142, 158, y 174 y 186 a los lados del acceso al helipuerto.
- Camino de la puerta sur, Z 36, yaw 0: X 94,2 y 103,8.
- Calle de la Estación, yaw 0: (53,2; 40), (64,8; 40), (53,2; 52) y (64,8; 52).

### 10.4 El atasco con la carretera de 10 m: carril norte abierto
Con E1 la carretera va de Z 18 a 28. Para que el camino de los vehículos tenga sentido (y no atraviesen coches), la historia es: **el ejército abrió el carril norte a empujones** desde la calle de la Estación hasta el helipuerto.
- De **X 64 a 200**: carril norte (Z 23-28) libre. Los coches van al carril sur (Z 19-22) o a la cuneta sur (Z 15-17, en la huerta), y uno de cada tres girado unos 60°, como empujado de lado.
- De **X 200 a 250**: atasco cerrado en los dos carriles, más junto (4,5-6,5 m), hasta el camión de X 258. Ahí va K1.
- Los «fuera del asfalto» del código (Z 25,2 y 17,8) ya caen dentro de la carretera de 10 m: pasan a **Z 16 y Z 30**.

### 10.5 Helipuerto (cambia algo respecto a E6)
- **Modelo de Teo v4** (de noche con torre de focos, con su luz real), en **(180; 0; 44), yaw 0**. Con yaw 0 la torre y la manga quedan al este, lejos del muro. Si cuesta FPS, la v0 (losa). Lo elige Lucía o Mak; yo recomiendo la v4 porque la partida es de noche.
- La losa del modelo ya mide unos 30 × 30 m con sus balizas. **Quito el anillo de HESCO de E6**: tapaba el paso de los soldados a la losa y sumaba instancias. Ahora defiende el helipuerto el puesto F3.
- **Set de rearme** de Teo, entre el muro este y la losa: en la franja **X 159-164, Z 31-41**, que es por donde llega la munición desde el recinto. Queda a más de 7 m del disco del rotor (NH90 de 16,3 m de rotor, SIN VERIFICAR).
- Aproximación y salida por el **sureste**, sobre la huerta. El poste de X 160 queda a 5 m de la esquina noroeste y el bloque de pisos, 16 m al norte: los dos están fuera de esa senda.

### 10.6 Lista para Marcos (vía Mak), por prioridad
1. **E1 y E2**: carretera vieja de 10 m (centro Z 23, ancho 10) con línea central discontinua en b8b8b8 (0,15 × 3 m cada 6 m) y arcenes de 1,5 m en 94948c; calle de la Estación de X 54 a 64 y paso a nivel de 10 m de ancho. Subir el `sagunto_zonas_1m.png` y el `sagunto_sin_vegetacion_1m.png` v1.2 a `Resources/Suelo` (con la misma vuelta en Z que ya les das).
2. **Helipuerto de Teo v4** en (180; 0; 44), yaw 0.
3. **Puerta de vehículos** de Teo en (99; 0; 45), yaw 180 (corregido el 8-nov, §10.9), o la hoja doble a partir de `Works` (lo que tengas previsto para la D-N111).
4. **Puestos de frente v2**: F2 en (43; 0; 82) con yaw 90 y F3 en (207; 0; 51) con yaw 270, con el hijo `Luces` según el IMPORTAR.md de Teo.
5. **Atasco con el carril norte abierto** (10.4) y los cortes K1 y K2.
6. **Dato de carreteras v1.2**: copiar `mapa_sagunto_carreteras_v1_2.json` sobre los dos `mapa_sagunto_carreteras.json` (Data y StreamingAssets).
7. **Balizas de ruta** (10.3) y **set de rearme** (10.5).
8. **Tres coches sobre el paso superior**, a la cota del tablero (8,3 m), en Z 56, 66 y 74, con giros distintos. Así se ve por qué el dato lo da por cortado.
9. **E3**: hilera trasera de Z 120 a 122.
10. **Después del P0** (10.8): puerta oeste-sur en (70; 0; 53), yaw 270 (corregido el 8-nov, §10.9); los VAMTAC pasan a (110; 53) y (118; 53); dato v1.3 con `acceso_oeste` y `acceso_sur`; armario de Adif en lugar de la caseta del paso a nivel.

Coste: unas 30 piezas nuevas (14 balizas, 2 cortes, 2 puestos, el helipuerto, la puerta, 3 coches y el rearme). Con el margen de 32 FPS, se mide antes de darlo por bueno (regla de D-N70).

### 10.8 Añadidos a la v1.2 (Álvaro, 7-nov, 08:55): F4 móvil, ETA medidas y acceso oeste para F2
**F4 Tren, decisión de Mak:** el sitio sigue al tren. La ETA se calcula en el momento de la orden con la posición que tiene el tren entonces, y la unidad que ya va de camino mantiene su destino aunque el tren siga avanzando. Al parar, el sitio queda en el andén (X 135-151,5). Hoy `Units/Transporte.cs` lo tiene fijo en (−68; 64,5): el cambio es de Nacho.

**ETA medidas por Nacho** (`TransportDirector.Estimate` sobre el `mapa_sagunto_carreteras.json` actual, pelotón de fusileros, salida desde el parque (99; 53); el total incluye subir, salir, giros y bajar, y entre paréntesis va solo el trayecto). Sustituyen a mis cuentas del 10.2 (19 s y 21 s), que eran casi en línea recta:

| Destino | Dragón | Pizarro | A pie | Recorrido en vehículo |
|---|---|---|---|---|
| F2 puesto (43; 82) | 36 s (32) | 34 s (30) | 37 s | 145 m: puerta sur, carretera vieja y calle de la Estación |
| F3 helipuerto (180; 44) | 31 s (27) | 29 s (25) | 47 s | 132 m |
| F3 puesto (207; 51) | 35 s (31) | 32 s (28) | 62 s | 166 m |

**F2: a pie se llega igual que en Dragón.** Mak pide que el vehículo compense. Lo he mirado de las dos formas que propuso:
- *Acercar el puesto a la calle* no arregla nada. El puesto ya está a 1,8 m de la calle de 10 m, y lo que alarga el viaje en vehículo es el rodeo por la puerta sur (salir hacia el sur, ir 40 m al oeste y subir 60 m por la calle), no los últimos metros. Pasarlo al otro lado de la calle, entre la calle y el muro oeste, acortaría todavía más el camino a pie (sale por la puerta oeste) y lo metería en el embudo de O1.
- **Elijo el acceso: una segunda puerta de vehículos en el muro oeste**, la **puerta oeste-sur**, al sur de la vía. Es el mismo modelo de la D-N111 (8 m, dos hojas de 4 m) en **(70; 0; 53), yaw 270** (corregido el 8-nov, §10.9), abierta en Z 49-57. La historia: el ejército abrió el muro por el lado del parque para llegar al paso a nivel sin dar la vuelta por la carretera.
  - **ETA medida por Nacho con la v1.3** (desde el parque): F2 **Dragón 25 s (21 de trayecto, 85 m), Pizarro 24 s, a pie 37 s**. El vehículo gana por 12 s. Helipuerto F3: Dragón 30 s, Pizarro 28 s. Puesto F3: Dragón 32 s, Pizarro 30 s. Las dos de F3 mejoran un poco respecto a la tabla de arriba.
  - **Hace falta también `acceso_sur`** (de (99; 53) a (99; 23), por la puerta de vehículos hasta la carretera vieja). Sin él, la ruta enganchaba el parque al `acceso_oeste` y todo salía por el oeste, de modo que F3 subía a 40 y 43 s. Lo encontró Nacho y lo dejó probado.
  - Recorrido (mi cuenta previa, solo trayecto): parque (99; 53) → hacia el oeste por Z 53 hasta la puerta (30 m) → calle de la Estación en (59; 53) (10 m) → hacia el norte cruzando el paso a nivel hasta (59; 82) (29 m). Son unos **69 m y 2 giros**. Con la fórmula de la D-N120 salen **≈ 18 s de trayecto y ≈ 22 s en total en Dragón, frente a 37 s a pie**. Es una cuenta mía: la medida la saca Nacho con el dato v1.3.
  - Coincide con las balizas que ya estaban en (53,2; 52) y (64,8; 52): la calle ya tenía marcado ese cruce.
  - **Para que el carril quede libre, los dos VAMTAC del parque pasan de (80; 53) y (88; 53) a (110; 53) y (118; 53)**, con yaw 180. Siguen en el parque (X 72-124) y fuera del paso de la puerta sur (X 95-103). El Dragón no se mueve.
  - **No rompe la defensa del paso, pero añade un punto débil**: la puerta queda a 6 m de la puerta de vía y mira hacia O1. La cubre el propio puesto F2 (desde X 36-52 y Z 75-89 ve la calle hasta Z 53) y, cerrada, aguanta como la puerta sur (misma vida que en la D-N111). La horda de O1 ya va hacia la puerta de vía, así que no se abre un camino nuevo; se suma un segundo blanco al mismo frente. Hay que confirmarlo con una corrida de Sara.
  - **Entra después del P0.** Tocar los muros del recinto mientras Marcos y Nacho cierran el pasillo de qa20 sería mezclar dos cambios en la misma prueba. Primero Sara gana la normal y después se abre la puerta.
- Dato: `mapa_sagunto_carreteras_v1_3.json` = v1.2 + los tramos **`acceso_oeste`** de (99; 53) a (59; 53) y **`acceso_sur`** de (99; 53) a (99; 23), los dos habilitados.
- F4 que sigue al tren: Nacho lo mete en `Transporte.cs` cuando se cierre el P0 (ahora solo se toca la calibración). Hasta entonces sigue fijo en (−68; 64,5).

**Referencias de Paula para F2** (`referencias-reales/entorno/P1`–`P4`, Adif, ancho ibérico): semibarreras con luces y armario, cruz de San Andrés con STOP, señal de «paso a nivel a 20 m», vista por el eje y placas entre carriles. **Cambio:** la «caseta» del paso a nivel (§2 y 10.2) pasa a ser **un armario de Adif**, porque en las fotos actuales lo que hay junto a la barrera es un armario y no una caseta de guardabarrera (de esas Paula no ha encontrado ninguna). Además deja más hueco al puesto F2, que antes estaba a 1 m. El resto del paso a nivel (barreras rotas, placas entre carriles y señal de 20 m en la calle, en el lado del pueblo) se viste con estas fotos. SIN VERIFICAR: la línea Valencia–Sagunto, las P-8 y P-9 de cerca y las cotas.

### 10.7 Pendiente de otros
- ~~Nacho: si el sitio del tren sigue al tren~~ Decidido por Mak: lo sigue (10.8). **Nacho**: la ETA de F2 con el dato v1.3 y la marca de «sin cruce» para el paso superior (10.3).
- **Lucía o Mak**: helipuerto v4 o v0.
- **Nivel 2** (512 × 256) sigue en P2, pendiente de las medidas de FPS de Nacho y Marcos (§9.3).

### 10.9 Puerta de vía y yaw de las puertas (Álvaro (3), 8-nov, 10:25)
**Criterio de yaw para puertas y muros (lo ha preguntado Teo).** En las piezas de Teo, el lado de fuera es +Z de Unity con yaw 0, y el yaw gira +Z hacia +X. El lado de fuera tiene que mirar fuera del recinto, de modo que:
- En el muro oeste (fuera = −X), **yaw 270**.
- En el muro sur (fuera = −Z, hacia la carretera vieja), **yaw 180**.
- En el muro este (fuera = +X), yaw 90. En el muro norte, yaw 0.

Con esto quedan corregidas la **puerta oeste-sur, de yaw 90 a 270**, y la **puerta sur, de yaw 0 a 180**. En el código, la hoja doble de la puerta sur todavía no se dibuja (§10.1 E4), así que no hay nada colocado que mover; SIN VERIFICAR hasta revisar la Noche57. Los puestos de frente no cambian, porque su yaw indica hacia dónde mira la entrada y no un lado de fuera.

**Puerta de vía (Bloque 2, D-N151; modelo de Teo en mr-mak 465da15, aprobado por Lucía; `entregas/teo-modelado/puerta-via/`):** va en **(70; 0; 64,5), yaw 270**. El hueco es de 5 m, en Z 62-67, y por él solo pasa la vía 1. Lleva dos hojas batientes de 2,5 m que abren hacia dentro y miden 2,1 m de alto. Al lado está el **tramo HESCO del tutorial**, al norte, en **(70; 0; 72,9), yaw 270**, en Z 67,9-77,9, a tope con la jamba norte de la puerta (Z 67,0-67,9; propuesta de Teo); empieza al 45 % (tutorial-textos.md:41). Al sur no cabe, porque entre Z 57 y 62 solo hay 5 m.
- **Datos de Marcos leídos en el código (8-nov, 10:33).** El muro oeste está en `Level.FortX0` = 70, con el sólido de X 70 a 72 y las piezas visibles de Obras centradas en X 70,0. Por eso todo lo de esta sección va en **X = 70**, no en 69: el 69 era el borde del hueco en mi croquis. El sólido mide `Level.WallH` = 2,5 m y las puertas se cierran con BuildWall de 2500 mm. La pieza visible de HESCO mide 2,1 m (D-N59 habla de la pieza) y los sacos bajos del sur, 1,2 m (de ahí la cifra de §9 E6). Los muros de la escena no tienen yaw; el 270 vale para los modelos de Teo.
- **Hueco:** hoy va de Z 62,9 a 66,1 (3,2 m). En el Bloque 2, Marcos lo amplía a **5 m, de Z 62,0 a 67,0**, centrado en la vía (64,5). Las jambas de Teo quedan en Z 61,1-62,0 y Z 67,0-67,9, y el HESCO del tutorial a tope desde 67,9.
- Las hojas de 2,1 m quedan 0,4 m por debajo del sólido de 2,5 m. Visualmente enrasan con el HESCO, que es lo que se ve; la colisión la pone el sólido. No hay nada que cambiar.

### 10.10 El tren de refuerzo de Nules en plena noche (Álvaro (3), 8-nov, ~13:05; retoque de la D-N172 y D-N166)
**Conclusión: el tren para fuera de la puerta este y la tropa baja por el lado sur.** Lo he comprobado en el código de marcos/noche-prototipo (8181db0):
- **El tren viene del este.** Nules está en la línea hacia Castellón, que en esta zona sale por el este, cruzando el Palancia (§1). Pararlo junto a la puerta oeste lo obligaría a atravesar O1, por donde entra la mitad de la horda, y allí quedaría tapado del todo.
- **Parada**: la cabeza de la locomotora en **X 162** (6 m fuera de la cara del muro este, en X 156, para que no pise las hojas de la puerta este) y la cola en **X 226**, sobre la vía 1 (Z 64,5). Son 64 m: R1 (24 m) y dos R2 (19,9 m cada uno), en el sentido de la marcha hacia el oeste. Queda a 33 m del estribo del viaducto del Palancia (X 259,5). **En mm: cabeza en (162000; 64500), cola en (226000; 64500).**
- **TrenAnden.PuntoBajada = (192000; 60000) mm**: el costado sur del primer R2, a 4,5 m del eje de la vía.
- **Hay sitio.** Al sur de la vía, entre X 162 y 226 y Z 47 y 61, solo hay postes de catenaria en X 160 y 210 (Z 60,9, sin colisión). El helipuerto y el rearme ya no van (D-N173). El puesto F3 (cuando entre, en (207; 51)) queda a 15 m del punto de bajada. Al norte de la vía, el bloque de pisos ocupa X 170–178 y Z 76–88: por eso bajan por el sur.
- **La horda no lo tapa.** En las tres dificultades de `noche_sagunto.json`, O4 (el puente, el este) trae **0 zombis**, y el asedio se coloca contra el muro oeste (X 54–67,5, Z 40–89, `SimWorldSetup.cs:117`). El punto de bajada queda a **unos 125 m** de la horda. Solo cambiaría cuando la Colmena abra O4, que es después del MVP; entonces hay que moverlo.
- **«Por la espalda» es, en Sagunto, un flanco por el sur.** Desde la puerta este, la tropa no ve a la horda: el muro tapa (D-N174) y el oeste queda a 86 m o más, fuera de los 60 m del fusil. **Posición de ataque recomendada: (100; 34)**, al sur del recinto, a unos 100 m de andar desde el punto de bajada. Desde ahí, la esquina suroeste de la horda (X 60–68, Z 40–48) queda a 35–45 m, y la línea de tiro pasa por fuera del muro (en X 70 va por Z 42,9, por debajo del muro sur en Z 44). El norte no sirve: entre el muro (Z 85) y las casas (Z 98) solo hay un pasillo de 13 m, y las casas tapan.
- **Riesgo, como pide la D-N166**: cuando la tropa empieza a disparar desde (100; 34), queda en campo abierto, al alcance de la parte de O2 que llega por la carretera (Z 14–31). Que la horda se dé la vuelta hacia ella lo tiene que medir Nacho en la versión del rescate.
- Para el tutorial (capítulo 3): la flecha de la D-N147 entra por el borde este, sobre la vía.

### 10.11 Tiro por encima del muro oeste con la D-N174 (Álvaro (3), 8-nov, ~13:20; decide Lucía, mide Nacho)
**El problema**: el HESCO del oeste mide 2,1 m, y la boca de un fusil está a 1,6 m. Con la D-N174, solo dispara a la pila quien está a 2 m o menos de la cara interior del muro (X 70,5–72,5). Sagunto no tiene NH90 (D-N173). Inventario: `sagunto-linea-vision.md`.

**Propuesta, por orden (lo que ya ha decidido Lucía va marcado):**
1. **La banqueta: dibujar la regla que ya existe. Coste 0 u.** Es una franja de 2 m pegada a la cara interior del HESCO del oeste, en **X 70,5–72,5, de Z 44,5 a 84,5**, sin el hueco de la puerta de vía. Desde Z 62,0 a 67,0 en el Bloque 2 quedan unos **35 m útiles**, que dan para **unos 35 tiradores a 1 m** (la tropa de dentro son 28 hombres en 5 pelotones). A la vista es un escalón de 0,4 m de palés y sacos, para que se entienda por qué se puede disparar por encima. La simulación ya lo hace con la regla de los 2 m. **Decidido por Lucía:** la excepción de los 2 m es lo que sostiene la defensa.
2. **Los nidos de la puerta de vía, a 1,5 m de la cara del muro (X 72,0).** **Decidido por Lucía.** El cambio está en `NetWorld.cs:1439`: el −X + 3.500 pasa a −X + 2.000, con Z ±7.000 (Z 57,5 y 71,5). Pasan a contar dentro de la banqueta.
3. **Dos atalayas en las esquinas interiores del frente oeste (propuesta nueva).** Son plataformas de 4 m (andamio con sacos), con la boca a unos 5,6 m, en **(73,5; 0; 47,5) y (73,5; 0; 81,5)**, de 3 × 3 m. Tiran **en enfilada a lo largo del pie del muro**:
   - desde la atalaya norte hasta el pie de la puerta, (68; 64,5), el rayo cruza el muro a 3,1 m de altura, por encima de los 2,1 del HESCO, y hasta la esquina sur (68; 47) hay 35 m, dentro de los 60 del fusil;
   - la sur, igual, en el otro sentido.
   Es la solución clásica del baluarte: el flanqueo cubre el pie del muro sin asomarse.
   - **No estorban**: la sur queda al sur del hueco de la puerta oeste-sur (Z 49–57, después del P0), y la norte, a 10 m del nido norte. La cola del tren (X 81) queda libre.
   - **Coste propuesto, para Hugo**: 10 u y 8 obrero·h cada una, entre un nido (8 u, 6 h) y una puerta de vía (8 u, 6 h), porque llevan más estructura. Dos dan 20 u.
   - Caben 2 tiradores por atalaya: el pelotón de tiradores (2 hombres, con 160 m de alcance) cabe entero en una.
   - **Pieza nueva para Teo**: `atalaya`, en 5 variantes (andamio con sacos, tablones, chapa, HESCO doble y una con foco).
4. **Lo que no recomiendo:**
   - **Una pasarela elevada detrás del muro** (1,2 m de alto y 3 m de ancho): con la boca a 2,8 m, a 3 m del muro solo ve lo que está a más de 4,7 m fuera. Añade una segunda fila, pero no ve la pila, y cuesta lo mismo que una atalaya.
   - **Troneras en el HESCO**: la regla ya deja disparar por encima a 2 m o menos, así que no añaden tiro. Solo tendrían sentido como protección, y eso hoy no se modela.
   - **La azotea del edificio de viajeros** (11 m, a 26 m del muro) queda **de reserva, como decidió Lucía**, por si la banqueta y las atalayas no dan.
- **Decisión de Lucía (8-nov, 13:08)**: aprueba la banqueta (coste 0) y los nidos a 1,5 m. Las atalayas entran solo si la banqueta sola no cumple la D-N169 **sin aire**; si la cumple, quedan para después del MVP. Fuera la pasarela y las troneras; la azotea, de reserva. El lanzagranadas AG36 es tiro curvo y el C90 sigue siendo fuego directo.
5. **Para Nacho (medir), sin el NH90 en Sagunto (D-N173)**: la normal con la horda vigente en tres casos: (a) solo banqueta y nidos a 1,5 m; (b) lo mismo con las dos atalayas; (c) lo mismo, con la mitad de la tropa en la cola del tren (D-N168). Si (a) cumple la D-N169, las atalayas sobran en el MVP.

### 10.12 Coches del atasco y del paso superior con el kit de Teo (Álvaro (3), 8-nov, ~13:25)
Teo (3) tiene un kit de coches civiles: `SM_CocheCivil_<Tipo>_v0..v4`, en cinco tipos (Utilitario, Berlina, Furgoneta, Todoterreno y Camion) y cinco variantes (intacto, puerta abierta, pinchado, accidentado y quemado). El morro mira a +Z con yaw 0, el origen está en el suelo y no llevan colisión. **Lista de instancias: `sagunto_coches_v1.csv`** (30 filas: grupo, tipo, variante, x, y, z y yaw), hecha con semilla fija y siguiendo §10.4. Sustituye al atasco de `AddCar` (`PrototypeBootstrap.cs:1455-1466`).
- **Tramo abierto, X 64–200** (11 coches): el carril norte (Z 23–28) queda libre. Los coches van en el carril sur (Z 19,5–21,5) o en la cuneta sur (Z 15–17). Uno de cada tres está girado unos 60°, como empujado de lado, y alguno está al revés. Ninguno pisa el carril norte, ya contando su largo girado. **X 93–106 queda libre**, para el acceso a la puerta sur.
- **Tramo cerrado, X 206–250** (15 coches): los dos carriles, a 0,8–2,2 m de parachoques a parachoques, mirando al este, con K1 delante, en (201,5; 23).
- **Cabeza**: un camión cruzado en (258; 0; 23), yaw 78, variante v3 (accidentado), en la entrada del tablero del Palancia. Ocupa el sitio del `AddTruck` actual.
- **Paso superior**: tres coches sobre el tablero, a **y = 8,3 m**, en Z 56, 66 y 74, con X y giro distintos: una berlina con la puerta abierta, una furgoneta al revés y un utilitario quemado.
- Más tarde, la ambulancia de Teo se puede poner en el lugar de una berlina del tramo cerrado. Kit aprobado por Lucía y entregado (mr-mak 5d04a19); Teo enlazó este CSV en su LEEME (mr-mak 185be31) y confirmó que existen todos los tipos y variantes, con el orden 0 intacto, 1 puerta abierta, 2 pinchado, 3 accidentado y 4 quemado.


### 10.13 Claros para el NH90 de Bétera, de 25 × 25 m (Álvaro (3), 8-nov, ~13:35)
Sagunto no tiene NH90 propio (D-N173). El de Bétera llega volando y se posa en un claro de **25 × 25 m** (Lucía, 8-nov; antes eran 20 × 20). Lo he comprobado contra `sagunto_obstaculos_v1.csv`, `sagunto_coches_v1.csv`, la vía, la zona de spawn del asedio y el mapa de zonas.
- **S1, la antigua explanada del helipuerto, en (180; 44)**: X 167,5–192,5 y Z 31,5–56,5. En el mapa de zonas es calle y está entera sin vegetación. Quedan 2,7 m hasta el borde norte de la carretera (Z 28,8), 5,3 m hasta el puesto F3 (X 197,8), 6,5 m hasta un tren parado en la vía (Z 63) y la catenaria queda fuera (postes en X 160 y 210). La punta del rotor (16,3 m de diámetro) llega a Z 52,2. El punto de bajada del tren de Nules (192; 60) queda fuera del claro, a 3,5 m de su borde norte. **Es el claro principal.** Se aproxima por el sureste, sobre la huerta.
- **S2, en la huerta al noreste, en (215; 97)**: X 202,5–227,5 y Z 84,5–109,5. Hoy es huerta, así que hay que **marcar ese cuadrado como sin vegetación** (255) en `sagunto_sin_vegetacion_1m.png`, como una parcela arrasada. No choca con ningún sólido ni coche. Sirve de alternativa cuando S1 está bajo fuego (O4 entra por el puente).
- **Dentro del fuerte no cabe ninguno**: el parque solo tiene 14 m de fondo. Los claros del oeste quedan en la llegada de O1, así que los descarto.
- Dato para Marcos e Iker: `claros: {"S1": [180, 44], "S2": [215, 97]}`, con lado de 25 m.
- **Revisado con la azotea y la banqueta nuevas (8-nov, ~18:00; plano [`sagunto_claros_nh90.png`](sagunto_claros_nh90.png))**:
  - **Dentro del muro sigue sin caber ninguno.** El tren de noche (X 81–145) parte el recinto en dos franjas de unos 19 m de fondo (Z 44–63 y Z 66–85). Ninguna llega a 25 m, y la azotea, la escalera y la banqueta ocupan todavía más.
  - **Fuera del muro: S1 y S2**, sin cambios. Ninguno choca con la azotea, la escalera, la banqueta, los coches ni el spawn del asedio (X 54–67,5).
  - **Para el capítulo 4 recomiendo S1 (180; 44)**:
    - Es el que queda más cerca del fuerte: a unos 75 m de la puerta sur (X 95–103), por la carretera vieja.
    - Ya está sin vegetación.
    - La aproximación entra por el sureste, sobre la huerta, sin cruzar la catenaria ni la horda, que llega por el oeste.
    - **Con la estación sitiada, las puertas siguen cerradas (D-N151; Lucía):** la tropa que baja en S1 combate desde fuera, como la del tren, y no entra por la puerta sur. Aprobado por Lucía (mr-mak 9163dcc).
  - Si el tren de Nules está parado al mismo tiempo, su punto de bajada (192; 60) queda fuera del claro y el rotor no llega a la vía (Z 52,2).
  - S2 es la alternativa cuando S1 está bajo fuego.


### 10.14 Banqueta del muro oeste por módulos (kit de defensas de Teo, 8-nov, ~13:55)
- La franja va de X 70,5 a 72,5 y de Z 44,5 a 84,5. Se corta en el hueco de la puerta de vía (Z 62–67) y en los dos **nidos movidos a X 72,0**. Los nidos son plataformas de 3 × 2,4 m con el lado largo a lo largo de Z, y ocupan X 70,8–73,2 y Z 56–59 y Z 70–73.
- Quedan cuatro tramos: Z 44,5–56 (11,5 m), Z 59–62 (3 m), Z 67–70 (3 m) y Z 73–84,5 (11,5 m).
- **Módulos de 5 m y de 2,5 m**:
  - En Z 45–55 y Z 74–84 van dos módulos de 5 m cada uno, con un hueco de 0,5–1 m en los extremos.
  - En Z 59,25–61,75 y Z 67,25–69,75 va un módulo de 2,5 m.
  - En total, **4 módulos de 5 m y 2 de 2,5 m**: 25 m de banqueta. Caben unos 25 tiradores, menos que los ~35 de la §10.11, porque los nidos ocupan su sitio (y ellos también disparan).
- Si entran las atalayas (§10.11), se quita el módulo de 5 m del extremo correspondiente (Z 45–50 o Z 79–84).


### 10.15 Medida de Nacho (D-N174) y azotea del edificio de viajeros (Álvaro (3), 8-nov, ~14:20; rehecha con las alas reales a las ~18:20)
**Medida de Nacho**: noche normal de 5520, sin NH90, con `sagunto_obstaculos_v1.csv` y 500 semillas por caso. Los CSV están en `docs/economia/entregas/linea-vision/`.

| Caso | Victorias |
|---|---|
| Sin línea de visión | 67,5 % |
| (a) Banqueta y nidos a X 72 | **23,6 %**: no cumple la D-N169 |
| (b) Con atalayas | 89,2 % |
| (c) Media tropa en la cola del tren | 9,6 % |
| **Azotea del edificio de viajeros** (2 pelotones de tiradores a 11 m) | **95,8 %**: cumple la D-N169 (≥95 %) |

Nacho propone la azotea en lugar de las atalayas, y estoy de acuerdo: da más, no hay que construir nada nuevo en el patio y no quita banqueta. **Lucía, 8-nov ~14:18: la azotea entra en el MVP y las atalayas se quedan fuera** (apuntado bajo la D-N174).

**Azotea reabierta (Lucía, 8-nov 18:03).** Paula (`sagunto_azotea.md`) muestra que la estación real (OSM 419847974, unos 32 × 11 m) tiene **dos alas de 1 planta con azotea a ~4,5–5 m** y balaustrada de ~1 m, y un **cuerpo central de 2 plantas con teja** (~9–10 m al alero). La azotea de 11 m sobre el sólido actual no existe: **queda anulada**, y con ella el pretil de sacos, la escalera exterior y las posiciones a 11 m de la versión de las 14:20. Los 95,8 % de Nacho eran con 11 m: **hay que volver a medir**.

**El edificio, como el real y movido al oeste** (la planta del recinto es nuestra). Sustituye al sólido `edificio_viajeros` (X 96,5–115,5, Z 75–83,8, 11 m). **Ajuste de las 18:12 (Paula, `almenara_y_sagunt_acceso.md`; Lucía)**: las terrazas miden ~9 × 9 m y el andén 1 va adosado a la fachada. Así que el edificio tiene **9 m de fondo, Z 71,8–80,8**, con la fachada sur pegada al andén, y el andén se ensancha hasta la fachada: hoy acaba en Z 70,7 y pasa a acabar en **Z 71,8** (pz1 = TrackY + 7,3), que es justo el borde de atrás de la marquesina. Del eje de la vía 1 (Z 64,5) a la fachada hay 7,3 m: 2,2 hasta el borde del andén y 5,1 de andén. En la real son ~4,2 m a la vía de estación y ~8,6 m a la primera general, con un andén de ~5–6 m, así que encaja con una vía general junto al andén. Detrás quedan 3,7 m libres hasta el muro norte (cara interior Z 84,5). Para la caja X 82,5–115,5, Z 71,3–81,3 he comprobado el solape con `sagunto_obstaculos_v1.csv` y con el código, y solo sale el propio edificio de viajeros. 

| Cuerpo | X | Z | Alto | Del muro oeste (cara interior X 70,5) |
|---|---|---|---|---|
| **Ala oeste**, azotea | 83–92 (9 m) | 71,8–80,8 (9 m) | **4,75 m** de suelo de azotea, balaustrada de 1 m | **12,5 m** (13,5 m a la cara exterior) |
| Cuerpo central, 2 plantas y teja | 92–106 (14 m) | 71,8–80,8 | 10 m (alero ~9,5) | 21,5 m |
| **Ala este**, azotea | 106–115 (9 m) | 71,8–80,8 | 4,75 m, balaustrada de 1 m | **35,5 m** |

**Zona ciega** (D-N174: muro de 2,1 m, blanco a 1 m, boca a 4,75 + 1,6 = 6,35 m; no se ve si d < 1,1 · D / 4,25):

| Borde del ala oeste a… | Zona ciega fuera del muro |
|---|---|
| 10 m del muro (X 80,5) | 2,6 m |
| **12,5 m (X 83, la propuesta)** | **3,2 m** (3,5 m contando a la cara exterior) |
| 15 m (X 85,5) | 3,9 m |
| Sin mover, borde en X 96,5 (26 m) | 6,7 m |

*Nota (aclarado con Lucía, 18:10)*: estas cifras siguen la regla de la D-N174, que apunta al blanco a 1 m. Si se apunta a los pies (blanco a 0 m, la sombra del muro en el suelo), la zona ciega sale de 2,1 · D / 4,25: **6,2 m para el ala a 12,5 m**. Entre 3,2 y 6,2 m se ve al zombi de cintura para arriba, pero no los pies. La simulación usa la regla de la D-N174.

La pila (X 54–68) queda a entre 15 y 29 m del borde del ala, dentro del alcance del fusil. Con un ala más baja la zona ciega sale **más corta** que la de 11 m a 26 m (2,7 m), porque el ala está mucho más cerca del muro. Elijo X 83: deja 12,5 m de patio para la banqueta (X 70,5–72 con los nidos en X 72) y para moverse por detrás.

**El ala este no sirve hacia el oeste**: el cuerpo central de 10 m le tapa todo lo que hay al oeste. Solo ve el norte y el este (el muro norte está 3,7 m por detrás). La dejo como posición de reserva y para cubrir la puerta este, no como frente oeste.

**Pelotones**: los 2 pelotones de tiradores empiezan en el **ala oeste**, en el borde oeste y con yaw 270: **(84,5; 4,75; 74,3)** y **(84,5; 4,75; 78,3)**, es decir, (84500; 74300) y (84500; 78300) mm sobre la cota 4750. El ala tiene 9 × 9 m (81 m²) y 9 m de borde oeste: caben los 2, pero apretados. **Nacho, que mida dos casos**: los 2 pelotones en el ala oeste, y 1 en el ala oeste más 1 en el ala este.

**Acceso**: por dentro, desde la primera planta del cuerpo central, con una puerta o ventanal a cada ala (Paula: ESTIMACIÓN, no hay foto; en la ortofoto no se ve escalera exterior). **Sin pieza nueva** (Lucía) y sin escalera exterior; en la simulación solo cuenta el tiempo de subida. **Nacho (18:31), SUPUESTO: 25 s por pelotón para subir, y otros 25 para bajar; mientras sube no dispara.**

**Lo que cambia para cada uno**:
- **Marcos (vía Mak)**: quitar el sólido `edificio_viajeros` y poner tres cajas: ala oeste X 83–92, Z 71,8–80,8, 4750 mm; cuerpo central X 92–106, Z 71,8–80,8, 10 000 mm; ala este X 106–115, Z 71,8–80,8, 4750 mm. Andén: pz1 de TrackY + 6,2 a TrackY + 7,3 (Z 71,8). La placa y el reloj de la fachada pasan del centro X 106 al del cuerpo central, X 99, sobre la fachada sur (Z 71,8). Mientras no haya modelo, primitivas con estas medidas.
- **Teo**: un edificio de viajeros nuevo como el real (32 × 9 m, alas de 9 × 9 m con azotea y balaustrada, cuerpo central con teja en el color a86c50), con 5 variantes. Origen en el centro de la planta (99; 0; 76,3) y la fachada del andén al sur, pegada al andén. La subida es por dentro: no hay pieza nueva de escalera. **El pretil de sacos y la escalera exterior quedan anulados**, así que la balaustrada va en el propio modelo.
- **Hugo**: el pretil de 11,2 u ya no existe. Si la balaustrada viene con el edificio, el muro de partida vuelve a 120 u; él dice si la balaustrada cuenta como muro y lo que cuesta. **Hugo (18:08): confirmado, el muro de partida vuelve a 120 u.** La balaustrada viene con el modelo y no es muro: no tiene vida, coste ni mantenimiento. Medido con sim_economia.py en 1000 partidas: equilibrado 13,9 %, prisa 44,8 %. Si Nacho pide sacos en las alas, se costean a 1,6 u por cada 8 m.
- **§10.13 (claros)**: S1 (180; 44) y S2 (215; 97) no se tocan; el edificio no se acerca a ninguno de los dos.
- **Atalayas**: siguen fuera del MVP.

<details><summary>Versión anterior (8-nov, ~14:20–14:25), anulada: azotea a 11 m sobre el sólido actual</summary>

Superficie de 19 × 8,8 m con pretil de sacos de 1,2 m (11,2 u, muro de partida a 131,2 u). Zona ciega de 2,7 m con la boca a 12,6 m y el muro a 26 m. Escalera exterior en el testero este (X 115,5–117,5, Z 76–82, centro (116,5; 0; 79), yaw 180). Esquinas del pretil: NE (115; 83,3) yaw 0, SE (115; 75,5) yaw 90, SO (97; 75,5) yaw 180, NO (97; 83,3) yaw 270. Tramos de 5,1 m en X 103,45 y 108,55 sobre Z 83,8 (yaw 0) y Z 75 (yaw 180). Hueco en Z 78,2–79,4. Pelotones en (98500; 77400) y (98500; 81400) mm a la cota 11 000, yaw 270.
</details>

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
