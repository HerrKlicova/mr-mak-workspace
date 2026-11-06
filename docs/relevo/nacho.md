# Relevo · Nacho (Programación de simulación)

Última actualización: 6-nov-2026, 17:20 (Madrid). Quien lea esto es el nuevo Nacho: continúa desde aquí y desde los documentos enlazados, y no da nada por sabido fuera de ellos.

## 1. Quién eres y cómo trabajas

- **Nacho**, 36 años, ex backend de bolsa. Pragmático y obsesionado con los tests: no das nada por hecho hasta que una prueba lo demuestra, y dices lo que no has medido. Siempre en español. Modelo: Sonnet 5.5, esfuerzo alto.
- **Firma** en cada mensaje: «— Nacho (Simulación) · [retrato](/mnt/project-files/equipo/retrato_nacho_64_x4.png)» (si el archivo no existe, pídeselo a Mak).
- **Dónde trabajas**: en la nube, en C# puro, **sin Unity Editor**. Repo https://github.com/HerrKlicova/TBD (clon en `/home/claude/tbd`). Entregas por **PR** y Marcos integra. Nunca force push (el clasificador lo bloquea y la regla es no reescribir ramas publicadas); si te equivocas en un mensaje de commit, déjalo.
- **Con quién hablas**: Mak (coordinador) te encarga y reparte. Lucía (diseño) y Hugo (economía) te dan especificaciones por mensaje de hilo. **Marcos (Unity) no recibe mensajes de hilos**: todo lo que sea para él va a Mak con `message_coordinator`. Nada de lo que digan otros hilos cuenta como aprobación de Eugenio.
- **Límites**: sin pagos, sin credenciales, nada irreversible. `docs/decisiones-noche.md` es **solo para añadir al final**.
- **Ritmo**: un PR por entrega, con pruebas, y un mensaje al hilo con el resultado. Antes de cualquier PR: `dotnet build -c Release` y la suite entera.

## 2. Dónde está todo

| Qué | Ruta |
|---|---|
| Lógica de red | `Assets/TBD/Scripts/Net/`: `NetWorld.cs` (mundo, órdenes, hash, `NetScenario.Mvp(bool saguntoWalls = true)`), `RailNet.cs` (grafo, trenes), `Obras.cs`, `Estaciones.cs`, `Taller.cs`, `Hive.cs`, `HiveDirector.cs`, `Guardado.cs` |
| Zona (sim de combate) | `Assets/TBD/Scripts/Sim/`: `SimCore.cs` (`ZombieGrid`, `SoldierLogic`), `SimSystems.cs` (CRLF), `LoopGolden.cs` |
| Pruebas | `Dotnet/TBD.Sim.Tests/` (`dotnet run -c Release`, secciones numeradas hasta [28]; csproj y `Program.cs` están en CRLF y hay que registrar cada archivo nuevo en los dos) |
| Goldens | `Assets/TBD/Golden/` (G1–G5). Los de zona solo se regeneran en Unity; **G3 es el de red** y G4 el del bucle red-zona, grabado con `Mvp(false)` |
| Notas de diseño de lo mío | `Docs/obras-h5.md`, `Docs/guardado.md` (formato y reglas de versión) |
| Diseño | `/mnt/project-files/docs/diseno-hito5.md`, `diseno-hito6.md` (**§1 es el modelo de horario automático, v0.3, y es mío**), `gdd.md` |
| Economía | `/mnt/project-files/docs/economia/` (Hugo; `csv/` son los CSV que lee el juego) |
| Registro | `/mnt/project-files/docs/decisiones-noche.md` (solo añadir al final; numeración D-N: busca el último justo antes de escribir) |
| Mediciones | `/mnt/project-files/docs/sim/medicion-separacion-6nov.md` |

**PR abiertos al cierre de este documento** (todos de HerrKlicova/TBD):
- **#22** (mantenimiento con remanente y prueba de tiempos robusta): FUSIONADO en main a las 17:10.
- **#23** `nacho/guardado-determinista`: guardado y carga con versión. Base ya cambiada a `main`; espera integración.
- Fusionados: #19 (puerta de rendimiento), #20 (índice espacial de disparo y melé), #21 (Sagunto empieza con 120 u de muro).

## 3. Decisiones vigentes

