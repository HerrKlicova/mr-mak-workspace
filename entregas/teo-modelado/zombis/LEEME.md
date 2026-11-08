# Zombis de la horda: 16 siluetas (D-N80, bloque B1). Teo, 8-nov. Aprobado por Lucía (17:59).

`SM_ZombiFino_v<n>_<Nombre>_LOD0/1.fbx`, con la misma `T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Origen en el suelo, entre los pies. Delante = −Y de Blender = +Z de Unity con yaw 0. Alto 1,75 m (Bajo: 1,60 m; Reptante: 0,45 m).

| v | Nombre | Qué cambia en la silueta |
|---|---|---|
| 0 | Base | Brazos al frente, desparejos |
| 1 | Mochila | Mochila a la espalda |
| 2 | Gorra | Gorra con visera |
| 3 | Chaqueta | Faldones abiertos que ensanchan la cadera |
| 4 | Falda | Falda o vestido hasta la rodilla |
| 5 | BrazoCaido | Un brazo a lo largo del cuerpo |
| 6 | Corpulento | La malla gruesa |
| 7 | Bajo | 1,60 m y algo más ancho |
| 8 | Capucha | Sudadera con la capucha puesta |
| 9 | Abrigo | Abrigo largo hasta la rodilla |
| 10 | Casco | Casco redondo y chaleco abultado (tiñe con el pantalón, no se lee como uniforme propio) |
| 11 | Bolsa | Bolsa colgando de la mano del brazo caído |
| 12 | Cojo | Ladeado 9°, arrastrando una pierna |
| 13 | Reptante | Se arrastra con los brazos (mismo radio e impacto en NightSim: solo cambia la malla) |
| 14 | Anciano | Muy encorvado, con bastón |
| 15 | Sombrero | Labrador de la huerta con sombrero de ala ancha |

**Color por instancia (D-N80, Bruno).** Máscara en el color de vértice: R = camisa y brazos, G = pantalón **y los objetos** (falda, mochila, gorra, casco, bolsa, bastón, sombrero), B = cabeza y manos; el calzado, a 0. Los tintes salen de `horda_paleta.json` de Bruno (banda L* 9–13). Los objetos ya no se quedan en 442c0c: de noche se fundían con el suelo.

**Medida de noche** (`horda_noche_b1.png`, 70 zombis, suelo a L* ≈ 25): mediana L* 11,3, p90 13,4, nada por encima de L* 20, contraste suelo p10 − horda p90 = 9,4 (Sara pide ≥ 8). La última palabra la da la -capdirecta de la build.

**Instanciado (Marcos):** probar con las 16. Si pesa, quedarse con v0, 1, 3, 4, 6, 7, 9, 13, 14 y 15. Escala ±5 % por instancia, como hasta ahora. Nada de niños.
