# GDD · «VÍA MUERTA» (nombre provisional, confirmado por Eugenio el 5-nov) — v1.15

> **Estado**: v1.15 (9-nov, noche, Lucía: **el núcleo de Eugenio**, con sus tres pilares PERSISTENCIA, TIEMPO REAL y SIMULACIÓN y el bucle de órdenes de la zona al mapa, §2 y §3a; fuera las resoluciones abstractas o instantáneas, §6; un solo reloj también en la zona, §3c; interfaz v3, §13; D-N186 y D-N185). v1.14 (9-nov, Lucía: hordas de decenas de miles como objetivo firme después del MVP y la horda que llega andando, §15b, D-N182). v1.13 (8-nov, Lucía: diseño de Eugenio del 7-nov y revisión del GDD, D-N151 a D-N162. Cambian el reloj único §3c, la interfaz con PixelLab §13 y el MVP §15, con asedio, construcción, tutorial nuevo, aire desde helipuerto y Colmena confirmada; detalle en §15b). v1.12 (noche del 5-nov, decisiones del equipo con libertad creativa dada por Eugenio: 4 cargas más población §9, escalas de tiempo §3c, licencias del relieve §7, interfaz §13, voz de la Colmena §12; registro en `decisiones-noche.md`). v1.11 (5-nov: mapa de operaciones en 3D con el relieve real, §7). v1.10 (5-nov: sin sensación de rejilla; movimiento continuo, construcción libre con muros trazados como líneas y rejilla interna invisible, §9c). v1.9 (5-nov: cámara libre compatible con el pixelado; muerte de personajes con nombre sin derrota; nombre provisional; propuesta de demo y acceso anticipado §18). v1.8 (5-nov: Eugenio mantiene Hunyuan para el 3D, conociendo el riesgo de licencia; §11 y §16). v1.7 (Hunyuan sustituido por TRELLIS.2; revertido en la v1.8). v1.6 (5-nov: estaciones como bases y fábricas de trenes §9b; ejército embarcado; aire y mar condicionados a aeródromos y puertos; ideas de Eugenio). v1.5 (5-nov: campaña larga y persistente, §3b; el MVP es el arranque de una campaña). v1.4 (5-nov: render en capas pixel art y alta resolución; interfaz nítida; ver `arte/direccion-visual.md`). v1.3 (5-nov: arte 100 % 3D pixelado, física de la horda §5.7, Pixelab solo para 2D auxiliar). v1.2 (5-nov: Pixelab reorientado a texturas 3D y paleta, §11). v1.1 (5-nov: preparación para cooperativo/multijugador, §17). v1.0 cerrado con las respuestas de Eugenio del 5-nov-2026 (P1–P17) y la decisión de usar Hunyuan para el 3D generado.
> Es la **fuente viva** que se traducirá a mr.mak. Cualquier cambio posterior se anota en `historial-diseno.md`.
> Lo que falta por decidir no es de diseño sino de **prototipo** (marcado como **PROTOTIPO**).
> Antecedentes: `investigacion.md`, `conceptos.md`, `gdd-borrador.md` (v0.2), `preguntas.md`.

---

## 0. Ficha
| | |
|---|---|
| Género | RTS/táctico en tiempo real con capa estratégica continua y progresión por etapas tipo incremental |
| Jugadores | Un jugador en el MVP. **Arquitectura preparada para cooperativo (2–4 jugadores) más adelante** (§17) |
| Plataforma | Windows (Mac, quizá más adelante) |
| Idiomas | Español e inglés (texto) desde el principio |
| Motor | Unity 6.3 LTS · URP en **Forward+** · Entities 1.5 (ECS) · Burst/Jobs |
| Estilo | 3D low-poly con render de pixel art |
| Escenario | Península Ibérica → pasos fronterizos → Francia (expansión futura) |
| Fuerzas | **Ficticias**, inspiradas en instituciones reales |
| Tono | Militar sobrio, decisiones morales, sin humor |

## 1. Premisa
Semanas después del brote, las carreteras están colapsadas y el combustible escasea. Lo único que todavía mueve cargas grandes es el tren. Diriges el **Mando Ferroviario de Emergencia** (nombre provisional), una fuerza ficticia que opera trenes blindados, convierte estaciones en fuertes y **reconstruye la red vía a vía** para llevar munición, combustible, materiales y víveres, y a la gente, donde hacen falta.

Enfrente está **la Colmena**: una inteligencia colectiva que vive en la horda, **aprende tus costumbres y se adapta**.

## 2. Pilares
> **Los tres pilares de Eugenio (9-nov, «PER SIS TEN CIA»). Mandan sobre todo lo demás del documento.** La referencia es Ebbtide: un solo mundo continuo. Lo que se sabe de su bucle, con fuentes, está en `referencias-reales/ebbtide/ebbtide_bucle_nucleo.md` (Paula). Los controles exactos están SIN VERIFICAR.
> 1. **PERSISTENCIA.** Cada zona (estación, aeródromo, tren, obra) es un lugar que existe. Lo que dejas en ella (tropa, vehículos, carga, daños, muros, cadáveres) se queda tal cual cuando te vas y lo encuentras igual al volver. Al guardar se guarda **todo el mundo**, no solo la red.
> 2. **TIEMPO REAL.** Hay un solo reloj para todo, el de la §3c. Mientras miras el mapa o una zona, el resto del mundo sigue a la vez: los trenes viajan, los helicópteros vuelan y las hordas avanzan y atacan estaciones que no estás mirando. No hay saltos de hora, turnos ni escenas de corte. Solo la pausa (§3) lo para todo a la vez.
> 3. **SIMULACIÓN.** Nada se resuelve de golpe ni con una tirada. Lo que no ves se simula con **las mismas reglas** que lo que ves, de forma continua y determinista (§6 y §17). Solo cambia cuánto se dibuja.
>
> Los pilares de debajo siguen valiendo y se leen a la luz de estos tres.

1. **La red es tu vida.** Logística visible: varias líneas y varios trenes a la vez. Lo que no llega por vía, no existe.
2. **Un único mapa continuo.** Del mando de toda la red a un tren concreto en una vía, sin cargas.
3. **Tu atención es el recurso más escaso.** Estás con un tren y tienes que irte a otra línea que están atacando *ahora*.
4. **La Colmena aprende.** Lo que repites, lo castiga. Automatizar te libera, pero te hace predecible.
5. **Crecer por etapas.** De 1 tren a una red continental, como un incremental: lo manual se vuelve automático y la escala sube.
6. **Construir el camino.** Reparar, reabrir y trazar vías es tan importante como combatir.

## 3. Bucles de juego
- **Minuto a minuto**: diriges un tren o una batalla en una zona (posiciones, fuego, construcción de urgencia, retirada) mientras entran alertas de otras líneas. Decides cuándo soltar y saltar.
- **Día de juego (≈20 min reales a x1)**: horarios y cargas, guarniciones, obras de vía, reacción a avisos de la Colmena.
- **Etapa**: abrir líneas, recuperar nodos clave, desbloquear automatismos, subir de escala.
- **Campaña**: **reconstruir la red sobre la marcha y crear nuevas líneas de suministro** hasta conectar la Península con Francia.

**Tiempo**: siempre corre (x1, x2, x4). **Pausa táctica opcional** sin castigo, más un modo "sin pausa" para quien quiera presión.

## 3a. Núcleo de órdenes: de la zona al mapa (v1.15, Eugenio 9-nov, D-N186)
El jugador da las órdenes **donde están las cosas** y elige el destino **en el mapa**, sin paneles intermedios:
1. **Seleccionar en la zona.** Entras en la estación o en el aeródromo y seleccionas lo que quieres mover: un tren, sus vagones y la tropa que sube; o los helicópteros en el aeródromo. **La carga se elige allí, en la zona**, sobre el andén.
2. **Salir al mapa con la rueda.** La selección se mantiene, y se ve marcada en el mapa.
3. **Clic derecho en el destino.**
   - **Helicópteros y aire**: a cualquier punto, también en mitad del campo. Si haces clic cerca de una estación (un imán de unos 40 px en pantalla), el juego entiende que vas **a esa estación exacta**.
   - **Trenes**: solo a estaciones, y siempre con el imán. Si el tren puede ir (vía abierta, plaza libre o espera a las puertas, combustible suficiente), sale. Si no, el cursor dice por qué no en una línea («Vía cortada en el km 112», «Sin combustible»). No se abre ningún menú.
