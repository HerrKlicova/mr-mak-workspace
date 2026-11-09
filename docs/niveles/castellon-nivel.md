# Castellón · estación de ciudad v0 y bucle entre estaciones (Álvaro, 7-nov, solo papel)

Encargo de Eugenio (7-nov, 09:03): «manda a alguien a diseñar otra estación importante. Que todas las estaciones generales reutilicen los assets de Sagunto, pero de diferente manera. Tienes que poder entrar en cada estación que hayas reclamado. [...] No podemos estar estancados en una sola estación». Plano: `castellon_plano_v0.png`; script: `herramientas/plano_castellon_v0.py`; dato: `mapa_castellon_carreteras_v0.json`. Es papel y no toca la build de esta noche.

## 0. Conclusión
- **Elijo Castellón.** Es la otra estación que de verdad importa en la demo:
  - el jugador equilibrado la toma **el día 1** (economía §1), así que es la primera estación que se reclama después de Sagunto;
  - es la **única fuente de combustible** (60 u al día, la refinería; economía §2), y sin combustible no se mueve ningún tren;
  - es **el talón de Aquiles**: la Colmena va a por ella el día 7 (D-N, idea de Hugo, ya en el guion).
  - Valencia-Nord no sirve como segunda estación, porque es un nido y nunca es segura (D-N14). Teruel llega el día 5 y queda lejos, en el interior.
- **Castellón se monta casi entera con el kit de Sagunto, combinado de otra manera**, y solo lleva **una pieza nueva**: el vagón cisterna. Lo propio de cada estación sale de lo que produce, no de un arte distinto.
- **Toda estación reclamada se visita igual que Sagunto**: desde el mapa, se entra en su zona de 256 × 128 m. Se propone un bucle de trenes (§4) que da a cada visita algo que hacer.

