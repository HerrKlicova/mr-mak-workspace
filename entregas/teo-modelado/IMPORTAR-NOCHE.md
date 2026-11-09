# Paquete de importación de la noche · Teo, 9-nov

Para Marcos. Encargo de Lucía (9-nov, 00:02). Junta en una sola pasada las entregas que tenías sueltas: el muro y la obra en curso (94cb579), las puertas del asedio (6822e61 y af7d2eb), la pila de zombis (6822e61) y el tren de la D-N157 (109ba85, más d06af89 con el R2 renombrado).

Lo he comparado con tu rama `marcos/noche-prototipo` en 8baca89 (9-nov, 00:24). Para cada fichero comparé el sha256 de la entrega con el puntero LFS del repo. Hay **426 FBX: 100 ya están iguales, 88 cambian y 238 son nuevos.** La lista fichero a fichero, con commit, destino, estado, triángulos, nodos y sha, está en [IMPORTAR-NOCHE.csv](IMPORTAR-NOCHE.csv).

## Cómo importarlo
- **Escala:** 1 unidad = 1 m. Al importar, Scale Factor 1 y Convert Units marcado, como el resto de mis FBX. Todas las piezas salen con escala (1, 1, 1).
- **Ejes:** el muro y las puertas van a lo largo de X local. **Fuera (por donde llega la horda) es +Z de Unity con yaw 0**, que es −Y en Blender. El tren va a lo largo de Z, como el que ya tienes.
- **Material:** URP/Lit con `_BaseMap` = `T_Paleta32.png` de la misma carpeta (32×16 px, filtro de punto). La excepción es la pila, que usa TBD/Horda con el color de vértice «Col», y **al importarla el alfa no se debe forzar a 1**.
- **Sustituir, no borrar.** Copia cada FBX encima del que ya existe con el mismo nombre (con el Editor cerrado o desde el propio Editor). Así se queda el `.meta` y no cambia el GUID. No hay prefabs: todo se carga con `Resources.Load` por ruta, así que no hay que tocar referencias.
- **Paletas:** copia también la `T_Paleta32.png` de cada carpeta. En `R1/`, `R2/` y `Vehiculos/tren/*` la del repo es más vieja (otro sha). En `Defensas/muro` y `Nules/puerta_via_doble` ya es la misma.

## 1 · Qué va a dónde
Las rutas de destino empiezan en `Assets/TBD/Resources/Models/`. Las carpetas marcadas con «nueva» no existen en tu rama: son una propuesta mía, cámbialas si prefieres otras.

| Entrega (entregas/teo-modelado/) | Commit | Destino | FBX | Estado | Pivote y sockets | Sustituye a |
|---|---|---|---|---|---|---|
| `muro-estados/hesco/` SM_MuroHesco (módulo de 10 m) | 94cb579 | `Defensas/muro/` | 40 | **iguales** | Origen en el suelo, en el centro del módulo | Nada: ya está |
| `muro-estados/sacos/` SM_MuroSacos (tramo de 8 m) | 94cb579 | `Defensas/muro/` | 40 | **iguales** | Ídem | Nada: ya está |
| `muro-estados/puerta_vehiculos/` SM_PuertaVehiculos (8 m) | af7d2eb | `Defensas/muro/` | 40 | **cambian los 40** | Origen en el centro del hueco. Hijos `Hoja_O` y `Hoja_E`, con el origen en su bisagra (x Unity +3,99 / −3,99) | Los 40 `SM_PuertaVehiculos_v*_<Variante>_e*` de la carpeta |
| `puerta-via/` SM_PuertaVia (5 m) | 94cb579 y 6822e61 | `Defensas/puerta_via/` (nueva) | 40 | nuevos | Ídem, bisagras en ±2,49 | La caja de 2,5 m sobre 3,2 m del código (ver §3) |
| `nules/puerta_via_doble/` SM_PuertaViaDoble (7,4 m) | 94cb579 y 6822e61 | `Nules/puerta_via_doble/` | 40 | 32 iguales, **8 cambian** (las v4) | Ídem, bisagras en ±3,69 | Las 8 v4 Blindada |
| `puertas-asedio/colision/` SM_<Puerta>_Col | 6822e61 | `Defensas/colision/` (nueva) | 3 | nuevos | La misma jerarquía y los mismos pivotes que la puerta: raíz = jambas, `Hoja_O` y `Hoja_E` | — |
| `obra-curso/` SM_Obra<Pieza>_v<n>_<8\|10>m | 94cb579 | `Defensas/obra/` (nueva) | 100 | nuevos | El mismo origen y el mismo giro que el tramo al que se superpone | — |
| `pila-zombis/celda/` SM_PilaZombi_Altura<1-5>_s<0-2> | 6822e61 | `Zombi/pila/celda/` (nueva) | 30 | nuevos | Origen en el suelo, al pie de la cara de fuera (y = 0); la pila baja hacia +Z | Los zombis sueltos a partir de 3 por celda |
| `pila-zombis/remate/` SM_PilaZombi_Remate{Der,Izq}_… | 6822e61 | `Zombi/pila/remate/` (nueva) | 60 | nuevos | Origen en el borde de la celda del extremo | — |
| `pila-zombis/colision/` SM_PilaZombi_…_COL | 0dd8b6a | `Zombi/pila/colision/` (nueva) | 15 | nuevos | Igual que la celda | — |
| `tren-dn157/tren_cercano/locomotora/` | 5018dd0 | `Vehiculos/tren/locomotora/` | 2 | **cambian** | Origen en el suelo, en el centro | Los dos SM_Locomotora_Cercana |
| `tren-dn157/tren_cercano/vagon_v0…v5/` | 84e1194 (la v2, 109ba85) | `Vehiculos/tren/vagon_v0…v5/` | 12 | **cambian** | Ídem. Hijo `Ventanillas` | Los 12 SM_Vagon_Cercano |
| `tren-dn157/r1_locomotora/` (+ `lod1/`) | 5018dd0 | `R1/` | 2 | **cambian** | Ídem | SM_R1_Locomotora_LOD0/1 |
| `tren-dn157/r2_vagon_tropa/juego/` (+ `lod1/`) | d06af89 | `R2/` | 2 | **cambian** | Ídem | SM_R2_VagonTropa_LOD0/1 |

