# Paquete para Marcos después del control de las 18:30 · Lucía (3), 8-nov 18:50

Todo decidido y medido en NightSim. Va en este orden, de lo que más pesa en el balance a lo que menos. Cada punto remite a su línea de `decisiones-noche.md`.

0. **IMPRESCINDIBLE ANTES QUE NADA: muro por tramos activo por defecto** (punto 8), sin -tramos. Sara (200 semillas): las hordas nuevas solo dan 100/100/79,5 % con tramos; sin tramos, la difícil sale al 100 %.
1. **Hordas sin aire** (D-N169 ampliada): fácil 4.480, normal 5.250 y difícil 5.700. Paquete en `economia/entregas/noche-sin-aire/` (permil 853/1000/1086).
2. **Quitar el NH90 y el helipuerto de Sagunto** (D-N173). El plantel de Sagunto es de 5 pelotones, 1 Dragón y 2 VAMTAC. El aire sale de Bétera (Iker c73a83e).
3. **Reloj ×103** (D-N161): 25.200 ticks por día en la red y en la zona. Lo cambia Nacho.
4. **Línea de visión** (D-N174): inventario de Álvaro (`niveles/sagunto-linea-vision.md` y su CSV), unos 0,3 ms por tick.
   - El muro propio no tapa a quien está a ≤ 2 m.
   - El AG36 es tiro curvo; el C90, directo.
   - Los terraplenes, las tolvas y el autobús tapan el tiro.
5. **Muro oeste y azotea** (`niveles/sagunto-nivel.md` §10.11 y §10.15):
   - banqueta X 70,5–72,5 con palés de 0,4 m;
   - nidos de la puerta de la vía a 1,5 m (NetWorld.cs:1439);
   - ~~azotea a 11 m~~ **AZOTEA EN SUSPENSO** (8-nov 19:05): la azotea real está a ~5 m, en las alas. Nacho vuelve a medir; hasta entonces no se integra.
   - Las piezas de Teo están en mr-mak.
6. **La horda reacciona a la tropa de fuera** (D-N175): un zombi de fuera con tropa a ≤ 25 m cambia el objetivo a esa tropa, con un tope del 30 % de la horda. La pila y los trepadores no cambian. Puede ir como segundo campo de flujo o como desvío local, como prefieras.
7. **Tutorial:**
   - las 4 señales que faltan: horda_avanza, ataque_rechazado, vehiculos_fuera y tramo_sobre_70;
   - el tren de Nules espera en la puerta este y la tropa baja en (192; 60) (textos 3.7 y 3.8 nuevos);
   - el cursor del modo posar del NH90 va en hueso donde cabe (claro de 25 × 25 m) y en gris donde no.
8. **Muro por tramos** activo por defecto, sin -tramos, con la API de Nacho (3277625).

Corridas después de integrarlo: -inputtest y -nightbot en las tres dificultades, con -batchmode y -nographics (nunca con ventana en el PC de Eugenio). Criterio de la D-N169: normal ≥ 95 %, difícil entre el 50 y el 80 %.