## 1. Disposición (coordenadas locales de la zona, vía principal a lo largo de X)
| Elemento | Dónde | Por qué existe | Kit |
|---|---|---|---|
| **Dos vías generales** (Z 57,5 y 66,5) con andén central de 120 m y andén lateral | X 70–190 | La línea de la costa es de doble vía, y una capital tiene andenes largos | Vía, andén y catenaria de Sagunto. Marquesina ×5 (v1–v5 por semilla) |
| **Paso entre andenes** (`kit_paso` de Teo, luz 9 m) | Origen en (120; 66,5), entre los ejes de los andenes (Z 62 y 71); escaleras hacia +X hasta X ≈ 129,5 | Con dos vías generales no se cruza a nivel en una capital | Por defecto, la v0 (paso inferior), que no tapa la vista cenital del andén; las otras 4 variantes, por semilla en otras principales. Las escaleras desembocan frente a la puerta del cuerpo central (X 130) |
| **Edificio de viajeros** | X 96–164, Z 75–88 (alas de 18 m en X 96–114 y 146–164; cuerpo central de 32 m, X 114–146, de Teo: dos torretas, cuatro módulos de tres plantas y el frontón con reloj, yaw 180) | Estación de capital: más grande que la de pueblo | **Dos edificios de viajeros de Sagunto en espejo** (variantes distintas) unidos por un cuerpo central de ladrillo, que es la única extrusión nueva. SIN VERIFICAR: la estación real de Castellón es moderna y no se parece; la lectura es genérica |
| **Plaza y avenida de la Estación** con coches abandonados | Z 92–104 | La salida a la ciudad | `coche_2000` y la ambulancia del kit |
| **Manzanas de bloques de pisos** | Z 108–124, en toda la X | Es una ciudad: aquí casi no hay casas bajas | `bloque_pisos` v1–v5. En Sagunto había uno solo; aquí son la mayoría |
| **Ronda sobre las vías** | X 34–42, de Z 0 a 128 | La ciudad cruza el haz de vías por arriba | `paso_superior` de Sagunto, con dos vanos. **Es el acceso de los vehículos** desde el sur (D-N96) |
| **Haz de mercancías** de 3 vías | Z 44 / 48 / 52, X 46–230 | Donde se forman los trenes de cisternas | Vía del kit |
| **Ramal del Grau** | Sale por el este en Z 44 | Une la estación con la refinería y el puerto (SIN VERIFICAR con el trazado real) | Vía del kit. Por aquí llega el combustible |
| **Cargadero de cisternas** | X 148–214, Z 34–37 | Donde se llenan los trenes de combustible | `muelle_mercancias` de Sagunto (v0–v5), puesto en otra función |
| **Depósito de combustible** | X 144–220, Z 10–31 | El ejército guarda en la estación lo que manda la refinería, aparcando cisternas llenas en tres vías muertas (Z 12, 17 y 22, a 5 m entre ejes) con un talud de tierra de 2 m al norte (Z 25–31, 7 módulos de Teo con yaw 90) y al este (X 214–220, 2 módulos con yaw 0). Al sur lo cierra el muro del recinto y al oeste quedan abiertas las vías | Vía del kit y vagones cisterna. **Castellón empieza con 1 depósito hecho: 100 + 200 = 300 u**, que son 5 días de producción (Hugo, `docs/economia/castellon-bucle.md`). Con el vagón de Teo (18 m entre topes y cuba de Ø 3 m, SIN VERIFICAR), en cada vía muerta de 68 m caben 3: **9 cisternas, cada una de unas 33 u (9 × 33 ≈ 300 u)**, y las que se ven llenas o vacías dicen el stock |
| **Naves de logística y cuartel** | X 68–136, Z 6–22 (tres naves de 20 m) | Polígono junto a la estación. **La primera nave (X 68–88) es el cuartel**: en una principal crea tropas (D-N124 §1) | `almacen_naranjas` de Sagunto girado 90°. Un camino interior (Z 26–32) va de la puerta de vehículos (X 64, Z 25–33) al depósito |
| **Recinto de HESCO** | X 64–222, Z 4–90 | **Lo levantaron los supervivientes de la ciudad.** Al reclamar Castellón se hereda dañado | HESCO y puertas del kit (dos de vía en cada extremo, una de vía para el ramal y la puerta de vehículos D-N111 al oeste) |
| **Puesto v2** | (238; 26), fuera del recinto | Cubre la cabeza del ramal, por donde entra el combustible | `puesto_frente` |

Recuento: **unas 14 piezas del kit y 1 nueva.** Hacen falta 5 variantes del **vagón cisterna** (regla de Eugenio): limpio, oxidado, con la escalera arrancada, con la chapa abollada y quemado. Además, un decal de lleno o vacío, para que el stock se lea en el depósito. Hugo confirmó que el depósito no necesita una pieza nueva.

## 2. Sitios del mapa de frentes y entradas de la horda
- **C1 Estación** (130; 79): el recinto.
- **C2 Depósito de combustible** (178; 22): **el punto que la Colmena busca el día 7.** Está dentro del recinto pero en el borde sur, pegado al muro, para que se note cuando lo atacan.
- **C3 Ronda** (38; 56): el único paso de vehículos sobre las vías. Si cae, el norte y el sur quedan separados.
- **C4 Ramal** (244; 44): la llegada del combustible desde la refinería.
- Entradas: **Ca** por la vía desde Nules (oeste), **Cb** por la vía desde Vinaròs (este; línea cerrada, la horda viene del norte), **Cc** desde las manzanas de la ciudad (norte; la entrada de los asedios grandes, porque es donde estaba la gente) y **Cd** por el ramal desde el Grau.

## 3. «Entrar» en una estación reclamada
- Desde el mapa, al pulsar una estación reclamada, la cámara entra en su zona como en Sagunto. Es la misma escena con otro dato: la disposición, el kit con semilla y los sitios.
- Mientras el jugador no la mira, la estación sigue viva en la simulación abstracta (D-N96: varios frentes a la vez). Si la atacan, su sitio parpadea en el mapa (D-N113/D-N117) y se puede entrar a defenderla.
- **Dato por estación** (propuesta para Nacho): `estaciones/<id>.json` con las vías, los andenes, la lista de piezas (pieza del kit, posición, yaw y la variante por hash de la posición) y los sitios y carreteras como en `mapa_sagunto_carreteras`. Así una estación nueva es un JSON y no una escena hecha a mano. ❓ Hoy `BuildSaguntoWorld` (`PrototypeBootstrap.cs`) está escrito en código; pasar a datos es trabajo de Marcos después del MVP.

