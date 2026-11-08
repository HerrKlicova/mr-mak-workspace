# Kit de huerta de Nules (Teo, 8-nov). Aprobado por Lucía (18:49).

`T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Banda de la horda: 0 % en las 25 piezas. Sin rojo ni ámbar. El agua va
en 6c7874 (no hay azul permitido). Medidas DE MEMORIA (SIN VERIFICAR). Origen en el suelo, en el centro de la pieza.
Sirve también para la huerta de Sagunto, con los naranjos.

| Pieza | Variantes v0–v4 | Medidas | Colisión y visión (Lucía) |
|---|---|---|---|
| `SM_CasetaPozo` | Encalada, Ladrillo, Motor (bajo tejadillo, +X), Abandonada, Deposito (elevado, +X) | 3 × 3 × 2,6 m; puerta a −Y | **Sólida y tapa la visión** |
| `SM_Tapia` | Encalada, Ladrillo, Bloque (con malla), Derrumbada (hueco en x −1,5…1,2), Porton (hueco de 2,8 m en el centro) | Módulo de 10 m a lo largo de X, 1,6 m de alto | **Sólida y tapa la visión**, salvo el hueco de Derrumbada y el portón abierto |
| `SM_Balsa` | Llena, Media, Vacia, Escalerilla (con caseta de bomba en −X), Rota | 8 × 6 m, muro de 1 m | **Frena el paso, pero no tapa la visión** (es un hueco con agua; solo taparía si el muro pasara de 1 m). La caseta de bomba de la v3 sí es sólida |
| `SM_Acequia` | Agua, Seca, Compuerta, Pasarela, Cegada | Tramo de 10 m a lo largo de X, cauce de 0,8 m | No tapa la visión. Si frena el paso, lo decide Álvaro |
| `SM_CasetaAperos` | Chapa, Madera, Ladrillo, Remolque (de palots, +X), Abandonada | 4 × 3 × 2,3 m, abierta a −Y | **Sólida y tapa la visión** |

Para Álvaro: añadir las sólidas al CSV de obstáculos de Nules. Una tapia entre los naranjos cambia de verdad el combate.
