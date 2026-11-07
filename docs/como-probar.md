# Cómo probar «La primera noche en Sagunto» (build de la noche del 6 al 7 de noviembre)

Marcos (Programación). Build: `C:\Dev\TBD\Builds\Noche13\TBD.exe` (o la última `Noche##`). Código: rama `marcos/noche-prototipo` del repositorio TBD (incluye el PR #24 de Nacho). Datos de Hugo: `StreamingAssets/Noche` (noche_sagunto.json, balance_noche.csv, balance_unidades.csv).

## Jugar
1. Abre `TBD.exe`. Menú: **Jugar** (entra directo a la zona de Sagunto de noche), Continuar (si hay partida guardada con F5), Cómo se juega, Opciones (volumen general, música, efectos, pantalla completa), Salir.
2. Empiezas a las 22:00 con 5 pelotones (fusileros, ametralladores, granaderos, tiradores, zapadores), el Dragón, 2 VAMTAC y el NH90 en el helipuerto. La Colmena llega por O1–O4 en 6 oleadas. Ganas si al amanecer siguen en pie la estación y el tren; si no, pierdes. Reloj ×28 (17 minutos).
3. Controles de noche: clic o arrastre = elegir pelotones; clic derecho (sin arrastrar) = mover; **A** + clic = atacar moviéndose; **S** mantener; **D** emplazar hacia el cursor; **G** alto el fuego; **T** reabastecer; clic en una tarjeta de vehículo = elegirlo (clic derecho: mover; el NH90 despega con la primera orden y aterriza si lo mandas al helipuerto). Cámara: flechas o bordes de pantalla (WASD NO), **Z** acerca, **X** aleja, rueda (15 % por muesca, centrada en el cursor), botón derecho arrastrando gira, **R/F** inclina. **F2** muestra la depuración, **F5** guarda, **F9** captura. Alejar del todo y una muesca más avisa; otra seguida sale al mapa.
4. Al amanecer sale el parte de la noche (sin velo) con **Seguir** (abre la noche siguiente +10 %). La derrota para el mundo y ofrece Volver a empezar o Menú principal.
5. **Vista cercana del tren**: en el mapa (escena Union, sin entrar en la zona) pulsa **V**; **V o Esc** vuelve. Z/X o rueda cambian el zoom.

## Banderas de línea de comandos (QA)
`-menu-auto` (salta el menú y juega) · `-nightclock N` (reloj ×N; 28 normal, 200 para ver el final en 2:24) · `-nightshots` (capturas a 12/40/90/150 s en `Captures`) · `-nightlose` (cae la estación a los 15 s) · `-vehdemo` (VAMTAC contra el muro oeste y NH90 despegando, con capturas) · `-trainview` (entra y sale tres veces de la vista cercana y captura el mapa al volver) · `-stress10k-sagunto -ortho N` (prueba de rendimiento, escribe `Captures/stress_10k_fps.txt` con FPS, p99 y peor fotograma) · `-nightbot` (bot de Nacho; vehículos sin disparar) · `-vehfuego` (con `-nightbot`, deja disparar a los vehículos) · `-nightwin` (estación y tren inmortales: sale el parte de victoria con «Seguir») · `-nightdense` (10.000 zombis a los 20 s) · `-menu-shot` (capturas del menú y de Opciones) · `-escala 1.0` (quita el ×1,3 del dibujo) · `-logFile ruta` (log de la build).

## Log
Líneas `[NOCHE]` para Hugo y Sara: inicio, una por oleada y el resultado final; y `[NOCHE-FPS]` cada 20 s.

## Conocido (honesto)
**Límite conocido (decisión de Mak, 7-nov): el fuego de los vehículos es local, fuera del hash.** `-vehfuego` (bot de Nacho + vehículos disparando) mide el techo, pero que el hash sea idéntico en los dos mundos con él no prueba determinismo del fuego de vehículos, porque no entra en el hash. Meterlo por la cola única queda para después de P1. Munición de vehículos y combustible no se descuentan; los vehículos atraviesan muros (la puerta E4 de Nacho no está integrada); no hay embarcar ni desembarcar; el HUD aún usa texto sobre cajas, solo con parte del arte de Bruno; zona y mapa son escenas distintas (D-N91 pide una sola: deuda); el sonido está generado pero sin pulir.

---

# Cómo probar el juego (H3 y H4), en 5–10 minutos

Marcos (Programación), noche del 5 al 6 de noviembre. Todo lo de aquí lo he comprobado yo en el Editor, y también desde una copia limpia del repositorio (clon nuevo, importado desde cero en 2 min 18 s, sin errores de compilación).

## 1. Abrir el proyecto
1. Unity Hub → **Add → Add project from disk** → `C:\Dev\TBD`. Versión: **6000.3.28f1** (la 6.3 LTS).
2. Abre la escena **`Assets/Scenes/Union.unity`** (el mapa 3D de operaciones). Pulsa **Play**.
3. No hace falta nada más. Los CSV de balance de Hugo se leen de `Assets/TBD/Data`: si cambias uno, se nota en la siguiente partida.

## 2. Teclas

**Mapa (escena Union)**

| Tecla | Qué hace |
| --- | --- |
| W A S D o flechas | mover |
| Q / E | girar |
| R / F | inclinar |
| rueda del ratón | zoom. A menos de 2 km de una estación **se entra en la zona** |
| botón derecho + ratón | girar y inclinar |
| Espacio | pausa |
| 1 / 2 / 3 | velocidad x1 / x2 / x4 |
| J | ir a la alerta más urgente |
| F8 | **emboscada de prueba** (solo para probar) |
| Intro | entrar en la emboscada activa |
| F3 | apagar la prueba de desincronización |
| F9 | captura (carpeta `Captures`) |

Una alerta crítica nueva baja la velocidad a x1 sola (D-N11): vuelve a pulsar 3.

**Zona de estación** (entras acercando la cámara a una estación)

| Tecla | Qué hace |
| --- | --- |
| 6 | pelotón a bordo: dispara desde el tren parado (sin bajas) |
| 0 | pelotón a pie (arriesgado) |
| K | reembarcar a los que estén a menos de 20 m del tren |
| 3 | mover o parar el tren |
| 2 | abrir o cerrar la puerta |
| 1 / 4 | más zombis (de prueba): al tejado / por el oeste |
| 5 | trazadoras |
| B | muros libres (clics = puntos, clic derecho corta) |
| P | pausa de la zona |
| **M** o alejar del todo | **volver al mapa** (los vivos vuelven a la mancha) |
| WASD, Q E, R F, rueda | cámara, como en el mapa |
| 7 / 8 / 9 | hora del día; `[ ]` pixelado; `, .` paleta |
| F9 / F10 | captura / grabar fotogramas para un GIF |

**Zona de emboscada (desmonte)**: las mismas, más:

| Tecla | Qué hace |
| --- | --- |
| Z | marcha atrás (la salida de emergencia: los primeros 40 m quedan libres) |
| X | adelante (lo frena el tapón de cuerpos) |
| C | parar |

## 3. Recorrido recomendado
1. **Día 1.** Pulsa Play. Pulsa **3** (x4). El reloj arranca a las 05:30. El Tren 1 sale de Valencia a las 06:00. Arriba a la derecha está el informe de la Colmena (cuando aparece una entrada nueva se ve ahí).
2. **Zona (H3).** Con la rueda, acércate a **Castellón** o a **Barracas**: empiezan «amenazadas» (la guarnición de la horda inicial). Entras en la zona. Pulsa **6** y mira cómo dispara el pelotón desde el tren. **4** añade zombis. **M** te devuelve al mapa.
3. **Caza (H4).** Hacia las 11:00 del día 1 el Tren 1 sale de Castellón y una manada lo sigue: aparece **ES-1** en el informe.
4. **Aviso y primer asedio.** Con x4 y unos 5–6 minutos reales llegas al día 2. A las 07:00 aparece la alerta **«Horda hacia Valencia en 3 h (10:00)»** (el objetivo se sortea con la semilla: puede ser otro nodo). Pulsa **J** para ir a ella. A las 10:00 el nodo pasa a **asediado** y entra **ES-2** en el informe. (Medido en el Editor: aviso a las 07:00, asedio a las 10:00 del día 2.)
5. **Emboscada y desmonte (H4).** Pulsa **F8** (emboscada de prueba) e **Intro**. Estás en el desmonte, con el tren parado, el tapón delante y la horda bajando por los taludes. Pulsa **6** (tropa a bordo), espera unos segundos (hay abatidos) y prueba **Z** (marcha atrás) y **C** (parar). **M** para salir: la red resuelve la emboscada, libera el tren y gasta la munición de su carga.
   - Si en la partida real no respondes en 30 min de juego, el tren pierde el 20 % de la carga. Una emboscada real necesita días de horario fijo: por eso F8 existe.

Una sesión limpia de punta a punta: unos 8 minutos.

## 4. Repeticiones doradas (un solo comando)
Con el Editor **cerrado** (si no, no se puede abrir el proyecto dos veces):

```bash
"C:\Program Files\Unity\Hub\Editor\6000.3.28f1\Editor\Unity.exe" -batchmode -nographics -projectPath C:\Dev\TBD -executeMethod TBD.EditorTools.GoldenBatch.Run -quit -logFile -
```

Verifica **G1 a G5** (red, zona, tropas, bucle mapa-zona y desmonte), escribe `Captures\golden_editor.txt` y sale con código **0 si todo es idéntico** y 1 si algo difiere. Con el Editor abierto: menú **TBD → Repetición dorada (todas)**. En un proyecto limpio tardó 2 min 18 s (importación incluida); con el proyecto ya importado, ~40 s.

Las pruebas de lógica pura (173 comprobaciones, incluida la ecuación de masa y la prueba de reparto de asedios):

```bash
cd C:\Dev\TBD\Dotnet\TBD.Sim.Tests && dotnet run -c Release
```

Añadir `TBD_SEEDS=20` mide además 20 partidas completas contra la referencia de Hugo (tarda unos 5 minutos).

## 5. Qué es provisional
- **Arte.** El desmonte son escalones coloreados por altura, sin sombra ni relieve continuo. El tren apenas contrasta. La curva y el puente usan el desmonte como decorado. Nada de esto es el arte final.
- **Relieve del mapa.** Es de sustitución, no son datos reales (Copernicus sigue pendiente de registro; las cifras reales de elevación no se usan).
- **Balance.** Los números son los de Hugo, en `Assets/TBD/Data/*.csv`. La emboscada sin respuesta (20 %) y las utilidades de emboscada y corte son prototipos.
- **Horda inicial.** Es guarnición con correa y paisaje estático: no la recluta el director. Las amenazas del día 1 son las del escenario de prueba (dos guarniciones pegadas a Castellón y Barracas).
- **F8 y las teclas 1 y 4 de la zona** son de prueba. No valen para coop.
- **Una sola zona a la vez** y un solo encuentro de emboscada a la vez.
- **La tropa a pie** que se queda en la zona al salir se pierde (aún no es guarnición del nodo).
- **Coop** no existe todavía: lo que hay es lockstep con dos mundos en una misma máquina, y su prueba de desincronización.

## Novedades de la Noche29 (7-nov)
- La noche es persistente: M (o alejar la rueda al tope) sale al mapa y la noche SIGUE fuera de pantalla (NightSim de Nacho); al volver a Sagunto se recrean los zombis donde van. Solo Volver a empezar o Menu reinician.
- Vehiculos: disparan solos (fuego libre); con un vehiculo seleccionado, G = alto el fuego, A = fuego libre, T = recargar del almacen (parado junto al tren; el NH90 en su plataforma).
- Trazadoras que viajan (no laseres) y fogonazos; soldados con el arma en la mano (SoldadoArmado de Teo); noche azul v3; texturas nuevas de los vehiculos.
- Banderas nuevas de QA: -leaveat N / -returnafter N (salir y volver), -shotsat 236,242, -sinrecarga, -luz luna|ambiente|focos, -colorcasos, -capdirecta, -lowrtsrgb, -vehfuego.
- Pendiente (no hecho): marca de seleccion, destino y formaciones al estilo Total War; pose de apuntar; parches del suelo; color del HUD (doble sRGB sin resolver); boton del parte; D-N118 de las tarjetas.

## Noche50: build P0 de esta noche (7-nov)
- Ejecutable: C:/Dev/TBD/Builds/Noche50/TBD.exe (Jugar en el menu). Rama marcos/noche-prototipo.
- Incluye el sonido de Nuria (449 MP3 con la mezcla por distancia segun el zoom: fusil, ametralladora, granada, canon, tirador; lecho de horda, ambiente, viento, motores, rotor, tren, alarma de ataque, impactos). Sin AudioMixer: volumenes directos.
- Hecho tambien: noche persistente, trazadoras que viajan, fogonazos, soldados armados, vehiculos con textura de Teo y fuego libre (G alto el fuego, A fuego libre, T recarga), puertas con muro, titular de derrota D-N133.
- Luz de noche: la v3 de Bruno (la E queda descartada hasta que Lucia elija entre G1-G5 en docs/capturas/qa29).
- Pruebas: -gradsweep (5 gradaciones en el mismo fotograma), -capdirecta.

## Control de unidades (Noche38 en adelante)
- Seleccion: clic o arrastre con el boton izquierdo; se ve un anillo bajo el pelotón y un punto bajo cada soldado (vehiculo: doble anillo con proa).
- Mover: clic derecho; la marca y la ruta se quedan hasta que llegan.
- Frente: clic derecho y ARRASTRAR dibuja el frente (el pelotón mira a la izquierda del arrastre; varios pelotones se reparten por la linea); se ve la silueta fantasma; aspa si el hueco cae fuera del recinto.
- Formacion: F1 línea, F2 cuña, F3 columna, F4 bloque. A+orden = atacar moviendose, S mantener, D emplazar, G alto el fuego, T recargar.
- Camara: flechas o bordes, Z/X zoom, y GIRA con el boton CENTRAL del raton si hay unidades elegidas (sin seleccion, con el derecho). La depuracion pasa de F2 a F12.

## Controles de la Noche50 (P0 de Eugenio)
- Camara: W A S D o flechas, Z/X zoom, rueda, boton central gira. Esc = pausa (Continuar / Salir al mapa / Menu principal). M = salir al mapa (la noche sigue).
- Seleccion: 1-5 pelotones (Mayus suma; doble pulsacion centra), 6-8 vehiculos, clic y rectangulo; clic derecho mueve, clic derecho + arrastrar dibuja el frente; F1-F4 formacion.
- Vehiculos: G alterna fuego libre / alto el fuego de todos; T recarga. El NH90 despega solo cuando hay horda.
- Las teclas de depuracion (4 zombis, 7-9 gradacion, B, H, N...) solo con -debug. Panel de iconos retirado. Al ganar, Seguir sigue en el mundo sin reiniciar.