4. **El viaje se ve y se sigue.** Doble clic sobre el tren o el helicóptero para seguirlo, y la rueda para volver a entrar en la zona a la que llega. Al llegar, todo **se queda allí** (pilar 1) hasta que le des otra orden.
- **Lo que se quita**: el panel «Preparar tren» como paso obligatorio y cualquier orden de destino que no se dé sobre el mapa. El panel de tren de la §13 queda solo para **consultar** (carga, población y horario).
- **Zonas que se pueden visitar**: todas las estaciones propias **y los aeródromos** (Bétera). Si no se puede entrar en un sitio donde tienes unidades, es un fallo.

## 3b. Duración y estructura de la partida (v1.5)
> Aclaración de Eugenio (5-nov): **una partida no se termina en 2 horas**. Es una campaña larga y persistente: pasan los días, te haces más fuerte y tienes más cosas, pero la Colmena también se endurece. Dura muchas horas, según cómo juegues.

- **Una partida = una campaña continua** sobre el mismo mundo, sin misiones separadas. Se guarda y se retoma durante semanas.
- **Duración orientativa [estimación propia, a ajustar con pruebas]**: con un día de juego de unos 20 min a x1, una campaña hasta la frontera francesa llevaría unas **40–100 h**. Depende de la velocidad que uses, de cuánto automatices y de lo arriesgado que juegues.
- **Calendario del mundo**: días, estaciones y años. La estación cambia el comportamiento de la Colmena (migraciones en primavera y otoño, letargo con el frío) y el ritmo de la campaña.
- **Carrera de escalada**: tú creces (red, trenes, automatismos, especialistas) y la Colmena **también**:
  - **Por tiempo**: cada día que pasa, la Colmena crece y acumula memoria.
  - **Por tu huella**: cuanto más grande y ruidosa es tu red, más presión atraes.
  - **Por adaptación**: nuevas cepas responden a cómo juegas.
  - La curva de la Colmena se ajusta a **ambas cosas** (tiempo y huella) para que no puedas "esperar y acumular" sin coste, ni correr sin consolidar.
- **Evitar bolas de nieve en ambos sentidos**:
  - si vas muy bien, la Colmena reacciona más (presión por huella);
  - si vas mal, hay margen para recuperarse: replegarse a un nudo seguro, el letargo invernal da respiro y los rescates aportan refuerzos.
  - **Perder una línea duele, pero no acaba la partida.**
- **Hitos de campaña**: las etapas de §4 son capítulos naturales, cada una con un objetivo grande (por ejemplo, reabrir Canfranc). Dan sensación de avance en una partida de muchas horas.
- **Final**:
  - **Victoria de campaña**: conectar la red peninsular con Francia por al menos un paso fronterizo y mantenerlo durante una estación.
  - **Después de la victoria**: se puede **seguir jugando** en modo continuo (expansión por Francia, Colmena en escalada sin techo).
  - **Derrota**: perder todos los nudos principales o que la red colapse (sin trenes operativos durante X días; **PROTOTIPO**).

## 3c. Escalas de tiempo y velocidad (v1.12, D-N11)
- **Un solo reloj también en la zona (v1.15, D-N186)**: la noche de una zona va con el reloj de la red, no con uno propio. Al acabar un ataque, el mapa marca la hora que es de verdad. **Queda anulado el salto de la red al amanecer** (decisión del 9-nov 21:26), porque rompe el pilar 2.
- **El reloj es abstracto y hay uno solo (v1.13, D-N161)**: **24 h de juego son 14 min reales a x1**, es decir, el reloj va unas **103 veces más rápido** que el tiempo real. Sustituye el ×72 de la v1.12 y el ×28 de la D-N124. El factor vive en una sola constante de datos, que leen la build y las simulaciones; ningún documento lo vuelve a escribir a mano. *Aviso*: los ejemplos de esta tabla y de la zona se calcularon con ×72, así que los tiempos reales son ahora un 30 % más cortos y Hugo los vuelve a medir.
- **Mapa (S0), en tiempo de juego**:

  | Qué | Velocidad orientativa | Ejemplo |
  |---|---|---|
  | Horda común | 2 km/h | — |
  | Zombis rápidos | 6 km/h | — |
  | Trenes en vía abierta | ~60 km/h | Sagunto–Teruel (~130 km) en ~2,2 h de juego: menos de 2 min reales a x1 |

- **Zonas en detalle (S2), a velocidad visual real**: zombis a 1–1,5 m/s; los trenes van limitados, como en una zona de maniobras. Una batalla de 5 min reales son unas 6 h de juego. El reloj no se frena dentro de la zona.
- **Avisos**:
  - La horda se detecta a ~3 km con visión normal; exploradores y drones amplían ese alcance. Con la horda común eso da **~75 s reales de margen a x1**.
  - El objetivo de diseño es ese margen de reacción, de 60 a 120 s reales a x1. Lo vigila una prueba automática.
  - Las alertas se muestran **en tiempo de juego con hora de llegada**: «Horda en 40 min (14:40)».
  - Las críticas **bajan la velocidad a x1** de forma automática (se puede desactivar).
- **Materializar una zona**:
  - **Umbrales**: la zona aparece al acercar la cámara a menos de ~2 km y desaparece al alejarla a más de ~2,5 km (histéresis).
  - **Escala**: la densidad S0 de la celda va de 0 a 1000 por mil y equivale a de 0 a 10.000 zombis.
  - **Al salir**: los muertos se restan de la mancha y los vivos vuelven a su celda.
  - **Tamaño de la zona**: 256 × 128 m, para que quepa un tren con margen.
  - Detalle en `decisiones-noche.md`, D-N05.
- **Ritmo de arranque (D-N08)**:
  - **Día 1**: sin asedios, solo sondeos de 100 a 300 zombis.
  - **Día 2**: primer asedio, anunciado.
  - **Asedios simultáneos como máximo**: 1 en la etapa 1, 2 en la etapa 2 y 3 o más en la etapa 3.

## 4. Progresión por etapas (incremental)
| Etapa | Red | Trenes | Automatismos que se desbloquean | Lo que haces tú |
|---|---|---|---|---|
| 1. Supervivencia | 1 línea, 6–8 nodos | 1–2 | — | Llevas cada tren a mano y luchas en cada parada |
| 2. Nudo | 2–4 líneas que se cruzan | 5–10 | Horario automático, orden permanente de estación | Saltas entre líneas atacadas |
| 3. Región | Varias regiones conectadas | 10–25 | Convoyes escoltados, guarniciones con reglas, rutas alternativas automáticas | Priorizas corredores y bajas a las crisis |
| 4. Península | 10–15 líneas, ancho ibérico | 25–50 | Horarios con variación aleatoria (contra la Colmena), logística por demanda | Mando de red |
| 5. Frontera | Portbou/Cerbère, Irún/Hendaya, Canfranc (línea cerrada que hay que reabrir) | 50+ | Transbordo y cambio de ancho | **Cambio de ancho de vía** como reto logístico propio |
| 6. Francia (expansión futura) | Red francesa | 100+ | Mando de teatro | Mismo bucle, más escala |

Lo que hace que se sienta incremental:
- **La automatización es la progresión**: lo que haces a mano en una etapa lo delegas en la siguiente, y eso te libera atención para más líneas.
- **Números que crecen**: toneladas al día, trenes en servicio, km de vía segura, población rescatada. Siempre visibles en el mapa.
- **La Colmena escala contigo**: a más red, más ruido, más que aprender. El juego no se queda "resuelto".

## 5. La Colmena (enemigo inteligente)

### 5.1 Concepto y diferencia con Ebbtide
Ebbtide tiene a *Nexus*, una mente colmena que actúa como **un general**: embosca, corta carreteras, asedia, y tiene **nodos de mando ocultos** que el jugador caza.

La Colmena de Vía Muerta es distinta en tres cosas:
1. **Aprende de ti, no solo te ataca.** Su inteligencia es **memoria y adaptación**: recuerda tus horarios, rutas, armas y defensas, y responde a ellas. Cuanto más predecible eres, más letal es.
2. **Choca con tu progresión.** Automatizar (pilar 5) te hace predecible y la Colmena aprende tus automatismos (pilar 4). Esta tensión no la tiene ningún referente que conozca.
3. **Es distribuida.** No hay un cerebro que matar: cada **nido** (ciudad infestada) guarda su propia memoria, y el conocimiento **se contagia** entre nidos con las migraciones. Cortar corredores de migración frena su aprendizaje; limpiar un nido hace que esa región "olvide".

