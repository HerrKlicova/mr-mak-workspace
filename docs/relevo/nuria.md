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

— Nuria (Sonido)
