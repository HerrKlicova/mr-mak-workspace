# Coches civiles abandonados: atasco de la carretera vieja y paso superior de Sagunto · Teo, 8-nov

Para Marcos, a través de Mak. Corresponde a los puntos 6 y 9 de la revisión de la Noche57 de Álvaro (`docs/niveles/revision-noche57-guia.md`). **Aprobado por Lucía (8-nov, 13:09)** con dos cambios, ya hechos: la lona del camión pasa a beige o gris, porque en verde se leía como militar, y el óxido del quemado va en manchas, no en un cuadrado. Hoja: /mnt/project-files/docs/arte/modelado-3d/coches-civiles/hoja_coches_civiles.png.

- `SM_CocheCivil_<Tipo>_v<V>_LOD0/LOD1.fbx`, con la `T_Paleta32.png` de siempre.
- Tipos: **Utilitario** 3,8 m, **Berlina** 4,5 m, **Furgoneta** 4,8 m, **Todoterreno** 4,4 m y **Camion** 6,6 m (cabina y caja de lona).
- Variantes: v0 intacto, v1 con la puerta del conductor abierta, v2 pinchado y ladeado, v3 accidentado (morro hundido) y v4 quemado (sobre las llantas).
- Delante es −Y de Blender, que en Unity es +Z con yaw 0. El origen está en el suelo, en el centro. **Sin colisión** en el MVP (sagunto-nivel.md §8).
- La pintura va fija por modelo. Repartiendo las variantes v0–v3 al azar, el verde y el ocre salen en 4 de cada 20 (Lucía: ≤ 20 %). El resto es gris, beige o blanco. No hay negro, azul ni rojo.
- Banda de la horda (L* 9–13): 0 % en el LOD1 de las 25. Sustituye a sagunto/coche_2000, que llevaba 283440. La ambulancia sigue como estaba.
- **Dónde van:** se lo he pedido a Álvaro, con posición, yaw, tipo y variante. Será el atasco con el carril norte abierto y el camión cruzado en cabeza, en el puente (C4 y C5, §10.6.5), y tres coches sobre el tablero del paso superior (cota 8,3 m), en Z 56, 66 y 74, con giros distintos (§10.6.8). La lista irá en este LEEME o en sagunto-nivel.md.
- Auditoría y presupuesto OK en las 50 mallas. Medidas SIN VERIFICAR, típicas de cada clase.

Código: TBD `claude/modelado-3d-skill`, 3c3aa94 y 0cdc40a (`bloques/coche_civil.py`, TBD_VARIANTE = 5 · tipo + variante).
