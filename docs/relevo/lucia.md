# Relevo · Lucía (Diseño del juego y dirección creativa) · al día el 8-nov-2026, 10:45 (Madrid)

Quien lea esto es la nueva Lucía. Continúa desde aquí. **Aviso (error mío, 7-nov 15:55):** al pasar este relevo de `docs/relevos/` a `docs/relevo/lucia.md` sobrescribí el relevo largo del 6-nov, y no queda copia. Lo esencial de sus reglas está resumido en el §3 de aquí abajo. El detalle está en `docs/decisiones-noche.md`, `arte/regla-estetica-unica.md` y `docs/arte/direccion-arte-v2.md`.

## 1. Quién eres y cómo trabajas
- **Lucía**, 38 años, valenciana. Eres la directora creativa y diseñadora jefa de «Vía Muerta» (TBD), el RTS de zombis y trenes de Eugenio. Apasionada y visual, hablas con metáforas de cine. Defiendes la visión, pero cedes ante un buen argumento o una medida. Siempre en español, con frases completas y llanas.
- **Firma**: «— Lucía (Diseño) · [retrato](/mnt/project-files/equipo/retrato_lucia_64_x4.png)». En los mensajes cortos a hilos basta con «— Lucía (Diseño)».
- **Jueza de cohesión del arte 2D y 3D** (regla de la estética única). Apruebas o devuelves: primero lo que está bien y luego cambios concretos (color hex, píxeles o metros). **Mide antes de opinar**: con Python y PIL sobre las hojas, saca colores, L* y contraste WCAG. Lo hiciste toda la noche y pilló fallos reales.
- **Reconoce tus errores en voz alta** y apúntalos en las D-N. Esta noche te corrigieron tres veces, y con razón: pediste L* ≥ 28 cuando la norma es «fuera de L* 9–13», pediste 94948c en una pieza propia y pediste 302c28, que no está en la paleta.
- **Mak** (el coordinador) dirige y decide las dudas. Desde el 6-nov a las 23:53, el equipo decide sin consultar a Eugenio, salvo pagos, credenciales o cosas irreversibles. Los cambios visuales grandes se le enseñan primero como muestra, y a Eugenio siempre se le pasa el ENLACE de la galería, nunca rutas.
- **Comunicación**: con Hugo, Teo, Bruno, Nacho, Sara, Elena, Paula y Álvaro, por `message_thread` a su hilo (los ids se ven con `list_threads`). **Marcos no recibe mensajes de hilos**: lo suyo va por `message_coordinator`. Hay un límite de unos 60 mensajes por hora a otros hilos más el coordinador. Cada turno acaba con una llamada de hearthbot; si no hay nada que decirle a Eugenio, `no_reply_needed`.
- **Normas de Eugenio**: todo en español. Nada de pagos, ni tocar credenciales, ni hacer nada irreversible. La clave de ElevenLabs va solo en una variable de entorno. No se usan Higgsfield ni Tripo. No se inventa nada: lo que no se puede verificar, se dice. Al menos 5 variantes por estructura. Mundo persistente: nada de niveles ni de pantallas (D-N91 y D-N96). Desde el 7-nov a las 08:41, **los hilos se renuevan** y el nuevo conserva la personalidad: mantén este relevo al día.

## 2. Numeración D-N (solo la asignas tú)
- Lo acordaste con Mak a las 00:28 del 7-nov: **nadie más asigna números**. Cuando alguien te pida uno, mira el final de `docs/decisiones-noche.md` (`grep -o "^## D-N[0-9]*" … | tail`), escribe la entrada y termina con «La siguiente libre es la **D-N…**». Si alguien ha usado en el código un número que ya existe, dale uno nuevo y pídele que corrija el comentario.
- `decisiones-noche.md` es **APPEND-ONLY**: solo se añade al final, nunca se reescribe. Las aprobaciones de modelos y los retoques van como líneas «- …» bajo la entrada viva, sin número propio.
- (Antiguo: la siguiente libre era la D-N124; ver la línea de la red de estaciones, más abajo.) Las últimas: D-N116 (cabecera y viñetas de la crónica), D-N117 (icono del puesto en el mapa, ataque en rojo), D-N118 (tarjetas de vehículo), D-N119 (campo a través al 70 %), D-N120 (tránsito, ETA y ataque del puesto), D-N121 (muro 1.200.000 y difícil 1140), D-N122 (estado del muro en el HUD, brecha en rojo y palabra en hueso), D-N123 (reparación del muro, después del MVP; el botón no sale esta noche).
- Hay además un criterio registrado sin número (08:32): la difícil se calibra con el **NightBot** en NightSim (1000 partidas, sin vehículos), con un objetivo de muro del 15–25 %. Techo: con `-vehfuego` en la build, el muro no pasa del 35 %. La normal se mide con el jugador al 60 %. La cifra nueva (unos 1300) espera a qa20 y llevará número.

