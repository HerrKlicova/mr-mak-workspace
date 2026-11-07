# Criterio de diseño para el sonido de Vía Muerta (Lucía → Nuria) · 7-nov, 10:46

Bienvenida, Nuria. Esto es lo que el juego necesita del sonido, para que lo uses como punto de partida. Los cómos son tuyos. Lo que pide Eugenio (09:44): sonidos para todo, disparos que suenan distinto de cerca, de lejos y con mucho zoom, el Dragón más potente, impactos y ambiente. Y lo principal: que todo se sienta bien.

## 1. Pilares
1. **El sonido es información antes que adorno.** En un RTS de hordas, el oído avisa de lo que el ojo todavía no ve: una puerta que cede, un pelotón sin munición, una oleada que llega por el norte. Todo aviso de juego tiene sonido, y cada sonido que importa se distingue de los demás.
2. **La distancia la decide la cámara.** Con zoom cercano (Z), el combate es físico: chasquido seco, mecánica del arma y casquillos. Con zoom medio, el estampido y la cola. Alejado del todo (X), solo el retumbar del frente, como una tormenta lejana. En el mapa, la estación en combate es un murmullo de fondo, porque **la noche sigue fuera de pantalla** (D-N91 corregida) y el jugador tiene que oírla seguir.
3. **La noche es silencio tenso con estallidos.** Igual que la imagen (D-N129: oscuro con charcos de luz), el ambiente baja mucho y lo que se oye son los disparos, el fuego y la horda. El contraste es lo que da miedo.
4. **La horda se oye antes de verse**: una masa grave y moteada, con pasos, roces y gemidos superpuestos, que crece con el número. No hay un zombi solista; es un mar. Se lee por el volumen, igual que en la imagen se lee por el valor (D-N80).
5. **Lo nuestro suena militar y real; lo de ellos, orgánico.** G36E, MG4E, G28, AG36, C90, el 30 mm del Dragón, el VAMTAC y el NH90: de referencia, grabaciones reales. Las armas no tienen nada de ciencia ficción.
6. **El tren es el corazón.** La llegada del tren (silbato, frenos y vapor o diésel) es el momento de alivio de la partida y tiene que sonar como un abrazo.

## 2. Jerarquía (qué tapa a qué)
1. Avisos de juego: brecha en el muro, ataque entrante, munición baja, tren llegando. Siempre se oyen.
2. Armas y explosiones cercanas.
3. La horda.
4. Vehículos y helicóptero.
5. Ambiente y música.

Hace falta un límite de voces por categoría. Con 512 trazadoras en pantalla no pueden sonar 512 disparos: se agrupan en «fuego de pelotón».

## 3. Coherencia con lo que ya está decidido
- Rojo 982420 = ataque → **el sonido de alarma solo para ataque o brecha**. Ámbar = aviso → un tono de aviso distinto y menos agresivo.
- Trazadoras de 1 de cada 3 y 1 de cada 4 (encargo de disparos §4): el sonido no sigue a las trazadoras, sino a todas las balas, agrupadas.
- Fogonazo de 2 fotogramas: el ataque del disparo es igual de corto y seco.
- Fuego de suelo solo visual: suena como crepitar ambiental, sin daño.
- Interfaz: clics secos y metálicos, de radio militar, coherentes con el HUD 181c30 / d4d0cc.

## 4. Normas del proyecto que te afectan
- La clave de ElevenLabs va **solo en una variable de entorno**, nunca en el repo. Modelo de texto a efectos: **v3** (lo pide Eugenio). No usar Higgsfield.
- Nada inventado: si un sonido no está comprobado con una referencia real, se marca SIN VERIFICAR.
- Al menos 5 variantes por sonido (también por la norma de variantes, y para no repetir).
- Los cambios grandes van primero como muestra a la galería. Las decisiones con número D-N las asigno yo.

## 5. Lo que te pido primero
Una tabla de sonidos (evento → capas → variantes → distancia cerca/media/lejos/mapa → prioridad) y una muestra corta: un pelotón de G36E disparando a tres distancias, el 30 mm del Dragón y la horda acercándose. Lo escuchamos y desde ahí cerramos el criterio con número.

— Lucía (Diseño)
