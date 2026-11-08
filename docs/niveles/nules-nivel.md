# Nules-La Vilavella · estación v0.2 (Álvaro (3), 8-nov; v0.1 ~13:40, v0.2 ~17:55 con las piezas de Teo colocadas)

Es la estación del **capítulo 3 del tutorial** («Llevar un tren a Nules», `TutorialGuion.Cap3`). En ese capítulo el jugador manda desde Sagunto munición, materiales, un pelotón y, si quiere, un vehículo, y los descarga en Nules. Es también el **destino de carga** y el origen de los refuerzos de la D-N172, que salen de aquí hacia Sagunto. En el código es una de las 3 estaciones del jugador al empezar (`NetWorld.cs:1343`, base 8; nodo de RailNet en (55; 68)).

- **v0.1** (8-nov, ~13:40): rehecha sobre la **planta real de Paula** (`/mnt/project-files/nules_planta.md`, `nules_planta_pnoa_osm.jpg`, `nules_planta_osm.jpg` y `nules_estacion_detalle.jpg`; OSM con licencia ODbL y PNOA del IGN con CC BY 4.0).
- La v0 del 7-nov (una vía, paso a nivel, huerta y canal al sur) era una disposición genérica de la Plana y queda archivada en [`nules-nivel-v0.md`](nules-nivel-v0.md). **Se quitan el paso a nivel, la huerta y el canal**, porque junto a la estación real no existen.

Plano: [`nules_plano_v1.png`](nules_plano_v1.png) (script `herramientas/plano_nules_v1.py`). Dato: [`estaciones/nules.json`](estaciones/nules.json), con el formato de `castellon.json`.

## 0. Conclusión
- **La estación real es de paso y no tiene vía de carga.** Tiene 2 vías generales elevadas, a 3,8 m entre ejes, y 2 andenes laterales de 205 m. El edificio mide 17 × 21 m y tiene 2 plantas. A un lado está el pueblo y al otro el polígono. No hay pasos a nivel en 300 m.
- **Para que sea un destino de carga, añado lo que propone Paula:** una **vía de apartado con muelle de carga, del lado del polígono**. Es ficción nuestra, pero verosímil, porque en la Plana las naves citrícolas cargaban en la vía. El tren del capítulo 3 entra por el apartado y descarga en el muelle, dentro del recinto.
- **Sin pasos a nivel, la vía parte la zona en dos**: el pueblo queda al norte y el polígono al sur. Los vehículos salen del muelle por el lado del polígono y se quedan en ese lado. El único cruce es el paso inferior, a unos 330 m al noreste, fuera de la zona (faldón). Es el cuello de botella natural de la horda que va del pueblo al polígono (Nd).
- **Datos de la línea** (Paula, `linea_valencia_castellon.md`): Nules-La Vilavella está en el PK 54,98 del C-6, a 21,35 km de Sagunt y a 18,62 de Castelló, con vía doble electrificada. **En OSM no tiene ni una vía de apartado**, lo que confirma que el apartado y el muelle son ficción. La playa de vías real más cercana está en Moncofa (9 vías, a 3,2 km hacia Sagunto).
- **La vía elevada** (`layer=1` en OSM; altura SIN VERIFICAR) va a cota 0 en el MVP, como en Sagunto. El terraplén solo se insinúa en los bordes de la zona.

## 1. Cómo paso la planta a la zona
- La zona mide 256 × 128 m. **X va a lo largo de la vía, hacia Castellón** (al noreste en la realidad), y **Z va hacia el pueblo** (al noroeste en la realidad). Escala 1:1 y sin girar: la vía real va a unos 35° y no lo tengo en cuenta.
- Las medidas están leídas en `nules_estacion_detalle.jpg`, a 0,40 m por píxel. El centro del edificio queda a unos 116 m del extremo noreste de los andenes y a unos 30 m del eje del andén del edificio. Todo lo que no sale de OSM va marcado.

