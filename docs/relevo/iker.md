# Relevo · Iker (Programación, 2.º ingeniero de Unity)

Última actualización: 8-nov-2026, 15:00 (Madrid). Quien lea esto es el nuevo Iker: empieza por aquí y por los archivos enlazados, y no des nada por sabido fuera de ellos.

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
   - Embarque ya real (iker/red-estaciones con nacho/tren-embarque fusionada): `EmbarqueRed` en TrenPanel. PROTOTIPO: desde el mapa, dentroRecinto = true y sin mirar zombis a 3 m; noche de 21:00 a 7:00 a ojo; ids de vehículo = índice en NightRun.Session.Sim.Vehicles (hay que confirmar que coincide con la lista de la zona). Pendiente: los 7 enganches de Marcos y bajar en Sagunto dentro de la zona (BajarPeloton con posición).

7. **Tarde del 8-nov** (todo en iker/red-estaciones; último c73a83e):
   - **NO lanzar TBD.exe en el PC de Eugenio** (abre ventana; se enfadó). Solo dotnet y Unity -batchmode (TutorialBuild.Construir compila; no ejecutar la build).
   - Capítulo 3 = D-N172 revisada: rescate en la primera noche. Salta con Senal(Pila150) o 60 s después de Senal(ContactoMuro) (3.1b), la horda no espera, Nules manda 1 pelotón (Destacamento: tren parado en Nules + pasajero EnEstacion). TrenAnden (zona) descarga en Sagunto: con asedio solo tropa; si no, CmdCargo baja la carga. Objetivo después de la noche: «Lleva el tren a Nules con munición».
   - Bétera (D-N173): AerodromoEstado (puro, lee Data/estacion_betera.json de Álvaro) + AerodromoVista (nodo y panel en el mapa, Llegadas para la zona, VolverARearmar). Capítulo 4 al abrir el aeródromo (textos míos, pendientes de Lucía). Plantel por estación en Aerodromo.cs. Zona de Bétera: elegido el encuadre de reserva 256 × 128 (no hecha).
   - El vuelo sale ~3,5 s porque NetConst sigue en ×72 (el ×103 de la D-N161 aún no está en la red).
   - Enganches pendientes de Marcos: RegistrarDestacamento, Senal(Pila150/ContactoMuro/OrdenAtacar), TrenAnden.PuntoBajada (costado sur, puerta este), anillo «pila» en (100;34), ComprobarC90 con recinto, ocultar Vehs Embarcado, consumir AerodromoVista.Llegadas y llamar VolverARearmar/PelotonEnTierra, señales nh90_posado/nh90_descargado.
   - Mañana 09-11: 5 muestras de interfaz con PixelLab (brief docs/relevo/iris.md, prefijo docs/arte/pixellab-prefijo-validado.md), saldo antes/después, ≤ 20 %, clave solo por variable de entorno.

8. **Rama nueva `iker/escenario-inicio`** (desde la tarde del 8-nov: lo que no debe entrar antes de la build de las 18:30; Marcos ya fusiona `iker/red-estaciones`). Último 2683fa3. Lleva todo lo de iker/red-estaciones más:
   - `NetScenario.Inicio()` (D-N156): Valencia/Teruel a 0, trenes sin horario en Sagunto, reserva de Sagunto en u 150/140/100/80, Nules propia con 0 de munición. Mvp() intacto (pruebas y goldens). Para estrenarlo, NetSession.Ensure → Inicio() (Marcos). Pendiente: víveres (Res no los tiene), Nules sin asedio la 1.ª noche (director), recinto de Nules (Obras).
   - `AlmacenZona` (regla de Hugo), `ObjetivoViaje` («Lleva munición a Nules», textos de Lucía), `AndenPuntos` (Nules v0.1), `SalidaTren` + `SalidaTrenSonido` (25 OGG de Nuria), `MapaGestos` (doble clic, D-N170), `AerodromoNivel` + `VueloLocal` + `AerodromoZona` + `Editor/AerodromoCaptura` (escena Assets/Scenes/Betera.unity, encuadre 256 × 128), `SonidoNH90` (OGG pendientes).
   - Piezas: Resources/Models/Betera (Teo r2 + helipuerto + rearme_set) y Resources/Models/Nules (148 FBX).
   - Pruebas: sección [30] 190 de 190; suite entera 1043 de 1043 (antes de la zona de Bétera).
   - Mañana: lote de PixelLab (`/mnt/project-files/pixellab-lote-0911.md`, 30 generaciones; saldo 8.228,05 el 8-nov).
