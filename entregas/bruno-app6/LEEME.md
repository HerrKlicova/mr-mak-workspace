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
- Comparación con los SVG de Commons: hecha el 8-nov (sección siguiente).

## Cotejo con los SVG de Commons de Paula (8-nov, 23:50; `referencias-reales/informe-inteligencia/app6/`)
Retocado:
- **Coraza** (acorazado y mecanizado): en APP-6 es un «estadio», un rectángulo con los extremos redondos de ~64 % del ancho y 50 % del alto
  del marco. Yo había dibujado una elipse. Cambiado.
- **Ala rotatoria**: la pajarita lleva un mástil vertical hacia abajo. Añadido. Se mantiene la cúpula de aire que eligió Lucía;
  Commons solo trae el helicóptero dentro del marco de tierra (APP-6A), que queda como alternativa si se prefiere.
- **Tamaño de unidad**: en la equivalencia española, ● = escuadra, ●● = pelotón, ●●● = sección, I = compañía. Yo tenía ● = pelotón, y estaba mal.
  `app6_amigo_*_peloton_*.png` lleva ahora **●●** (mismo nombre de archivo, cambia el dibujo). **Pregunta para Lucía**: el pelotón del juego
  tiene unos 21 hombres, que por tamaño es una sección OTAN (●●●). Si se prefiere el tamaño real al nombre, basta con usar los `_seccion_`.
- **Nuevos**: `app6_amigo_motorizado_peloton_16/24.png` (X + trazo vertical; p. ej. VAMTAC) y `app6_amigo_ruedas_peloton_24.png`
  (X + dos ruedas, blindado de ruedas como el Dragón). Las ruedas **solo existen a 24 px**: a 16 px se comen la X (en la muestra se ve).
Coincide sin cambios: la X del hostil (va a los puntos medios de los lados del rombo) y los marcos. Commons no trae marcos vacíos.
Las metas nuevas llevan GUID nuevo; las de los archivos que ya existían no cambian.
