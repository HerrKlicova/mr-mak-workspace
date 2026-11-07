# Decal de carga del vagón cisterna (Bruno, 7-nov) · aprobado por Lucía

Va sobre el panel liso del vagón cisterna de Teo (2,6 x 1,1 m, placa 605c48, a 1 cm de la cuba, en los dos costados; TBD 9c0885d, `bloques/vagon_cisterna.py`). Es para Castellón (`docs/niveles/castellon-nivel.md` §1). **Es para después del MVP**, cuando se monte Castellón.

- `decal_cisterna_carga_N_26x11.png`, con N de 0 a 4: **cuartos de carga encendidos** (Lucía). Se elige N según el stock: `N = round(4 * carga / capacidad)`. Para el depósito, cada cisterna representa unas 17 u, así que lo normal es 0 o 4, y las de 1 a 3 se ven en la cisterna que se está llenando o vaciando.
- `_52x22`: la misma pieza a x2 para la vista cercana del tren.
- Texel 0,1 m: el decal cubre el panel entero (26x11 px = 2,6 x 1,1 m). Point, sin mipmaps, Clamp, sin compresión y sRGB. Los .meta llevan GUID nuevos.
- Lectura: claro = carga y oscuro = vacío. Sin texto, sin d4d0cc y sin ámbar.
