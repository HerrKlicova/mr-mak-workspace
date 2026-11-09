# Bétera · aeródromo «Base Jaime I» v0.2 (Álvaro (3), 8-nov, D-N173; solo en papel)

- **v0.1** (8-nov, ~13:00): Lucía (3) la aprobó como base, con tres decisiones que siguen vigentes. La pista mide 275 m. El plantel es de 2 NH90, 2 pelotones de embarque y 1 de guarnición. En el MVP la base no recibe asedios.
- **v0.2** (8-nov, ~13:15): ajustada a la **planta real** que ha conseguido Paula (`/mnt/project-files/betera_planta.md`, `betera_planta_osm.jpg` y `betera_planta_pnoa_osm.jpg`; OSM con licencia ODbL y PNOA del IGN con CC BY 4.0). La v0 estaba hecha a ciegas. Ahora la zona aérea, la pista, las rodaduras y la torre van a escala 1:1 y en su sitio.

- **Encuadre oficial (Iker, 8-nov 13:03): el de reserva, 256 × 128 m** (X 0–256, Z −4 a 124), con la plataforma y la torre dentro y la pista en el faldón, porque la zona y el ECS de Marcos están hechos para ese tamaño. La zona de 324 × 224 m queda para después del MVP.

Plano: `betera_plano_v0.png` (script `herramientas/plano_betera_v0.py`, que ya dibuja la v0.2). Dato: `estaciones/betera.json`.

## 0. Conclusión
- **La zona de juego es la zona aérea**, que está en el extremo norte de la base real. Tiene la pista de 275 m, la plataforma de 277 × 99 m unida a la pista por 3 rodaduras, y la torre en la esquina sureste de la plataforma. La zona de vida (17 edificios, deportes, antenas y depósito de agua) queda al sur, fuera de la zona: es de donde sale la guarnición.
- **La zona aérea real no cabe en 256 × 128 m.** De la torre a la pista hay unos 175 m de fondo, y la plataforma ya mide 277 m de ancho. **Recomiendo, para el aeródromo, una zona de 324 × 224 m** (X −40 a 284, Z −44 a 180), que lo enseña todo a escala real. En el MVP no hay horda aquí (Lucía), así que el coste es solo de suelo y piezas, y hay que medirlo (D-N70).
  - **Si la zona tiene que seguir siendo de 256 × 128 m** (lo decide Iker según el código), el encuadre es la plataforma con la torre (X 0–256, Z −4 a 124). La pista y las rodaduras quedan en el faldón del norte, a la vista al alejar la cámara pero fuera de la zona, como el castillo en Sagunto. Así se pierde el frente B4, que en el MVP no se usa.
- **El reducto de HESCO se mantiene**, porque es ficción nuestra: lo levantó el ejército alrededor de la plataforma después del colapso. La pista se queda fuera, al norte, igual que en la v0.1, y el frente B4 conserva su sentido.

## 1. Lo que dice la planta real (Paula) y cómo la paso a la zona
- **Medidas** sobre `betera_planta_osm.jpg`: 200 m = 240 px, es decir, 0,833 m por píxel, con el norte arriba.
  - Pista de **275 m** (dos fuentes ya: OSM y GlobalMilitary).
  - Plataforma de **277 × 99 m**.
  - **3 rodaduras** de unos 35 m, en px x 882, 998 y 1.116.
  - **Torre** a unos 20 m al sur de la esquina sureste de la plataforma.
  - Dos viales salen de la plataforma hacia el sur, en px x 888 y 1.100, hasta un vial transversal a unos 54 m.
- **Conversión a coordenadas locales** (X al este, Z al norte, a escala 1:1 y sin girar; la plataforma real está girada unos 2° y no lo tengo en cuenta): X = 128,5 + (px − 999) × 0,833 y Z = 24 + (372 − py) × 0,833.
- **No se puede verificar** (Paula): los hangares, porque el IGN difumina el interior de la base. Tampoco aparecen helipuertos sueltos en OSM, y los helicópteros usan la plataforma y la pista. Las posiciones del combustible y del polvorín son mías.
- **Ancho de la pista**: 18 m, SIN VERIFICAR. En la imagen se ve como una línea.

