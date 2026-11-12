# Relevo de Marcos · Hito 1 (núcleo v2)
Actualizado: 12-11, 00:10.
- **Rama:** TBD `marcos/mundo-zum` (sale de iker/f1-aire d98b4ea2). Último commit: ver `git log -1 origin/marcos/mundo-zum`.
- **Qué hay:** escena `Assets/Scenes/Mundo.unity` + `Assets/TBD/Scripts/Mundo/MundoBootstrap.cs`; se lanza con `TBD.exe -mundo` (MainMenu salta a la escena). Build de prueba: `C:\Dev\TBD\Builds\Mundo3`. Compilar en batch: `Unity.exe -batchmode -projectPath C:\Dev\TBD -executeMethod TBD.EditorTools.MundoEscena.CrearYCompilar -quit` (variable TBD_MUNDO_BUILD = destino).
- **Hecho:** zum continuo de 6 a 4000 m (umbrales de Bruno), perspectiva a baja resolución (pixel art), terreno de Álvaro (alturas 2049 → mallas de 128 m a paso 2 m; usos → textura de 1 m con grano), estaciones A y B, caserío (cajas de los 13 edificios), 1800 naranjos, 100 zombis y pelotón de relleno; iconos por encima de 250 m; norte arriba por encima de 900 m. Controles: rueda o Z/X zum, WASD, Q/E girar, F ir al pelotón, clic dcho mandar.
- **Ojo:** el Terrain de Unity sale MAGENTA en la build (no entra su shader): por eso el terreno son mallas.
- **Hecho también:** la vista lee el Mundo de Nacho (MundoVista.cs; merge de nacho/hito1), -hashlog, -grabar, -reproducir, -relleno. Sin compilar en Unity (turno de Iker).
- **Siguiente:** (1) compilar y probar con ventana la vista con la simulación; (2) trazado de vía con el ratón; (3) conectar los shaders de Bruno cuando los suba (no escribirlos: los hace él); (4) sonido de Nuria (nuria/sonido-hito1).

## 12-11, 02:50 · Marcos (2)
- marcos/mundo-zum 161cb89f contiene: iker dbb03ed8/382dd9a5 (coste de vía, 19 palés en A), nacho e97a27be (palés del caserío), mis -trenlog, -red-ticks y la salida automática de -reproducir.
- Ojo: TBD_MUNDO_BUILD debe ser la ruta del EXE (…/MundoN/TBD.exe). Si pones solo la carpeta, la build cae suelta en Builds/.
- Guion (MundoVista.Guion): A→P→B con los puntos de Iker. 106 a las 2300 se rechaza con el tren encima ✓, 106 a las 2410 se acepta y el tren para en P ✓, 107 a las 2500 ✓, re-trazado P→B a las 3700 ✓.
- Bloqueo: el caserío no queda limpio (73–89 de 100), porque la munición limita. Sin limpiar no salen los palés de Nacho y no llega material a A. He preguntado a Nacho, Hugo y Sara (opciones 1–3); pendiente de su respuesta antes de grabar la A definitiva y repetir H2–H4.
- H2 contra la A provisional de Mundo13: desync=False en 18 301 ticks. Mundo12 y Mundo13 dan el mismo hash final (1f80b73817d0704c).
