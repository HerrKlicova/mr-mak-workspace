# Capa de obras: contornos de los tramos, estilo A (Lucía, 8-nov). Bruno (Arte técnico)

Para Marcos (modo reparar, construccion-reparar.md §1 y §2). Referencia visual: /mnt/project-files/docs/arte/pixel-codigo/tutorial-obras/obras_A.gif.

## Qué se dibuja por tramo (solo con el modo obras abierto, tecla B)
| Estado | Vida | Marca |
|---|---|---|
| Sano | ≥ 70 % | nada |
| Dañado | 30–70 % | contorno ámbar e08c30 sólido |
| Muy dañado | 1–30 % | el mismo contorno, que late: 0,6 s sólido y 0,6 s tramado al 50 %; nunca se apaga del todo |
| Brecha | 0 | relleno 982420 tramado (Bayer 6/16) y contorno 982420 sólido de 0,1 m |

## Medidas (texel de 0,1 m, la norma de D-N67)
- **Contorno**: rectángulo alrededor de la huella del tramo, separado 0,2 m por fuera y de 0,2 m de ancho (2 téxeles del mundo; a la escala de la cámara, unos 2 px del mundo a 1/3, lo mismo que la muestra). Va en el suelo (y ≈ 0,03) y además sube por los dos extremos del tramo hasta la altura de su cara de arriba, para que se lea aunque el muro tape el lado de atrás.
- Los tramos contiguos comparten el lado: dibuja solo uno (el del tramo de la izquierda), para que no salga un trazo doble.
- Capa del mundo (no VFX_HD), para que se pixele con el muro. Material sin luz (URP Unlit o el Sprites/Default de siempre), con transparencia, ZWrite Off y ZTest Always, para que el contorno se vea a través del modelo. Sin bloom ni HDR: el ámbar es un aviso, no una luz.
- **Tramado del muy dañado**: `T_obra_tramado50` (damero de 2x2, blanco con alfa; tíñelo con el color del material). Repeat y Point. UV en espacio de mundo: `uv = mundo.xz * 10 / 2`, es decir, un téxel por cada 0,1 m, para que el damero quede fijo en el suelo y no "nade" con la cámara.
- **Brecha**: quad que cubre la huella, con `T_obra_brecha_bayer` (4x4, cobertura 6/16), con las mismas UV en mundo y el color 982420. El contorno de la brecha es de 0,1 m (más fino que el ámbar).
- **Icono de ruido** (§3, D-N123): `ui_obra_ruido_32` (y `_16` para el minimapa o la cola). Encima del tramo que se está reparando, a la altura de la cara de arriba más 1,5 m, en VFX o en la UI. Es una pala con ondas en ámbar.

## Archivos
`Assets/TBD/Resources/Obras/` con su `.meta` (Point, sin mipmaps y sin compresión; las dos T_ en Repeat y los iconos en Clamp) y `Obras.meta`. Copiar desde el Editor o con Unity cerrado.
SIN PROBAR en Unity. Los colores son los de la paleta, y el rojo de la brecha está permitido por construccion-reparar.md §1.
