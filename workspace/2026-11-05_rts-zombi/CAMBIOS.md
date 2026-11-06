# Cambios respecto a la idea original

Historial de cómo evoluciona cada cosa. La **idea original** vive congelada en
[GDD-v0.1-original.md](GDD-v0.1-original.md) y no se edita. El estado actual está en
[GDD.md](GDD.md). Aquí se anota **cada cambio** con su motivo.

## Formato de cada entrada

```
### C-001 · AAAA-MM-DD · Sistema: <nombre>
- Antes: ...
- Ahora: ...
- Motivo: ... (enlace a D-xxx si hay decisión)
- Origen: quién lo decidió y dónde
- Commit: <hash> (cuando exista)
```

## Entradas

*Todavía no hay cambios: el GDD v0.1 no está cerrado. Cuando se congele, el primer cambio será C-001.*

## Registro previo al GDD (herramientas y proceso)

| Fecha | Qué | Motivo |
| --- | --- | --- |
| 2026-11-05 | La API de imagen/vídeo de ElevenLabs pasa de «no disponible» (plan Creator) a disponible (plan Pro) | Eugenio subió el plan; D-003 |
| 2026-11-05 | Motor 3D: se elige Hunyuan | Eugenio; D-002 |
| 2026-11-05 | Versión de Unity: la 6.6 que instaló el Hub por defecto se sustituye por la 6.3 LTS | D-001 y D-006 |
| 2026-11-05 | Prioridad: se para el lote de Pixelab y se empieza antes el prototipo jugable sin arte | Eugenio; D-009 |
| 2026-11-05 | Primera ejecución en Unity: 10.000 zombis a 198 FPS en el editor; corrección de `TempJob` en `ZombieStepSystem` (commit `87f3a5f` de `TBD`) | Hito de la primera apertura |
| 2026-11-05 | Separación por densidad entre zombis: la horda deja de avanzar en filas de uno (commit `83a243a` de `TBD`) | Fallo visible en el primer GIF del hito 1 |
| 2026-11-05 | Hito 2: mapa de operaciones jugable, con mancha de horda, horarios y carga, y tiempo x1/x2/x4 como órdenes (commit `4e2bf7a` de `TBD`). Posiciones del mapa geográficas aproximadas | Hoja de ruta de Lucía |
