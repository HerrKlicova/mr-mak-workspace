# Encargo para Marcos: selección, destino y formaciones; trazadoras y fogonazos; noche sin sepia; parches y reinicio al alejar (v1)

Lucía (Diseño), 7-nov, 09:30 (Madrid). Lo que Eugenio ha visto en la build a las 09:20, con una foto de la pantalla. Va en orden de prioridad. **Nada de esto se mete antes de que la Noche23 confirme que la noche se gana** (P0 del plan del día), salvo el punto 1, que es un fallo que rompe la partida.

## 1. P0 · Alejar con la rueda reinicia la noche (corregido a las 09:40 tras la aclaración de Eugenio)
- Eugenio: «me acabo de alejar sin querer con el ratón y se ha reiniciado la noche». Y luego (09:25): **«Tú puedes salir. Es un mundo persistente. Si te apetece, puedes salir y visitar otra estación. El combate no se para».**
- **El fallo no es salir al mapa: es que al salir se reinicia la noche.** Salir de la zona tiene que estar permitido siempre, también en mitad de un ataque.
- **Comportamiento correcto**:
  1. Alejar del todo (o M) lleva al mapa **en cualquier momento**, también durante la noche.
  2. **La noche sigue corriendo mientras estás fuera**: el reloj, las oleadas, la pila, el muro, la munición y los pelotones con su última orden. Fuera de pantalla se resuelve igual que dentro: la simulación de la noche (el mismo orden por tick que NightSim, contrato de Nacho) sigue avanzando aunque la zona no se dibuje.
  3. En el mapa, Sagunto sale como frente activo (D-N95) con el estado del muro y la munición, y se puede volver a entrar.
  4. **Al volver, la zona enseña el estado actual**, no la noche desde el principio.
  5. Solo «Volver a empezar» reinicia.
- **Mientras la zona y el mapa no estén unidos (deuda aceptada)**: si a Marcos le cuesta mantener viva la simulación de la zona fuera de pantalla, la salida mínima aceptable es que la escena de la zona **no se descargue** al ir al mapa: se oculta y sigue simulando. **No vale limitar el zoom para impedir salir**, porque contradice el mundo persistente.
- Prueba: a mitad de la O2, salir al mapa durante 60 s reales y volver. El reloj ha avanzado 60 s × 28, la pila y la munición han cambiado y el hash coincide con el de una corrida sin salir.

## 2. Selección: que se vea qué controlas
Eugenio: «cuando tienes unidades seleccionadas, no hay nada visual que te indique qué unidades controlas».
- **Las piezas ya están dibujadas y aprobadas (D-N92, Bruno, TBD c8e477e)**: anillo de selección del pelotón (9,6 m, en bucle), del vehículo (12,8 m, doble y con muesca de proa) y anillo de «encima». Solo hay que montarlas.
- Pelotón seleccionado: el anillo de 9,6 m en d4d0cc bajo el pelotón, que lo sigue, y además **una marca de 1 px bajo cada soldado** (un punto en d4d0cc), para que se vea quién es de quién cuando dos pelotones se mezclan.
- Vehículo seleccionado: su anillo doble con muesca hacia la proa.
- Al pasar el ratón por encima: el anillo de «encima», más fino.
- La tarjeta del pelotón en el HUD se enmarca en d4d0cc mientras está seleccionado. El número de la tarjeta (1–5) selecciona y, pulsado dos veces, lleva la cámara.
- Selección por arrastre con el botón izquierdo (el rectángulo de la D-N92).

## 3. Destino y formaciones, al estilo Total War
Eugenio: «tienes que poder elegir dónde moverlos… esa pista visual de a dónde los quieres mover y qué formación les pones… en línea o dibujando un cuadrado los pones como en pelotón».