### Abrir y cerrar las puertas (Hoja_O / Hoja_E)
- Se gira el `localRotation` de cada hijo sobre la Y local. **Las tres puertas abren hacia dentro:** cerrada 0°, a medio cerrar O +45° y E −45°, y abierta O +90° y E −90°.
- **Cambia respecto al LEEME de muro-estados:** la de vehículos ya no gira O −90° y E +90°. En tu rama ningún script gira todavía `Hoja_O` ni `Hoja_E` (lo he buscado), así que no hay nada que corregir en el código.
- **Colisión:** mete el `SM_<Puerta>_Col` como hijo de la puerta y gira a la vez los `Hoja_*` de los dos. Usa `transform.Find("Hoja_O")` sobre cada raíz por separado, porque los dos tienen hijos con el mismo nombre. En Brecha (e3), desactiva las dos hojas de la colisión.
- **La pila delante de una puerta cerrada** va con el origen 0,16 m hacia fuera del centro del muro. Delante del HESCO va a 0,55 m.

### Sockets Muzzle_N
**Ninguna pieza de este paquete lleva `Muzzle_N`.** Las bocas de fuego están en otra entrega, [bocas-arma/LEEME.md](bocas-arma/LEEME.md), con el soldado armado y los vehículos. Tu `Infanteria/` solo tiene los `SM_SoldadoArmado_v0–5_LOD1` con rig: faltan las mallas Reposo y Apuntando y la v6 (C90). Si quieres meter también eso en la misma pasada, dímelo y te preparo su tabla.

## 2 · Triángulos
### Por pieza (máximo y media de las variantes y estados)
| Pieza | LOD0 máx. (media) | LOD1 máx. (media) | Presupuesto LOD0 / LOD1 |
|---|---|---|---|
| SM_MuroHesco (10 m) | 1.656 (1.045) | 708 (425) | — |
| SM_MuroSacos (8 m) | 1.152 (815) | 528 (288) | — |
| SM_PuertaVehiculos | 780 (552) | 540 (326) | 3.000 / 1.500 |
| SM_PuertaVia | 692 (439) | 396 (246) | 2.500 / 1.200 |
| SM_PuertaViaDoble | 692 (473) | 396 (251) | 3.000 / 1.400 |
| Colisión de puerta | 48 (3 cajas) | — | — |
| SM_Obra*, todas | 1.140 (250) | 580 (144) | 3.000 / 900 |
| · de ellas, Reconstruccion (la mayor) | 1.140 (546) | 580 (274) | |
| Celda de pila, Altura4 | 460 (416) | 268 (247) | 700 / 400 |
| Celda de pila, Altura5 | 528 (471) | 304 (283) | 700 / 400 |
| Remate de pila, Altura4 | 528 (475) | 288 (252) | 700 / 400 |
| Colisión de pila | 4–24 | — | — |
| SM_Locomotora_Cercana | 2.456 | 1.744 | 4.000 / 2.000 |
| SM_Vagon_Cercano v0–v5 | 872–2.720 | 680–1.200 | 4.000 / 2.000 |
| SM_R1_Locomotora | 2.096 | 1.384 | 4.000 / 2.000 |
| SM_R2_VagonTropa | 1.808 | 848 | 4.000 / 2.000 |

**Ninguna pieza pasa de su presupuesto.** He revisado los 426 ficheros.

### Peor caso en pantalla: Sagunto con asedio y la pila a la altura 4
Cuento todo el recinto a la vez, con la pieza más cargada de cada familia. Es un techo: la cámara del RTS no ve los cuatro lados de cerca a la vez. Tu código carga el LOD1, así que esa es la columna que cuenta. La del LOD0 es para la cámara cercana.

Las cuentas del recinto salen de `sagunto_obstaculos_v1.csv` (X 70–156, Z 44–85) y de la tabla de puertas de Álvaro (puertas-asedio/LEEME.md):