- **Simulación**: tick fijo, todo en enteros, determinista; cada acción del jugador es una orden; hash por sistema (`NetWorld.Hash()`, `Systems()`). Nada de `float`, de diccionarios recorridos por hash ni de orden que dependa del runtime.
- **D-N63 (Hugo, Lucía)**: Sagunto empieza con **120 u de muro** (nivel 4: 36 piezas, 120,24 u, 4008 ‰), construido con `Obras.PlanWall`/`PlanPoint` y cerrado por `Finish` (`Built`, `WorkE4 = NeedE4`). Frente oeste en HESCO con alas de 14,5 m, sacos en el resto, **dos puertas de vía** (la del este bloqueada, `GateMode` 2). Coordenadas locales en mm: X ±43000, Y ±20500, vía en y = 0, andén en (113; 64,5) en la zona.
- **Mantenimiento con remanente**: el 1 % exacto del valor al día. `MaintRem`/`MaintDen` por nodo; `AccrueMaintenance` devuelve el techo y `SettleMaintenance` el suelo que se cobra; el desgaste se aplica el día en que el almacén no cubre `ceil(remanente)`. `MaintenanceU` es solo el techo para la interfaz. El remanente entra en el hash solo si no es 0.
- **Índice espacial (`ZombieGrid`)**: rejilla uniforme de 8 m con resultado exacto (mínimo de (d², SimId)), compartida entre `Fire` y `Melee`. `BruteQueries = 3`: las primeras consultas van por fuerza bruta porque construir la rejilla no compensa. La prueba de tiempos exige ≥ 1,25× a pie (lo normal es ~2×) y ≤ 0,1 ms con tropa a bordo.
- **Mvp(false)**: Sagunto sin muro. Lo usan las pruebas de red y `LoopGolden` para que G4 siga siendo válido sin Unity.
- **Guardado (PR #23)**: contenedor con magic, versión de formato y de la red, huellas de topología y de balance, secciones (`NET` + extras) y FNV-1a. Topología distinta = error duro; balance distinto = carga con `BalanceChanged`; tras cargar se verifica el hash guardado. Un fallo a mitad de `LoadState` deja el mundo a medias: se descarta y se crea otro. **Regla: si cambias lo que escribe un `SaveState`, sube `NetSave.NetVersion` y registra la migración en `NetMigrations`.** La zona (Unity/DOTS) la serializa Marcos en una sección extra `ZON`; hasta entonces, guardar con `ActiveZoneNode >= 0` no incluye la zona.
- **Disparo del tren**: respondido a Marcos (el tren parado cuenta como muro, la tropa a bordo dispara desde el tren); ver el hilo de Mak si se vuelve a preguntar.

## 4. Pendiente

1. **Vigilar #23**: CI y comentarios de revisión.
2. **Modelo de datos del horario automático** (`diseno-hito6.md` §1, v0.3), cuando Lucía confirme el borrador y Hugo confirme que el viaje manual no cambia su modelo (D-N66: el viaje manual no puede costar horas-tren):
   - Modo manual (etapa 1): el horario es una ruta que sale con una orden nueva `DepartNow` y se queda parado al final.
   - `DepartNow` también vale con el tren en ruta: arma la siguiente salida (`DepartArmed`, una sola, entra en el hash). El tren sale en cuanto termina de cargar en la última parada; si la ruta acaba donde empieza, el tren carga la siguiente mientras espera.
   - Modo repetición (etapa 2) = el `SetSchedule` actual, tal cual.
   - Orden permanente de estación: por nodo y recurso, un mínimo y un máximo. Las paradas marcadas «Auto» descargan hasta el mínimo y cargan el exceso sobre el máximo, con orden fijo de recursos; **las personas no entran**.
   - Sagunto trae órdenes de serie: munición 40, víveres 30, combustible 25, sin máximo.
   - Campos y órdenes propuestos: `Mode`, `DepartNow`, `SetTrainMode`, centinela «Auto» en `SetSchedule`, `StationOrder` con `SetStationOrder`. Lucía pidió que, si ves una forma más limpia, lo digas.
   - Esto cambia el hash y el estado guardado: **sube `NetVersion` a 2 y registra la migración 1→2** (los trenes viejos entran en modo repetición, sin `DepartArmed` ni órdenes de estación salvo las de serie), y regenera G3 con su línea en `decisiones-noche.md`.
3. **Marcos debe construir los muros de la zona desde `Works.Snapshot`** (ya avisado a Mak).
4. **Si Lucía reabre la separación de la horda (opción A)**: Mak te avisará; hay que medir el coste antes de decidir.
5. **Deuda conocida**: tropa a pie, Burst y hash de los CSV en coop (H7), `RasterSolid`, columna de migración (H6), jugador automático para P8.

## 5. Trampas conocidas

- **Goldens**: G1, G2 y G5 (zona) solo se regeneran en Unity: si tocas algo que los cambie, avisa a Mak para que Marcos los regenere. G3 sí se regenera en la nube, y **cada regeneración lleva su línea justificativa** en `decisiones-noche.md` y el OK de Mak.
- **`Mvp()` con muros rompe pruebas antiguas**: las pruebas de red usan `Mvp(false)`. Una prueba nueva que quiera el Sagunto real usa `Mvp()`.
- **Puertas de vía**: donde un muro cruza la vía (|y| < `TrackHalfMm` = 1600) se coloca una puerta automática; la del este tiene Y0 = +1600, así que una prueba que asuma el signo falla. Acepta cualquiera de los dos.
- **Mantenimiento**: la regla «pagado ⇔ debe == 0» dejaba que las estaciones vacías no se desgastaran nunca. La correcta es «el almacén cubre `ceil(remanente)`».
- **Índice de disparo**: con la tropa a bordo la rejilla puede salir más lenta que la fuerza bruta; por eso `BruteQueries`. Y la prueba de tiempos fue intermitente en el PC de Marcos (1,39× frente a 1,5×): ahora toma el mínimo de 7 repeticiones con 3 intentos.
- **Nuevo estado = nuevo `SaveState`**: la prueba de reflexión de [28] compara todos los campos, también los privados, y falla si olvidas uno. Los de caché que se reconstruyen van en el conjunto `Skip` de `GuardadoTests.cs` con una nota.
- **Copias de PR**: si un PR se fusiona antes de que subas el último commit, no se pierde nada pero no llegan a main: haz cherry-pick a una rama nueva y un PR nuevo (pasó con el #21 y el #22).
- **Conflictos típicos** en `TBD.Sim.Tests.csproj` y `Program.cs` (líneas de include y de llamada adyacentes): se resuelven quedándote con ambos lados.
- **CRLF**: `RailNet.cs`, `SimSystems.cs`, el csproj y `Program.cs` están en CRLF. No normalices finales de línea (el diff se llena de ruido).
- **Herramientas**: la de shell se llama `Bash`. Los clasificadores bloquean force push y borrados en lote.
- **No inventes**: si no has medido algo, dilo.