7. **Tarde del 8-nov** (iker/escenario-inicio hasta 302d22a; ya lleva fusionadas nacho/sombra-reloj y marcos/noche-prototipo):
   - Víveres (Res.Viveres = 4 de Nacho): Sagunto con 80 u en Inicio y sin horarios de víveres (Lucía). Bétera con 20 u y `Consume = false` (lista «no_consumen_en_mvp» de existencias_red.json de Hugo).
   - Reloj ×103: ya no existe NetConst.GameMsPerTick; se usan HourTicks y GameMs.
   - Castellón v0.4: kit subterráneo de Teo en Resources/Models/Castellon/<carpeta>, con 150 piezas y el mobiliario urbano en Models/Urbano. `CastellonKit.Archivo` lleva de la pieza al fichero. `BajadaSubterranea` da la tropa por el vestíbulo, los vehículos en (144; 38), la escalera de 7,1 m y la subida de 30 s. La captura tiene una toma bajo losa (oculta los hijos Losa y Cubierta).
   - Carga visible (`CargaVisible`, 20 u por plataforma, Dañado por debajo del 70 % y Destrozado por debajo del 30 %) y `CargaVagonVista`. Acopio de Nules (`AcopioViveres`, 30 u de referencia) y `AcopioVista` con Data/nules_instancias.csv. Marcos los engancha en su zona.
   - Bétera: el ambiente (51 piezas) en Models/Betera/ambiente, a través de `AerodromoNivel.Ambiente`. El rearme (`RearmeBetera`, Models/Betera/rearme) cambia de malla con `AerodromoZona.Actualizar(res, estado)`.
   - Mapa táctico de Bruno: MapaTactico.cs y 4 cambios en OperationsMap3D. El parche de cerca tiene 512 téxeles y se calcula en segundo plano (Task). Las capturas salen con `Editor/MapaCaptura`, que no pinta OnGUI. El fundido a navy es de Marcos (NetSession).
   - Pruebas: 1194 de 1194.
8. **PAUSA del 8-nov a las 20:18 (Eugenio juega).** El punto para retomar es iker/escenario-inicio bbb29ad, subido. Ya lleva fusionadas marcos/noche-prototipo 2643f16 y nacho/tren-puertas d091856. Suite: 1237 de 1237. Compila en Unity por lotes. No hay ningún Unity mío abierto.
   - Hecho desde el punto 7:
     - D-N173: plantel por estación en la zona (Plantel.Pelotones y Plantel.Vehiculos) y `-zona <nombre>` para Sara.
     - D-N152: regla de red de Nacho; `Puertas` solo la lee.
     - D-N177: aviso ámbar «Sin escolta: X está sitiada».
     - D-N157: fuera la barra de la noche y el contador de oleadas.
     - Las 4 señales del tutorial en la zona (`SenalesZona` y `TutorialHud.Zona`).
     - D-N156: Nules sin asedio la 1.ª noche (`HiveDirector.SinAsedioNodo`, no se guarda). NetSession.Ensure ya usaba Inicio().
     - Parche del mapa en segundo plano.
   - Pendiente al volver:
     - D-N91: revisar que el tiempo real no se pare ni salte al cambiar de vista.
     - Comprobar la corrida de Sara (qa45) con -zona.
     - Plazas: Lucía dice que solo tienen plaza Sagunto, Nules y Bétera, y que Teruel y Zaragoza van a 0. Está en NetWorld.TrainSlots, que es de Nacho. Bétera no es nodo de la red.
     - D-N160, el informe de inteligencia, va después del tutorial.
     - El FARP de Bétera y el huerto de Nules los integra Marcos.
