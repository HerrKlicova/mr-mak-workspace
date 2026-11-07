# Suelo de noche con la paleta de 32 (D-N129, regla 6). Bruno (Arte técnico), 7-nov

Encargo de Lucía: el suelo de noche deja de pasar por SnapSub (17 colores), usa la paleta de 32 con 3 o más valores de su familia
y el color dominante en el 30 % como mucho. Hoy (Noche41, 347ea06) el dominante está en el 54,5 %.
Causa: las texturas de día son beige b4a080 en un 91 % (apisonada 3743 de 4096 px), y SnapSub devuelve casi todo a beige.
Con el 70 % de detalle no se llega nunca al 30 %, porque falta materia.

## Qué entrego
Una textura de detalle de noche de 64x64 (téxel 0,1 m, anclada al mundo como las de día) que vale para TODAS las zonas, porque
D-N129 dice que de noche ninguna zona se distingue. Se usa tal cual: sin SnapSub y sin mezclar con la media. 5 variantes, todas comprobadas:

| | reparto | dominante | valores > 5 % |
|---|---|---|---|
| A (recomendada) | beige 30 · concrete_light 30 · olive_light 30 · olive 10 | 30,0 % | 4 |
| B | igual que A con más estructura; se ve la repetición en bandas | 30,0 % | 4 |
| C | beige 28 · concrete_light 30 · olive_light 28 · tan 14; el tan forma manchas de óxido | 30,0 % | 4 |
| D | beige 20 · concrete_light 30 · olive_light 30 · olive 20; más fría y más oscura | 30,0 % | 4 |
| E | 5 valores con olive_yellow; se ven manchas repetidas | 30,0 % | 5 |

L* de los valores: beige 66,8 · concrete_light 61,1 · olive_light 55,7 · olive 48,8. La rampa es continua, de 5 a 7 L* por paso.
No usa valores de la horda, ni d4d0cc, ámbar, rojos o 442c0c. No hay tramado ordenado: es fbm de periodo 8-4 con un 30 % de ruido de 1 px,
cortado por cuantiles. Generador: TBD .claude/skills/pixel-art-codigo/ejemplos/build_suelo_noche.py.

## Cambios para Marcos (PrototypeBootstrap.cs, 347ea06)
1. Importar en Assets/TBD/Resources/Suelo/ la que elija Lucía (por defecto la A), DESDE EL EDITOR, con su .meta. El .meta va con GUID nuevo y los mismos
   ajustes que suelo_apisonada_64: Point, sin mips, isReadable 1 y sRGB.
2. En GroundSrc, añadir `nocheTex = Px("suelo_noche_A_64")`.
3. En ComposeChunk (hacia la línea 1863), sustituir el cálculo de night[idx] por esto:
   ```
   var n = gs.nocheTex[v * 64 + u];
   float t = Mathf.Clamp01((dLampC - 9f) / 2f);     // 0 bajo el foco, 1 a 11 m o más
   night[idx] = t >= 1f ? n : t <= 0f ? c : (Color32)Color.Lerp(c, n, t);
   ```
   Bajo los focos se queda el color de día, como ahora. En el anillo de 9 a 11 m hay un fundido suave. Ahí salen colores fuera de paleta,
   pero solo en ese anillo de 2 m, y sin tramado (D-N129 lo prohíbe). En BuildGroundSample (hacia la línea 1950) va el mismo cambio.
4. SnapSub se queda solo para el día.

## Ojo
- La media de la textura nueva es más gris y algo más oscura que el beige de día (L* medio aprox. 60 frente a 67). El barrido G1–G5 de la noche
  tiene que hacerse CON esta textura puesta, o la exposición quedará mal. SIN VERIFICAR en Unity.
- Medición en la captura directa: ≥ 3 valores > 5 % de la zona de mundo y ninguno > 30 %, sin bordes rectos.
  Con la luz encima, dos albedos pueden juntarse en un mismo valor de pantalla. Si pasa, lo arreglo yo en la textura.