## 4. Bucle entre estaciones (lo que se ve dentro; los números son de Hugo)
1. **Cargar en origen.** En Sagunto, el tren se carga de materiales (80 al día, la acería), munición y personas. En el andén se ven los palés y la gente esperando.
2. **Viajar.** Por el mapa, con la ETA y el riesgo de emboscada (desmonte, Palancia y Mijares están por el camino).
3. **Descargar en destino.** En Castellón, el tren para en el andén central. **Un tren lleva 100 u en 5 vagones de 20, y cada vagón deja un montón visible** en el andén y después junto a las naves (Hugo; solo visual, SIN VERIFICAR). Caben unas 30 personas por tren (Hugo, SIN VERIFICAR: el R2 no tiene capacidad en ningún CSV). Las personas bajan y van al edificio de viajeros, que hace de cuartel. La carga y la descarga duran 4 h por viaje (economía §3), fijas: solo el andén de Sagunto las rebaja un 25 %. Las grúas y el muelle de Castellón son decorado.
4. **Construir.** Con los materiales que han llegado se repara el recinto heredado tramo a tramo (D-N123: 1 u repara 5.000), o se amplía. Lo hacen los obreros de la guarnición, y la obra se ve con el estado «en reparación» del muro de Teo.
5. **Producir.** Con 30 personas, Castellón rinde el 100 %, y con 90 el ×2 (tope de 250 y mínimo de 24; Hugo). El combustible llega por el ramal y llena el depósito C2: las cisternas llenas o vacías dicen el stock. Qué pasa al llenarse los 300 u está SIN VERIFICAR (Hugo se lo pregunta a Nacho).
6. **Volver cargado.** El tren se llena en el cargadero de cisternas y vuelve a Sagunto con combustible. Con eso se cierra el bucle: Sagunto pone materiales y gente, y Castellón pone combustible. **Hugo**: un viaje redondo dura ~7,3 h, así que salen 2 viajes al día con un tren (hasta 200 u de combustible, gastando 16). Si carga en los dos sentidos, ~1,5 viajes al día, que también cuadra pero está sin medir. Castellón pesa ×1,5 para la Colmena (D-N34).
- Nules (`nules-nivel.md`) es el mismo bucle con víveres, y empieza con la fundación.
- Las cifras del bucle son de Hugo (`docs/economia/castellon-bucle.md`). Cómo se entra en cada estación y la plantilla por tamaño las define Lucía en `docs/diseno-red-estaciones.md`, y mi §3 se ajusta a lo que ella decida.

