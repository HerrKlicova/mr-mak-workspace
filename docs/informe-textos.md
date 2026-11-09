# Informe de inteligencia (D-N160) · textos · Lucía (Diseño), 08-11

Pantalla V1 de Bruno (dos columnas, con remaches). Tono: parte militar sobrio, frases cortas en presente, sin adjetivos de miedo. La Colmena se nombra como «la Colmena», nunca como «los zombis». Las cifras siguen la regla de precisión (24:30 y 25:15): con ojos, centenas «~2.400»; sin ojos, millares con interrogación «~2.000?»; en Enjambre, «2.400» sin tilde. Se escribe solo lo que existe en la partida: si una estación no tiene tropa, no se inventa.

Los campos `{así}` los rellena el juego. Una línea que se queda vacía no se muestra.

## 1. Cabecera
- `INFORME DE INTELIGENCIA · INTSUM {nn}` · `{DTG}` (formato «D41 · 2030A»)
- `De: Sección de Inteligencia · {estación_mando}` · `Periodo: {DTG_inicio} – {DTG_fin}`
- Marca: `USO INTERNO`

## 2. Resumen (una línea, la más importante del informe)
Por estado de la Colmena:
- Dispersa: «La Colmena está dispersa. Sin amenaza concentrada sobre la red.»
- Al acecho: «La Colmena está al acecho y se junta {dirección} de {estación} ({cifra}). Ataque probable la noche del {día}.»
- Enjambre: «ENJAMBRE. La Colmena marcha sobre {estación} ({cifra}). Ataque esta noche.»
Si hay asedio anunciado, manda sobre lo anterior: «Asedio sobre {estación} a las {hora}. {cifra}.»

## 3. Situación de la amenaza (máximo 3 líneas, la más peligrosa primero)
- «{estación}: masa {dirección}, {cifra}, rumbo {rumbo}. Llegaría hacia {DTG}.»
- Memoria de tráfico: «{tramo}: el tren {n} pasa a la misma hora {k} días seguidos. Lo ha aprendido.»
- Memoria de atención: «{zona}: la Colmena se aparta de donde miramos y crece donde no.»
- Trébol desconocido: «{estación}: movimiento sin identificar {dirección} de la estación.»

## 4. Fuerzas propias (una línea por estación con algo)
- «{estación}: {n} pelotones{, Dragón}{, n VAMTAC}. Munición {u} u{. Víveres {v} u}.»
- Sin tropa: «{estación}: sin tropa.»
- Bétera: «Bétera: {n} NH90 en base{, uno rearmando}.»

## 5. Sin novedad en
- «{lista de estaciones y tramos sin actividad}.» Si no hay ninguno, la línea no sale.

## 6. Valoración (una o dos frases, con probabilidad en palabras: «probable», «posible», «poco probable»)
- Estación sin defensa ante asedio: «Si {estación} no recibe tropa y munición antes de {DTG}, cae {cuándo}.»
- Tren sin escolta hacia una estación sitiada: «El tren {n} llegará a {estación} sitiada sin escolta. Se perderá con su carga.»
- Señal de la Colmena en 5–6: «La Colmena se agita. Si abrimos más nodos esta semana, pasará a enjambre.»
- Nada urgente: «Sin cambios previstos en las próximas 24 horas.»

## 7. Necesidades (lo que se pide, accionable)
- «≥ {u} u y un pelotón en {estación}.»
- «Un NH90 sobre {estación} para identificar el movimiento.» (cuando hay trébol)
- «Escolta para el tren {n}.»

## 8. Firma
- `Cap. Ibarra` · `Inteligencia · fuentes: {fuentes}` (por ejemplo «Mora (observación), Llorens (radio)»)

## Avisos de la Colmena (entradas CO, glifo sin color)
- CO-1 · Pasa a Al acecho: «La Colmena ha dejado de vagar. Se junta y escucha.»
- CO-2 · Pasa a Enjambre (resaltada): «ENJAMBRE. Has crecido demasiado deprisa: {n} nodos en 7 días y huella {h}. Atacará más de una estación a la vez.»
- CO-3 · Baja de Enjambre a Al acecho: «El enjambre se deshace. La Colmena sigue atenta.»
- CO-4 · Baja a Dispersa: «La Colmena se dispersa. Ventana para crecer.»
- Ámbar del panel de avisos (señal 6): «La Colmena se agita: si abres más nodos, irá a por ti.»

## Otros avisos ámbar ya decididos (mismo tono)
- «Sin escolta: {estación} está sitiada.»
- «{zona} sin defensa: llega la horda.»
- «Saca el tren del apartado: con asedio, espera fuera de la puerta oeste.»
- Objetivo del día 2 (D-N179): «Defiende Nules antes de la noche: manda tropa y munición (≥ 20 u).»

## Añadidos 08-11 (a partir de la propuesta de Bruno, revisados por Lucía)
- Resumen, asedio ya empezado: «Asedio sobre {estación} en curso. {cifra}.»
- Amenaza, ataque en marcha: «{estación}: la Colmena ataca por el {lado}. {cifra}.»
- Valoración, estación sin tropa bajo ataque: «{estación}, sin tropa, está bajo ataque. Cae esta noche si no llega ayuda.»
- Fuerzas propias en la estación de mando, mientras la red no cuente los pelotones de casa: «{estación}: guarnición{, Dragón}{, n VAMTAC}. Munición {u} u.» Cuando Nacho exponga el número, vuelve a la plantilla normal con «{n} pelotones».

## Añadido 09-11 00:12 · CO-0 (presentación de la Colmena)
- CO-0, una sola vez por partida, la primera vez que se abre el mapa de la red después del tutorial, con estado Dispersa: «La Colmena está dispersa. Si creces despacio, no se fija en ti.»
- No sale al cargar una partida guardada ni si el estado ya no es Dispersa (en ese caso manda el CO que toque). Sin sonido propio: usa el de Dispersa.

## Añadido 09-11 00:18 · Memoria de tráfico sin número de tren ni días
- Mientras la red no dé el número de tren ni los días seguidos: «{tramo}: el tren pasa siempre hacia las {hora}. Lo ha aprendido.» Cuando los dé, se vuelve a la plantilla completa.
- Los textos CO que mandan son los de este documento (CO-0 a CO-4 y el ámbar de la señal 6). La lógica de cuándo sale cada uno es de Nacho; las palabras, de Diseño.
- Precisión del 09-11 00:28 sobre el CO-0: si la partida cargada todavía no lo ha mostrado (Nacho guarda el «ya salió» con la partida), sale la primera vez que se abra el mapa de la red, siempre que el estado sea Dispersa. Lo que se evita es repetirlo, no que salga tras una carga.

## Añadido 09-11 01:22 · Huecos cubiertos por la red (Nacho, 28ba0fd)
- Memoria de tráfico: con IntelTraffic() sale la plantilla completa. Sin racha (partidas antiguas) sale la versión corta.
- Memoria de atención: {zona} es el nodo propio olvidado, el que lleva más de 6 h sin mirarse. Si hay varios, el que más ha crecido. Ejemplo: «Nules: la Colmena se aparta de donde miramos y crece donde no.»
- Fuerzas propias: Sagunto vuelve a «{n} pelotones» (IntelForcesAt) y la línea provisional de «guarnición» se retira. La red no cuenta las bajas de la noche en curso: las cifras son las del comienzo del periodo, sin avisarlo en el texto.
