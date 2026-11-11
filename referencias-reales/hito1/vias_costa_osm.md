# Vía Sagunt–Nules (línea 600): datos OSM y fotos · Hito 1

Para Álvaro. Datos: © colaboradores de OpenStreetMap, ODbL. Consulta hecha el 11-nov-2026 en Overpass (overpass-api.de; las estaciones, en overpass.private.coffee porque los otros dos fallaron: 502 y tiempo agotado).

## Vía
- Filtro: `railway=rail` + `ref=600` («FFCC València - Sant Vicenç de Calders», `usage=main`), recortado entre las latitudes 39,67 y 39,86. La relación C-6 2184632 existe («C-6: València-Nord => Castelló de la Plana») y coincide con esta línea. La línea 610/612 (Sagunt–Teruel) cae en la misma caja y la he dejado fuera.
- La vía es **doble** en todo el tramo. En OSM hay dos tipos de carril: uno mixto (`gauge=1435;1668`) y otro solo ibérico (`1668`, desde la latitud 39,727 hacia el norte). Al sur de 39,727, las dos vías van etiquetadas como mixtas.
- Longitud de todas las vías dentro del tramo: 48,1 km (31,3 km mixtos y 16,8 km ibéricos). **Longitud de la línea (de vía doble): ≈ 24,1 km**, entre el sur de la estación de Sagunt y el norte de la de Nules.
- Archivo `via_sagunt_nules_osm.geojson`: cada vía (way) con su id de OSM, ancho, electrificación, velocidad máxima, puente y longitud, más las 8 estaciones y apeaderos. Cifras y puentes también en `via_sagunt_nules_resumen.json`.

## Estaciones (de sur a norte)
| Nombre | Tipo | Lat. | Lon. |
|---|---|---|---|
| Sagunt | estación | 39,67567 | −0,27141 |
| Gilet | apeadero (está en la línea 610, no en la 600) | 39,67941 | −0,32066 |
| Les Valls | apeadero | 39,71926 | −0,23965 |
| Almenara | estación | 39,74867 | −0,21822 |
| La Llosa | apeadero | 39,76777 | −0,20296 |
| Xilxes | apeadero | 39,78278 | −0,19031 |
| Moncofa | estación | 39,82088 | −0,16236 |
| Nules - La Vilavella | estación | 39,85297 | −0,15224 |

## Puentes de la línea 600 (`bridge=yes`; cada uno, con sus dos vías)
El cauce lo he sacado cruzando la geometría con los `waterway` de OSM. Ningún puente tiene `bridge:name`.
| Lat. | Cauce | Longitud (m) | Vías (way) |
|---|---|---|---|
| 39,680 | **Riu Palància** (river) | 128 | 144777742, 144777743 |
| 39,682 | ningún cauce en OSM (seguramente un paso sobre un camino o una carretera) | 13–14 | 311094611/612 |
| 39,727 | Barranc de la Font (stream) | 18–28 | 1272561690/691 (+166458261/262, de 8–9 m, al lado) |
| 39,771 | ningún cauce en OSM | 13 | 241375095/096 |
| 39,811 | **Riu Belcaire** (stream) | 43 | 243665083/086 |
| 39,841 | barranco sin nombre (stream 37088412) | 19–20 | 243665085/088 (+082/089, de 15 m) |
| 39,860 | ningún cauce en OSM (justo en el límite norte) | 18–19 | 243490352/356 |

## Fotos (Commons, a 3840 px; las he revisado una a una)
| Id | Qué muestra | Licencia | Autor |
|---|---|---|---|
| VC1 | Puente del tren sobre el Palancia, de lado: tablero de vigas, pilas y catenaria | CC0 | Joanbanjo (2018) |
| VC2 | El mismo puente entero, de orilla a orilla, y la costa al fondo | CC0 | Joanbanjo (2018) |
| VC3 | Otro encuadre de VC2: pilas y estribos | CC0 | Joanbanjo (2018) |
| VC4 | Viaducto ferroviario con catenaria sobre el Palancia en crecida (2017) y, detrás, un puente de arcos | CC BY-SA 4.0 | ElExploraMontañas |

Hoja de contactos: `contacto_hito1.jpg`. Datos completos en `manifest_hito1.json`.
Descartadas: «Rio palancia desbordado pt2» y «Riu Palància i ponts», porque son puentes de carretera y no de tren.

## Huecos
- **No sé seguro qué línea sale en VC4.** La descripción solo dice «sagunto». Por la catenaria y el tablero ancho podría ser la 600 o la 610, que también cruza el río cerca. VC1–VC3 parecen de la 600 (se ve la costa detrás), pero Commons tampoco lo dice.
- **Belcaire:** en Commons no hay fotos del puente del tren. La categoría «Belcaire River» solo tiene dos fotos de la Vall d'Uixó.
- **Tren por la marjal entre Sagunt y Nules:** se me acabó el tiempo y no lo busqué. Queda pendiente.

— Paula