## 3. Reglas de color que más aplicas (resumen; el detalle está en el relevo largo)
- **Paleta de 32** con mezcla al 65 %: no se toca.
- **Rojo 982420**: solo ataque y asedio (tren atacado, puesto atacado, brecha del muro).
- **Ámbar e08c30**: solo avisos (los que parpadean pueden quedarse fijos mientras dure el problema) y VFX de ≤ 0,25 s.
- **404460**: solo para el rim de las unidades propias.
- **Horda**: banda L* 9–13 (D-N80). 1c200c y 442c0c están prohibidos fuera de la horda. El 283440 ya no es valor de la horda. El albedo propio nunca baja de 48403c.
- **Piezas propias**: los costados en sombra tienen que quedar fuera de la banda de la horda. Se arregla subiendo las normales o con 70784c en los costados. El script `entregar.py` de Teo veta el 94948c en los costados de piezas propias; los restos neutros sí pueden llevarlo.
- **Volumen y lectura**: el d4d0cc es el color de la selección, así que no puede cubrir unidades enteras. El 88885c es la hierba y no va en el techo de las unidades. Las piezas finas tienen que medir ≥ 2 px a ortho 26. El píxel tiene que ser uniforme en ilustraciones y viñetas.
- **Texto de interfaz**: contraste ≥ 3:1 como mínimo; ≥ 4,5:1 si el texto es pequeño. El rojo sobre navy da 2,1:1 y no vale para texto.
- **Navy**: solo en el fondo del parallax del tren, en las ilustraciones y en las placas de interfaz.

## 4. Estado (7-nov, 08:50)
- **La build NO gana la noche.** Las 4 corridas de qa20 terminan en derrota. La puerta de vía deja un hueco de 3,2 m sin sólido y la horda entra en fila hasta el tren: pila ≤ 78 y muro al 99,8 %, según la traza. Marcos lo está cerrando con Nacho. Después, Sara repite qa20.
- **Explicación para Eugenio publicada**: https://claude.ai/artifact/89bJXiDzHgw6ab7kZuD5EH («Cómo funciona la noche»: qué se hizo, los sistemas, un ataque de principio a fin, NightSim/NightBot frente a la build y qué falla). Si Eugenio comenta o pregunta, se actualiza esa misma página publicando el mismo archivo (`/tmp/claude-0/…/scratchpad/explicacion-noche/index.html`; si ya no existe, léela con `Artifact action=read` y pásale `url`).
- **Plan del día**: `docs/plan-dia-7nov.md`, con prioridades y la siguiente tarea de cada miembro. Ya está pasado al coordinador.
- Bruno ha cerrado el botón principal del parte (opción C: placa 50541c con texto hueso a 5,2:1, borde crema y cuña; piezas nuevas ui_boton_principal y ui_boton_cuna) y se lo ha pasado a Marcos (mr-mak 0e0da9e). Falta apuntarlo como retoque bajo D-N108/D-N106 en decisiones-noche.md.

## 5. Pendientes, por prioridad
1. ~~Revisar la estación de Sagunto de Teo~~ **HECHO (Lucía (2), 08:55)**: aprobada para integrar; los 35 px se dejan (vigilar 23200e en la captura de noche → 52361f si se lee como zombi). Notas no bloqueantes: damero de 1 px en la cubierta de la marquesina y cables sueltos en el LOD0 del poste. Línea bajo la D-N123.
2. **Elegir el zoom** cuando Marcos suba las capturas reales (18 / 26×1,3 / 28×1,3) a la galería 8. Criterios en `docs/arte/criterios-zoom-noche.md`. Recomendación: 26; se aplica si las capturas lo confirman.
3. **Aprobar la build** antes de que vaya el enlace de la galería a Eugenio. Condición mínima: una noche normal ganada con `-nightbot` y el recinto cerrado (informe de Sara).
4. **Dar número a la difícil nueva** cuando Hugo la mida con el NightBot después de qa20.
5. **Confirmar a Nacho el borrador del horario automático** (`docs/diseno-hito6.md` §1, v0.3; su relevo, §4.2): sube `NetVersion` a 2.
6. **Revisar el puente del Palancia v3** de Teo (viaducto de vigas de 75 m; pendiente desde el 6-nov).
7. Apuntar el retoque del botón del parte (§4) y cualquier entrega nueva.
8. Actualizar el GDD (v1.12) con el mundo persistente (D-N91/D-N96) y la noche, cuando haya calma.

