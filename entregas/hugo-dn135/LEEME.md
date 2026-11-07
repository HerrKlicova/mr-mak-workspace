# D-N135 · Noche de primer contacto: 4 oleadas y recargas ×0,6 (Hugo, 7-nov, 11:50)

Encargo de Eugenio: «que se puedan ganar las hordas. Reducid de 6 a 4. Es un primer contacto, no tiene que ser difícil». Número de Lucía. **Sustituye a `dn128-build`** (y por tanto a mr-mak-workspace 5521db8).

## Qué cambia
| Qué | Antes | Ahora |
|---|---|---|
| Oleadas | 6: 22:20, 23:20, 00:40, 02:00, 03:20 y 04:40 | **4: 22:20 (900), 00:10 (1500), 02:10 (2000) y 04:10 (3000)**, a escala 1000; la grande queda como clímax antes del amanecer |
| Zombis de la noche (×1000) | 16.000 | **7.400** (−54 %). Normal 850: 6.290 · difícil 1140: 8.436 |
| Recarga de vehículos (coste de una recarga completa) | 2000/3000/3000 ‰ u | **1200/1800/1800** (Dragón/VAMTAC/NH90), en `nightsim_params.json` NightVehicles.ResupplyMilliU y en `recarga_u_mil` del HUD |
| Escalas | normal 850 · difícil 1140 | sin cambios (la D-N127 y la D-N132 quedan en suspenso) |
| Munición | Sagunto 47 u y a bordo 2/3/3 u (D-N128) | sin cambios |

## Para Marcos y Nacho
- **El número de oleadas sale del JSON** (`oleadas`, 4 entradas por dificultad; `noche_oleadas` = 4 en el CSV). Si algún código da por hecho que son 6 (bucles, carteles «O5»/«O6», el parte, el HUD), hay que adaptarlo. Por favor, revisadlo.
- La recarga de los vehículos en la zona tiene que leer ResupplyMilliU (cobrando la parte que se rellena).

## Criterio de primer contacto (Lucía, D-N135), lo mide Sara con 1000 semillas
- **Normal**: se gana en ≥ 95 % de las noches, con el muro tocado (mediana ≤ 85 %).
- **Difícil**: se gana entre el 50 y el 80 % de las noches. Si sale peor, Hugo baja la escala sin pedir otro número.
