# D-N157 · Sagunto de día con la horda atacando el muro (Bruno, 9-nov). MUESTRA

Render por código (build_dia_horda.py, TBD claude/sprites-importar), sin Unity. Cámara del juego: ortho, 55°, 1 px = 0,144 m.
Las 5 siluetas de Teo (OBJ de teo-horda-obj) con los tonos del LUT de la horda. La máscara va por altura (aproximada: los OBJ no la traen).
Exposición automática por variante: el suelo apisonado al sol queda en L* 64.
`hoja_dia_horda.png` tiene las 5 con sus medidas; `hoja_dia_horda_muro_claro.png` es lo mismo con la cara del muro en #94948c.
Los albedos del muro y del tren están SIN VERIFICAR contra la build.

## Banda de día de la horda (propuesta)
- **El shader no cambia**: el mismo LUT (albedo L* 9–13). De día, en pantalla, da **L* final de 3 a 16 (p5–p95), con la mediana entre 6 y 11**.
  Esa es la banda de día. El albedo es tan oscuro que el sol no lo saca de ahí.
- Regla de acompañamiento: todo el decorado en pantalla (mediana de cada superficie) **≥ 24**, es decir, p95 de la horda + 8.
  El hueso d4d0cc (L* 83) queda a más de 65 de distancia.
- Lo que la rompe: la **niebla o bruma aditiva** (calima como niebla). En la primera pasada subía la horda a L* 40 y la juntaba con el tren y la vía.
  El polvo tiene que ir en el color de la luz, nunca en niebla.

## Resultado por muestra (ΔL* ≥ 8)
| | horda p5–p95 | horda→suelo/muro/vía/tren lateral/soldado | tren lateral↔vía | vía↔muro | muro↔suelo |
|---|---|---|---|---|---|
| A Mediodía | 1,2–11,7 | 52 / 24 / 25 / 12 / 23 ✓ | 13,5 ✓ | **1,8 ✗** | 28,8 ✓ |
| B Mañana rasante | 2,9–14,8 | 49 / 16 / 11 / **5,4 ✗** / 16 | **5,5 ✗** | **5,3 ✗** | 33 ✓ |
| C Nublado | 5,5–12,1 | 52 / 31 / 25 / 17 / 30 ✓ | **7,9 ✗** | **5,6 ✗** | 21 ✓ |
| D Tarde dorada | 3,6–15,6 | 48 / 19 / 14 / **7,4 ✗** / 19 | **6,1 ✗** | **5,3 ✗** | 30 ✓ |
| E Calima sin niebla | 4,0–13,0 | 51 / 32 / 24 / 18 / 32 ✓ | **5,6 ✗** | 8,2 ✓ | 18,8 ✓ |

Muro claro (#94948c): la distancia vía↔muro pasa a A 7,5, B 13,8, C 16,2, D 14,6 y E 19,4, pero muro↔suelo en E baja a 7,6.

## Recomendación: E, calima sin niebla
Sol a 45° velado, cielo beige y ambiente fuerte. La horda es la que más separación tiene con todo (≥ 18), las sombras son cortas y no forman manchas
oscuras que se confundan con la masa (eso pasa en B y D), y el tono cálido es el de la huerta en septiembre.
Falla en un punto: el lateral oliva del tren (#50541c) contra el balasto (5,6). Falla en 4 de las 5 luces, así que es un problema del albedo y no de la luz.
Propongo aceptarlo, porque a 55° el techo claro (L* 71) es la mayor parte del tren que se ve y es lo que lo lee (techo↔vía ≈ 34).
Si no se acepta, se aclara el lateral un escalón (#70784c): eso lo decide Lucía con Teo.
B y D, la luz rasante, quedan descartadas para el ataque: el lateral del tren cae en sombra y se junta con la horda.

## Nueva medida con el lateral del tren de Teo (9-nov, 01:45; mr-mak d54dd0f)
Lucía no hace excepción (registro 25:05) y Teo sube el lateral de #50541c a #70784c. He vuelto a medir las 5 luces y he añadido la noche de referencia (N: luna 0,45 y suelo en L* 25).
La noche es un modelo mío, SIN VERIFICAR contra la build. Medianas de tren lateral − vía D:

| | A | B | C | D | **E** | N (noche) |
|---|---|---|---|---|---|---|
| #50541c (antes) | −13,5 | −5,5 | −7,9 | −6,1 | **−5,6** | −3,1 |
| #70784c (Teo) | −2,1 | 5,0 | 5,1 | 5,1 | **7,9** | 4,0 |
| #88885c (un escalón más) | 3,4 | 10,0 | 11,3 | 10,5 | **14,5** | 7,3 |

- Con #70784c, la E se queda en **7,9**, a una décima del 8. El render es aproximado, así que no lo doy por bueno.
- Con #88885c, la E da **14,5**, que deja margen. De noche se queda en 7,3: de noche todo se comprime (el suelo está en 25) y ningún albedo del tren llega a 8 en mi modelo.
- La horda frente al tren pasa siempre de largo: E ≥ 31 y noche ≥ 12.
- Hojas: `hoja_dia_horda_tren70784c.png` (las 5 + N) y `hoja_dia_horda_tren88885c.png`.

## Segunda pasada de Teo (mr-mak 5018dd0): lateral #88885c, techos ≤ #b8b8b8. Medido en la E (y la N de referencia)
| par | E | N (noche, sin verificar) |
|---|---|---|
| tren lateral ↔ vía D | 14,5 ✓ | 7,3 (lo mide Sara en la build) |
| techo ↔ lateral | 19,8 ✓ | 10,7 ✓ |
| tren lateral ↔ suelo | 12,5 ✓ | 6,5 |
| tren lateral ↔ muro (cara) | **6,3 ✗** | 2,9 |
| techo ↔ muro | 26 ✓ | 13,6 ✓ |
| horda (p95) → lateral | 38,5 ✓ | 16,2 ✓ |
El único par por debajo de 8 en la E es el lateral contra la cara del muro. El techo, que es lo que más se ve del tren a 55°, se separa del muro por 26.

**CERRADO (Lucía, 9-nov):** se acepta lateral↔muro 6,3, porque la regla de Sara es para pares que se tocan y se pueden confundir; el techo (26) recorta el tren en las puertas de vía. El muro no cambia. Si en la build el tren se pierde en las puertas, se reabre. Falta la noche, que mide Sara en la build.

## Carga visible sobre el vagón (Teo, mr-mak 84e1194), medida en pantalla en la E (cajas sobre el vagón del centro)
| carga | carga ↔ lateral #88885c | techo ↔ carga | noche: carga ↔ lateral |
|---|---|---|---|
| #847c34 (Teo) | **3,1 ✗** | 22,9 ✓ | 1,7 |
| #845c28 | **11,4 ✓** | 31,2 ✓ | 6,3 |
En pantalla, #847c34 se junta con el lateral; el croma no lo salva en una cámara pixelada a 1/3. Recomiendo #845c28 (dia_E_carga845c28.png).
