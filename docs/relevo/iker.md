# Relevo · Iker (Programación, 2.º ingeniero de Unity)

Última actualización: 8-nov-2026, 12:45 (Madrid). Quien lea esto es el nuevo Iker: empieza por aquí y por los archivos enlazados, y no des nada por sabido fuera de ellos.

## Quién eres
- Iker, segundo ingeniero de Unity junto a Marcos. Trabajas con Remote Control en el PC de Eugenio (DESKTOP-1BLD8V4). Siempre en español.
- Firmas «— Iker (Programación)» con tu retrato. Avisa a Eugenio con enlaces, nunca con rutas.
- Nacho revisa todo antes de fusionar. **Nunca hagas push a main de TBD ni a la rama de Marcos.** El force-push está denegado: para ponerte al día, haz merge, no rebase.
- Marcos no recibe mensajes de los hilos: lo que sea para él va por Mak (el coordinador).
- Regla de Eugenio (7-nov): cuando se acaba el uso semanal, se cierra lo que haya y se para hasta que se reinicie.

## Dónde
- Proyecto Unity: repo **TBD** (`github.com/HerrKlicova/TBD`). Tu copia es `C:\Dev\TBD-2`, en la rama `iker/red-estaciones`. La de Marcos es `C:\Dev\TBD`: no la toques, porque tiene cambios sin confirmar y un Unity abierto.
- Base de trabajo: `origin/marcos/noche-prototipo`. Antes de empezar, `git fetch origin` y `git merge origin/marcos/noche-prototipo` en tu rama. El 8-nov por la mañana iba por 4012165.
- La documentación y las decisiones están en `C:\Dev\mr-mak-workspace` (repo mr-mak) y en `/mnt/project-files/docs`.
- Unity 6000.3.28f1. Tu editor es la ventana «TBD-2 - … Unity». Para cerrarlo sin tocar el de Marcos, búscalo con `tasklist /V /FI "IMAGENAME eq Unity.exe"` y ciérralo con `taskkill /PID <pid>` (sin /F).

## Cómo se prueba
- Lógica pura: `dotnet run -c Release` en `Dotnet/TBD.Sim.Tests`, unos 4 min. La última vez dio 792 de 792. Para regenerar el golden G3, `TBD_REGEN_GOLDEN=1`, y hace falta aprobación con una línea en el registro de decisiones.
- Archivos de prueba nuevos: hay que añadirlos a `TBD.Sim.Tests.csproj` (no usa comodines) y a `Program.cs`.
- Unity en batch: con tu editor cerrado, `Unity.exe -batchmode -projectPath C:\Dev\TBD-2 -executeMethod TBD.EditorTools.EstacionCaptura.CapturarCastellon -quit -logFile Logs\captura_castellon.log`. Compila, monta Castellón y deja las capturas en `Captures/estaciones/` (carpeta ignorada por git).
- `.meta`: cada archivo nuevo tiene que llevar el suyo, generado por Unity (abre el editor o lanza el batch). Nacho no fusiona sin ellos.
- Capturas para Eugenio: se adjuntan en el hilo con SendUserFile y se le pide al coordinador que las suba a la galería y al índice.

## Tus archivos (Marcos no los toca)
- `Scripts/Net/Produccion.cs`: producción por hora, tope del almacén y `BucleCastellon`.
- `Scripts/Net/EstacionDato.cs`: lee `estacion_<id>.json`.
- `Scripts/View/EstacionVista.cs` y `RadarAntena.cs`.
- `Editor/EstacionCaptura.cs` y `Assets/Scenes/Castellon.unity` (escena de prueba).
- `Resources/Models/{KitEstaciones, Cisterna, Radar, CastellonPiezas, puesto_frente, puerta_vehiculos}`.
- `Data/estacion_castellon.json` (copia de `docs/niveles/estaciones/castellon.json` de Álvaro, b6c5098). `BalanceBuildCopy` copia `estacion_*.json` a la compilación.

Marcos toca `PrototypeBootstrap*.cs`, `MainMenu.cs`, `UiNoche/*`, `NetSession.cs` y `OperationsMap3D.cs`. Él llamará a `EstacionVista.Build(root, dato)` desde OperationsMap3D al entrar en un nodo que no sea Sagunto. No cargues escenas en modo Single: la noche sigue viva al salir.

