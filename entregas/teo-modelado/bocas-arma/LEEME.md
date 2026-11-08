# Puntos de boca de arma (Muzzle_n) · Teo, 8-nov

Para Marcos, para la mecánica «El disparo sale de la boca del arma». Encargado por Lucía (8-nov, 24:34).

Todos los modelos que disparan llevan ya un punto vacío en el centro de la boca del arma, con nombres fijos: `Muzzle_0`, y `Muzzle_1` cuando hay una segunda arma. **El disparo sale por el +Z local del punto.** Se buscan por nombre (`transform.Find` en profundidad). Los FBX se han sustituido en sus carpetas de siempre, con los mismos nombres.

**Las mallas y los pivotes no cambian.** Se han regenerado con la misma tubería, y las 72 parejas (nuevo y entregado, LOD0 y LOD1) dan vértices, UV, materiales, jerarquía y huesos idénticos (diferencia máxima 0,0000). Las texturas y T_Paleta32.png no se tocan.

## Dónde está cada uno
- **Soldado con esqueleto** (`SM_SoldadoArmado_vN_<arma>`): `Muzzle_n` es un **hueso hoja sin pesos, hijo de `brazos`**, así que sigue al arma en todos los clips. No se usa un vacío porque un vacío colgado de un hueso salía desplazado 1,9 m en el FBX. Comprobado reimportando: en reposo, andar, disparar, apuntar y morir queda a 3 cm del extremo del cañón, que es su radio.
- **Mallas fijas** (`…_Reposo` y `…_Apuntando`): `Muzzle_n` es un vacío hijo de la raíz, ya colocado en esa pose. Usan la misma convención que el soldado (nodo a −90 en X). Si cambias de malla en DOTS, coge la posición de la tabla de la pose que toque.
- **Dragón**: hijo de `Canon`, así que sigue a la torre y a la elevación. **VAMTAC**: hijo de `Ametralladora`. **NH90**: dos vacíos en la raíz (las MAG van fijas), Muzzle_0 a la derecha y Muzzle_1 a la izquierda. Valen para los 5 usos y para la carpeta por defecto.

## Tabla
Posición en el espacio del modelo, con los ejes de Unity (x a la derecha, y arriba, z adelante) y el origen en el pivote (los pies o la base). En metros, primero el LOD1, que es el que carga el juego.

| Modelo | Arma | Punto | Padre | LOD1 (x; y; z) | LOD0 (x; y; z) |
|---|---|---|---|---|---|
| SM_SoldadoArmado_v0_G36E | G36E | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v0_G36E_Reposo | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v0_G36E_Apuntando | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 1.429; 0.495) | (0.275; 1.429; 0.497) |
| SM_SoldadoArmado_v1_G36E_AG36 | G36E + AG36 | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v1_G36E_AG36 | AG36 (lanzagranadas) | Muzzle_1 | hueso `brazos` | (0.249; 0.912; 0.452) | (0.252; 0.912; 0.454) |
| SM_SoldadoArmado_v1_G36E_AG36_Reposo | G36E + AG36 | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v1_G36E_AG36_Reposo | AG36 (lanzagranadas) | Muzzle_1 | raíz (malla fija) | (0.249; 0.912; 0.452) | (0.252; 0.912; 0.454) |
| SM_SoldadoArmado_v1_G36E_AG36_Apuntando | G36E + AG36 | Muzzle_0 | raíz (malla fija) | (0.272; 1.429; 0.484) | (0.275; 1.429; 0.484) |
| SM_SoldadoArmado_v1_G36E_AG36_Apuntando | AG36 (lanzagranadas) | Muzzle_1 | raíz (malla fija) | (0.249; 1.344; 0.497) | (0.252; 1.344; 0.497) |
| SM_SoldadoArmado_v2_G36E | G36E | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.436) | (0.275; 0.992; 0.438) |
| SM_SoldadoArmado_v2_G36E_Reposo | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.436) | (0.275; 0.992; 0.438) |
| SM_SoldadoArmado_v2_G36E_Apuntando | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 1.429; 0.495) | (0.275; 1.429; 0.497) |
| SM_SoldadoArmado_v3_MG4E | MG4E | Muzzle_0 | hueso `brazos` | (0.304; 0.958; 0.556) | (0.308; 0.958; 0.559) |
| SM_SoldadoArmado_v3_MG4E_Reposo | MG4E | Muzzle_0 | raíz (malla fija) | (0.304; 0.958; 0.556) | (0.308; 0.958; 0.559) |
| SM_SoldadoArmado_v3_MG4E_Apuntando | MG4E | Muzzle_0 | raíz (malla fija) | (0.304; 1.453; 0.512) | (0.308; 1.453; 0.514) |
| SM_SoldadoArmado_v4_G28 | G28 | Muzzle_0 | hueso `brazos` | (0.330; 0.943; 0.561) | (0.333; 0.943; 0.564) |
| SM_SoldadoArmado_v4_G28_Reposo | G28 | Muzzle_0 | raíz (malla fija) | (0.330; 0.943; 0.561) | (0.333; 0.943; 0.564) |
| SM_SoldadoArmado_v4_G28_Apuntando | G28 | Muzzle_0 | raíz (malla fija) | (0.330; 1.464; 0.575) | (0.333; 1.464; 0.577) |
| SM_SoldadoArmado_v5_G36E | G36E (jefe) | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.516) | (0.275; 0.992; 0.513) |
| SM_SoldadoArmado_v5_G36E_Reposo | G36E (jefe) | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.516) | (0.275; 0.992; 0.513) |
| SM_SoldadoArmado_v5_G36E_Apuntando | G36E (jefe) | Muzzle_0 | raíz (malla fija) | (0.272; 1.429; 0.541) | (0.275; 1.429; 0.538) |
| SM_VCR_Dragon_Animable (todos los usos) | cañón de 30 mm | Muzzle_0 | `Canon` (bajo `Torre`) | (-0.250; 2.860; 3.462) | (-0.250; 2.860; 3.522) |
| SM_Vamtac_Animable (todos los usos) | ametralladora del aro | Muzzle_0 | `Ametralladora` (bajo `Aro`) | (0.000; 2.733; 1.885) | (0.000; 2.733; 1.885) |
| SM_NH90 (todos los usos) | MAG 58 de puerta derecha | Muzzle_0 | raíz | (2.350; 1.750; 3.750) | (2.350; 1.750; 3.750) |
| SM_NH90 (todos los usos) | MAG 58 de puerta izquierda | Muzzle_1 | raíz | (-2.350; 1.750; 3.750) | (-2.350; 1.750; 3.750) |
Posición local respecto al padre (LOD1, ejes de Unity):
- Dragón, respecto a `Canon`: (0; 0; 2,60). En LOD0 es (0; 0; 2,66).
- VAMTAC, respecto a `Ametralladora`: (0; 0,08; 1,65).
- NH90: la de la tabla, porque cuelgan de la raíz.
- Soldado: el hueso lleva su propia rotación. Usa `Muzzle_n.position` y `Muzzle_n.forward` en el mundo y no hagas la cuenta a mano.

