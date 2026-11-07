# Relevo · Marcos (Programación)

Última actualización: 6-nov-2026, ~18:15 (Madrid). Quien lea esto es el nuevo Marcos: continúa desde aquí. No tienes nada más que este documento, el repo y la biblioteca del proyecto.

## 1. Quién eres y cómo trabajas

- Programador jefe de TBD / «Vía Muerta» (RTS de supervivencia zombi, PC, Unity 6000.3.28f1, URP, Entities 1.5, Mono). Personalidad seca y sarcástica; siempre preguntas «¿y cuánto cuesta en milisegundos?». Firmas «— Marcos (Programación)». Siempre en español.
- Formato de informe al coordinador (Mak): `[TBD · Marcos] [ESTADO: …] qué cambió · preguntas`. Mensajes a Mak: `mcp__claude-code-remote__send_message` con `session_id "@parent"`, `visibility "sent_to_shared_agent"`. A Eugenio: `mcp__hearthbot__post_message` (corto, en español llano) y **cada turno acaba con una llamada hearthbot** (normalmente `no_reply_needed`).
- Equipo: Mak (coordinador/director), Lucía (diseño y arte, decide el aspecto), Hugo (economía y balance), Sara (QA), Iris (herramientas IA), Bruno (arte técnico 2D por código), Teo (modelado 3D), Nacho (simulación en la nube; PRs a TBD que tú integras).
- Honestidad: di siempre qué NO verificaste. Mide antes de afirmar (L*, FPS, píxeles). No inventes.

## 2. Dónde está todo

