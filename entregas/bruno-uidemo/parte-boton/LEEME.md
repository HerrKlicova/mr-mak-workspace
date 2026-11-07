# Botón principal del parte: opción C (Lucía, 7-nov 07:39)

Para Marcos. Lucía la aprobó y pidió que te llegue directamente.

**Problema:** el botón principal del parte («Seguir» o «Volver a empezar») usa `ui_boton_encima`, una placa olive 70784c. El texto en hueso solo da 3,1:1 sobre ella, y en la build no se lee (QA15 y QA20).

**Opción C:** el botón principal pasa a usar la placa de `ui_boton_normal` (50541c), con el texto en hueso, que da 5,2:1. Para que se distinga como principal lleva el borde en crema f0dc9c y la cuña crema a la izquierda. Es el mismo marcado que el estado «encima» del menú (retoque D de la D-N115).

## Piezas nuevas
Las dos van a `Assets/TBD/Resources/Icons/noche/`, con su `.meta`. Los `.meta` son una copia del de `ui_boton_normal` (Point, sin compresión) con un GUID nuevo.

- `ui_boton_principal.png` (48x16): `ui_boton_normal` con el borde exterior en crema. Su 9-slice es 4,4,4,4.
- `ui_boton_cuna.png` (4x7): la cuña. Va como pieza aparte para que el 9-slice no la estire.

No se cambia ninguna pieza existente. `ui_boton_encima` y `ui_boton_normal` siguen igual, y el panel de órdenes del HUD (línea 139) no se toca.

## Cambios en el código
`UiNocheKit.cs`, en el diccionario de slices, junto a `ui_boton_normal`:
```csharp
{ "ui_boton_principal", new RectOffset(4, 4, 4, 4) },
```
`UiNocheDemo.cs`, en el bucle de los botones del parte (línea 252):
```csharp
var rb = new Rect(bx + i * (bw + 8), by, bw, 18);
UiNocheKit.Slice(i == 0 ? "ui_boton_principal" : "ui_boton_normal", rb);
if (i == 0) UiNocheKit.Pieza("ui_boton_cuna", rb.x + 4, rb.y + rb.height / 2 - 3);
```
El texto sigue igual (hueso y centrado).

## Comprobación
- `muestra_parte_boton_C.png`: arriba la versión actual y abajo la C, con victoria y derrota.
- `parte_victoria_C_1080.png` y `parte_derrota_C_1080.png`: maquetas completas a 1080.
- Contraste: hueso sobre 50541c da 5,2:1. Crema sobre el panel 283440 da 9,3:1.
- No está comprobado en Unity. Si el fallo de espacio de color sigue sin arreglar (ver `../color/LEEME.md`), el texto saldrá más oscuro que en la maqueta. Aun así, sobre esta placa se lee mejor que sobre la olive.

Script: `build_parte_boton.py` (`python build_parte_boton.py <carpeta>`).
— Bruno (Arte técnico)
