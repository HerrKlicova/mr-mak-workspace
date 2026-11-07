# Nules · emplazamiento fundable v0 (Álvaro, 7-nov, solo papel)

Es el único emplazamiento fundable de la demo (D-N18, D-N49; `diseno-hito5.md` §4). Se funda el día 3 con un tren parado que lleve 30 u y 12 personas, sin horda encima (densidad < 500), y produce víveres de la huerta. Uso la plantilla del desmonte: cada cosa tiene que tener una razón de estar ahí. Plano: `nules_plano_v0.png`; script: `herramientas/plano_nules_v0.py`; dato: `mapa_nules_carreteras_v0.json`. Para después del MVP, sin código.

## 0. Conclusión
El GDD (§9b) dice que los emplazamientos se eligen por **terreno llano, agua y cruce de caminos**. Nules v0 dibuja esas tres razones en el sitio:
- la huerta llana de naranjos de la Plana;
- una acequia con su pozo y su motor de riego;
- el cruce del camino de la Vilavella con la avenida de la Estación, en un paso a nivel.

Además, lo que produce tiene edificio: la **cooperativa citrícola** junto a la vía. Lo que se funda es la estación vieja, que está abandonada. Por eso el jugador no empieza de cero: hay andén y un edificio que sirve de primer refugio para las 12 personas.

**Aviso de realidad:** Nules sí tiene estación real en la línea de la costa (Nules–La Vilavella, SIN VERIFICAR con fuente). En el juego se lee como «estación abandonada que se vuelve a abrir», no como un descampado. Paula todavía no tiene fotos de Nules, así que la disposición es genérica de la Plana y va **SIN VERIFICAR** entera.

## 1. Disposición (coordenadas locales de la zona, 256 × 128 m, vía en Z 64,5)
| Elemento | Dónde | Por qué existe | Qué hace en el juego |
|---|---|---|---|
| **Andén de 60 m** | X 100–160, Z 67,5–71,5 | La estación vieja | Donde para el tren de fundación (`fundar_radio_tren_mm` 5000). Es el centro de los 60 m que cuentan para la fortificación (D-N44) |
| **Edificio de viajeros abandonado** | X 121–139, Z 74–82 | La estación vieja | Primer refugio. Sitio N1 |
| **Cooperativa citrícola** con muelle a la vía | X 140–176, Z 34–55 | En la Plana, las cooperativas se pusieron junto a la vía para cargar la naranja | **La producción de víveres.** Sitio N2, a unos 40 m del centro del andén: entra en el perímetro de 60 m |
| **Naranjal en hileras** cada 5 m | Norte (Z 92–126) y esquinas del sur | La huerta | Lo que se protege. Tapa la vista: la horda Nc sale de entre los árboles a menos de 30 m |
| **Acequia y pozo con motor** | Acequia en Z 100; caseta en X 196–204 | El agua que hace fundable el sitio | Línea de lectura de noche y punto de referencia. Más adelante podría ser un objetivo (sin agua, no hay víveres) |
| **Camino de la Vilavella y avenida de la Estación** | X 76–84, de norte a sur | El cruce de caminos | Acceso de los vehículos (D-N96) y entrada Nd desde el pueblo |
| **Paso a nivel sin barreras** | (80; 64,5) | Lo abandonaron cuando se cerró la estación | Sitio N3: el único sitio por donde un vehículo cruza la vía |
| **Ramal de tierra a la cooperativa** | Z 28–34, de X 84 a 160 | Para los camiones de la naranja | Habilitado: lleva los vehículos a N2 |

## 2. Fortificación sugerida (lo construye el jugador; el plano solo lo propone)
- **Trazado de 150 m de HESCO**, 44 × 31 m (X 108–152, Z 56–87), alrededor del andén y del edificio de viajeros. Es la cifra del ejemplo de la D-N44 (150 m de HESCO, una puerta, dos nidos y tres focos: 118 u). Todo queda a 60 m o menos del centro del andén.
- Al cruzar la vía, el recinto necesita **dos puertas de vía** (oeste y este), igual que el de Sagunto, además de **una puerta de vehículos** al sur, hacia el ramal y la cooperativa. Son dos puertas más que en el ejemplo de la D-N44. **Hugo (docs/economia/nules-recinto-v0.md): 127,2 u y 90,8 obrero·h** (cada puerta de vía cuesta 8 u, D-N59), con un mantenimiento de ~1,27 u al día y 0,6 u de combustible por noche. Criterio de Hugo: en la primera noche, la descarga con las dos puertas abiertas no debe coincidir con una oleada.
- La cooperativa queda **fuera del recinto**, a 15 m de la puerta de vehículos. Es a propósito: es lo que la horda ataca y obliga a elegir entre ampliar el muro o defenderla con un puesto. Es un frente del mundo persistente (D-N96) desde el primer día.

