# Kit de obra en curso, capítulo 2 del tutorial: reparar (Teo, 8-nov). Aprobado por Lucía (18:40).

`T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Banda de la horda: 0 % en las 50 piezas. Sin ámbar ni rojo (el aviso
de ruido es el icono de Bruno). Medidas DE MEMORIA (SIN VERIFICAR).

## SOLO VISUALES (condición de Lucía)
**Sin colisión, sin efecto en el pathing (A*, D-N139) y sin tapar la línea de visión (D-N174).** Las piezas de fuera
quedan entre la horda: si bloquearan, cambiarían el combate. No añadir colliders ni NavMeshObstacle, y excluirlas de los
rayos de visión.

## Uso
`SM_Obra<Pieza>_v<n>_<8|10>m_LOD0/1`. Se ponen sobre el tramo con su mismo origen y giro (suelo, centro del tramo, muro a
lo largo de X, fuera = −Y) mientras los zapadores reparan o reconstruyen, y se quitan al acabar. **8 m**: tramo de
sacos y puerta de vehículos. **10 m**: módulo de HESCO.

La obra va repartida por las dos caras: montones y pilas por fuera, herramientas por dentro, y en la puerta, el aspa de
tablones por fuera. Así se ve desde la cámara del RTS en cualquier lado del recinto.

| Pieza | Cuándo | Variantes v0–v4 |
|---|---|---|
| `Sacos` | Reparar un tramo de sacos | Hilada empezada encima del muro y pila · cadena de sacos · palé con sacos vacíos · montón de arena y sacos a medio llenar · dos pilas |
| `Herramientas` | Cualquier reparación (se puede poner con otra) | Carretilla llena y palas · carretilla volcada y pico · dos carretillas · palas en fila y cubo · carretilla y tablón de rodadura |
| `HescoAbierto` | Reparar un HESCO (la celda va en la línea del muro, en x 0) | Arena a 1/4 · 1/2 · 3/4 · con el geotextil colgando · dos celdas |
| `PuertaApuntalada` | Reparar una puerta (puntales por dentro, aspa por fuera) | 2 puntales · 3 · 4 · con travesaño · con sacos al pie |
| `Reconstruccion` | Reconstruir una brecha (hasta el 30 %) | Primera hilada a 1/3 · 2/3 · entera · con estacas y cordel · con palé de sacos |

La reconstrucción va sobre el modelo de brecha del tramo. Se puede avanzar con la obra: v0 al empezar, v1 a la mitad y
v2 al acabar.
