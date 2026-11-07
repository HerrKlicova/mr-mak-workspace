# Soldado con el arma en la mano, y pose «apuntando» (Teo, 7-nov, 08:35)

## 1. Por qué las armas salían en el suelo
Las `SM_Arma_*` sueltas (6-nov) se exportaron con la conversión de ejes **horneada** (su nodo no lleva rotación), mientras que el soldado, que tiene esqueleto, se exporta **sin hornear**: su nodo de malla y su `_Rig` llevan `Lcl Rotation (-90, 0, 0)`. Lo he comprobado leyendo los FBX. Si un arma cuelga del nodo del soldado (o copia su transform) con identidad, hereda ese -90° en X y se queda tumbada en el suelo. No he vuelto a exportar los soldados v2 y v5 con otro pivote: los seis se exportaron juntos el 7-nov a las 00:11, y el arma nunca ha ido en el FBX del soldado. Un md5 distinto no significa que cambie la geometría, porque el FBX guarda la fecha de exportación y el md5 cambia con cada exportación aunque el modelo sea el mismo.

## 2. El arreglo: el arma va dentro de la malla del soldado
`SM_SoldadoArmado_*` es el mismo cuerpo aprobado, con los mismos colores y el mismo esqueleto, pero con el arma dentro de la malla y asignada al 100 % al hueso `brazos` (el C90 no entra en estas seis). Así no hay que emparentar nada, y el arma sigue a las manos en todos los clips.

| Variante | Arma (propuesta según las dotaciones de decisiones-noche.md) |
|---|---|
| v0 | G36E |
| v1 | G36E con AG36 (granadero) |
| v2 | G36E |
| v3 | MG4E (ametrallador) |
| v4 | G28 (tirador) |
| v5 | G36E (jefe, con la radio) |

Si quieres otra combinación, pídela y la saco en dos minutos.

## 3. Ficheros (LOD0 y LOD1 de cada uno; misma T_Paleta32.png de siempre)
- `SM_SoldadoArmado_vN_<arma>_LODn.fbx`: con esqueleto y clips `reposo`, `andar`, `disparar`, `morir` y uno nuevo, **`apuntar`** (pose fija, 12 f).
- `SM_SoldadoArmado_vN_<arma>_Reposo_LODn.fbx` y `..._Apuntando_LODn.fbx`: **mallas fijas, sin esqueleto**, para cambiar de malla en DOTS (§4.3 del encargo de Lucía). Las he exportado con la misma convención que el soldado (nodo `-90` en X), así que al cambiar una por otra en la misma entidad no gira nada. Las dos de cada variante coinciden en los pies y en el origen.
- `md5.txt` con los md5 de estos FBX.

## 4. Pose «apuntando»
La culata va al hombro, el arma a la horizontal y orientada al frente (+Z en Unity), con el pecho adelantado y una pierna atrasada. El paso de reposo a apuntando (0,25 s) y el retroceso (2 px, 1 fotograma) los haces tú por código, como dice el encargo. Los ángulos están ajustados a ojo, SIN VERIFICAR contra captura, y **falta el visto bueno de Lucía** (la hoja va en `hoja_soldado_apuntando.png`).

Las SM_Arma_* sueltas siguen valiendo para otras combinaciones, pero solo si van como hijas del **mismo nodo que lleva el -90** (la malla del soldado) y con la rotación local (90, 0, 0), o con «Bake Axis Conversion» activado en el importador de Unity. Es más sencillo usar SoldadoArmado.
