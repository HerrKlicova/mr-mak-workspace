# Ambiente de día de Sagunto y Nules, y atardecer (D-N157)

Encargo de Lucía (la primera horda de día), 9-nov-2026. Nuria (Sonido).
Escucha: https://claude.ai/artifact/9LsaV25QzwJsWQahQSexzV

Noviembre en la huerta: viento suave, pocos pájaros y la vía a lo lejos. Sin chicharras ni grillos, sin música y sin voces.
Todo es mono, 44,1 kHz y OGG Vorbis (q6), con el nivel horneado. Al importar, Normalize va apagado (AudioImportRules.cs).
Herramienta: `herramientas\sonido\ambiente_dia.py`. Brutos: `herramientas\sonido\brutos_ambiente_dia\`. Medidas completas: `medidas.json`.

## Entrega

| Archivo | Qué es | LUFS | Pico | Duración |
|---|---|---|---|---|
| `sfx_amb_dia_sagunto_1..5.ogg` | Pueblo con estación junto a la huerta. Bucle | −53,0 (las 5) | −38,4 a −36,4 dBFS | 20,0 s |
| `sfx_amb_dia_nules_1..4.ogg` | Naranjal con acequia muy baja y la vía lejos. Bucle | −53,0 (las 4) | −38,4 a −32,8 dBFS | 20,0 s |
| `sfx_amb_atardecer_1..2.ogg` | Transición del día a la noche, sin bucle | −51,5 (las 2) | −35,7 a −33,6 dBFS | 20,0 s |
| `prueba.mp3` | 20 s de Sagunto, 20 s de Nules, el atardecer y 10 s de la noche actual | | | 70 s |

**Faltan variantes**: hay 4 de Nules (no 5) y 2 de atardecer (no 5). El tope de 5.500 créditos no dio para más (ver Créditos).
Entre las variantes de cada sonido no hay diferencia de nivel (0,0 dB; el encargo pedía ±0,5 como mucho).

## Medidas de referencia (la noche)

Medidas con ebur128 en `C:\Dev\TBD\Assets\TBD\Resources\Audio\` (8baca89), sin tocar los archivos. Son idénticos (md5) a los de `entregas\sonido-noche46\unity\Audio\`.

| Archivo | LUFS integrado | Pico | Formato |
|---|---|---|---|
| `sfx_amb_estacion_pequena_1.ogg` | −30,0 | −15,5 dBFS | estéreo, 48 kHz, 20 s |
| `sfx_amb_viento_1.ogg` | −30,1 | −17,1 dBFS | estéreo, 48 kHz, 20 s |

- Nivel efectivo de la noche en la zona (cámara cerca): −30,0 + 20·log10(0,10) = **−50,0 LUFS**.
  Con la cámara alejada del todo (far01 = 1): estación −66,5 y viento −56,1 (0,05), unos −55,7 en conjunto.
- Día: 3 dB por debajo → **−53,0 LUFS** sonando a 1,0.
- Atardecer: 1,5 dB por debajo → **−51,5 LUFS**.
- Ojo, mono frente a estéreo: el ambiente de noche es estéreo y bastante decorrelado (su mezcla a mono mide −31,7, no −30,0). Los nuevos son mono. Si Unity reparte un clip mono 2D a plena ganancia en los dos canales, se oirá unos 3 dB más fuerte de lo que dice su cifra de LUFS frente al estéreo. No lo he podido comprobar en el motor: hay que escucharlo en la zona y, si el día se come la noche, bajarlo a 0,7.

## Comprobaciones

- **Costuras de los bucles (en el OGG)**: los 9 bucles tienen exactamente las mismas muestras que su bucle de origen (de 881.946 a 882.016, sin hueco). El salto en la unión (de 0,00001 a 0,0013) es menor que el percentil 99 de los saltos entre muestras de cada bucle (0,0005–0,0024), así que no hay clic. El salto de nivel en la unión (ventanas de 50 ms, de 0,2 a 1,8 dB) es menor que el p95 de los saltos de dentro del bucle (de 1,5 a 4,3 dB). Fundido cruzado de potencia constante de 1,5 s, cortado en cruces por cero.
- **Sucesos que se reconocerían al repetirse**: ninguna ventana de 400 ms pasa de 3,3 dB sobre la mediana (el límite era 6).
- **Insectos**: el detector se calibró con los grillos de Nules de noche (bulto de 11,9 a 25,1 dB a unos 4,4 kHz, presente en el 100 % de las tramas de 0,5 s) frente a viento, acequia y la noche actual (≤ 5,8 dB). Se descarta una toma si tiene un bulto ≥ 8 dB presente en ≥ 60 % de las tramas. Las entregadas están todas por debajo: hay dos de Sagunto con un bulto de 10–14 dB, pero solo en el 9–27 % de las tramas, que son pájaros sueltos y no un coro.
- **Música o voces**: 0 tonos sostenidos en todas (el detector da positivo con 4 notas sintéticas sobre ruido).
- **Atardecer**: trinos (2–8 kHz) en los primeros 7 s frente a los últimos 7 s, y el grave (< 400 Hz) de los últimos 5 s frente a los primeros 5 s.
  - `_1`: 11 → 0 trinos, el viento sube 5,1 dB.
  - `_2`: 4 → 1 trino, el viento queda igual (−0,3 dB). Es la más plana de las dos.
- No puedo escuchar: todo se ha comprobado midiendo. Que Lucía y Eugenio escuchen `prueba.mp3`.

## Descartes (5 de 16 tomas)

| Toma | Motivo |
|---|---|
| `dia_nules_b_v03` | Nivel inestable: 7,2 dB de variación en la ventana de 20 s |
| `dia_nules_c_v01` | La costura salta 2,5–2,6 dB en las dos ventanas posibles, más que el p95 de dentro (2,0) |
| `atardecer_a_v01` | Los pájaros no se callan: 14 trinos al principio y 10 al final |
| `atardecer_b_v01` | Casi sin pájaros al principio (1 trino en 0–7 s) |
| `atardecer_b_v02` | Sin pájaros al principio (0 trinos) |

El prompt b del atardecer dio 0 de 2: no empieza con pájaros. Si se repone, hay que usar el prompt a.
**Fallos de mis instrumentos que he corregido antes de descartar** (el primer pase descartó 10 de 15):
1. El suelo de «toma muda» (−54 LUFS en bruto) venía de ambientes que iban a −32. Aquí el objetivo es −53, así que tomas de −54/−55 eran válidas. El suelo nuevo es −62 LUFS o un pico de −55 dBFS.
2. Los detectores de tonos e insectos medían la prominencia contra la mediana de todo el espectro. En un ambiente con más graves que agudos, cualquier trama de 250–700 Hz «destacaba» de 30 a 45 dB, y salían «músicas» falsas. Ahora usan la prominencia local y la persistencia, calibradas como se dice arriba.
3. Límite de nivel inestable de los bucles: lo subí de 4,0 a 4,5 dB. `sagunto_4` (toma a_v01) da 4,03 dB, con la costura limpia (0,26 frente a 3,83) y sin sucesos (3,1 dB).

## Créditos

- Contador antes: 85.632. Después: 90.963. **Gasto: 5.331 créditos** (tope 5.500), a unos 12,1 créditos por segundo.
- De ellos, **1.164 se perdieron por un fallo mío**: en la primera toma de calibración, el modo `extra` no creaba la carpeta de brutos. El guardado falló, la API cobró los 4 reintentos y no se guardó nada. Ya está corregido (`mkdir` antes de lanzar).
- Para completar las 5 + 5 + 5 harían falta unos 4 tomas de atardecer (prompt a, 20,3 s) y 1–2 de Nules (22 s): unos **1.300–1.600 créditos** más.

## Notas para Marcos (integración)

- **Zona de día**: `Sfx.Loop("sfx_amb_dia_<estación>_<n>", 1.0f, false)` mientras sea de día. Sagunto para el pueblo con estación y Nules para el naranjal.
- **Atardecer**: unos 20 s de juego antes de la noche, `sfx_amb_atardecer_<n>` a 1,0, una vez (no es bucle). Fundido cruzado con el ambiente de día al empezar. En sus últimos 3 s, fundido cruzado de potencia constante con el ambiente de noche (`sfx_amb_estacion_pequena_1` a 0,10, como ahora). La prueba hace exactamente eso.
- **Mapa de día**: propongo `sfx_amb_dia_sagunto_<n>` en 2D a 0,3 (unos −63,5 LUFS), para que no haya silencio. Hoy el mapa solo tiene `sfx_batalla_mapa` de noche.
- Se calla al pausar, como el resto (sonido 3D con silencio en la pausa).
- **Mapa (integrado)**: el mapa a 0,3 lleva además `Sfx.Duck` de −6 dB (ya integrado), así que el día no tapa los avisos del mapa.
- **Volumen en la zona**: `DiaZonaVol` está a 1,0 sin escuchar (03bffef). Si al escucharlo en la zona el día se come la noche (posible por lo del mono frente al estéreo, ver arriba), hay que bajarlo a **0,7**.
- **Variantes fijas elegidas por Lucía (ya en el juego)**: `sfx_amb_dia_sagunto_1`, `sfx_amb_dia_nules_2` y `sfx_amb_atardecer_1`, integradas por Marcos en 03bffef (repo TBD). No se tocan: las variantes nuevas solo se añaden con números libres (`ambiente_dia.py completar`).
- **Variante por semilla**: `n = 1 + hash(estación, día) % N`, con N = 5 en Sagunto, 4 en Nules y 2 en el atardecer. Cuando se completen, N = 5 en los tres (pendiente: la generación de las 6 tomas que faltan está bloqueada a la espera de permiso, 9-nov). Es determinista, así que la misma estación y el mismo día dan siempre la misma variante.
- Importación: mono, Vorbis, sin Normalize, Load Type Streaming o Compressed in Memory (son 20 s).