### 3.1 Cómo se da la orden
- **Clic derecho**: mover al punto. El pelotón conserva la formación que tenía y mira hacia donde iba.
- **Clic derecho y arrastrar**: **dibujas el frente**. Desde que pulsas hasta que sueltas, el juego dibuja la línea del frente y la **silueta fantasma** de dónde va a quedar cada soldado. El largo de la línea decide cuánto frente ocupa el pelotón (cuanto más larga, menos filas) y la dirección de arrastre decide hacia dónde miran: a la izquierda de la dirección del arrastre, como en Total War. Al soltar, se da la orden.
- **Con varios pelotones seleccionados**, se reparten a lo largo de la línea en el orden de sus tarjetas, con 2 m de separación entre pelotones.
- **Vehículos**: sin formación. El arrastre solo da el punto y la orientación final (la flecha de proa).
- La orden lleva la marca de mover de la D-N92 en el destino, que se queda hasta que llegan. Mientras van, se ve la línea de la ruta con los chevrones de la D-N94.

### 3.2 Formaciones (4; teclas y botones del HUD)
| Formación | Tecla | Cómo queda | Para qué |
|---|---|---|---|
| **Línea** (por defecto) | F1 | 1 o 2 filas a lo largo del frente dibujado, 1,5 m entre soldados | Fuego contra el muro: todos disparan |
| **Bloque** (cuadrado) | F2 | El arrastre dibuja un lado y el pelotón forma un cuadrado lleno detrás, 1,2 m entre soldados | Pelotón compacto que aguanta el contacto, en reserva o defendiendo un punto |
| **Columna** | F3 | Fila de a dos en la dirección del arrastre | Moverse por calles y andenes estrechos |
| **Dispersa** | F4 | Línea con 3 m entre soldados y un ligero zigzag | Menos bajas por contacto en campo abierto |
- **Bloque con el ratón** (lo que dice Eugenio de «dibujar un cuadrado»): con **Alt + arrastre derecho**, el arrastre dibuja la diagonal de un rectángulo y el pelotón lo llena, orientado hacia el lado largo más alejado del recinto. Si a Marcos le cuesta, vale con F2 + arrastre.
- Las formaciones son **propias del pelotón**: el HUD muestra la activa con un icono pequeño en la tarjeta. Bruno dibuja los 4 iconos (encargo aparte).
- **Silueta fantasma**: un punto de 2×2 px por soldado en d4d0cc al 50 % y una flecha corta de orientación. Si un punto cae dentro de un muro o fuera del recinto, se pinta en hueso con una × y el soldado ocupa el sitio libre más cercano.
- Determinismo (GDD §17.3): la orden que entra en la cola lleva los dos puntos del frente (en enteros de mm), la formación y la lista de pelotones. Los huecos se calculan en la simulación, nunca en la vista.
- En el MVP, el pelotón **se mueve como ahora y forma al llegar**. Mantener la formación en marcha es para después.

## 4. Disparos: trazadoras, no láseres
Eugenio: «los disparos parecen rayos láser. Quiero trazadoras, que se vea por dónde viaja pero no se mantenga con una línea dibujada… que la bala se ilumine suavemente por donde viaja, que los soldados tengan animación de apuntar y fogonazos».

### 4.1 Trazadora
- Cada trazadora es un **trazo corto que viaja**: cabeza de 2 px y estela de 4–6 px que se apaga hacia atrás. **Nunca une el arma con el blanco de golpe.**
- **Velocidad visual de unos 200 m/s** (no la real de ~900 m/s), para que a 20–30 m se vea cruzar durante 0,1–0,15 s. A tiradores y lanzagranadas, más lento (proyectil del lanzagranadas en arco, ~60 m/s, con humo de 1 px).
- **Estela que se desvanece** en 0,08 s: en cada fotograma, los píxeles de atrás pierden brillo (de la cabeza al final: f0dc9c → e08c30 → e08c30 al 50 % → nada). Es el «se ilumina suavemente por donde viaja».
- **Colores**: cabeza en crema f0dc9c y estela en ámbar e08c30. Es un VFX de ≤ 0,25 s, el único uso del ámbar fuera de los avisos que permite la reserva. **Nada de rojo.**
- **No todas las balas son trazadoras**: 1 de cada 3 en los fusileros, 1 de cada 4 en las ametralladoras (que disparan mucho más, así que se ven más) y todas en los tiradores. Así se lee el volumen de fuego sin cubrir la pantalla.
- Dragón: trazadora más gruesa (3 px de cabeza) y más lenta (150 m/s visual). NH90: las de la ametralladora de puerta, como las de las ametralladoras.
- Impacto: un chispazo de 1 fotograma en el zombi (2 px en hueso). Sin sangre.
- Límite de rendimiento: como mucho 512 trazadoras a la vez, en un pool. Si se pasa, se saltan las más viejas.
- Es solo vista: no toca la simulación ni el hash.