### 5.2 Qué aprende (memoria)
| Memoria | Qué registra | Cómo lo usa |
|---|---|---|
| **De tráfico** | Por tramo y hora: cuándo pasan tus trenes | Emboscadas en el km y la hora exactos; vía bloqueada con escombros antes de que llegues |
| **De armas** | Cómo mueren sus zombis (balas, fuego, explosivos, aplastados por el tren) | Cambia el peso de las **cepas** que nacen: acorazados contra balas, resistentes al fuego, dispersos contra explosivos |
| **De defensas** | Qué muros y puntos fuertes resisten | Trepadores y excavadores; ataca por el punto más débil |
| **De atención** | Dónde estás mirando tú (qué zona está en detalle) | **Ataca dos líneas a la vez** cuando sabe que estás ocupado en una tercera |
| **De luz y ruido** | Tus focos, generadores y batallas | Se acerca de noche o evita la luz, según la cepa |

Toda memoria **decae con el tiempo**: si cambias de costumbre, la Colmena acaba olvidando la anterior.

### 5.3 Estados de comportamiento
**Deriva** (dispersa, pasiva) → **Migración** (desplazamiento masivo, estacional o por ruido) → **Caza** (sigue a un tren o convoy) → **Asedio** (rodea un nodo y lo desgasta) → **Enjambre** (respuesta violenta a una amenaza) → **Letargo** (frío, invierno, tras grandes pérdidas). Las transiciones dependen de variables de la simulación: hambre, densidad, ruido, estación y memoria.

### 5.4 Legibilidad y justicia
- **Informe de inteligencia**: el jugador ve lo que la Colmena ha aprendido ("Ha aprendido que el Tren 3 pasa por Caminreal cada 2 h"; "Cepa acorazada en aumento en Teruel"). Lo descubren exploradores, drones y especialistas.
- **Avisos con antelación** antes de ataques grandes (además dan tiempo técnico a pre-cargar la zona).
- **Contramedidas del jugador**: variar horarios, trenes señuelo, rutas alternativas, cambiar de arma, limpiar nidos, cortar corredores de migración.
- **Dificultad = velocidad de aprendizaje** de la Colmena (parámetro ajustable).

### 5.5 Viabilidad técnica
- **Sin aprendizaje automático real**: la "inteligencia" son **tablas de memoria con decaimiento** en la capa S0 y un **director de IA por utilidad** que elige tácticas según esa memoria. Es barato, depurable y ajustable por diseño.
- En la capa S2, las cepas y tácticas son **variaciones paramétricas** del mismo agente de flow field (velocidad, resistencia, si trepa, a qué objetivo prefiere ir). No hacen falta IAs individuales complejas.
- Riesgo: que se perciba como "trampa". Se mitiga con el informe de inteligencia y los avisos.

### 5.6 Tipos de zombi
- **MVP**: común (lento, abundante), rápido, pesado (rompe muros).
- **Cepas adaptativas (completa)**: acorazado, ignífugo, trepador (se apila), excavador, chillón (atrae a otros), nocturno. Además, animales infectados.
- Los soldados muertos **se levantan** (refuerzan la horda local).

### 5.7 Física de la horda: caer, amontonarse, trepar (v1.3)
Petición de Eugenio: los zombis **caen de los tejados, se amontonan** y son una masa física creíble.
- **Amontonamiento**: cada celda de la rejilla interna (invisible, ver §9c) guarda una **altura de pila**, que se interpola entre celdas para que la pila sea una rampa continua y no escalones. Los zombis bloqueados contra un muro o una puerta suben la pila de las celdas de delante, y los que llegan después caminan *sobre* ella. Cuando la pila alcanza la altura del muro, **la horda se derrama por encima**. Es el momento más espectacular del juego y avisa visualmente del peligro (la pila crece).
- **Caídas**: los zombis en tejados, puentes y andenes se desplazan por celdas con altura. Si el flow field los lleva al borde, **caen** con gravedad simple (integración vertical en Burst), aterrizan con animación de impacto y pueden dañar o derribar a quien esté debajo. También caen de trenes en marcha y desde pasos elevados sobre la vía.
- **Trepar**: la cepa trepadora sube por fachadas y muros sin necesidad de pila.
- **Empuje**: la presión de la masa empuja puertas y vallas débiles (daño por densidad acumulada).
- **Técnica**: todo en DOTS, sobre la misma rejilla interna del flow field (§9c). **Sin física de Unity en la jugabilidad**, lo que mantiene el determinismo para el coop (§17.3) y el rendimiento con 10–20k agentes. Animaciones VAT de caída, aterrizaje, trepar y apilarse. Los cadáveres cercanos pueden tener *ragdoll* solo visual.
- **Riesgo**: que la pila se vea "flotante" o artificial. Se mitiga con la animación de apilarse (manos sobre otros zombis) y con el desfase de alturas. Va en el **hito 1** (prototipo de zona), porque define el aspecto del juego.
- Objetivo técnico: **10–20k activos** en una zona (MVP); más de 30k como meta. Estimación que hay que validar en tu equipo (**PROTOTIPO**).

## 6. Simulación global
- **Niveles de simulación** (ver `investigacion.md` §3.3):
  - **S0 (mundo)**: grafo de vías y nodos, campo de densidad de horda, memoria de la Colmena, trenes y fuerzas. *(v1.15)* ~~combate abstracto calibrado~~: **no hay combate abstracto**. Un combate que no se mira lo simula NightSim con las mismas reglas que la zona, de forma continua, y la zona lo retoma en el mismo estado cuando entras.
  - **S1**: manadas y escuadras sin animación.
  - **S2**: entidades ECS completas.
- Como mucho **1–3 zonas en detalle a la vez**. Nunca se congela nada.
- **Niebla de guerra**: solo ves densidad donde tienes visión.
- **Sin facciones humanas** en el MVP. Se valorarán para la versión completa.
- Pruebas automáticas que comprueban que una pelea da **el mismo resultado con la misma semilla** se mire o no se mire (pilar 3). Sustituye la calibración del combate abstracto.
- **Nada se resuelve de golpe (v1.15)**: ni la emboscada, ni el cerco, ni la pérdida de un tren. Todo dura el tiempo que dura, en el reloj de la §3c, y puedes llegar a mitad.

## 7. Mapa de operaciones y saltos de atención
- **Mapa en 3D con el relieve real** *(petición de Eugenio, v1.11)*: la Península como terreno 3D a partir de un modelo digital de elevación real, con sierras, valles, ríos, costa y ciudades. Lleva una ligera exageración vertical para que el relieve se lea desde arriba, y se puede girar e inclinar con la misma cámara libre (§11).
  - **Por qué importa**: el relieve real explica la red (las vías van por valles y pasos de montaña) y hace que el **zoom continuo** sea creíble, porque el terreno del mapa es el mismo que el de la zona, solo que con menos detalle.
  - **Técnica**: terreno por bloques con niveles de detalle. Malla gruesa (cientos de metros por punto) para toda la Península y más fina (decenas de metros o menos) alrededor de la zona a la que te acercas. Va a resolución completa, sin pixelar (capa del mapa, `arte/direccion-visual.md`), y se funde con la capa pixelada en el umbral del zoom.
  - **Datos (licencias verificadas el 5-nov, D-N12, `arte/licencias-elevacion.md`)**:

    | Uso | Fuente | Licencia |
    |---|---|---|
    | Mapa de toda la Península y el sur de Francia | **Copernicus DEM GLO-90/GLO-30** | Licencia pública gratuita; permite el uso comercial con aviso y descargo |
    | Detalle de las zonas en España | **IGN MDT05/MDT25** | CC BY 4.0 |
    | Ríos, poblaciones y vías | **IGN BTN** | CC BY 4.0 |

    - **Cartela de atribución** discreta en una esquina del mapa de operaciones, al estilo de los mapas antiguos («CC-BY 4.0 scne.es · Copernicus WorldDEM»). La atribución completa va en los créditos y en el aviso legal.
