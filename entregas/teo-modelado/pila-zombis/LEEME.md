# Pila de zombis contra el muro · Teo, 8-nov

Para Marcos (integración en la zona y NightSim), Nacho (umbrales) y Bruno (material). **Aprobado por Lucía (8-nov, 24:20), remates incluidos.** La hoja está en /mnt/project-files/docs/arte/modelado-3d/pila-zombis/hoja_pila_zombis.png.

A partir de 3 zombis por celda, las instancias sueltas pegadas al muro se sustituyen por una pieza de pila por celda, para que se lea como una masa y rinda.

## Celda (`celda/`)
- `SM_PilaZombi_Altura<1-5>_s<0-2>_LOD<0|1>.fbx`: 5 alturas × 3 semillas.
- Mide **0,5 m de ancho** (x −0,25..0,25), igual que la celda de Nacho. El origen está en el suelo, al pie de la cara de fuera del muro. El muro corre a lo largo de X y FUERA es −Y de Blender (−Z en Unity con yaw 0), como en muro-estados.
- La altura depende del número de zombis por celda (umbrales de Nacho; lo que manda es el número, no los metros):

| Zombis por celda | Pieza | Alto contra el muro | Rampa hasta |
|---|---|---|---|
| < 3 | zombis sueltos | — | — |
| 3 | Altura1 | 1,05 m | 1,62 m |
| 4 | Altura2 | 1,4 m | 2,16 m |
| 5 | Altura3 | 1,75 m | 2,69 m |
| 6 | Altura4 | 2,1 m (a ras del HESCO; empiezan a trepar) | 3,23 m |
| 7 o más | Altura5 | 2,45 m, con una cresta de 0,6 m sobre la coronación | 3,77 m |

- Para que no parpadee (Nacho): la pila vuelve a zombis sueltos solo cuando baja de 2 por celda, y cambia de altura como mucho una vez por segundo.
- La semilla se elige por el índice de la celda (`s = índice % 3`), para que la misma malla no se repita cada 0,5 m.
- Los cuerpos se salen 0,2 m por cada lado, así que las celdas vecinas se funden en un solo tramo aunque tengan alturas distintas.

## Remates (`remate/`)
- `SM_PilaZombi_RemateDer_…` y `SM_PilaZombi_RemateIzq_…`, con las mismas alturas y semillas. Son las piezas que cierran cada extremo de un tramo, para que no se vea la cara lisa de la cuña.
- El RemateDer se coloca con su origen en el borde +X de la última celda (x de la celda + 0,25) y baja hacia +X. El RemateIzq va en el borde −X de la primera celda y baja hacia −X. Se usa la altura y la semilla de la celda del extremo. No hace falta escala negativa.
- Bajan a 40° hacia fuera, así que ocupan de 1,25 m (Altura1) a 2,92 m (Altura5) más allá del extremo.

## Colisión (`colision/`)
- `SM_PilaZombi_Altura<n>_COL.fbx`: una cuña lisa de 0,5 m con el perfil de la celda (rampa de 33° y la cresta en la Altura5), con objeto UCX_. `SM_PilaZombi_Remate{Der,Izq}_Altura<n>_COL.fbx`: el casco convexo del remate.
- La rampa es para que trepen por ella. Nacho: en NightSim, la pila crece por número de zombis por celda (pegados si están a menos de 1,5 m, PileRadiusMm), así que la cuña solo cuenta para lo visual y la física de la zona.

## Material (Bruno, TBD/Horda)
- La misma máscara de color de vértice «Col» que los zombis de la D-N80: R = camisa y brazos; G = pantalón y objetos; B = piel; negro = calzado.
- **El núcleo de la cuña va en negro (1c200c fijo).** Teñido por instancia, cada celda salía de un color y la pila se veía a rayas.
- **Alfa por cuerpo**: cada trozo de cuerpo lleva su semilla de tono en el alfa de «Col» (254, 253…; 255 en el núcleo). TBD/Horda (47ac1ed / 697282c) la usa para desplazar camisa, pantalón y piel dentro de la LUT, así que en una misma pieza hay cuerpos de varios tonos. Al importar, el alfa no debe forzarse a 1.

## Comprobado
- Son trozos de las cinco siluetas de la D-N80 (torsos, brazos y piernas cruzados, cabezas, el ala del sombrero, el casco) y algunos brazos que asoman hacia arriba en la parte alta. No hay ninguna figura entera. Sin gore.
- Banda: en un tramo con remates y el tinte de Bruno, del 62 al 67 % de los píxeles de pila queda en L* 9–13; el resto es el sombreado del render (L* 9,0–13,9). Sin rojo ni ámbar.
- Auditoría OK en LOD0 y LOD1 de las 45 piezas (15 celdas y 30 remates), sin aristas no-manifold. Triángulos en LOD1: de 120 a 304 por celda y como máximo 378 por remate.

Código: TBD `claude/modelado-3d-skill`, `bloques/pila_zombis.py` (b8c8850). Render de prueba: /mnt/project-files/docs/arte/modelado-3d/pila-zombis/pila_noche.py.
