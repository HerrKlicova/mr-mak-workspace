# Puerta de vía del muro oeste de Sagunto (SM_PuertaVia) · Teo, 8-nov

Para Iker y Marcos. Los datos son de Álvaro (8-nov, 10:18; sagunto-nivel.md §6.3 y §7 C1). **Aprobada por Lucía (8-nov, 10:22)** con un cambio, ya hecho: el dintel de la v4 sube de 3 m a 6 m. La variante la pone la semilla en cada instancia; para capturas, la v1. Hoja: /mnt/project-files/docs/arte/modelado-3d/puerta-via/.

## La pieza
- Hueco de **5 m** (Z 62–67 del nivel), por el que solo pasa la vía 1. Lleva **dos hojas batientes de 2,5 m que abren hacia dentro**, para que el tren no las pise.
- Las jambas son de HESCO, de 0,9 m, por fuera de los 5 m. En la v4 son pilares de hormigón de 6,5 m con el dintel por encima del tren y de la catenaria: cara de abajo a 6,0 m. Verificado por Paula con la Orden FOM/1630/2015 (catálogo, RC1–RC3): hilo de contacto CA-160 a 5,30 m y zona libre del pantógrafo a 5,63 m, así que el dintel deja 0,37 m de margen. El sustentador (a ~6,7 m, SIN VERIFICAR) no cabe y se ancla bajo el dintel, como bajo la losa de RC3: la v4 lleva un **anclaje colgado** (soporte, travesaño a 5,75 m y dos aisladores en el LOD0). El hilo del nivel pasa por debajo, a 5,30 m.
- Las hojas miden 2,1 m, enrasadas con el HESCO. **SIN VERIFICAR:** la altura real del sólido del muro la tiene que confirmar Marcos.
- Hay 5 variantes y 4 estados: los de la puerta de vehículos de la D-N163, con la misma paleta. El nombre sigue el patrón `SM_PuertaVia_v<V>_<Variante>_e<E>_<Estado>_LODn.fbx`, con la misma `T_Paleta32.png` de siempre.

## Jerarquía y ejes
- El origen está en el suelo, en el centro del hueco, sobre el eje de la vía 1. El muro va a lo largo de X local.
- `Hoja_O` tiene la bisagra en x = −2,49 y `Hoja_E` en x = +2,49. **Abren hacia dentro** girando +90° (O) y −90° (E) sobre la vertical, al revés que la puerta de vehículos.
- **Fuera es +Z de Unity con yaw 0**, y tiene que mirar fuera del recinto (Álvaro, sagunto-nivel.md §10.9): muro oeste yaw 270, sur 180, este 90 y norte 0. Coordenadas de Álvaro con el muro oeste en X = 70 (dato de Marcos):
  - **Puerta de vía: (70; 0; 64,5), yaw 270.** Hueco en Z 62,0–67,0 y jambas en Z 61,1–62,0 y 67,0–67,9.
  - **HESCO del tutorial: (70; 0; 72,9), yaw 270.**
  - Puerta oeste-sur: (70; 0; 53), yaw 270. Puerta sur: (99; 0; 45), yaw 180.
- Alturas: el sólido del muro mide 2,5 m (Level.WallH) y todas las piezas visibles 2,1 m (hojas hasta 2,16 m). Se quedan así (Mak, 8-nov).

## Tramo de HESCO del tutorial
No es una pieza nueva: es `muro-estados/hesco/SM_MuroHesco_*` (módulo de 10 m), con yaw 270, pegado al norte de la puerta. Empieza en e1 (Danado, 45 %); al repararlo por encima del 70 % pasa a e0, y si cae más, e2 y e3 como cualquier tramo.
- **Posición: (70; 0; 72,9)**, a tope con la jamba norte (Z 67,9–77,9); con Z 72 se metía 0,9 m en la jamba.
- Comprobación de cómo se lee junto a la puerta: /mnt/project-files/docs/arte/modelado-3d/puerta-via/hoja_puerta_tutorial.png (escena de prueba `escena_puerta_tutorial.py`, no es una pieza del juego).

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de las 20 (la v4 vuelta a pasar con el dintel nuevo, 8/8 OK).
- También va actualizada la e2 (muy dañado) de muro-estados/puerta_vehiculos: el corte de la hoja ahora queda por encima del nervio de la blindada. Los nombres no cambian.

Código: TBD `claude/modelado-3d-skill`, ca38a9c (`bloques/puerta_via.py`).
