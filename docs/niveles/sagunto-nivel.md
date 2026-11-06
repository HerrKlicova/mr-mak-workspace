# Sagunto · diseño del nivel (v1.1, aprobado por Lucía)

Autor: Álvaro (Niveles) · 6-nov-2026 · Origen: Eugenio, 17:20: «¿es normal que la vía esté cortada? […] que tenga sentido, que sea realista, que se sienta vivo».
Revisión de cohesión: **Lucía** (última palabra). **Aprobado el 6-nov a las 18:27** con las correcciones de color y contenido de la v1.1 (abajo). Modelos: **Teo**. Integración: **Marcos** (vía Mak).
Plano: `docs/niveles/sagunto_plano_v1.png` (vista cenital de la zona de 256 × 128 m con lo que hay hoy y lo que propongo).

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
| E1 | Carretera vieja | 6 m (Z 20-26) | **10 m (Z 18-28)**: 7 m de calzada con línea central en #d4d0cc y arcenes de 1,5 m. El atasco ocupa los dos carriles |
| E2 | Calle de la Estación | 6 m (X 56-62) | **10 m (X 54-64)**: 7 m de calzada y aceras de 1,5 m. El paso a nivel se ensancha igual |
| E3 | Calle del pueblo | 7 m | **9 m**: la hilera de delante se queda en Z 103 (12 m de campo de tiro), la calle pasa a Z 108-117 y la de atrás a Z 122 |
| E4 | **Puerta de vehículos** en el muro sur | No hay | **8 m de hueco en X 95-103**, con un camino de 8 m hasta la carretera vieja. Hoy los vehículos no pueden salir del fuerte, salvo por la vía. **Toca la simulación** (sólidos del muro y `Works`): Nacho/Marcos, y el coste, Hugo (como la puerta de vía, 8 u) |
| E5 | **Parque de vehículos** dentro del fuerte | No hay | **X 72-124, Z 46-60** (52 × 14 m), al sur de la vía, frente a la puerta nueva: 3 Dragón y 4 VAMTAC en batería, que salen de frente por E4. Nada de decorado en esa franja |
| E6 | **Helipuerto anexo** | No hay | **30 × 30 m despejados en X 165-195, Z 29-59** (centro en (180; 44)), con un anillo de HESCO bajo (1,2 m) y una H en #d4d0cc. Está fuera del muro, al sureste, como la zona de toma anexa de una base avanzada. Queda a 5 m del poste de catenaria de X = 160 y la aproximación entra por el sureste, sobre la huerta. **Cabe un helicóptero medio** |

**Nivel 2: agrandar la zona de Sagunto (es lo que de verdad lo arregla).** Recomiendo **512 × 256 m**: el doble por lado, cuatro veces la superficie. Así la cámara al máximo deja de ver el nivel entero, hay sitio para un fuerte de ~120 × 70 m con patio de armas y helipuerto dentro, un pueblo con plaza, una huerta en la que se pueda luchar y unos 200 m de carrera de la horda hasta el muro (más tiempo para disparar). Con celdas de 0,5 m son 1024 × 512 celdas (×4); si el FPS no lo aguanta, con celdas de 0,75 m la zona sería de 384 × 192 m. **Lo deciden Marcos y Nacho midiendo el FPS** (ZombieGrid: 361 FPS con 10.000 zombis en la zona actual), y obliga a regenerar los goldens de zona. Si sale adelante, rehago la distribución completa (v2) sobre la zona nueva.

### 9.4 Boceto del nivel 2 sobre 512 × 256 m (7-nov; no entra esta noche, se decide con las medidas)
Plano: `sagunto_plano_v2_boceto.png` (script en `herramientas/plano_v2.py`). Misma lógica que la v1, con sitio de verdad:
- **Vía en Z = 128**, en el centro. Los remates (paso superior y puente) siguen fuera de la zona. La horda tiene **176 m de carrera** desde el borde oeste hasta la puerta oeste (hoy, 70).
- **Fuerte de 140 × 80 m** (X 176-316, Z 96-176), que sigue cabiendo con el tren de 64 m y sus 70 m de andén. Al sur de la vía: **parque de vehículos de 80 × 20 m** con la **puerta de vehículos** de 8 m en el muro sur y el almacén. Al norte: andén, edificio de viajeros pegado al muro y **patio de armas con helipuerto de 44 × 38 m dentro del recinto**.
- **Glacis** de 30 m al oeste y de 12 m en el resto.
- **Pueblo** al norte (Z 188-236): tres hileras de casas de 6 m con dos calles de 9 m y una **plaza mayor de 36 × 48 m con su iglesia**. La plaza es la zona de toma alternativa y el sitio para que maniobren los pelotones. Las calles llegan hasta la calle de la Estación.
- **Calle de la Estación** de 10 m (X 130-140) y **carretera vieja** de 10 m (Z 50-60) con el atasco.
- **Huerta** al sur con su acequia madre, ramales y 3 alquerías sueltas, y **huerta este** detrás del bloque de pisos.
- Para el tamaño del perímetro (440 m frente a los 254 de hoy) habría que recalcular el muro de partida de D-N63 con Hugo.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

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