## 6. Plantilla de principal y campos del dato (D-N124, `docs/diseno-red-estaciones.md` §2)
Castellón cumple todo lo obligatorio de una **principal** (§2.1): doble vía y haz de mercancías, andén de 120 m con 5 tramos de marquesina, edificio grande (dos del kit en espejo), naves, **sitio de cuartel** (la primera nave, (78; 14)), acceso de vehículos por la ronda, 4 sitios y puertas de vía en los dos extremos. De lo opcional lleva el cargadero, el depósito, el paso superior y los bloques de ciudad. No lleva helipuerto ni taller: el taller solo está en Sagunto, y el helicóptero llega desde Sagunto.
- **Sitio de inteligencia: radar en (206; 82)**, en la esquina noreste del recinto, entre el andén lateral y la avenida. Está dentro del muro, sobre el lado de la ciudad (Cc), que es por donde llegan los asedios grandes. Una alternativa con más altura sería la azotea de un bloque de pisos, pero queda fuera del recinto y no la recomiendo. Cuando llegue el centro de inteligencia de una principal (después del MVP), va en el mismo sitio.
- **Paradas del tren de asalto**, a unos 300 m del centro del andén (130) por cada vía de entrada, todas fuera del encuadre de la zona: **oeste, desde Nules, en (−170; 57,5); este, desde Vinaròs, en (430; 66,5); y por el ramal del Grau en (430; 44).** El pelotón baja y entra andando unos 170 m.
- **Estado inicial: infestada** (propuesta). Los supervivientes resisten en el edificio de viajeros (C1), y C2–C4 están ocupados. Reclamarla es el asalto del §5 en este **orden de liberación: C3 Ronda** (abre el acceso de los vehículos), **C4 Ramal**, **C2 Depósito** y, por último, **C1 Estación**, el corazón y donde está la gente. ❓ Hugo tiene que confirmar que el jugador equilibrado la sigue tomando el día 1 con un asalto en lugar de una simple conexión. Si no, el estado inicial pasa a «propia, con el recinto dañado».
- **Dato**: `estaciones/castellon.json`, con los 5 campos de Lucía, 80 piezas (kit, posición, yaw y variante por hash), vías, andenes, recinto, puertas, carreteras, sitios, cuartel, radar, paradas y orden de liberación.

### 6b. Recinto heredado (Hugo, `docs/economia/castellon-bucle.md` §5)
- **Infestada, confirmado**: con 1000 partidas, el jugador equilibrado la toma el día 1 en todas (asalto abstracto: 760 zombis, tropa de 30 y 1,9 u). Un asalto jugado en la zona está sin medir.
- **Se hereda muy dañado: al 15 % de la vida media y con brechas** (con 482,1 m: 289,3 u nominales y 43,4 u efectivas, nivel 1). Repararlo entero cuesta unas 241 u y 145 h con el tren de obras: es el motivo para volver con trenes.
- **Regla de los 60 m (D-N44: el punto medio de cada módulo, a ≤ 60 m del andén).** Medido contra el rectángulo de los andenes (X 70–190, Z 60–73), con módulos de 10 m, solo quedaban fuera ~19 m de la esquina sureste, junto al depósito. **Arreglo: chaflán en esa esquina, de (212; 4) a (222; 14).** Así todo el recinto cuenta para el nivel y nada se desgasta sin mantenimiento. El perímetro queda en **≈ 482 m** (488 − 20 + 14,1 = 482,1 m). Las cisternas del depósito siguen dentro.
- Aviso para Hugo y Lucía: si los 60 m se miden **desde el centro del andén** (130; 66,5) y no desde el andén, se quedan fuera unos 380 m de los 488, porque la estación es más larga que el radio. Para una principal, la lectura correcta es «desde el andén». En Nules las dos lecturas dan lo mismo.

## 5. Pendiente
- **Hugo**: respondido (6b).
- **Teo**: el vagón cisterna (5 variantes y el decal de lleno o vacío) y el cuerpo central del edificio de viajeros.
- **Paula**: la estación de Castellón y el ramal del Grau, si hay fotos libres.
- **Nacho y Marcos**: el dato por estación (§3), después del MVP.
- **FPS**: 12 bloques, 2 edificios de viajeros, 5 marquesinas, unos 20 coches, 12 cisternas (9 en el depósito y 3 en el cargadero) y el recinto. Menos vegetación que Sagunto. Hay que medirlo (D-N70).


