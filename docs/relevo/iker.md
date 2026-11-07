# Relevo · Iker (Programación, 2.º ingeniero de Unity)

Última actualización: 7-nov-2026, 10:50 (Madrid). Se para hasta que se reinicie el uso semanal.

## Quién eres
Iker, segundo ingeniero de Unity junto a Marcos. Trabajas con Remote Control en el PC de Eugenio. Firmas «— Iker (Programación)». Nacho revisa todo antes de fusionar. Nunca hagas push a main ni a la rama de Marcos. El force-push está denegado: para ponerte al día, haz merge, no rebase.

## Dónde
- Proyecto Unity: repo **TBD**. Tu copia es `C:\Dev\TBD-2`, rama `iker/red-estaciones`, que parte de `marcos/noche-prototipo`. La de Marcos es `C:\Dev\TBD`: no la toques.
- Pruebas: `dotnet run -c Release` en `Dotnet/TBD.Sim.Tests` (unos 4 min). Para regenerar el golden, `TBD_REGEN_GOLDEN=1`, y hace falta aprobación con una línea en el registro.
- Capturas de estaciones: cierra tu Unity (la ventana «TBD-2 - …», con `taskkill /PID` sin /F) y lanza `Unity.exe -batchmode -projectPath C:\Dev\TBD-2 -executeMethod TBD.EditorTools.EstacionCaptura.CapturarCastellon -quit`. Salen en `Captures/estaciones/`.

## Tus archivos (Marcos no los toca)
Scripts/Net/Produccion.cs (producción y BucleCastellon), EstacionDato.cs; Scripts/View/EstacionVista.cs, RadarAntena.cs; Editor/EstacionCaptura.cs; Assets/Scenes/Castellon.unity; Resources/Models/{KitEstaciones, Cisterna, Radar, CastellonPiezas, puesto_frente, puerta_vehiculos}; Data/estacion_castellon.json.
Marcos toca PrototypeBootstrap*.cs, MainMenu.cs, UiNoche/*, NetSession.cs y OperationsMap3D.cs. Él llamará a `EstacionVista.Build(root, dato)` desde OperationsMap3D al entrar en un nodo que no sea Sagunto. No cargues escenas en Single, porque la noche sigue viva.

## Hecho
1. Producción por hora y tope del almacén (nudo 1000, estación 100, +200 por depósito), con NetVersion 2 y migración. Fusionado (f41155f; el G3 lo aprobó la D-N131).
2. Escenario de Mak: Sagunto con 80 personas; Castellón infestada y reclamable con FoundStation, que hereda su depósito. Fusionado.
3. Castellón con el kit de Teo: torretas, talud, cisternas con el decal de Bruno y radar. Fusionado (84b5ca4).
4. Bucle Sagunto–Castellón (`BucleCastellon.Horario`, dos viajes al día) y el puesto de frente y la puerta de vehículos: **9f49202, pendiente de que lo revise Nacho**. Dotnet da 792 de 792.

## Pendiente
- Que Nacho fusione 9f49202 en la build de Marcos.
- Hugo: el bucle está limitado por la producción de Castellón (60 al día con 30 personas); en Unity el tren no gasta combustible; TrainCapacity es 400 y no 100. ¿Arranca el escenario con el bucle puesto? Mi recomendación es que no.
- (3) Red de estaciones de Lucía (estados Caída, En liberación y Liberada). No está empezada. Toca NetWorld y HiveDirector, así que hay que coordinarlo con Nacho.

## Trampas
- Los puntos de castellon.json pueden venir como [x, z] o [x, y, z]. La cisterna se gira 90° en el código (el JSON la da a lo largo de X).
- La variante explícita del JSON solo se respeta en kit_cuerpo, kit_remate, la torreta, el puesto y la puerta; el resto va por hash, como en Sagunto.
- El G3 cambia desde el primer tick por el escenario.
