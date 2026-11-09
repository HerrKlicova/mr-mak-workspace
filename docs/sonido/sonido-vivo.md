# Sonido vivo (Nuria, 9-nov noche)

Eugenio quiere que el juego «se sienta vivo». Todo está en la rama **`nuria/sonido-vivo`** de tbd (675e59d5), que sale de `iker/escenario-inicio` (db8fb237). **No está compilado.** Solo toca la vista: ni la simulación ni el hash. No se han gastado créditos. Todo usa clips que ya estaban en `Resources/Audio`, salvo el barrido de zoom, que es nuevo y está sintetizado (`herramientas/sonido/zoom_sfx.py`).

| Momento | Sonido | Dónde (código) | Vol. | 2D/3D | Regla |
|---|---|---|---|---|---|
| **Horda que se acerca, de lejos** | `sfx_horda_lejos_1` (más de 80 m) y `sfx_horda_media_1` (35–70 m), en bucle | `PrototypeBootstrap.SonidoVivo.cs`, `HordaLejana()` (lo llama `NightAudio`) | 0,06 / 0,07 × tamaño | **3D** en el centro de la horda (400 / 250 m) | Se oye venir de su lado. Al llegar calla y entra la «cerca» que ya había (que no se toca) |
| Aviso «la horda se acerca» | `sfx_horda_acercandose_1..5` (sin uso hasta ahora) | igual | 0,7 | 3D | Una vez por noche, cuando el centro de la horda pasa a menos de 120 m de la estación |
| **Llegada del tren** | `sfx_tren_llegada_1..6` (sin uso hasta ahora) | `TrenPanel.Vigilar()` | mapa 0,3 / zona 0,9 | mapa 2D / zona 3D en el andén | Como el pitido de salida en el mapa: como mucho uno cada 10 s. La salida ya sonaba (SalidaTren) |
| **NH90 en la zona** | arranque, despegue, pasada y toma (`SonidoNH90`, ya estaba escrito y nadie lo llamaba) y ralentí | `HelicopterosZona()` | 0,8–0,9; ralentí 0,15 × Rpm | 3D | Según `Veh.State`: 0→1 arranque, al pasar de 1,5 m despegue, →3 toma. Pasada: en vuelo, a más de 8 m/s y a menos de 25 m del foco, una cada 20 s. El rotor en vuelo sigue igual |
| **Atropello** | `sfx_impacto_carne_1..8` y, con 3 o más, `sfx_zombi_caida` | `RunOver()` → `AtropelloSonido()` | 0,55 / 0,4 | 3D en el morro | Hueco de 0,12 s: con turbo no se amontona |
| **Tren perdido** (zona) | `sfx_tren_caido_puertas_1..5` | `PrototypeBootstrap.Emboscada.cs`, junto al rótulo «Se ha perdido el…» | 1,0 | 3D en el tren | — |
| **Tren perdido** (mapa, fuera de pantalla) | `sfx_tren_caido_puertas` | `OperationsMap3D.SonidosRed()`, cuando `LastAmbush.TrainLost` pasa a true | 0,6 + Duck 2 s | 2D | Al abrir el mapa no suena lo que ya había pasado |
| **Estación atacada** (mapa) | `sfx_alarma_ataque` | `SonidosRed()`, al empezar un asedio (`Started`) | 0,3 + Duck 2 s | 2D | La alarma de la zona, más baja. El aviso ámbar de antes (anuncio sin tropa) sigue igual |
| **Zoom zona → mapa** | `sfx_zoom_salir_mapa_1..5` (**nuevo**) | `LeaveToMap()` | 0,8 | 2D | Barrido de aire que sube y acaba en un chasquido de radio. Dura 0,85 s, con el fundido de 0,6 s |
| **Zoom mapa → zona** | `sfx_zoom_entrar_zona_1..5` (**nuevo**) | `OperationsMap3D.EnterZone()` | 0,8 | 2D | Barrido que baja y acaba en un golpe grave suave |

Los 10 OGG nuevos están a −29,0 LUFS y como mucho a −15,7 dBFS de pico, con la misma configuración de importación que `sfx_ui_tecla` (copiada en su .meta). En el repo van en `Resources/Audio` (LFS) y en `entregas/sonido-vivo/` de mr-mak-workspace.

## Para Iker y Marcos

1. Fusionar `nuria/sonido-vivo` y compilar. Son 8 líneas en 6 archivos más un archivo nuevo, y no debería chocar con nada.
2. En el log, comprobar que no sale `FALTA` para los clips nuevos.
3. Escuchar sobre todo **la horda lejana**. Eugenio pidió (n.º 17) que la horda «solo se oiga si te acercas, y bajito». Por eso va a 0,06, por debajo del ambiente de noche: si aun así molesta, bajarla a 0,03 o quitarla poniendo `vLejos = vMedia = 0`.
4. Los clips reutilizados (`tren_llegada`, `horda_acercandose`, `impacto_carne`) se generaron el 7-nov y nunca han sonado en el juego. Si alguno suena mal, decídmelo y lo cambio por otro.

## Lo que falta y costaría créditos (cuando haya permiso)

- **Atropello propio:** golpe en chapa con crujido, 5 variantes (unos 300 créditos). `impacto_carne` es un impacto de bala y vale de momento.
- **Horda vista desde el mapa:** un rumor de masa a kilómetros para cuando haya una migración, a −40 LUFS y 5 variantes (unos 600 créditos).
- **Paso del tren por la vía, en la zona** (traqueteo que pasa), para los trenes que cruzan sin parar. 5 variantes (unos 500 créditos).
- Las 3 variantes del atardecer que faltan (D-N157, prompt nuevo, unos 1.000–1.500 créditos).

Las llamadas de pago desde el PC solo funcionan si Eugenio lanza él el comando.

— Nuria (Sonido)
