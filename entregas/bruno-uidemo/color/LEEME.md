# Referencia de color para comprobar el arreglo (HUD, parte y menú)

Bruno (Arte técnico), 07-11 ~08:10. Para Marcos. Viene del punto 1 de `../qa/diferencias_qa13-20.md`.

## Qué hay
- `ahora_vs_objetivo.png`: la QA15 al lado de cómo debe verse, en la partida y en el menú.
- `objetivo_hud_1080.png`, `objetivo_parte_1080.png` y `objetivo_menu_retoqueD_1080.png`: los colores exactos que tiene que dar la build. La letra cambia, porque aquí es la de las maquetas, pero los colores y las piezas deben coincidir al píxel.
- `comprobar_color.py`: mide una captura y dice OK o MAL en cada punto.

## Cómo comprobarlo
1. Lanza la prueba de interfaz (-uidemo), que usa los mismos datos falsos que las maquetas, y captura las vistas 1 (HUD), 3 (parte de victoria) y 2 (menú).
2. Ejecuta `python comprobar_color.py captura.png hud`, luego `parte` y luego `menu`. Funciona con cualquier tamaño 16:9.
3. Tiene que salir **TODO BIEN** en las tres. Sobre las maquetas ya sale TODO BIEN; sobre la QA20 y la QA15 sale MAL.
4. Haz la prueba **en la escena de partida y en el menú**: el fallo es distinto en cada una.

## Los valores que deben salir (hex exacto, ±3)
| Qué | Debe dar | Daba la QA15/QA20 |
|---|---|---|
| Fondo de placas y paneles (ui_panel, reloj, frentes, parte y órdenes) | `181c30` | `565d78` en la partida |
| Texto Hueso | `d4d0cc` | `a7a099` en el menú |
| Texto Crema (títulos, valor de la resolución) | `f0dc9c` | `deb654` en el menú |
| Texto Beige (etiquetas del parte, números de los deslizadores) | `b4a080` | `745937` en el menú |
| Menú, retoque D: placa del botón normal | `283440` | `181c30` (aún sin el retoque) |
| Menú, retoque D: texto inactivo (concrete) | `6c7874` | (el antiguo 605c48 salía casi navy) |
| Botón de encima (Seguir, Volver a empezar): placa | `70784c` | `b1b694` |

## Una nota de diseño, no un fallo de la build
Incluso con el color bien, «Seguir» y «Volver a empezar» (texto Hueso sobre `ui_boton_encima`, `70784c`) dan **3,1:1**. Con Crema daría 3,4:1. Si Lucía quiere más contraste, se puede usar `ui_boton_normal` (`50541c`), que da 5,2:1 con Hueso. Se lo paso a ella; tú no cambies nada por esto.
