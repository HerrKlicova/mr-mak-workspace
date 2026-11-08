# Mobiliario urbano para la plaza de Castellón y la calle de la estación de Nules (Teo, 8-nov). Aprobado por Lucía (18:52).

`T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Banda de la horda: 0 % en las 25 piezas. Sin rojo ni ámbar: las señales
tienen la cara en b8b8b8 con el borde en 6c7874 y se leen por la forma; los semáforos van apagados. Medidas DE MEMORIA
(SIN VERIFICAR). Origen en el suelo, en el centro de la pieza, con el frente a −Y. Completa `nules/urbano` (palmera,
farola y banco).

| Pieza | Variantes v0–v4 | Medidas | Colisión y visión (Lucía) |
|---|---|---|---|
| `SM_Contenedor` | Verde, Abierto (gris), Reciclaje (crema), Volcado (con bolsas a −Y), Fila (tres) | 1,4 × 1,0 × 1,3 m | Sin colisión |
| `SM_ParadaBus` | Entera, SinCristales, Anuncio (panel en +X), Refugio (bolsas y mantas), Caida | 4,2 × 1,6 × 2,6 m | **No tapa la vista.** Colisión solo en el banco y los postes, como obstáculo bajo. Excepción: en `Anuncio`, el panel sí tapa |
| `SM_Quiosco` | Cerrado, Abierto (toldo), Loteria (más bajo), Saqueado, Quemado | 2,4 × 2,4 × 2,6 m | **Sólido y tapa la vista** |
| `SM_Senal` | Direccion, Redonda, Triangular, Doble, Doblada | Poste de 2,6 m | Sin colisión |
| `SM_Semaforo` | Simple, Brazo (de 4 m hacia −X, sobre la calzada), Peatonal, Doblado, Caido | Poste de 3,2 m | Sin colisión |
