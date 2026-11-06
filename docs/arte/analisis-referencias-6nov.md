# Análisis de las referencias visuales del 6-nov

Autora: Lucía (Dirección de arte) · 6-nov-2026
Fuente: cinco capturas de Ebbtide que mandó Eugenio (calle de día al amanecer, base con artillería y construcción, atardecer, noche con focos y asedio masivo).
Regla: **inspirarse, no calcar**. Eugenio lo ha dicho claro: no tiene que ser igual. Lo que extraemos son principios de lectura; la paleta, la interfaz y la composición siguen siendo nuestras (Península, el tren y la vía como protagonistas, paleta de 32).

Sobre las cifras: las capturas están comprimidas y reescaladas, así que **todo tamaño en píxeles es una estimación** medida a ojo sobre recortes ampliados y normalizada a una pantalla de 1920 px de ancho. Lo marco con «(est.)». Los valores de nuestro lado salen de `direccion-visual.md` v1.4, de la paleta y de la captura del prototipo `captura_20261106_000156.png`.

---

## 0. Resumen en cinco frases

1. **Se ven zombis porque cada uno es una figura vertical aislada con su sombra.** No es más resolución: es separación, pose y sombra proyectada.
2. Nuestra horda hoy es una **alfombra**: cuerpos pegados, sin huecos, sin sombra y con ruido de color. Por eso se lee como textura (las «garras»), no como gente.
3. La luz de Ebbtide es **un único color dominante por hora** (amarillo cálido, naranja, negro con charcos de luz) y la horda siempre queda **más oscura** que el suelo.
4. La construcción se lee por un **contorno blanco de 2 px**, una rejilla celeste bajo el cursor y **radios dibujados como arcos de línea fina**.
5. La interfaz es plana, negra translúcida, con **un acento ámbar y rojo solo para alertas**, y se queda en los bordes: el centro de la pantalla es del mundo.

---

## 1. Legibilidad de los zombis a distintas escalas

### Lo que se ve

| Captura | Altura de la figura en pantalla (est.) | Cómo se lee |
|---|---|---|
| 1 · calle al amanecer, zoom medio | 15–20 px | Figura negra vertical, brazos extendidos al frente, **sombra proyectada 2–3 veces más larga que la figura**, en diagonal y con el mismo tono. Hay huecos de suelo entre casi todos. |
| 2 · base de día, zoom cercano | 25–35 px (soldados) | Modelo low-poly con volumen y color propio; se ve hasta la pose de carga del cañón. |
| 3 · atardecer | 12–18 px | Siluetas oscuras contra el suelo naranja; donde la masa se aprieta junto al muro se funde en mancha, pero el **borde exterior de la masa siempre deja figuras sueltas**. |
| 4 · noche | 10–15 px | Solo se ven dentro de los charcos de luz, como negro sobre amarillo. Fuera de la luz son ruido oscuro y no importa. |
| 5 · asedio, zoom lejano | 8–12 px | Miles de palitos verticales con su sombra. Aun así cada uno es un trazo vertical separado: **la densidad visual se mantiene baja aunque haya miles**. |

### Los cuatro principios que explican que «se vea que son zombis»

1. **Silueta vertical alta y estrecha.** Proporción de alto a ancho de 3:1 o más (est.). Nunca un cuadrado. La cabeza no se distingue a distancia, pero el palito vertical ya dice «persona».
2. **Pose con brazos al frente.** A 15–20 px el gesto de los brazos rompe la silueta en una «T» torcida. Es lo único que diferencia un zombi de un soldado a esa escala. A menos de 12 px desaparece y solo queda el palito.
3. **Sombra proyectada como segunda silueta.** Es el truco principal. La sombra duplica el área legible, marca la dirección del sol y separa la figura del suelo aunque el color se parezca. De día y al atardecer la sombra es larga (sol bajo); en el asedio también.
4. **Densidad con aire.** Incluso en el asedio queda suelo visible entre la mayoría de figuras. Estimo un 30–50 % de suelo visible dentro de la masa (est.). Donde no hay huecos (pegado al muro), la masa se convierte en mancha, y eso es aceptable porque el borde sigue teniendo figuras sueltas.

