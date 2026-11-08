# La noche de Nules: borrador para medir · Hugo (3), 8-nov 19:05

`nules.json` usa el mismo esquema que `noche_sagunto.json`, porque es el único que lee FromJson (Nacho). Lo genera `generar_nules.py`. **SIN MEDIR**: Nacho lo mide en NightSim cuando tenga la geometría de Nules.

## 1. Qué hay dentro
- **Entradas** (Álvaro, `niveles/nules-nivel.md` §5), en claves O1–O4, con nombre y lado del recinto, como pidió Nacho:
  - O1 = Na, por el lado O (vía desde Almenara): 25 %
  - O2 = Nb, por el lado E (vía desde Castellón, infestada): **40 %**, la que más presiona
  - O3 = Nc, por el lado N (pueblo): 20 %
  - O4 = Nd, por el lado S (calle del polígono, contra la puerta de vehículos): 15 %
- **Geometría**: `docs/niveles/estaciones/nules.json` (recinto, 4 puertas, tren del apartado, punto de bajada si está sitiada).
- **Fuerza**: la guarnición de 12 personas de `sim_economia.py`, es decir, fusileros (8) y ametralladores (4). Sin vehículos ni aire.
- **Recursos (caso de referencia)**: 20 u de munición, el mínimo del objetivo «Lleva munición a Nules» de después de la 1.ª noche (Lucía, 8-nov: se cumple al descargar 20 u o más). Materiales, 20 u (supuesto mío). La reserva de Nules empieza con 0 u. Ojo: el tren del capítulo 3 va de Nules a Sagunto y lleva el pelotón, no munición.
- **Recinto**: 124,3 u, ya construido.

## 2. De dónde sale la horda (fácil 2050, normal 2400, difícil 2610)
- Es una regla de tres, no una medida. Sagunto aguanta 5250 en la normal con 26 soldados, el Dragón y 2 VAMTAC. Nules tiene 12 soldados y nada más, y un perímetro más largo, así que tiene en torno al 45 % del fuego: unos 2400.
- **Munición**: 2400 zombis son unas 6 u sin muro. Con las 20 u del tren y los 3,5 u de las dotaciones, debería sobrar munición (p10 ≥ 2 u). **Sin el tren** (solo las dotaciones, 3,5 u, unos 1400 zombis) **Nules cae**. Es lo que se busca: que el objetivo de la munición tenga sentido.
- Mismas palancas que Sagunto sin aire: 853, 1000 y 1086 ‰.

## 3. Qué hay que medir (Nacho) y criterio
1. **Caso A** (este JSON): la normal tiene que dar ≥95 % de victorias, la pila p50 ≥150 y la munición p10 ≥2 u. La difícil, entre el 50 y el 80 %.
2. **Caso B**, con un pelotón de fusileros de más (el que pueda llevar el jugador en el tren de la munición): para ver cuánto lo regala.
3. **Caso C**, con 0 u de munición en el almacén: tiene que perderse casi siempre.
Si A no cumple, ajusto BASE en `generar_nules.py` con la curva que salga. No cambio el reparto sin hablar con Álvaro.
