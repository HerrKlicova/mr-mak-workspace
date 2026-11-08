# Hordas «sin aire» (Hugo (3), 8-nov 16:20)

Para la build que lleve D-N173 (Sagunto sin NH90), D-N174 (línea de visión + azotea con pretil) y D-N175 (la horda va a la tropa a ≤25 m). **No es para Noche58**: Noche58 sigue con entregas/noche58/ (4710/5520/6400, con NH90).

| Dificultad | Horda | Permil | Victorias (NightSim, 1000 semillas, sin NH90, sin rescate de Nules) | Pila p50/p90 | Munición p10 |
|---|---|---|---|---|---|
| Fácil | 4480 | 853 | 100 % (pila >150 en el 100 % de las noches) | 257/283 | 42,4 u |
| Normal | 5250 | 1000 | 99,9 % | 343/371 | 41,7 u |
| Difícil | 5700 | 1086 | 79,6 % | 390/410 | 39,9 u |
| (Difícil alternativo) | 5800 | — | 64,4 % | 399/419 | 39,7 u |

- Base OLEADAS = [(0, 5250, 180)], reparto O1/O2/O3 = 50/30/20 (comprobado en noche_sagunto.json).
- fuerza: 5 pelotones, Dragón, helicopteros = [] (los 2 VAMTAC van por vehiculos_tierra.json).
- Difícil a 5700 (borde alto del 50-80 %), porque la build sale ~11 % más dura que NightSim en pila y debería caer hacia el 65-70 %.
- Control obligatorio antes de pasar a Eugenio: -inputtest y -nightbot **con esta horda**.
- Ojo: docs/economia/unidades/unidades.py ya tiene estos valores, pero csv/ y json/ siguen en Noche58 hasta que Marcos meta D-N173/174/175. Si alguien vuelve a correr unidades.py, se publican estos.

## Existencias en el JSON de la build (8-nov 18:55)
- **`existencias_red.json` (nuevo)**: la reserva de la red por estación (Sagunto 150/140/100/80 u y 80 personas; Nules 0; Bétera 50 u de munición y 70 u de combustible, que no se reponen; Castellón 300 u de combustible), los topes del almacén de zona (47/30/40 u) y las reglas de llenado: al empezar la partida y cada ataque, `min(tope, reserva)`, y lo que sobra vuelve a la reserva. Los `id` (`sagunto`, `nules`, `betera`, `castellon`) tienen que coincidir con los de RailNet; si no coinciden, me lo decís y los cambio en `unidades.py`.
- **`noche_sagunto.json`**: `recursos_iniciales` ahora se presenta como los TOPES del almacén de zona. Sin NH90 en Sagunto, `combustible.almacen_inicial_u` pasa de 16 a **22** (30 menos el depósito del Dragón). `fuerza` lleva una nota con los 2 VAMTAC.
- Los dos ficheros salen de `unidades.py` (no se editan a mano). Para integrarlos, copiadlos encima de los de `docs/economia/json/` cuando entren D-N173/174/175.
