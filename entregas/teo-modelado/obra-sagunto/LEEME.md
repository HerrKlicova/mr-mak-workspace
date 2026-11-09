# Obra en curso de Sagunto: qué pieza sale en cada tramo · Teo, 9-nov

Encargo de Lucía (9-nov): los datos del kit de obra en curso (`Models/Defensas/obra/`, ya en Unity desde 64a00ac) para que Marcos solo tenga que conectarlo a la cola de obras de la D-N163. Es lo cuarto en la prioridad del MVP.

## Archivos
- `obra_sagunto.json`: los **31 tramos** de la simulación de Sagunto, en el mismo orden que `NightSim.PiecesFromWorks` (lado 0 oeste, 1 este, 2 sur, 3 norte, y dentro de cada lado por A0). El índice `tramo` es el `Seg` de `WallJob` y de `WallEvent`. Cada tramo lleva su posición (x, z, en metros del mundo), el giro y las piezas de cada estado. Está calculado con el hueco de vía de **5 m** (`TrackHalfMm` 2500, aprobado).
- `obra_sagunto_hueco3m2.json`: lo mismo con el hueco de hoy (`TrackHalfMm` 1600). Usa este hasta que entre el de 5 m.
- `codigo/obra_sagunto.py`: reproduce `NetWorld.SagunteStart` y `Obras.PlanWall` (módulo de 10 m, partido en tramos iguales) y saca el JSON.

## Dónde va cada pieza
Cada pieza va en el **centro del tramo**, sobre el eje del muro, con el giro del tramo: 270 en el oeste, 90 en el este, 180 en el sur y 0 en el norte, con el fuera hacia +Z local, igual que los muros del kit. Todos los tramos de Sagunto miden de 5,25 a 9 m, así que va una pieza por tramo. Las de 10 m (HESCO) sobresalen un poco en los tramos de 7,25 m, y no pasa nada. Las piezas son **solo visuales**: sin colisión, sin NavMeshObstacle y fuera de los rayos de visión (condición de Lucía en `obra-curso/LEEME.md`).

## Qué sale en cada estado
| Estado de la cola | Muro de HESCO | Muro de sacos | Puerta (de vía o de vehículos) |
|---|---|---|---|
| Reparar, trabajando (`ObraEmpieza` → `Reparado`) | `SM_ObraHescoAbierto_v{p}_10m` + `SM_ObraHerramientas_v{h}_10m` | `SM_ObraSacos_v{s}_8m` + `SM_ObraHerramientas_v{h}_8m` | `SM_ObraPuertaApuntalada_v{s}_8m` + `SM_ObraHerramientas_v{h}_8m` |
| Reconstruir, en cola (ordenada, aún sin zapadores) | `SM_ObraReconstruccion_v3_10m` (estacas y cordel) | `SM_ObraReconstruccion_v3_8m` | `SM_ObraReconstruccion_v3_8m` |
| Reconstruir, trabajando (`ObraEmpieza` → `Reconstruido`) | `SM_ObraReconstruccion_v{p}_10m` + herramientas | `SM_ObraReconstruccion_v{p}_8m` + herramientas | ídem |
| `Reparado`, `Reconstruido` u `ObraCancelada` | se quita todo | | |

- **{s} y {h}** ya vienen resueltos en el JSON: {s} = `EstacionDato.VariantOf(x, z, 5)` en el centro del tramo, y {h} = ({s} + 2) mod 5, para que las herramientas no coincidan con la pieza principal.
- **{p}** sale del avance y se cambia mientras dura la obra:
  - HESCO reparando: según la vida del tramo, `Hp/HpMax` < 0,5 → v0 (arena a 1/4), < 0,8 → v1 (1/2) y el resto → v2 (3/4).
  - Reconstruyendo: según `WorkTicks / RebuildTicksFor(seg, zapadores)`, < 1/3 → v0, < 2/3 → v1 y el resto → v2 (primera hilada a 1/3, 2/3 y entera). `RebuildTicksFor` es privada: haría falta exponerla o guardar el total en el `WallJob`.
- La reconstrucción va **encima del modelo de brecha** del tramo (e3), que sigue puesto hasta `Reconstruido`.
- La puerta de vía mide 5 m y la pieza `PuertaApuntalada` 8 m: los puntales pasan 1,5 m por cada lado, por encima de las jambas.

## Para conectarlo (propuesta)
```csharp
// al leer WallEvents de la sombra (TickWallJobs / ApplySegmentPile)
case ObraEmpieza:  Obra.Poner(seg, job.Kind);      // instancia las piezas del JSON en (x, 0, z), yaw
case Reparado: case Reconstruido: case ObraCancelada:  Obra.Quitar(seg);
// cada segundo, para las obras activas: si cambia {p}, sustituye solo la pieza principal
// al ordenar una reconstrucción (Rebuild(seg) == true): Obra.PonerEnCola(seg)  → Reconstruccion_v3
```

— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)
