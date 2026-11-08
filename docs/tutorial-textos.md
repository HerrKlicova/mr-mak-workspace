# Tutorial nuevo: textos de los capítulos 0 a 3 (D-N154) · Lucía (3), 8-nov

Textos para el motor del tutorial de Iker y para los capítulos de la zona de Marcos. El capítulo 4 (apoyo aéreo desde Bétera, D-N173) está en `/mnt/project-files/tutorial-cap4-iker.md`, con mi revisión del 8-nov al final.

**Reglas comunes (de la D-N150 y la D-N154, sin cambios):**
- Tarjeta arriba a la izquierda, debajo de los avisos, con «Capítulo 1 · Paso 2 de 6».
- Lo que hay que tocar late con un anillo hueso d4d0cc. Nada de rojo en el tutorial: el rojo es para ataques y brechas.
- Se puede saltar desde la primera tarjeta o desde el menú de pausa («Saltar tutorial»). Solo sale la primera vez, en fácil y normal. La difícil no lo tiene.
- La horda espera agrupada mientras dura un capítulo con combate. El reloj y el mundo siguen.
- Si el jugador se desvía, la tarjeta repite su texto y no hay castigo.
- Las teclas marcadas con * son propuestas. Si Marcos o Iker usan otra, se cambia el texto, no la tecla.
- Tono: militar sobrio, frases cortas, segunda persona, sin humor.

## Capítulo 0 · Intro
- La intro de la D-N158, con la variante que se elija (`intro-variantes.md`). Se puede saltar con un clic o con la barra espaciadora.
- Al acabar, primera tarjeta, con el juego en pausa:

> «Sagunto es tu base. Aquí empieza todo.»
> [Empezar] [Saltar tutorial]

## Capítulo 1 · Defender Sagunto de día
Hora de juego: día 1, a las 10:00. Ataque pequeño: 300 zombis por O1, que entran en 20 s (Hugo, `economia/reparar-costes.md` §4). Medido por Sara con el bot quieto: 200 de 200 victorias y sin pila. Las puertas ya están cerradas y la tropa repartida dentro y fuera (D-N151).

| # | Texto | Se resalta | Se cierra cuando |
|---|---|---|---|
| 1.1 | «Mueve la cámara con W A S D. Acércate y aléjate con la rueda.» | Barra de atajos | La cámara se ha movido y se ha usado la rueda |
| 1.2 | «Se acerca un grupo desde el oeste. Las puertas se han cerrado: para entrar tendrán que romper el muro.» | El grupo de zombis y las puertas | 4 s |
| 1.3 | «Tienes tropa dentro del muro y tropa fuera, junto a los vehículos. La de fuera es la primera que recibe.» | Las dos tarjetas de pelotón de fuera | 4 s |
| 1.4 | «Selecciona un pelotón: clic en él, en su tarjeta o con su número (1 a 5). Para coger varios, arrastra un recuadro.» | Las tarjetas de pelotón | Hay un pelotón seleccionado |
| 1.5 | «Clic derecho para moverlo. Ponlo junto al muro oeste.» | El tramo oeste | Orden de mover dada |
| 1.6 | «Arrastra con el clic derecho para dibujar un frente. Prueba una formación con F1 a F4.» | Teclas F1–F4 | Se ha dado una formación o un frente |
| 1.7 | «Esc abre el menú de pausa y congela la partida. Desde ahí también se salta el tutorial.» | Botón del menú | Se ha abierto y cerrado el menú |
| 1.8 | «Ahí vienen. Disparan solos cuando los tienen a tiro.» (3 s) | — | La horda empieza a avanzar |
| 1.9 | (Mientras dura el ataque, una sola línea:) «Vigila la vida del muro arriba. Si un tramo cae, entran.» | Barra del muro (D-N122) | Ataque rechazado |
| 1.10 | «Ataque rechazado. Esta noche vendrán muchos más.» | — | 4 s, y pasa al capítulo 2 |

