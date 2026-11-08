# Estado de los hilos

Última actualización: **lunes 9-nov, 00:40 (Madrid)**, hecha por Elena (Crónica) a partir de los hilos del proyecto y de la memoria del proyecto. La foto es de la noche del 8 al 9 de noviembre: Eugenio duerme y el equipo sigue trabajando con su permiso («sí, tenéis mi permiso para todo», 08-11 21:13 Madrid).

**Sobre el modelo:** desde la nube solo puedo comprobar el modelo de mi propio hilo (Opus 5.5). Los demás hilos de la nube usan el valor por defecto del proyecto, que es el mismo, pero eso no lo he podido verificar. Marcos, Iker y Paula trabajan con Remote Control en el PC de Eugenio, y el modelo de esas sesiones no se ve desde aquí. El esfuerzo que aparece es el que pide cada rol.

| Miembro | Hilo | Modelo y esfuerzo | Por qué | Objetivo | Estado | Pendientes | Preguntas sin responder |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Lucía** | Lucía · Diseño del juego (3) | Opus 5.5, alto | Toma decisiones de diseño (D-N), lleva el GDD y prioriza el MVP | Diseño, GDD, tablón del MVP; asigna las tareas libres | Terminado por ahora. Tablón v18: 8 mecánicas hechas, 23 en build y 11 pendientes de 42. D-N179 cerrada (Nules hay que ganárselo) | Revisar los puntos de boca de Teo. Recibir de Marcos la lista de la Noche69. Escribir su relevo. La siguiente D-N libre es D-N180 | Ninguna para Eugenio |
| **Marcos** | Marcos · Programación en Unity (por renovar) | Sin comprobar (Remote Control en el PC) | Programación de la zona y las builds en el editor de Unity | Zona, noche y builds | En curso. Arregla el turbo: hay que ordenar `_zomPos`, `_zomId` y `_tgt` por SimId, porque el SimHash se separa entre los ticks 1383 y 1790. Lanzando las semillas de la Noche75 | Comparar los hashes 9 de 9 (es condición de Lucía y Sara). Entregar a Lucía la lista de la Noche69. Después, el ambiente de Nules y el pueblo r2 con campanario. Hilo por renovar | Si su sesión de Remote Control se cae, solo Eugenio puede reabrirla (aviso para la mañana) |
| **Iker** | Iker · Programación de la red de estaciones (2) | Sin comprobar (Remote Control en el PC) | Programación de la red, el mapa, los trenes, el tutorial y la intro | Red de estaciones e integración de builds | En curso. Noche70 (3e265e2, 1258 pruebas) y Noche71 (cf4f0db, 0 errores, con existencias_red.json) entregadas. Integra la Noche72: D-N179, informe APP-6 y asedio de Nules | Corrida qa46 (semillas 1 a 5, con `-menu-auto`). Escribir su relevo. Dar a Eugenio los pasos de la regla de permisos para las capturas con GPU | **Eugenio:** añadir la regla en los ajustes de Claude Code para que se puedan hacer capturas con GPU |
| **Nacho** | Nacho · Hacer ganable la noche (3) | Opus 5.5, alto | Simulación determinista (NightSim, A*, C90); necesita rigor | Que la noche se pueda ganar y se pueda medir | Rama nacho/asedio-nules (1d426cf) entregada para la Noche72 | Bajas por u y por arma (200 semillas). Nules A/B/C. Apartadero de Nules con escolta de 8 y de 16. Medir el muro de Nules con Álvaro | Ninguna |
| **Hugo** | Hugo · Economía y balance (3) | Opus 5.5, alto | Modelos numéricos de economía y hordas | Balance de munición, víveres y hordas | En curso. Munición resuelta a las 00:22: el bonus del muro multiplicaba la eficacia de cada bala. Lo quita y recalibra H0, con el equilibrado entre el 13 y el 15 %. La build no se toca | Comprobar que Nules aguanta con 1 pelotón y 20 u (Nacho midió que se gastan 4 u y aguanta). Apartadero de Nules | Ninguna |
| **Sara** | Sara · QA (3) | Opus 5.5, alto | Las mediciones y los criterios de aceptación tienen que ser exactos | QA, mediciones y corridas | Esperando las corridas del PC (aparece como bloqueada). Pasada de la Noche70 con 14 comprobaciones | Leer qa46. Repetir la comparación del turbo 9 de 9. Informe. Escribir su relevo | Ninguna para Eugenio. Espera las corridas de Iker y Marcos |
| **Bruno** | Bruno · Arte técnico (3) | Opus 5.5, alto | Shaders, VFX y código de arte en ramas claude/* | Arte técnico, VFX e interfaz | En curso. Iconos APP-6 terminados (el pelotón lleva ●●, el amigo en slate) | Juntar en una rama los fogonazos, las trazadoras y los impactos de vehículos. D-N157: primera horda de día con 5 muestras de Sagunto de día y ΔL* ≥ 8. Hoja de noche D-N80 cuando lleguen las capturas de la Noche71. Desde la nube no puede subir PNG por LFS | Ninguna |
| **Teo** | Teo · Modelado 3D (relevo) | Opus 5.5, medio | Modelado 3D en FBX; no tiene acceso al PC | Modelos 3D | Puntos de boca entregados. Aparece como bloqueado: espera la revisión de Lucía | Lo que salga de esa revisión | Ninguna para Eugenio |
| **Álvaro** | Álvaro · Diseño de niveles (2) | Opus 5.5, alto | Diseño de niveles y medidas | Niveles y recintos | Sin tarea activa | Medir el muro de Nules con Nacho (el recinto mide 124,3 u) | Ninguna |
| **Paula** | Paula · Referencias reales (3) | Sin comprobar (Remote Control) | Busca referencias reales de material y vehículos | Referencias reales | Terminado: 21 símbolos APP-6 entregados. Hilo resuelto | Nada | Ninguna |
| **Nuria** | Sonido (2) | Opus 5.5, medio | Sonido con ElevenLabs v3; la clave va solo en variable de entorno | Sonido completo en 3D, con silencio al pausar | Terminado: sonidos de FARP, Nules y avisos entregados (4.924 créditos) | Nada asignado | Volumen de la bocina del tren: lleva tiempo sin respuesta. Puede decidirlo el equipo (Lucía) |
| **Elena** | Elena · Crónica del estudio (2) | Opus 5.5 (comprobado) | Redacción con citas literales; no hace falta más | Crónica del estudio | Crónica v25 publicada con el panel del MVP. Este documento | Siguiente capítulo: 66 | Ninguna |
| **Iris** | Iris · Herramientas de IA (por renovar) | Opus 5.5, medio | Herramientas de IA (PixelLab) | Generación con IA | **Bloqueada desde el 06-11** | Muestras de PixelLab el 09-11. **El saldo caduca el 17-11.** Hilo por renovar | Lo que la bloquea sigue sin respuesta; hay que revisarlo antes de que caduque el saldo |
| **Galería** | Galería · Capturas (14) | Opus 5.5, medio | Recopila y publica capturas | Galería de capturas para Eugenio | Esperando capturas nuevas (aparece como bloqueada). La página (9) tiene 44 imágenes | Añadir las capturas de la Noche71/72 cuando las haya (las de GPU dependen de la regla de permisos) | Ninguna |

## Avisos para la mañana (Eugenio)

1. Si se ha caído una sesión de Remote Control (Marcos o Iker), solo Eugenio puede reabrirla. Los relevos al día están en `docs/relevo/marcos.md` e `iker.md`.
2. La regla de permisos para las capturas con GPU sigue pendiente. Iker tiene los pasos.
3. El saldo de PixelLab de Iris caduca el 17-11.

---

## Historial (5-nov, hilos A y B)

Última actualización: **2026-11-05, ~15:30 UTC** (hilo de preparación). Este archivo vive en el repositorio de mr.mak;
la copia de la carpeta compartida del proyecto la mantiene el coordinador. Cuando difieran, manda la más reciente.

## Hilos

| Hilo | Modelo y esfuerzo | Por qué | Objetivo | Estado |
| --- | --- | --- | --- | --- |
| **A · Diseño** («Diseñar concepto del RTS zombi») | Opus 5.5, razonamiento alto | Diseño, arquitectura y decisiones difíciles | Investigación, conceptos, GDD y preguntas | **En curso.** GDD v1.0 cerrado con las respuestas de Eugenio y v1.1 preparado para cooperativo con lockstep determinista (sin paquetes de red; hito 7 tras el MVP). Falta revisar los resultados del piloto de Pixelab y recalcular el lote. |
| **B · Preparación** («Preparar entorno Unity y herramientas») | Sonnet 5.5, razonamiento alto | Sobre todo verificar documentación y probar herramientas en el PC | Guía de preparación y verificación de herramientas | **En curso.** Guía entregada y actualizada; piloto de Pixelab hecho; pruebas de Hunyuan hechas; tarjeta de mr.mak creada. Espera «guía completada» de Eugenio para crear el proyecto. |
| **Repaso de hilos** (rutina, 9:00, 15:00 y 21:00 Madrid) | — | Resumen solo si hay algo nuevo | Detectar pendientes y preguntas sin responder | Activa |

## Hecho en el hilo B hoy

- **Guía de preparación** (`docs/guia-preparacion.md`) con comprobaciones y marcas de verificación; `docs/unity.gitignore` listo.
- **ElevenLabs:** plan Pro desde el 5-nov. Imagen de prueba por API creada con `gpt-image-2.5-flare`.
- **Piloto de Pixelab:** 78 generaciones gastadas (saldo 8.747,05), 42 elementos. Resumen y costes medidos en la pestaña Arte de la tarjeta.
- **Hunyuan (3D):** prueba de punta a punta de 3 min 01 s, 40.000 caras. Prueba con More Views en curso.
- **Tarjeta de mr.mak:** `workspace/2026-11-05_rts-zombi/` (GDD, idea original, cambios, decisiones, investigación, arte, audio, herramientas, manifiesto de assets).

## Actualización ~15:30 UTC (hilo B)
- **Lote de Pixelab parado** por decisión de Eugenio. Gasto de hoy: 78 (piloto) + 89 (lote) = **167 generaciones**; saldo **8.658,05**. 69 iconos y 19 emblemas de mapa generados; 18 efectos VFX animados **gratis** con `vfx_workbench`. 11 trabajos enviados quedan sin descargar (anotados en `assets/pixelab/lote/estado.jsonl`).
- **Prototipo de zona escrito** en `C:\Dev\TBD` (commit `df5f7cf`, subido a `TBD`): horda en DOTS que se amontona y cae, tren, shader de pixelado con paleta de 32 colores, reglas de determinismo y prueba de desincronización con dos mundos. **No se ha compilado ni probado**: Unity necesita la licencia Personal activa.
- **Música de ElevenLabs:** verificado que el plan Pro permite uso comercial en un Indie Game (menos de 500.000 USD del juego y menos de 1.000.000 USD de la entidad); detalle en la guía, apartado 8.
- **Pendiente de Eugenio:** activar la licencia Personal y abrir `C:\Dev\TBD`; cambiar el `origin` de mr.mak (bloqueado por el sistema de permisos).

## Actualización ~16:00 UTC (hilo B)
- **Hilo nuevo, «Herramientas IA»** (terminado): sus conclusiones están en `docs/herramientas-ia.md`. Recomienda instalar el **plugin oficial de Unity para Claude Code** al abrir el proyecto y **probar la Unity CLI** junto a MCP for Unity; crear una skill propia de DOTS.
- **Licencia de Hunyuan:** el archivo de licencia local de Hunyuan3D 2.1 excluye la UE, el Reino Unido y Corea del Sur y prohíbe usar el resultado fuera del territorio (apartado 4c). **El addon usa los pesos en local**: la carga se hizo desde `D:D ENGINES\models	encent\...` y el motor trabaja sin conexión; no hay API de Tencent. Propuesta: TRELLIS.2 (README local: MIT). Pendiente de verificar por el Hilo A y de decisión de Eugenio (D-011).
- **Render en capas** del prototipo según `direccion-visual.md` (commit `fdff041` de `TBD`), sin compilar ni probar.

## Actualización 5-nov (hilo B): código adelantado sin Unity
- **Pruebas fuera de Unity** (`dotnet run -c Release --project Dotnet/TBD.Sim.Tests` en `C:\Dev\TBD`): **49 comprobaciones en verde**. Encontraron y corrigieron tres fallos de la simulación (oscilación de la pila, parpadeo caer/andar, deslizamiento sin apilar).
- **Índice espacial de sólidos** (cubetas de 4 m): mismo resultado que sin índice (20.000 muestras y hash idéntico en 300 ticks); 1,6 ms frente a 81 ms por tick con 307 sólidos. Commit `28124f4`.
- **Hito 2, lógica pura:** red de vías, trenes y alertas con orden estable y caminos deterministas (`Assets/TBD/Scripts/Net/RailNet.cs`). Longitudes de las vías **provisionales** (sin verificar). Commit `c46f9ee`.
- **Skill propia `tbd-dots`** (`.claude/skills/tbd-dots/SKILL.md`): versiones fijadas, API comprobada o no, trampas.
- **Guía de primera apertura** en `Docs/PRIMERA_APERTURA.md` de `TBD` (licencia, paquetes, MCP for Unity, plugin oficial de Unity: comandos sin verificar).
- **Sigue sin poder comprobarse sin el editor:** compilación en Unity, Burst determinista, prueba `F3`, rendimiento y render.

## Actualización 5-nov ~21:45 UTC (hilo B): primera ejecución en Unity
- **Unity 6000.3.28f1 abierto y funcionando.** Consola sin errores de compilación. Al pulsar Play salía en cada frame un error de ejecución: el búfer `PileRead` de `ZombieStepJob` usaba `Allocator.Temp`, y `IJobEntity.Run()` lo rechaza. Se cambió a `TempJob` (commit `87f3a5f` de `TBD`).
- **Medido en el editor:** 10.000 zombis a **198 FPS**. La prueba de desincronización da el mismo hash en los dos mundos. Captura: `workspace/2026-11-05_rts-zombi/assets/capturas/captura_20261105_223710.png`.
- **Primera apertura guardada** en el commit `9cdee58`: .meta, ProjectSettings, `packages-lock.json` y `ProjectVersion.txt`. El botón Configure de MCP for Unity sacó `unityMCP` del `.mcp.json` y lo registró en la configuración local de Claude Code para `C:\Dev\TBD`. Push hecho.
- **MCP for Unity desde otra carpeta:** una sesión abierta en mr.mak no ve las herramientas de `unityMCP`, pero puede usarlas por HTTP (`initialize` + `tools/call` en `http://localhost:8080/mcp`). Lo más cómodo es trabajar con sesiones abiertas en `C:\Dev\TBD`.
- **MCP de ElevenLabs:** funciona (plan Pro activo, consulta de suscripción correcta). La clave está en la variable de entorno de usuario `ELEVENLABS_API_KEY`. `.env` y `Assets/Audio/_raw/` están ignorados por git, y `git grep sk_` no encuentra nada.
- **Plugin oficial de Unity:** comandos comprobados en el README oficial. El sistema de permisos bloqueó su instalación porque integra código de terceros, así que la tiene que hacer Eugenio.
- **Paquetes resueltos** (packages-lock.json): Burst **1.8.31** (cumple ≥ 1.8.25), Entities 1.5.0, Entities Graphics 1.5.0, URP 17.3.0, MCP for Unity v10.3.0.
- **Sin comprobar todavía:** la prueba `F3` a mano y los fps en una build.

## Actualización 5-nov ~21:55 UTC (hilo B): plugin de Unity, skills de terceros y Unity CLI
- **Plugin oficial de Unity instalado** por Eugenio: `unity@unity-agent-plugin` 0.1.9-beta, en el ámbito del proyecto `C:\Dev\TBD` (activado en `.claude/settings.json`). Trae 33 skills. Ninguna es de DOTS. Incluye la skill `unity-cli`.
- **Skills de awesome-gamedev-agent-skills** (Apache-2.0) copiadas a `TBD/.claude/skills`: `save-systems`, `procedural-gen` y `performance-optimization`, con su `LICENSE`, su `NOTICE` y una cabecera de origen y modificación. No se usó su cargador. Cada una lleva «Notas para TBD (DOTS)» con lo que choca: `System.Random` (prohibido; se usa `Unity.Mathematics.Random`), el pooling de MonoBehaviour (no aplica a entidades) y el guardado (tiene que reproducir el hash). `tbd-dots` dice que manda sobre ellas y recoge la trampa de `Allocator.Temp`. Commit `03bc059`, subido.
- **Unity CLI: desaparcada.** No está instalada (`unity` no aparece en el PATH, aunque el PATH ya incluye `%LOCALAPPDATA%\Unity\bin`, que no existe). La instalación oficial descarga y ejecuta un script (`irm https://unity.com/install.ps1 | iex`), así que la lanza Eugenio. Para manejar el editor abierto, la CLI necesita además el paquete `com.unity.pipeline` en el proyecto (`unity pipeline install`; experimental). Plan: **MCP for Unity sigue siendo la vía principal y la CLI es complementaria.** Hay que probar las dos con la misma tarea antes de decidir más.

## Actualización 5-nov ~22:05 UTC (Marcos, Programación): Unity CLI y hito 1
- **Unity CLI 1.0.0-beta.16 conectada** al editor con `com.unity.pipeline` 0.10.0-exp.1 (experimental). Probada: Play y Stop, captura del Game view, consola, `script eval` (C# en el editor) y recompilación. Cada orden tarda menos de 2 s. Detalles prácticos:
  - `unity command editor.playmode set_run_in_background`: sin esto, el Play se congela con el editor en segundo plano.
  - Tras editar scripts desde fuera, `script recompile` contesta «no hace falta». Antes hay que refrescar los assets (por ejemplo con `refresh_unity` de MCP for Unity).
  - `unity recompile` devolvió HTTP 400.
  - Aviso «immutable packages altered» sobre archivos de `com.unity.pipeline`: viene del propio paquete, no se ha tocado.
  Reparto: **CLI para el día a día, MCP for Unity de respaldo.**
- **Hito 1 «Zona»:** la horda se amontona contra el muro (unos 1.700 apilados), se derrama, sube y cae del tejado. La prueba de desincronización es correcta. Rinde entre 164 y 222 FPS en el editor con 10.000-10.500 zombis.
  - **Fallo corregido:** los zombis iban en filas de uno porque no se separaban entre sí. Ahora hay separación por densidad del tick anterior: suma de enteros, determinista. Prueba nueva: de 1,38 a 1,22 zombis por celda ocupada, y el máximo baja de 9 a 4.
  - **Segundo arreglo:** un zombi ya no puede quedar dentro de un muro por debajo del escalón al subir por la pila.
  - **Pruebas:** 51 en verde. Commit `83a243a`, subido.
  - **Capturas** en `assets/capturas/`: `h1_zona.gif` y `h1_hoja.png`, que junta día y noche, una volea de noche y el pixelado 2, 3 y 4.
- **Falta para dar el hito por cerrado:** que Eugenio dé el visto bueno al aspecto. Lo que queda del render (contorno por profundidad, luz toon, corrección de subpíxel) espera a ese visto bueno.
- Los archivos de ejemplo de la plantilla (`Assets/Readme.asset`, `Assets/TutorialInfo/`) aparecen borrados en `TBD` sin commit. No los he tocado.

## Actualización 5-nov ~22:30 UTC (Marcos, Programación): hito 2 «Red», primera versión jugable
- **Escena `Assets/Scenes/Red.unity`** en `TBD`: mapa de operaciones en pixel art (textura de 224 × 180 ampliada sin suavizar). Muestra la red del MVP, la mancha de horda con tramado, los nodos con su estado (segura, amenazada, asediada), los trenes en movimiento, las alertas priorizadas, el panel del tren (horario y carga) y el reloj (día y hora).
  - Controles: Espacio pausa, 1/2/3 para x1/x2/x4, Tab cambia de tren, H retiene o suelta, F3 prueba de desincronización, F9 captura.
- **Simulación S0** (`Net/NetWorld.cs`), toda en enteros:
  - Reloj: 1 tick = 2,4 s de juego, así que un día dura 20 min reales a x1 (GDD §3).
  - Mancha de horda en una rejilla de 96 × 96: se difunde y deriva hacia lo que atrae a la Colmena (el tamaño de la ciudad más el ruido del tráfico, que se olvida poco a poco). Conserva la masa.
  - Nodos y vías salen de la mancha: una vía se corta con la horda encima y el tren se detiene y avisa.
  - 3 trenes con horario diario y carga de los 4 recursos (carga y descarga al salir de cada parada; capacidad de 400 t).
  - Velocidad, pausa y retener o soltar un tren son órdenes con tick (GDD §17.3, regla 9).
  - Hash y segundo mundo para la prueba de desincronización: correcta en el editor.
- **Pruebas:** 70 en verde (19 nuevas). Cubren la conservación de la masa, los horarios (06:00, llegada a las 06:30, salida a las 09:00), la carga sin pérdidas en dos días, la pausa y la velocidad, retener un tren, la vía cortada que genera aviso y el determinismo durante un día entero. Coste: 0,02 ms por tick. Commit `4e2bf7a`, subido.
- **Posiciones del mapa:** ahora salen de latitud y longitud aproximadas, de memoria y sin verificar. Las longitudes de las vías siguen siendo de ejemplo.
- **Capturas:** `assets/capturas/h2_red.gif` y `red_final.png`.
- **Limitaciones conocidas (prototipo):**
  - Valencia, Sagunto y el Puerto quedan muy juntos y sus etiquetas se pisan; el zoom llega en el hito 3.
  - El tiempo de las alertas («horda a 16 s») está en segundos reales a x1, no en tiempo de juego.
  - Hacia las 11:00 la mancha ya asedia cuatro nodos: el equilibrio está por ajustar.
  - Las vías cortadas se despejan solas cuando se va la horda (las obras llegan en el hito 5).
  - Falta el consumo de las unidades embarcadas.
- Sin commit en `TBD`, por si los tocó Eugenio: `Assets/Settings/*_RPAsset.asset`, `ProjectSettings/SceneTemplateSettings.json` y el borrado de los archivos de ejemplo de la plantilla.

## Actualización 5-nov ~22:45 UTC (Marcos, Programación): hito 2 aprobado y comienzo del hito 3
- **Eugenio aprueba el hito 2** (5-nov, 22:20). Requisito de arte que pidió: un mapa 3D con el relieve real. Lucía lo ha metido en el GDD §7 y en el hito 3 como versión funcional; el acabado artístico queda para el hito 7. **No se usan datos reales de elevación** hasta que Lucía confirme las licencias (IGN o Copernicus). Mientras tanto, relieve de sustitución detrás de una interfaz que luego se cambia por el modelo de elevación real.
- **Menos presión de la horda** (commit `81e90c0`): deriva 1/60, difusión 1/48, ruido del tráfico 70, asedio a partir de 500. Ahora hay una estación asediada a las 12:00 y dos o tres por la tarde; antes había cuatro antes de las 12:00. Hay una prueba que lo vigila (71 en verde).
- **Hito 3 «Unión», plan por partes:**
  1. Terreno compartido (una sola función de elevación para el mapa y la zona) y mapa 3D con la red encima.
  2. Zoom continuo del mapa a la zona, sin pantalla de carga.
  3. Materializar y desmaterializar la horda entre la capa S0 y la zona.
  4. Unidades embarcadas que desembarcan, combaten y gastan la carga del tren.

## Actualización 6-nov ~00:00 (hora de Madrid ~01:00), Marcos (Programación): noche del hito 3
Todo subido a `TBD` y registrado en `docs/decisiones-noche.md` (N-001 a N-030). 109 pruebas en verde.
- **QA de Sara:** arreglados Q1 a Q5, Q8 y Q10 a Q13. Siguen abiertos Q6, Q7 y Q9 (prioridad baja).
- **Arte del H1 (revisión de Lucía):** horda oscura sobre suelo ocre, tejado de terracota, sol bajo y paleta al 65 % en el mundo 3D. Focos ámbar de noche con siluetas a contraluz. El contraste de día pasa la prueba de Sara.
- **Balance de Hugo en código:** lector CSV, combate S0, Colmena, memoria de tráfico, pila, viajes, producción y asalto a pie con tope por cadencia. Los casos P1a-f y P2 a P6 dan exacto y los esperados se leen del CSV.
- **Red canónica D-N14** y 8 puntos de emboscada revisados por Lucía.
- **Hito 3 «Unión»:**
  - Mapa 3D (escena `Union`) con relieve de sustitución detrás de `IElevationSource`.
  - Entrar y salir de una zona con zoom (2 / 2,5 km), con órdenes Materializar y Desmaterializar, celda congelada mientras dura la zona, fundido y vuelo de cámara. La red sigue corriendo en `NetSession`.
  - Tropas: el pelotón dispara desde el tren parado, que hace de muro móvil (D-N27), o va a pie. Munición en disparos equivalentes. P7 dentro del rango de Hugo.
- **Bloqueado:** la fase A de Pixelab y la prueba de ElevenLabs gastan créditos y el sistema de permisos exige el «sí» de Eugenio.

## Actualización 6-nov ~02:10 (hora de Madrid), Marcos (Programación): repetición dorada y Colmena
- **Vídeo del hito 3** (bucle completo, 44 s, sin trucos): `/mnt/project-files/h3_bucle-20261105T235927-e3ac.gif` y su hoja.
- **Repetición dorada** de G1 a G4 (zona, tropas, red y bucle): idéntica en el Editor, en una compilación Mono y en una compilación IL2CPP (`TBD.exe -batchmode -nographics -tbd-golden -tbd-golden-out resultado.txt`). Destapó y arregló un fallo real de determinismo entre Mono e IL2CPP, fuera de Burst. La zona exige Burst. Falta la prueba entre dos PC (necesita otra máquina).
- **Hito 4:** memoria de tráfico (D-N31: tope de 1.200, un paso por tren, tramo, franja y día, olvido por debajo de 300) e informe de inteligencia con los textos de Lucía en el mapa 3D. Primer director de la Colmena: emboscadas, cortes y asedios reales desde el día 2, conservando la masa. 137 pruebas en verde.
- **Pendiente para Eugenio:**
  - Aprobar el gasto de la fase A de Pixelab (~450) y la prueba de ElevenLabs (~60).
  - Repetir la repetición dorada en su PC y, si hay otra máquina, en ella.
  - Registro en Copernicus (lo pidió Lucía).

## Pendiente

| # | Qué | Quién | Nota |
| --- | --- | --- | --- |
| 1 | ~~Confirmar la versión de Unity~~ **Hecho:** 6000.3.28f1 (6.3 LTS). Falta la licencia Personal (ver 4b) | Eugenio | Comprobado en el disco |
| 2 | ~~Decir «guía completada»~~ **Hecho** (5-nov, «guía completada todo bien», «te autorizo a todo») | Eugenio | Desbloqueó la creación del proyecto |
| 3 | ~~Cambiar el `origin` de mr.mak~~ **Hecho** (comprobado el 5-nov a las 22:30: `origin` apunta a HerrKlicova/mr-mak-workspace y `upstream` a witnesstodark). Antes: Cambiar el `origin` de mr.mak a `https://github.com/HerrKlicova/mr-mak-workspace.git` (el sistema bloqueó dos veces al hilo B, incluso con la autorización de Eugenio) | Eugenio | Dos comandos en la guía (apartado 6); el repositorio existe y está vacío |
| 4 | ~~Primer commit y push del juego a `TBD`~~ **Hecho** (commit `0726f9f`, 5-nov) | Hilo B | Proyecto en `C:\Dev\TBD`, sin abrir en Unity todavía |
| 4b | ~~Activar la licencia~~ **Hecho** (5-nov, primera ejecución a 198 FPS). Antes: **Activar la licencia Unity Personal en el Hub** y abrir `C:\Dev\TBD` con 6000.3.28f1 (descarga de paquetes, comprobar Burst ≥ 1.8.25, MCP for Unity «Connected») | Eugenio | El editor en línea de comandos respondió «No valid Unity Editor license found» (0 licencias) |
| 5 | Aprobar o ajustar el estilo del piloto de Pixelab | Eugenio | Antes de lanzar el lote (antes del 12-nov) |
| 6 | Recalcular el lote de Pixelab con los costes medidos | Hilo A | Costes en la pestaña Arte |
| 7 | ~~Comprobar Burst~~ **Hecho:** 1.8.31 | Hilo B / Eugenio | No se puede hasta abrir el proyecto en Unity (necesita licencia) |
| 8 | ~~Documentar el flujo de More Views~~ **Hecho** (guía, apartado 10; tarjeta, pestaña Arte) | Hilo B | |
| 9 | ~~Instalar el plugin oficial de Unity~~ **Hecho** (0.1.9-beta, ámbito de proyecto). Antes: (`/plugin marketplace add Unity-Technologies/unity-agent-plugin` y `/plugin install unity@unity-agent-plugin`) | Eugenio | El sistema de permisos bloquea la instalación a Claude |
| 10 | ~~Hacer push de `TBD`~~ **Hecho** (hasta `9cdee58`) | Hilo B | |
| 11 | ~~Instalar la Unity CLI~~ **Hecho** (1.0.0-beta.16 + `com.unity.pipeline`). Antes:: `irm https://unity.com/install.ps1 \| iex` en PowerShell; después, en `C:\Dev\TBD`: `unity pipeline install` | Eugenio (instalación) y hilo B (paquete y prueba) | Experimental; complementaria a MCP for Unity |
| 12 | Dar el visto bueno al aspecto del hito 1 (GIF y hoja de capturas: día y noche, pixelado 2, 3 y 4) | Eugenio | Cierra el hito 1 |
| 13 | ~~Probar la escena Red~~ **Hecho:** visto bueno (5-nov). Antes: Probar la escena Red y decir si el mapa de operaciones va por buen camino (lectura, ritmo y presión de la horda) | Eugenio | Hito 2 |

## Actualización 6-nov ~04:00 (hora de Madrid), Marcos (Programación): H4 completo hasta el desmonte jugable
- **Director (D-N32 a D-N39)**: asedio por calendario con aviso de 3 h y respiro, sorteo por peso², presupuesto del modelo de Hugo (curva, huella, rampa, estación y ruido, enteros), masa inyectada por los bordes y retirada a los 6 días, horda inicial con correa (≤1.500 ‰ a tiro de la vía). Total de 20 semillas dentro del 0,3 % de la referencia de Hugo. 173 pruebas dotnet.
- **Emboscada materializada**: encuentro en la red (`Encounter`, `ResolveAmbush`), zona de 256 × 128 m, **desmonte jugable** (tapón, taludes con caídas, marcha atrás, Z/X/C), verificado en el Editor y en GIF (`emboscada_desmonte.gif`). Goldens G1 a G5 idénticos en el Editor.
- **Deuda (no es de esta noche)**: H5/H7 arte del desmonte: sombra y fondo oscuro para que se lea como trinchera, talud continuo (MDT o degradado), contraste de valor del tren (D-N13), talud de un solo tono · curva y puente con su propia disposición · H6 columna de migración en el borde · H7 hash del balance al conectar en coop y rechazo sin Burst · tropa a pie que sale como guarnición · estacionalidad y MDT reales (Copernicus pendiente de Eugenio) · seguimiento de combate por celda para la retirada · «hoy» de la atención a las 05:30.

## Preguntas respondidas por Eugenio (5-nov, «respondo lo que tú recomiendas»)
Unity 6.3 LTS y no la 6.6 · comparar GPT Image 2.5 y Nano Banana Pro con el mismo prompt cuando haya concepto · estilo del piloto de Pixelab (aprobar retratos y personaje, repetir mapa y VFX cuando se retome) · CLI de Unity más adelante, no ahora · zombi 3D desde la base de Kenney.

## Preguntas sin responder para Eugenio

| # | Pregunta | Recomendación |
| --- | --- | --- |
| 1 | ¿Confirmas **no usar Unity 6.6** (Update release, sin soporte largo) y quedarte con la 6.3 LTS? (D-006) | Sí, quedarse con la 6.3 LTS |
| 2 | ¿Qué modelo de imagen usamos para referencias: **GPT Image 2.5** o **Nano Banana Pro**? (D-003). Ambos existen en la API de ElevenLabs. | Probar los dos con una imagen del concepto elegido y quedarse con el que respete mejor el estilo |
| 3 | ¿Apruebas el estilo del piloto de Pixelab? | Aprobar los retratos y el personaje; rehacer fichas del mapa y VFX con instrucciones más estrictas |
| 4 | ¿Quieres probar la **CLI de Unity** más adelante? | No ahora: es experimental; MCP for Unity primero |

## Marcos (Programación) · pausa 6-nov ~11:25
- Estado: sin builds ni capturas lanzadas (Eugenio juega). Último commit en C:\Dev\TBD (rama main, pusheado) con PR #7–#9, #12 y #14 de Nacho integrados, PuertaVia dibujada, LOD de masa y sombra de horda (D-N61), trinchera por bandas.
- La build de Builds\Prototipo NO incluye el último commit (trinchera por bandas, PuertaVia, #12/#14): rehacer al volver.
- Pendiente: medir en captura normal la horda densa (escena 777: dense.cs en scratchpad) y las 4 bandas; cuerpo LOD ≤19 y mancha ΔL* ≥25 sin verificar; si falla, LOD fuera del post.
- Pendiente: dibujar muerte del zombi y oficial (atlas ya importados), Dragón v5 LOD0/LOD1 + AssetPostprocessor (tbd_rim), contorno interior solo con saltos de profundidad, BLENDER_PATH, solape de iconos de estación en el mapa, G1–G5 y 382 pruebas tras la última integración.
