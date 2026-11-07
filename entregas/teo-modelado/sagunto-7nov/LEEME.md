# Sagunto, marquesina y poste de catenaria: notas de Lucía (D-N123), 7-nov

Teo para Marcos. Sustituyen a los FBX de la estación que tienes en `herramientas\modelado-3d\sagunto\marquesina\` y `...\poste_catenaria\`. Tienen los mismos nombres y la misma estructura: copia las dos carpetas encima de las de allí. El edificio de viajeros no cambia.

- **Marquesina (v0 a v5)**: en el LOD1, la cubierta lleva tres bandas de chapa a lo largo de la pieza, de 1 m (2 px o más también a tamaño de juego), en lugar del damero de 1 px. En el LOD1, los pilares y las cerchas pasan a 70784c y el canalón a 605c48, porque su cara en sombra caía a L* 19 (D-N80). El LOD0 no cambia.
- **Poste de catenaria (v0 a v5)**: en el LOD0, el hilo cortado ahora cuelga de la punta de la ménsula. Antes salía flotando, separado del poste, por un fallo de lado en el código. Es un solo tramo de 2 px y se quita el tramo diagonal suelto. En la v4, el hilo llega al suelo, también a 2 px. El LOD1 no cambia.
- Cada carpeta lleva su T_Paleta32.png, que es la misma de siempre. Importa con Normals = Import, como antes (NORMALES_ARRIBA).
- Comprobación: las 24 pasadas del pipeline dan OK y ninguna vista de juego del LOD1 tiene nada con L* < 20 (48 de 48).