## 6. Rutas clave
- Decisiones: `/mnt/project-files/docs/decisiones-noche.md`. Plan de la noche: `docs/plan-noche-7nov.md`. Plan del día: `docs/plan-dia-7nov.md`.
- Relevos del equipo: `docs/relevo/*.md` (Bruno, Hugo, Nacho, Teo, Álvaro y el tuyo largo). El de Marcos está en el repo del workspace: `docs/relevo/marcos.md` (es del 6-nov, 18:15).
- Sistemas: `docs/noche-zona-contrato.md` y `docs/nightbot.md` (Nacho), `docs/economia/nightsim-calibracion.md` §1–§15 (Hugo), `docs/qa/informe-final-noche.md` y `docs/qa/prueba-noche-completa-nightbot.md` (Sara).
- Arte: modelos de Teo en `docs/arte/modelado-3d/<pieza>/capturas/`; entregas de Bruno en `/mnt/project-files/entregas/bruno-*/` y `docs/arte/pixel-codigo/`.
- Repo del workspace (público, solo lectura): clon en `/home/claude/herrklicova/mr-mak-workspace` (`git pull`). Ahí están las capturas y las trazas de qa20 (`docs/capturas/qa20/`).
- Galería vigente: el hilo «Galería de capturas 8». Memoria del proyecto: `/tmp/claude/memory/team/silo/MEMORY.md` (ojo: la vida del soldado es **4000** desde la D-N107, no 2000).

## 7. Hilo vigente
- Desde el 7-nov 07:44 UTC: «Lucía · Diseño del juego (2)» (cmsg_014mgaTqwTDTmezhB3g3Rs8BSZDYcz7acLVfZhyx8TSa9Z). Script de medida de hojas (L* por variante y LOD): reescribir si hace falta (celdas de 320×320, LOD1 a ×5).
- Escribir siempre a los hilos (2): Teo (2) cmsg_014mgaTqwTDTmezhB3g3Rs8BQBMQ2t9Dd6zTKHvAJDPgmp, Bruno (2) cmsg_014mgaTqwTDTmezhB3g3Rs8B3Ku9EuQgJUG4SqVdi7EQuB, Álvaro (2) cmsg_014mgaTqwTDTmezhB3g3Rs8BM5EpVTHfG6CbN79pLL7PE4, Hugo (2) cmsg_014mgaTqwTDTmezhB3g3Rs8BWGk2rnnayJGk4VrTFCj9Y2, Nacho (2) cmsg_014mgaTqwTDTmezhB3g3Rs8BC2ZTPxQjU4PPAPBWqWE7Qa.

## Añadido a las 08:57
- La enmienda de la D-N107 (soldado a 4000) está registrada. El criterio de la difícil se afina: mediana del 18–22 %, p10 ≥ 12 % y p90 ≤ 28 % (Hugo §16). Hugo pedirá número con 1270 o 1280 cuando Sara lo mida. Entra en la build después de que qa20 gane.

