# Anillo que late del tutorial, estilo D (Lucía, 8-nov). Bruno (Arte técnico)

Para Iker. En `TutorialHud.cs` (iker/red-estaciones), sustituir el método `Ring(Rect r, float t)` por lo que hay en `TutorialHud.Ring_D.cs.txt` (Ring, Esquinas y Barra). No hace falta tocar nada más: usa `Bone` y `_white`, que ya existen, y la llamada de la línea ~349 se queda igual.

- Esquinas fijas en hueso d4d0cc (3u por fuera del objetivo, trazo de 1u y brazos de 4u; u = alto/360, es decir, 3 px a 1080p) y un eco de esquinas que sale de 4u a 11u y se apaga. Ciclo de 1,2 s. Sin rojo.
- Por qué esquinas: un marco hueso entero es como se ve una tarjeta seleccionada (D-N147). Con esquinas, «toca aquí» no se confunde con «ya está seleccionado».
- `FlechaBorde(objetivoEnPantalla, t, rotulo)` es opcional, para el capítulo 4: una cuña de 14x16 a 1080p en el borde cuando el objetivo no se ve.
- Referencia visual: /mnt/project-files/docs/arte/pixel-codigo/tutorial-obras/anillo_D.gif (la geometría es la misma). SIN COMPILAR: no tengo Unity aquí.
