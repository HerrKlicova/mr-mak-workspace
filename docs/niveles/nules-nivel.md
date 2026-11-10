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
- **Si Nules está sitiada (D-N166, paso 3.10 del tutorial)**, el tren espera en el apartado, fuera de la puerta oeste (X 20–84), y solo baja la tropa, en **(50000; 44500) mm**, entre el apartado y la calle del polígono. **Con el asedio, las puertas siguen cerradas (D-N151)**: la tropa se queda fuera y combate desde ahí, igual que en Sagunto, sin portillo (corregido el 8-nov a las 23:50; antes decía que entraba por la puerta del apartado). La entrada Na llega justo por ese lado: es el momento débil.
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
- **Muros**: 19 tramos de 10 m sin escalar, 9 cortos, 4 esquinas y **9 remates**. Son 9 y no 10, porque en la jamba este de la puerta de vehículos la esquina SE hace de remate. Lo que sobra en cada tramo (0,55 m como mucho) queda repartido en los dos extremos. Los remates de la derecha de cada hueco son **`SM_HescoRemateEspejo`** (Teo, mr-mak dbef5f3), sin escala negativa, porque con Entities Graphics puede dar caras del revés. Las esquinas van en el origen de la pieza (el centro de la celda de esquina, sobre la línea del muro), así que la puerta de X 177,22–185,22 está bien (Teo).
- **Andenes, ojo**: con la convención de los LEEME (el borde a −Y de Blender, que es +Z de Unity con yaw 0), el andén 1 (al norte de las vías) va con **yaw 180** y el andén 2 (al sur) con **yaw 0**. Teo lo confirmó y corrigió su LEEME (mr-mak dbef5f3).
- **Lo que sigue SIN VERIFICAR en Unity**: el eje X del exportador (afecta a las esquinas, a los remates y a la escalera) y la posición de las marquesinas del andén a 0,68 m.
- **Claro del NH90**: N-C1 (178; 15,75), de 25 × 25 m, marcado en el plano y en el JSON.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 10. Acopio de víveres (Álvaro (3), 8-nov, ~18:40; pieza de Teo en mr-mak af18bac, aprobada por Lucía)
`SM_AcopioViveres_v<n>_<Estado>`: 10 × 6 m, con el largo a lo largo de X y el origen en el suelo, en el centro. Tiene 5 estados, que siguen a las existencias de víveres (D-N176). Hay 5 instancias en `nules_instancias_v02.csv` (grupo `viveres`, ya son 252 filas):

| # | Posición (x; y; z) | Yaw | Sitio |
|---|---|---|---|
| 1 | (69,2; 0; 9) | 90 | Hueco entre la nave oeste y el almacén citrícola |
| 2 | (69,2; 0; 22) | 90 | Ídem |
| 3 | (100; 1,2; 44,4) | 0 | Encima del muelle |
| 4 | (115; 1,2; 44,4) | 0 | Encima del muelle |
| 5 | (155; 1,2; 44,4) | 0 | Encima del muelle |

**Cambio respecto al reparto de Lucía (3 en el patio y 2 en el muelle):** en el patio de carga (X 164–192, Z 2–29) no cabe ninguno, porque lo ocupa el claro del NH90 N-C1 (X 165,5–190,5, Z 3,25–28,25). Las franjas que quedan libres miden 1,5 y 1 m. Así que pongo 2 en el hueco de 9,7 m entre naves (X 64,3–74), girados 90° (en Z no caben 3 de 10 m) y 3 en el muelle. Sobre el muelle quedan libres X 120–140, para la bajada de la tropa, y la rampa. El acopio tiene 6 m de fondo y el muelle 5,8 m, así que sobresale 0,1 m por cada lado: o se acepta, o Teo lo deja en 5,8. **Lucía (18:36): aprobado así.** El claro no se toca y los 0,1 m que sobresalen se dan por buenos.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 11. Huerta: no va en Nules (Álvaro (3), 8-nov, ~18:55; Lucía, 18:52)
Puse el kit de huerta de Teo en la franja X 192–252, Z 40,5–52, y **Lucía lo ha quitado**, por dos motivos: junto a la estación real no hay huerta, y unas tapias sólidas delante del muro este, en la entrada Nb, cambiarían la defensa sin que nadie lo haya medido. **El kit va a la huerta noreste de Sagunto** (`sagunto-nivel.md`). Ya he quitado las filas de `nules_instancias_v02.csv` (vuelve a 252) y de `nules_obstaculos_v1.csv`.

