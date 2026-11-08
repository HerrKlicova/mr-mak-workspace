# Azotea del edificio de viajeros de Sagunto · Teo, 8-nov

> **ANULADO (8-nov 18:03, Lucía y Álvaro):** la azotea real está en las alas, a 4,75 m. Usa `edificio-viajeros-sagunto/` en lugar de estas piezas.

Para Marcos. Sale de sagunto-nivel.md §10.15 (Álvaro): Lucía aprobó la azotea, que sustituye a las atalayas, y **estas piezas, el 8-nov a las 14:22**. Medido sobre el LOD1 a tamaño de juego, el 0 % de los píxeles cae en la banda de la horda. Las hojas están en /mnt/project-files/docs/arte/modelado-3d/azotea/. Todas las carpetas comparten la misma `T_Paleta32.png`. Medidas SIN VERIFICAR.

| Carpeta | Piezas | Origen y montaje |
|---|---|---|
| pretil | `SM_PretilTramo`, `SM_PretilEsquina` y `SM_PretilEsquinaPaso` × 5 variantes × 4 estados (`_v<a>_<Variante>_e<n>_<Estado>`). Son los sacos del muro aprobado, con 1,2 m de alto y 1 m de grueso. Sin estado de obra, porque viene hecho. Estados: Sano ≥70 %, Danado 30–70, MuyDanado 1–30 y Brecha 0 | Origen a la altura de la azotea (11 m). **Tramo**: 5,1 m, centrado, con fuera = −Y. **Esquina**: bloque de 1 × 1 m y brazos de 3,4 m hacia +X y +Y, con fuera = −X −Y; cubre 4,4 m por lado. **Esquina con paso**: el brazo +Y mide 2,2 m. Azotea de 19 × 8,8 m (X 96,5–115,5, Z 75–83,8): cuatro esquinas (la del sureste, con paso: hueco en Z 78,2–79,4) y dos tramos en cada lado largo. Lo que cae hacia fuera no está en el modelo |
| escalera | `SM_EscaleraAzotea` v0 Metalica, v1 Jaula, v2 Obra, v3 Andamio y v4 Danada (sin el tramo de abajo y con una escalera de mano) | Origen en el suelo, en el centro de la planta de 2 × 6 m (X 115,5–117,5, Z 76–82). El testero queda en −X local y los tramos van a lo largo de Y. Son 4 tramos de 2,75 m, con plataforma arriba a 11 m que da al hueco del pretil |

Auditoría y presupuesto OK en las 130 mallas. Código: TBD `claude/modelado-3d-skill` 2d2ac5f (`bloques/pretil_azotea.py` y `escalera_azotea.py`).

**Comprobar al colocar (Marcos):** lo único medido del exportador es que −Y de Blender sale como +Z en Unity; el eje X no está comprobado. En las piezas en L (esquinas del pretil) y en la escalera, mirar la primera que se coloque. Si la plataforma de la escalera no queda contra el edificio, va con yaw 180. Si los brazos de una esquina salen hacia fuera de la azotea, se gira 90°. El origen de las esquinas está en el centro del bloque de dentro, a 0,5 m del vértice exterior en cada eje (posiciones de Álvaro en sagunto-nivel.md §10.15).
