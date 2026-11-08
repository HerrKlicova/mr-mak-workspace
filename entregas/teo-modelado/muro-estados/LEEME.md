# Estados del muro: sacos, HESCO y puerta de vehículos (D-N163 §1) · Teo, 8-nov

Para Iker y Marcos. Siguen la muestra de Álvaro (236586a), que Lucía aprobó con los cambios de los sacos. **Pendiente de la revisión de Lucía sobre el modelo.** Hojas: /mnt/project-files/docs/arte/modelado-3d/muro-estados/.

Cada pieza tiene 5 variantes y 4 estados, en LOD0 y LOD1, con el nombre `SM_<Pieza>_v<V>_<Variante>_e<E>_<Estado>_LODn.fbx`. Los estados son e0 Sano (≥ 70 %), e1 Danado (30–70 %), e2 MuyDanado (1–30 %) y e3 Brecha (0: escombro que no bloquea).
- Todas usan la misma `T_Paleta32.png`: un material URP/Lit con `_BaseMap` = paleta, como el kit.
- El origen está en el suelo, en el centro de la pieza. El muro va a lo largo de X local, y **fuera (por donde llega la horda) es −Y de Blender, que en Unity es +Z con yaw 0**. Lo que se cae, cae hacia fuera.

## sacos/ · SM_MuroSacos (tramo de 8 m)
- **El tramo mide 8 m** (x −4..4), como en la muestra, y sustituye a dos módulos de 4 m de muro_sacos. Repítelo cada 8 m: n = round(L / 8) tramos, escalados en X a L / n. Tiene 1,0 m de grueso.
- Colores: sacos 605c48, reventados y escombro 48403c, arena b4a080, sacos claros de la v2 847c34, tablón de la v3 a86c50 y red de la v4 303424.
- Variantes:
  - v0 Recto, de 4 hiladas (1,2 m).
  - v1 Talud, de 5 hiladas, cada una 0,5 m más corta por cada punta.
  - v2 Irregular, de 0,9 a 1,8 m, con dos aspilleras en la 4.ª hilada. **Lo que pasa de 1,2 m es solo silueta: en el juego el tramo cuenta como 1,2 m** (Lucía, D-N163).
  - v3 Tablon y v4 Red.
- Los muro_sacos v0–v4 anteriores (de 4 m, con el estado de reparación) siguen valiendo; la v0 de aquí es su equivalente de 8 m con el color nuevo.

## hesco/ · SM_MuroHesco (módulo de 10 m, 2,1 m de alto)
- Tiene 9 celdas de 1,11 m y 1,1 m de fondo.
- Colores: HESCO 70784c (geotextil 50541c), malla b8b8b8 y relleno b4a080.
- Variantes:
  - v0 MallaLimpia
  - v1 Geotextil
  - v2 Escalonado: celdas de 2,1 y 1,4 m alternas.
  - v3 RemateSacos: celdas de 1,8 m con sacos encima.
  - v4 Red

## puerta_vehiculos/ · SM_PuertaVehiculos (8 m, dos hojas)
- Es la misma puerta de la D-N111, con las **mismas jerarquía y bisagras**: `Hoja_O` y `Hoja_E`, con el origen en su bisagra. El código de apertura no cambia.
- En la brecha, las hojas solo conservan las bisagras arrancadas; los trozos están por el suelo, en la parte fija.
- Los colores de la D-N163 son chapa 94948c, malla b8b8b8, tablones a86c50, sacos de las jambas 605c48 y el boquete 48403c.
- La e0 de cada variante equivale a la puerta_vehiculos/ de la D-N111 con estos colores.

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de las 60 piezas, sin ningún aviso.
- SIN VERIFICAR: las medidas son de memoria; la forma de los sacos sale de la foto K3_control_1 de Paula.

Código: TBD `claude/modelado-3d-skill`, c7efa71 (`bloques/muro_sacos_estados.py`, `muro_hesco_estados.py` y `puerta_estados.py`).
