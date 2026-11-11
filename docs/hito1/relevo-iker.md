# Relevo de Iker · Hito 1 del núcleo v2 (red de vías, trenes y líneas)

Actualizado: 12-11, 00:20.

## Dónde voy
- Rama: `iker/nucleo-v2` en TBD (sale de main 9772c9de, la I-Noche178, y lleva nacho/hito1 fusionada). Último commit: 23e1ceeb.
- Ya dentro de Mundo: `Mundo/Red/MundoRed.cs` (partial class Mundo), con órdenes 100–105 (PuntoVia, TrazarVia, CancelarVia, NuevaLinea, AsignarTren, NuevoTren), StepRed y hash red.via, red.trenes, red.almacen, red.cargas y red.trazos. Cifras de Hugo puestas: 6 huecos, 40 km/h, 15 s por hueco; línea por defecto de 4 cajas y 2 palés. Pruebas: [50] 24/24 y [Mundo] 15/15.
- Hecho (lógica pura, SIN Unity, probada en dotnet): `Assets/TBD/Scripts/Mundo/Red/Via.cs` y `Red.cs`, namespace `TBD.Mundo`. Encaja en el contrato de Nacho: `Mundo.Red`, `Red.Step(tick)`, `Red.Hash()` y `Red.Save/Load`.
  - Via: estaciones, nodos y tramos trazados por el jugador. Curva Catmull-Rom en enteros, muestreada cada 2 m. Radio mínimo de 60 m (se rechaza sin tocar nada), encaje de 12 m a nodos existentes, longitud mínima de 10 m. Dijkstra para la ruta y posición y rumbo a lo largo del tramo.
  - Red: trenes (aceleración de 1 mm/tick², vmáx de 600 mm/tick = 65 km/h, frenada para parar justo en el nodo) y líneas de N paradas con carga y descarga por recurso (1 u cada 6 ticks, al menos 3 s parado; −1 = todo). Almacén por estación, con 4 recursos provisionales. Si no hay vía, el tren espera y lo reintenta cada segundo.
  - Pruebas: `Dotnet/TBD.Sim.Tests/RedTests.cs`, sección [50], 18 de 18 (`TBD_ONLY_RED=1 dotnet run -c Release`).
- Coop: D-N206, lockstep. Todo en enteros, sin float y sin azar. El hash cambia con el estado.

## Lo siguiente
1. (Hecho) Encajado en Mundo.
2. Vista (cuando haya escena única de Marcos y turno de PC): dibujar los tramos con el kit de Teo, el tren interpolando entre ticks y la herramienta de trazado con vista previa válida o inválida (estética de Bruno; interacción de Lucía en docs/hito1/diseno-vias-lineas.md).
3. Cifras de Hugo: capacidad del tren, tiempos de carga y velocidad. Ahora están en constantes de `Red`/`Tren`.

## Acuerdos
- Una sola simulación: la posición del tren es de `Mundo.Red`, y la vista solo lee e interpola. La red no conoce Unidades ni Zombis; si hace falta (un tapón en la vía, tropa a bordo), se pregunta a Mundo.
- Trampas del juego viejo que siguen valiendo: las corridas en batch no terminan solas (hay que matar el proceso); con la pantalla apagada las capturas salen en negro; no compilar mientras alguien juega en el PC.