**`nules_obstaculos_v1.csv`** (nuevo, con el formato del de Sagunto) lleva el recinto de HESCO por tramos con sus 4 puertas, el edificio de viajeros, el muelle y las 3 naves. Las alturas de los edificios están SIN VERIFICAR.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 12. Mobiliario urbano de Teo (Álvaro (3), 8-nov, ~19:00; mr-mak 71cb05b, aprobado por Lucía)
Hay 11 filas del grupo `urbano` en `nules_instancias_v02.csv` (pasa a 263). Todo va en la acera norte de la calle de la Estación (Z 92,8) o en la plaza, fuera del recinto (que corta la calle en X 85–188):
- Paradas de bus: en (30; 92,8), y la de la variante Anuncio en (215; 92,8). Las dos con yaw 180, mirando a la calle.
- Quioscos: en (76; 99,5) y el saqueado en (200; 95).
- Contenedores: en X 12, 196 y 230.
- Señales: en X 4 y 192.
- Semáforos: el de brazo en (80; 92,8) con yaw 270, para que el brazo quede sobre la calzada, y el peatonal en X 190.

En `nules_obstaculos_v1.csv` entran los quioscos (sólidos, tapan la vista), las paradas (obstáculo bajo de 0,5 m que no tapa la vista) y el panel de la parada Anuncio, que sí tapa la vista.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 13. Huerto de víveres alrededor del recinto: propuesta (Álvaro (3), 8-nov, ~20:10; D-N176 y D-N178)
Lucía lo pide para el kit de víveres que va a modelar Teo (referencias de Paula en `referencias-reales/nules_viveres/`, ninguna de Nules). Esta parte cambia respecto a la §11: allí se quitó la huerta porque cambiaba la defensa sin medir; ahora entra por la D-N176 (víveres), y **Nacho tiene que medir Nules con las tapias** antes de que entren en la build. Las posiciones son definitivas en cuanto lleguen las medidas de Teo. **Aprobado por Lucía (08-11, 21:20).**

**Reglas**:
- Los naranjos no cortan la vista, las tapias sí (D-N178).
- Las tapias dan cobertura a la tropa que combate fuera.
- **No se tapa ninguna entrada de tren**:
  - las vías generales (Z 60,8–68,2) en X 85 y X 188;
  - el apartado (Z 46,5–51,5) desde el oeste;
  - el punto de bajada con asedio, en (50; 44,5).
- El claro N-C1 y la puerta de vehículos (X 177–185) quedan libres.

**Parcela este** (X 192–252, Z 40,5–52, entre la calle del polígono y la valla del andén 2). Es la que da la cara a Nb (por la vía) y a Nd (por la calle):
- **Tapia del testero este**, de norte a sur, en (250; 46), con yaw 90: tramo roto, de 10 m (Z 41–51). Es cobertura de cara al este.
- **Tapia de la calle**: 3 módulos en Z 40,5 (X 227, 237 y 247), con yaw 180 y el portón en X 237. Es cobertura de cara al sur, hacia Nd. Desde X 192 hasta 222 la calle se deja abierta.
- **Casa de labor** en (205; 46), con la fachada a la calle (yaw 180). **Balsa** en (217; 47).
- **Naranjos**: 3 hileras en Z 43, 46,5 y 50, de X 224 a 248, cada 4 m (21 árboles).

**Franja oeste** (X 8–80, Z 38,5–46,5, entre la calle y el apartado): **solo naranjos**, sin tapias. Tapias aquí taparían la bajada de la tropa con asedio y el apartado.
- 2 hileras en Z 41 y 44,5, de X 10 a 78 cada 4 m.
- Sin árboles en X 44–56, que queda libre alrededor del punto de bajada (50; 44,5).
- Son unos 30 árboles.

**Para Teo**: hacen falta unos 51 naranjos, 4 módulos de tapia de 10 m (uno roto y uno con portón), 1 casa de labor y 1 balsa. La casa de labor debería caber en unos 10 × 8 m.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