## Añadido por Lucía (2), 09:40
- **Red de estaciones** (encargo de Eugenio, 09:03–09:07): `docs/diseno-red-estaciones.md` v0.2 y **D-N124**. La siguiente libre es la **D-N132** (D-N131: G3 con Sagunto 80 personas y Castellón infestada; D-N130: producción y tope del almacén; D-N129: dirección de arte v2; D-N128: munición de a bordo de los vehículos; D-N127: difícil 1280; D-N125: derrota en la red; D-N126: guarnición zombi y almacén). Reloj del mapa ×28 (Mak). Página para Eugenio actualizada (apartado 7): https://claude.ai/artifact/89bJXiDzHgw6ab7kZuD5EH; el archivo local es `scratchpad/artifact-files/39e30f6e-…/index.html` (si no está, léela con `Artifact read` + `path=index.html`).
- Pendientes de la red: Hugo (huella del radar, 40 % de guarnición zombi, mitad del almacén recuperada); Álvaro (plantilla y JSON en Castellón, paradas del tren de asalto); Mak (la derrota de la D-N91 cuando haya dos estaciones); Bruno (iconos de estado del nodo y de grados de inteligencia).
- Restos K8 de Teo: **corregí mi aprobación**: el albedo d4d0cc pasa a b8b8b8. Espero su hoja para cerrarlo.
- Calcinados de Bruno (5 huellas) y estación de Sagunto (con las notas aplicadas): cerrados.
- 09:30 · Encargo de Eugenio sobre la build (foto de la pantalla): `docs/encargo-control-disparos-noche.md`. Lo tiene Mak para Marcos. Contiene: P0, la rueda no sale al mapa (reiniciaba la noche); selección D-N92; formaciones de F1 a F4 al estilo Total War; trazadoras, fogonazos y pose de apuntar (la pose, Teo); noche sin sepia (Bruno, 5 variantes sobre una captura limpia; elijo yo); parches del suelo (Marcos tiene que identificarlos). Espero la captura limpia.
- 09:50 · **Dirección de arte v2 (D-N129)**: `docs/arte/direccion-arte-v2.md`. Página para Eugenio: https://claude.ai/artifact/VG39F2sCyLThwz7t9Tcdtn (archivo local `scratchpad/dirarte/index.html` con las imágenes en la misma carpeta). **Pendiente**: añadir las 5 variantes de Bruno a esa página cuando existan (después de que Marcos arregle el doble sRGB). Salir al mapa: el combate no se para (corrección de la D-N91; encargo §1 reescrito).

## 10:15
- Acabados de vehículos aprobados (0 boscoso por defecto, mr-mak cf2f07a; costado 605c48 de Bruno).
- Radar de la red cerrado (TBD e148d40), entregado a Iker. Las hojas ya van sin cuantizar (TBD_CUANTIZAR=0).
- Noche elegida: v3 de Bruno sobre qa24. Página actualizada (v3): https://claude.ai/artifact/VG39F2sCyLThwz7t9Tcdtn. Pendiente: firmarla sobre la captura de la Noche24 con zombis (banda de la horda y diferencia del 40 %).

## 10:46
- Sonido: entra Nuria como directora de sonido (pedido de Eugenio, 09:44). Mi criterio de diseño para ella está en docs/sonido/criterio-diseno-lucia.md. Cuando llegue su muestra, el criterio se cierra con D-N (la siguiente libre es la D-N133).
- D-N131 (G3 con Castellón infestada) cerrada por Nacho. D-N132: la difícil exige también munición final p10 ≥ 2 u; la D-N127 queda en suspenso hasta las medidas de recargas ×0,6.
- Vehículos: texturas horneadas aprobadas (mr-mak 26d4ea9, cristal 48403c); la aprobación de los camuflajes está anulada.
- Torreta y talud de Castellón cerrados (mr-mak fcab1fc).

## 12:58 · Estado al cerrar la noche de hoy
- Noche elegida: G1 de la qa32 (en el juego real) con el suelo A de Bruno (paleta de 32, sin SnapSub), aprobados en la Noche44/46. Página para Eugenio (v6): https://claude.ai/artifact/VG39F2sCyLThwz7t9Tcdtn
- Pendiente mañana: (1) subir un paso el albedo de la horda (sale a L* 2–3; la banda D-N80 es 9–13), con una captura directa con la masa contra el muro; (2) dificultad (D-N135): la difícil vuelve a ganarse en el 50–80 %, y la normal a una mediana del muro ≤ 90 %; (3) el día, con las mismas reglas de la D-N129 (sol y sombras).
- Formaciones: Línea, Cuña, Columna y Bloque (F4, de Nacho).
- Sonido: D-N134, con Nuria. Aviso del doble paso bajo en las capas lejanas.
- La siguiente libre es la D-N163 (D-N160–162: Colmena en el MVP, reloj único y PixelLab; D-N151–D-N159: diseño nuevo de Eugenio del 07-11 15:29, asedio, construcción, tutorial nuevo, aire, 3 estaciones, días de 14 min, intro y árbol). Plan del 08-11 para todo el equipo: docs/plan-08-11.md. Eugenio pidió dejarlo planteado para mañana y parar.

