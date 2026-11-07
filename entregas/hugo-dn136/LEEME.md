# D-N136 · Una sola gran horda al entrar (Hugo, 7-nov, 13:50)

Decisión de Lucía (D-N136, prueba de Eugenio en la Noche46): **sin oleadas**; una sola horda al entrar en la noche, que llega en 60–90 s; la noche se gana al acabar con ella. **Sustituye a `dn135`** solo en las oleadas: las recargas ×0,6, la munición a bordo y todo lo demás siguen igual.

## Números
| Dificultad | Escala | Horda total | O1 | O2 | O3 | O4 |
|---|---|---|---|---|---|---|
| Fácil | 725 | 3410 | 1023 | 1023 | 682 | 682 |
| Normal | 850 | **4000** | 1200 | 1200 | 800 | 800 |
| Difícil | 1140 | **5360** | 1608 | 1608 | 1072 | 1072 |

- Base 4700 a escala 1000; aparece a las 22:00 (minuto 0) y **llega en 75 s reales** (centro de 60–90).
- Reparto 30/30/20/20 por las cuatro entradas del oeste.
- En el JSON: `oleadas.<dificultad>` es una lista de UN elemento. El código que cuente oleadas debe aceptar 1.

## Método (solo cálculo, sin partidas)
Del barrido A–D de Sara (e6ccaef, 1000 semillas) ajusté el daño al muro de la última oleada frente a su tamaño: daño ≈ 0,021 × (H − 1790)² zombi·s (B 4250 → 126k, C 5100 → 228k, D 5950 → 360k).
- Normal 4000 → ~102k zombi·s, muro esperado ~91 %. Munición ~17 u de 62 → ★★★ probable. Primer contacto fácil.
- Difícil 5360 → ~265–290k, muro esperado ~76 %. Tensa pero ganable.

## SIN MEDIR (riesgos)
1. **Pila que trepa**: con todo a la vez, el pico de la pila al pie del muro es ≈ H − 42/s × 75 s ≈ 850 (normal) y 2200 (difícil), por encima de ClimbPileZ 150 → habrá trepadores. El ajuste anterior venía de oleadas escalonadas; esto puede empeorar el muro en difícil.
2. **Ataque al tren**: NightSim no lo modela bien (QA-35 lo deja esperando en X 90–154).
3. Pide una corrida de NightSim (normal y difícil) antes de cerrar la difícil; el criterio de mañana sigue siendo normal ≥95 % con muro p50 ≤90 %, difícil 50–80 %.

## Archivos
noche_sagunto.json, balance_noche.csv, balance_unidades.csv, hud_municion.csv, nightsim_params.json, vehiculos_tierra.json (regenerados con unidades.py; rc 0).