### 13.1 Colocación con las piezas de Teo (20:20; mr-mak 263c2b8, que todavía es local)
Son 17 filas del grupo `huerto_viveres` en `nules_instancias_v02.csv` (pasa a 280). Las tapias y la casa de labor van en `nules_obstaculos_v1.csv`.
- **Tapias** (10 × 0,4 × 2,2 m):
  - testero Roto en (252; 46), con yaw 90;
  - en la calle, en Z 40,5 con yaw 180: X 227 (Recto), X 237 (Portón, hueco en X 235,8–238,2) y X 247 (Recto).
- **Casa de labor** v2 (Porche) en (205; 47), con yaw 180: casa en X 200–210 y Z 43–51, y el emparrado hasta Z 40. **Palots** (Bloque) en (214; 44).
- **Naranjos**:
  - parcela este: hilera adulta en Z 44 y joven en Z 48, en X 223 y 239;
  - franja oeste: 2 hileras (Z 40,6 y 44,5) en X 18, 34 y 66, con X 44–56 libre.
  - En total son 10 piezas de hilera, sin colisión.
- **Balsa** (Ø 16,4 m): **no cabe** en la parcela, que tiene 11,5 m de fondo. Va en el **faldón este, en (264; 49,5)**, sin colisión y fuera de la zona del MVP.
- **Las tapias no entran en la build hasta que Nacho mida Nules con ellas** (Lucía, 21:20).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 14. Revisión del recinto de Teo (mr-mak `entregas/teo-modelado/nules-recinto/`, 9-nov ~01:30)
Lista de 43 piezas sacada de `RecintoPlan.Nules()`: HESCO al este y en alas de 15 m, sacos en el resto y el edificio como muro norte. Teo me pide tres decisiones. Además he encontrado un problema que no había preguntado.

**Hallazgo: los sacos del muro oeste sobre los andenes.** Los andenes van de X 26 a X 231 (§2), así que cruzan los muros oeste y este por fuera y por dentro. En esos tramos el suelo está a 0,68 m: un muro de sacos de 1,2 m colocado a y 0 solo asoma **0,52 m** sobre el andén, y un zombi que llega andando por el andén lo tiene a la altura de la rodilla. El HESCO (2,1 m) asoma 1,42 m, que es lo que ya ponía la v0.2 (§3). **Cambio: el muro oeste pasa a HESCO en los dos cruces de andén**, que son Z 52,4–59,9 (entre la puerta del apartado y la doble) y Z 69,1–~80 (desde la doble hasta pasar el borde del andén 1, en Z 79,2). Teo ajusta el corte exacto a celdas de 1,11 m. El resto del muro oeste sigue de sacos. El muro este ya es HESCO y no cambia. SIN VERIFICAR: que el andén sea un sólido de 0,68 m en Unity (ver §9). Hugo: el coste lineal cambia un poco si el HESCO cuesta distinto que los sacos; Teo lo saca con su código.

**1) Puerta de vehículos en X 177,22–185,22: sí.** Es la v0.2 (§3) y ya está así en `nules_obstaculos_v1.csv` (muro_sur_0 llega a X 177,22). El hueco sigue midiendo 8 m y el punto de bajada (184; 44,4) queda dentro. Cambia el JSON de Marcos (`estacion_nules.json`) y la simulación de Nacho.

**2) Remates con vuelta:**
- **Puertas dobles (piezas 36, 40, 15 y 18): se cierran con cortos, sin vuelta.** Las cuatro celdas caen encima del andén, al final y a 0,9 m del borde, justo donde se descarga el tren, y además se hundirían 0,68 m en él. Así queda igual que en Sagunto.
- **Puerta del apartado (piezas 41 y 42):** la 41 desaparece con el cambio a HESCO (ese tramo se cierra con cortos). **La 42 se queda**: su celda (X 85,5–86,6, Z 44,5–45,6) no toca nada.
- **Contra el edificio (25 y 32): se quedan.** Las celdas (Z 94,4–95,5) quedan fuera de la marquesina adosada (X 104,5–125,5) y de la calle (Z 82–92).
- **Puerta de vehículos (12): se queda.** Su celda pisa 0,17 m el pie de la rampa del muelle (X 170–182, Z 41,5); es una tolerancia aceptable y no estorba al paso.

