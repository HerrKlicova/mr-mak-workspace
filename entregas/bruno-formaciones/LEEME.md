# Iconos de formación y silueta fantasma (Bruno, 7-nov) · aprobados por Lucía

Para el §3 de `docs/encargo-control-disparos-noche.md` (Lucía, en mr-mak 1378d4b).

## Iconos de formación (frente arriba, hueso sin marco: el marco lo pone el botón)
| Formación | Tecla | 32 (botón) | 16 (botón pequeño) | 12 (esquina de la tarjeta del pelotón) |
|---|---|---|---|---|
| Línea | F1 | ui_formacion_linea_32.png | _16 | _12 |
| Bloque | F2 | ui_formacion_bloque_32.png | _16 | _12 |
| Columna | F3 | ui_formacion_columna_32.png | _16 | _12 |
| Dispersa | F4 | ui_formacion_dispersa_32.png | _16 | _12 |
- El de 12 va en la esquina inferior derecha de la tarjeta de 48, en (34,34), sobre una placa 181c30 de 14x14 en (33,33). Lo enseña muestra_formaciones_fantasma_x4.png.
- Se pintan siempre a escala entera (x1 o x2, la misma que el resto del HUD), nunca a x1,5, y con filtro Point.

## Silueta fantasma (a resolución de pantalla, mientras se arrastra el frente)
- `ui_fantasma_punto_2.png`: 2x2, d4d0cc al 50 % (el alfa ya viene en el PNG). Uno por soldado, en su hueco.
- `ui_fantasma_flecha_7x5.png`: d4d0cc al 50 %, mira a +X. Una por pelotón, delante del centro de la línea, girada hacia donde mirará.
- `ui_fantasma_no_valido_3.png`: aspa 3x3 en hueso b4a080 al 100 %, en lugar del punto cuando el hueco cae dentro de un muro o fuera del recinto.

Importación: Point, sin mipmaps, Clamp, sin compresión, sRGB y alpha is transparency. Los .meta llevan GUID nuevos. Cópialos con el Editor; no los muevas ni renombres fuera de él.
