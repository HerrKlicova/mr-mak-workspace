# Sagunto · obstáculos para la línea de visión (D-N174), v1

Álvaro (3), 8-nov, ~13:15. Encargo de Mak para Nacho (NightSim) y Marcos. Todo está sacado del código de `marcos/noche-prototipo` (8181db0) y de sus datos. Donde no hay dato, lo pone.

**Dato**: [`sagunto_obstaculos_v1.csv`](sagunto_obstaculos_v1.csv). Tiene 50 filas, separadas por `;`, con coordenadas en mm (X al este, Z al norte, que es la «Y» de NightSim). Las columnas son: id, tipo, forma (`seg` = segmento con medio grosor; `caja` = rectángulo alineado), x0, z0, x1, z1, medio grosor, altura, si tapa la vista, si tapa el paso, fuente (archivo:línea) y nota.
- **Filas con sólido en el código (40)**: los muros, las puertas cerradas, los nidos, el tren de noche, el edificio de viajeros, los dos almacenes, las 21 casas y el bloque de pisos. Es lo mismo que ya ve el A*.
- **Filas «SIN SÓLIDO» (10)**: el paso superior con sus terraplenes (4 filas), las tolvas, el autobús, el camión, el atasco, la barricada y el cauce del Palancia. Se ven en la escena, pero hoy no existen para la simulación. Propongo cuáles deberían tapar la vista (columna `tapa_vision`) aunque no tapen el paso.
- `BuildWall` hace muros de **1 m de grosor** (medio grosor de 0,5 m, `Sim/SimSystems.cs:140`), así que la cara interior del muro oeste está en X 70,5.

## 1. Alturas de disparo que propongo (no las da el código; las decide Nacho)
| Quién | Altura de la boca del arma | Por qué |
|---|---|---|
| Fusilero, ametrallador o granadero, de pie | **1,6 m** | Arma al hombro |
| Fusilero en la banqueta (a 2 m o menos de la cara de su muro) | Dispara por encima, como dice la D-N174 | — |
| Nido (pieza de 1,5 m) | 1,6 m | El tirador está detrás de los sacos |
| Dragón, torre de 30 mm | **≈ 2,9 m**, SIN VERIFICAR | El casco mide 2,34 m (ficha de Paula, V1) y la altura con torre no está verificada |
| VAMTAC, aro con ametralladora | ≈ 2,4 m, SIN VERIFICAR | — |
| NH90 en vuelo | 30 m | Lo que da el HUD |
| **Blanco (zombi)** | **Se apunta a 1,0 m**, el centro del cuerpo | Un zombi mide unos 1,7 m |

Regla geométrica (2,5D): un obstáculo de altura h, a una distancia s del tirador sobre un rayo de longitud L, tapa si h > h_blanco + (h_boca − h_blanco) × (L − s) / L.

## 2. Dónde cambia mucho la defensa
1. **La franja al pie del muro oeste es zona muerta para todo el que no esté en la banqueta.** El HESCO mide 2,1 m, más que la boca de un fusil (1,6 m). Desde dentro, a más de 2 m del muro, ningún infante ve nada al otro lado, ni cerca ni lejos. Justo ahí se forma la pila (X 54–68). Contra la pila solo quedan:
   - quien esté en la banqueta;
   - el Dragón, pero solo a los blancos que estén fuera a más de 1,4 veces su distancia al muro. Desde el parque (99; 53), a 28 m de la cara del muro, solo ve lo que queda a más de unos 39 m fuera, o sea, no ve la pila;
   - el NH90.
   **La regla traslada la defensa de la pila a la banqueta y al NH90.** Hay que medir cuánta tropa cabe en la banqueta del oeste (41 m de muro, quitando la puerta).
2. **Los dos nidos de la puerta de vía se quedan sin tiro hacia fuera.** Están en X 73,5, a 3 m de la cara interior del muro, que es más de los 2 m de la regla. Detrás de 2,1 m de HESCO, un tirador a 1,6 m no ve la horda. **Propongo moverlos a X 72,0**, a 1,5 m de la cara (`NetWorld.cs:1439`, de −X + 3.500 a −X + 2.000). Si no, los dos nidos solo sirven contra los que trepan.
3. **Los sacos (1,2 m) apenas tapan.** Un infante de pie a d metros de un muro de sacos ve a los zombis que están fuera a más de d/2 (con 1,6 / 1,0 / 1,2 m). El norte, el este y casi todo el sur son de sacos, así que la regla casi no cambia nada en esos lados. Si Lucía quiere que esos muros también protejan, la palanca es la altura de los sacos; no lo recomiendo, porque la presión está en el oeste.
4. **El tren de noche (2,2 m, X 81–145) parte el recinto en dos.** Lo que pase al sur del tren no se ve desde el norte, y al revés. **La zona de muerte para los que trepan es X 70,5–81, entre el muro y la cola del tren**, que se ve desde los dos lados. Encaja con la D-N168: la tropa de dentro junto a la cola del tren.
5. **El edificio de viajeros (11 m) tapa el noreste del recinto desde el noroeste**, y el almacén del muelle (5 m) hace lo mismo con el sureste. Dentro no importa mucho, porque los que trepan entran por el oeste.
6. **Las puertas cerradas (2,5 m)** tapan como el HESCO. La puerta de vía en Z 62,9–66,1, que pasa a Z 62–67 en el Bloque 2, crea una zona muerta en el centro de la franja.
7. **Fuera: el almacén de naranjas (X 40–51, Z 30–51) tapa la llegada de O2** por el lado del muro sur. Su sólido mide 4 m y el modelo, 7,5 m de cumbrera. **Para la vista, usad 7,5 m**, que es lo que el jugador ve. Las **casas** (6 m) tapan el pueblo, por donde llega O3, desde el muro norte. El **bloque de pisos** (14,5 m) tapa el noreste.
8. **Lo que se ve y no tapa** (incoherencias para el jugador):
   - Los **terraplenes del paso superior** (hasta 8,3 m) no tienen sólido. Tienen que tapar la vista, pero no el paso por debajo del tablero (Z 47,6–81,4, que queda a 7,8 m).
   - Las **tolvas volcadas** (≈ 3 m) y el **autobús** (3 m) deberían tapar.
   - Los **coches del atasco** (1,5 m) y la **barricada** (1,4 m) pueden quedarse sin tapar, porque quedan por debajo de un fusil de pie.
   - El **cauce del Palancia** (−4,5 m) solo importa con O4, que va después del MVP.
9. **Puestos elevados: hoy no hay ninguno.** Si Lucía quiere un contrapeso a la zona muerta del punto 1, el sitio natural es la **azotea del edificio de viajeros** (11 m, a 26 m del muro oeste): desde ahí se ve la pila por encima del HESCO. Es una decisión de diseño, y solo la propongo.

## 3. Para Nacho y Marcos
- El CSV se puede cargar tal cual en la capa de alturas sobre la rejilla de 1 m (`NavGrid`, D-N174). Las cajas de altura negativa son relieve, por debajo del suelo.
- **Datos que cambian con el Bloque 2**: el hueco de la puerta de vía pasa a Z 62,0–67,0, y llega la puerta de vía de Teo (2,1 m visibles y 2,5 m de sólido) con el tramo HESCO del tutorial en (70; 72,9) (§10.9 de sagunto-nivel.md). Las Z de la puerta este están SIN VERIFICAR: supongo el mismo hueco que en el oeste.
- **Lo que no he podido medir**: la altura real de las tolvas y del autobús, la altura de la torre del Dragón y la del aro del VAMTAC.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
