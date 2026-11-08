# Puntos de boca de arma (Muzzle_n) · Teo, 8-nov

> **Revisión de las 24:50 del 8-nov (Lucía).** (1) En `Apuntando` y en el clip `disparar` el fusil mira **al frente** y horizontal: la boca está a 1,22 m y su +Z es (0; 0; 1). (2) Variante nueva **v6 con G36E y C90** (tecla C, D-N137), con `Muzzle_1` en la boca del tubo. (3) **NH90: M3M en la puerta derecha (Muzzle_0) y MAG 58 en la izquierda (Muzzle_1)**, con las bocas en el mismo sitio. (4) Arreglado de paso: el esqueleto del soldado armado estaba 26 cm desplazado respecto a su malla, y por eso el clip `apuntar` y la malla fija `Apuntando` no coincidían. Ahora coinciden exactamente. Las mallas en reposo no cambian (comprobado: idénticas a las entregadas). Lo que cambia son los huesos y los clips, así que **hay que reimportar los seis `SM_SoldadoArmado_vN_<arma>` con esqueleto y los seis `_Apuntando`**.

Para Marcos, para la mecánica «El disparo sale de la boca del arma». Encargado por Lucía (8-nov, 24:34).

Todos los modelos que disparan llevan ya un punto vacío en el centro de la boca del arma, con nombres fijos: `Muzzle_0`, y `Muzzle_1` cuando hay una segunda arma. **El disparo sale por el +Z local del punto.** Se buscan por nombre (`transform.Find` en profundidad). Los FBX se han sustituido en sus carpetas de siempre, con los mismos nombres.

**Las mallas y los pivotes no cambian.** Se han regenerado con la misma tubería, y las 72 parejas (nuevo y entregado, LOD0 y LOD1) dan vértices, UV, materiales, jerarquía y huesos idénticos (diferencia máxima 0,0000). Las texturas y T_Paleta32.png no se tocan.

## Dónde está cada uno
- **Soldado con esqueleto** (`SM_SoldadoArmado_vN_<arma>`): `Muzzle_n` es un **hueso hoja sin pesos, hijo de `brazos`**, así que sigue al arma en todos los clips. No se usa un vacío porque un vacío colgado de un hueso salía desplazado 1,9 m en el FBX. Comprobado reimportando: en reposo, andar, disparar, apuntar y morir queda a 3 cm del extremo del cañón, que es su radio (el C90, a 7 cm).
- **Mallas fijas** (`…_Reposo` y `…_Apuntando`): `Muzzle_n` es un vacío hijo de la raíz, ya colocado en esa pose. Usan la misma convención que el soldado (nodo a −90 en X). Si cambias de malla en DOTS, coge la posición de la tabla de la pose que toque.
- **Dragón**: hijo de `Canon`, así que sigue a la torre y a la elevación. **VAMTAC**: hijo de `Ametralladora`. **NH90**: dos vacíos en la raíz (las armas van fijas), Muzzle_0 a la derecha (M3M) y Muzzle_1 a la izquierda (MAG 58). Valen para los 5 usos y para la carpeta por defecto.

## Tabla
Posición en el espacio del modelo, con los ejes de Unity (x a la derecha, y arriba, z adelante) y el origen en el pivote (los pies o la base). En metros, primero el LOD1, que es el que carga el juego.