## 2. Disposición v0.2 (coordenadas locales en metros)
| Elemento | Dónde | Fuente | Pieza |
|---|---|---|---|
| **Pista** | X −37–238, Z 154–172 (275 × 18 m, 09/27) | OSM: largo y posición. El ancho es mío | Asfalto con línea central b8b8b8 |
| **Rodaduras R1–R3** | X 31, 128 y 226 (10 m de ancho), de Z 123 a 154 | OSM | Asfalto |
| **Plataforma** | X −10–267, Z 24–123 (277 × 99 m) | OSM | Asfalto 6c7874 con marcas b8b8b8 |
| **P1, helipuerto principal** | (128; 0; 104), yaw 0, losa de 30 × 30 m, en la cabeza de R2 | Mío | **Helipuerto v4 de Teo** |
| **P2 y P3** | (31; 104) y (226; 104), de **25 × 25 m** (Lucía, 8-nov; antes 20 × 20), en la cabeza de R1 y R3 | Mío | Marcas pintadas |
| **Rearme** | (172; 0; 104), yaw 90 | Mío | `rearme_set` de Teo |
| **Hangares H1 y H2** | Centrados en (90; 40) y (160; 40), de **40 × 25 m** (estimación de Paula para dos helicópteros con las palas montadas; antes 30 × 24), con el portón al norte (yaw 0), en la franja sur de la plataforma | En la ortofoto «se adivinan naves junto a la plataforma»; posición y tamaño SIN VERIFICAR | Nueva: `aerodromo/hangar` |
| **Torre de control** | (224; 0; 4), yaw 0 (mira a la plataforma) | OSM y fotos AE1 | Nueva: `aerodromo/torre_control` |
| **Viales al sur** | X 36 y X 213, de Z 24 hacia el sur, hasta el vial transversal en Z −30 | OSM | Asfalto |
| **Depósito de combustible** | X 236–262, Z −28 a −8: 3 tanques (**yaw 0**, con el eje a lo largo de X; con yaw 90 se pisaban) en cubeto con talud | Mío: junto al vial este y a la torre, lejos del polvorín | Nueva: `aerodromo/tanque_combustible`; talud de Castellón |
| **Polvorín** | 2 iglús en (−18; −26) y (−18; −8), yaw 90, con talud. Huella de Teo: 14,4 m en Z × 25 m en X (bóveda 11 × 22 + talud trasero hacia −X). Caben: quedan 3,6 m entre ellos; con el origen de Teo en el centro de la bóveda (frente 11,3 m a +X y talud 13,5 m a −X), la huella va de X −31,5 a −6,7 y quedan 4,5 m hasta el HESCO oeste. Hangar y torretas: mr-mak 3b9ea17 y LEEME de Teo. En el MVP es faldón | Mío: en el lado contrario al combustible, a más de 240 m de él | Nueva: `aerodromo/polvorin` |
| **Reducto de HESCO** | X −36–276, Z −36 a 124 (unos 940 m de muro) | Ficción nuestra | HESCO del kit |
| **Puertas del reducto** | Norte: 3 de vehículos donde lo cruzan las rodaduras, en (31; 124), (128; 124) y (226; 124), yaw 0. Sur: 2 donde lo cruzan los viales, en (36; −36) y (213; −36), yaw 180 | Siguen los viales y las rodaduras reales | `puerta_vehiculos` (D-N111) |
| **Torretas de vigía** | `SM_TorretaVigia` de Teo (4 × 4 m, 6,7 m), dentro del HESCO norte en (4; 121) y (252; 121), yaw 0, en el MVP. En las esquinas sur (−33; −33) y (273; −33), yaw 180, después del MVP (faldón) | Mío | `SM_TorretaVigia` |
| **Valla de la base** | Norte: Z 176, al norte de la pista (en OSM va en diagonal entre Z 138 y 173; la enderezo). Este: X ≈ 305, junto a la carretera, fuera de la zona | OSM | Nueva: `aerodromo/valla` |
| **Zona de vida** | Al sur de Z −44, fuera de la zona | OSM | — |
| **Pinar** | Fuera del reducto y lejos de la pista | Ortofoto | Nueva: `aerodromo/pino` |

## 3. Frentes, entradas de la horda y claros para posarse
- **En el MVP, Bétera no recibe asedios de la gran horda** (Lucía, 8-nov). Los frentes y las entradas quedan en el dato para cuando la Colmena aprenda a atacar lo que más usa el jugador.
- **Frentes**: **B1 Plataforma** en (128; 74). **B2 Polvorín** en (−18; −17). **B3 Puerta sureste** en (213; −36). **B4 Pista** en (100; 163), fuera del reducto.
- **Entradas**:
  - **Ba** por el sur, desde Valencia (rumbo 154°), a través de la zona de vida.
  - **Bb** por el oeste, desde el campo de maniobras.
  - **Bc** por el este, por la carretera desde Bétera.