## Hecho (todo fusionado en marcos/noche-prototipo)
1. **Producción por hora y tope del almacén.** Pulso cada 1500 ticks, prod × factor / 24, con el remanente en 1/24.000 de u. Tope por recurso: nudo 1000, estación 100 y +200 por depósito sano (también en el nudo). NetVersion 2, con migración 1 → 2. Las dos pruebas de Hugo pasan: 300 u en 5 días con 30 personas y en 2,5 días con 90. (f41155f; G3 aprobado en la D-N131).
2. **Escenario de Mak.** Sagunto arranca con 80 personas. Castellón empieza infestada, sin gente ni almacén, y se reclama con FoundStation (30 u y 12 personas). Con las estructuras de partida hereda su depósito (300 u). Hasta que se reclama, la Colmena no la elige como objetivo (Hugo, de acuerdo).
3. **Castellón con el kit de Teo** (84b5ca4): `EstacionVista.Build`, `SetTankLoad` (decal de Bruno, N = round(4 · carga / capacidad)), `SetRadar` (v3 obra, v1 Segura, v2 fortificado, v4 caído) y la antena que gira.
4. **Bucle Sagunto–Castellón y piezas que faltaban** (9f49202, fusionado). `BucleCastellon.Horario(w)` es el payload de SetSchedule: Sagunto 06:00 → Castellón 10:00 → Sagunto 14:00 → Castellón 18:00. No viene puesto en el escenario. Puesto de frente v2 y puerta de vehículos v1 integrados: ya no queda ninguna caja gris.

5. **Motor del tutorial, capítulos 0 y 3, tarjeta del C90 e intro C** (c6df090, en `iker/red-estaciones`, sin fusionar). C# puro en `Scripts/Tutorial/` (TutorialMotor, TutorialGuion con los textos de Lucía de los capítulos 0 a 3, C90Aviso, IntroSecuencia) y vista IMGUI en `View/TutorialHud.cs` e `View/IntroVista.cs`. Pruebas: sección [30], 42 de 42 (suite entera 873 de 873). Corrida automática: `Editor/TutorialBuild.Construir` (build en `Builds/iker-tutorial/`) y `TBD.exe -menu-auto -tutorial-auto -intro`; capturas en `Builds/iker-tutorial/Captures/tutorial/`. Recorre los 31 pasos hasta «terminado».
   - **Enganches que faltan (Marcos):** `IntroVista.Antes(seguir)` en MainMenu.StartGame; `TutorialHud.PidePausa` y `HordaEnEspera` en la zona; botón «Saltar tutorial» en el menú de pausa si `TutorialHud.Activo`; `TutorialHud.Senal(...)` de los capítulos 1 y 2 (nombres en `TutorialGuion.Senales`); `TutorialHud.Objetivo(clave, rect)` para los anillos; `TutorialHud.AnclaY` (fin de los avisos); `TutorialHud.ComprobarC90(_uw, zombis)` cada segundo. Lo del mapa (mapa_abierto, tren_en_nules, vuelta_zona y anillos de los 3 nodos) ya lo hace la vista sola.
   - **Capítulo 3 bloqueado en el 3.4** hasta que exista el panel «Preparar tren» (carga, pelotón, vehículo, destino, ETA, enviar, descargar): tiene que mandar las señales panel_tren_abierto, carga_puesta, peloton_a_bordo, vehiculo_a_bordo/sin_apoyo, destino_nules, tren_enviado, panel_nules_abierto y descargado.
   - Trampa: las capturas con ScreenCapture salen con la zona en negro (no pasan por el blit de Marcos); la tarjeta sí se ve.

