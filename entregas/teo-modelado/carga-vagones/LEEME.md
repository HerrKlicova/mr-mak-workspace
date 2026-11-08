# Carga visible en los vagones (Teo, 8-nov). Aprobado por Lucía (18:32).

`T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Banda de la horda: 0 % en las 20 piezas. Sin rojo ni ámbar. Medidas
SIN VERIFICAR.

`SM_Carga<Recurso>_<Estado>_LOD0/1`, con Recurso = Municion, Combustible, Materiales o Viveres, y Estado = Lleno, Mitad,
Vacio, Danado o Destrozado.

- **Dónde va:** encima del tablero de la plataforma Rgs (18,5 × 2,9 m, a 1,25 m del carril). Ocupa 18,2 × 2,7 m y mide
  1,6 m como mucho. Origen: centro del tablero a la cota de su cara de arriba. En Unity: hijo del vagón en (0; 1,25; 0),
  sin giro (largo a lo largo del vagón). Los estados comparten origen: para cambiar el llenado basta con cambiar la malla.
- **Regla de llenado (Lucía):** Lleno a partir de 2/3 de la capacidad, Mitad a partir de 1/3, y Vacío por debajo.
  Danado y Destrozado, cuando el tren recibe daño o ataque.
- **Destrozado** deja bultos en el suelo a los dos lados de la vía (hasta 3,7 m del eje y 1,25 m por debajo del origen).
- **Tropa:** no lleva módulo; es el vagón R2 que ya existe.
- **Contenido:** munición en cajas de 0,75 × 0,4 × 0,34 m (las del `rearme_set`), combustible en bidones de 200 l, materiales
  en tablones, HESCO plegado y sacos, y víveres en cajas de fruta (limones, en f0dc9c) y sacos de harina.
