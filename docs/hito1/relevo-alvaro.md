# Relevo de Álvaro (Niveles) · Hito 1

Actualizado: 11-nov ~23:50. **Lucía aprobó el terreno y las plantillas** (22:58); el coordinador le pasa la rama a Marcos.

## Hecho
- **Terreno de 2 × 2 km** ([terreno-hito1.md](terreno-hito1.md)): alturas en RAW y PNG de 16 bits, usos, posiciones (A, B, caserío, 100 zombis y depósito), 77 obstáculos de visión y plano con cotas. Está en `docs/hito1/terreno/`. Generador determinista en `docs/niveles/herramientas/terreno_hito1.py`.
- A Hugo: el caserío queda a 237 m de B y entre A y B hay 1234 m en recta (contad 1250 de vía).

- **Plantillas** ([plantillas-asentamientos.md](plantillas-asentamientos.md)): pueblo de la huerta (260 × 220 m) y ciudad en ruinas (640 × 640 m), con 5 variantes de cada una (edificios en el esquema de obstáculos, calles, zombis y botín, y plano). Están en `docs/hito1/plantillas/`; el generador es `docs/niveles/herramientas/plantillas_hito1.py`.

## Ramas y repos
- mr-mak-workspace, main: `docs/hito1/` y el generador.
- Repo del juego: rama `alvaro/hito1-terreno`, con los mismos archivos en `Assets/StreamingAssets/Hito1/`, para Marcos. Solo datos, sin código.

## Falta
- Que Nacho y Hugo calibren los zombis de las plantillas; las plantas propias del hospital y el cuartel.
- Que Marcos confirme en Unity si hay que voltear Z en el RAW (SIN VERIFICAR).

## Congelado
- El pulido del 19 (Nules y E4): está en `docs/niveles/nules-nivel.md` §17–19 y en `sagunto-nivel.md` §10.25. La rama `alvaro/nules-los` (b19027fd) se le pasó a Iker.