- Encima del terreno van la red, la densidad de horda (mancha), los trenes y su carga, las obras de vía y el estado de cada nodo (**Segura → Amenazada → Asediada → Perdida**).
- **Zoom continuo** hasta la zona: al pasar un umbral se pre-carga la SubScene y se funde con el mapa. Sin pantallas de carga.
- **Alertas priorizadas** ("Tren 7 detenido en el km 112, horda a 90 s"). Una tecla te saca de donde estás y te lleva al nuevo punto.
- **Lo que dejas sigue** con la orden que le diste (aguantar, seguir, retirarse).

## 8. Vías: reconstruir y trazar
- **Reparar**: tramos destruidos, puentes volados, desvíos y señales. Hace falta un **tren de obras** y materiales.
- **Reabrir**: líneas cerradas, como Canfranc o ramales en desuso (muchas son hoy vías verdes). Son rutas conocidas y caras, pero valiosas.
- **Trazar**: nuevas conexiones a lo largo de **corredores posibles predefinidos**, no con trazado libre. Así el problema técnico y de diseño se mantiene acotado.
- **Estaciones nuevas** *(idea de Eugenio, v1.6)*: al tender vía puedes **fundar estaciones** en los emplazamientos de cada tramo (ver §9b).
- **La obra es una batalla**: hay que proteger a los obreros mientras avanzan, y el ruido de la obra atrae a la Colmena.
- La Colmena también **corta vías** (escombros, vagones volcados), y aprende dónde te hace más daño.

## 9. Bases, recursos y fuertes
- **Recursos (v1.12, D-N01)**:
  - **4 cargas**: munición, combustible, materiales y **víveres** (comida y agua).
  - **La población** (refugiados, obreros y tropa) no es una carga: viaja en plazas de pasajeros, no ocupa toneladas y no se gasta. Come víveres, trabaja y atrae a la Colmena.
  - Sin cadenas de producción complejas.
- **Munición (D-N02, D-N08)**:
  - En el MVP hay una sola reserva, medida en «disparos de fusil equivalentes». Cada arma gasta a su ritmo; un proyectil de obús cuesta 100 equivalentes, así que la artillería pesa en la reserva.
  - Las clases ligera, pesada y especial llegan en la etapa 2, con las cepas.
- **Tensión logística (D-N04, en validación con el modelo de Hugo)**: si nada sale mal, la capacidad nominal de los trenes cubre el 90–100 % de la demanda. **El déficit lo provoca la Colmena**: cortes, emboscadas y asedios bajan lo que llega de verdad al 75–85 %. La etapa 1 es más suave.
- **Producción**: los nodos especiales (refinería, taller, almacén, granja) producen si están guarnecidos y suministrados.
- **Ciclo de zona**: limpiar → asegurar → fortificar → guarnecer → mantener.
- **Construcción libre** (posición y rotación libres; muros trazados como líneas), solo en zonas limpiadas y con materiales llegados por tren. Ver §9c.
- **El muro compra tiempo (v1.12, D-N27, medido en el hito 3)**:
  - en campo abierto, lo que limita es la **cadencia**: la horda llega al cuerpo a cuerpo y la tropa cae, aunque le sobre munición;
  - tras un muro, la horda queda retenida y el límite pasa a ser la **munición**;
  - la tropa es frágil en campo abierto a propósito.
  - **El tren es un muro móvil**: la tropa que dispara desde los vagones blindados o desde la plataforma de tiro cuenta como «tras muro» mientras el tren está parado. Bajarse del tren es una decisión de riesgo.
- **Piezas MVP**: muro (sacos/HESCO), puerta, nido de ametralladora, foco, depósito y andén fortificado. Completa: hormigón, torres, minas, alambradas, morteros, antiaéreo y generadores.
- **Mantenimiento**: las piezas se desgastan y repararlas cuesta materiales. Sin suministro, la zona se degrada y acaba perdida.

## 9c. Sin sensación de rejilla: movimiento y construcción continuos (v1.10, petición de Eugenio)
> Eugenio: «aunque se usen rejillas, que no se sienta como un juego 2D que limita el movimiento de los personajes y la construcción».

Hay tres "rejillas" distintas y **ninguna se ve ni limita al jugador**:

| Rejilla | Qué es | Qué ve el jugador |
|---|---|---|
| **Píxeles de la cámara** | El ajuste de la cámara a la rejilla de píxeles para que la imagen no "baile" (§11) | Nada: es **solo visual**. No afecta a dónde están ni cómo se mueven las cosas |
| **Rejilla interna de navegación** | Celdas finas (orientativo 0,5 m; **PROTOTIPO**) donde se guardan los datos agregados de la horda: dirección del flow field, densidad, coste de paso, altura de pila | Nada: es un mapa de datos invisible |
| **Construcción** | **No hay rejilla de construcción** | Colocación y rotación libres |

**Movimiento continuo**
- Soldados, vehículos, trenes y zombis tienen **posición, velocidad y orientación continuas**. Nadie se mueve casilla a casilla.
- El flow field solo da **una dirección deseada**, interpolada entre las celdas vecinas. El movimiento real sale de esa dirección más la separación entre agentes, la inercia y los obstáculos. Así las curvas son suaves y la masa fluye como un líquido, no en escalera.
- Las unidades del jugador usan su propio pathfinding con caminos suavizados, no el flow field de la horda.

**Construcción libre**
- **Piezas sueltas** (nidos, focos, depósitos, sacos): se colocan en cualquier punto y con cualquier ángulo, con el ratón y la rueda para girar. Ajuste opcional a otras piezas, como alinear con un muro, nunca obligatorio.
- **Muros, vallas y alambradas se trazan como líneas**: haces clic en un punto, clic en otro, y el muro sigue esa línea con cualquier ángulo. Con varios clics, una polilínea que rodea la estación. Las piezas se reparten a lo largo de la línea.
- Las restricciones son físicas, no de rejilla: pendiente máxima, no bloquear la vía y no colocar dentro de otro objeto.

**Cómo se mantiene la colisión y la pila con la rejilla invisible**
- **Colisión exacta con la geometría**: cada muro es un **segmento con grosor y altura**. Zombis y unidades chocan contra ese segmento real (prueba de cápsula contra segmento en Burst), no contra celdas. Un muro en diagonal es un muro en diagonal, sin dientes de sierra.
- **La rejilla interna se "pinta" a partir de la geometría**: al construir un muro, sus celdas se marcan como bloqueadas (con la altura del muro) **solo para calcular el flow field y la pila**. Se recalcula únicamente la región tocada.
- **Pila de la horda**: se acumula en las celdas pegadas a la cara del muro y se **interpola** entre celdas, así que la rampa de cuerpos es continua y sigue el ángulo del muro. Cuando su altura supera la del segmento, los zombis cruzan por encima en ese punto exacto.
- **Determinismo (§17.3)**: posiciones y colisiones en Burst determinista. Las celdas solo agregan datos. Nada de esto depende de la cámara.

## 9b. Estaciones: bases, checkpoints y fábricas (v1.6, idea de Eugenio)
Las estaciones son **la base del juego**: checkpoints de la red, con gente dentro, que hay que fortificar y mantener.
- **Fundar**: al ampliar o reabrir una vía, puedes fundar una estación en un **emplazamiento** del tramo. Hay 2–5 emplazamientos por tramo, elegidos por terreno llano, agua y cruce de caminos.
  - *Por qué emplazamientos y no cualquier punto*: cada estación es una zona de batalla. Con emplazamientos conocidos, la zona se puede generar con el **relieve real y un kit modular** de piezas de estación, en lugar de diseñar a mano cada sitio posible. Resuelve el choque con las "zonas diseñadas a mano" de §6.
- **Población**: cada estación tiene gente (refugiados rescatados, obreros, tropa).
  - Permite trabajar, producir y guarnecer.
  - Necesita víveres y protección; sin ellos cae la moral y la gente se va o muere.
  - **La gente atrae a la Colmena** (ruido y calor): crecer tiene un coste.
- **Fortificar**: construcción libre en la estación (§9, §9c). Andén, muros, puertas, nidos y focos. Desde ella se controla el tramo de alrededor.
- **Niveles**:
  - **Apeadero**: punto de paso, poca gente, defensas mínimas.
  - **Estación**: almacén y guarnición.
  - **Nudo**: cruce de líneas, hospital y cuartel.
  - **Taller ferroviario**: fabrica y repara material rodante.