**3) Solapes del muro oeste de sacos:** el de 2,2 m entre la esquina SO y el apartado **se queda así**: quitar el remate dejaría un hueco de 1,7 m que solo se puede tapar con un tramo aplastado (escala 0,21). El de 0,3 m entre el apartado y la doble desaparece con el cambio a HESCO.

Las puertas oeste no se mueven, así que la D-N177 sigue igual. Con estos cambios, Teo regenera la lista y yo la miro una última vez antes de que vaya a Marcos.

**Aprobado por Lucía (9-nov 01:23).** Teo regenera la lista y va a Marcos. Pendiente: que Nacho confirme si el recinto de NightSim con el que midió 2200 y 2440 ya tenía estos tramos de HESCO; si no, repite solo el punto de 2200. Nacho (01:24): la puerta no altera las medidas; el HESCO del oeste entra en su próxima tanda de Nules, y en ella repite el punto de 2200. Matiz de Nacho (01:24): en NightSim todo el muro mide 2,1 m y la trepada no depende del material (240 ‰/s, máximo 55/s). El HESCO solo cambia la vida del tramo: 6 u frente a 2 u por cada 10 m de sacos. Repite el 2200 dando triple vida a esos tramos del oeste. Que el HESCO frene también la trepada sería una regla nueva, y la decide Lucía. **Lucía (01:24): la trepada no se toca antes del MVP.** Si el nuevo 2200 se aleja menos de 2 puntos del 96 %, todo queda como está.

**Lista regenerada (mr-mak a75067c, 42 piezas): OK de Álvaro (01:27).** Muro oeste en HESCO de Z 52,4 a 59,9 (cortos 3 + 4) y de Z 69,1 a 80,21 (corto 1 + tramo de 10 m). Las dobles van sin remates. Quedan 4 remates (41, 12, 24 y 31). Tolerancia aceptada: los cortos centrados se meten de 0,13 a 0,33 m en la jamba de 0,9 m (oeste Z 52,27 y 60,04; este Z 60,23), pero no tocan el hueco libre. **Coste: 132,24 u** (90,24 de muro + 42 de puertas), antes 124,08, porque 20,41 m pasan de sacos a HESCO. Para que el juego cuente lo mismo, `RecintoPlan.Nules()` tiene que poner HESCO en esos dos trozos (Marcos). Hugo, tenlo en cuenta.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

**Medida de Nacho (01:33):** Nules 2200 con el HESCO del oeste a triple vida gana 486 de 500 semillas (97,2 %); antes, sin él, 96 % en 200 semillas. La diferencia está dentro del ruido y los trepadores no cambian (1542 frente a 1535). Como se mueve menos de 2 puntos, **la horda de 2200 se queda**, según la regla de Lucía.

## 15. Terreno definitivo de Nules (opción B): dos flancos, la vía y el norte (Álvaro (3), 9-nov ~23:00; encargo del coordinador con libre albedrío de Eugenio)
Plano: [`nules_terreno_b.png`](nules_terreno_b.png) (lo genera `herramientas/plano_nules_b.py`). Es el Nules de verdad para cuando se deje la opción A, la del terreno de Sagunto. El recinto es el de Teo, a75067c (§14), y no se toca.

**La idea:** con 2 pelotones no se defienden cuatro lados. El jugador tiene que leer en cuanto entra que la horda llega por dos sitios, **la vía, al oeste, y el norte, por la plaza**, y que la esquina noroeste es la bisagra entre los dos.
- **Entradas** (`estaciones/nules.json`, ya con peso y rectángulo de aparición):
  - **Na**, por la vía desde el oeste: **50 %**. Es el flanco de la vía, con la emboscada del segundo tren al oeste.
  - **Nc**, desde el pueblo por la plaza (X 20–100): **40 %**. Es el flanco norte.
  - **Nb**, por la vía desde el este: **10 %**, porque Castellón ahora es tuya y está cercada (D-N184).
  - **Nd**, por el polígono: **0 %**.
