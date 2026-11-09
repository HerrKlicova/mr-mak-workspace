# Trazas de derrotas (Noche82, difícil) · Marcos (2), 9-nov

Son las trazas que piden Nacho y Hugo: la build es la Noche82 (TBD 6401db8, la combinada, SIN el rodeo del edificio) y se corrieron con `-batchmode -nographics -menu-auto -nightbot -dificultad dificil -semilla N -turbo 4`.
Cada fila es una muestra por tick con `_fullTrace`: estacion_hp, tren_hp, muro_hp, pila (pila del muro), atacan_tren (_nearTrain), atacan_estacion (_pileNearStation), abatidos, bajas, trepan y entradas por lado.

| Archivo | Resultado |
|---|---|
| noche82_dificil_s1.csv | derrota, causa=estacion, 4216 abatidos, 20 bajas, 6,1 u gastadas |
| noche82_dificil_s12.csv | derrota, causa=estacion, 4423 abatidos, 14 bajas, 6,9 u |
| noche82_dificil_s14.csv | derrota, causa=estacion, 4926 abatidos, 16 bajas, 7,0 u |

La causa (atascos detrás del edificio y cuelas por su colisión) está explicada en el relevo de Marcos; el arreglo va en la rama marcos/rodeo-edificio de TBD.