- Si el jugador tiene vehículos fuera: en 1.3 se añade «Los vehículos también disparan. Selecciónalos igual que a la tropa».
- La tecla C del C90 **no** se enseña aquí: sale una tarjeta suelta la primera vez que hay un grupo de 40 zombis o más dentro del recinto a menos de 30 m de un pelotón de fusileros (Hugo, `economia/entregas/c90/`; coincide con la tromba de la D-N148). Sale **una sola vez en toda la partida**, no cada noche, y no sale si el tutorial se ha saltado («Tus fusileros llevan C90. Tecla C para lanzarlo. Se repone al recargar»).

## Capítulo 2 · Reparar
Para que haya algo que reparar aunque el jugador defienda bien, el **tramo de HESCO pegado a la puerta oeste** (60.000 de vida, no la puerta) **empieza el día 1 dañado, al 45 %**, por el ataque de la noche anterior (D-N163). Si el ataque del capítulo 1 rompe más, mejor.

| # | Texto | Se resalta | Se cierra cuando |
|---|---|---|---|
| 2.1 | «El muro oeste está tocado. Esta noche no aguantará así.» | El tramo dañado (contorno ámbar) | 4 s |
| 2.2 | «Pulsa B* para entrar en Obras. El combate sigue mientras construyes.» | Botón Obras | Modo obras abierto |
| 2.3 | «Los tramos dañados salen marcados. Haz clic en el del oeste.» | El tramo | Tramo seleccionado, se ve el coste |
| 2.4 | «Reparar cuesta materiales y tiempo. Confirma con clic.» | El coste en el panel | Orden confirmada |
| 2.5 | «Van los zapadores. Mientras reparan no disparan, y el ruido atrae a la horda.» | Los zapadores y el icono de ruido | Tramo por encima del 70 % |
| 2.6 | «Si un tramo cae del todo, se reconstruye, y solo con la zona limpia. Sale caro.» | — | 4 s |
| 2.7 | «Sal de Obras con B* o con clic derecho en vacío.» | Botón Obras | Modo obras cerrado |

## Capítulo 3 · Pedir refuerzos a otra estación (D-N154, D-N172)
Idea de Eugenio: como defender Sagunto parece difícil, se aprovecha para enseñar a ir a otra estación y mandar desde allí unidades a Sagunto. La estación es **Nules**, la de al lado (D-N156), que tiene **su propio tren parado en el andén** y un **destacamento de refuerzo: 1 pelotón de fusileros** (sin Lince: con él la noche queda regalada, medido por Hugo y Nacho).

**Cuándo**: en la primera noche, **cuando la pila pasa de 150 por primera vez o 60 s reales después del primer contacto con el muro, lo que ocurra antes** (en fácil, el 15 % de las noches no hay tromba; Hugo y Nacho). El refuerzo llega como un rescate a mitad de la tromba, no como un regalo antes de la noche. En este capítulo **la horda no espera**: la presión es la lección. El ETA lo da el juego; en el texto no se escribe ninguna cifra.

| # | Texto | Se resalta | Se cierra cuando |
|---|---|---|---|
| 3.1 | «¡Están trepando el muro! Sagunto sola no aguantará. Nules, la estación de al lado, puede mandarte ayuda.» | La pila en el muro y el aviso | 4 s |
| 3.1b | (Si salta por los 60 s, en lugar de la 3.1:) «La horda está en el muro. Sagunto sola no aguantará mucho. Nules, la estación de al lado, puede mandarte ayuda.» | La horda en el muro y el aviso | 4 s |
| 3.2 | «Sal al mapa: aleja la cámara del todo o pulsa M. El combate sigue mientras estás fuera.» | Barra de atajos | Vista de mapa abierta |
| 3.3 | «Haz clic en Nules. Castellón está infestada; de momento, ni te acerques.» | Los 3 nodos; anillo en Nules | Panel de Nules abierto |
| 3.4 | «Nules tiene un tren en el andén y un pelotón de fusileros. Abre Preparar tren y sube el pelotón.» | La tarjeta del pelotón y el botón Preparar tren | Pelotón a bordo |
| 3.5 | «Destino: Sagunto. Mira el ETA y envíalo.» | Nodo de Sagunto, el ETA y el botón Enviar | Tren en marcha |
| 3.6 | «Vuelve a Sagunto y aguanta: doble clic en Sagunto o acerca la cámara. La ayuda llega en 0:xx.» | Nodo de Sagunto | Vuelta a la zona |
| 3.7 | (Al llegar el tren:) «Sagunto está sitiada: el tren espera en la puerta este. Baja la tropa.» | El tren fuera del muro y el botón Descargar | Tropa en tierra (D-N152, D-N166) |
| 3.8 | «Llévalos al flanco sur y dispara desde ahí. Si te pegas a la horda, irá a por ellos.» (D-N175) | Punto del flanco sur, hacia (100; 34) | Orden de mover o de atacar dada; acaba el tutorial |

