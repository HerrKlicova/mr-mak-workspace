# Kit «Sagunto vivo»: la vida dentro del fuerte y las huellas de fuera · Teo, 8-nov

Para Álvaro (colocación), Marcos (zona de Sagunto) y Bruno (luz del fuego). Sale de sagunto-nivel.md §3 («aquí vive gente») y §10.8 (armario de Adif). **Aprobado por Lucía (8-nov, 19:01)**, con sus dos retoques ya hechos: el solar en tierra y los bidones solo en gris. Hojas: /mnt/project-files/docs/arte/modelado-3d/sagunto-vivo/.

8 piezas × 5 variantes, en LOD0 y LOD1: `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas usan la misma `T_Paleta32.png` (material URP/Lit con `_BaseMap` = paleta, como el kit). El origen está en el suelo, en el centro de la pieza, con el frente hacia −Y de Blender (+Z en Unity con yaw 0). El juego carga el LOD1.

## Condiciones de Lucía (obligatorias)
1. **Ninguna pieza lleva colisión**, tampoco el armario de Adif, ni pathing ni bloqueo de visión.
2. **La luz del bidón con fuego la pone Bruno** y se comprueba con -capdirecta. Tiene que ser cálida y pequeña y no iluminar la horda al otro lado del muro. La llama y las brasas van en el hijo `Emision` (en BidonFuego y en CocinaCampana/Lena), con el mismo origen: el punto de luz va ahí.
3. **La colocación la hace Álvaro**: lejos de la banqueta, de la azotea del ala oeste y de los recorridos de la tropa. El tren parte el recinto en dos franjas de unos 19 m.
4. El STOP y el aspa de la cruz llevan la cara en b8b8b8 y el borde en 605c48, sin el rojo real. En el LOD1 el aspa va blanca, sin borde.
5. **Los bidones de combustible son decorado** y no cuentan como existencias. Van en gris, porque en la carga el verde es munición.

## Piezas
| Carpeta | Variantes | Dónde (propuesta; decide Álvaro) |
|---|---|---|
| BidonFuego | Solo, Parrilla, Dos, Corro, Apagado | Junto al almacén, dentro del fuerte |
| Tendedero | Cuerda, DosCuerdas, Sabanas, Balcon (sale de una pared en +Y), Vacio | Patios traseros de la hilera de delante y terrazas del bloque de pisos |
| Bancales | Plantas, Plantado, Regadera, Tomateras, Seco | Huerto improvisado entre el almacén y el muro sur |
| Tienda | Militar, Lona, Iglu, Colchones, Caida | Dentro del fuerte |
| CocinaCampana | Olla, Lena, Garrafas, Comedor, Recogida | Junto al edificio de viajeros |
| Bidones | Pale4, Fila6, Tumbados, Lona, Volcados | Junto a la vía, dentro del fuerte |
| Solar | Escombro, Medianera, Vigas, Despejado, Tejas | Los dos huecos de la hilera de delante (5.ª y 9.ª casa), 6 × 10 m como casa_pueblo |
| ArmarioAdif | Completo, Pintado, Abierto, CruzDoblada, Volcado | Paso a nivel (59; 63,6), en lugar de la caseta (§10.8). Armario en −X y cruz en +X |

## Comprobado
- Auditoría OK en LOD0 y LOD1 de las 40 piezas. Banda de la horda (L* 9–13): 0 % en todas.
- SIN VERIFICAR: las medidas son de memoria. El armario y la cruz salen de las fotos P2 y P3 de Paula (referencias-reales/entorno/).

Código: TBD `claude/modelado-3d-skill`, `bloques/vida_fuerte.py` (03bb160 + e39e2ad) y `bloques/sagunto_vivo.py`.
