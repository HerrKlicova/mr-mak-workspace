# Vía con traviesas para la vista de zona (muestra, 5 variantes). Bruno, 8-nov

**Problema.** En PrototypeBootstrap, las traviesas son unas 150 cajas por tramo con `_mSleeper = Mat("442c0c")`.
#442c0c es un color **reservado a la horda**: de noche, una traviesa se lee como un zombi tumbado. Además, son muchos objetos.

**Propuesta.** Sustituirlas por una sola textura que se repite (Point, sin mipmaps, wrap Repeat) sobre el quad del balasto.
La escala es 1 téxel = 0,15 m, la de 1 px del mundo a ortho 26. La textura mide 24 px de ancho (3,6 m) y los carriles van a 11 px.
El ancho ibérico está sin verificar para esta línea; lo confirmaría Paula.

| Var. | Qué es | L* balasto | ΔL* horda | ΔL* tren (#303424) |
|---|---|---|---|---|
| A | traviesa de hormigón cada 0,6 m | 27,8 | 16,4 | **6,9** (< 8) |
| B | hormigón cada 1,2 m | 27,8 | 16,4 | **6,9** (< 8) |
| C | madera en brown #543820 | 27,8 | 16,4 | **6,9** (< 8) |
| D | balasto claro (olive_grey + concrete_light) | 38,9 | 27,6 | 18,0 |
| E | banda tramada, sin traviesas sueltas | 27,8 | 16,4 | **6,9** (< 8) |

Con el balasto actual (#48403c), el tren no llega al ΔL* ≥ 8 de Sara. **Recomiendo la D.** Si hay ruido detrás de los zombis,
la alternativa es la D con el periodo de la B (8 px), que es un cambio de una línea en build_vias_zona.py.

**Uso en Unity (Marcos), cuando Lucía elija:**
- Material Unlit con `_BaseMap = Resources/Vias/T_via_X`, en el quad del balasto y con `mainTextureScale = (1, largo_m / (alto_px · 0,15))`.
- Quitar el bucle de cajas «Vía 2 traviesa» y los carriles «Carril» (ya vienen en la textura).

Generador: TBD `claude/sprites-importar`, `.claude/skills/pixel-art-codigo/ejemplos/build_vias_zona.py`.
Muestra: `muestra/muestra_vias_zona.png`, de día y de noche. La noche es una aproximación, no el render del juego.

## ELEGIDA: D (Lucía, 8-nov, 24:10). Plan B: la D con traviesas cada 1,2 m, si en la build hay ruido detrás de los zombis.
Código en TBD, rama `claude/vias-zona` (sobre marcos/noche-prototipo ae93063). Para Marcos:
1. Copiar `Assets/TBD/Resources/Vias/` de esta entrega (T_via_*.png con sus .meta y Vias.meta) al proyecto.
2. Fusionar `claude/vias-zona`. Pone el balasto de la zona en #605c48, la vía principal y la vía 2 pasan a ser un quad con la textura,
   y las traviesas de reserva van en hormigón #6c7874. El desvío en diagonal de la vía 2 sigue con sus carriles de caja.
3. `_mSleeper` (#442c0c) solo queda en el fantasma de obra (WallVisual). Habría que revisarlo con Lucía, porque también es color de la horda.