- **El norte se lee**: una **explanada sin sólidos en Z 96–111**, delante de los sacos del muro norte, y detrás **una hilera seguida de 14 casas** del kit del pueblo, en X 129–207 y Z 116 (yaw 180, con la fachada a la explanada). La hilera cierra el lado este, así que el norte solo puede entrar por la plaza, que está abierta (palmeras sin colisión), y llega de frente a la esquina noroeste. Las casas van en `nules_instancias_v02.csv` (grupo `pueblo`) y en `nules_obstaculos_v1.csv` (`manzana_norte`, 7 m).
- **Guarnición** (`guarnicion_puestos_v1.json` v1.3, `Nules_B_terreno_propio`):
  - **Fusileros**: en el HESCO del oeste sobre el andén 2 (87; 56,2), cubriendo las dos puertas oeste. No cambian.
  - **Ametralladores**: pasan a la **esquina noroeste por dentro, (87,5; 93), mirando al noroeste**. Tiran por encima de los sacos (1,2 m; con la D-N174 la zona ciega es de menos de 1,5 m) hacia el oeste (la vía) y hacia el norte (la plaza). Antes iban junto al edificio, mirando al apartado.
- **`nules_obstaculos_v1.csv` al día con el recinto de Teo**: el muro ya no es todo de HESCO. Lleva sacos al sur, al norte y en las puntas del oeste, y HESCO al este, en las alas de 15 m y en los dos cruces de andén del oeste (Z 51,5–60,8 y 68,2–80,21).
- **Postes de catenaria** (`nules_instancias_v02.csv`): con yaw 0 y 180, la ménsula quedaba a lo largo de la vía. Pasan a **yaw 270 en Z 68,2** (el mástil en Z 69,6, sobre el andén 1, y la ménsula hasta la vía 1, en Z 66,4) y a **yaw 90 en Z 60,77** (el mástil en Z 59,4, sobre el andén 2, y la ménsula hasta la vía 2, en Z 62,6). La cuenta del mástil está en sagunto-nivel.md §10.23.
- **Por medir (Nacho)**, cuando Nules pase a la B: la horda de la noche 2 con estas entradas y estos puestos. La emboscada y el 96 % de la A no valen para la B.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

**Lucía (22:15): aprobado** para la opción B, después del MVP. Cuando toque, Nacho mide con los objetivos de siempre (noche 2 con el objetivo cumplido ≥ 90 %; emboscada sin escolta, tren perdido; con escolta ≥ 90 %). Si no se llega, se cambia la cifra de la horda, no el terreno.
**Suelo (22:20, para Bruno):** `nules_zonas_1m.png` (1 m/px, X −80..336, Z −80..208, mismos ids que Sagunto; `nules_zonas.json`, generador `herramientas/zonas_nules.py`). mr-mak d7d2b89.

## 16. Acopios de carga en Nules (encargo de Bruno, 9-nov ~23:10)

Ya están las filas en `nules_instancias_v02.csv` (grupo `acopios`) y las cajas en `nules_obstaculos_v1.csv`. Los tres van dentro del recinto, al norte del andén 1, en Z 88 y con yaw 0:

| Acopio | X | Huella |
|---|---|---|
| Munición | 140 | X 135–145, Z 85–91 |
| Combustible | 152 | X 147–157, Z 85–91 |
| Materiales | 164 | X 159–169, Z 85–91 |

Lo que tienen alrededor:
- **Coches aparcados en Z 81** (X 140–170, que ocupan Z 80–82): pasillo de 3 m.
- **Muro norte** (cara interior en Z 95,5): pasillo de 4,5 m.
- **Andén 1 y marquesina** (Z 73,7): más allá de los coches, sin cruce.
- **Hueco libre:** queda X 170–173, para llegar al tramo HESCO del muro norte.

Las cajas miden 1,8 m de alto, tapan el paso y no la vista. La variante la manda el estado del acopio: 0 lleno … 4 quemado.

**Nules A:** con el terreno de Sagunto que usa la partida de 30 minutos, valen los mismos sitios de Sagunto (§10.24 de sagunto-nivel.md).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

## 17. Puesto de la fachada este (D-N194), para la noche 2 de Nules (Álvaro, 10-nov ~11:00)

