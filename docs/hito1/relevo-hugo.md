# Relevo de Hugo (Economía) · Hito 1 del núcleo v2
Encargo (docs/hito1-reparto.md): cifras del Hito 1 (munición por soldado, munición inicial en B, capacidad y tiempo del tren, material del caserío; sin línea el pelotón se queda seco a mitad del caserío y con ella termina) y consumos por hora y en combate de munición, gasoil, raciones y material para el corte completo. Hecho = tabla con cifras y su medida (NightSim o modelo).

## Estado
- 11-11 23:00 · Arranque. Pulido del 19 congelado (último estado en docs/economia/pulido-19-hugo.md: Nules {m} = techo(horda ÷ 139) + 2, ×20 con 18 u a medias, s1–s2 ganan con 2,2 y 2,1 u).

## Archivos
- docs/economia/hito1/modelo_hito1.py (modelo Monte Carlo del bucle)
- docs/economia/hito1/cifras-hito1.md (tabla de cifras y medida)

- 11-11 23:40 · cifras-hito1.md y modelo_hito1.py hechos. Regla: cargador = 100 × k ÷ 16 (k = cartuchos por zombi; trabajo k = 5 → 30 cartuchos/soldado), caja = 4 cargadores, B = 1 caja, tren 6 plazas (4 cajas A→B, material B→A), ciclo 6,6 min con vía de 1200 m, entrega 36 cajas/h, caserío 4 palés, A 14 palés. Modelo (1000 semillas, k 4–6): sin línea seco a ~50 % y limpio ≤ 1 %; con línea 100 %. Consumos del corte completo en la §2. Enviado a Lucía y a Nacho.

## Falta
- Que Nacho mida k (pelotón de 8 contra los 100 del caserío, 200 semillas) y la prueba con la regla (sin línea ≤ 5 % limpio; con línea ≥ 95 %).
- Que Álvaro fije la longitud de la vía A–B y la distancia B–caserío (pido 150–250 m); recalcular ciclo y material de A.
- Que Lucía fije la escala de tiempo del corte (el Hito 1 va 1:1).
- 11-11 23:55 · Lucía aprueba con k = 5 SIN VERIFICAR (la k la pide ella a Nacho). D-N208: movimiento/combate/trenes 1:1; reloj ×30 (día = 48 min reales); munición y gasoil por acción; raciones y desgaste por día. §2 ajustada (sin consumos en reposo; raciones 3/día; propongo mostrar por viaje/minuto real y no «por hora»).
- 11-11 23:58 · Terreno de Álvaro: vía 1250 m → ciclo 6,7 min (no 6,6); A empieza con 16 palés (13 + 1 por el paso a nivel + 2). Caserío a 237 m de B. Modelo rehecho: sin línea 0 % limpio, seco p50 48; con línea 100 %.
- 11-11 23:59 · Subido a main (916557c). Respondidas a Iker las dudas (6 plazas = huecos de carga; ciclo 6,7 = 225 s de viaje + 180 s de carga). Nacho, medida rápida: 79/100 abatidos, 3000 disparos (~38 por zombi), 8 bajas → k=5 no vale; pedido desglose (disparos/abatido, distancia, minuto de bajas). Propuesta: primero que el pelotón con munición sin límite limpie con 0–2 bajas, luego el cargador = mitad del gasto.
- 11-11 23:59 · Iker metió el tren: vuelta real 430 s (aceleración 0,9 m/s² + 3 s/parada). Acepto 430 (≈7,2 min); texto con la vuelta medida. Línea sostiene 56 % (antes 60).
