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

## 12-11, 03:15 · Marcos (2) · A definitiva cerrada
- Mundo18 (marcos/mundo-zum d9e3bab3): A a 28 500 ticks. H2, H3 y H4 dan desync=False en 28 501 ticks. Todo está en docs/capturas/hito1/Mundo18/ (NOTAS.txt).
- El guion lleva el pelotón de Nacho (guion_peloton_A.txt) y los 106/107 en la vuelta tras la primera entrega: 6000, 6100, 6200 y re-trazado A→P en el 7800. Para moverlos sin recompilar está -red-ticks.
- La reproducción sale sola en el último tick de la referencia. -trenlog da tren, carga, almacenes, munición y abatidos, y al salir los zombis vivos.
- Vista: el montón de palés en el suelo, el aviso de material y la placa del caserío, que hoy cuenta los vivos. Nacho expone ZombisQuedan y OleadaFinal: cambiar a eso.
- Pendiente: gamma de Bruno a 1800 m. Pasar H3_camara.png a la galería (a través del coordinador).

## 12-11, 05:40 · Marcos (2) · partidas a mano y vista
- Partidas a mano en verde: Mundo21 (larga, 41 714 ticks) y Mundo25 (corta, 26 683 ticks). Capturas en docs/capturas/hito1/Mundo21_a_mano, Mundo25_corta y Mundo26_27.
- Ratón sintético: scratchpad/ventana.ps1 (Mov2 = SetCursorPos + un mouse_event relativo, para que el Input System vea el movimiento; arrastrar/presionar/camino/soltar; vkext para Supr). Helpers en scratchpad/m26/f.sh (qa = tecla K → Captures/qa_pantalla.txt con píxeles de los puntos de qa_puntos.txt).
- Vista (marcos/mundo-zum 8a425736): P pausa, L línea, Supr borra tramo, munición por soldado y aviso de seco, placa del almacén (D-N210; textos de Iker en Red.ExistenciasAlmacen/TendenciaAlmacen), zum al cursor y aviso de punto inalcanzable (D-N211), mensajes encima del panel de la línea, HUD con fondo, -fpslog con el peor fotograma.
- Rendimiento (Mundo27, camguion): peor media de 375 fps; peor fotograma 34,5 ms.
- Pendiente: «Lleno» en la placa de B (D-N211 c), cuando Iker tenga la capacidad del almacén. El hilo ha llegado a 24 adjuntos.
