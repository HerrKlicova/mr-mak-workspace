# Recinto de Nules con el kit de defensas, cortado por las jambas · Teo, 9-nov

Encargo de Lucía (9-nov). Es la lista de colocación de Nules con el muro cortado **por fuera de las jambas de 0,9 m** de cada puerta, igual que en Sagunto. Va primero porque Nules entra en juego la noche 2. **Pendiente de la revisión de Álvaro.**

![plano](plano_nules_recinto.png)

## Archivos
- `nules_recinto.json`: el recinto, el material de cada lado, las 4 puertas y las 43 piezas (campos de `PiezaMuro` y su `ruta` en `Models/`).
- `nules_piezas.csv`: una pieza por fila, con los números del plano.
- `codigo/`: `driver_nules.py` lee `estacion_nules.json` de `marcos/noche-prototipo` y hace lo mismo que `RecintoPlan.Nules()` (HESCO en el frente este y en alas de 15 m, sacos en el resto, el edificio como muro norte), con las reglas de abajo. Se ejecuta con `python3 driver_nules.py estacion_nules.json salida.json --mover-vehiculos`.

## Lo que no cambia
- **El coste.** `CosteLineal` se sigue calculando con el hueco libre de las puertas (`hueco_z` y `hueco_x` del JSON, que no cambio): 82,08 u de muro + 42 u de puertas = 124,08 u, lo mismo que da hoy el código (los 124,3 u de la D-N177). Para cortar las piezas añado `hueco_muro_z` y `hueco_muro_x` aparte, y el coste no los usa.
- **La D-N177.** Las puertas oeste (la doble y la del apartado) siguen en el mismo sitio y con el mismo hueco libre, así que no cambian las fracciones del apartado (25 %) ni de fuera de la puerta oeste (10 %).

## Lo que cambia
1. **Las piezas se cortan por fuera de las jambas**: Z 59,9–69,1 en las dos puertas dobles, Z 45,6–52,4 en la del apartado y X 176,32–186,12 en la de vehículos. Con el JSON de hoy, los remates pisan las jambas 0,9 m.
2. **Puerta de vehículos: propongo X 177,22–185,22** (la v0.2 de Álvaro, `nules-nivel.md` §3), en lugar de los 178–186 del JSON. Con 178–186, el brazo de 2,78 m de la esquina SE se mete 0,78 m dentro del hueco de 8 m. Con 177,22–185,22, el brazo acaba justo en el borde del hueco y la jamba este queda dentro del brazo, como dijo Álvaro. El hueco sigue midiendo 8 m, así que el coste no cambia. **Es un cambio de sólidos y de la simulación: lo decide Álvaro, con Marcos y Nacho.** El punto de bajada del vehículo, (184; 44,4), sigue dentro del hueco.
3. **El resto se reparte igual que en Sagunto.** En los sacos van tramos iguales (de escala 0,73 a 1,09) en vez de un tramo aplastado. En el HESCO va un corto centrado. Si la esquina ya cubre un trozo, no se pone nada.

## Para la revisión de Álvaro
- **Remates con vuelta.** Hay remates en las 8 jambas y en los 2 lados del edificio, con una celda de 1,1 m hacia dentro. En Sagunto los quitaste del muro oeste por la banqueta. En el JSON de Nules no hay banquetas, pero los muros oeste y este cruzan los andenes (Z 53,8–60,8 y 68,2–79,2): ¿estorban ahí las celdas de vuelta? Si estorban, los cierro con cortos, como en Sagunto.
- **Trozos cortos con solape (sacos, muro oeste).** Entre la esquina SO y la jamba del apartado (Z 40–45,6) el brazo de la esquina y el del remate se solapan 2,2 m. Entre la jamba norte del apartado y la sur de la doble (Z 52,4–59,9, 7,5 m) se solapan 0,3 m. Se ven como sacos amontonados y el muro queda cerrado. Si lo prefieres, se puede quitar el remate del trozo de la esquina.
- En X 173 el HESCO (2,1 m) se junta con los sacos (1,2 m) sin pieza de transición.

## Para importar
Necesita `SM_SacosRemateEspejo` (3 piezas), igual que Sagunto (IMPORTAR-NOCHE §5). Las puertas: `Nules/puerta_via_doble` (v4 Blindada en las dos), `Defensas/puerta_via` (v3 MallaEspino) y `Defensas/muro/SM_PuertaVehiculos` (v4 Blindada). Las variantes salen de `VariantOf` en la posición de cada puerta. Las colisiones están en `Defensas/colision/`.

— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)