- **Claros de 25 × 25 m para el NH90** (D-N173; Lucía subió el tamaño de 20 a 25 m el 8-nov): P1 (losa de 30 m) y P2–P3 en la plataforma. **C1** en la pista, centrado en (100; 160): como la pista mide 18 m, el claro incluye la franja de tierra lisa al sur, y quedan 3,5 m hasta la valla (Z 176) y 10 m hasta R2. Después, **C2** en (−20; 140), al noroeste, entre la plataforma y la valla (3,5 m al HESCO norte y 1,5 m a la pista), y **C3** en (128; −14), al sur de los hangares.
- Paleta: nada rojo ni ámbar. La H, las marcas y la línea central van en b8b8b8, y las luces en crema f0dc9c.

## 4. Para Iker: el nodo
- **Dato**: `estaciones/betera.json`, con el formato de `castellon.json` más estos campos: `tipo: "aerodromo"`, `zona` (el rectángulo propuesto de 324 × 224 m), `nodo`, `valla`, `pista`, `rodaduras`, `plataforma`, `claros`, `entradas_horda` y `asedios_mvp: false`. El lector actual (`Net/EstacionDato.cs`) ignora las claves que no conoce. **`tamano` va como `"estacion"`** hasta que añadas Aerodromo al enum. `vias` y `andenes` van vacíos.
- **Hay coordenadas negativas y mayores de 256**, porque la zona propuesta va de X −40 a 284 y de Z −44 a 180. Si la zona tiene que ser de 256 × 128, se usa el encuadre de reserva (§0) y lo que cae fuera se dibuja como faldón.
- **Posición en el mapa de operaciones: (48; 75)** (corregida el 8-nov: con la fórmula de `RailNet.cs` y la latitud y longitud de la base sale (47,8; 75,1); antes era (49; 75), ajustada a nodos aproximados). Las coordenadas reales de Paula confirman que los nodos de la costa del código están a 0,5 o menos de su sitio.
- **Distancias reales** (para la ETA de Nacho, D-N120): a **Sagunto, 18,1 km con rumbo 72°** (por carretera 29,7 km, ~28 min, OSRM; `linea_valencia_castellon.md` §3); el NH90 entra en la zona de Sagunto por el borde oeste, algo al sur, con la flecha de la D-N147. A **Nules, 37,4 km con rumbo 47°**.
- **Plantel** (Lucía): 2 NH90, 2 pelotones de embarque y 1 de guarnición fijo. Lo revisa Hugo, que también pone las existencias propias.
- **Estado inicial: propia.** El capítulo 4 del tutorial empieza la primera vez que se abre el aeródromo.

## 5. Para Teo: piezas nuevas (cada una con 5 variantes, D-N70 y FPS medidos)
1. `aerodromo/torre_control`, a partir de las fotos AE1: fuste con escalera exterior, fanal acristalado y antenas.
2. `aerodromo/hangar` de 30 × 24 m, con portón corredero a +Z.
3. `aerodromo/tanque_combustible`, tanque horizontal de unos 12 × 3 m sobre cunas.
4. `aerodromo/polvorin`, iglú semienterrado con puerta blindada.
5. `aerodromo/valla`, malla de 2,5 m con concertina, en tramos de 10 m.
6. `aerodromo/garita` y la puerta de la valla, que en la v0.2 quedan fuera de la zona y se usan después del MVP.
7. `aerodromo/pino`, pino carrasco, sin colisión.

## 6. Pendiente
- ~~**Iker**: tamaño de la zona~~ Resuelto: 256 × 128 (reserva) en el MVP. Lo que cae fuera (pista, rodaduras, polvorín, combustible y parte del reducto) se dibuja como faldón; B2 y B4 quedan fuera hasta que la zona crezca.
- **Hugo**: revisar el plantel y las existencias propias.
- **Paula**: si aparece una foto de los hangares, ajusto su número y su sitio.


