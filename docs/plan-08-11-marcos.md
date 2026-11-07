# Plan del 8-nov para Marcos (Programación), pendiente al parar el 7-nov

Última build entregada: C:/Dev/TBD/Builds/Noche56/TBD.exe (rama marcos/noche-prototipo, 4f0ea7b). Todo lo de abajo está SIN HACER en la rama, salvo lo indicado.
La corrida automática larga de la Noche55 (horda final de Hugo, 7310 en normal) estaba en marcha al parar: mirar docs/capturas/qa39 (log_final.log, traza_noche.csv).
El -inputtest de la Noche55 movió la cámara bien (D/W/A/S «MUEVE»), pero la parte de selección salió «fuera de pantalla» porque el foco ya se había movido: hay que hacerla antes de mover la cámara.

## Orden de trabajo

1. **Paquete de sonido de Nuria** (entregas/sonido-noche55/LEEME.md y codigo/Sfx.cs): Sfx.cs parcheado (GlobalGain 0,45, oído ≥ 22 m, curva sin meseta); zombi_caida 3D 1 de cada 10 muertes (Night.cs, KillZombies); quitar la tanda 2D de impacto/caída/muerte; explosion_granada, cola_urbana e impacto_30mm en 3D con PlayAt; bucles a la mitad (ambiente 0,10, viento 0,05, horda 0,10, tren 0,12, motores 0,25, batalla 0,15, rotor 0,22).
2. **Pausa en silencio**: AudioListener.pause = _paused al abrir/cerrar la pausa (Esc).
3. **Recuadro de selección** al arrastrar con el botón izquierdo (borde hueso, relleno tenue), dibujado en pantalla con coordenadas reales (no la RT del pixelado).
4. **Sin estrellas (D-N149)**: nada de estrellas en NightEnded, el parte del kit (UiNocheDemo.ParteNoche) ni la pantalla antigua; al ganar «Sagunto resiste» y se sigue en el mundo. Copiar el noche_sagunto.json nuevo de Hugo (sin resultados.estrellas) y el commit de Nacho que quita las estrellas de NightGame/NightSim.
5. **Boca del arma**: el disparo de los vehículos sale de la boca del cañón (punto de la torreta, Veh.Gun), no del centro; dejar un punto de boca por vehículo para los VFX de Bruno (fogonazo, trazadora desde la boca, impactos).
6. **Rueda para salir al mapa** desde una localización (zoom más allá del máximo) con transición suave y la noche persistente; M como atajo; al acercarse en el mapa sobre una estación se entra. Probarlo en -inputtest.
7. **Aterrizaje y carga del helicóptero (D-N143)**: Helicoptero.LandingClear (claro de 20×20 m sin edificios ni zombis), la U baja el pelotón entero.
8. **VFX de Bruno** (cuando los pase): fogonazo, trazadoras, impactos; partículas.
9. **A\* de vehículos de Nacho** y obstáculos de la infantería (D-N139: rellenar _uw.Obstacles con edificios, muros, tren y vehículos parados; desvío del vehículo atascado > 2 s).
10. **C90 con la tecla C** (OrderC90 con apuntado por clic) y mostrar los tiros que quedan (Platoon.C90Left).
11. **Tutorial guiado D-N150** (Lucía lo especifica): salir al mapa, ir a otra estación, elegir 2 helicópteros con infantería, mandarlos a Sagunto con su ETA, volver a entrar y verlos llegar, aterrizar y desembarcar.
12. **Cartel de Sagunto centrado y carreteras de vuelta** (con el suelo A solo en la tierra).

## Ayuda para mañana
- docs/relevo/scripts-marcos/lote_8nov.py: script ya escrito (sin aplicar ni compilar) que hace los puntos 1, 2, 3, 4 (parcial) y 6 sobre el código de la rama. Revisar antes de ejecutar; usa chr(10)/chr(13) a propósito porque el entorno convierte las barras invertidas.
- Compilar y construir: `bash /tmp/build.sh NocheNN` (copia en el workspace de scratch; si no existe, ver docs/relevo/marcos.md para el comando unity eval) y comprobar con `-inputtest`, `-capdirecta`, `-nightbot`.
- Interfaz v2: la básica en IMGUI está en PrototypeBootstrap.HudV2.cs (franja de tarjetas y formaciones). Falta UI Toolkit, tipografía Inter, minimapa con órdenes, avisos y reloj nuevos, etiquetas «1 Fus» en el mundo.
