# Huellas de vehículo calcinado · 5 variantes (Bruno, 7-nov) · aprobadas por Lucía

Sustituyen a `decal_calcinado_1_64.png` y `decal_calcinado_2_64.png` de la D-N87. Son el decal de suelo que va **debajo** de los restos 3D de Teo (VAMTAC, Dragón, NH90); el armazón lo pone su modelo.

| Archivo | Variante | Referencia |
|---|---|---|
| decal_calcinado_1_reciente_64.png | recién quemado, aro de alambre de neumático suelto | K8_1 |
| decal_calcinado_2_oxidado_64.png | restos viejos, escamas de óxido y hojas | K8_2 |
| decal_calcinado_3_ceniza_64.png | huella más larga, ceniza y cristales | K8_3 |
| decal_calcinado_4_piezas_64.png | puerta y parachoques caídos | K8_1 y K8_2 |
| decal_calcinado_5_cadenas_64.png | tramos de cadena sueltos (Pizarro) | K8_4 |

## Cómo se usan
- 64x64, texel 0,1 m (6,4 x 6,4 m), planta, el vehículo va a lo largo de X. Fondo transparente.
- **Variante por instancia con semilla determinista** (norma de las 5 variantes). Para el Pizarro usa preferentemente la 5; los demás, cualquiera de la 1 a la 4.
- **Escala el proyector de decal a la planta de cada vehículo** (unas 1,4 veces su largo y su ancho; el factor está sin verificar en Unity).
- Importación: filtro Point, sin mipmaps, Clamp, sin compresión, sRGB activado. Los `.meta` llevan GUID nuevos.
- Cópialos con el Editor de Unity a la misma carpeta que las dos de la D-N87; no los muevas ni los renombres fuera del Editor. Las dos viejas se pueden retirar cuando estas estén puestas.

## Reglas comprobadas
- Base 48403c y 605c48; hollín 303424 solo al centro (del 2,7 al 9,2 % de los píxeles); L* mínimo 21.
- Sin 442c0c, sin rojo, sin ámbar y sin d4d0cc (es el color de la selección).
- Generador: `build_restos_calcinados.py` (TBD, rama claude/sprites-importar).