## 7. Lista de instancias con las piezas de Teo (v1, 8-nov, ~17:55)
- **Dato: [`betera_instancias_v1.csv`](betera_instancias_v1.csv)**, 219 filas, con el mismo formato que Nules y la columna en_zona_mvp (zona X 0–256, Z −4 a 124; lo demás es faldón). Plano de comprobación: [`betera_instancias_v1.png`](betera_instancias_v1.png). Generador: `herramientas/instancias_v1.py`.
- **Piezas** (LEEME de `entregas/teo-modelado/betera`):
  - `SM_Hangar` ×2, de 40 × 25 m, con el portón a +Z.
  - `SM_TorreControl`.
  - `SM_TorretaVigia` ×4: 2 en el MVP y 2 en el faldón.
  - `SM_TanqueCombustible` ×3, con yaw 0.
  - `SM_Polvorin` ×2, con yaw 90.
  - `SM_VallaBase` ×33, en la valla norte de Z 176 (faldón).
  - `SM_Pino` ×60, en el faldón sur y norte, sin colisión.
  - El helipuerto v4 en P1 y el `rearme_set`.
  - El reducto entero de HESCO, con 81 tramos de 10 m, 12 cortos, 4 esquinas y 10 remates, y 5 `SM_PuertaVehiculos`.
  - `SM_Garita` y `SM_PuertaValla` quedan fuera: después del MVP.
- **Claros de 25 × 25 m, marcados en `betera_plano_v0.png` y en el plano de instancias**:
  - **P1–P3, en la zona del MVP**: P1 en la losa de 30 m, P2 en (31; 104) y P3 en (226; 104).
  - **C1, C2 y C3, en el faldón**: C1 en (100; 160), en la pista; C2 en (−20; 140); C3 en (128; −14), con un trozo dentro de la zona.
  - **En el MVP se posa en P1–P3.**
- La garita y la puerta de la valla van después del MVP, en la entrada real de la base (al sur, fuera de la zona).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 8. Ambiente del aeródromo (Álvaro (3), 8-nov, ~18:50; piezas de Teo en mr-mak 7b4478f, aprobadas por Lucía)
Hay 51 filas nuevas en `betera_instancias_v1.csv`, con el grupo `ambiente`; el CSV pasa a 270 filas. Están en azul en el plano de comprobación `betera_instancias_v1.png`.

- **Balizas**: 40 tramos de 12 m (`SM_Balizas`). Van en los cuatro lados de P1, P2, P3 y C1, con 2 tramos por lado, centrados en ±6 m del eje y a **1 m por fuera del claro**. Ninguna pisa un claro: lo he comprobado. Lados norte y sur con yaw 0, este y oeste con yaw 90. P1 cuenta con la losa de 30 m. Variante v0 (blancas) en los P y v1 (verdes, de umbral) en C1, que está sobre la pista.
- **Manga de viento**: (106; 0; 120), junto a P1 y fuera de la losa.
- **Casetas**: la Oficina (v0) en (116; 0; 30), junto al hangar H1, y el Almacén (v1) en (186; 0; 30), junto al H2. Van con yaw 0, con la puerta al norte, hacia la plataforma.
- **Torres de luz**: en las cuatro esquinas de la plataforma, a 3 m por dentro: (−7; 27) con yaw 71, (264; 27) con yaw 289, (−7; 120) con yaw 109 y (264; 120) con yaw 251. Los focos apuntan al centro (128,5; 73,5). Con la convención de Teo (focos a −Y de Blender, que es +Z con yaw 0) el yaw sale así; lo confirma Marcos con la primera.
- **Vallas**: conos con cinta (v3) a 10 m a cada lado de las tres salidas a la pista (X 31, 128 y 226), en Z 121, por dentro del HESCO. En las dos puertas sur (X 36 y 213), barreras jersey (v2) a ±11 m por fuera, en Z −40, y vallas de obra (v0) en chicane en Z −48. Las de las puertas sur quedan fuera de la zona del MVP (`en_zona_mvp` = no).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 9. Revisión del rearme que propone Iker (Álvaro (3), 8-nov, ~19:20)
Los largos de las piezas están SIN VERIFICAR; he supuesto unos 8 m.
- **Medidas reales** (Iker, 19:27): el camión mide 8,0 × 2,45 m y el remolque 3,6 × 2,3 m. **El remolque va en (152; 106,5)** para que se vea enganchado detrás del camión, que ocupa Z 96–104.
- **Camión y remolque**: los pasa de (135; 100) y (135; 109), que caían dentro de P1 (la losa de 30 m, X 113–143) y encima de sus balizas del este (X 144), a **(152; 100) y (152; 109), con yaw 180**.
- **Aparcado**: en **(31; 84), con yaw 90**, junto a P2. Con yaw 0 o 180 tocaría las balizas del lado sur, en Z 90,5.
- **Tapado**: en **(226; 84), con yaw 90**, junto a P3.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 10. FARP del NH90 junto al claro P2: propuesta (Álvaro (3), 8-nov, ~20:10; decisión de Lucía de las 21:15, RA2 de Paula)
Se compone de una cisterna flexible en el suelo, una manguera tendida, sacos y cajas, **pegado al claro y sin invadirlo**. Lo pongo en **P2** (X 18,5–43,5, Z 91,5–116,5), por el lado este. Es el claro de 25 × 25 m con más sitio libre alrededor, porque entre P2 y P1 hay 69 m de plataforma vacía.
- **Cisterna flexible**: en (53; 104), con yaw 90 (el largo a lo largo de Z). Queda a 8,5 m de las balizas del lado este (X 44,5).
- **Sacos**: una U alrededor de la cisterna, abierta hacia el claro: dos tramos en Z 98 y Z 110 (de X 49 a 57) y uno de cierre en X 58,5.
- **Manguera**: de la cisterna (X 50) al borde del claro (X 44), en Z 104, tendida en el suelo y sin colisión.
- **Cajas de munición**: en (50; 95), al sur de la U, por fuera.