- **Fabricar y lanzar trenes**: los **talleres** construyen locomotoras y vagones con materiales y gente especializada, y los trenes nuevos salen desde allí a la red. Es el motor del crecimiento incremental (§4).
- **Checkpoint**: control de entrada de supervivientes. Decisiones de cuarentena: aceptar, aislar o rechazar. Encaja con el tono de decisiones morales. **Cada grupo llega con su rostro en primer plano** (retratos de Pixelab), para que la decisión mire al jugador a la cara (v1.12).
  - **Oleadas (v1.12, D-N23)**: llegan **4–8 grupos con tarjeta**, cada uno con rostro, tamaño y un rasgo (obreros, desertores, familia, heridos, médico…).
  - El jugador elige **qué grupos entran**, con un indicador de días de víveres que se actualiza en directo.
  - La **cuarentena son plazas limitadas** según el nivel de la estación.
  - **Los rechazados no desaparecen**: una parte acaba sumándose a la horda cerca de la estación.
  - Aceptar sin aislar tiene un pequeño riesgo oculto de infección.
  - **Lo que se decide no es «acepto o no», sino «¿a quién dejo fuera?»**. La población es el motor de la economía (`economia/economia-balance.md`).
  - **Las familias cuentan**: cada familiar sube un 1 % la producción del nodo, hasta un 25 % («la gente trabaja mejor si tiene a quién proteger»).
- **Reputación (v1.12, D-N23)**: una sola barra, de 0 a 100 %, sin pantalla propia.
  - Baja un 2 % por cada persona rechazada (el triple si es familia o herido), con un suelo del 30 %.
  - Sube un 1 % al día y un 3 % por cada familia acogida.
  - **Efectos**: multiplica la gente que llega en las oleadas, porque la noticia se corre. Por debajo del 50 %, la moral cae y la producción baja un 10 %.
- **Producción especializada** según el emplazamiento: refinería, granja, mina o fábrica de munición. Sin cadenas complejas (§9).

## 10. Unidades y vehículos
- **Infantería**: fusileros y armas pesadas en el MVP. Completa: ingenieros, francotiradores, lanzallamas y médicos.
- **Trenes** (unidad estrella): locomotora más vagones configurables (transporte, artillería, grúa, obras, hospital, antiaéreo, plataforma de tiro y señuelo).
- **El tren lleva al ejército** *(idea de Eugenio, v1.6)*: los trenes blindados transportan **unidades de tierra** (infantería, blindados de transporte de tropas tipo BTR y vehículos) en vagones plataforma y de tropa. En cada parada se **despliegan** a la zona, combaten y vuelven a embarcar.
- **Logística a bordo**: las unidades embarcadas **consumen el combustible, la munición y los víveres que lleva el propio tren**. Cada tren tiene un **inventario**: si llevas mucha carga para otra estación, puedes gastarla en el camino, pero entonces no llega entera. Es una decisión constante: escolta potente o carga íntegra.
- **Autonomía de los vehículos desplegados**: tienen combustible limitado y vuelven al tren para repostar. Lejos de la vía son vulnerables.
- **Vehículos**: uno ligero en el MVP. Completa: blindados, excavadoras y camiones grúa.
- **Apoyo de artillería**: vagón artillero en el MVP; artillería ferroviaria pesada en la versión completa.
- **Apoyo aéreo** *(idea de Eugenio, v1.6)*: se **habilita al recuperar aeródromos**, que funcionan como un tipo de nodo. Cada aeródromo da un catálogo pedible (cazas, helicópteros de ataque o transporte, drones) con radio de acción, combustible y munición que llegan **por tren**. Sin aeródromo no hay aviación. **Fuera del MVP.**
- **Apoyo naval** *(idea de Eugenio, v1.6)*: solo en **líneas de costa**, al recuperar puertos. Fuego naval y evacuación por mar con alcance desde la costa. En el interior no hay. La Península tiene costa en tres de sus lados y un interior montañoso: el mapa decide dónde hay apoyo. **Fuera del MVP.**
- **Catálogo de armas y unidades**: amplio en la versión completa. Detalle en `catalogo-unidades.md` (v0.1): roles, etapa de desbloqueo, logística, contra qué cepa sirve cada unidad y qué entra en el MVP.
- **Personas con nombre**: **especialistas y mandos**, con retrato, rasgos y posibilidad de morir. La tropa es anónima.
  - **Si muere uno con nombre, no se pierde la partida** (Eugenio, v1.9). Se pierden sus bonificaciones y queda en el memorial de la campaña; puede sustituirlo otro especialista rescatado. En modo hierro también es definitivo, pero tampoco termina la partida.
- **Control directo** de una unidad: no en el MVP. Se valorará después.

## 11. Arte
- **Pilar**: low-poly 3D con shader de pixelado (render a baja resolución, snapping de cámara, contornos por profundidad y normales, luz toon y paleta fija).
- **Cámara libre** *(idea de Eugenio, v1.9)*: rotación libre, inclinación ajustable dentro de un rango (aprox. 35–75°, del picado de mando a una vista más baja de calle) y zoom continuo. Así encaja con el pixelado:
  - **Zoom**: la resolución interna es fija respecto a la pantalla (factor 2–4, §11), así que **el píxel siempre mide lo mismo en pantalla**. Al alejarte, los objetos ocupan menos píxeles y pierden detalle de forma natural. Sin escalones de zoom.
  - **Desplazamiento**: *snapping* de la cámara a la rejilla de píxeles más la compensación de subpíxel en pantalla (pasada D de `arte/direccion-visual.md`). Así, al moverte, el mundo no "baila".
  - **Rotación**: es lo más delicado. Al girar, los bordes de los modelos cruzan la rejilla y los píxeles "titilan". Mitigaciones:
    1. contornos y luz estables (normales suavizadas y sombras con filtro);
    2. factor de pixelado 2–3 en lugar de 4 mientras se gira;
    3. el giro se sigue haciendo con el ratón, pero se puede activar en ajustes un **"giro asistido"** que se asienta en el ángulo de 15° más cercano al soltar.
    - Cuánto titila es **PROTOTIPO** (hito 1): se medirá con capturas en movimiento.
  - **Transición al mapa de operaciones**: el zoom continuo hacia fuera acaba en el mapa (resolución completa, §7). Se funde en el umbral.
- **Modelos 3D generados por IA: Hunyuan3D** (addon Image to 3D en Blender, en local). **Decisión de Eugenio del 5-nov-2026 (v1.8), tomada conociendo el riesgo de licencia** (ver §16).
  - Solo para **piezas clave**: locomotoras, vagones, estaciones, edificios emblemáticos y vehículos. No sirve para personajes ni hordas (no salen con rig).
  - Flujo:
    1. Imagen de referencia limpia u hoja de vistas (API de imagen de ElevenLabs).
    2. Hunyuan, con *More Views*, *Enhance Detail* y *Enhance Texture* si hace falta.
    3. Blender: diezmado al presupuesto de la pieza (orientativo 1.500–4.000 polígonos), limpieza, UV y textura en la paleta.
    4. Unity, validando bajo el shader.
  - **Alternativa ya preparada si algún día hace falta**: TRELLIS.2-4B (MIT; descargado). Sus condiciones están en `historial-diseno.md`, v1.7.
- **Personajes y zombis**: bases low-poly CC0 (Quaternius, Kenney) modificadas, animaciones de Mixamo o Quaternius, y hordas con **VAT**.
- **Zombis muy pixelados pero reconocibles**: diseño por **silueta** (postura encorvada, brazos adelantados, proporciones exageradas), colores de alto contraste en la paleta y contorno de 1 píxel del shader. Altura en pantalla con el zoom por defecto: unos 12–24 px (**PROTOTIPO**). Lejos se usan LOD 3D más simples, no sprites.
- **Pixelab** se usa **solo para la UI, los iconos y el 2D auxiliar** (v1.3): interfaz, iconos, marcadores del mapa, retratos, VFX en planos que miran a la cámara, decals, ilustraciones de eventos y, si la prueba sale bien, texturas para los modelos 3D. **Nada del mundo 3D sale de Pixelab: todos los zombis, soldados, trenes y edificios son modelos 3D a cualquier distancia.** Plan del lote: `pixelab-piloto.md`.
- **Paleta**: 32 colores (`arte/paleta_propuesta_32.png`), compartida por las texturas, la UI y el shader de pixelado mediante una LUT. **Aprobada (5-nov).**
- **Entrada para la IA 3D**: hojas de vistas generadas con la API de imagen de ElevenLabs (GPT Image), no con Pixelab.
- **Render en capas (v1.4)**: mundo 3D a baja resolución (factor de pixelado entre 2 y 4, por defecto 3); efectos de luz, bloom, interfaz y mapa de operaciones a resolución completa. Detalle y especificación del shader en `arte/direccion-visual.md`.
- **Interfaz moderna y nítida** (no pixel art). El pixel art queda para iconos, retratos y logotipo.
- Valor final del factor de pixelado: **PROTOTIPO** (hito 1).

