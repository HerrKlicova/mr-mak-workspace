# VFX de armas por código (fogonazo, trazadora desde la boca, impacto y miniexplosión). Bruno (Arte técnico), 7-nov

Queja de Eugenio con la Noche55: «las balas no salen de sus cañones, no tienen fogonazos, no hay feedback en los disparos, nada. ni efectos de partículas».

## Por qué ahora no se ve nada (leído en marcos/noche-prototipo 4f0ea7b)
- VehicleFire lanza la trazadora y el fogonazo desde el centro del vehículo a 2,2 m (`v.Pos` + altura), no desde el cañón.
- El fogonazo dura 0,05 s y mide de 0,5 a 1,1 m. Además se crea en la capa del mundo, que se pinta a 1/3 de resolución: dura 1 o 2 fotogramas y se pierde.
- La trazadora del VAMTAC mide 0,07 m de ancho, menos de un píxel del mundo a 1/3, así que parpadea o no sale.
- No hay impacto, ni luz, ni humo, ni casquillos. Las explosiones de la simulación (`StepResult.Blasts`: granadas y C90) no se dibujan en ningún sitio de la vista.

## Qué entrego
`PrototypeBootstrap.VfxArmas.cs` (partial de PrototypeBootstrap, solo vista; no toca la simulación ni el hash):
- **Fogonazo según el arma**: estrella crema en la boca, lengua ámbar hacia delante y destello de luz puntual (pool de 8 luces, de 0,05 a 0,1 s). Tamaños por arma:
  ametralladora ligera o de puerta 0,7 m; ametralladora pesada del VAMTAC 0,9 m; 30 mm del Dragón 1,6 m con cono de 2,4 m; fusil 0,45 m.
- **Trazadora desde la boca**: la SpawnTracer de siempre, pero desde la boca, más ancha (0,10–0,20 m) y en la capa VFX_HD, a resolución completa y con bloom.
  La ametralladora suelta 3 trazadoras por disparo de la vista, separadas 0,09 s.
- **Impacto al llegar la trazadora** (tiempo = distancia / velocidad): polvo y chispas en el suelo, y sangre oscura 4c1008 si da a un zombi.
- **Miniexplosión del 30 mm** con el radio del daño (2,5 m): destello, bola de fuego de menos de 0,25 s, 12 chispas, 10 cascotes, **anillo de polvo del diámetro del daño** (5 m) y humo que queda 1,5–2 s.
  Sirve igual para granada (4 m), C90 (5 m) y cohetes (7 m): VfxBlast escala con el radio.
- **Humo en la boca** (el 30 mm en cada disparo, la ametralladora cada 2 o 3) y **casquillos** de latón 847c34 que salen por la derecha y caen.
- Paleta de 32: crema f0dc9c, ámbar e08c30 (solo en efectos de 0,25 s o menos), oliva gris 605c48, gris pardo 48403c, latón 847c34 y sangre 4c1008. De día, el polvo va en beige b4a080 y oliva claro 88885c.
  Sin d4d0cc ni 982420.
- Capas: lo que brilla (fogonazo, cono, chispas y fuego) va en VFX_HD con el material aditivo TBD/FxAdditive ya existente (`_fxMat`, intensidad HDR de 4 a 6). Lo que es materia (humo, polvo, cascotes, casquillos, sangre y anillo) va en la capa del mundo, para que se pixele con él. Texturas en píxel hechas por código.

## Cómo engancharlo (4 cambios)
1. Copiar `PrototypeBootstrap.VfxArmas.cs` a `Assets/TBD/Scripts/View/` desde el Editor (con su .meta, que Unity crea al importarlo).
2. `PrototypeBootstrap.Vehicles.cs`, VehicleFire (líneas 191–192): cambiar las dos llamadas
   ```
   SpawnTracer(new Vector3(v.Pos.x, v.Alt + ...), ...);
   SpawnFlash(new Vector3(v.Pos.x, v.Alt + ...), ...);
   ```
   por
   ```
   VfxVehicleShot(v, new Vector3(tp.x, 0.8f, tp.y));
   ```
   En la línea 193, quitar `Sfx.Play("impacto_30mm", Vector3.zero, 0.7f, 0.5f);`. El impacto ahora suena donde cae, dentro de VfxBlast, y si no se quita suena dos veces.
3. `PrototypeBootstrap.Night.cs`, justo después de `for (int i = 0; i < _res.Shots.Count; i++) NightShotFx(_res.Shots[i]);` (línea ~245):
   ```
   for (int i = 0; i < _res.Blasts.Count; i++) { var b = _res.Blasts[i]; VfxBlast(new Vector3(b.X / 1000f, 0f, b.Y / 1000f), b.RadiusMm / 1000f, b.Weapon); }
   ```
4. `PrototypeBootstrap.Night.cs`, donde se llama a `UpdateFx();` (línea ~470): añadir `UpdateVfxArmas();` detrás.

Opcional, para la infantería: en NightShotFx, cambiar el SpawnFlash por
`VfxShot(s.Weapon, from + (to - from).normalized * 0.6f, to, s.Hit, tracer, !s.Splash);` y quitar el SpawnTracer.
Con `!s.Splash`, la granada no sale dos veces, porque su explosión ya llega por Blasts.

## Punto de boca por vehículo (SIN VERIFICAR)
VxMuzzle busca primero un vacío llamado **«Boca»** en el modelo; si Teo lo añade al FBX, se usa tal cual. Si no lo encuentra:
- Dragón y VAMTAC: posición del transform del arma (`Canon` y `Ametralladora`, que ya se buscan en MakeVeh) más 2,8 m (Dragón) o 1,1 m (VAMTAC) hacia el blanco.
- NH90: la puerta del costado que mira al blanco, a 1,4 m del eje y 1,3 m sobre la altura de vuelo.
Para ajustarlo: arrancar con **`-vfxboca`**, que deja una marca crema durante 2 s en cada boca. Si la marca cae fuera del cañón, se corrige el largo en VxMuzzle.

## Lo que no he podido comprobar
No tengo Unity aquí: el código no está compilado ni probado. Lo he escrito sobre la API de 4f0ea7b (Veh, Find, _fxMat, LayerFx, _tracerLive, SpawnTracer, Sfx.PlayDistAt y _gradeIndex).
- El brillo HDR depende de que la cámara VFX_HD siga teniendo bloom. Si tras quitar su post (QA29) ya no lo tiene, los fogonazos se ven pero no derraman luz; habrá que subir `_Intensity`.
- Las luces puntuales necesitan las luces adicionales de URP, como los focos.
- Coste: 8 sistemas de partículas compartidos, con Emit por evento. Unas 15 partículas por disparo de ametralladora y unas 50 por explosión. Nada se crea en cada disparo.
