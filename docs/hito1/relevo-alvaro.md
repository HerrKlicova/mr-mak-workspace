# Relevo de Álvaro (Niveles) · Hito 1

Actualizado: 11-nov ~23:15.

## Hecho
- **Terreno de 2 × 2 km** ([terreno-hito1.md](terreno-hito1.md)): alturas en RAW y PNG de 16 bits, usos, posiciones (A, B, caserío, 100 zombis y depósito), 77 obstáculos de visión y plano con cotas. Está en `docs/hito1/terreno/`. Generador determinista en `docs/niveles/herramientas/terreno_hito1.py`.
- A Hugo: el caserío queda a 237 m de B y entre A y B hay 1234 m en recta (contad 1250 de vía).

## Ramas y repos
- mr-mak-workspace, main: `docs/hito1/` y el generador.
- Repo del juego: rama `alvaro/hito1-terreno`, con los mismos archivos en `Assets/StreamingAssets/Hito1/`, para Marcos. Solo datos, sin código.

## Falta
- Plantillas de pueblo y de ciudad en ruinas.
- Que Marcos confirme en Unity si hay que voltear Z en el RAW (SIN VERIFICAR).

## Congelado
- El pulido del 19 (Nules y E4): está en `docs/niveles/nules-nivel.md` §17–19 y en `sagunto-nivel.md` §10.25. La rama `alvaro/nules-los` (b19027fd) se le pasó a Iker.