**Qué falla.** Con la D-N193, la noche 2 sigue cayendo a las 01:51 en la zona (I-Noche139), sin bajas y con 18,6 u sin gastar. Los trepadores entran por el tren y la puerta de vía este (X 142–159, Z 65–68) y van por dentro del recinto hasta la esquina SE y la fachada este del edificio: (115,9; 75,5), (116,0; 76,1) y (118,4; 74,4). La guarnición está en la banqueta oeste (X 71,5) y en la azotea del ala oeste, y el edificio (caja sólida de 11 m, 96,5–115,5 × 75,2–83,6) se los tapa.

**El puesto: fusileros en (124,0; 75,5), en el suelo, mirando al este (rumbo 0), en Línea.**

| Dato | Valor |
|---|---|
| Plantel (mm) | X 124000, Y 75500, rumbo 0 (este), `Formation.Linea`, cota 0 |
| Despliegue (2,2 m entre hombres) | con 8 hombres, Z 66,7–82,1; con 4, Z 73,3–77,7. No llega al tren (borde en Z 66,1) ni al muro norte (cara interior en Z 84,5) |
| Fachada este (X 115,5, Z 75,2–83,6) y esquina SE | a 8,5–9 m, sin nada en medio |
| Tramo del andén por donde suben (X 125–156, Z 66–72) | a la vista; el tren (Z 64,5, 2,2 m de alto) queda al sur de todas esas líneas |
| Puerta de vía este (156; 64,5) | a 34 m |

He comprobado las líneas de visión con `sagunto_obstaculos_v1.csv` y la regla de la D-N174. Hacia los tres puntos de la fachada y hacia el tramo del andén no cruzan ningún obstáculo. El fusil dispara en 360° (solo la ametralladora emplazada tiene arco), así que puede mirar al este, de cara a la entrada, sin perder la fachada.

**Cómo se llega (criterio 2).** Andando por el andén 1, de la banqueta a X 124, por la franja Z 66–75 que queda entre el tren y la fachada sur. Eso lo resuelve ya el A* de los pelotones. No hay que construir nada.

**Coherencia con las fotos de Paula.** En la estación real (`nules_planta.md`, N1_estacion_2/3/5), el andén sigue al este del testero bajo la marquesina, con pilares y valla. El puesto queda en ese tramo, junto al testero, entre la cocina de campaña (121; 78) y las tiendas (X 132–148, Z 80) del kit vivo. Ninguna de esas piezas tiene colisión.

**Quién va (criterio 3: siguen siendo 16).** Dos opciones para que las midan Nacho e Iker (criterio 4):
1. **Recomendada: el pelotón «fusileros:4» de la banqueta (71500; 68500) pasa a este puesto.** Como queda como el puesto de tierra más al norte (Y 75,5 > 58,5), la colocación de la D-N192 lo completa a 8 con la escolta sin tocar el código. Solo cambia una fila del Plantel. Riesgo: la mitad norte de la puerta de vía oeste se queda solo con los ametralladores de la azotea, que la cruzan desde (84,5; 76,3).
2. Los fusileros:4 se quedan en la banqueta, y la escolta superviviente va primero a este puesto (hasta 8) y después a los extremos. Hay que tocar `PrototypeBootstrap.Reloj.cs` (D-N192). Con 4 bajas en la escolta, el puesto tendría 4 hombres.

Con el tutorial, el pelotón del capítulo 3 sigue en (71500; 72000). Nules B (`Nules_B_terreno_propio`) no cambia: tiene otro edificio y es para después del MVP.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)

**Lucía (10-nov 10:45):** el puesto cumple. Entre las dos opciones decide la medida de Nacho. Si dan lo mismo, se queda la 1, para que el puesto no esté vacío si la escolta llega tarde o diezmada.

**D-N195 (Lucía, 10-nov 11:00), sustituye a las dos opciones de arriba.** Gana el orden de llenado de Nacho:
1. los puestos norte y sur de la puerta oeste, hasta 8 cada uno;
2. este puesto, hasta 4;
3. la banqueta, que puede quedarse a 0.

