# Noche: control y 5 variantes sobre qa24 (Bruno, 7-nov ~09:20 UTC)

Están simuladas con las pasadas de luna y de ambiente de qa24 (22:18). El proceso:
- Primero deshago la codificación sRGB de más.
- Después combino la luz en lineal.
- Los focos y las trazadoras salen de la captura «actual», restándole la luna y el ambiente.
- El HUD lleva su valor correcto.
- Ninguna variante usa tramado. Con mezcla 0,2, la distancia se mide en sRGB; en el control se mide en lineal, como en el shader de origin.

| | luna (color × intensidad) | ambiente | filtro | sat. | mezcla | suelo L* (n.º de valores) | suelo b* | croma de la sombra | croma p90 |
|---|---|---|---|---|---|---|---|---|---|
| control | .42/.48/.62 × .45 | .012/.016/.026 | blanco, exp +0,35 | −15 | 0,65 | 31,0 (4) | +4,6 (sepia) | 7,5 a 111° (oliva) | 17,9 |
| v1 | .45/.58/1,0 × .35 | .04/.05/.10 | .80/.88/1 | −20 | 0 | 24,4 (5) | −1,9 | 5,4 | 8,1 |
| v2 | igual que v1 | | | | 0,2 | 24,6 (5) | −1,4 | 7,0 | 8,1 |
| **v3** | **.40/.55/1,0 × .45** | **.03/.045/.10** | **.78/.86/1** | **−10** | **0** | 26,4 (5) | **−3,6** | 6,5 a −75° | **10,4** |
| v4 | .55/.62/.85 × .30 | .05/.055/.08 | .75/.85/1 | −40 | 0 | 23,1 (6) | +1,0 | 2,4 | 5,3 |
| v5 | .45/.58/1,0 × .55 | .04/.05/.10 | .80/.88/1 | −15 | 0,2 | 31,7 (6) | +0,3 | 5,2 | 10,0 |

Recomendada: **v3**.
- Es la única en la que el suelo sale frío de verdad.
- Es la que más color propio conserva: la teja, el oliva y la fachada se reconocen.
- El foco es el único sitio cálido.
- Las sombras son de un gris azulado poco saturado.

Lo que no se ha medido:
- La banda de la horda: a las 22:18 no hay zombis en el encuadre.
- El modelo de luz no cuadra del todo con la captura «actual», que sale un 40 % más oscura que la suma de las pasadas.

Hasta verlo en la build, todo esto está SIN VERIFICAR.
