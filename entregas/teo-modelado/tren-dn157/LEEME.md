# Lateral del tren más claro (D-N157) · Teo, 8-nov

> **Segunda pasada (23:44).** Bruno midió en pantalla 7,9 con #70784c (en la E, lateral contra el balasto D) y 14,5 con #88885c. Lucía elige **#88885c para el lateral**. El techo del vagón v2 y el canto del parapeto de la R2 pasan a **#b8b8b8**, como los demás techos. Por encima de #b8b8b8 solo está el hueso #d4d0cc, reservado para la interfaz. Lo que sigue describe la primera pasada (#70784c), que queda sustituida por esta. Mallas y pivotes, otra vez idénticos en las 18 parejas.
>
> **Carga (23:45, Lucía).** La carga visible pasa de #88885c a **#847c34**: las cajas de munición de la R2 y la carga del vagón cercano v2. Solo cambian esas dos piezas. Por albedo queda a ΔL* 4,4 del lateral (51,3 frente a 55,7), aunque se distingue también por el croma (40 frente a 25). Frente al techo #b8b8b8 da 23,5, y del ámbar #e08c30 está lejos (L* 65,6 y tono 67° frente a 100°). **Bruno tiene que medirlo en pantalla.**

Lo pidió Lucía el 8-nov a las 24:33. El lateral oliva de los vagones (#50541c, L* 34,3) quedaba a ΔL* 5,6 del balasto D con la luz de día, y Sara pide 8 o más.

**Cambio:** el lateral pasa de **#50541c a #70784c**, el siguiente oliva de la paleta de 32 (L* 48,8; mismo tono, 115° frente a 108°). Frente al balasto (L* 28–32) la diferencia sube a unos 17–20. Está lejos de la banda de la horda (L* 9–13) y del hueso. Se descartó #605c48 (L* 38,9) porque es gris y es el color de las chapas, las puertas y el piso: el lateral se fundiría con ellos.

**Retoques que salen de este cambio:**
- Techo del vagón cercano v2: de #70784c a #88885c, para que no se funda con el lateral nuevo.
- Canto del parapeto del R2: de #70784c a #88885c, por el mismo motivo.
- Las caras de abajo del casco siguen en #50541c y los techos en #b8b8b8.

**Mallas y pivotes, sin tocar.** Se han regenerado con la misma tubería. Las 18 parejas (nuevo y entregado, LOD0 y LOD1) tienen vértices, materiales, jerarquía y huesos idénticos (diferencia máxima 0,0000). Solo cambian las UV, que apuntan a otra celda de T_Paleta32.png. Antes se comprobó que, con los colores viejos, la tubería reproduce exactamente lo entregado (UV incluidas).

## Piezas (mismos nombres y carpetas que en docs/arte/modelado-3d)
- `tren_cercano/locomotora/SM_Locomotora_Cercana_LOD0/1.fbx`
- `tren_cercano/vagon_v0` … `vagon_v5/SM_Vagon_Cercano_vN_LOD0/1.fbx`
- `r1_locomotora/SM_R1_Locomotora_LOD0.fbx` y `lod1/SM_R1_Locomotora_LOD1.fbx`
- `r2_vagon_tropa/v3/SM_vagon_tropa_r2_LOD0.fbx` y `lod1/…_LOD1.fbx` (la versión aprobada)

T_Paleta32.png es la de siempre. Los vagones abandonados, la cisterna, la locomotora de «Aquí pasó algo» y la carga de los vagones no usan #50541c en el lateral, así que no cambian.

**Para Bruno:** volver a medir de día y de noche contra el balasto D.

Código: TBD `claude/modelado-3d-skill` 36a2410, db95b64 y b12ca52 (vagon_cercano.py, locomotora_cercana.py, locomotora_r1.py, vagon_tropa_r2.py). Se entrega con `--costado 88885c` y `--claro b8b8b8`.