Medidas de Nacho:
- orden de Nacho: 98,5 % y 0,9 bajas;
- opción 1: 97,5 %, pero el 59,5 % si la escolta llega con 4 bajas;
- opción 2: 98 % y 8,8 bajas.

El puesto se queda en (124; 75,5), donde ganó la -dia2-auto de la I-Noche141 con 0 bajas.

**Plan B (si falla la medida con 4 bajas en la escolta, que tiene que dar ≥ 90 %, o la -dia2-auto con el orden nuevo): mover el puesto a (118000; 80500), rumbo 0, Línea.** En NightSim dio 200/200. Comprobado con los obstáculos:
- Queda a 2,5 m de la fachada este, a 3 m al norte del Z 77,5 de la cocina de campaña (sin colisión) y a 4 m del muro norte (cara interior Z 84,5).
- Con 4 hombres ocupa Z 78,3–82,7. Con 8 llegaría a Z 73,9–87,1 y chocaría con el muro, pero con la D-N195 el puesto lleva 4.
- Ve la esquina SE (a 6 m) y el andén hacia la puerta este sin nada en medio.
- Se llega por el mismo camino que al puesto de (124; 75,5).

**Puesto definitivo (Lucía, 10-nov 11:09, decisiones 27a1745): (118000; 80500), rumbo 0 (este), Línea, cota 0, con 4 hombres (D-N195).** Comprobado:
- **Línea de visión:** 130 líneas, de 5 posiciones de la fila (Z 78,3–82,7) a la fachada este, a la esquina SE, a los tres puntos de la I-Noche139 y a 21 puntos del andén entre X 120 y 156 (Z 65,5–71). Se miden contra la caja del edificio (96,5–115,5 × 75,0–83,8) y el tren (Z 64,5, X 81–145), y no se tapa ninguna. La fila está a 2,5 m al este de la fachada, así que la ve entera de canto y en diagonal.
- **A pie:** de la banqueta oeste se va por el andén 1 (franja Z 66,1–75,0 entre el tren y la fachada sur), se dobla la esquina SE y se sube por la franja X 115,5–156 hasta Z 80,5. No hay obstáculos con colisión. Por detrás del edificio no se pasa: entre el edificio y el muro norte solo quedan 0,7 m, en Z 83,8–84,5.
- **Holguras:** 1,8 m al muro norte por el hombre de más al norte (Z 82,7; cara interior Z 84,5); la cocina de campaña (121; 78), sin colisión, queda a 3 m al este.
- **Ojo, Iker:** con 8 hombres la fila llegaría a Z 87,1, más allá del muro. Por eso el tope de 4 de la D-N195 hace falta también por sitio. Y si queda algo del código de la D-N192 que elige «el puesto de tierra más al norte» por Y, este puesto (Y 80,5) le ganaría a la banqueta: el orden lo tiene que dar la D-N195, no la Y.

**Plantel para 20 (D-N194 cerrada, Lucía 8a80d2a, 10-nov 11:22; Plantel v1.7).**

| Puesto | Pelotón | Hombres al empezar | X, Y (mm) | Rumbo | Cota |
|---|---|---|---|---|---|
| SUR | fusileros | 8 | 71500, 58500 | oeste | 0,4 |
| Azotea del ala oeste | ametralladores | 4 | 84500, 76300 | oeste | 4,75 |
| NORTE | fusileros:4 | 4 (la escolta lo completa hasta 8) | 71500, 68500 | oeste | 0,4 |
| ESTE (D-N194) | fusileros:4 | 4 (tope) | 118000, 80500 | este (0) | 0 |
| Banqueta, lo que sobra | lo que quede de la escolta | 0–4 | 71500, 81500 | oeste | 0,4 |

En total son 20. Así cuadra con las cifras de Nacho:
- Con la escolta entera (28), 4 completan NORTE y 4 van a la banqueta.
- Con 4 bajas (24), los 4 que llegan completan NORTE.

El sitio de «lo que sobra» sustituye al de ahora en el código, (106; 72,2) delante del edificio, que no es banqueta. Con 4 hombres ocupa Z 79,3–83,7 y no pisa a NORTE, que con 8 llega a Z 77,3. Con el tutorial, el pelotón del capítulo 3 sigue en (71500; 72000).