### 4.2 Fogonazo
- En la boca del arma, **2 fotogramas (≈ 0,05 s)**: una estrella de 3×3 px en crema f0dc9c con las puntas en ámbar e08c30. En las ametralladoras, 4×4 px; en el Dragón, 6×6 px con un anillo de humo gris que dura 0,4 s.
- De noche, el fogonazo **ilumina un instante al soldado**: un destello de 1 fotograma que sube el brillo de su silueta. Es lo que hace que la tropa se lea en la oscuridad.
- No hace falta luz real de Unity: con un sprite emisivo vale. Si cuesta FPS, fuera.

### 4.3 Animación de apuntar
- Tres poses: **reposo** (arma baja), **apuntando** (arma al hombro, orientado al blanco) y **disparo** (1 fotograma de retroceso).
- El soldado pasa a «apuntando» en 0,25 s en cuanto tiene blanco y vuelve a reposo 1,5 s después del último disparo.
- **Teo** hace la pose «apuntando» del soldado aprobado (LOD0 y LOD1, para las 5 variantes, sin cambiar el material). Con dos poses y el retroceso por código (2 px hacia atrás, 1 fotograma) basta. Si con DOTS solo se puede cambiar de malla, vale el cambio de malla.

## 5. La noche sale en sepia
Eugenio: «de noche todo está pintado en sepia. Es bastante feo… que los vehículos tengan sus texturas».
- **Lo que se ve en la foto** (es una foto de la pantalla con el móvil, así que los colores no se pueden medir; **SIN VERIFICAR**): el suelo sale beige crema plano, todo lo demás oliva y las sombras en un azul muy saturado. No hay ningún color propio: ni el boscoso, ni la teja, ni la chapa de los vehículos. Parece que la cuantización a la paleta de 32 con la luz de noche junta casi todo en 3 o 4 tonos (beige, oliva y azul).
- Lo que pido a **Marcos**: (1) **una captura limpia de la noche desde el juego** (F12 o la de Sara, no una foto de la pantalla), con un vehículo, soldados y suelo, para medirla; (2) comprobar que los vehículos usan los modelos de Teo con su textura T_Paleta32 y no un color plano; (3) decirnos qué hace ahora la luz de noche (color, intensidad y si va antes o después de la cuantización).
- **Bruno** prepara, sobre esa captura, **5 variantes de la noche** (es un cambio visual grande: va primero como muestra). Criterios que fijo yo:
  - **Luz de luna fría y poco saturada**, gris azulada, no sepia ni beige. Las sombras van en gris azulado oscuro (de la familia 181c30 / 303424), **nunca en un azul saturado**.
  - **Los colores propios se tienen que reconocer**: el boscoso del soldado, la teja, el blanco de la fachada, la chapa de los vehículos. La noche baja el brillo, no borra el color.
  - El suelo no puede ser una losa plana: tiene que tener por lo menos 3 valores.
  - La horda sigue en su banda L* 9–13 (D-N80) y se tiene que leer contra el suelo de noche.
  - Los focos dan luz cálida en su cono: es el único sitio cálido de la noche, y eso ayuda a leer el recinto.
- Elijo yo la variante con la captura delante y se la paso a Marcos.

## 6. Siguen los parches en el suelo
- En la foto se ven **rectángulos oliva oscuros sobre el suelo beige**, con los bordes rectos. Pueden ser las celdas del fuego de suelo (3 m), las teselas del suelo de Sagunto o los decals de la huerta. **SIN VERIFICAR** con una foto.
- Marcos: con la captura limpia del punto 5, dinos qué objeto es (nombre en la jerarquía). Si son celdas del fuego, no deberían verse sin fuego; si son teselas, su borde tiene que fundirse con el de al lado.

— Lucía (Diseño) · [retrato](/mnt/project-files/equipo/retrato_lucia_64_x4.png)
