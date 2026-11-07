# Castellón · estación de ciudad v0 y bucle entre estaciones (Álvaro, 7-nov, solo papel)

Encargo de Eugenio (7-nov, 09:03): «manda a alguien a diseñar otra estación importante. Que todas las estaciones generales reutilicen los assets de Sagunto, pero de diferente manera. Tienes que poder entrar en cada estación que hayas reclamado. [...] No podemos estar estancados en una sola estación». Plano: `castellon_plano_v0.png`; script: `herramientas/plano_castellon_v0.py`; dato: `mapa_castellon_carreteras_v0.json`. Es papel y no toca la build de esta noche.

## 0. Conclusión
- **Elijo Castellón.** Es la otra estación que de verdad importa en la demo:
  - el jugador equilibrado la toma **el día 1** (economía §1), así que es la primera estación que se reclama después de Sagunto;
  - es la **única fuente de combustible** (60 u al día, la refinería; economía §2), y sin combustible no se mueve ningún tren;
  - es **el talón de Aquiles**: la Colmena va a por ella el día 7 (D-N, idea de Hugo, ya en el guion).
  - Valencia-Nord no sirve como segunda estación, porque es un nido y nunca es segura (D-N14). Teruel llega el día 5 y queda lejos, en el interior.
- **Castellón se monta casi entera con el kit de Sagunto, combinado de otra manera**, y solo lleva **dos piezas nuevas**: el vagón cisterna y el depósito flexible de combustible. Lo propio de cada estación sale de lo que produce, no de un arte distinto.
- **Toda estación reclamada se visita igual que Sagunto**: desde el mapa, se entra en su zona de 256 × 128 m. Se propone un bucle de trenes (§4) que da a cada visita algo que hacer.

## 1. Disposición (coordenadas locales de la zona, vía principal a lo largo de X)
| Elemento | Dónde | Por qué existe | Kit |
|---|---|---|---|
| **Dos vías generales** (Z 57,5 y 66,5) con andén central de 120 m y andén lateral | X 70–190 | La línea de la costa es de doble vía, y una capital tiene andenes largos | Vía, andén y catenaria de Sagunto. Marquesina ×5 (v1–v5 por semilla) |
| **Edificio de viajeros** | X 98–162, Z 75–88 | Estación de capital: más grande que la de pueblo | **Dos edificios de viajeros de Sagunto en espejo** (variantes distintas) unidos por un cuerpo central de ladrillo, que es la única extrusión nueva. SIN VERIFICAR: la estación real de Castellón es moderna y no se parece; la lectura es genérica |
| **Plaza y avenida de la Estación** con coches abandonados | Z 92–104 | La salida a la ciudad | `coche_2000` y la ambulancia del kit |
| **Manzanas de bloques de pisos** | Z 108–124, en toda la X | Es una ciudad: aquí casi no hay casas bajas | `bloque_pisos` v1–v5. En Sagunto había uno solo; aquí son la mayoría |
| **Ronda sobre las vías** | X 34–42, de Z 0 a 128 | La ciudad cruza el haz de vías por arriba | `paso_superior` de Sagunto, con dos vanos. **Es el acceso de los vehículos** desde el sur (D-N96) |
| **Haz de mercancías** de 3 vías | Z 44 / 48 / 52, X 46–230 | Donde se forman los trenes de cisternas | Vía del kit |
| **Ramal del Grau** | Sale por el este en Z 44 | Une la estación con la refinería y el puerto (SIN VERIFICAR con el trazado real) | Vía del kit. Por aquí llega el combustible |
| **Cargadero de cisternas** | X 148–214, Z 34–37 | Donde se llenan los trenes de combustible | `muelle_mercancias` de Sagunto (v0–v5), puesto en otra función |
| **Depósito de combustible del ejército** | X 144–216, Z 6–33 | El ejército guarda en la estación lo que manda la refinería, para no depender del ramal cada día | **Nuevo**: depósitos flexibles con muro de tierra, como los de las fotos H8 (FARP) de Paula |
| **Naves de logística** | X 52–130, Z 14–32 | Polígono junto a la estación | `almacen_naranjas` de Sagunto girado 90° |
| **Recinto de HESCO** | X 64–222, Z 4–90 | **Lo levantaron los supervivientes de la ciudad.** Al reclamar Castellón se hereda dañado | HESCO y puertas del kit (dos de vía en cada extremo, una de vía para el ramal y la puerta de vehículos D-N111 al oeste) |
| **Puesto v2** | (238; 26), fuera del recinto | Cubre la cabeza del ramal, por donde entra el combustible | `puesto_frente` |

Recuento: **unas 14 piezas del kit y 2 nuevas.** De cada pieza nueva hacen falta 5 variantes (regla de Eugenio):
- **Vagón cisterna**: limpio, oxidado, con la escalera arrancada, con la chapa abollada y quemado (este último como resto).
- **Depósito flexible**: lleno, a medias, vacío y arrugado, con una lona encima y roto en un charco seco.

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
3. **Descargar en destino.** En Castellón, el tren para en el andén central. Los palés pasan al almacén, y se ve el montón crecer junto a las naves. Las personas bajan y van al edificio de viajeros, que hace de cuartel. La carga y la descarga duran 4 h por viaje (economía §3).
4. **Construir.** Con los materiales que han llegado se repara el recinto heredado tramo a tramo (D-N123: 1 u repara 5.000), o se amplía. Lo hacen los obreros de la guarnición, y la obra se ve con el estado «en reparación» del muro de Teo.
5. **Producir.** Con la plantilla completa (30 personas), Castellón rinde el 100 %. Con más gente, hasta el doble (economía §2). El combustible llega por el ramal y llena el depósito C2: los depósitos flexibles se ven llenos, a medias o vacíos según el stock. Esto es una de las 5 variantes, y aquí sirve para dar información.
6. **Volver cargado.** El tren se llena en el cargadero de cisternas y vuelve a Sagunto con combustible. Con eso se cierra el bucle: Sagunto pone materiales y gente, y Castellón pone combustible.
- Nules (`nules-nivel.md`) es el mismo bucle con víveres, y empieza con la fundación.
- **Pendiente de Hugo** (se lo he pedido): cuánto ocupa una descarga en el andén, cuántas personas caben en un tren, dónde y cuánto se almacena el combustible (300 u se llenan en 5 días) y si el bucle mínimo le cuadra.

## 5. Pendiente
- **Hugo**: lo del §4, más el coste del recinto heredado (488 m de perímetro) y en qué estado se hereda.
- **Teo**: vagón cisterna y depósito flexible, con 5 variantes cada uno, y el cuerpo central del edificio de viajeros.
- **Paula**: la estación de Castellón y el ramal del Grau, si hay fotos libres.
- **Nacho y Marcos**: el dato por estación (§3), después del MVP.
- **FPS**: 12 bloques, 2 edificios de viajeros, 5 marquesinas, unos 20 coches, 6 cisternas, 7 depósitos y el recinto. Menos vegetación que Sagunto. Hay que medirlo (D-N70).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