9. **Integrador desde el 8-nov a las 22:10** (encargo del coordinador: descargar a Marcos). Las builds de integración salen de iker/escenario-inicio a `C:\Dev\TBD-2\Builds\NocheNN` con `TutorialBuild.ConstruirNoche -noche NN`.
   - **Noche70** (3e265e2): plantel, puertas, víveres, avisos ámbar, capítulo 3 y sonidos de Nuria.
     - Le falta existencias_red.json, porque BalanceBuildCopy solo copiaba estacion_*.json. Arreglado en cf4f0db.
   - **Noche71** (cf4f0db):
     - horda de Nules de Nacho;
     - fracción de las puertas: Sagunto 0 %, Nules 10 %;
     - capítulo 3 con la 3.8 simple y la 3.8b condicional;
     - arte de Bruno: D-N80, pila, vías, fantasma y bocas de arma;
     - bocas de Teo f42c931;
     - NOCHE-ARMAS;
     - CapturaLotes (captura por RenderTexture).
   - **Noche72** (edd7645): D-N179 (ObjetivoDefensa), los 24 iconos APP-6, nacho/asedio-nules 1d426cf y claude/informe-app6 f438db8 (tecla I).
   - **QA**:
     - Scripts en el scratchpad: qa70.sh y qa46.sh. Siempre con `-menu-auto`: sin él, -nightbot se queda en el menú.
     - Los logs van a docs/capturas/qa70 y qa46.
     - qa46 hecha: unos 390 zombis por u y pila_max entre 0 y 19.
   - **Capturas**: el clasificador de permisos bloquea el player sin -nographics. Hace falta la regla en `.claude/settings.local.json` (ver memoria no-ventanas-en-el-pc).
   - **Si Marcos se corta**: sigo desde docs/relevo/marcos.md, con el turbo por SimId y las semillas de la Noche75.
   - Trampa: un -nographics deja las capturas en blanco y vuelve a guardar las escenas. Hay que hacer `git checkout` de Assets/Scenes después de compilar así, y las capturas se sacan solo con -batchmode.

## Estado al 9-nov 12:45 (integrador; rama iker/escenario-inicio en C:\Dev\TBD-2)
- Última build: **I-Noche107** (3a05e9b7). Compilar: `Unity.exe -batchmode -nographics -projectPath C:\Dev\TBD-2 -executeMethod TBD.EditorTools.TutorialBuild.ConstruirNoche -noche N [-dev] -quit`. Antes `touch C:\Dev\TBD\Builds\Noche82\PAUSA` y después borrarlo (las tandas de Marcos esperan).
- Ramas que se fusionan: claude/sombra-tren (Bruno), nacho/dn183-castellon (Nacho), marcos/partida-30 (Marcos).
- Partida de 30 min: D-N183 (guarniciones por estación: PuestosPel/PuestosVeh en Aerodromo.cs, Álvaro v1.1/v1.2), D-N184 (Castellón cercada), emboscada (PrototypeBootstrap.Emboscada.cs: franja AmbushSpawn*, AmbushEnd, TrainLost), EM-1 y «tren parado» (OperationsMap3D; log en Update), objetivo del día 2 (ObjTroops), S2 «ha caído» (LoseNode, guardado del atardecer atardecer.tbd, Repetir la noche), tutorial (tope 10 s en cap. 1-2, mínimo 3 s por tarjeta, 2.4b, 1.8 de 4 s), título de entrada en la zona.
- **Cada zona tiene su noche** (NightSession.Node + NightRun.Aparcadas). Antes Nules reanudaba la de Sagunto.
- Nules opción A: StreamingAssets/Noche/nules.json de Hugo (tren fuera de la puerta este, X 160–224). Sin tren en la estación, la noche empieza con TrainHp = 0 (_nocheSinTren: sin aviso, frente ni barra). Almacén de munición de la zona = min(47, reserva de la red).
- Corridas: `-dia2-auto` (escoltado, saca el tren a las 19:30 → victoria), `-dia2-auto-sinescolta` (derrota), `-dia2-auto-tren-aparcado` (tren perdido, victoria). `-tutorial-auto` implica -menu-auto. NetSession.Turbo solo para corridas.
- Pendiente: limpieza de C:\Dev\TBD-2\Builds (el clasificador deniega `rm -rf`; plan: borrar I-Noche76–99 salvo 91dev y Noche70–73; decide Eugenio). Nombres en fachadas y puerta de Castellón de Marcos para la 108.
- Trampa (3 veces hoy): un comentario `//` insertado a mitad de línea por un script se traga el código que sigue. Ponlo siempre al final de la línea.

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