| Modelo | Arma | Punto | Padre | LOD1 (x; y; z) | LOD0 (x; y; z) |
|---|---|---|---|---|---|
| SM_SoldadoArmado_v0_G36E | G36E | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v0_G36E_Reposo | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v0_G36E_Apuntando | G36E | Muzzle_0 | raíz (malla fija) | (-0.225; 1.223; 0.577) | (-0.222; 1.223; 0.580) |
| SM_SoldadoArmado_v1_G36E_AG36 | G36E + AG36 | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v1_G36E_AG36 | AG36 (lanzagranadas) | Muzzle_1 | hueso `brazos` | (0.249; 0.912; 0.452) | (0.252; 0.912; 0.454) |
| SM_SoldadoArmado_v1_G36E_AG36_Reposo | G36E + AG36 | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.483) | (0.275; 0.992; 0.486) |
| SM_SoldadoArmado_v1_G36E_AG36_Reposo | AG36 (lanzagranadas) | Muzzle_1 | raíz (malla fija) | (0.249; 0.912; 0.452) | (0.252; 0.912; 0.454) |
| SM_SoldadoArmado_v1_G36E_AG36_Apuntando | G36E + AG36 | Muzzle_0 | raíz (malla fija) | (-0.225; 1.223; 0.577) | (-0.222; 1.223; 0.580) |
| SM_SoldadoArmado_v1_G36E_AG36_Apuntando | AG36 (lanzagranadas) | Muzzle_1 | raíz (malla fija) | (-0.225; 1.136; 0.560) | (-0.222; 1.136; 0.562) |
| SM_SoldadoArmado_v2_G36E | G36E | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.436) | (0.275; 0.992; 0.438) |
| SM_SoldadoArmado_v2_G36E_Reposo | G36E | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.436) | (0.275; 0.992; 0.438) |
| SM_SoldadoArmado_v2_G36E_Apuntando | G36E | Muzzle_0 | raíz (malla fija) | (-0.225; 1.223; 0.530) | (-0.222; 1.223; 0.532) |
| SM_SoldadoArmado_v3_MG4E | MG4E | Muzzle_0 | hueso `brazos` | (0.304; 0.958; 0.556) | (0.308; 0.958; 0.559) |
| SM_SoldadoArmado_v3_MG4E_Reposo | MG4E | Muzzle_0 | raíz (malla fija) | (0.304; 0.958; 0.556) | (0.308; 0.958; 0.559) |
| SM_SoldadoArmado_v3_MG4E_Apuntando | MG4E | Muzzle_0 | raíz (malla fija) | (-0.274; 1.223; 0.681) | (-0.270; 1.223; 0.684) |
| SM_SoldadoArmado_v4_G28 | G28 | Muzzle_0 | hueso `brazos` | (0.330; 0.943; 0.561) | (0.333; 0.943; 0.564) |
| SM_SoldadoArmado_v4_G28_Reposo | G28 | Muzzle_0 | raíz (malla fija) | (0.330; 0.943; 0.561) | (0.333; 0.943; 0.564) |
| SM_SoldadoArmado_v4_G28_Apuntando | G28 | Muzzle_0 | raíz (malla fija) | (-0.283; 1.223; 0.699) | (-0.280; 1.223; 0.702) |
| SM_SoldadoArmado_v5_G36E | G36E (jefe) | Muzzle_0 | hueso `brazos` | (0.272; 0.992; 0.516) | (0.275; 0.992; 0.513) |
| SM_SoldadoArmado_v5_G36E_Reposo | G36E (jefe) | Muzzle_0 | raíz (malla fija) | (0.272; 0.992; 0.516) | (0.275; 0.992; 0.513) |
| SM_SoldadoArmado_v5_G36E_Apuntando | G36E (jefe) | Muzzle_0 | raíz (malla fija) | (-0.225; 1.223; 0.610) | (-0.222; 1.223; 0.607) |
| SM_SoldadoArmado_v6_G36E_C90 | G36E | Muzzle_0 | hueso `brazos` | (0.201; 0.992; 0.526) | (0.201; 0.992; 0.529) |
| SM_SoldadoArmado_v6_G36E_C90 | C90 (a la espalda) | Muzzle_1 | hueso `pecho` | (0.326; 1.520; -0.492) | (0.326; 1.520; -0.489) |
| SM_SoldadoArmado_v6_G36E_C90_Reposo | G36E | Muzzle_0 | raíz (malla fija) | (0.201; 0.992; 0.526) | (0.201; 0.992; 0.529) |
| SM_SoldadoArmado_v6_G36E_C90_Reposo | C90 (a la espalda) | Muzzle_1 | raíz (malla fija) | (0.326; 1.520; -0.492) | (0.326; 1.520; -0.489) |
| SM_SoldadoArmado_v6_G36E_C90_Apuntando | G36E | Muzzle_0 | raíz (malla fija) | (-0.297; 1.223; 0.620) | (-0.297; 1.223; 0.623) |
| SM_SoldadoArmado_v6_G36E_C90_Apuntando | C90 (a la espalda) | Muzzle_1 | raíz (malla fija) | (0.326; 1.489; -0.543) | (0.326; 1.489; -0.540) |
| SM_VCR_Dragon_Animable (todos los usos) | cañón de 30 mm | Muzzle_0 | `Canon` (bajo `Torre`) | (-0.250; 2.860; 3.462) | (-0.250; 2.860; 3.522) |
| SM_Vamtac_Animable (todos los usos) | ametralladora del aro | Muzzle_0 | `Ametralladora` (bajo `Aro`) | (0.000; 2.733; 1.885) | (0.000; 2.733; 1.885) |
| SM_NH90 (todos los usos) | M3M de puerta derecha | Muzzle_0 | raíz | (2.350; 1.750; 3.750) | (2.350; 1.750; 3.750) |
| SM_NH90 (todos los usos) | MAG 58 de puerta izquierda | Muzzle_1 | raíz | (-2.350; 1.750; 3.750) | (-2.350; 1.750; 3.750) |
Posición local respecto al padre (LOD1, ejes de Unity):
- Dragón, respecto a `Canon`: (0; 0; 2,60). En LOD0 es (0; 0; 2,66).
- VAMTAC, respecto a `Ametralladora`: (0; 0,08; 1,65).
- NH90: la de la tabla, porque cuelgan de la raíz.
- Soldado: el hueso lleva su propia rotación. Usa `Muzzle_n.position` y `Muzzle_n.forward` en el mundo y no hagas la cuenta a mano.