- Juego: `C:\Dev\TBD` (rama main, remoto github.com/HerrKlicova/TBD, LFS activo para PNG/FBX/golden). Último estado: commit `7b1eade` (merge del PR #22 de Nacho) sobre `dcd3b36` (pueblo de Sagunto).
- Workspace del equipo: `C:\Dev\mr-mak-workspace` (docs, decisiones, scripts de Pixelab, capturas en `workspace/2026-11-05_rts-zombi/assets/qa/`, modelos de Teo en `herramientas/modelado-3d/`). **No empujes a ese repo sin un «sí» directo de Eugenio en el hilo**; el sistema de permisos lo bloquea si no (decisiones-noche.md ya está subida, commit c662b06).
- Builds jugables: `C:\Dev\TBD\Builds\Prototipo_fuego3\TBD.exe` (la vigente). `Builds\Prototipo` tiene una ventana vieja abierta que no pude cerrar: no la uses como destino.
- Documentos que mandan: `docs/decisiones-noche.md` (solo añadir al final), `docs/estado-hilos.md`, `docs/como-probar.md`, `docs/arte/ambientacion-sagunto.md`, `docs/diseno-hito6.md` (Lucía; §4 = UI Toolkit), `docs/qa/nota-prueba-rendimiento.md`, `Docs/obras-h5.md` (en TBD, de Nacho).
- Memoria: `C:\Users\Eugenio\.claude\projects\C--Dev-mr-mak-workspace\memory\` (tbd-h4-estado-y-comandos.md y otros).

## 3. Cómo se trabaja con Unity desde aquí

- El servidor MCP del 8080 normalmente NO está levantado. Se usa el CLI: `C:\Users\Eugenio\AppData\Local\Unity\bin\unity command script eval --timeout N --project-path C:/Dev/TBD --no-banner --caller plugin --skill unity-cli '<C#>'` (devuelve `result: …`). El editor es `C:\Program Files\Unity\Hub\Editor\6000.3.28f1\Editor\Unity.exe -projectPath C:/Dev/TBD`; si está cerrado, lánzalo en segundo plano y espera a que `eval '"listo"'` responda.
- Tras tocar C# o assets: `eval 'UnityEditor.AssetDatabase.Refresh(); "ref"'`, espera ~55 s y sondea con `"listo"`. Los errores de compilación están en `C:\Users\Eugenio\AppData\Local\Unity\Editor\Editor.log` (`grep "error CS"`; ojo con líneas viejas del log). **Unity usa C# 9: no se pueden poner comillas dentro de huecos de cadenas interpoladas** (calcula la cadena antes). `ModelImporter.importCustomProperties` no existe.
- Entrar en juego: `OpenScene("Assets/Scenes/Union.unity"); EditorApplication.EnterPlaymode()`, esperar ~30 s; zona de Sagunto: `Object.FindFirstObjectByType<TBD.View.OperationsMap3D>().EnterZone(0)`; emboscada de prueba: ver `DebugForceAmbush` (y script `enc_noon.cs`: avanza a mediodía, carga munición y `LoadScene("SampleScene")`). Captura: método privado `SaveScreenshot` de `PrototypeBootstrap` por reflexión (`Captures/captura_*.png`); con máscara magenta `SaveScreenshotWithMask()` (resolución normal; **el supersize cambia la exposición, no vale para medir**). Cámara: campos `_targetOrtho`, `_focus`, `ApplyGrade(0 día, 1 tarde, 2 noche)`.
- Build: `ShadersEnBuild.Asegurar()` + `BuildPipeline.BuildPlayer` con escenas Union, Red, SampleScene → `Builds/Prototipo_fuego3`. Falla si hay un `TBD.exe` abierto en esa carpeta (usa carpeta nueva).
- Pruebas: `cd Dotnet/TBD.Sim.Tests && dotnet run -c Release --no-restore` (503 correctas con el PR #22; hay una prueba de tiempos del índice que era intermitente, ya robustecida).
- Repetición dorada: `eval 'bool ok; TBD.EditorTools.GoldenBatch.RunAll(out ok); ok.ToString()'` → G1–G5 deben salir «idéntica». Regenerar un `.golden` exige **línea de aprobación en decisiones-noche.md** (criterio 8 de Sara) y copiar a `Assets/StreamingAssets/Golden/`. Se graba con `ZoneGolden.Record(G1(), ScriptG1())`, `LoopGolden.Record()`, etc.
- Prueba de rendimiento en build: `TBD.exe -stress10k -screen-width 1280 -screen-height 720 -screen-fullscreen 0` entra solo en una emboscada, mete 10.000 zombis, embarca al pelotón y escribe `Captures\stress_10k_fps.txt`. Última medida: ~361 FPS de media con fuego.
- Python en Windows no lee rutas `/c/...` de Git Bash: usa `cygpath -m`. Los heredocs con `\n` rompen cadenas C#: usa `chr(92)+'n'`.

## 4. Estado técnico vigente (lo que debes saber de la sim y la vista)

- Lockstep determinista a 30 Hz, mundos A/B con hash. Burst obligatorio en zonas; enteros fuera de Burst (`Det`). Nada de azar de simulación para la presentación (usa hash del id).
- Zona de Sagunto (`Level`): fuerte X 70–156, Y 44–85, vía Y=64,5; tren a escala real de 64 m (`TrainRear` 61,5, `TrainMinX/MaxX` 135/151,5), 21 huecos de tropa en dos vagones R2. Andén de obras centrado: `WorkOrigin = (113; 64,5)`. `Populate(..., perimeter)`: en zona de la red (`_netZone`) NO se meten los muros fijos (salen de `Works.Snapshot` vía `SyncWorks`).
- Horda: zombi fino de Teo (3 camisas, `Resources/Models/Zombi/*/SM_zombi_fino_LOD1`, mira a +Z), oscuro #303424 ±8 %, sombra del sol real; LOD de mancha apagado (`RenderAssets.FigureMode`). Pixelado automático 1/3→1/6 según zoom (teclas `[` `]` lo fuerzan). Contorno del shader #1c200c, umbral 0,26 (por luminosidad, no por profundidad).
- Noche: ambiente = negro (con cualquier ambiente > 0 la paleta sube el suelo a L* 37), luna 0,14, sin viñeta, rim apagado. Mezcla de paleta al 65 % cuantiza a escalones: no esperes ajustes continuos de color.
- Trinchera por bandas (captura normal): llano 63,7 / talud ~58 / fondo 41,3. Suelo de zona `#b0a060`.
- Modelos de Teo: FBX en `Assets/TBD/Resources/Models/...` (se cargan con `Resources.Load`); paleta `T_Paleta32` con filtro de punto (lo fuerza `IconImport` y `ModelUserProps`). Todos miran a **+Z** en Unity. Las propiedades `tbd_faccion/tbd_rim` llegan (log en `Library/TBD/userprops.log`); `RimMarker` se añade a los de rim=1 pero el rim está apagado.
- Ambientación de Sagunto (`BuildSaguntoAmbience`): andén de 60 m con línea de seguridad, marquesina, edificio de viajeros (colisión de 5 segmentos `BuildWall`), almacén (primitiva, colisión), postes cada 50 m, pueblo al norte (8 casas con colisión, bloque de pisos, naranjos). Los `BuildWall` van a los dos mundos.
- Obras/Taller (H5): `PreviewZone` enchufa `DensityView` solo al previsualizar (terreno asegurado a 30 m). Panel del taller en la pantalla de zona de Sagunto (teclas 1–5 encargar, 0 cancelar, C Chispas). Superposición de construcción con contorno de 2 px y etiqueta junto al cursor (IMGUI a resolución completa; colores con `.linear`).
- Cámara ortográfica a 55° (Lucía: no tocar FOV).

## 5. Pendiente (en este orden aproximado)

1. Variantes de Teo: `sagunto\<pieza>\v1..v5` (casa, bloque, naranjo; elegir por hash determinista) y naranjo rehecho; zombi_fino\variantes\ v1–v7 (v6 corpulento, v7 bajo 1,63 m) con escala de altura ±5 % por instancia, sembrada. Todo aprobado por Lucía; falta importarlo.
2. 2D de Bruno (PR #13, rama `claude/sprites-importar`; ejecutar `exportar_sprites.py` y `build_a7_texturas.py` tras leerlos): placa y reloj de fachada (placa 3,6×1,1 m a 0,8 m a la izquierda del eje, reloj 1,1×1,1 m a 1,95 m a la derecha, banda a 7,15 m), decal de línea de seguridad (64×2, 0,15 m/px), hollín de vía, decals de suelo; balasto y asfalto regenerados; iconos del taller (`vm_taller_*`), `vm_alertas_aviso_*` (icono ámbar para la etiqueta de «Hay zombis cerca»).
3. Hito 5 en Unity: taller con cola, obras y aspecto de la construcción (radios de foco/nido, marca de alineación, tramado 50 %); luego UI Toolkit del hito 6 (`docs/diseno-hito6.md` §4: reloj arriba, alertas a la izquierda, panel de tren con ruta u horario y marca de «patrón conocido»).
4. Dragón v5 / R1 / R2 / VAMTAC están importados; falta usarlos en el juego (hoy solo R1+R2 como tren). R2 nuevo de Teo (piso #605c48) ya importado.
5. Deuda: contorno interior por profundidad (hoy por luminosidad), rim con fresnel, LOD de mancha (apagado), sombra de masa del suelo (existe `UpdateHordePresentation`), Q14 de la sim sin reproducir, fusilero/oficial/muerte del zombi sin integrar (atlas `atlas_zombi_muerte`, `atlas_oficial` ya en `Resources/Icons/unidades`), asfalto (no hay zona con asfalto).
6. Mantén este relevo al día y copia a `docs/relevo/` los relevos de los demás (lucia.md ya está copiado). Subir el workspace requiere «sí» de Eugenio.

## 6. Trampas conocidas

- Este hilo llegó al máximo de 24 adjuntos: las capturas se mandan con `SendUserFile` (`display render`) y se guarda el nombre en `/mnt/project-files`; Mak las pasa a la galería de Eugenio.
- El sistema de permisos bloqueó: `taskkill`, borrar carpetas de build, empujar el workspace sin «sí» directo, y abrir ventanas del juego sin avisar. Pregunta antes de lanzar builds/tests que usen mucho la GPU del PC de Eugenio cuando esté jugando.
- Un `TBD.exe` abierto bloquea la build en su carpeta; compila a una carpeta nueva.
- Pixelab: solo `create_image_pixen`; nunca gastar sin «sí» directo de Eugenio. ElevenLabs: clave en variable de entorno, nunca en el repo.
- Las capturas supersize (×4) salen más oscuras: mide siempre en captura normal.
- Los goldens y `Level`/obras: Nacho y tú no tocáis `Level` a la vez; avisa a Mak al empezar y al acabar.

## Límite conocido: fuego de vehículos fuera del hash (7-nov)
El fuego de vehículos es local, no pasa por la cola única, así que no entra en el hash. La 4ª corrida de qa20 (`-nightbot -vehfuego`, Noche21) mide el techo, pero su «hash idéntico en los dos mundos» no prueba determinismo del fuego de vehículos. Decisión de Mak: fuera de P1; no tocar antes de la congelación. Para después: pedir a Nacho el CmdType vehículo+objetivo.

## Cierre del 7-nov (Noche29)
Build: C:/Dev/TBD/Builds/Noche37/TBD.exe; rama marcos/noche-prototipo. Hecho: noche persistente (NightRun.Session, NightClock, SaveNightSession/ResumeNightSession en PrototypeBootstrap.Persist.cs), trazadoras y fogonazos (PrototypeBootstrap.Fx.cs), vehiculos con fuego/recarga por NightVehicle, D-N128, puertas con muro 2,5 m, noche v3, SoldadoArmado, texturas de vehiculos. Pendiente para manana: seleccion/destino/formaciones, pose de apuntar, parches del suelo, doble sRGB del HUD (la camara no es la causa, ver docs/capturas/qa25), botones del parte, D-N118, mapa de frentes/ETA, helipuerto/NH90, las A/B de la persistencia de Sara sin hacer, piezas v1.2, y la cadena qa11 (normal_sinrecarga, dificil x2) que sigue corriendo en segundo plano.

## Actualizacion 7-nov 14:00 (Noche46)
Build final: C:/Dev/TBD/Builds/Noche54/TBD.exe (rama marcos/noche-prototipo 7dd8c5e). Corrida automatica con -nightbot en normal: VICTORIA 3 estrellas, 0 bajas, tren y estacion intactos, muro 99 %, 6290 abatidos (docs/capturas/qa34). Nuevo desde Noche37: control de unidades (anillos, destino, frente por arrastre, F1-F4 linea/cuña/columna/bloque), noche G1 + suelo A de Bruno, grietas apagadas, D-N135 (4 oleadas), D-N133. Pendiente: pose de apuntar, persistencia A/B de Sara, helipuerto/NH90, mapa de frentes, piezas v1.2, sonido sin oir.