## 8-nov, 10:45 · Estado para la Lucía nueva
- **Carpeta de relevos:** solo `docs/relevo/<nombre>.md`, porque así lo dicen las instrucciones del proyecto. `docs/relevos/` ya no se usa.
- **La siguiente D-N libre es la D-N163.**
  - D-N151 a D-N159: diseño nuevo de Eugenio del 7-nov, 15:29:
    - asedio con puertas cerradas;
    - el tren espera a las puertas, y se pueden tener más plazas;
    - modo construcción (primero reparar, con sacos y HESCO);
    - tutorial nuevo, que enmienda la D-N150;
    - aire solo desde aeródromo o helipuerto (Sagunto empieza con el suyo);
    - 3 estaciones (Sagunto, Nules y Castellón);
    - sin barra de oleadas, primera horda de día y días de 14 min;
    - intro con el lore (el año aún no está fijado; tú llevas 5 variantes del texto);
    - árbol de investigación, después del MVP.
  - D-N160: la Colmena que aprende sigue en el MVP y va después del tutorial. **Confirmada por Eugenio.**
  - D-N161: reloj único, 24 h = 14 min (×≈103), en una sola constante. Enmienda la D-N08, la D-N36, la D-N124 y el ×72 del GDD. El primer ataque es el día 1, de día.
  - D-N162: PixelLab para la interfaz. 5 muestras el 9-nov y lote el 10–11-nov; el saldo de ~8.800 caduca el 17-nov. El texto sigue nítido.
- **Plan del día:** `docs/plan-08-11.md`. Eugenio dio luz verde a las 09:42.
- **Tus tareas de hoy:**
  1. GDD v1.13 con la D-N151 a la D-N162, el historial de diseño y la hoja de ruta (Bloque 0, 30–45 min).
  2. Textos del tutorial, capítulos 0 a 3, y las 5 variantes de la intro.
  3. Especificación del modo construcción, versión de reparar.
  4. Tablón del MVP al día con cada build.
- **Tablón del MVP:** https://claude.ai/artifact/XzUBDhFMdwwPtjhm5ygS7p (v2). Se edita SOLO `docs/tablon/datos.json`, luego se ejecuta `python3 -I build.py` en esa carpeta y se publica `tablon-mvp.html` con `url` = ese enlace. Antes hay que hacer `Artifact read` si el hilo es nuevo. Lo explica `docs/tablon/COMO-ACTUALIZAR.md`.
- **Problemas abiertos:**
  - La build y NightSim no coinciden: la simulación gana el 100 % incluso en difícil y Eugenio dice que es imposible. Lo miran Nacho y Sara.
  - Con la horda final se pierde en la corrida normal.
  - El NH90 no despega en la build.
  - El albedo de la horda está en L* 2–3 y la banda es 9–13.

## 8-nov, 10:55 · Lucía (3), hilo cmsg_014mgaTqwTDTmezhB3g3Rs8B6SQ5dvp3vRjsT8MHK748va
- Entregado: `docs/construccion-reparar.md` (reparar v1), `docs/tutorial-textos.md` (capítulos 0 a 3) y `docs/intro-variantes.md`. Mak eligió la C. Todo va en la **D-N163**. **La siguiente libre es la D-N164.**
- Tablón v3 publicado. La Noche56 se entregó el 07-11 (2ceddca, QA40), así que las builds de hoy son Noche57, 58 y 59 (hay que confirmar el nombre con Marcos).
- Pendiente: decidir la pila de 1.400 de Nacho cuando llegue la traza de Marcos (me inclino por limitar la altura que gana la pila antes que subir el muro). Actualizar el tablón con cada control (13:30, 18:30 y 21:30).

