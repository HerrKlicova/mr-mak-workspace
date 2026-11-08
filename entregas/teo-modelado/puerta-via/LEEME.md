# Puerta de vía del muro oeste de Sagunto (SM_PuertaVia) · Teo, 8-nov

Para Iker y Marcos. Los datos son de Álvaro (8-nov, 10:18; sagunto-nivel.md §6.3 y §7 C1). **Pendiente de la revisión de Lucía.** Hoja: /mnt/project-files/docs/arte/modelado-3d/puerta-via/.

## La pieza
- Hueco de **5 m** (Z 62–67 del nivel), por el que solo pasa la vía 1. Lleva **dos hojas batientes de 2,5 m que abren hacia dentro**, para que el tren no las pise.
- Las jambas son de HESCO, de 0,9 m, por fuera de los 5 m. En la v4 son pilares de hormigón con dintel a 3 m.
- Las hojas miden 2,1 m, enrasadas con el HESCO. **SIN VERIFICAR:** la altura real del sólido del muro la tiene que confirmar Marcos.
- Hay 5 variantes y 4 estados: los de la puerta de vehículos de la D-N163, con la misma paleta. El nombre sigue el patrón `SM_PuertaVia_v<V>_<Variante>_e<E>_<Estado>_LODn.fbx`, con la misma `T_Paleta32.png` de siempre.

## Jerarquía y ejes
- El origen está en el suelo, en el centro del hueco, sobre el eje de la vía 1. El muro va a lo largo de X local.
- `Hoja_O` tiene la bisagra en x = −2,49 y `Hoja_E` en x = +2,49. **Abren hacia dentro** girando +90° (O) y −90° (E) sobre la vertical, al revés que la puerta de vehículos.
- **Fuera es +Z de Unity con yaw 0.** Álvaro propone colocarla en (69; 0; 64,5) con yaw 90, pero con yaw 90 el fuera mira a +X, que es el este, hacia dentro del recinto. En el muro oeste, para que el fuera mire al oeste, probablemente haga falta **yaw 270**. Comprobadlo con la puerta oeste-sur, que usa la misma convención.

## Tramo de HESCO del tutorial
No es una pieza nueva: es `muro-estados/hesco/SM_MuroHesco_*` (módulo de 10 m), colocado en (69; 0; 72) y pegado a la hoja norte. Empieza dañado (e1) al 45 %.

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de las 20.
- También va actualizada la e2 (muy dañado) de muro-estados/puerta_vehiculos: el corte de la hoja ahora queda por encima del nervio de la blindada. Los nombres no cambian.

Código: TBD `claude/modelado-3d-skill`, ca38a9c (`bloques/puerta_via.py`).
