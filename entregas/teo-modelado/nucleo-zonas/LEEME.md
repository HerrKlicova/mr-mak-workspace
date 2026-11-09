# Núcleo: hangar de Bétera en el que se entra y acopios de carga de las estaciones (Teo, 9-nov, noche)

Son los modelos para el bucle de Eugenio del 9-nov 21:59: entras en la zona, seleccionas helicópteros o el tren con lo que
vas a cargar, sales con la rueda al mapa y haces clic derecho en el destino. También sirven para la persistencia: lo que
hay en la zona se ve. Los dos llevan `T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta), 5 variantes y LOD0/LOD1. La banda
de la horda queda al 0 %: no hay rojo, ámbar ni d4d0cc. Medidas SIN VERIFICAR. Exportado con `--costado 88885c --claro b8b8b8`.

## 1. `hangar_abierto/` → Resources/Models/Betera/hangar_abierto

`SM_HangarAbierto_v<n>_<Uso>`: Taller, Almacen, Refugio, Castigado, Fortificado. Es el hangar de `betera/hangar`
(40 × 25 m, muros de 8,5 m, clave a 12 m y hueco de 32 × 8 m), pero hueco por dentro y amueblado. Va en el mismo sitio de
`betera_instancias.csv` (SM_Hangar en X 90 y 160, Z 40; portón a +Z, hacia la plataforma). El hangar cerrado sigue sirviendo
para el panel y para las vistas lejanas.

**Jerarquía:** la raíz contiene los muros, el suelo y el interior, y tiene tres hijos:
- `Cubierta`: la bóveda (o las dos aguas), los nervios y la red. Su origen está a 8,5 m. **La vista la apaga, o la funde,
  al entrar en el hangar o al acercar la cámara**, para que se vean los NH90 desde arriba. Encendida, el hangar se ve como
  el cerrado.
- `Porton_O` y `Porton_E`: se entregan **abiertos**, con las hojas corridas 16 m hacia fuera. Para cerrar, cada hoja se
  traslada 16 m hacia el centro en X local. En hangar.py es al revés, porque aquel se entrega cerrado.

**Puestos de los NH90**, en coordenadas locales de Unity con yaw 0: (−10; 0; +1) y (+10; 0; +1), con el morro a +Z, hacia
el portón. Cada puesto tiene un círculo de 8,2 m de radio y su eje pintados en b8b8b8 fino. Los puestos están libres en
las cinco variantes, porque el mobiliario va pegado al fondo y a los costados. Los helicópteros son las unidades del juego
(`Vehiculos/nh90`), no van en el modelo: así se pueden seleccionar y sacar.

| v | Uso | Nave | Interior |
|---|---|---|---|
| 0 | Taller | bóveda | bancos, estanterías, carros y plataformas de mantenimiento |
| 1 | Almacen | bóveda | palés de cajas de munición, bidones y un contenedor de 20' |
| 2 | Refugio | dos aguas | literas, mesas y colchonetas |
| 3 | Castigado | bóveda con chapas arrancadas | chapas caídas y estanterías volcadas |
| 4 | Fortificado | bóveda con red | sacos a los lados del portón, por dentro y por fuera, y cajas |

![sin cubierta](hangar_abierto/hoja_sin_cubierta.png)

*v0 a v4 sin la cubierta y, abajo a la derecha, v0 con ella (render del script, no de Unity).*

## 2. `acopio_carga/` → Resources/Models/Acopios (o junto a `Nules/acopio_viveres`)

`SM_Acopio<Recurso>_v<n>_<Estado>`, con Recurso = Municion, Combustible o Materiales (los de `TrenPreparar.Recurso`, aparte
de los víveres) y Estado = Lleno, Mitad, Vacio, Saqueado o Quemado. **Misma huella (10 × 6 m), mismo origen y misma regla
que `AcopioViveres`**: Lleno desde 2/3 de la capacidad de referencia, Mitad desde 1/3, Vacío por debajo, Saqueado si la
estación cae y Quemado si arde. Así, `AcopioViveres.Estado()` sirve para los cuatro cambiando solo el nombre del fichero.
Están pensados para el patio o el andén de carga de cada estación: al elegir la carga, el jugador ve cuánto hay, y al
volver encuentra lo que dejó.

- Munición: palés de cajas en 70784c con flejes.
- Combustible: bidones de 200 l y depósitos GRG (IBC) en jaula.
- Materiales: fardos de gaviones plegados, sacos terreros, tablones y rollos de concertina.
- En el estado Vacío quedan palés apilados y un resto que dice qué había.

![acopios](acopio_carga/hoja.png)

*Filas: munición, combustible y materiales. Columnas: Lleno, Mitad, Vacío, Saqueado y Quemado.*

Bloques: `hangar_abierto.py` y `acopio_carga.py` del skill modelado-3d (TBD, rama `claude/modelado-3d-skill`).

## Tabla de colores por celda (leída de los UV, colores_uv.py)

Es la primera entrega de estos modelos, así que no hay entrega anterior con la que comparar. Ninguna celda cae en la banda
ni en los colores reservados (283440, 303424, 1c200c, 543820, 48403c, 442c0c, 50541c, 982420, e08c30, d4d0cc). En el hangar,
la tabla va por objeto (RAIZ, Cubierta y portones).

| Modelo | LOD | Celda y vértices |
|---|---|---|
| SM_HangarAbierto_v0_Taller | LOD0 | Cubierta: 88885c 686, 94948c 98; Porton_E: 605c48 120, 6c7874 24; Porton_O: 605c48 120, 6c7874 24; RAIZ: 6c7874 720, 70784c 696, b8b8b8 432, 845c28 96, 94948c 72, 605c48 72 |
| SM_HangarAbierto_v0_Taller | LOD1 | Cubierta: 88885c 232, 94948c 58; Porton_E: 605c48 72, 6c7874 24; Porton_O: 605c48 72, 6c7874 24; RAIZ: 6c7874 432, b8b8b8 240, 70784c 232, 845c28 96, 94948c 72, 605c48 72 |
| SM_HangarAbierto_v1_Almacen | LOD0 | Cubierta: 88885c 686, 94948c 98; Porton_E: 605c48 120, 6c7874 24; Porton_O: 605c48 120, 6c7874 24; RAIZ: 70784c 1808, 605c48 1008, b8b8b8 432, 845c28 384, 94948c 72 |
| SM_HangarAbierto_v1_Almacen | LOD1 | Cubierta: 88885c 232, 94948c 58; Porton_E: 605c48 72, 6c7874 24; Porton_O: 605c48 72, 6c7874 24; RAIZ: 70784c 1408, 845c28 384, b8b8b8 240, 94948c 72, 605c48 72 |
| SM_HangarAbierto_v2_Refugio | LOD0 | Cubierta: 88885c 266, 94948c 38; Porton_E: 605c48 120, 6c7874 24; Porton_O: 605c48 120, 6c7874 24; RAIZ: 6c7874 1776, b4a080 720, b8b8b8 432, 70784c 172, 94948c 72, 605c48 72, 845c28 48 |
| SM_HangarAbierto_v2_Refugio | LOD1 | Cubierta: 88885c 152, 94948c 38; Porton_E: 605c48 72, 6c7874 24; Porton_O: 605c48 72, 6c7874 24; RAIZ: b4a080 720, 6c7874 624, b8b8b8 240, 70784c 172, 94948c 72, 605c48 72, 845c28 48 |
| SM_HangarAbierto_v3_Castigado | LOD0 | Cubierta: 88885c 490, 94948c 98, 605c48 72; Porton_E: 605c48 120, 6c7874 24; Porton_O: 605c48 120, 6c7874 24; RAIZ: 70784c 552, b8b8b8 432, 94948c 168, 605c48 96, 6c7874 72, 845c28 24 |
| SM_HangarAbierto_v3_Castigado | LOD1 | Cubierta: 88885c 116, 605c48 72, 94948c 58; Porton_E: 605c48 72, 6c7874 24; Porton_O: 605c48 72, 6c7874 24; RAIZ: 70784c 328, b8b8b8 240, 94948c 168, 605c48 72, 6c7874 72, 845c28 24 |
| SM_HangarAbierto_v4_Fortificado | LOD0 | Cubierta: 88885c 806, 94948c 98; Porton_E: 605c48 120, 6c7874 24; Porton_O: 605c48 120, 6c7874 24; RAIZ: 605c48 1032, 70784c 456, b8b8b8 432, 845c28 144, 94948c 72 |
| SM_HangarAbierto_v4_Fortificado | LOD1 | Cubierta: 88885c 352, 94948c 58; Porton_E: 605c48 72, 6c7874 24; Porton_O: 605c48 72, 6c7874 24; RAIZ: 70784c 376, b8b8b8 240, 605c48 216, 845c28 144, 94948c 72 |
| SM_AcopioMunicion_v0_Lleno | LOD0 | 70784c 2592, b4a080 432, 605c48 432 |
| SM_AcopioMunicion_v0_Lleno | LOD1 | b4a080 432, 70784c 432 |
| SM_AcopioMunicion_v1_Mitad | LOD0 | 70784c 1056, b4a080 504, 605c48 216 |
| SM_AcopioMunicion_v1_Mitad | LOD1 | b4a080 348, 70784c 216 |
| SM_AcopioMunicion_v2_Vacio | LOD0 | b4a080 576, 70784c 144 |
| SM_AcopioMunicion_v2_Vacio | LOD1 | b4a080 264, 70784c 72 |
| SM_AcopioMunicion_v3_Saqueado | LOD0 | 70784c 1200, b4a080 312, 605c48 144 |
| SM_AcopioMunicion_v3_Saqueado | LOD1 | b4a080 312, 70784c 312 |
| SM_AcopioMunicion_v4_Quemado | LOD0 | 605c48 1656 |
| SM_AcopioMunicion_v4_Quemado | LOD1 | 605c48 688 |
| SM_AcopioCombustible_v0_Lleno | LOD0 | 6c7874 6336, 88885c 2112, 94948c 576, b4a080 432, b8b8b8 144 |
| SM_AcopioCombustible_v0_Lleno | LOD1 | 88885c 1152, 6c7874 1152, b4a080 432, b8b8b8 144, 94948c 144 |
| SM_AcopioCombustible_v1_Mitad | LOD0 | 6c7874 3168, 88885c 1056, b4a080 504, 94948c 288, b8b8b8 72 |
| SM_AcopioCombustible_v1_Mitad | LOD1 | 88885c 576, 6c7874 576, b4a080 348, b8b8b8 72, 94948c 72 |
| SM_AcopioCombustible_v2_Vacio | LOD0 | b4a080 576, 88885c 204 |
| SM_AcopioCombustible_v2_Vacio | LOD1 | b4a080 264, 88885c 144 |
| SM_AcopioCombustible_v3_Saqueado | LOD0 | 6c7874 1584, 88885c 1004, b4a080 312, 94948c 288, b8b8b8 72 |
| SM_AcopioCombustible_v3_Saqueado | LOD1 | 88885c 624, b4a080 312, 6c7874 288, b8b8b8 72, 94948c 72 |
| SM_AcopioCombustible_v4_Quemado | LOD0 | 605c48 4080 |
| SM_AcopioCombustible_v4_Quemado | LOD1 | 605c48 2416 |
| SM_AcopioMateriales_v0_Lleno | LOD0 | 6c7874 1776, b4a080 552, 845c28 504, 88885c 144 |
| SM_AcopioMateriales_v0_Lleno | LOD1 | 6c7874 576, b4a080 552, 88885c 144, 845c28 144 |
| SM_AcopioMateriales_v1_Mitad | LOD0 | 6c7874 888, b4a080 564, 845c28 252, 88885c 72 |
| SM_AcopioMateriales_v1_Mitad | LOD1 | b4a080 408, 6c7874 288, 88885c 72, 845c28 72 |
| SM_AcopioMateriales_v2_Vacio | LOD0 | b4a080 648, 845c28 72 |
| SM_AcopioMateriales_v2_Vacio | LOD1 | b4a080 336, 845c28 72 |
| SM_AcopioMateriales_v3_Saqueado | LOD0 | b4a080 544, 845c28 420, 6c7874 416, 88885c 48 |
| SM_AcopioMateriales_v3_Saqueado | LOD1 | b4a080 544, 845c28 240, 6c7874 96, 88885c 48 |
| SM_AcopioMateriales_v4_Quemado | LOD0 | 605c48 1368 |
| SM_AcopioMateriales_v4_Quemado | LOD1 | 605c48 864 |