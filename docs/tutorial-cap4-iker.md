# Capítulo 4 del tutorial: apoyo aéreo desde Bétera (D-N173) · Iker, 8-nov

Para que lo revise Lucía. Está programado en `TutorialGuion.Cap4` (iker/red-estaciones c73a83e). Es una adaptación de `tutorial-refuerzos.md` con el aeródromo como origen.

- **Cuándo salta**: la primera vez que el jugador abre el panel del aeródromo en el mapa. Solo en fácil y normal, y una sola vez (lo recuerda la clave «tutorial4.visto»). Si el tutorial principal sigue en marcha, espera a que acabe.
- **Reglas de siempre**: tarjeta arriba a la izquierda con «Capítulo 4 · Paso x de 8», anillo en hueso d4d0cc, nada de rojo. Se puede saltar y se repite el texto si el jugador se desvía.
- **La horda no espera** en este capítulo, porque puede saltar en cualquier momento de la partida.

| # | Texto | Se resalta | Se cierra cuando |
|---|---|---|---|
| 4.1 | «Esto es la base de Bétera. Aquí viven los helicópteros: dos NH90, y pelotones de fusileros para embarcar.» | Las tarjetas de los NH90 en el panel del aeródromo | 5 s |
| 4.2 | «Elige un NH90 y sube un pelotón.» | Las tarjetas de los NH90 y el botón «Con pelotón a bordo» | NH90 con pelotón elegido |
| 4.3 | «Mándalo a Sagunto. Fíjate en el ETA: es lo que tarda en llegar.» | Sagunto en la lista de destinos, el ETA y el botón Enviar | NH90 enviado |
| 4.4 | «Vuelve a Sagunto: doble clic en Sagunto o acerca la cámara.» | El nodo de Sagunto | Vuelta a la zona |
| 4.5 | (Al llegar:) «Ya viene. Mira el borde de la pantalla.» | La flecha del borde (D-N147) | 5 s |
| 4.6 | «Pósalo en un claro de 20 × 20 m: tecla L.» | La tarjeta del NH90 | NH90 posado (la zona, Marcos) |
| 4.7 | «Baja la tropa: tecla U.» | La tarjeta del NH90 | Pelotón en tierra (la zona, Marcos) |
| 4.8 | «Cuando le quede poca munición, volverá solo a Bétera a rearmar. Tarda: tenlo en cuenta.» | — | 6 s; acaba el capítulo |

## Dudas para Lucía
1. ¿Mandar uno o los dos NH90? Lo he hecho con uno, por el riesgo de balance que señala Hugo con dos pelotones de más.
2. En el 4.8 no se escribe el tiempo de la vuelta, porque lo da el ETA del panel: 20 s de tomar tierra, más 30 s de rearme, más el vuelo.
3. El 4.5 sale cuando el NH90 entra en la zona. Si el jugador sigue en el mapa, ve el aviso «NH90 1 llega a Sagunto».

— Iker (Programación)

## Revisión de Lucía (3), 8-nov 15:10: aprobado con estos cambios
Buen trabajo: el orden de los pasos es el del capítulo 3, y así el jugador reconoce el patrón. Los cambios son de tono (militar sobrio, sin «viven») y para enseñar el coste.

| # | Texto definitivo | Cambio |
|---|---|---|
| 4.1 | «Base aérea de Bétera. Desde aquí operan los helicópteros: dos NH90 y pelotones de fusileros para embarcar.» | Tono |
| 4.2 | «Elige un NH90 y sube un pelotón.» | Sin cambios |
| 4.3 | «Destino: Sagunto. Mira el ETA y envíalo.» | Igual que la 3.5 |
| 4.4 | «Vuelve a Sagunto: doble clic en Sagunto o acerca la cámara.» | Sin cambios |
| 4.5 | «El NH90 entra por el borde. Sigue la flecha.» | Más concreto |
| 4.6 | «Pósalo en un claro: tecla L*. El cursor marca dónde cabe.» | No se cita la medida de 20 × 20. Marcos: el cursor del modo posar sale en hueso donde cabe y en gris donde no, nunca en rojo. |
| 4.7 | «Baja la tropa: tecla U*.» | Tecla marcada como propuesta |
| 4.8 | «Cada salida gasta combustible de Bétera. Con poca munición vuelve solo a rearmar, y mientras tanto no lo tienes.» | Enseña el coste, que es la decisión (3 u por salida) |

Las teclas con * son propuestas: si Marcos usa otras, se cambia el texto, no la tecla.

**Dudas:**
1. Uno solo. De acuerdo: la lección es el viaje, no la potencia de fuego.
2. De acuerdo: sin cifras en el texto, el tiempo lo da el ETA.
3. De acuerdo. El aviso «NH90 1 llega a Sagunto» va en hueso, como el del tren. La 4.5 sale solo si el jugador ya está en la zona; si sigue en el mapa, espera a que vuelva.

**Añadido:** si el tutorial se ha saltado, el capítulo 4 tampoco sale (la misma regla que la tarjeta del C90), y en difícil no sale nunca.

— Lucía (Diseño)
