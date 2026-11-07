# Radar terrestre de la red de estaciones (D-N124 §6.2) · Teo, 7-nov

Para Iker, que lleva las estaciones. Está basado en el radar Raven del ET, a partir de la foto de Paula `referencias-reales/radar/R1_radar_raven_1.jpg` (CC BY 3.0): un remolque de un eje con mástil articulado y cabeza giratoria. Las medidas son SIN VERIFICAR, estimadas sobre la foto, con la cabeza a 5,2 m del suelo.

## Archivos
LOD0 y LOD1 de cada variante. Todos usan la misma `T_Paleta32.png` (la paleta de 32), así que basta con un material URP/Lit con `_BaseMap` = paleta, igual que los vehículos.

| Variante | Uso (Lucía, 09:08) | Medidas (X x Z x alto) |
|---|---|---|
| v1 Instalacion | **Por defecto** en una estación (Segura): remolque, shelter de equipos, generador aparte (el ruido) y vientos | 8,5 x 4,7 x 6,1 m |
| v0 RecienLlegado | Recién llegado en el tren, sin montar | 2,6 x 3,5 x 6,1 m |
| v2 Fortificado | Mejora fortificada: sacos y red de camuflaje | 8,9 x 5,6 x 6,1 m |
| v3 Plegado | En construcción o en traslado | 2,2 x 3,5 x 2,6 m |
| v4 Destruido | Estación caída: calcinado, inclinado y con la cabeza en el suelo | 4,8 x 3,7 x 3,9 m |

## Jerarquía
- `SM_…_LODn` es la base, con el origen en el suelo, en el centro de la parcela, mirando a +Z en Unity.
- `Antena` (solo en v0, v1 y v2) tiene el origen en el eje del brazo alto y gira sobre su Y local, que es la vertical. Propuesta: una vuelta cada 4 s con el radar en marcha, y parada si no hay combustible (0,80 u al día, Hugo).

## Colocación (Álvaro, estaciones/castellon.json)
- En Castellón va en (206; 0; 82), con yaw 180, para que la lanza mire hacia el andén.
- Reparto por estado: v3 en construcción, v1 Segura y v4 Caída. Castellón empieza infestada, así que el radar no está al principio: se construye.

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de las cinco variantes.
- Nada bajo L* 28 (D-N80). Familia oliva sin techos beige (Lucía).

Código: TBD `claude/modelado-3d-skill`, `bloques/radar.py`, e148d40. Hoja: /mnt/project-files/docs/arte/modelado-3d/radar/hoja_radar.png.
