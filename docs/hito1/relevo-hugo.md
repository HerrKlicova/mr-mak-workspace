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
- 11-11 23:59 · Lucía, objetivo de combate para calibrar con Nacho: k 4–6 disparos por zombi; sin línea, seco a mitad SIN morir entero (se retira o aguanta con bajas); con línea, limpia con 0–2 bajas. Se corrige el combate, no la munición.
- 11-11 00:00 · Iker (iker/nucleo-v2): Red.TextoLinea saca X de la vuelta medida; «midiendo la vuelta…» hasta la primera. Cerrado.
- 11-11 23:10 · Terreno v2 de Álvaro: vía igual (1250 m, 16 palés); caserío a 213 m de B (antes 237). El modelo ya usaba 200 m: sin cambios en los resultados.
- 11-11 23:25 · Nacho: k medido; puntería 6000 → k 5,4 (4,8 con munición limitada). Sin línea: seco ~58, se retira 40/40, aniquilado 1/40. Cifras: 35 cartuchos/soldado; caja = 3 cargadores (105) porque con 140 limpiaba sin línea el 7,6 %; B = 1 caja; línea 4 cajas; sostiene 49 %. Falta prueba con línea (Nacho).
- 11-11 23:25 · Unidad de la puntería: UnitsWorld.HitScalePm va en milésimas; 6000 = probabilidad de acierto de la tabla actual (fusil y MG) ×6; 1000 = sin cambio. Solo en Mundo (Hito 1), no en balance_unidades.csv. Lucía aprueba 35 cartuchos y caja de 105; se cierra con la prueba de Nacho con línea.
- 11-11 23:56 · CERRADO en NightSim (Nacho, 100 semillas): sin línea 0/100 limpio, 0 bajas, se retira; con línea 96/100, 1 baja, p50 11,5 min. Iker tenía 120 por caja: corregir a 105 (Mundo.CartuchosPorCaja).
- 11-11 23:57 · Lucía da por CERRADAS las cifras del Hito 1. Pendiente de otros: Sara lo comprueba con ventana cuando haya build (paso del pelotón seco). Iker: caja 105.
- 12-11 01:01 · Marcos: 450 ticks/caja (=15 s a 30 t/s) y salida a 1920 ticks: cuadra. Vuelta vacía hasta limpiar: previsto. Propuesto a Iker/Nacho: al limpiar el caserío, los 4 palés pasan al almacén de B cuando vuelve el pelotón; la línea los lleva a A en 2 vueltas; nadie más produce material.
- 12-11 01:05 · Coste de vía acordado (§5): en metros enteros, sin redondeo por tramo; borrar devuelve 100 % en Hito 1; A = coste real A–B + 2. Espera coste real de Iker con la curva.
- 12-11 01:12 · Coste real (Iker): recta 14,9 palés, guion A–P–B 17,0 → A = 19 palés (guion + 2). Iker proponía 20.
