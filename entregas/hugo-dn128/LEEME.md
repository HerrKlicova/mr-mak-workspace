# D-N128 · Munición de a bordo de los vehículos, para Marcos (Hugo, 7-nov, 09:30)

Lo deciden Mak y Eugenio: los vehículos no se pueden quedar sin munición en una sola oleada. Empiezan la noche en **fuego libre** y **G** pone el alto el fuego (sustituye a la regla de disparar solo con orden).

## Qué cambia en la build
| Vehículo | Antes en la build | Ahora (munición de a bordo) | En disparos de la build (escalado ×) | Dura en fuego libre |
|---|---|---|---|---|
| Dragón | 120 salvas de 3 (~360 abatidos) | **2 u** | **~400 salvas** (×3,3) | ~3–4 oleadas |
| VAMTAC | 300 disparos | **3 u** | **~750 disparos** (×2,5) | ~3 oleadas |
| NH90 | 400 disparos | **3 u** | **~930 disparos** (×2,3) | ~3 oleadas |

- **La munición de a bordo sale del almacén al empezar la noche**: Sagunto pasa de **52 a 47 u** (`recursos_iniciales.municion_u` de `noche_sagunto.json`). La munición total de la noche no cambia: 47 + 7,3 de los pelotones + 8 de los vehículos ≈ 62,3 u, como antes.
- **La recarga no cambia**: sale del almacén al bajar del 30 %, rellena hasta la dotación (unas 2,1 u el VAMTAC y el NH90, y 1,4 u el Dragón, por recarga desde el 30 %), tarda 20 s junto al tren y 30 s en el helipuerto.
- **Columna «en disparos de la build»**: es la carga de la build escalada para que dure unos 300 s de fuego continuo. La cadencia de `hud_municion.csv` (fuego_continuo_s) es la de mi modelo y no la de la build. Para la build mandan los disparos de esta tabla, y el coste en u sale del JSON.
- **Ficheros** (regenerados con `unidades.py`): `noche_sagunto.json`, `vehiculos_tierra.json`, `balance_noche.csv`, `balance_unidades.csv` y `hud_municion.csv`, que ahora tiene una fila nueva para el VAMTAC.

## Difícil a 1280 (D-N127)
Ya está en el JSON. **Solo entra en la build cuando la normal se pueda ganar** (qa23 o Noche23). Nacho tiene la rama `nacho/dificil-1280` (8c64498), comprobada con cmp.

## Qué se mide después
Las 4 corridas con `-nightbot -vehfuego`: normal 850 y difícil 1280, con y sin recarga. Sara las mide contra ★★★ (normal) y contra el techo del 35 % (difícil).
