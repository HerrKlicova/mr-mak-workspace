# Coches civiles abandonados: atasco de la carretera vieja y paso superior de Sagunto · Teo, 8-nov

Para Marcos, a través de Mak. Corresponde a los puntos 6 y 9 de la revisión de la Noche57 de Álvaro (`docs/niveles/revision-noche57-guia.md`). **Aprobado por Lucía (8-nov, 13:09)** con dos cambios, ya hechos: la lona del camión pasa a beige o gris, porque en verde se leía como militar, y el óxido del quemado va en manchas, no en un cuadrado. Hoja: /mnt/project-files/docs/arte/modelado-3d/coches-civiles/hoja_coches_civiles.png.

- `SM_CocheCivil_<Tipo>_v<V>_LOD0/LOD1.fbx`, con la `T_Paleta32.png` de siempre.
- Tipos: **Utilitario** 3,8 m, **Berlina** 4,5 m, **Furgoneta** 4,8 m, **Todoterreno** 4,4 m y **Camion** 6,6 m (cabina y caja de lona).
- Variantes: v0 intacto, v1 con la puerta del conductor abierta, v2 pinchado y ladeado, v3 accidentado (morro hundido) y v4 quemado (sobre las llantas).
- Delante es −Y de Blender, que en Unity es +Z con yaw 0. El origen está en el suelo, en el centro. **Sin colisión** en el MVP (sagunto-nivel.md §8).
- La pintura va fija por modelo. Repartiendo las variantes v0–v3 al azar, el verde y el ocre salen en 4 de cada 20 (Lucía: ≤ 20 %). El resto es gris, beige o blanco. No hay negro, azul ni rojo.
- Banda de la horda (L* 9–13): 0 % en el LOD1 de las 25. Sustituye a sagunto/coche_2000, que llevaba 283440. La ambulancia sigue como estaba.
- **Dónde van:** lista de Álvaro en `docs/niveles/sagunto_coches_v1.csv` (30 filas: grupo, tipo, variante, x, y, z y yaw; morro a +Z con yaw 0; explicada en sagunto-nivel.md §10.12). Son 11 coches en el tramo abierto (X 64–200), 15 en el cerrado (X 206–250), el Camion v3 cruzado en cabeza en (258; 0; 23) con yaw 78, y 3 en el paso superior a y = 8,3 m. Todos los tipos y variantes del CSV existen en el kit. Con ese reparto, el verde y el ocre son 3 de 30 (10 %).
- Auditoría y presupuesto OK en las 50 mallas. Medidas SIN VERIFICAR, típicas de cada clase.

Código: TBD `claude/modelado-3d-skill`, 3c3aa94 y 0cdc40a (`bloques/coche_civil.py`, TBD_VARIANTE = 5 · tipo + variante).
