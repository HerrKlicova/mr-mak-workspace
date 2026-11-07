# Puente del Palancia · zona de emboscada v0 (Álvaro, 7-nov, solo papel)

Plantilla del desmonte (`desmonte-nivel.md`) aplicada al puente del Palancia, el de la línea de la costa justo al este de Sagunto. Plano y sección: `palancia_plano_v0.png`; script: `herramientas/plano_palancia_v0.py`; dato: `mapa_palancia_carreteras_v0.json`. Es para después del MVP: **nada de esto está en el código**.

## 0. Conclusión
**El Palancia no es el puente del §8.3.** El §8.3 (`diseno-colmena-h4.md`) pide un puente de 60–100 m a 12–20 m de altura, con caídas al vacío y la horda entrando en columna por los dos extremos. Las fotos F2 de Paula muestran otra cosa: un **viaducto bajo de vigas de hormigón** (5 vanos de unos 15 m, con el carril a unos 4,5 m sobre el lecho en el modelo v3 de Teo) **sobre una rambla ancha y seca**, con el puente de la carretera paralelo y muy cerca.

Propongo dos tipos de puente:
- **Puente alto** (el §8.3, tal cual): Jiloca y Mijares si las fotos lo confirman.
- **Puente bajo sobre rambla** (este): la horda no llega solo por los extremos, **cruza el lecho, se amontona contra las pilas y sube al tablero por su propia pila de cuerpos** (§5.7). El lecho es un campo de tiro de 75 m de ancho y el tablero es un muro de 4,5 m. Es otra forma de jugar y sale de la foto.

## 1. Dónde está: coordenadas del mundo
Con el mundo persistente (D-N91, D-N96) no hay pantallas, así que la zona se dibuja **en coordenadas del mundo**, justo al este de la de Sagunto: **X 240–496, Z 0–128**. Se solapa 16 m con Sagunto (X 240–256: el final del atasco), y así la emboscada y la estación son el mismo lugar. Todo lo que ya existe se mantiene:
- Viaducto de Teo v3, centrado en **X 302,6**, con estribos en X 262–265,6 y 340,8–344,4 y el **cauce de X 265,6 a 340,8, con el lecho a −4,5 m** (§7d de sagunto-nivel.md).
- Carretera vieja en Z 23 con su propio tablero sobre el mismo cauce, y el **camión cruzado en X 258** a la entrada. El atasco sigue cerrado de X 200 a 344 (§10.4) y el corte K1 está en X 201,5.
- La vía, en Z 64,5. ❓ En la foto hay doble vía con catenaria, y en Sagunto llevamos una dentro del recinto (decidido con Lucía). Para el MVP, una; la segunda es un cambio de Lucía.

## 2. Por qué cada cosa está ahí
| Elemento | Dónde | Por qué existe | Qué hace en el juego |
|---|---|---|---|
| **Cauce seco** (grava, hierba rala, matorral suelto; cañas solo al pie de las orillas, F2_3) | X 265,6–340,8, en toda la Z | El Palancia en Sagunto lleva agua muy pocas veces | Campo de tiro abierto. P2 entra por aquí desde el norte (el pueblo, aguas arriba) y desde el sur (el mar) |
| **Escollera de las orillas** | 3,6 m a cada lado | Defensa contra las avenidas (foto F2_3) | Talud corto. Quien cae del tablero no muere: se queda en el lecho y vuelve a la pila |
| **Pilas del viaducto** | X 280,6 / 295,6 / 310,6 / 325,6 | Vanos de 15 m (Teo v3) | **Donde se amontona la horda.** Cada pila es una rampa de cuerpos posible: cuatro sitios por los que puede subir |
| **Senda del cauce** | X 268–272, de norte a sur | El paseo del río, que pasa por debajo del puente (foto F2_1) | Solo a pie. Por aquí el pelotón baja al lecho desde el estribo oeste, si se atreve |
| **Tablero de la carretera con el atasco** | Z 17–29 | Ya estaba en Sagunto: la gente intentó huir hacia Castellón | **P3: los del atasco.** Salen de los coches a 41 m del tren. Además explica que **los vehículos no puedan cruzar**: la carretera está muerta y no hay otra |
| **Puesto del estribo** (v2 HESCO, yaw 90) | X 244–258,3, Z 78–94,4 | Es el lado propio del río, a 50 m del puesto F3 de Sagunto | Tira sobre el lecho y sobre la cabeza del tren. Desde el estribo oeste se puede desplegar; en el tablero, no (§8.3) |
| **Naranjos** | Al este, en hileras | Huerta de Sagunto hacia Castellón | Ocultan a P1 hasta los últimos 100 m de vía |

## 3. El tren, el tapón y la salida
- El tren va hacia Castellón y **para con la locomotora en X 340, en el estribo este**. El tapón está en X 345–355, al salir del puente: es donde la columna de P1, que viene por la vía, choca con el tren (igual que en el §8.3).
- Con unos 100 m de tren (SIN VERIFICAR), los vagones quedan sobre los cinco vanos y la cola en X 240, en tierra.
- **Salida atrás: hacia Sagunto.** Aquí los 40 m libres no hacen falta como regla, porque detrás está el recinto. Dar marcha atrás es volver a casa.

## 4. Entradas de la horda
- **P1**: por la vía, desde el este (X 496), en columna (§8.3).
- **P2**: por el lecho, desde el norte (Z 128) y el sur (Z 0). Llega a las pilas y sube por su pila de cuerpos.
- **P3**: desde el atasco del tablero de la carretera, a 41 m del tren.
- **No hay entrada por el oeste**: es Sagunto. Encaja con la **O4 de la noche** («la Colmena entra por el puente, por donde no miras», §9.5), que de noche viene por este mismo puente y hace frente en F3. Emboscada y oleada usan el mismo sitio, visto desde los dos lados.

## 5. Vehículos (D-N96)
**Ninguno llega a esta zona en la v0.** La carretera vieja está cerrada en K1 y el tablero de la carretera tiene el atasco. Es coherente y aprieta la lectura del §8.3: «si se acaba la munición, no hay adónde ir». Se abre más adelante con una obra de despeje del atasco (como en H5 §3, la obra es una batalla), y entonces `carretera_vieja_este` pasa a habilitada en el dato.

## 6. Cosas que dependen de otros
- **Nacho**: cuántos cuerpos hacen falta en la pila para subir 4,5 m (§5.7) y que una pila pueda hacerse **contra una pila de puente** y no solo contra un muro. Si no se puede, el tipo «puente bajo» no funciona y vuelvo al §8.3 con el tablero más alto (que contradice la foto).
- **Lucía**: el lecho de noche (grava 94948c con luna 0,45) tiene que dejar la horda en su banda L* 9–13 con contraste. Con muestra.
- **Teo**: nada nuevo. El viaducto v3, el tablero de la carretera, los coches y el puesto v2 ya existen. Solo falta la senda del cauce como franja del mapa de zonas.
- **Paula**: el estribo este y la huerta de detrás (las fotos F2 son desde el oeste).
- **FPS**: el atasco ya se paga en Sagunto. Esta zona suma unos 180 naranjos y 140 matas: hay que medirlo (D-N70).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
