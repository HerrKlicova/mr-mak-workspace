# Fondo de la intro «Día 41» (D-N158, variante C). Bruno (Arte técnico), 8-nov

Para Iker. Copiar `Assets/TBD/Resources/Intro/` (con `fondo_intro.png`, su .meta y `Intro.meta`) al proyecto, desde el Editor o con Unity cerrado. IntroVista (c6df090) ya lo carga con `Resources.Load<Texture2D>("Intro/fondo_intro")` y ScaleAndCrop, así que no hay que tocar código.

- 1920x1080, hecho a 640x360 en la paleta de 32 y ampliado x3 por vecino más próximo. El .meta va en Point, sin mipmaps y sin compresión, para que no se emborrone.
- Variante entregada: **A, «La ciudad apagada»**: el perfil de una ciudad sin una luz, con tres columnas de humo, el cerro del castillo a la derecha y el tren con el faro como única luz que se mueve. Encaja con las tarjetas 2 y 3 («las ciudades cayeron», «lo único que todavía se mueve es el tren»).
- **Hueco para la letra nueva** (más gruesa, de máquina de escribir): la banda de y 22–76 % y x 8–92 % es navy casi liso. Todo el detalle va arriba (estrellas y luna) o abajo (horizonte a y 77 %). El hueso d4d0cc sobre navy da unos 11:1 de contraste. La muestra con la letra de prueba (FreeMono Bold de 54 px a 1080p) está en `muestra/intro_fondo_?_texto.png`.
- Muestra de 5 (A–E) en `muestra/intro_fondo_hoja.png`: B catenaria, C Sagunto desde fuera, D el faro que se acerca y E andén vacío. Para cambiar de variante: `python build_intro.py <carpeta> --var C` (necesita pixelvm y build_menu de la skill pixel-art-codigo).
- Sin 1c200c ni 442c0c (son de la horda), sin ámbar y sin rojo.