## 12. Audio
- **Todo con IA (ElevenLabs)**, también la música, por decisión de Eugenio: no hay otro recurso.
  - **Efectos y ambientes**: horda lejana o cercana como capa dinámica según la densidad, trenes, clima y ciudad muerta.
  - **Voces**: radio y mandos, con frases cortas y procesado de radio para que encajen.
  - **Música**: adaptativa por estado (calma, alerta, asedio).
  - **La Colmena suena, pero no habla (v1.12, D-N07)**. Su firma sonora tiene tres partes:
    - **el coro**: un zumbido de miles de gemidos afinados que crece en asedio y en enjambre;
    - **el motivo**: tres notas descendentes y disonantes que suenan cada vez que la Colmena aprende algo (una entrada nueva en el informe de inteligencia), y que la música de asedio cita;
    - **la interferencia**: estática con ritmo de respiración en la radio cerca de los nidos.
  - **Voces**: solo de radio (mandos, especialistas, maquinistas y jefes de estación), sin narrador, en español y en inglés.
  - Lista por hito: `arte/necesidades-2d-audio.md`.
- **Riesgos y mitigación**:
  - Es lo que más rechazo le ha costado a Ebbtide. Lo mitigamos con un estilo coherente, una curación estricta y la declaración en Steam (obligatoria).
  - **Licencia de la música (verificada por Iris, D-N09)**: los términos de Eleven Music del 9-oct-2026 permiten la música en juegos indie con el plan Pro. Hay un límite de facturación; los detalles y las fuentes están en `arte/plan-assets-audio.md` §3. No se usan modelos en beta para el juego. Falta confirmar que el plan de Eugenio es Pro.

## 13. Interfaz
- **Interfaz v3 (v1.15, D-N185, aprobada por Eugenio el 9-nov)**: https://claude.ai/artifact/RN1FJnAfriYpcEX8HGxh9T. Fondo oliva casi negro, el objetivo fijo arriba en el centro, un panel de trabajo único a la izquierda, guía de tutorial con «Haz esto» y foco, fuentes Barlow Condensed, Barlow e IBM Plex Mono. Estados solo en d4d0cc, e08c30 y 982420. **La horda va en rojo en el mapa** (982420 tramado, con flecha y hora de llegada). Leyenda con L, tres niveles de zoom, estaciones propias agrupadas al alejarse. Sustituye a la D-N162 en lo que choque.
- **Cambiado en la v1.13 (D-N162, pedido de Eugenio)**: los marcos, paneles, tarjetas, botones e iconos pasan a ser **pixel art de PixelLab**, con la estructura de la D-N147 (`interfaz-v2.md`). **El texto sigue nítido** (UI Toolkit, fuente sin serifa SDF), para que se lea bien. Antes del lote van 5 muestras, y cada una pasa por la hoja de cohesión de la D-N53.
- *(v1.4–v1.12, sustituido)*: ~~Moderna, plana, oscura y nítida; el pixel art solo en iconos, retratos, marcadores y logotipo.~~
- **Colores**: solo de la paleta de 32, con tokens por uso (`arte/necesidades-2d-audio.md` §1).
- **Iconos**:
  - maestros de 16 y 32 px, mostrados siempre a escala entera (×1, ×2 o ×3);
  - filtro de punto y posiciones de píxel entero.
- **Marcos con estilo**:
  - chapa remachada para los retratos y los eventos;
  - placa de locomotora para la ficha de tren.
- **Mapa**: los marcadores siguen la simbología de los mapas ferroviarios y de estado mayor antiguos.
- **Elementos**:
  - barra de órdenes contextual;
  - alertas priorizadas (en tiempo de juego, §3c);
  - panel de tren (carga, población y horario);
  - panel de obras;
  - informe de inteligencia de la Colmena;
  - checkpoint con rostros.

## 14. Guardado y dificultad
- Guardado libre, más un **modo hierro** opcional (una sola ranura con autoguardado).
- **Pensado para campañas de muchas horas**:
  - autoguardado al empezar cada día de juego y antes de cada gran ataque anunciado, con rotación de ranuras;
  - guardado manual en cualquier momento;
  - el formato del guardado tiene versión, para que las partidas largas sobrevivan a las actualizaciones del juego (migración de partidas).
- El guardado es el estado completo de la simulación (§17.3). Hay que medir su tamaño y tiempo con una red grande y con la memoria de la Colmena acumulada: **PROTOTIPO**.
- **Dificultad (v1.12, D-N25)**: tres niveles. Cada uno mueve dos cosas: la **curva de crecimiento** de la Colmena (el modelo de Hugo) y la **velocidad con la que aprende** (los umbrales y el decaimiento de la memoria, §5).

  | Nivel | Jugador equilibrado | Jugador con prisa |
  |---|---|---|
  | Fácil | 2 % de derrotas | 11 % |
  | **Normal (por defecto)** | 5 %, pero pasa escasez el 45 % de los días y pierde unos 4–5 nodos por partida | 42 % |
  | Veterano | 12 % | 75 % |

  - **Por qué tres niveles**: la huella castiga a la vez al que crece deprisa y al equilibrado. Con una sola curva no se pueden cumplir los dos objetivos.
  - En una campaña de 40–100 h, el nivel por defecto hace sufrir sin tirar a la basura decenas de horas.

## 15. MVP (rebanada vertical)
- **Red**: nudo en **Sagunto**, con la línea Sagunto–Teruel–Zaragoza (interior y montaña) y la costera Valencia–Sagunto–Castellón (puerto y costa). Son unos 10–12 nodos y **3–4 trenes**.
  - **Nodos canónicos (D-N14)**: Sagunto (con el Puerto) · Puçol–Valencia · Almenara–Nules–Castellón · Segorbe–Barracas–Teruel–(puente del Jiloca)–Caminreal–Calamocha–Cariñena–Zaragoza. Los ganchos para después son reabrir Caminreal–Calatayud y Castellón–Vinaròs.
  - **Guion de la demo** en tres actos, con 8 personajes con nombre y la pantalla final «Lo que la Colmena aprendió de ti»: `demo-sagunto-guion.md`. El diseño del hito 3 está en `diseno-hito3.md`.
- **Contenido**: 3 tipos de zona (estación, pueblo y tramo/desmonte), 3 tipos de zombi, 2 de infantería, 1 blindado de transporte **que viaja en el tren y se despliega**, 1 tren de combate y 1 de obras, 6 piezas de construcción y 4 recursos.
- **Estaciones MVP (v1.6)**: fundar **1 estación nueva** en un emplazamiento, con población, fortificación y checkpoint. **1 taller** (Sagunto) que fabrica un tren nuevo. Inventario del tren con consumo de las unidades embarcadas.
- **Apoyo MVP (v1.13, D-N143 y D-N155)**: el vagón artillero y **el NH90 desde el helipuerto de Sagunto**, que aterriza y lleva un pelotón. El apoyo aéreo solo despega de aeródromos o de helipuertos construidos en estaciones. Sagunto empieza con el suyo. Los cazas, el Chinook y el apoyo naval quedan fuera del MVP.
- **Colmena MVP**: memoria de tráfico y de atención, y 3 estados (deriva, caza y asedio), con el informe de inteligencia. **Confirmado por Eugenio el 7-nov (D-N160)**: sigue en el MVP y entra en la build **después del tutorial**.
- **Progresión MVP**: etapas 1 y 2, con 2 automatismos.
- **Vías MVP**: reparar tramos y un puente.
- **Alcance**: el MVP es **el arranque de una campaña larga** (etapas 1 y 2), no un juego de 2–4 h. Las "2–4 h" son lo que dura **jugar todo el contenido de la demo**. Debe poder guardarse y seguir, y mostrar ya la escalada mutua (tú creces y la Colmena se endurece).
- **Criterio de éxito**: 2–4 h de juego con el contenido del MVP en la que tienes que saltar entre líneas atacadas a la vez, la Colmena castiga un horario repetido, se mantienen 10k+ zombis activos a 60 fps en tu equipo y la logística te obliga a elegir.
- **Estado (5-nov, noche)**:
  - el prototipo corre en Unity (10k zombis a 198 FPS);
  - el hito 1 está casi hecho y el hito 2 está aprobado por Eugenio;
  - el hito 3 funciona de punta a punta: mapa 3D, zoom a la zona, horda materializada, disparo desde el tren o a pie, munición de la carga del tren y vuelta al mapa (Marcos graba un vídeo del bucle);
  - el hito 4 empieza por la memoria de tráfico (`diseno-colmena-h4.md`);
  - hoja de ruta vigente en `hoja-de-ruta.md`.