Comprobado sobre el plano: no pisa P2 ni sus balizas, y no toca el «aparcado» en (31; 84), con yaw 90, ni el camino de rodadura de X 31 (Z 123–154). Las medidas son a la espera de Teo. **Aprobado por Lucía (08-11, 21:20).**

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

### 10.1 Colocación con las piezas de Teo (20:20; mr-mak 263c2b8, que todavía es local)
Son 11 filas del grupo `farp` en `betera_instancias_v1.csv` (pasa a 281). Ninguna lleva colisión.
- **Cisterna** (Llena) en (53; 104), con yaw 180, para que la manguera de salida (+X local) vaya hacia el claro. La berma ocupa X 49,4–56,6 y Z 101,3–106,7, y la manguera llega hasta X ≈ 45,3, sin pasar de las balizas (X 44,5). Si sale hacia el este, se gira a yaw 0; lo comprueba Marcos.
- **Sacos** Hilera6: en Z 108,5 y 99,5 (en X 51 y 55), y el cierre este en X 58,5 (Z 102 y 106, con yaw 90).
- **Carrete** en (46,5; 99). **Cajas**: el palé en (50; 95) y la pila de 4 en (52; 95), con una U de sacos alrededor (yaw 180), abierta hacia la cisterna.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 11. Bétera como zona en la que se entra (Álvaro (3), 9-nov ~22:40; encargo del coordinador con libre albedrío de Eugenio)
Hasta ahora Bétera se montaba solo en la escena de captura (`Editor/AerodromoCaptura.cs`) y en el juego era un panel. Para que el núcleo de la zona (el de Sagunto) la abra con tropa, NH90 y cámara, dejo tres datos:
- **[`betera_zona_v1.json`](betera_zona_v1.json)**: el encuadre de 256 × 128 m, el suelo, el recinto (en el encuadre solo entra el muro norte, en Z 124, con 3 puertas), los claros P1–P3, la cámara de inicio en (128; 70) a 60 m, las rutas entre la guarnición y los claros, y las entradas de la horda para después del MVP (todas con peso 0: sin asedios en el MVP).
- **[`betera_obstaculos_v1.csv`](betera_obstaculos_v1.csv)**: 24 sólidos con las columnas de `sagunto_obstaculos_v1.csv`. Son los hangares, la torre, las 2 torretas, las casetas, el FARP, el camión y el remolque de rearme, las vallas de obra y el muro norte con sus puertas. Las medidas salen de los FBX de Teo (LOD1). Lo genera `herramientas/betera_zona_v1.py`, que comprueba que nada se pisa ni cae en un claro.
- **Tropa y NH90**: los de `guarnicion_puestos_v1.json` (estación Bétera), que ya están aprobados.

**Dos correcciones que salen al medir los FBX:**
- **Los hangares miden 64 × 25,9 m**, no 40 × 25. H1 va de X 58 a 122 y H2 de X 128 a 192, y entre los dos quedan 6 m. No los muevo.
- **Las dos casetas caían dentro de los hangares.** La de (116; 30) pasa a (125; 30) con yaw 90, en el hueco de 6 m entre los dos, y la de (186; 30) pasa a (198; 30). Ya está corregido en `betera_instancias_v1.csv`.

SIN VERIFICAR: que el exportador de Teo no invierta la X. No cambia nada, porque todas estas cajas son simétricas.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
