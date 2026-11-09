# Colores reservados en las piezas del MVP · Teo, 9-nov

Encargo de Lucía (9-nov, 00:16). He repasado las piezas buscando tres colores reservados:
- **d4d0cc**: interfaz y selección.
- **e08c30**: avisos.
- **982420**: ataques y brechas.

**Qué he mirado:** todos los FBX que hay en Unity (rama `marcos/noche-prototipo`, 8baca89) y el paquete [IMPORTAR-NOCHE.md](../IMPORTAR-NOCHE.md). En total son 1.732 FBX distintos. Para cada cara he leído el color de su píxel en `T_Paleta32` y he medido qué parte del área ocupa. También he revisado el color de vértice de la pila. En Unity hay 409 FBX que no estaban en mr-mak, y esos los he leído directamente del LFS.

## Resultado
- **982420:** no está en ninguna pieza.
- **e08c30:** solo en la franja del frontal de las locomotoras R1 y Cercana (del 0,45 al 0,57 % del área). Es la excepción aprobada en la D-N42 y la dejo como está.
- **d4d0cc:** aparece en 180 FBX. Los casos claros ya están corregidos (lista A). Las fachadas encaladas no las he tocado y las decide Lucía (lista B).

## A · Corregido: de d4d0cc a b8b8b8 (o 88885c en la cara de abajo)
Son 37 piezas, 74 FBX. Las mallas son idénticas a las de antes (lo he comprobado con los vértices de las 74), y solo cambia el píxel de la paleta. Después del cambio no queda d4d0cc en ninguna. Las paletas de Unity de esas carpetas tienen los mismos píxeles que la nueva, así que **no hace falta copiar `T_Paleta32`**.

| Pieza | Material | Antes | Ahora | % del área antes | En Unity |
|---|---|---|---|---|---|
| Tapia de víveres de Nules v0–v4 | cal | d4d0cc | b8b8b8 | casi todo el muro | No está todavía (nules-viveres/Tapia) |
| Casa de labor de víveres v0, v2, v3 y v4 (la v1 Ocre ya iba en f0dc9c) | cal | d4d0cc | b8b8b8 | fachada | No está todavía (nules-viveres/CasaLabor) |
| SM_PuertaVehiculos_Castellon v4 | placa | d4d0cc | b8b8b8 | 2 % | `puerta_vehiculos/` (renombrar antes; ver IMPORTAR-NOCHE §3.2) |
| SM_PuertaValla v0–v4 (Bétera) | placa y muretes | d4d0cc | b8b8b8 | 25–53 % | `Betera/puerta_valla/` |
| SM_TanqueCombustible v2 (el blanco) | cuerpo | d4d0cc | b8b8b8 | 63 % | `Betera/tanque_combustible/` |
| SM_Helipuerto v0–v4 | marcas de la losa y manga | d4d0cc | b8b8b8 | 8–16 % | `Betera/helipuerto/` |
| SM_coche_2000 v2 y v5 (los blancos) | carrocería arriba / abajo | d4d0cc / b8b8b8 | b8b8b8 / 88885c (como coche_civil) | 22–24 % | `Sagunto/coche_2000/v2`, `v5` |
| SM_poste_km v0–v5 | hormigón | d4d0cc | b8b8b8 | 44–68 % | `Sagunto/senales/` |
| SM_senal_via v0–v5 | placa | d4d0cc | b8b8b8 | 4 % | `Sagunto/senales/` |
| SM_paso_superior | línea de la calzada (solo LOD0) | d4d0cc | b8b8b8 | 0,2 % | `Sagunto/paso_superior/` |

Los FBX para Unity están en `colores-reservados/Models/`, con las mismas rutas que `Assets/TBD/Resources/Models/`. Basta con copiarlos encima de los que ya hay. Los de mr-mak (`nules-viveres/`, `betera/`, `puerta_vehiculos/`) ya están sustituidos en su sitio.

**En el paquete, ya corregido:** los 8 FBX de `Defensas/muro` (la placa de la puerta de vehículos v4) y los 4 de `Nules/puerta_via_doble` que tenían d4d0cc en Unity se sustituyen con IMPORTAR-NOCHE (la placa de la v4 ya va en b8b8b8).

## B · Sin tocar: lo decide Lucía
Son el encalado y las fachadas de los edificios fijos. Es el blanco de los pueblos de la zona, y Lucía lo aprobó así (por ejemplo, la estación de Sagunt «blanca, cal d4d0cc», 7-nov). Pasarlo a b8b8b8 los vuelve grises. Recuerda que la torre de control y el vestíbulo de Castellón ya se pasaron a b8b8b8 por esto mismo («d4d0cc en grande es el color de la selección»).

| Pieza | Material | % del área |
|---|---|---|
| Sagunto: edificio de viajeros v0–v5 | fachada (cal) | 33–39 % |
| Sagunto: casa_pueblo v0, v2, v4 y v5 | cal | 57–62 % |
| Sagunto: casa_baja v0, v2 y v4 | cal | 40–42 % |
| Sagunto: almacén de naranjas v0–v3 y v5 | cal | 36–39 % |
| Sagunto: muelle de mercancías v0–v3 y v5 | mampostería | 26–27 % |
| Sagunto: bloque_pisos v4 | fachada blanca | 44–46 % |
| Sagunto: paso a nivel (caseta) | cal | 32–47 % |
| Kit de estaciones: KitCuerpo v0–v6, KitRemate v0–v5 y KitSueltas v2, v5 y v6 | fachada | 3–84 % |
| Kit de estaciones: montajes de Castellón v0–v3 y de Nules v0–v4 | fachada | 35–37 % |
| Nules: edificio de viajeros v0–v4 | fachada | 51–53 % |
| VCR Dragón v5 (LOD1) | visor del tirador, una mancha de 2×2 px | 0,4 % (Bruno lo puso así a propósito) |

Si se decide pasarlas a b8b8b8 (o a f0dc9c en algunas, para que no quede todo gris), son unos 110 FBX. Con el mismo método, cambia solo el color y no la malla.

Código: TBD `claude/modelado-3d-skill` c3cb55a (bloques coche_2000, tanque_combustible, helipuerto, puerta_valla, poste_km, senal_via, paso_superior, puerta_vehiculos y viveres_nules).

— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)
