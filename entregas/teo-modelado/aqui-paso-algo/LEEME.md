# Kit «Aquí pasó algo» de Sagunto · Teo, 8-nov

Para Álvaro (colocación) y Marcos (zona de Sagunto). Sale de sagunto-nivel.md §3 («aquí pasó algo», fuera del muro). **Aprobado por Lucía (8-nov, 19:07).** Hoja: /mnt/project-files/docs/arte/modelado-3d/aqui-paso-algo/hoja_aqui_paso_algo.png.

4 piezas × 5 variantes, en LOD0 y LOD1: `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas usan la misma `T_Paleta32.png`, como el kit. Lo largo va a lo largo de X. El origen está en el centro, en el suelo (a la cota del carril en las piezas de vía). El vuelco ya viene en la malla. El juego carga el LOD1.

## Condiciones de Lucía (obligatorias)
1. **El mercancías descarrilado y la vía rota van solo en vías muertas o apartaderos sin uso**, nunca en un recorrido de tren. Una vía rota en un recorrido diría que la línea está cortada, y reparar vías es de después del MVP.
2. **La catenaria caída es solo visual**: no corta la vía ni hace daño. El poste está a 3,2 m del eje, en +Y, fuera del gálibo. Cuando cae, queda paralelo a la vía.
3. **El autobús cruzado SUSTITUYE al `autobus_cruzado` del inventario de obstáculos de Álvaro**, no se añade. Mantiene su caja envolvente: centro en (59; 92), yaw 74, 11,3 × 5,5 m. Tapa la visión y no tiene sólido.
4. Nada en la banda de la horda. Las lunas y los bastidores van en 605c48, no en 48403c.

## Colocación (Álvaro, 19:07; él avisa a Marcos y actualiza el CSV)
- Vía 2 (muerta), en Z 59,5, de este a oeste:
  - Locomotora con el centro en X 33. **Mide 19,3 m**, así que ocupa X 23,4–42,6; la v4 Aplastada lleva 2,9 m de chatarra en +X, hasta X 45,5.
  - Tolva v0 en X 16, v2 en X 1 (yaw +8) y v3 en X −14 (yaw −12).
  - Todo queda lejos del desvío (X 50–64), de la calle (X 56–62) y del paso a nivel (X 59).
- Vía rota (tramos de 12 m), entre X −40 y −22.
- Catenaria caída sobre la vía 2, entre X 0 y 30.

## Piezas
| Carpeta | Variantes | Medidas |
|---|---|---|
| Locomotora | Descarrilada (girada 6°), Ladeada (15°), Volcada, Quemada, Aplastada | 19,3 × 2,9 × 4,3 m (de pie) |
| ViaRota | Levantada, Traviesas, Socavon, Cruzada, Grava | 12 × 3,4 m |
| CatenariaCaida | Colgando, MensulaRota, Inclinado, Caido, Enredado | vano de 15 m, poste de 7,5 m |
| AutobusCruzado | Cruzado, Barricada, Volcado, Quemado, Empujado | 11 × 2,6 × 3,2 m |

## Comprobado
- Auditoría OK en LOD0 y LOD1 de las 20 piezas. Banda de la horda (L* 9–13): 0 %.
- SIN VERIFICAR: medidas de memoria. Locomotora genérica de mercancías, en gris y sin el naranja real.

Código: TBD `claude/modelado-3d-skill`, `bloques/aqui_paso_algo.py` (e19da1f).
