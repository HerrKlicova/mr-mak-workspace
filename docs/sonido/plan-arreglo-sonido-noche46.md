# Arreglo del sonido de la Noche46 (Nuria → Marcos) · 7-nov

Eugenio jugó la Noche46 y el sonido no funciona: todo suena muy alto y de golpe al acercarse, los bucles se cortan, el helicóptero suena igual a cualquier distancia, el ambiente molesta, la horda arranca de forma horrible y salta música de repente (puntos 3, 4, 8 y 17 a 21). **Tiene razón en que el sonido no es 3D.** Lo he comprobado leyendo una copia de `Sfx.cs` y de los `PrototypeBootstrap.*.cs` (en Unity no he tocado nada).

## 1. Diagnóstico
| Lo que oye Eugenio | Causa en el código |
|---|---|
| No suena en 3D | `Sfx` usa **una sola AudioSource en 2D** (spatialBlend 0) para todos los efectos. La posición que recibe `Play(evento, pos)` no se usa, y casi todas las llamadas pasan `Vector3.zero`. |
| Todo exageradamente alto | Los 462 clips se importaron con **Normalize activado**, así que Unity los sube todos al máximo y se pierde la mezcla por distancia que venía en los archivos (D-N134). No hay mixer y suenan unos 10 bucles a la vez, todos a volumen fijo. |
| Al acercar suena todo de golpe | La capa cerca, media o lejos salta en ortho 14 y 34 sin fundido. Los impactos solo suenan con ortho < 14 y entran todos a la vez al cruzar ese umbral. |
| Bucles con cortes | (a) `Loop` **pausa** con volumen 0 y luego sigue a mitad de clip sin fundido. (b) Los bucles son **MP3**, y el MP3 mete un hueco de silencio en el punto de bucle (relleno del codificador). (c) El tono de la AudioSource compartida cambia en cada disparo y desafina lo que ya sonaba. (d) Solo hay 32 voces reales. |
| Helicóptero igual a cualquier distancia | Suenan **dos** bucles a la vez: `sfx_nh90_rotor_1` a 0,5 fijo y `sfx_rotor_nh90`, que se atenúa por la distancia a la cámara. Pero la cámara siempre está a unos 120 u del foco, así que ese factor se queda fijo en 0,7. |
| Música que salta | `mus_oleada` entra de golpe a 0,55 con más de 200 zombis y se pausa al bajar de 200 (Night.cs:498). |
| Arranque de la horda horrendo | Al empezar la oleada suenan tres avisos a la vez (`aviso_horda`, `horda_acercandose` y `sfx_alerta_oleada`). El lecho de la horda llega al máximo con solo 150 zombis, entra la música y, como la precarga está desactivada, el primer play carga el clip en ese momento. |
| Ambiente intrusivo de lejos | Ambiente a 0,5 fijo y viento que **sube** al alejar (hasta 0,6). Es justo al revés de lo que pide. |
| El BTR dispara como un fusil | Con normalize, todo a 2D y el mismo volumen, el cañón de 30 mm no se distingue. El impacto suena en 2D a la vez que el disparo, no en el punto donde cae. |

## 2. La solución
**Un oído de RTS.** Un único AudioListener **en el suelo, en el foco de la cámara**, a una altura que crece con el zoom: `h = clamp(ortho × 1,6; 12; 140)`. Todos los efectos con posición suenan en 3D con una curva de atenuación propia: plana hasta 15 m, −5 dB a 44 m, −13 dB a 100 m y silencio a 220 m. El resultado es el que describe Eugenio:
- Con zoom cerca, oyes lo que tienes debajo y en su sitio, a izquierda o derecha.
- Al alejar, el oído sube y todo baja de volumen y se vacía. Lo lejano queda como un rumor.
- El helicóptero o el Dragón suenan al acercarte a ellos, no siempre.

Te dejo el código listo:
- **`Sfx.cs` nuevo** (sustituye al viejo y mantiene su API, así que compila sin tocar nada más; las llamadas viejas suenan en el centro de la pantalla):
  - pool de 40 fuentes 3D, cada una con su tono;
  - topes por grupo: armas 12, impactos 8, zombis 4, vehículos 4, muros 3, interfaz 2 y alertas 2; si no hay hueco, se roba la voz menos importante;
  - bucles con fundido (0,6 s de entrada y 0,8 s de salida) que nunca se pausan: bajan a 0, paran a los 3 s y al volver arrancan en un punto al azar;
  - las alertas bajan el resto −5 dB durante 1,5 s.