| Qué | Cuántos | LOD1 | LOD0 |
|---|---|---|---|
| HESCO: el frente oeste, sin los huecos de 5 y 8 m, y las dos alas (≈ 57 m) | 6 módulos | 4.248 | 9.936 |
| Sacos: norte, este y sur, sin huecos (≈ 171 m) | 21 tramos | 11.088 | 24.192 |
| Puertas de vía (oeste y este) | 2 | 792 | 1.384 |
| Puertas de vehículos (sur E4 y oeste-sur) | 2 | 1.080 | 1.560 |
| Obra en curso (una reparación por lado) | 4 | 2.320 | 4.560 |
| Tren de noche parado: R1 y dos R2 | 3 | 3.080 | 5.712 |
| **Pila a la altura 4 en TODO el perímetro de fuera (≈ 254 m)** | 508 celdas | **136.144** | 233.680 |
| Remates de la pila (en las puertas y en las esquinas) | 8 | 2.304 | 4.224 |
| **Total** | | **≈ 161.000** | ≈ 285.000 |

- **Con el frente oeste atacado** (41 m, el caso de la noche que probáis), la pila son 82 celdas: unos 22.000 triángulos en LOD1. El recinto entero baja a unos **47.000**.
- **No he encontrado un presupuesto de triángulos por pantalla** escrito en el GDD ni en los criterios (solo hay presupuestos por pieza). Como referencia, la primera prueba movió 10.000 zombis a 198 FPS en el editor, y un zombi suelto de la D-N80 tiene de 144 a 248 triángulos. **Nada del paquete supera lo que ya se dibuja con la horda.**
- **La pila ahorra en lugar de gastar.** Una celda a la altura 4 son 6 zombis o más, unos 1.150 triángulos sueltos, y la pieza tiene como mucho 268. Las 508 celdas sustituyen a unos 3.050 zombis (≈ 580.000 triángulos sueltos).
- **Aviso (no es de triángulos):** 508 celdas son 508 objetos. Hay solo 15 mallas de celda, con un único material, así que conviene activar GPU Instancing en el material TBD/Horda o dibujarlas con `Graphics.RenderMeshInstanced`. Si van como GameObjects sueltos, lo que pesará serán las llamadas de dibujo, no los triángulos.

## 3 · Choques de nombres y cosas que pueden confundir
1. **Ningún fichero nuevo coincide de nombre con otro de `Resources/`** (lo he comprobado en todas las carpetas, sin distinguir mayúsculas). Las carpetas nuevas tampoco existen ya con otra grafía. Las 188 coincidencias que hay son los ficheros que se sustituyen en su misma ruta.
2. **Hay dos modelos que se llaman SM_PuertaVehiculos:**
   - `puerta_vehiculos/SM_PuertaVehiculos_v0–4` es la D-N111 antigua, sin estados. La sigue cargando `EstacionVista.cs` para `estacion_castellon.json`.
   - `Defensas/muro/SM_PuertaVehiculos_v*_<Variante>_e*` es la de este paquete.

   **No borres la antigua** mientras Castellón la use. Castellón está cerrada en el MVP, pero el JSON sigue ahí.
3. **El hueco de la puerta de vía no cuadra.** El código cierra el hueco de 3,2 m (Z 62,9–66,1) con una caja de 2,5 m de alto (`PrototypeBootstrap.cs`, junto a la línea 2645). La pieza de este paquete tiene un hueco de 5 m (jambas en Z 61,1–62,0 y 67,0–67,9), y su colisión mide 2,1 m de alto. Al colocar la puerta de vía hay que ensanchar el hueco del muro oeste a 5 m o la pieza quedará metida en el HESCO. El muro de 2,5 m de la noche es cosa de Nacho, así que se lo paso.
4. **Los nombres de dentro del FBX no son los del fichero.** Los nodos raíz se llaman como el bloque que los generó (`SM_bloques.puerta_estados_v0_LOD1`, `SM_pila_zombis_v3_LOD1`, `SM_obra_curso_v11_LOD0`…), y en la pila se repiten entre celda, RemateDer y RemateIzq (30 nombres repetidos). Al cargar por ruta no pasa nada. Lo que no hay que hacer es buscar las mallas por nombre (`LoadAll<Mesh>`, `Find` por nombre de malla).
5. **Las mayúsculas de la colisión no son iguales:** la pila acaba en `_COL` y las puertas en `_Col`. El prefijo `UCX_` del objeto de la pila es de Unreal, y Unity no crea el collider solo. Pon un `MeshCollider` con Convex en las cuñas y un `BoxCollider` (o un `MeshCollider`) en las cajas de las puertas.
6. **R2:** en la entrega de la D-N157 el R2 se llama `SM_vagon_tropa_r2` (carpeta `r2_vagon_tropa/v3/`), pero el juego carga `Models/R2/SM_R2_VagonTropa_LOD1`. Usa la copia de `r2_vagon_tropa/juego/`, que tiene el nombre bueno (d06af89). Es la misma malla que la v3 (comprobado).
7. **`Hoja_O` y `Hoja_E` se repiten** en cada puerta y en su colisión. Es a propósito, pero conviene buscarlos siempre bajo la raíz que toque (ver §1).

— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)
