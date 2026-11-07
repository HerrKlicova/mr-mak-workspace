# Relevo de Nuria (dirección de sonido) · 7-nov-2026

## Estado
- Efectos de la Noche26 terminados: 402 tomas de ElevenLabs (SFX v3) en `entregas/sonido-noche26/brutos/`, másteres WAV en `master/` (398 MB), 450 MP3 para Unity en `unity/Audio/` (69 eventos, 68 MB), con `manifiesto.csv`.
- Demo para Lucía: `entregas/sonido-noche26/demo/demo_lucia.mp3`.
- Falta que Marcos lo integre en `C:\Dev\TBD\Assets\TBD\Resources\Audio\` (Unity tenía TBD abierto; no lo toqué). La guía para él es `docs/sonido/integracion-noche26.md`.

## Decisiones vigentes
- Nombres para `Sfx.cs`: `sfx_<evento>_<cerca|media|lejos>_<n>` con distancia y `sfx_<evento>_<n>` sin ella. Lo que falta de una distancia se deriva con paso bajo y eco.
- Sonoridad por grupo y picos: tablas `LUFS` y `PICO` de `herramientas/sonido/postproceso_sfx.py`.
- `impacto_hormigon` e `impacto_metal` llevan un prompt nuevo (golpe único con ataque fuerte). El anterior daba un siseo plano.

## Rutas
- Herramientas: `herramientas/sonido/` (`generar_sfx.py`, `postproceso_sfx.py`, `catalogo_sfx.json`).
- Descartes: `entregas/sonido-noche26/descartes/` (rondas 1 a 3) y `descartes_mudos/` (de antes).

## Trampas conocidas
- El pico no separa las tomas malas de las buenas. Hay que mirar la envolvente: un impacto bueno da más de 25 dB de rango y uno malo, menos de 15 dB y plano. Los sostenidos (gemidos, sirenas, rotor) son planos por naturaleza.
- `generar_sfx.py` solo crea las variantes que faltan. Para regenerar, primero se mueve la toma a `descartes/`, y su máster también: el posproceso salta los WAV que ya existen.
- La clave solo sale de `ELEVENLABS_API_KEY`. Nunca se imprime.

## Noche50 — rotor NH90 (7-nov)
- Diagnóstico: en la build suenan DOS rotores a la vez. `PrototypeBootstrap.Vehicles.cs:230` sigue con `Sfx.Loop("sfx_rotor_nh90", …)` (MP3 viejo de 5 s, 2D, una sola clave para todos los helicópteros). `PrototypeBootstrap.Fx.cs:82` pone el rotor 3D a 0 en los estados 0 y 3 (vuelta y aterrizaje) aunque las palas sigan girando. Además, el «duck» de `Sfx.Update` (×0,55 durante 1,5 s tras una alerta) se aplica de golpe a los bucles.
- Entrega: `entregas/sonido-noche50/` (8 tomas v3 en `brutos/`, bucles en `master/`, 6 OGG mono 48 kHz q6 en `unity/Audio/`, origen en `unity/Audio/origen.csv`, medidas en `medidas_b.csv` y `medidas_c.csv`, escucha `prueba_rotor_4x.mp3`). Herramientas en `entregas/sonido-noche50/herramientas/`.
- Coste: 267 caracteres por toma de 22 s (8 tomas = 2.136).
- Trampa: la unión de un bucle que empieza en un golpe de pala da por sí sola 1–2,6 dB entre ventanas de 50 ms. Hay que compararla con el mismo salto en la toma original continua (`rms_natural`), no con 1 dB a secas.
- Trampa: `character_count` tarda en actualizarse. La primera lectura tras generar dio 0; hay que volver a leerlo al cabo de un rato.

— Nuria (Sonido)