### 2b. Recinto v0 tramo a tramo (para Hugo, `docs/economia/nules-recinto-v0.md`)
Rectángulo X 108–152 × Z 56–87: **150 m de perímetro**, de los que **132 m son de HESCO y 18 m son puertas**.
| Tramo | Longitud | HESCO | Puerta |
|---|---|---|---|
| Sur (Z 56, de X 108 a 152) | 44 m | 36 m (X 108–126 y 134–152) | **De vehículos**, 8 m, en X 126–134 (modelo de la D-N111) |
| Oeste (X 108, de Z 56 a 87) | 31 m | 26 m (Z 56–62 y 67–87) | **De vía oeste**, 5 m, en Z 62–67 |
| Norte (Z 87, de X 108 a 152) | 44 m | 44 m | — |
| Este (X 152, de Z 56 a 87) | 31 m | 26 m (Z 56–62 y 67–87) | **De vía este**, 5 m, en Z 62–67 |
- Módulos de 10 m como máximo (D-N44, regla 1): sur 2 × 18 m, oeste y este 6 + 20 m, norte 44 m. Todo cae a 60 m o menos del centro del andén (130; 69,5); la esquina más lejana queda a unos 27 m.
- Propuesta de nidos y focos, que no cambian el perímetro: nidos en las esquinas noroeste (108; 87), hacia el naranjal (Nc) y la vía oeste, y sureste (152; 56), hacia la cooperativa y la avenida. Focos en el centro del muro norte, sobre la puerta de vehículos y sobre la puerta de vía este.
- **El tren no queda dentro.** El andén mide 60 m (X 100–160) y el recinto solo 44 m, y el tren de fundación, de unos 70–100 m, sobresale por las dos puertas de vía. Meterlo entero obligaría a un recinto de unos 104 × 31 m, con 270 m de perímetro: casi el doble de material. Mi recomendación es dejarlo fuera. Mientras descarga, el tren queda parado con **las dos puertas de vía abiertas**, y ese es el momento débil de la fundación. Después se va y las puertas se cierran. El tren es un muro móvil (D-N27), así que mientras está parado tapa él mismo los huecos.

## 3. Sitios del mapa de frentes
- **N1 Estación** (130; 78): el recinto.
- **N2 Cooperativa** (158; 44): la producción. Puesto v2 opcional.
- **N3 Paso a nivel** (80; 64,5): el cruce. Si cae, los vehículos se quedan a un lado de la vía.

## 4. Entradas de la horda
- **Na / Nb**: por la vía, desde Almenara (oeste) y desde Castellón (este).
- **Nc**: desde el naranjal del norte, a corta distancia y sin verse.
- **Nd**: por la avenida, desde el pueblo (sur). Es la entrada de los asedios grandes, porque el pueblo es donde estaba la gente.

## 5. Vehículos (D-N96)
Los vehículos llegan en el tren (GDD, contenido del MVP: el blindado viaja en el tren y se despliega). Desde el andén salen por la puerta de vehículos al ramal. **Habilitados**: la avenida (de Z 0 al paso a nivel), el camino de la Vilavella (del paso a nivel a Z 128) y el ramal de la cooperativa.

## 6. Pendiente
- **Paula**: fotos de la estación de Nules–La Vilavella, de una cooperativa citrícola de la Plana con muelle de vía, de una acequia y de una caseta de pozo con motor.
- **Teo** (5 variantes cada una): cooperativa (nave de ladrillo, nave de bloque con cubierta de fibrocemento, nave con marquesina, nave con torre de oficinas y nave quemada), caseta de pozo y acequia (como franja del mapa de zonas). El almacén de naranjas de Sagunto (F4) sirve de base.
- **Hugo**: el coste de las dos puertas de vía y si el día de nivel de estación se mueve.
- **FPS**: unos 500 naranjos. Es la zona más cara de vegetación, y hay que medirla (D-N70). Si no da, el naranjal se pinta en el mapa de zonas y solo las hileras cercanas son 3D.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
