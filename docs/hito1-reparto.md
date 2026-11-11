# Hito 1 del núcleo v2 · reparto (Lucía, 11-11 23:15)

Eugenio (22:47): «arranca si… pensado para coop… empezad con todo… coordinaros bien… seguramente haya sesiones que se caigan».

Plan: [plan-nucleo-v2.md](plan-nucleo-v2.md). Decisiones: D-N205 (núcleo v2, aprobado) y D-N206 (coop, lockstep).

**El Hito 1** es un terreno de 2 × 2 km en una sola escena, con zum continuo del mapa al soldado.
- Hay dos estaciones, A y B. El jugador traza la vía entre ellas.
- Una línea de dos paradas lleva munición sola.
- Un pelotón se manda a mano y tiene munición limitada.
- Un caserío con unos cien zombis deja material de vía al limpiarlo.
- Hay prueba de hash en dos instancias.

## Reglas para todos (por si se cae una sesión)
1. **Relevo vivo.** Cada uno mantiene `docs/hito1/relevo-<nombre>.md`, con lo hecho, lo que falta, las ramas y los archivos. Se actualiza cada vez que se cierra algo, para que otra sesión pueda seguir sin preguntar.
2. Lo que no está verificado se marca SIN VERIFICAR.
3. Nada de builds a Eugenio sin una partida completa con ventana.
4. PC por turnos, que da el coordinador. Ahora le toca a Marcos, con el prototipo del zum.
5. Lo original es lo nuestro: nada copiado de ningún juego de transporte, ni interfaz, ni nombres, ni aspecto.
6. Si una sesión no responde en 2 horas, el coordinador abre otra con el relevo de esa persona.

| Quién | Encargo | Cuándo está hecho |
|---|---|---|
| **Marcos** (lo arranca el coordinador) | Escena única con zum continuo y carga por trozos, y la vista de la zona dibujando lo que dice la simulación. | Prototipo del zum de mapa a soldado sobre el terreno de Álvaro, en captura y vídeo. |
| **Iker** (coordinador) | Red de vías construible en NetWorld (grafo, trazado y estaciones), líneas y trenes visibles moviéndose. | Trazar vía A–B y ver un tren hacer la línea en bucle. |
| **Nacho** (coordinador) | NightSim como simulación única del mundo: zombis con nivel de detalle, pelotón con munición y prueba de hash en dos instancias. | Pruebas en verde y el mismo hash en las dos instancias tras 10 minutos de juego. |
| **Hugo** | Cifras del Hito 1: munición por soldado, munición inicial en B, capacidad y tiempo del tren, material del caserío. Que sin la línea el pelotón se quede seco y con ella termine. Cuatro recursos para el corte completo (munición, gasoil, raciones y material) con consumos por hora y en combate. | Una tabla con las cifras y su medida en NightSim o en el modelo. |
| **Álvaro** | El terreno de 2 × 2 km de costa (relieve, huerta, carretera vieja y cauce), con las posiciones de A, B y el caserío, y obstáculos para la línea de visión. Plantillas de pueblo y de ciudad en ruinas para más adelante. | Mapa de alturas y CSV de posiciones en el repo, y un plano con cotas. |
| **Teo** | Kit de vía modular para trazar (recta, curva en tres radios, desvío, topera y cruce a nivel), con los raíles sobre balasto y traviesas. Estación pequeña colocable. 5 variantes de casa en ruinas para el caserío. | FBX en el repo con la tabla de entregas, y capturas. |
| **Bruno** | Estética del zum: qué se ve en cada nivel (mapa, comarca, pueblo, soldado), fundidos, iconos de unidades y trenes en el mapa, y el trazado de vía con vista previa (válido o inválido). La calima de día, adaptada. | Una lámina por nivel de zum y la paleta, en la galería. |
| **Nuria** | Sonido del Hito 1: tender vía, tren saliendo y llegando, carga y descarga, «sin munición» y ambiente por nivel de zum (más lejos, menos detalle). Primero lo que ya hay; ElevenLabs solo con la clave en variable de entorno. | Tabla de evento → archivo, con los archivos en el repo. |
| **Sara** | Plan de QA del Hito 1: guion de los pasos con ventana, lo que cuenta como fallo, la prueba de hash en dos instancias y los «no tiene sentido para un jugador» que hay que buscar. | docs/qa/plan-hito1.md, listo antes de la primera build. |
| **Paula** | Referencias de juegos de logística militar y de construcción de redes: cómo enseñan consumo, alcance y abastecimiento (sin copiar). Vías de la costa valenciana reales (Sagunto–Nules) para el terreno. Con fuente y licencia. | Un documento con citas o capturas y 5 o más referencias de cada parte. |
| **Elena** | Crónica: el giro del 11-11 («aprovechar lo que tenemos y empezar con otra idea») y el arranque del núcleo v2. | Crónica actualizada con el enlace. |
| **Lucía** | Diseño del trazado de vía y de las líneas (interacción, clics y paneles), el coop (papeles y recursos compartidos), y revisión de cada entrega contra el plan. | docs/hito1/diseno-vias-lineas.md. |