- **`Editor/AudioImportRules.cs`**: quita Normalize, pone mono en los efectos 3D y activa la precarga. Bucles en Compressed In Memory. Incluye el menú **TBD > Audio > Reimportar con las reglas**.

## 3. Pasos para Marcos (en este orden)
1. Copia `Sfx.cs` encima de `Assets/TBD/Scripts/View/Sfx.cs` y `AudioImportRules.cs` en `Assets/TBD/Editor/`. Luego usa **TBD > Audio > Reimportar con las reglas**.
2. En **Project Settings > Audio**, pon Max Real Voices en **64**.
3. **Bucles en OGG.** Borra de `Resources/Audio` los MP3 de los bucles (peloton, horda_cerca/media/lejos, batalla_mapa, zombi_golpe_muro, tren_ralenti, vamtac_motor, dragon_motor, nh90_rotor, amb_* y fuego_crepitar) y copia los `.ogg` con el mismo nombre que te paso en `entregas/sonido-noche46/unity/Audio/`. Sin el MP3, el bucle no tiene hueco.
4. **`PrototypeBootstrap.Fx.cs`: sustituye `NightAudio()` entero por esto:**
```csharp
void NightAudio()
{
    if (_ng == null) return;
    float o = _orthoSize, z = Mathf.Clamp01((o - 10f) / 60f);                 // 0 = Z al máximo, 1 = X al máximo
    Sfx.Ear(_focus, o, _worldCam != null ? _worldCam.transform.eulerAngles.y : 0f);   // OÍDO: cada fotograma
    Sfx.Loop("sfx_amb_estacion_pequena_1", Mathf.Lerp(0.14f, 0.04f, z), false); // ambiente bajo; al alejar, más vacío
    Sfx.Loop("sfx_amb_viento_1", 0.04f + 0.04f * z, false);
    // horda: 3D, en el grupo de zombis más cercano al foco; solo se oye de cerca y bajita
    if (NearestHorde(out var hp, out int hn)) Sfx.LoopAt("horda", "sfx_horda_cerca_1", hp, Mathf.Min(0.3f, hn / 150f), 60f); else Sfx.StopLoop("horda");
    // vehículos: un bucle 3D por vehículo, pegado a él
    foreach (var v in _vehs)
    {
        if (v.Go == null) continue; var p = v.Go.transform.position;
        if (v.Heli) Sfx.LoopAt("rotor" + v.Name, "sfx_nh90_rotor_1", p, v.Rpm * 0.6f, 200f);
        else Sfx.LoopAt("motor" + v.Name, v.Name.StartsWith("Drag") ? "sfx_dragon_motor_1" : "sfx_vamtac_motor_1", p, Mathf.Abs(v.Speed) > 0.5f ? 0.45f : 0.12f, 120f);
    }
    // tren: Sfx.LoopAt("tren", "sfx_tren_ralenti_1", <posición del tren>, 0.3f, 120f);
    bool attack = _ng.State == NightState.Jugando && (_pileNearStation > 0 || _nearTrain > 0);
    if (attack && !_alarmOn && Time.unscaledTime - _alarmT > 20f) { _alarmT = Time.unscaledTime; Sfx.Play("alarma_ataque", Vector3.zero, 0.6f, 1f); }
    _alarmOn = attack;
}

bool NearestHorde(out Vector3 pos, out int n)   // centroide de los zombis a menos de 25 m del más cercano al foco
{
    pos = default; n = 0; int best = -1; float bd = 90f * 90f; var f = new Vector2(_focus.x, _focus.z);
    for (int i = 0; i < _zomPos.Count; i++) { float d = (_zomPos[i] - f).sqrMagnitude; if (d < bd) { bd = d; best = i; } }
    if (best < 0) return false; var c = _zomPos[best]; Vector2 sum = Vector2.zero;
    for (int i = 0; i < _zomPos.Count; i++) if ((_zomPos[i] - c).sqrMagnitude < 625f) { sum += _zomPos[i]; n++; }
    sum /= n; pos = new Vector3(sum.x, 0.5f, sum.y); return true;
}
```
   Con esto ya no se llaman `sfx_horda_media_1`, `sfx_horda_lejos_1` ni los motores en 2D. Si `_zomPos` no se rellena cada fotograma en la noche, usa la lista de posiciones de zombis que tengas.
