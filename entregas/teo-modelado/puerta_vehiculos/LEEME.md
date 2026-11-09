# Puerta de vehículos de Castellón (SM_PuertaVehiculos_Castellon_vN, D-N111) · Teo

> **9-nov: renombrada** de `SM_PuertaVehiculos_vN` a `SM_PuertaVehiculos_Castellon_vN` (Lucía), para que no se confunda con la puerta con estados de `muro-estados/puerta_vehiculos/` (`SM_PuertaVehiculos_v<n>_<Variante>_e<n>`). Las mallas son las mismas. En `castellon.json` la pieza es ahora `puerta_vehiculos/SM_PuertaVehiculos_Castellon`.

Para Iker. Aprobada por Lucía la madrugada del 7-nov. Son 5 variantes, v0–v4, en LOD0 y LOD1, y todas usan la misma `T_Paleta32.png`: un material URP/Lit con `_BaseMap` = paleta, como el kit.
- El origen está en el suelo y la puerta mira a +Z de Unity con yaw 0.
- Tiene dos hijos, `Hoja_E` y `Hoja_O`, que son las dos hojas para abrir y cerrar. Cuelgan directamente de la raíz.
- La colocación va en `docs/niveles/estaciones/castellon.json`, de Álvaro.
