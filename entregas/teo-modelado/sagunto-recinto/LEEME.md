# Recinto de Sagunto con el kit de defensas · Teo, 9-nov

Encargo de Lucía (9-nov): la lista de colocación de Sagunto en el formato de `RecintoPlan`. HESCO al oeste y en las alas, sacos en el resto, y las 4 puertas. **Pendiente de la revisión de Álvaro antes de pasarla a Marcos.**

![plano](plano_sagunto_recinto.png)

## Archivos
- `sagunto_recinto.json`: el recinto, el material de cada lado, las 4 puertas y las 34 piezas. Cada pieza lleva los campos de `PiezaMuro` (malla, x, z, yaw, largo, escala_x, espejo) y su `ruta` en `Assets/TBD/Resources/Models/`.
- `sagunto_piezas.csv`: lo mismo, una pieza por fila. Los números son los del plano.
- `codigo/`: `plan.py` es una copia en Python de `RecintoPlan.Plan` (rama `marcos/noche-prototipo`) con las dos mejoras de abajo, y `driver.py` saca la lista (`python3 driver.py salida.json`; con `--literal` sale lo que haría el código de hoy).

## De dónde sale
- Recinto: X 70–156, Z 44–85 (`docs/niveles/sagunto_obstaculos_v1.csv`). HESCO de 2,1 m en el muro oeste y en las alas hasta X 84,5; sacos de 1,2 m en el resto. Las piezas van sobre los mismos ejes y con las mismas alturas que los sólidos del CSV.
- Variante de cada pieza: la del código, `EstacionDato.VariantOf(x, z, 5)`. Todas en estado e0 Sano.
- Puertas (CSV y `sagunto-nivel.md` §10.8–10.9, confirmadas por Álvaro):

| Puerta | Posición, giro | Hueco libre | Hueco en el muro (con jambas de 0,9 m) | Malla |
|---|---|---|---|---|
| Vía oeste | (70; 64,5), yaw 270 | Z 62–67 (5 m, D-N151) | Z 61,1–67,9 | `Defensas/puerta_via/SM_PuertaVia_v1_ChapaOndulada` |
| Vía este | (156; 64,5), yaw 90 | Z 62–67, solo visual y cerrada en el MVP | Z 61,1–67,9 | `Defensas/puerta_via/SM_PuertaVia_v4_Blindada` |
| Vehículos sur (E4) | (99; 44), yaw 180 | X 95–103 | X 94,1–103,9 | `Defensas/muro/SM_PuertaVehiculos_v2_Tablones` |
| Vehículos oeste-sur | (70; 53), yaw 270 | Z 49–57 | Z 48,1–57,9 | `Defensas/muro/SM_PuertaVehiculos_v0_TuboChapa` |

Cada puerta lleva su colisión de `Defensas/colision/` (IMPORTAR-NOCHE). La Z de la puerta este está **SIN VERIFICAR** (la doy igual que la oeste, como el CSV).

## Lo que cambia respecto a `RecintoPlan` tal cual
1. **El muro se corta por fuera de las jambas**, no por el hueco libre. Las jambas quedan por fuera de los 5 m y de los 8 m (`puerta-via/LEEME.md`), y si el remate empieza en el borde del hueco, se mete 0,9 m en la jamba. *Marcos: en Nules el JSON da el hueco libre (`hueco_z` 60,8–68,2); allí los remates pisan las jambas.*
2. **Trozos cortos de HESCO.** En el muro oeste quedan dos trozos donde no caben dos remates: 3,2 m entre las dos puertas (Z 57,9–61,1) y 1,3 m entre la esquina y la puerta de vehículos (Z 46,8–48,1). El código pondría remates solapados; aquí van un `HescoCorto3` (pieza 32) y un `HescoCorto1` (pieza 33).
3. **El resto se centra.** En HESCO, un solo corto centrado en el resto (prefiero que solape unos centímetros a que quede un agujero de 0,4 m). En sacos, cada trozo se reparte en tramos iguales, con escala de 0,71 a 1,16, y no un tramo aplastado a 0,16 al final.

## Para importar
- Las 34 piezas y las puertas ya están en Unity o van en IMPORTAR-NOCHE, **menos `SM_SacosRemateEspejo`** (2 piezas: 3 y 15), que no está en Unity. Hay que copiar los 40 FBX de `entregas/teo-modelado/defensas/sacos/SM_SacosRemateEspejo_*` a `Assets/TBD/Resources/Models/Defensas/sacos/`.
- Las piezas con `espejo: true` ya llevan el nombre de la malla espejada; no hay que escalarlas a −1.

## Para la revisión de Álvaro
- Los muros siguen los ejes y las alturas de los sólidos de hoy, así que las líneas de tiro no deberían cambiar. Lo único nuevo que abulta son la celda de vuelta de los remates (1,1 m hacia dentro, junto a las jambas) y las hojas de las puertas de vehículos, que abren hacia dentro.
- **Posible choque:** la hoja norte de la puerta de vehículos oeste-sur gira sobre Z 57 y, abierta, llega hasta X ≈ 74. El nido sur está en X 72,7–74,3, Z 57,0–58,0: la hoja abierta lo roza.
- En X 84,5 el HESCO (2,1 m) se junta con los sacos (1,2 m) sin pieza de transición, como ya está en el CSV.
- El poste de catenaria suelto junto al tren (qa47): por ver con Álvaro. Si en ese tramo no hay catenaria, se quita.

— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)