## 2. Disposición v0.1 (coordenadas locales en metros)
| Elemento | Dónde | Fuente | Pieza |
|---|---|---|---|
| **Vía general 1** (ancho ibérico, la del lado del edificio) | Z 66,4, de lado a lado | OSM | `SM_KitVia` |
| **Vía general 2** (tercer carril) | Z 62,6 (3,8 m entre ejes) | OSM y Orden FOM/1630/2015 | `SM_KitVia`, con una variante nueva de tercer carril |
| **Catenaria** | Postes cada ~50 m, a los dos lados | Fotos N1 | Postes de Sagunto, en versión para doble vía |
| **Andén 1** (el del edificio) | X 26–231, Z 68,2–79,2 (205 × 11 m) | OSM | `SM_KitAnden`, 21 módulos de 10 m |
| **Andén 2** | X 26–231, Z 53,8–60,8 (205 × 7 m), con una valla de malla detrás (Z 53,4) | OSM; la valla sale de las fotos N1 | `SM_KitAnden` y valla |
| **Marquesina del andén** | En el andén 1, X 90–160 (unos 70 m) | Fotos N1; longitud estimada por Paula (60–80 m) | `SM_KitMarquesina`, 7 módulos |
| **Marquesina antigua adosada** | Adosada a la fachada del edificio que da a la vía: X 104,5–125,5 y Z 79,2–96 (21 × 16,8 m), con pilares y valla. Cubre toda la franja entre el edificio y el andén | Paula (revisión del 8-nov, fotos N1_2, N1_3 y N1_5): celosía metálica, unos 13 m de vuelo (ESTIMACIÓN). OSM solo dibuja el volumen de teja. Aquí el vuelo es de 16,8 m, dentro del margen de 13–17 m de Paula | Nueva: `nules/marquesina_adosada`, con la celosía del kit |
| **Edificio de viajeros** | Centro en (115; 104,5), X 104,5–125,5 y Z 96–113, con la fachada a la vía (yaw 180) | OSM: 17 × 21 m y 2 plantas. Aspecto según las fotos N1 y E1: encalado, 5 huecos por planta, piñón escalonado con óculo y persianas en a86c50 | Nueva: `nules/edificio_viajeros` |
| **Calle de la Estación**, con aparcamiento en línea | Aparcamiento en Z 80–82 y calle en Z 82–92, **cortada delante del edificio por la marquesina adosada**: tramo oeste X 0–104,5, con la glorieta en (95; 87), y tramo este X 125,5–256 | PNOA | Kit de coches de Teo, estados 0–2 (aparcados) |
| **Plaza con jardín** | X 10–100, Z 92–128 | PNOA | Pinos (los de Bétera), palmeras, bancos y farolas |
| **Manzanas del pueblo** | Z 98–128, a los lados del edificio | PNOA | Casas y bloques del kit de Sagunto |
| **Vía de apartado** | Z 49, desde la aguja (en el faldón oeste, X ≈ −100) hasta la topera (X 184) | **Ficción** (idea de Paula) | `SM_KitVia` y una topera nueva |
| **Muelle de carga** | X 90–170, Z 41,5–47,3, de 1,2 m de alto, con una rampa de 12 m al este (X 170–182) | **Ficción** | Nueva: `estacion/muelle_carga` |
| **Calle del polígono** | Z 31,5–38,5, de lado a lado; por el este va hacia el paso inferior | PNOA; el paso inferior, OSM | Asfalto |
| **Naves del polígono** | Todas en Z 2–29: una nave de 60 × 28 m (X 4–64), el **almacén citrícola** de 90 × 28 m (X 74–164) y una nave de 60,6 × 28 m (X 191,5–252,1; 6 módulos de Teo). Entre las dos últimas queda el patio de carga (X 164–192) | PNOA (naves de 50–150 m). El almacén citrícola es la cooperativa del kit (v0) | Nueva: `poligono/nave`. La cooperativa ya está aprobada (mr-mak e774d0a) |
| **Paso inferior** | Unos 330 m al noreste, fuera de la zona | OSM | Solo faldón, después del MVP |