6. **Revisión de Nacho, panel «Preparar tren», máquina de escribir e intro con fondos** (98826bc aprobado por Nacho; 40c846d y siguiente, sin revisar). La rama está fusionada con marcos e72c3b2 (merge, no rebase: el force-push está denegado). Program.cs y el csproj, en CRLF: para conservarlo, `git hash-object -w --no-filters` + `git update-index --cacheinfo` (con autocrlf=true, `git add` los pasa a LF).
   - `Net/TrenPreparar.cs`: Envio, Descarga, **Aparcar** (horario de una parada: SetSchedule es cíclico), ETA. `View/TrenPanel.cs`: panel en el mapa contra `IEmbarque` con `EmbarqueStub` (1 pelotón y 1 vehículo por tren) hasta nacho/tren-embarque (TrainLoad/TrainUnload, ids ATren=2000+tren y EnEstacion=3000+nodo, D-N166). Corrida: `TBD.exe -menu-auto -sinintro -sintutorial -leaveat 15 -trenpanel-auto` → Captures/tren/.
   - `Tutorial/Maquina.cs`: letra a letra con sfx_ui_tecla_1..8 de Nuria (±3 %), retorno 0,4 y campanilla; al saltar el texto no suena nada. Intro y tarjetas del tutorial en negrita y más grandes (Eugenio). Fondos de Bruno por tarjeta: D, A, B, C, C (`Resources/Intro/`).
   - Pendiente: cambiar el stub por la API de Nacho (después de las 16:00); que Marcos ponga los 7 enganches.

## Pendiente
### Nuevo encargo (D-N154, D-N158 y D-N163; Lucía, 8-nov)
- **Motor del tutorial**, más los **capítulos 0 y 3** y la **tarjeta suelta del C90**. Textos: `docs/tutorial-textos.md`; el capítulo 4 está en `docs/tutorial-refuerzos.md`. Marcos hace los capítulos 1 y 2, el tramo oeste al 45 % y la horda en espera.
  - Reglas: tarjeta arriba a la izquierda, debajo de los avisos, con «Capítulo N · Paso x de y». Anillo que late en hueso d4d0cc y nada de rojo. Se salta desde la primera tarjeta o desde la pausa. Solo la primera vez, y solo en fácil y normal. Si el jugador se desvía, se repite la tarjeta sin castigo.
  - Las teclas con * son propuestas: si usamos otra, se cambia el texto, no la tecla.
  - El capítulo 3 usa el mapa (M), «Preparar tren», cargas, pelotón y vehículo a bordo, ETA y descargar en Nules. Mira qué existe ya en NetSession/OperationsMap3D (es de Marcos) antes de diseñar el motor, y acuerda con él dónde se engancha.
  - Sara probará con `-nightbot` el tutorial entero y también saltándolo.
- **Intro: variante C («Día 41», sin año)**, decidida por Mak. Va en el Bloque 2. Texto en `docs/intro-variantes.md`: 5 tarjetas de unos 6 s, saltable con un clic o con la barra espaciadora. El fondo lo hace Bruno.
### De antes
- **Red de estaciones de Lucía** (`docs/diseno-red-estaciones.md`): estados Caída, En liberación y Liberada, la línea cortada y la inteligencia. No está empezada. Toca NetWorld y HiveDirector, así que hay que coordinarlo con Nacho.
- **Hugo, sin respuesta:**
  - El bucle está limitado por la producción de Castellón (60 al día con 30 personas; para traer 200 u al día hacen falta ~90).
  - En Unity el tren no gasta combustible.
  - `NetConst.TrainCapacity` es 400 «t, PROTOTIPO» y no las 100 u de su modelo.
  - ¿El escenario arranca con el bucle puesto? Mi recomendación es que no.

## Trampas conocidas
- Los puntos de `castellon.json` pueden venir como [x, z] o [x, y, z]. `EstacionDato.XZ` acepta las dos formas.
- La cisterna se gira 90° en el código, porque el JSON la da a lo largo de X con yaw 0 y el modelo de Teo va a lo largo de Z. No sumes otro giro.
- La variante explícita del JSON solo se respeta en kit_cuerpo, kit_remate, la torreta, el talud, el puesto y la puerta. El resto va por hash de la posición, con la misma función que Sagunto (`math.hash(int2(x·10, z·10))`, copiada en enteros en `EstacionDato.VariantOf`).
- Las piezas de Sagunto vienen en dos formatos: base + carpetas v1..v5, o ficheros planos `SM_x_vK` (el muelle). `SaguntoPiece` prueba los dos.
- Las pruebas de mantenimiento, taller y conservación de carga apagan la producción con `ProductionEnabled` (solo pruebas, no se guarda).
- El G3 cambia desde el primer tick por el escenario de Mak. Es legítimo.
- Los finales de línea: el repo normaliza a LF. Un diff enorme en un `.csproj` suele ser solo eso; revísalo con `--ignore-cr-at-eol`.
- Los FBX van por LFS. El aviso «LF will be replaced by CRLF» al añadirlos no los estropea.

— Iker (Programación)