- **Ritmo de trabajo**: continuo; Eugenio revisa sobre la marcha. No hay fecha fija, pero los hitos van en orden. **La fuente vigente es `hoja-de-ruta.md`**:
  1. Zona.
  2. Red.
  3. Unión.
  4. Colmena.
  5. Construir.
  6. Campaña.
  7. Demo pulida de Sagunto.
  8. *(Después de la demo)* prototipo de coop en LAN (§17).

## 15b. Cambios del 7-nov (v1.13): de «la noche de Sagunto» al MVP
Desde el 6-nov el trabajo ha ido a «la noche de Sagunto» (D-N71), un combate en una sola estación. El 7-nov Eugenio dio el diseño que convierte eso en el arranque del MVP. Todo está en `decisiones-noche.md`:
- **Inicio (D-N156)**: se empieza con 3 estaciones, que son **Sagunto** (principal), **Nules** (pequeña) y **Castellón** (principal). *(v1.15)* ~~infestada, D-N131~~: es tuya, pero está **cercada** y aislada, y romper el cerco es una misión (D-N183, D-N184, `misiones/romper-cerco-castellon.md`). El resto de la red se ve bloqueada y se abre reparando la vía.
- **Intro (D-N158)**: antes de la primera partida, una intro breve con el lore (el año, lo que pasó, que el tren es lo único que queda y tu objetivo de recuperar la península reparando la red). El año está por fijar.
- **Ataques (D-N136, D-N157, D-N161)**: no hay oleadas, ni barra de progreso hacia el día. Cada ataque es una sola gran horda. **El primer ataque es el día 1, de día**, más pequeño, y es el del tutorial. Esto enmienda la D-N08 y la D-N36. La primera gran horda llega esa noche.
- **Asedio (D-N151)**: cuando atacan una estación, las puertas se cierran del todo. Los zombis tienen que romper muro o puerta. Una parte de la infantería está dentro y otra fuera, con los vehículos.
- **Estación ocupada (D-N152)**: un tren que llega a una estación sitiada espera a las puertas, expuesto, y no puede entrar. Cada estación tiene plazas para trenes, y ampliándola se ganan más. Aquí empieza la gestión de la red.
- **Modo construcción (D-N153; amplía el §9 y el §9c)**: lo primero es reparar muros, que se modelan como sacos terreros y HESCO de verdad. Después vienen ampliar la estación, las torretas de muro (que hacen crecer el muro), las torretas automáticas, la artillería emplazada y los helipuertos. Más adelante, minas y morteros.
- **Tutorial (D-N154; enmienda la D-N150)**:
  - 0, intro;
  - 1, defender Sagunto de día;
  - 2, reparar en el modo construcción;
  - 3, preparar y cargar un tren, con apoyo terrestre, y llevarlo a Nules;
  - 4, más tarde, el apoyo aéreo desde un helipuerto.
  - Se puede saltar. *(v1.15)* ~~Solo sale la primera vez~~: cada «Nueva partida» pone la intro (se puede saltar) y pregunta «¿Quieres hacer el tutorial?» (decisión del 9-nov 21:18).
- **Fin de un ataque (D-N149, D-N146)**: no hay estrellas. Sale «Sagunto resiste» y se sigue en el mundo.
- **Después del MVP (D-N159)**: el árbol de investigación, para mejorar y desbloquear unidades.
- **Hordas de decenas de miles (objetivo firme después del MVP; Eugenio, 9-nov)**: Eugenio quiere ver decenas de miles de zombis en pantalla, como en la referencia. En el MVP las hordas van de 2.200 a 6.550 porque el balance está calibrado con esas cifras. Después del MVP es un objetivo firme, no una idea. Hay dos vías en estudio (`economia/hordas-grandes.md`, D-N182): (a) hordas enteras que combaten, con más defensores, supervivientes por tren y tope de zona por nivel; (b) una masa visible de decenas de miles de la que solo combate la fracción que llega al muro, y la dificultad se regula con esa fracción. Se decide con las medidas de render (Marcos y Bruno), de simulación (Nacho) y de economía (Hugo) posteriores a qa48. Desde el MVP, la horda ya nace fuera de la vista y llega andando (D-N182).
- **Orden del MVP** (plan del 8-nov): primero los bloques del domingo (controles, asedio, reparar, trenes y tutorial), luego la Colmena (D-N160) y luego la construcción ampliada. La hoja de ruta lo recoge.

## 16. Riesgos principales
| Riesgo | Tipo | Mitigación |
|---|---|---|
| Integración entre S0 y S2 | Técnico, muy alto | Hito 3 dedicado y pruebas de calibración |
| Zoom continuo sin cargas | Técnico, alto | SubScenes pre-cargadas cuando llega la alerta; fundido |
| Rendimiento (horda, shader y construcción) | Técnico, alto | Presupuesto por frame desde el hito 1 y profiler |
| Colmena percibida como injusta | Diseño, alto | Informe de inteligencia, avisos y memoria que decae |
| Muchas crisis a la vez abruman | Diseño, alto | Pausa táctica, automatismos y prioridad de alertas |
| Microgestión que crece con la red | Diseño, medio | La automatización es la progresión |
| Rechazo a todo el audio con IA | Reputación, medio | Curación, coherencia y declaración en Steam |
| **Licencia de Hunyuan3D**: excluye la UE, el Reino Unido y Corea del Sur, incluidos sus resultados (LICENSE §1(l) y §5(c) en la 2.0; §4(c) en la 2.1). Eugenio está en España | **Legal, alto** | **Riesgo aceptado por Eugenio el 5-nov-2026**, conociéndolo. Mitigación disponible: rehacer las piezas en Blender o regenerarlas con TRELLIS.2 (MIT) antes de publicar si hiciera falta. Guardar en el registro de assets qué piezas vienen de Hunyuan |
| Calidad irregular del 3D generado | Producción, medio | Solo para piezas clave; limpieza en Blender; el shader unifica |
| Pixelab no se renueva (reinicio el 17-nov) y el **lote está parado** por decisión de Eugenio (primero el juego) | Producción, medio | Piloto, paleta y reparto listos para retomarlo. Si no se renueva, los iconos y retratos se harán con la API de imagen de ElevenLabs más reducción a la paleta, o a mano |
| ECS sin animación oficial | Técnico, medio | VAT y modelo híbrido con GameObjects para lo poco numeroso |
| Alcance | Producción, alto | Hitos en orden; lo que no sirve a los pilares se recorta |
| Determinismo para un coop futuro | Técnico, medio | Reglas de §17.3 y prueba de hash desde el hito 1 |

## 17. Red: preparación para cooperativo y multijugador (v1.1)

> Decisión de Eugenio (5-nov): el juego se prepara desde el principio para un posible coop o MP. **El MVP no lleva código de red**, pero sí las reglas de arquitectura que lo hacen posible sin reescribir.

### 17.1 Qué modo de juego
- **Recomendación: cooperativo para 2–4 jugadores sobre la misma red ferroviaria.** Cada jugador lleva sus líneas y todos comparten recursos y la Colmena. Encaja con el pilar 3: la atención se reparte entre personas.
- **Versus (PvP)**: no se recomienda (necesitaría equilibrio competitivo y otro juego). Como idea futura queda un modo asimétrico en el que un jugador es la Colmena. **[idea, sin evaluar]**

