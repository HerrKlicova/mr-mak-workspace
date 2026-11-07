# D-N128 para la build, con la difícil en 1140 (Hugo, 7-nov, 09:40)

Lo decide Mak: entra **solo la munición de los vehículos (D-N128)**. La difícil se queda en **1140** hasta que esté la recalibración con vehículos de Sara (la 1280 de la D-N127 se midió sin vehículos y no vale).

- **Sustituye a** `entregas/dn128/` (mr-mak-workspace 4ba5b27), que llevaba la difícil a 1280.
- **Diferencias con la build actual (D-N127 fuera)**: solo `municion_u` 52 → 47, el NH90 a 3000, la fila nueva del VAMTAC (3000) en el HUD y la nota de `balance_noche.csv`. Las oleadas de las tres dificultades no cambian.
- **Ficheros**: `noche_sagunto.json` y `balance_noche.csv`, generados aparte con la difícil en 1140. `vehiculos_tierra.json`, `balance_unidades.csv`, `hud_municion.csv` y `nightsim_params.json` son los mismos que los de `docs/economia` (la dificultad no los toca).
- **Para Marcos** (en disparos de la build): Dragón ~400 salvas, VAMTAC ~750 disparos, NH90 ~930 disparos. Fuego libre al empezar y G para el alto el fuego. La recarga, como antes. Detalle en `entregas/dn128/LEEME.md`.
- **docs/economia** sigue con la D-N127 (1280) como fuente de diseño. Cuando llegue la difícil nueva, la regenero y la paso.