## 7. v0.1: la estación es subterránea, como la real (Álvaro (3), 8-nov, ~18:10; kit de Teo, D-N156)
**Real (Paula):** Castelló está bajo tierra (`linea_valencia_castellon.md`, PK 73,60). La foto RC3 muestra un andén lateral y otro con fila de pilares redondos, vía en placa, losa con vigas de canto y catenaria colgada del techo. La v0, con la estación en superficie, cambia así:
- **Cota de vía: −8 m** (SIN VERIFICAR). Las vías generales siguen en Z 57,5 y 66,5, el andén central en Z 60–64 y el lateral en Z 69–73, con X 70–190.
- **Cajón bajo losa en X 70–190**, de Z 55 a 74. Lleva el módulo central de Teo (14 m, Z 55–69: andén central y las dos vías, pilar de Ø 0,9 m cada 10 m en Z 62) y el lateral (Z 69–74, con el muro de fondo en Z 73,5–74). El intradós queda a 6,5 m sobre la vía (cota −1,5) y la losa tiene 1,5 m, así que su cara de arriba es el suelo de la ciudad (cota 0): se pisa como la plaza. **La losa es un hijo aparte («Losa»)**, y Marcos la funde con la cámara cenital cuando hay unidades debajo.
- **Trinchera abierta en X 0–70 y X 190–256**, con muros de contención de 8 m en Z 55 y Z 74. Por ahí se ve entrar y salir el tren desde la cámara. Las rampas reales quedan fuera de la zona. La **ronda** (X 34–42) pasa por encima de la trinchera como puente: es el paso superior de siempre.
- **Puertas de vía, en la trinchera**: en X 64 y X 222, sobre las dos vías, a la cota −8. El HESCO del recinto va por arriba, por los dos bordes de la trinchera. Nadie sale de la trinchera trepando: solo por los extremos (Ca y Cb) o por las escaleras del vestíbulo.
- **Vestíbulo de calle** (pieza nueva de Teo: 24 × 14 m, 5 m de alto, con los 5 estados de la D-N124). Va en **(130; 0; 81)**, X 118–142, Z 74–88, con la **entrada principal hacia la plaza (norte, yaw 0)** y la **boca de escaleras al sur**, que baja por el muro de fondo al andén lateral (Z 69–73). Del andén lateral al central se pasa por el paso inferior del kit (`kit_paso` v0, en (120; 66,5)). **Sustituye al edificio de viajeros de la v0** (las dos alas de Sagunto y el cuerpo central se quitan; en X 96–118 y X 142–164 de Z 75–88 queda plaza).
- **C1 Estación** pasa a (130; 81), el vestíbulo. Los supervivientes resisten en el vestíbulo y en los andenes. Recuperarla es limpiar los andenes bajo la losa: una ratonera con dos entradas por la vía y una por la escalera.
- **Lo que se queda en superficie**: el haz de mercancías (Z 44–52), el ramal del Grau, el cargadero, el depósito C2, las naves, el cuartel, el radar (206; 82), la plaza, los bloques y el recinto. Entre el haz (cota 0) y el cajón hay un muro de contención en Z 54–55. El enlace del haz con las generales queda fuera de la zona.
- **Catenaria rígida** colgada de la losa, con el hilo a 5,3 m sobre la vía (RC3; que sea rígida está SIN VERIFICAR).
- **Barricadas civiles** en tramos de 8 m (como los sacos) en la plaza y la avenida. **Vagones abandonados** de 18–20 m en las vías del cajón y en el haz.
- **Para Iker**: la parada del tren en Castellón es a la cota −8. La tropa baja al andén y sube por la escalera del vestíbulo. El desnivel es de **unos 7,1 m**, de la cota −7,1 del andén a la calle (corrijo los 12 m que había puesto antes; SIN VERIFICAR con la cota real). El tiempo de subida lo pone Nacho.
- **Bajada de vehículos (v0.2, 18:15)**: los vehículos no bajan en el andén. Bajan en superficie, en la **cabeza oeste del cargadero, X 140–148**: el tren para en la **vía 44 del haz** con la plataforma de vehículos en X 140–148, al oeste del muelle (X 150–222). El **punto de bajada es (144000; 38000) mm**. De ahí salen al sur por tierra hasta el camino interior (Z 29, que acaba en X 144) y siguen hasta la puerta de vehículos. No uso la rampa del muelle porque no tengo verificado a qué lado sale.
- **castellon.json v0.2**: quitados el edificio de viajeros viejo (`kit_cuerpo`/`kit_remate`, 7 piezas) y las 5 marquesinas, que no van bajo la losa. Los 24 `kit/anden_10m` y el `kit_paso` bajan a la cota −8. Añadido el vestíbulo (`castellon/vestibulo`, nombre SIN VERIFICAR hasta que lo dé Teo). Datos nuevos en `subterranea.bajada_vehiculos` y en `vestibulo.desnivel_escalera_m`.
- **castellon.json v0.4 (18:15, piezas de Teo aprobadas por Lucía)**:
  - 24 `castellon/anden_losa` (Central en Z 62 y Lateral en Z 71, cada 10 m de X 75 a 185, a −8).
  - 24 `castellon/catenaria_losa` sobre Z 57,5 y 66,5.
  - 28 `castellon/muro_trinchera` Muro: 7 por cada lado y trinchera, en X 5–65 y 195–255, con el origen en Z 54,7 (yaw 180) y en Z 74,3 (yaw 0), para que la cara vista quede en Z 55 y 74.
  - 2 bocas, en X 70 (yaw 90) y en X 190 (yaw 270).
  - 4 `castellon/barricada_civil` en Z 92, en X 110, 118, 142 y 150. Dejan un hueco en X 122–138 frente a la entrada del vestíbulo, y la avenida queda libre para los vehículos.
  - 4 `castellon/vagon_abandonado` (con yaw 90) en las vías 48 y 52 del haz.

  Quedan libres la vía 44, para la bajada de vehículos, y las del cajón, para la parada. Los yaws de muros y bocas los confirma Marcos con la primera pieza.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 8. Mobiliario urbano de Teo (Álvaro (3), 8-nov, ~19:00; mr-mak 71cb05b)