5. **`PrototypeBootstrap.Vehicles.cs:187`** (disparo del vehículo):
```csharp
var gun = new Vector3(v.Pos.x, v.Alt + 2.2f, v.Pos.y); var hit = new Vector3(tp.x, 0.5f, tp.y);
Sfx.PlayDistAt(dragon ? "canon_30" : "ametralladora", gun, 1f, dragon ? 0.3f : 0.2f);
if (dragon) Sfx.PlayAt("impacto_30mm", hit, 0.9f, 0.12f);      // la explosión suena DONDE cae
```
   Quita la `cola_urbana` 2D de esa línea. El daño en área del 30 mm ya existe (3 m, `sqrMagnitude < 9`). Falta la miniexplosión visual en `hit` (Bruno o tú).
6. **`PrototypeBootstrap.Vehicles.cs:224`**: **borra** la línea de `sfx_rotor_nh90`. Es el rotor duplicado; ahora va en `NightAudio`.
7. **`PrototypeBootstrap.Night.cs:352`** (disparos de infantería), usando la posición del tirador:
```csharp
var from = new Vector3(man.X / 1000f, 1.2f, man.Y / 1000f); var to = new Vector3(s.AimX / 1000f, 0.5f, s.AimY / 1000f);
if (s.Splash) { Sfx.PlayDistAt("granada_40", from, 1f, 0.25f); Sfx.PlayAt("explosion_granada", to, 0.8f, 0.2f); }
else if (s.Kind == InfKind.Ametrallador) Sfx.PlayDistAt("ametralladora", from, 0.9f, 0.15f);
else if (s.Kind == InfKind.Tirador) Sfx.PlayDistAt("tirador", from, 1f, 0.2f);
else Sfx.PlayDistAt("fusil_rafaga", from, 0.8f, 0.1f);
```
   Pon este bloque después de calcular `man` y quita la línea vieja (y la `cola_urbana` 2D).
8. **`Night.cs:289`** (impactos): quita la condición `_orthoSize < 14f` (ahora atenúa la distancia) y pasa la posición del impacto:
   `Sfx.PlayAt("impacto_carne", hitPos, 0.35f, 0.04f); Sfx.PlayAt("zombi_caida", hitPos, 0.3f, 0.06f);` y `zombi_muerte` 1 de cada 4 a 0,25.
9. **`Night.cs:299`**: cambia `Sfx.Play("sfx_zombi_muerte", 0.3f, …)` por `Sfx.PlayAt("zombi_muerte", new Vector3(zs[i].Pos.x, 0.5f, zs[i].Pos.z), 0.25f, 0.15f);`.
10. **`Night.cs:171` y `:173`** (inicio de oleada): quita `aviso_horda`, `horda_acercandose` y `sfx_alerta_oleada`. Como las oleadas desaparecen (punto 13 de Eugenio), cuando la horda se detecte por primera vez basta con `Sfx.Play("radar_contacto", Vector3.zero, 0.5f, 5f);`.
11. **`Night.cs:498`**: **borra** la línea de `mus_oleada`. Durante la noche no hay música.
12. **`Persist.cs:35`**: deja `sfx_batalla_mapa_1` a 0,2 en vez de 0,3.

## 4. Lo que hago yo ahora (en el PC, con ElevenLabs v3)
- **Cañón del BTR (el Dragón) nuevo y mucho más pesado**: `canon_30` cerca, media y lejos, con 8 variantes por capa. Disparo grave y lento de 30 mm, con estampido y eco.
- **Impactos explosivos del 30 mm**: `impacto_30mm`, 8 variantes. Pequeña explosión con tierra y metralla, para que se note el daño en área.
- **Bucles en OGG sin hueco** y un ambiente nuevo más vacío (`amb_estacion_pequena`, más silencio y menos elementos).

Te los paso con los mismos nombres. Basta con copiarlos encima de los viejos (y en los bucles, borrar antes el MP3).

— Nuria (Sonido)
