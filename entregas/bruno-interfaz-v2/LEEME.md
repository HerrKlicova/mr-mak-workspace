# Interfaz v2 (D-N147): 5 maquetas y piezas. Bruno (Arte técnico), 7-nov

Encargo de Lucía (docs/interfaz-v2.md). 5 maquetas a 1920×1080 sobre una captura de la Noche46 (qa34, horda_2235_oeste; ya con CaptureRoutine
corregida, la placa da 283440). La disposición es la misma en las cinco; cambian las tarjetas, el minimapa y las órdenes.

| | estilo |
|---|---|
| 1_plano | Plano oscuro v1.4 tal cual: franja 181c30 al 85 %, tarjetas 202538 con borde de 1 px en 353a55 |
| 2_sueltas | Sin franja: cada pieza flota con su fondo; cabecera 283440 con el nombre; el minimapa lleva título |
| 3_esquinas | Franja al 70 %, tarjetas sin caja, con esquinas de visor y raya oliva bajo el nombre; minimapa con rejilla |
| 4_minima | Sin franja ni bordes, fondo al 55 % y texto con sombra; minimapa redondeado |
| 5_retrato | Como la 1, con el retrato del jefe (de las tarjetas de 48) y las siluetas en 2 filas de 4; minimapa con bisel |

## Medidas
- Panel inferior de 140 px más barra de atajos de 16 px: 156 px, el 14,4 % de 1080 (límite: 15 %). Las órdenes flotan encima del minimapa, fuera del panel, como pide §2.
- Contraste del texto (WCAG). En el peor caso, el fondo al 85 % está sobre el suelo más claro de la captura.
  - Hueso d4d0cc: 11,0 sobre 181c30 · 9,9 sobre 202538 · 9,6 al 85 % en el peor caso · 7,0 al 55 % (estilo 4).
  - Gris 94948c (etiquetas y textos secundarios): 5,5 · 5,0 · 4,8 · **3,5 en el estilo 4 (no llega a 4,5)**.
  - Ámbar e08c30 («Sin munición»): 6,4 · 5,8 · 5,6 · **4,1 en el estilo 4**.
  Conclusión: los estilos 1, 2, 3 y 5 cumplen. El 4 solo cumple subiendo su fondo al 75 % o más.
- Colores reservados: el hueso solo en la selección (marco de 2 px en la tarjeta 1), en el texto y en la orden activa. El ámbar solo en avisos y en munición
  por debajo del 25 %. El rojo solo en el ataque (aviso de brecha y tramo del muro en el minimapa).
- Texto: Inter (OFL, libre), 24 px el reloj, 13–15 px el texto, 10–11 px etiquetas y atajos. En Unity, el texto lo pinta UI Toolkit; las piezas en píxel van a 1x.

## Piezas (piezas/, con .meta de GUID nuevo, Point y sin mips como las de formaciones)
- ui_sil_{fusilero,ametrallador,tirador}_{viva,caida}_10x20: una silueta por hombre; viva en hueso y caída en 353a55.
- ui_veh_{dragon_56,vamtac_48,nh90_64}x22: siluetas laterales en hueso.
- ui_orden_{linea,cuna,columna,bloque,fuego_libre,alto_fuego,aterrizar,descargar}_16. La cuña es nueva (F2 de la D-N147). Línea, columna y bloque son las de build_formaciones.
- El icono de formación de 12 px de la esquina de la tarjeta usa ui_formacion_*_12 (entregas/bruno-formaciones); la cuña de 12 la genera build_interfaz_v2.py.
- Los iconos de recursos y de avisos son los de siempre (vm_cargas_*_16 y vm_alertas_*_16, a 2x en recursos).

## Lo que NO es la build
- La captura lleva el HUD viejo. Lo he quitado subiendo el mundo limpio y rellenando 192 filas encima del panel con suelo de la misma captura.
  Queda una costura en la fila 732, tapada con un degradado oscuro entre las filas 690 y 924. **Ese degradado es solo de la maqueta, no forma parte de la propuesta.**
  Para la próxima ronda pido una captura sin HUD (por ejemplo, una bandera -sinhud).
- Los datos (munición, estados, avisos, minimapa) son de ejemplo. El minimapa es un esquema, no un render del mapa.
- No conozco el comportamiento de la interfaz de Ebbtide en movimiento. Solo se han tomado patrones de disposición, no gráficos.

Generador: TBD .claude/skills/pixel-art-codigo/ejemplos/build_interfaz_v2.py