## 3. Recinto (propuesta; lo costea Hugo)
- **Es un rectángulo de X 85–188 por Z 40–96** que rodea el tramo central de los dos andenes, el apartado y el muelle. **El edificio de viajeros hace de tramo del muro norte**: con 2 plantas es más sólido que el HESCO y queda dentro de lo que se defiende.
- **El perímetro es de 318 m**: 269,2 m de HESCO, 21 m de edificio y 27,8 m de puertas. Es más del doble que el recinto de la v0 (150 m), porque la geometría real obliga a ello: hay dos vías y el edificio está a 30 m de la vía. **Hugo tiene que costearlo.** Como Nules empieza siendo propia y «aislada», propongo que el recinto ya exista al empezar, levantado por los supervivientes, como en Castellón.
- **Puertas**:
  - Oeste: una **puerta de vía doble** de 7,4 m (Z 60,8–68,2) para las dos generales, y una puerta de vía normal de 5 m para el apartado (Z 46,5–51,5).
  - Este: otra puerta de vía doble de 7,4 m. El apartado no llega hasta el este.
  - Sur: una **puerta de vehículos** de 8 m (X 177,22–185,22), justo al pie de la rampa del muelle, que da a la calle del polígono.
  - La puerta de vía doble es una pieza nueva: con 3,8 m entre ejes, dos puertas de 5 m no caben una al lado de la otra.
- Dentro del recinto, los muros oeste y este cortan la calle de la Estación. La cerró el ejército.
- **Tramos para el kit de defensas de Teo** (8-nov, ~13:55). Todo el recinto es de HESCO; no hay tramos de sacos.
  - Sur (Z 40): de X 85 a X 177,22 y de X 185,22 a X 188. La puerta de vehículos queda en **X 177,22–185,22** (v0.2): el brazo de la esquina de Teo ocupa 2,78 m desde el vértice, así que la jamba este cae justo donde acaba.
  - Oeste (X 85): Z 40–46,5, Z 51,5–60,8 y Z 68,2–96.
  - Este (X 188): Z 40–60,8 y Z 68,2–96.
  - Norte (Z 96): de X 85 a X 104,5 y de X 125,5 a X 188.
  - Suman 269,2 m. Hay **4 esquinas exteriores en L**: (85; 40), (188; 40), (188; 96) y (85; 96).
  - Hay **10 remates**: 8 en las jambas de las 4 puertas (si la pieza de puerta no trae sus propios pilares) y 2 contra el edificio, en X 104,5 y X 125,5.
  - Los muros oeste y este cruzan los andenes: hay HESCO sobre el andén, a 0,68 m, en Z 53,8–60,8 y Z 68,2–79,2.

## 4. El tren del capítulo 3 y el de la D-N172 (para Iker y Marcos)
- El tren llega desde Sagunto por el oeste, cambia al apartado en la aguja del faldón y **para con el morro a 2 m de la topera, en (182000; 49000) mm**. Si mide 64 m, la cola queda en (118000; 49000) mm: el tren entero queda junto al muelle y dentro del recinto. La plataforma del vehículo va en cabeza, junto a la rampa.
- **Puntos de bajada (`TrenAnden.PuntoBajada`)**:
  - Tropa y carga: **(130000; 44500) mm**, sobre el muelle.
  - Vehículo: **(184000; 44400) mm**, al pie de la rampa. Sale por la puerta de vehículos.
- **Si Nules está sitiada (D-N166, paso 3.10 del tutorial)**, el tren espera en el apartado, fuera de la puerta oeste (X 20–84), y solo baja la tropa, en **(50000; 44500) mm**, entre el apartado y la calle del polígono. Desde ahí entra por la puerta del apartado. La entrada Na llega justo por ese lado: es el momento débil, igual que en Sagunto.
- Los **refuerzos de Nules de la D-N172** (1 pelotón y 1 Lince) suben por los mismos puntos: la tropa en el muelle y el Lince por la rampa.
- **Hoy la red de trenes tiene una vía por nodo.** Si el código no distingue vías dentro de la estación, basta con que el tren de Nules use el apartado (Z 49) como su vía en la zona. Lo decide Iker.

## 5. Sitios, entradas de la horda y claro del NH90
- **Sitios**:
  - **N1 Estación** (115; 104,5): el edificio, que es a la vez refugio y muro norte.
  - **N2 Muelle** (130; 44,5): la carga, que es lo que viene a buscar el jugador.
  - **N3 Polígono** (215; 35): la calle que va al paso inferior, junto a la puerta de vehículos.