### 17.2 Arquitectura recomendada: lockstep determinista
| Opción | Cómo funciona | Encaje con Vía Muerta |
|---|---|---|
| **Servidor autoritativo con réplica de estado** (Netcode for Entities) | El servidor simula y envía *snapshots* de cada entidad ("ghost") a los clientes | **Malo para la horda**: 10–20k zombis por zona no se pueden replicar uno a uno. Hasta usuarios de los foros de Unity coinciden en que sincronizar cada unidad "no escala más allá de unas pocas decenas". Netcode for Entities (v1.5) está pensado para pocas entidades con predicción (shooters) |
| **Lockstep determinista** ★ | Solo se envían las **órdenes** de los jugadores; todas las máquinas simulan lo mismo en el mismo orden | **Bueno**: es el modelo clásico de los RTS. El ancho de banda no depende del número de zombis |
| Motor determinista de terceros (Photon Quantum) | Su propio ECS determinista | Implica reescribir sobre otro ECS. Es de pago. Descartado |

- **Por qué ahora es viable**: desde **Burst 1.8.25** (septiembre de 2025), `FloatMode.Deterministic` está soportado. Usa funciones matemáticas deterministas y desactiva optimizaciones que varían entre plataformas, pero solo en 64 bits, solo en código Burst y sin garantizar el patrón de bits de los NaN. [Docs de Unity](https://docs.unity.com/en-us/engine/6000.6/manual/programming-environment/script-compilation/burst/compilation/float-precision-determinism), [Unity Discussions](https://discussions.unity.com/t/what-is-the-state-of-bursts-floatmode-deterministic/1668491)
- **Unity no ofrece lockstep hecho.** Según usuarios del foro, el Multiplayer Center de Unity 6 lo lista como arquitectura pero no lo incluye **[sin verificar en fuente oficial]**. La capa de lockstep será propia y pequeña: cola de órdenes por tick, retardo de entrada y hash de estado.
- **Transporte (cuando toque)**: Unity Transport o Steam Networking (con relay de Steam). Para publicar en Steam hay que pagar la tasa de Steamworks Direct **[importe sin verificar hoy]**. Unity Relay y Lobby (UGS) son alternativas con capa gratuita limitada **[sin verificar]**.

### 17.3 Reglas de arquitectura desde el día 1 (coste del MVP)
1. **Simulación a tick fijo** (orientativo 20–30 Hz, **PROTOTIPO**) separada de la presentación, que interpola. Nada de `Time.deltaTime` en la simulación.
2. **Todo lo que hace el jugador es una orden** (`Command`): serializable, con número de tick, y entra por una única cola. La simulación solo lee órdenes, nunca el teclado ni la cámara.
   - **Ojo con la Colmena**: su "memoria de atención" lee hacia dónde miras. Con varios jugadores, el foco de cada uno **también es una orden**.
3. **Toda la simulación en jobs Burst con `FloatMode.Deterministic`**. Recursos, economía y la capa S0 con **enteros o punto fijo** (no necesitan decimales).
4. **Aleatoriedad determinista**: `Unity.Mathematics.Random` con semillas por sistema y por tick. Nunca `UnityEngine.Random`.
5. **Orden determinista**: IDs estables propios (`SimId`) y ordenar cuando el orden importe. Nada de escrituras paralelas a hash maps cuyo recorrido afecte al resultado. Doble búfer en la horda: cada agente lee el estado del tick anterior.
6. **Sin física de Unity en la jugabilidad**: colisión continua propia (cápsula contra segmento, §9c) y bloqueo agregado en la rejilla interna del flow field. La física queda solo para efectos visuales.
7. **Hash del estado por tick** y una **prueba de desincronización sin red**: dos simulaciones en el mismo proceso con las mismas órdenes deben dar el mismo hash. Es barato y mantiene el determinismo comprobado desde el hito 1.
8. **Guardado = serialización completa del estado de la simulación**. Sirve también para que un jugador se una a una partida empezada o se reconecte.
9. **Velocidad y pausa** como órdenes. En coop se deciden por votación o las controla el anfitrión.

**Coste estimado [estimación propia]**: un **10–15 % más de trabajo** en los hitos 1–3, sobre todo disciplina. A cambio da **repeticiones, pruebas automáticas, guardado robusto y depuración** también en un jugador, así que compensa aunque el coop no llegue nunca.

### 17.4 Riesgos
| Riesgo | Dónde | Mitigación |
|---|---|---|
| Rendimiento de `FloatMode.Deterministic` en la horda (desconocido) | Horda en DOTS | Medirlo en el hito 1 con 10k agentes; si cuesta demasiado, punto fijo en las partes críticas |
| Diferencias entre CPU (Intel y AMD) a pesar del modo determinista | Toda la simulación | Prueba de hash entre 2 PCs distintos en cuanto exista el prototipo de zona. La garantía oficial es "consistente en plataformas soportadas", sin más detalle |
| Orden no determinista en jobs paralelos (separación, hash espacial) | Horda en DOTS | Doble búfer, ordenación por `SimId` y prueba de hash en CI |
| **Cada máquina simula todas las zonas activas**: en coop, cada jugador quiere su zona y la CPU se multiplica | Simulación global y horda | Límite global de zonas en detalle (p. ej. 1 por jugador, 4 como máximo) y menos zombis por zona en coop |
| El jugador más lento frena a todos (lockstep) | Red | Retardo de entrada adaptativo y requisitos mínimos claros |
| Materializar y desmaterializar con aleatoriedad no reproducible | Simulación global | Semilla derivada del nodo y del tick |
| Desincronizaciones difíciles de depurar | Red | Hash por sistema (no solo global) para localizar el sistema culpable |
| Unirse a mitad de partida implica transferir un estado grande | Red | Guardado compacto y comprimido |
| Que el coop se coma el alcance | Producción | **Fuera del MVP.** Se valora en el hito 8 (prototipo de 2 jugadores en LAN, después de la demo) |

### 17.5 Impacto
- **MVP**: el alcance de juego no cambia. Se añaden las reglas 1–9 a los hitos 1–3.
- **Guía de preparación (Hilo B)**: **no hay que instalar paquetes de red ahora** (ni Netcode for Entities ni Transport). Burst ya viene con Entities; conviene que la guía indique **Burst 1.8.25 o superior** (comprobar la versión que trae Unity 6.3).
- **Hitos**: se añade el **hito 8**, prototipo de coop de 2 jugadores en LAN, después de la demo.

## 18. Publicación: demo y acceso anticipado (v1.9, propuesta)
Eugenio quiere valorar sacar la demo como **acceso anticipado**. Propuesta en tres pasos, cada uno sobre el anterior:

| Paso | Qué es | Contenido | Precio | Cuándo |
|---|---|---|---|---|
| **1. Página de Steam** | Recoger listas de deseos | Tráiler y capturas de la rebanada vertical | — | Cuando el hito 6 tenga imágenes que enseñar |
| **2. Demo gratuita** | Probar el juego y medir interés, idealmente en un Steam Next Fest | Etapas 1–2 en el nudo de Sagunto, limitadas a unos 10 días de juego (unas 3–4 h). La partida de la demo **no** pasa a la versión de pago, para que la demo siga siendo una muestra | Gratis | Después de la página, con la rebanada vertical pulida |
| **3. Acceso anticipado** | Versión de pago en desarrollo, campaña larga real | Etapas 1–3: región Valencia–Aragón con varias líneas, estaciones y talleres, Colmena completa. **Partidas persistentes que sobreviven a las actualizaciones** (guardado con versión, §14) | Inferior al precio final | Cuando la demo valide el bucle |
| **4. Versión 1.0** | Juego completo | Península entera y paso a Francia (etapas 4–5); coop si llega (§17) | Precio final | — |

- **Por qué no vender la demo directamente**: una rebanada de 2–4 h no aguanta el precio de un acceso anticipado sin una campaña que crezca. La demo gratuita da datos (retención, dónde se atasca la gente) antes de cobrar.
- **Actualizaciones durante el acceso anticipado**: cada una abre una región o etapa, nuevas cepas de la Colmena y unidades del catálogo. Encaja con la estructura por etapas (§4).
- **Requisitos de Steam a tener en cuenta**:
  - declarar el uso de IA generativa (audio, imágenes y 3D);
  - la tasa de Steam Direct (**importe sin verificar hoy**);
  - las reglas de acceso anticipado de Valve, que piden ser honesto sobre el estado del juego.
- **Riesgo**: lanzar en acceso anticipado con poco contenido quema la primera impresión. Criterio mínimo propuesto: unas 10–15 h de campaña con la región completa antes de cobrar.