`castellon.json` lleva ahora 11 piezas `urbano/…`, en total 150:
- Paradas de bus en la acera sur de la avenida (Z 92,8), en X 80 y 180, con yaw 0 para que miren a la avenida.
- Quioscos en la plaza del vestíbulo, dentro del recinto: en (104; 84) y el quemado en (156; 84).
- Contenedores en X 60, 92 y 166.
- Señales en X 48 y 200.
- Semáforos en el cruce de la ronda con la avenida: el de brazo en (44; 92,8) con yaw 90, con el brazo sobre la avenida, y el doblado en (44; 103,5).

Ninguno pisa las barricadas (X 106–154). Hay un CSV nuevo, **`castellon_obstaculos_v1.csv`**, que de momento solo lleva el mobiliario sólido: los 2 quioscos y las 2 paradas.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 9. Coste del recinto, calculado como el de Nules (Álvaro (3), 9-nov ~08:05; D-N183, para Hugo)
Sale de `estaciones/castellon.json`. El recinto es [[64,4],[212,4],[222,14],[222,90],[64,90]], todo de HESCO (0,6 u/m), y con el chaflán SE mide **482,14 m**.
- **Huecos que se restan:** la trinchera, de 19 m (Z 55–74), en X 64 y en X 222. Ahí no hay HESCO: las 4 puertas de vía están abajo, a −8, entre los muros de contención. También se restan la puerta del ramal (222; 44), de 5 m, y la de vehículos (64; 29), de 8 m. Quedan **431,14 m de muro, que son 258,69 u**.
- **Puertas:** 5 de vía × 8 u (las 4 de la trinchera y la del ramal) y 1 de vehículos × 10 u, que suman **50 u**.
- **Total: 308,69 u**, entero y construido. Si las 4 puertas de la trinchera se restaran como en Nules (5 m cada una, en vez de los 2 × 19 m), saldrían 449,14 m: 269,48 + 50 = **319,48 u**. Recomiendo los 308,69 u, porque sobre la trinchera no hay muro.
- Ojo: es casi 2,6 veces Sagunto y llega al tope de nivel 5. La economía la decide Hugo (en su §5 de castellon-bucle.md proponía heredarlo al 15 %).
- **Hugo (07:45):** usa los 308,69 u, que entran enteros al empezar. Para compensar, sube el H0 de la Colmena a 1400 (equilibrado 14,0 %).
