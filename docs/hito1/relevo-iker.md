# Relevo de Iker · Hito 1 del núcleo v2 (red de vías, trenes y líneas)

Actualizado: 12-11, 01:50.

## Dónde voy
- Rama: `iker/nucleo-v2` en TBD (sale de main 9772c9de, la I-Noche178, y lleva nacho/hito1 fusionada). Último commit: aef24ba8 (lo de Unity SIN COMPILAR).
- Ya dentro de Mundo: `Mundo/Red/MundoRed.cs` (partial class Mundo), con órdenes 100–105 (PuntoVia, TrazarVia, CancelarVia, NuevaLinea, AsignarTren, NuevoTren), StepRed y hash red.via, red.trenes, red.almacen, red.cargas y red.trazos. Cifras de Hugo puestas: 6 huecos, 40 km/h, 15 s por hueco; línea por defecto de 4 cajas y 2 palés. Pruebas: [50] 24/24 y [Mundo] 15/15.
- Hecho (lógica pura, SIN Unity, probada en dotnet): `Assets/TBD/Scripts/Mundo/Red/Via.cs` y `Red.cs`, namespace `TBD.Mundo`. Encaja en el contrato de Nacho: `Mundo.Red`, `Red.Step(tick)`, `Red.Hash()` y `Red.Save/Load`.
  - Via: estaciones, nodos y tramos trazados por el jugador. Curva Catmull-Rom en enteros, muestreada cada 2 m. Radio mínimo de 60 m (se rechaza sin tocar nada), encaje de 12 m a nodos existentes, longitud mínima de 10 m. Dijkstra para la ruta y posición y rumbo a lo largo del tramo.
  - Red: trenes (aceleración de 1 mm/tick², vmáx de 600 mm/tick = 65 km/h, frenada para parar justo en el nodo) y líneas de N paradas con carga y descarga por recurso (1 u cada 6 ticks, al menos 3 s parado; −1 = todo). Almacén por estación, con 4 recursos provisionales. Si no hay vía, el tren espera y lo reintenta cada segundo.
  - Pruebas: `Dotnet/TBD.Sim.Tests/RedTests.cs`, sección [50], 18 de 18 (`TBD_ONLY_RED=1 dotnet run -c Release`).
- Coop: D-N206, lockstep. Todo en enteros, sin float y sin azar. El hash cambia con el estado.

- D-N209 (vía por piezas del kit de Teo): Via.TrazarLibre ajusta el trazo libre a piezas (Recta10, Recta2_5, curvas de R 60/120/240) por persecución pura; cada tramo guarda RumboIni y Piezas[]. Carreteras y pasos a nivel (Via.Carreteras y Via.PasosNivel; menos de 30° = «Cruce demasiado sesgado»). Texto de la línea con la vuelta medida (Red.TextoLinea). Pruebas: [50] 30/30.

- Vista: `Mundo/Red/RedVista.cs` sobre la escena de Marcos (marcos/mundo-zum fusionada, y también alvaro/hito1-terreno). T traza con el ratón y la vista previa va en hueso o en ámbar con la causa; vía como cinta de balasto y carriles; tren de 3 coches interpolado; línea A–B automática. Build: Builds/Mundo-I1/TBD.exe -mundo [-redauto -redx8 -redcapturas]. RedVista lleva su propia Red hasta tener el Mundo común en la escena. Capturas: docs/capturas/hito1/red/ (aún no son presentables).

- RedVista v2: UsarMundo(Mundo) (órdenes por Encolar), vista previa con ZumTrazado de Bruno, símbolo en MAPA (≥ 900 m), FBX del kit de Teo pieza a pieza (Resources/Models/Red, LFS) y paso a nivel de 60°. Mundo.MontarRedHito1() en MundoRed.cs: Nacho tiene que llamarlo desde Mundo.Caserio. Fusionadas nacho/hito1 18f1cc7d, bruno/zum-shaders y alvaro/hito1-terreno.

## Lo siguiente
1. (Hecho) Encajado en Mundo.
2. Vista, siguiente pasada (con turno de PC): símbolo de vía con grosor a 900 m o más (Bruno), FBX del kit de Teo en lugar de la cinta, paso a nivel, sonidos de Nuria, cámara a las estaciones y prueba a mano de 10 min. Antes: fusionar nacho/hito1 8a550fc3 y usar un solo Mundo en la escena.
3. (Hecho) Cifras de Hugo puestas. Pendiente: forzar recta en los 20–30 m del paso a nivel y recibir las carreteras de Álvaro en mm.

## Acuerdos
- Una sola simulación: la posición del tren es de `Mundo.Red`, y la vista solo lee e interpola. La red no conoce Unidades ni Zombis; si hace falta (un tapón en la vía, tropa a bordo), se pregunta a Mundo.
- Trampas del juego viejo que siguen valiendo: las corridas en batch no terminan solas (hay que matar el proceso); con la pantalla apagada las capturas salen en negro; no compilar mientras alguien juega en el PC.