### Nuestro estado (captura de las 00:01 del 6-nov)

- 10.000 zombis a pixelado 1/3, paleta al 65 %. Cada zombi ocupa unos **3×4 a 4×6 píxeles de la capa baja**, es decir 9–18 px de pantalla: el tamaño en sí es parecido al del asedio de Ebbtide.
- Pero están **pegados**: no hay suelo visible entre ellos dentro de la masa. Se lee como una alfombra granulada.
- **Sin sombra proyectada.**
- **Ruido de color**: mezcla de marrones, azules y rojizos por zombi. A ese tamaño el color distinto rompe la silueta en vez de ayudar. En Ebbtide la horda es prácticamente **un solo valor oscuro**.
- La mancha LOD por debajo de 16 px (4×5, #1c200c, sin iluminar) va en la buena dirección de valor, pero **4×5 es casi cuadrada**: pierde justo la verticalidad que hace legible la figura.

### Recomendaciones

**Marcos (Unity, render de la horda)**
1. **Sombra proyectada de la horda** (prioridad 1). Opción barata compatible con DOTS: un quad de sombra por zombi, plano sobre el suelo, oscuro (#000000 al 45–55 % de opacidad, est.), alargado en la dirección contraria al sol, con largo = 1,5× la altura del zombi de día y 2,5× al amanecer y atardecer. Se dibuja en la capa baja, así se pixela con el mundo. Si las sombras reales de URP son más baratas de lo que pienso, valen igual; lo que importa es que existan para todos los zombis, también en LOD.
2. **Mancha LOD vertical**: pasar de 4×5 a **2×6 o 3×7 píxeles de la capa baja**, proporción ~1:3, con un píxel de cabeza más estrecho arriba si cabe. Mantener #1c200c, que va bien sobre nuestros suelos claros. Añadirle su sombra (punto 1).
3. **Un solo valor para la horda**: reducir la variación de color por zombi al ±8 % de luminosidad sobre un tono base oscuro (#1c200c o #303424). La variedad se nota al zoom cercano, no a 10 px.
4. **Aire en la masa**: pedir a Nacho/Marcos una **separación mínima entre zombis de 0,6–0,8 de su anchura** en la evitación de la simulación (o un radio de colisión un poco mayor que el visual). Objetivo: 30–50 % de suelo visible dentro de una masa normal. Pegados al muro pueden compactarse; ahí la mancha está bien.
5. **Pose**: si el zombi está por encima de 16 px, que el modelo tenga los brazos al frente siempre (aunque no haya animación). Es lo que dice «zombi» y no «soldado».

**Bruno (pixel art por código)**
- Hacer una **lámina de prueba** de la silueta del zombi a 6, 8, 10, 12, 16 y 20 px de alto, con su sombra, sobre los tres suelos (tierra clara, olivo, asfalto) y en las tres horas. Paleta estricta. Sirve como referencia para que Marcos ajuste la mancha LOD y como criterio de aprobación.
- Proponer el **umbral de cambio a LOD**: por debajo de qué altura deja de verse el brazo. Mi estimación es 12 px, no 16.

**Teo (3D)**
- Modelo del zombi para cerca: **proporción alargada** (piernas largas, torso estrecho), brazos adelantados en la pose base y una cabeza algo grande para que se lea en 3D pixelado. Presupuesto bajo, pensado para instanciado masivo (no Hunyuan para hordas).

---

## 2. Iluminación por hora del día y paleta

| Hora | Lo que se ve | Sombra | Horda |
|---|---|---|---|
| Amanecer (cap. 1) | Luz rasante amarillo crema, casi blanca en techos; suelos verdes y beige saturados. | Larguísima, azul grisácea oscura. | Negro sobre suelo claro. |
| Día (cap. 2) | **Gradación casi monocroma amarillo verdosa**: hierba, muros y vehículos tirando a amarillo. Mucha luz, poco contraste de color, contraste de valor por la sombra. | Media, marrón oscuro neutro. | — |
| Atardecer (cap. 3) | Todo naranja ámbar. Bloom fuerte. **Viñeta oscura**. Las sombras se vuelven casi negras. | Larga, casi negra. | Negro sobre naranja. |
| Noche (cap. 4) | Fondo prácticamente negro azulado. **Charcos de luz amarillo verdoso** de los focos con borde suave. Solo dentro de la luz hay color. | Ya no hay sol; la sombra la hacen los focos. | Silueta negra a contraluz dentro de los charcos, invisible fuera. |
| Asedio (cap. 5) | Naranja saturado de fuego e iluminación general. Explosiones que queman a blanco. | Sombras cortas por todas las figuras. | Negro con sombra. |

**Principio**: cada hora tiene **un color dominante** que tiñe todo el mundo, y la horda nunca pierde ser el valor más oscuro del suelo. Es lo que ya decidimos en D-N13 y v1.4, ahora con evidencia directa.

**Comparación con nosotros**: nuestra gradación «día» es beige cálido y apagada; cumple el principio de valor pero le falta luz y contraste de sombra. La paleta de 32 es más terrosa y mediterránea que la de Ebbtide, y así debe seguir: es nuestra identidad.

**Recomendaciones (Marcos, perfiles de gradación)**
- **Día**: subir exposición y contraste (est. +0,3 EV, contraste +15 %), tinte cálido hacia #f0dc9c en luces y hacia #303424 en sombras. Sol a 35–45° de elevación para que haya sombra legible.
- **Amanecer y atardecer**: sol a 10–20°, luz #e08c30, sombras hacia #181c30. Viñeta 0,25–0,35. Bloom con umbral bajo.
- **Noche**: ambiente casi negro (#000000 a #181c30, luz ambiental al 5–10 %), focos con luz cálida #f0dc9c y caída suave; el borde del charco debe ser legible tras el pixelado (2–3 px de degradado en la capa baja, no un corte duro). Ya tenemos foco y haz de Bruno; la clave es **bajar el ambiente** hasta que fuera de la luz no se vea casi nada.
- Revisar que la mezcla de paleta al 65 % no empaste los focos de noche; si se empasta, bajar al 50 % solo en el perfil de noche.

---

## 3. Lectura de la construcción

En la captura 2 se ve el modo construcción completo:

- **Contorno blanco de 2 px** (est.) alrededor de todo el tramo de muro seleccionado y de cada torre. Blanco puro, sin brillo, por encima del pixelado.
- **Fantasma en rejilla**: bajo el objeto a colocar hay una **rejilla de celdas blancas finas de 1 px** de unas 6×6 celdas y la celda ocupada rellena en **celeste saturado** semitransparente. Se sabe exactamente dónde va.
- **Radios**: el alcance del foco es un **sector circular dibujado solo con línea blanca de 2 px**, sin relleno. El alcance general de la base es un **arco blanco grande** que cruza la pantalla. Sin relleno, el mundo se sigue viendo debajo.
- **Etiqueta junto al cursor**: nombre, orientación en grados, tipo y nivel, en caja negra translúcida.
- **Aviso contextual en rojo**: «áreas amuralladas sin entrada», con botón para arreglarlo. Valida el diseño en tiempo real.
- Sacos terreros en anillos con las unidades dentro: la forma de la fortificación cuenta su función.

**Nuestro estado**: H5 tiene obras en la red, coste de muros y nivel de fortificación (Nacho), pero no conozco aún el aspecto del modo construcción en el prototipo. Si no existe, este es el patrón a seguir.

**Recomendaciones**
- **Marcos**: contorno de selección en postproceso a resolución completa (no en la capa baja) para que quede nítido: 2 px, color #d4d0cc o #f0dc9c de nuestra paleta (no blanco puro, para diferenciarnos). Fantasma: el modelo al 50 % con tinte #70784c si es válido y #982420 si no. Rejilla de 1 px en las celdas cercanas al cursor (radio de 3 celdas), que se desvanezca hacia fuera. **Radios como contorno sin relleno**, 2 px, mismo color que la selección; el del foco como sector con su ángulo. Aviso de validez de la estación (muro sin puerta, vía cortada) en la esquina inferior derecha, en rojo, con botón «arreglar» si es posible.
- **Bruno**: iconos de la barra de construcción (muro, puerta, foco, torre, sacos) a 32 px con el mismo lenguaje que A1–A7.

---

## 4. GUI: disposición, jerarquía, tipografía y colores

**Disposición (todas las capturas de juego)**
- **Arriba centro**: reloj del día con anillo de progreso, día, hora y cuenta atrás a la siguiente fase («Night in 1:34», en rojo cuando queda poco). Es el elemento más importante: el ciclo día y noche manda.
- **Arriba izquierda**: cola de avisos de escuadra («SQ-8 Reloading!»), en tarjetas negras apiladas.
- **Arriba derecha**: música, velocidad y modo.
- **Abajo izquierda**: recursos en una sola línea con icono y número.
- **Abajo centro**: tarjetas de unidades (roster) con retrato pequeño, nombre corto y barra de estado; en construcción, pestañas de categorías y 4 botones grandes con número de tecla y alcance en metros.
- **Abajo derecha**: órdenes en rejilla con atajo, y minimapa con filtros y orientación de la cámara («VIEW 311° NW»).
- **Barra de atajos contextual** sobre el panel inferior: «Click Place · Drag Aim · Q E Rotate…».

**Jerarquía**: el centro de la pantalla queda libre. Los paneles ocupan aprox. el 12–15 % inferior y una franja fina arriba (est.). Las etiquetas sobre unidades en el mundo son minúsculas (caja blanca con texto corto) y no tapan.

**Tipografía**: sans serif geométrica en negrita para cifras y títulos, con mayúsculas en etiquetas cortas. Tamaños estimados a 1080p: 22–26 px el reloj, 13–15 px el resto, 10–11 px las pistas de teclado.

**Colores**: fondo negro al 75–85 % de opacidad, texto blanco, **un solo acento ámbar** (anillo del reloj, borde del botón seleccionado, pausa) y **rojo solo para peligro**. Verde únicamente en el botón de confirmar. Bordes de 1 px gris claro.

**Comparación con nosotros**: ya decidimos interfaz moderna, plana y oscura con sans serif (v1.4). El HUD de depuración del prototipo es texto suelto arriba a la izquierda, que es normal en esta fase.

**Recomendaciones (inspiración, no calco)**
- Nuestro elemento central arriba no debe ser un calco del reloj: propongo **reloj + horario del próximo tren** («Día 3 · 17:42 · Noche en 1:30 · Tren a Sagunto en 0:45»), porque nuestro ritmo lo marcan la noche *y* el tren.
- Acento propio: **#e08c30** (ámbar de nuestra paleta) para selección y progreso, **#982420** para peligro, fondo **#181c30** al 85 % en vez de negro puro. Así tenemos identidad sin perder el patrón.
- Tarjetas de unidad con los retratos de la fase C y barra de estado de 4 segmentos.
- Barra de atajos contextual siempre visible en modo construcción: es barata y enseña a jugar.
- Responsables: Marcos (estructura UI Toolkit), Bruno (iconos y marcos de tarjeta a 1 px), yo reviso cohesión.

---

## 5. Efectos: fuego, humo y trazadoras

- **Trazadoras**: líneas finas de 1–2 px (est.), rojo anaranjado brillante con bloom, largas, en ráfagas. Desde el aire se leen como **líneas discontinuas rojas** (capturas 1 y 5).
- **Fogonazos y explosiones**: núcleo blanco quemado de gran tamaño con bloom muy amplio (captura 5: la explosión ocupa hasta un 10 % de la pantalla), rodeado de **chispas** como trazos cortos que salen en abanico.
- **Humo**: columnas oscuras marrón negruzco, densas, con borde suave, que **sí** se ven pixeladas (van en la capa del mundo). Polvo claro beige a ras de suelo tras la artillería.
- **Fuego**: puntos naranja muy brillantes con bloom en las zonas de impacto; de noche (cap. 4) los fuegos y fogonazos son las únicas fuentes de color fuera de los focos.
- **Decals**: sangre roja oscura en el asfalto (cap. 1, abajo izquierda) que se acumula donde hay combate. Cuenta la historia del combate sin interfaz.

Esto coincide con nuestro plan de capas (efectos de luz a resolución completa, humo en la capa baja). Lo que falta es **intensidad**.

**Recomendaciones**
- **Marcos**: trazadoras en `VFX_HD` de 1,5 px de grosor, color #e08c30 a #f0dc9c en el núcleo, emisión HDR 4–6 para que el bloom las coja, largo 6–10 m de mundo. Explosión de artillería: destello blanco de 0,1 s con emisión HDR 10+, luego bola naranja de 0,4 s, chispas (20–40 trazos) y humo pixelado que dure 6–10 s. Bloom: umbral 1,0, intensidad 0,8–1,2 y dispersión alta (est., ajustar en caliente).
- **Bruno**: decals de sangre y de quemado en 3 tamaños, que se acumulen; ya entregó decals, comprobar que encajan con este uso.

---

## 6. Cámara y ángulo

- Proyección en perspectiva con **FOV estrecho** (est. 15–25°): parece casi isométrica, las verticales apenas convergen.
- **Inclinación de 50–60° desde la horizontal** (est.) en el juego normal; la captura 4 está casi cenital (70–80°).
- **Rotación libre** (el minimapa marca 311° NW, 46° NE, 272° W): la cámara gira y la brújula lo indica.
- Zoom de 3 niveles claros: cercano (cap. 2, se ven soldados con detalle), medio (cap. 1 y 3) y lejano (cap. 5, se ve toda la base y la horda).

**Nuestro estado**: cámara libre con rotación, inclinación y zoom continuo (v1.9). Bien.

**Recomendaciones (Marcos)**
- Si nuestro FOV es mayor de 30°, bajarlo a **20–25°** y alejar la cámara para compensar: las figuras verticales se leen mejor y el pixelado baila menos al girar.
- **Inclinación por defecto 55°**, límites 40–75°.
- Que la **sombra de la horda siga la dirección del sol, no la de la cámara**: al girar, la sombra ayuda a orientarse.
- Brújula en el minimapa con el rumbo de la cámara.

---

## 7. Prioridades accionables

| # | Quién | Qué | Por qué |
|---|---|---|---|
| 1 | Marcos | Sombra proyectada para todos los zombis, incluida la mancha LOD | Es lo que más diferencia «gente» de «textura» |
| 2 | Marcos | Mancha LOD vertical 2×6 o 3×7, umbral a revisar (12 px) | Recupera la verticalidad |
| 3 | Marcos + Nacho | Separación mínima entre zombis, 30–50 % de suelo visible | Quita el efecto alfombra |
| 4 | Marcos | Un solo valor oscuro para la horda (±8 %) | Quita el ruido de color |
| 5 | Bruno | Lámina de siluetas a 6–20 px con sombra, 3 suelos y 3 horas | Criterio de aprobación |
| 6 | Marcos | Perfiles de gradación con sol bajo, noche más negra | Contraste y ambiente |
| 7 | Marcos | Contorno de selección, fantasma, rejilla y radios sin relleno | Construcción legible |
| 8 | Teo | Zombi cercano alargado con brazos adelante | Pose que dice zombi |
| 9 | Marcos + Bruno | HUD con reloj y tren arriba centro, acento #e08c30 | Identidad propia |
| 10 | Marcos | Intensidad de trazadoras y explosiones | Espectáculo del asedio |

Criterio de éxito para el prototipo de hoy: **una captura a zoom medio, de día, con 10k zombis, donde alguien que no conoce el juego diga «son zombis» sin que se lo expliquemos.** Los puntos 1 a 4 bastan para eso.

— Lucía (Dirección de arte) · [retrato](/mnt/project-files/equipo/retrato_lucia_64_x4.png)