- **Entradas**:
  - **Na**: por la vía, desde el oeste (Almenara).
  - **Nb**: por la vía, desde el este (Castellón, que empieza infestada). Es la que más presiona.
  - **Nc**: desde el pueblo, por el norte. Llega por las calles y entre las manzanas, a corta distancia y sin que se la vea, y choca con el edificio.
  - **Nd**: por la calle del polígono, desde el este, viniendo del paso inferior.
- **Claro del NH90 de 25 × 25 m** (Lucía, 8-nov): en el **patio de carga del polígono**, X 165,5–190,5 y Z 3,25–28,25, con el centro en (178; 15,75). Queda fuera del recinto, a 12 m de la puerta de vehículos. Para que quepa he acortado la nave este de 76 a 60,6 m (6 módulos), y queda 1 m hasta el claro; la longitud de las naves es una estimación, así que no se pierde nada real. Dentro del recinto no cabe ningún claro.

## 6. Para Teo: piezas (5 variantes cada una, con D-N70 y FPS medidos)
- **Nuevas**:
  1. `nules/edificio_viajeros`, de 21 × 17 m y 2 plantas. La fachada del kit (5 huecos por planta y piñón escalonado con óculo) se alarga hasta 21 m, con un cuerpo trasero hasta los 17 m de fondo. Los 17 m de OSM pueden incluir anexos (SIN VERIFICAR).
  2. `estacion/muelle_carga`, en módulos de 10 × 6 m y 1,2 m de alto, con borde de hormigón, rampa de testero de 12 m y topes.
  3. `via/topera`.
  4. `estacion/puerta_via_doble`, de 7,4 m, para dos vías a 3,8 m. Es el modelo de la D-N59, ensanchado.
  5. `poligono/nave`, modular: testeros y módulos de 10 m, 28 m de fondo, cubierta clara y persianas de muelle. Estados: intacta, con la persiana abierta, con la cubierta hundida, quemada y saqueada.
  6. `nules/marquesina_adosada`, de 21 × 16,8 m, en celosía metálica antigua con pilares y valla, adosada a la fachada de la vía (fotos N1_2, N1_3 y N1_5).
  7. `urbano/palmera`, `urbano/farola` y `urbano/banco`, para la plaza (sin colisión).
  8. Vía de tercer carril, como variante de `SM_KitVia`.
- **Del kit**:
  - `SM_KitAnden`: 42 módulos para los dos andenes de 205 m. Hay que confirmar si el módulo sirve para 11 m y para 7 m de ancho.
  - `SM_KitMarquesina`: 7 módulos.
  - La cooperativa, como almacén citrícola.
  - Las casas y los bloques de Sagunto, los postes de catenaria y el HESCO.
  - El kit de coches, para el aparcamiento.
  - El pino de Bétera.
- **El montaje `estacion_nules_v0–v4`** tiene ahora 60 m de andén y un edificio de unos 16,5 × 8 m, así que con la v0.1 se queda corto. Teo decide si lo amplía o lo rehace.

## 7. Pendiente
- **Hugo**: el coste y el mantenimiento del recinto de 318 m (269,2 m de HESCO, 2 puertas de vía dobles, 1 de vía y 1 de vehículos), y si existe ya al empezar.
- **Iker**: si el tren puede usar el apartado como vía propia en la zona, y los puntos de bajada del §4.
- **Paula**: la altura del terraplén. (Lo de la marquesina quedó resuelto el 8-nov: va adosada al edificio y cubre la franja hasta el andén; ver §2.)
- **FPS**: los 410 m de andén y las naves grandes. Hay que medirlo antes de darlo por bueno (D-N70).