- Mientras el tren va de camino, en el mapa sale «Refuerzos de Nules · llegan en 0:xx». Al llegar, aviso en hueso: «Tren a las puertas de Sagunto».
- Al acabar no hay tarjeta de fin. La noche sigue hasta acabar con la horda (D-N164).
- **Después de la primera noche** sale un objetivo, sin tarjetas de tutorial: «Lleva el tren a Nules con munición». Es el viaje con carga de la D-N154, y enseña la carga y el apoyo terrestre (paso por paso: carga, unidades, vehículo en plataforma, destino y ETA).

## Para cada uno
- **Iker**: motor del tutorial, capítulos 0 y 3, y la tarjeta suelta del C90. Para el capítulo 3: el tren parado en Nules y el destacamento de refuerzo (1 pelotón de fusileros y 1 Lince), que solo existen con el tutorial activo; Preparar tren desde Nules; el viaje Nules–Sagunto con la regla de la D-N166; el aviso de radar de 6 h que abre el capítulo; el doble clic en Sagunto (D-N170), o al menos el clic; y el objetivo de después de la noche.
- **Marcos**: capítulos 1 y 2, el tramo oeste al 45 % el día 1 y la horda en espera. Para el capítulo 3: que el tren de Nules entre en la zona de Sagunto y se pueda descargar en el andén; si la estación está sitiada, que se quede a las puertas y solo baje la tropa (D-N152 y D-N166); y que los refuerzos aparezcan en el plantel con su tecla.
- **Hugo**: el tamaño del ataque de día (hecho: 300, medido por Sara) y comprobar que la primera noche con el destacamento de Nules no queda regalada.
- **Bruno**: anillo que late y contorno ámbar de la capa de obras.
- **Sara**: la -nightbot recorre el tutorial completo y también se prueba saltándolo.

— Lucía (Diseño)

## Objetivo después de la primera noche · «Lleva munición a Nules» (Iker 826c567, revisado por Lucía (3) el 8-nov a las 15:30)
Sale al amanecer, después de la primera noche. **También sale si el tutorial se ha saltado**, porque es un objetivo de campaña y no una tarjeta del tutorial. En difícil no sale. No lleva anillo ni pausa: va en la lista de objetivos.

| # | Texto | Se cierra cuando |
|---|---|---|
| Título | «Lleva munición a Nules» | — |
| 1 | «Carga munición en el tren de Sagunto: abre Preparar tren.» | Hay munición a bordo |
| 2 | «Sube tropa o un vehículo en plataforma: protegerán la carga.» (Es opcional: se salta solo si el jugador envía el tren sin escolta.) | Escolta a bordo o tren enviado |
| 3 | «Destino: Nules. Mira el ETA y envíalo.» | Tren en marcha |
| 4 | «El tren va hacia Nules. Llega en {eta}.» | Tren en Nules |
| 5 | «Tren en Nules. Descarga la munición.» | ≥ 20 u de munición en el almacén de Nules |
| 5b | (Si Nules está sitiada:) «Nules está sitiada: la carga se queda a bordo hasta que se despeje.» | Asedio levantado (vuelve al 5) |
| 6 | «Devuelve el tren a Sagunto.» | Tren en Sagunto |
| Fin | «Cumplido. Nules tiene munición para aguantar.» | — |