## Dirección del disparo (+Z del punto, ejes de Unity del modelo)
- Dragón y VAMTAC: (0; 0; 1), hacia delante. Gira con la torre y el cañón.
- NH90: Muzzle_0 (M3M) (0,80; −0,08; 0,60) y Muzzle_1 (MAG 58) (−0,80; −0,08; 0,60), hacia fuera y algo hacia delante, como está modelada la MAG.
- Soldado: en reposo, la del cañón tal como está modelado, (0,58; −0,25; 0,78), cruzado entre las manos. **En `apuntar`, `disparar` y la malla fija `Apuntando`, (0; 0; 1): recto al frente** (Lucía, 8-nov 24:50). En `disparar`, los fotogramas de retroceso suben el cañón 5° sobre la empuñadura. Para el disparo usa `Muzzle_n.position` y `Muzzle_n.forward`. Si el objetivo no está justo delante, puedes seguir usando la dirección hacia el objetivo, porque ahora sale del frente y no torcida.
- C90 (v6, `Muzzle_1`): (0; 0; 1), al frente del soldado. El tubo va a la espalda en diagonal y no hay pose de disparo del C90, así que el punto está en la boca del tubo, por encima del hombro y por detrás, y dispara hacia delante. Es de un solo uso. Si al disparar hay que ocultar el tubo, dímelo y lo saco como pieza aparte.
## Notas
- El C90 va en la variante v6 (`SM_SoldadoArmado_v6_G36E_C90`, con el mismo cuerpo que v0 y el tubo a la espalda, hijo del hueso `pecho`). Las seis variantes de antes no cambian de arma.
- El Lince no está en el MVP (Lucía, 8-nov 24:50), así que no lleva Muzzle.
- NH90: puerta derecha con FN M3M (12,7 mm: cajón y cañón más gruesos y caja de munición al lado) y puerta izquierda con MAG 58, como en la ficha del ET. Las bocas no se han movido.
- Los tiradores de la azotea usan los mismos SoldadoArmado (v4 G28 o cualquiera), así que ya lo llevan.
- La malla fija `Apuntando` y el clip `apuntar` dejan ahora la boca en el mismo punto (1,22 m de alto). El desfase de antes (1,43 frente a 1,27 m) venía de los huesos desplazados y ya está corregido.
- **SIN VERIFICAR en Unity:** la orientación está comprobada leyendo el FBX, donde el nodo del Dragón tiene la rotación local a cero, como su `Canon`, con +Z adelante. Una línea con `Debug.DrawRay(m.position, m.forward)` lo confirma.

Código: TBD `claude/modelado-3d-skill` 951e2b0 y 9ad4e08 (`rig_humano.py`: _encarar y huesos con la malla; `entregar.py`: crear_bocas; `malla3d.py`: vacíos en el FBX; BOCAS en `soldado_armado.py`, `dragon_animable.py`, `vamtac_animable.py` y `nh90.py`).
