# Huellas de vehículo calcinado · 5 variantes (Bruno, 7-nov) · aprobadas por Lucía

Sustituyen a `decal_calcinado_1_64.png` y `decal_calcinado_2_64.png` de la D-N87. Son el decal de suelo que va **debajo** de los restos 3D de Teo (VAMTAC, Dragón, NH90); el armazón lo pone su modelo.

| Archivo | Variante | Referencia |
|---|---|---|
| decal_calcinado_1_reciente_64.png | recién quemado, aro de alambre de neumático suelto | K8_1 |
| decal_calcinado_2_oxidado_64.png | restos viejos, escamas de óxido y hojas | K8_2 |
| decal_calcinado_3_ceniza_64.png | huella más larga, ceniza y cristales | K8_3 |
| decal_calcinado_4_piezas_64.png | puerta y parachoques caídos | K8_1 y K8_2 |
| decal_calcinado_5_cadenas_64.png | tramos de cadena sueltos (Pizarro) | K8_4 |

## Tamaños por vehículo (añadido 7-nov 08:15, con las medidas de Teo)
Los restos de Teo se salen de 6,4 m, así que hay un juego de 5 por vehículo con la **misma densidad de texel (0,1 m)**. No hace falta escalar el proyector: se pone a su tamaño real (lado en píxeles / 10 = metros).

| Vehículo | Lado | Archivos | Planta de los restos (Teo) |
|---|---|---|---|
| Genérico y Pizarro | 64 px = 6,4 m | decal_calcinado_1..5_*_64.png (las aprobadas) | — |
| VAMTAC | 85 px = 8,5 m | decal_calcinado_vamtac_1..5_*_85.png | 4,9 x 6,6 a 7,2 x 8,5 m |
| Dragón | 110 px = 11 m | decal_calcinado_dragon_1..5_*_110.png | 7,1 x 8,4 a 10,7 x 9,2 m |
| NH90 | 180 px = 18 m | decal_calcinado_nh90_1..5_*_180.png | 10,5-13,5 x 17,4 m |

En los tres tamaños grandes, la 5 es «dispersa» (dos aros de alambre y trozos de chapa) en lugar de «cadenas», porque esos vehículos no llevan cadenas. Las piezas (puerta, cable, chapa) mantienen su tamaño real; el hollín crece menos que la huella para seguir siendo una mancha pequeña en el centro (del 2,4 al 8,4 % de los píxeles). Si Teo quita sus placas de hollín, esta huella es la única mancha.

## Cómo se usan
- 64x64, texel 0,1 m (6,4 x 6,4 m), planta, el vehículo va a lo largo de X. Fondo transparente.
- **Variante por instancia con semilla determinista** (norma de las 5 variantes). Para el Pizarro usa preferentemente la 5; los demás, cualquiera de la 1 a la 4.
- Proyector a tamaño real (lado en px / 10 = m), centrado en los restos y girado con ellos (el vehículo va a lo largo de X).
- Importación: filtro Point, sin mipmaps, Clamp, sin compresión, sRGB activado. Los `.meta` llevan GUID nuevos.
- Cópialos con el Editor de Unity a la misma carpeta que las dos de la D-N87; no los muevas ni los renombres fuera del Editor. Las dos viejas se pueden retirar cuando estas estén puestas.

## Reglas comprobadas
- Base 48403c y 605c48; hollín 303424 solo al centro (del 2,7 al 9,2 % de los píxeles); L* mínimo 21.
- Sin 442c0c, sin rojo, sin ámbar y sin d4d0cc (es el color de la selección).
- Generador: `build_restos_calcinados.py` (TBD, rama claude/sprites-importar).