## Dirección del disparo (+Z del punto, ejes de Unity del modelo)
- Dragón y VAMTAC: (0; 0; 1), hacia delante. Gira con la torre y el cañón.
- NH90: Muzzle_0 (0,80; −0,08; 0,60) y Muzzle_1 (−0,80; −0,08; 0,60), hacia fuera y algo hacia delante, como está modelada la MAG.
- Soldado: la dirección del cañón tal como está modelado, que en reposo es (0,58; −0,25; 0,78) y en `apuntar` (0,57; 0,18; 0,80). **Ojo:** el arma del modelo apunta unos 35° a la derecha del frente, porque va cruzada entre las dos manos. Si el disparo tiene que ir recto al objetivo, usa la posición de `Muzzle_n` y la dirección hacia el objetivo, y no su forward.

## Notas
- El C90 no está en ninguna de las seis variantes de SoldadoArmado (va aparte, con las SM_Arma_* sueltas, a la espalda), así que no lleva Muzzle. Si se monta en un soldado, se le añade.
- **El Lince no tiene entrega de modelo** (solo el bloque lince.py), así que se queda sin Muzzle hasta que se entregue.
- Lucía pedía M3M y MAG 58 en las puertas del NH90. **El modelo lleva dos MAG 58**, una por puerta. Si una tiene que ser M3M, se cambia el arma y su Muzzle va en el mismo sitio.
- Los tiradores de la azotea usan los mismos SoldadoArmado (v4 G28 o cualquiera), así que ya lo llevan.
- La malla fija `Apuntando` deja la boca a 1,43 m de alto, y el clip `apuntar` del soldado con esqueleto a 1,27 m. Era así antes de este cambio, porque las dos poses no son iguales. Lo apunto por si el fogonazo no cuadra al cambiar de malla.
- **SIN VERIFICAR en Unity:** la orientación está comprobada leyendo el FBX, donde el nodo del Dragón tiene la rotación local a cero, como su `Canon`, con +Z adelante. Una línea con `Debug.DrawRay(m.position, m.forward)` lo confirma.

Código: TBD `claude/modelado-3d-skill` 951e2b0 (`entregar.py`: crear_bocas; `malla3d.py`: vacíos en el FBX; BOCAS en `soldado_armado.py`, `dragon_animable.py`, `vamtac_animable.py` y `nh90.py`).
