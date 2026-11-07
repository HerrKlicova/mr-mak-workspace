# Interfaz v2, estilo 1 (elegido por Lucía, D-N147): medidas para UI Toolkit. Bruno (Arte técnico), 7-nov

Referencia: interfaz_v2_1_plano.png (1920×1080). Coordenadas en píxeles a 1080p; con otra resolución se escala todo por igual.
Los marcos no son imágenes: son fondo más borde en USS, así salen nítidos a cualquier escala.

## Colores
- fondo 181c30 al 85 % (alfa 217); tarjeta 202538 opaca; borde 1 px 353a55; texto hueso d4d0cc; texto secundario 94948c.
- selección: marco de 2 px en d4d0cc por fuera de la tarjeta. Aviso: borde de 2 px e08c30. Ataque: borde de 2 px 982420.
- barras: hueco 0c0e18; munición b4a080 (e08c30 por debajo del 25 %); blindaje 94948c.

## Zonas
- Franja inferior: y 940–1080, ancho completo, fondo 181c30 al 85 %, línea superior de 1 px en 353a55.
- Barra de atajos: y 924–940, x 316–1590, fondo 0c0e18 con alfa 170, texto de 11 px en 94948c, centrado.
- Tarjetas: 8 de 152×128, en y 946, desde x 316, con 8 px de separación. Teclas: 1–5 pelotones y 6–8 vehículos.
  - Pelotón: tecla en una caja de 18×18 (6,6) con fondo 0c0e18, borde 353a55 y texto Bold de 13; nombre SemiBold de 14 en (30,7);
    icono de formación de 12 px en (CW−18, 9); 8 siluetas de 10×20 en (8 + k·17, 32); «Munición» de 11 px en (8,60) y el % a la derecha;
    barra de 5 px de alto en (8,76) y ancho 136; estado SemiBold de 13 en (8,104) («Sin munición» en ámbar).
  - Vehículo: tecla y nombre igual; silueta lateral centrada en y 30; «Blindaje» y «Munición» en y 56 y 78, cada uno con una barra de 4 px 15 px más abajo; estado en (8,104).
- Recursos: x 24 + i·70, icono de 16 px a 2x en y 990, número Bold de 15 en (+38, 994), etiqueta de 10 px en y 1030; título «Sagunto · almacén» de 11 px en (24,960).
- Minimapa: x 1604–1904, y 946–1074, fondo 283440 y borde de 1 px en 353a55.
- Órdenes: 2×2 botones de 146×30, en x 1604 / 1758 e y 870 / 904; icono de 16 px en (8,7); texto SemiBold de 13 en (32,7); tecla en una caja de 25×17 a la derecha.
  La orden activa lleva fondo 353a55 y borde d4d0cc. Encima va «Órdenes · <selección>», de 11 px, en y 850.
- Reloj: caja de 300×64 en x 810, y 10; anillo de 40 px (trazo de 4, hueco 353a55, progreso b4a080); «Noche · 22:34» Bold de 24; objetivo de 13 px en 94948c.
- Avisos: cajas de 340×38 en x 16, y 16 + i·44 (4 como mucho); icono de 16 px en (12,11); texto SemiBold de 14 en (38,10); los segundos que quedan, de 10 px, a la derecha.
- Pausa y velocidad: 1× y 2× de 40×30 en x 1720 / 1764, y 16; Menú (Esc) de 92×30 en x 1812.
- En el mundo: etiqueta «1 Fus» SemiBold de 9 px en hueso; flecha de borde de 14×16 con «4 Tir · 140 m» de 11 px.
- Tipografía: Inter (OFL), Medium, SemiBold y Bold. Hay que importarla en Unity.