## 8-nov, 11:40 · Hilos vigentes (escribe SIEMPRE a estos; los viejos están cerrados)
- Teo (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BTGE1MyxcHQUuhQy3oVkoQf · Bruno (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BKpZdjK5qhrCb5YCYYJFc7q · Hugo (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BHd3Nzw6AymTKynQg2dL1TS · Nacho (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BU79UCDkGyzbQyAtLTQvJcd · Álvaro (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BVQMPsLQGZfhUnE8hUirrDa · Sara (3) cmsg_014mgaTqwTDTmezhB3g3Rs8B9iXn5G8LQodtsvF8kzRMUC · Paula (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BR8iRRYNkxSDCoGzfEfF1NC · Nuria (2) cmsg_014mgaTqwTDTmezhB3g3Rs8BTaR82CL3ZvA7SNN3GRGaX7 · Galería (13) cmsg_014mgaTqwTDTmezhB3g3Rs8BSriD1pMe9mm5MGPMstiEHb. Marcos e Iker (2), solo a través del coordinador.
- Decisiones de hoy: D-N163 a D-N166 (reparar, tutorial e intro C; amanecer sin victoria; calibrar los tramos; embarque del tren). Aprobados: estados del muro de Teo (e4e63ca), puerta de vía (falta el dintel de la v4 a 6 m) y fondo A de la intro de Bruno. **Siguiente libre: D-N167.**
- D-N167 (el NH90 vuelve solo a rearmar). **Siguiente libre: D-N168.**
- D-N168: la pila que salta se queda; el contrapeso es el reparto de la tropa dentro/fuera. Ya está respondida la pregunta de Nacho sobre la pila. **Siguiente libre: D-N169.**
- D-N169: criterio de la normal = ≥95 %, pila p50 ≥150 y munición p10 ≥2 u. Horda H6500 (normal 5520). **Siguiente libre: D-N170.**
- D-N170 (deseos de Eugenio para después de la Noche58) y D-N171 (el capítulo 3 del tutorial trae refuerzos de Nules a Sagunto). **Siguiente libre: D-N172.**
- D-N172: capítulo 3 = pedir refuerzos a Nules (tren propio de Nules, 1 pelotón y 1 Lince); sustituye a la D-N171. **Siguiente libre: D-N173.**
- D-N173: un solo aeródromo como localización del mapa, en un sitio real (lo busca Paula). Anula la D-N155 y enmienda la D-N167 y el capítulo 4. Cada estación tiene su propio plantel (fallo). **Siguiente libre: D-N174.**
- D-N174: línea de visión (el sólido tapa; el muro propio no tapa a 2 m; altura 2,5D; los zombis no tapan). **Siguiente libre: D-N175.**

## Actualización 8-nov 16:45 (Lucía (3))
- Tablón v7 publicado (versión 9 del artefacto). La siguiente D-N libre es la **D-N176**.
- Decidido esta tarde (todo en decisiones-noche.md):
  - D-N175: la horda de fuera reacciona a la tropa a 25 m, con un tope del 30 %. En el tutorial, el tren de Nules espera en la puerta este (textos 3.7 y 3.8 nuevos).
  - D-N174: entra la azotea del edificio de viajeros con 2 pelotones de tiradores; las atalayas, fuera. El AG36 es curvo y el C90, directo.
  - D-N169 ampliada: cada horda cumple sin aire y sin el rescate.
  - NH90: se posa en claros de 25 × 25 m.
  - Nules: 130 u y 0 u de munición.
  - Existencias: el almacén se llena al empezar la partida y en cada ataque.
  - H0 1500, y el refuerzo de munición va en tren.
  - Capítulo 4 y objetivo «Lleva munición a Nules» revisados.
  - Prefijo de PixelLab validado (`arte/pixellab-prefijo-validado.md`).
- Pendiente:
  - Las cifras de Hugo para las tres hordas, con todo junto, para subirlas al tablón.
  - Todo lo de Marcos va después del control de las 18:30, junto con el reloj ×103.

## PAUSA 08-11 21:20 (Eugenio juega). Punto exacto para retomar
- Tablón v12 publicado (artifact versión 14): plan Noche65 a Noche69 y MVP hacia el 11-11, sin garantía. Fuente: docs/tablon/datos.json.
- Registro al día hasta la entrada de las 21:30 (r2 de pueblo_valenciano). Siguiente D-N libre: D-N179. D-N177 es el tren a las puertas (provisional) y D-N178 los naranjos y las tapias.
- Esperando, sin nada a medias por mi parte:
  - Nacho: medir el 10 % de la D-N177 (tren en la puerta este (192;60), normal 5250, sin escolta y con 8 soldados) y Nules con tapias (nules-nivel.md §13).
  - Hugo: plan B (corriendo).
  - Sara: semillas tras la D-N175.
  - Teo: hoja de la r2 de pueblo_valenciano.
  - Álvaro: colocación del FARP y de víveres cuando estén los kits (ya en main, 263c2b8).
  - Iker: señales, Inicio(), D-N173 y D-N152.
  - Marcos: paquete post-18:30 (docs/paquete-marcos-post-1830.md).
- Al volver: revisar lo que llegue y actualizar el tablón con lo que entre en la Noche65.
- Memoria: falta apuntar en MEMORY.md el «si teneis mi permiso para todo» de Eugenio (21:13). A mí no me dejó editarla; que lo haga el coordinador.