## 8. Colocación con las piezas de Teo (8-nov, ~13:50; pendientes del visto bueno de Lucía)
- **Edificio**: el origen está en el centro de la huella de 21 × 17 m y la fachada en −8,5. Va en (115; 0; 104,5) con yaw 180, mirando a la vía. **Marquesina adosada**: el origen está en el centro, en (115; 0; 87,6) con yaw 180; encaja entre la fachada (Z 96) y el andén (Z 79,2).
- **Muelle**: módulos de 10 × 5,8 m, con el canto a 1,7 m del eje del apartado (Z 49 → canto en Z 47,3). Hay 8 módulos de X 90 a 170:
  - la v4 (cabeza oeste con topes) centrada en X 95;
  - las v0–v2 en el resto, por semilla;
  - la v3 (rampa de 12 m) centrada en X 176.
- **Topera**: en (185; 0; 49) con **yaw 0**, porque su cara ya mira a −X, hacia el tren que llega desde el oeste. Así está en el JSON. Se elige entre la v0 y la v5.
- **Puertas de vía dobles**: el origen está en el centro del hueco y las vías quedan a ±1,9 m. Van en (85; 0; 64,5) con yaw 270 (fuera = oeste) y en (188; 0; 64,5) con **yaw 90** (fuera = este), según la convención de la §10.9 de Sagunto (+Z fuera con yaw 0). Lo corrigió Teo.
- **Naves**: módulos de 9,98 m y testeros de 0,3 m. Las dos naves «de 60» llevan 6 módulos (60,6 m), centradas en X 34 y X 221,8.
- **Andenes**: `SM_KitAnden` de 11 m (el andén 1) y de 7 m con yaw 180 (el andén 2, con el borde hacia la vía 2). La vía 2 es `SM_KitVia` v2 (tercer carril), o la v3 si está rota.
- **Urbano**: palmeras (v0–4), farolas (v5–9) y bancos (v10–14), sin colisión.


## 9. v0.2: lista de instancias con las piezas entregadas (8-nov, ~17:55)
- **Dato: [`nules_instancias_v02.csv`](nules_instancias_v02.csv)**, 247 filas separadas por «;»: grupo, prefab, variante (−1 = semilla), x, y, z, yaw, escala_x, en_zona_mvp y nota. Plano de comprobación: [`nules_instancias_v02.png`](nules_instancias_v02.png). Generador: `herramientas/instancias_v1.py` (semillas fijas).
- **Nombres de los LEEME de Teo** (mr-mak-workspace, `entregas/teo-modelado/nules`, `defensas`, `muro-estados` y `kit-estaciones`): `SM_EdificioViajerosNules` (v1 = Segura), `SM_MarquesinaAdosada`, `SM_MuelleCarga` (v4 cabeza oeste, v3 rampa), `SM_PuertaViaDoble`, `SM_NavePoligono_Modulo`/`_Testero`, `SM_Palmera`, `SM_Farola`, `SM_Banco`, `SM_KitVia` (v2 tercer carril), `SM_KitAnden_F11`/`_F7`, `SM_KitMarquesina`, `SM_Cooperativa` v4, `SM_poste_catenaria`, `SM_CocheCivil_*`, y los muros `SM_MuroHesco`, `SM_HescoEsquina`, `SM_HescoRemate` y `SM_HescoCorto1–4`.
- **Muros**: 19 tramos de 10 m sin escalar, 9 cortos, 4 esquinas y **9 remates**. Son 9 y no 10, porque en la jamba este de la puerta de vehículos la esquina SE hace de remate. Lo que sobra en cada tramo (0,55 m como mucho) queda repartido en los dos extremos. Los remates de la derecha de cada hueco llevan **escala X −1**, porque la pieza no es simétrica; si el brazo sale hacia el hueco, se invierte.
- **Andenes, ojo**: con la convención de los LEEME (el borde a −Y de Blender, que es +Z de Unity con yaw 0), el andén 1 (al norte de las vías) va con **yaw 180** y el andén 2 (al sur) con **yaw 0**. El LEEME de Teo dice que el de 7 m va con yaw 180, pero eso sería si estuviera al norte. **Lo comprueba Marcos con el primer módulo.**
- **Lo que sigue SIN VERIFICAR en Unity**: el eje X del exportador (afecta a las esquinas, a los remates y a la escalera) y la posición de las marquesinas del andén a 0,68 m.
- **Claro del NH90**: N-C1 (178; 15,75), de 25 × 25 m, marcado en el plano y en el JSON.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
