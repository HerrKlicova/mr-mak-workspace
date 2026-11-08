# Edificio de viajeros de Sagunt, como el real (Teo, 8-nov). Aprobado por Lucía (18:18).

Sustituye al sólido `edificio_viajeros` (sagunto-nivel.md §10.15, Álvaro; fotos SG1/SG2 y sagunto_azotea.md de Paula). `SM_EdificioViajerosSagunto_v<n>_<Estado>_LOD0/1.fbx`, con `T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Medidas SIN VERIFICAR (Nacho va a medir).

- **Planta de 32 × 9 m.** El cuerpo central tiene 14 m y 2 plantas, con el alero a 9,5 m, teja a cuatro aguas y un frontón con óculo en cada fachada larga (la punta llega a 11,4 m). Las dos alas son de 9 × 9 m, con **azotea a 4,75 m** y balaustrada de 1 m en el propio modelo; no es muro: no tiene vida ni coste (Hugo). No hay escalera exterior: se sube por dentro, por una puerta en la primera planta del central hacia cada azotea.
- **Origen** en el centro de la planta, en el suelo. La fachada del andén está en −Y (y = −4,5). **Va en (99; 0; 76,3) con yaw 180**, con la fachada del andén al sur, pegada al andén (Z 71,8). Las alas ocupan x −16..−7 y 7..16. Con yaw 180, la de +x local cae al **oeste** (X 83–92), donde van los tiradores. **Marcos: compruébalo en la exportación**; si la X sale espejada, cambia el yaw.
- **Estados (D-N124)**: v0 Abandonada, v1 Segura (sacos sobre la balaustrada oeste, solo a la vista), v2 EnLiberacion, v3 Caida (un tramo de balaustrada caído, tejas arrancadas y hollín), v4 Liberada (andamio).
- **Colores**: paredes f0dc9c; pilastras, zócalo, imposta y recercados 7c181c (8c5048 en el LOD1); balaustrada b8b8b8; azotea 94948c; teja a86c50; carpintería 6c4038. Banda de la horda: 0,0–0,4 %.
- **Anulados**: el pretil de sacos y la escalera de `azotea-sagunto/` (14:37) ya no se usan.
