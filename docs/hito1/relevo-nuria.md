# Relevo de Nuria (Sonido) · Hito 1

Actualizado: 11-nov, 23:40.

## Hecho
- Tabla de evento → archivo: `docs/hito1/sonido-hito1.md` (también en mr-mak `docs/hito1/`).
- Rama de tbd `nuria/sonido-hito1`, solo audio: tren_salida y tren_llegada a −20,5 LUFS, ui_construir a −26,3 y ui_error a −24,3.
- Script de lo nuevo: mr-mak `herramientas/sonido/hito1_sonido.py`. Probado en seco, SIN VERIFICAR contra ElevenLabs.

## Falta
- Generar los 5 sonidos nuevos (via_tendido, via_tramo_hecho, tren_rodando, carga_material, sin_municion_clic), unos 820–1.640 créditos. Hace falta el sí de Eugenio. Funciona si la sesión del PC lo lanza con el «sí» de Eugenio escrito en el hilo (así fue con la puerta E4).
- Después: copiar `entregas/sonido-hito1/*.ogg` a `Assets/TBD/Resources/Audio` con su .meta (plantilla: sfx_ui_tecla_1.ogg.meta, con un guid nuevo) en la rama.
- Las llamadas del código las pone quien haga cada sistema (Iker, la red y los trenes; Marcos, el zum), siguiendo la tabla.

## Avisos
- Los avisos del juego viejo están congelados (rama nuria/avisos-pulido, ya en main).
- Medir los clips desde la nube: `git lfs pull --include=...` en tbd y ebur128 o pyloudnorm.
