# D-N160 · Símbolos APP-6 en pixel art para el mapa del informe de inteligencia (Bruno, 8-nov). MUESTRA

Formas de APP-6 y colores de nuestra paleta, según el encargo de Lucía y la referencia de Paula (§b):
- **Amigo**: rectángulo 3:2 en tierra y cúpula en el aire. Iconos: infantería X, mecanizado X+óvalo, acorazado óvalo, helicóptero con rotor en pajarita.
  Tamaño de unidad encima: ● pelotón, ●●● sección, I compañía.
- **Hostil**: rombo en **hueso d4d0cc**. **Rojo 982420 solo mientras ataca**, con un contorno de 2 px porque el rojo tiene poco valor sobre la banda alta (ΔL* −4,8 frente a 605c48).
- **Desconocido**: trébol en **neutro 94948c**, nunca amarillo.
- **Horda**: rombo **vacío**, sin icono de infantería.
- Tamaños: 16 px de alto (mapa a ×1) y 24 px (informe ampliado). Contorno de 1 px y marco relleno, salvo la horda.

## Azul amigo: 5 variantes (`muestra/muestra_app6.png`, sobre las 3 bandas del plano táctico y el mar)
| Var. | Relleno / contorno | ΔL* del contorno con las bandas (meseta, media, alta, mar) |
|---|---|---|
| A | slate / hueso | 62,8 · 55,9 · 44,8 · 72,9. **Descartada**: el hueso es el color de lo hostil |
| B | slate_dark / slate | 8,7 · 1,8 · −9,3 · 18,7. No se lee |
| C | navy / slate | igual que B. No se lee |
| **D** | **slate / grey_light** | 53,9 · 47,0 · 35,9 · 63,9. **Recomendada** |
| E | slate_dark / grey_light | igual que D, con el relleno más oscuro (L* 21) |

La paleta no tiene un azul vivo. El único azul medio es slate #404460, que está reservado al rim de NUESTRAS unidades.
En el mapa significa lo mismo (lo propio), así que lo uso como relleno de lo amigo.

Los PNG de `Assets/TBD/Resources/Icons/app6/` son de la variante D. El dibujo exacto está **SIN VERIFICAR** frente a los SVG de Commons:
cuando Paula los baje a referencias-reales/informe-inteligencia/app6/, los comparo y retoco.
Generador: TBD `claude/sprites-importar`, `.claude/skills/pixel-art-codigo/ejemplos/build_app6.py`.

## ELEGIDA la D (Lucía, 8-nov, 24:45). Retoques posteriores
- Trébol desconocido **dibujado a mano**, por filas (`TREBOL` en build_app6.py). Tiene una muesca de 2 px en cada diagonal y a 16 px ya no se lee como un octógono.
- Horda frente a hostil (`muestra/comparacion_horda_hostil.png`): a 16 px y sobre las 4 bandas, el hostil lleva la X y el relleno oscuro,
  y la horda va vacía, así que no se confunden. Por si en el juego sí se confunden, queda preparada la opción **tramada** (`app6_horda_tramado_16/24.png`,
  con el contorno a píxeles alternos).
- Sigue pendiente comparar con los SVG de Commons cuando Paula los baje.
