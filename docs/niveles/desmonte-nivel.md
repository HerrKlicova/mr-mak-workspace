# Desmonte · diseño de la zona v0 (Álvaro, 7-nov, solo papel)

Zona de emboscada de **256 × 128 m** (D-N38, `diseno-colmena-h4.md` §8.1). La vía va a lo largo de X, centrada en Z 64. El tren entra por X 0 y sale por X 256. Aquí uso **(X; Z)** como en Sagunto: la «Y» del §8.1 es la Z del juego. Plano y sección: `desmonte_plano_v0.png`; script: `herramientas/plano_desmonte_v0.py`; dato: `mapa_desmonte_carreteras_v0.json`. **Nada de esto está en el código**: es para después del MVP y no se toca hasta que la noche de Sagunto se pueda ganar (P0).

## 0. Conclusión
El desmonte del §8.1 se juega bien (GIF de las 02:54) pero **su geometría no cuadra**, y no cuenta por qué hay una trinchera, por qué para el tren ni por qué quedan libres los 40 m de atrás. Propongo mantener lo que funciona (7 m de hondo, taludes de 35–45°, tapón en X 175–185, la ratonera) y darle una historia: **la vía única de la línea de Teruel cruza una loma de olivar abandonado**. Al sur, la trinchera se abrió en roca y al norte en tierra. La cruza un camino agrícola por un paso superior, y detrás del tren hay un terraplén sobre una rambla seca.

## 1. Lo que no cuadra en el §8.1
- **Taludes**: con 16 m de fondo, 7 m de hondo y bordes en Z 34 y 94, cada talud ocupa 22 m en horizontal para bajar 7 m. Eso son **17,6°**, no 35–45°. Con eso la horda no rueda: baja andando. Es una cuenta, no una medida.
- **Fondo de 16 m** para una sola vía: la plataforma de vía única con sus dos cunetas mide del orden de 11–12 m (SIN VERIFICAR con la norma de Adif; es el orden de magnitud).
- Ni los 40 m libres ni el sitio del tapón tienen una razón en el terreno: son reglas del juego sin un lugar que las cuente.

## 2. Geometría propuesta
- **Fondo**: 12 m, de Z 58 a 70, con cunetas de 1,5 m a cada lado y la vía en 64.
- **Hondo**: 7 m entre X 80 y 180. Los emboquilles van en rampa: de 0 a 7 m entre X 60 y 80, y de 7 a 0 m entre X 180 y 200, que es como empieza y acaba una trinchera de verdad.
- **Talud sur, en roca, a 45°** (1:1): borde en **Z 51**. Lleva **malla de triple torsión** colgada, la de casi todos los desmontes de Adif. Aquí la horda **se despeña**: cae sin rodar y golpea el fondo.
- **Talud norte, en tierra, a 35°** (1:1,43): borde en **Z 80**. Lleva surcos de erosión y algún matorral. Aquí la horda **rueda**. Las dos caídas del §5.7 quedan cada una en su sitio, y el jugador sabe de dónde viene cada tipo.
- Las dos inclinaciones caen dentro de los 35–45° de la D-N38. ❓ Nacho tiene que confirmar que la física de caídas acepta un talud distinto a cada lado.
- **Bordes**: vallado de Adif (malla de 2 m) a 1,5 m del borde en los dos lados, y **cuneta de coronación** en el norte (la tierra necesita desviar el agua). De noche dibujan una línea continua que dice «aquí empieza la caída». Era la nota 1 de la revisión del GIF: que el talud se lea.
- El suelo de arriba, de Z 0 a 51 y de Z 80 a 128, es **la loma**: la trinchera existe porque la vía no podía subirla.

## 3. Por qué cada cosa está ahí
| Elemento | Dónde | Por qué existe | Qué hace en el juego |
|---|---|---|---|
| **Loma con olivar y almendro abandonados**, en bancales de piedra seca de 0,8 m | Norte, Z 85–128; bancales en Z 96 y Z 110 | Secano del Alto Palancia. La vía la corta | D1 baja de aquí. Los bancales son muro bajo si se sube la tropa (es arriesgado, pero domina el talud) |
| **Matorral** (coscoja, romero y lentisco; foto H3 de Paula) | Sur, Z 0–48 | Ladera de roca, sin cultivo | D2 llega al borde de roca y se despeña. Cobertura ligera |
| **Camino del Mas y paso superior** | X 117–123, de Z 0 a 128; tablero de Z 48 a 83 (vano de 35 m, pretil de 1,1 m, a +8 m) | Al abrir la trinchera se cortó un camino agrícola, y Renfe/Adif tuvo que reponerlo con un puente | **El único acceso de los vehículos de tierra** (D-N96). Desde el tablero se dispara hacia abajo. La horda de D4 se amontona en el puente y cae sobre los vagones: el plano espectacular, a 50 m detrás de la locomotora |
| **Camino de servicio de Adif** (tierra, 4 m) | Borde norte, Z 86–90, de X 62 a 200 | Mantenimiento del talud de tierra, que es el que se mueve | Habilitado. Lleva a los vehículos por lo alto hasta el puesto de obra |
| **Terraplén de 3 m y pontón de 12 m sobre una rambla seca** | X 0–60; pontón en X 20–36; rambla de 5 m de hondo | Antes de la loma, la vía cruza una rambla | **Por esto quedan libres los 40 m de atrás**: a la vía solo se llega por la trinchera, porque la rambla corta el paso por los lados. Los que caen a la rambla quedan fuera |
| **Tapón** | X 175–185 | Cuando el tren entra, la horda que viene por la vía (D3) choca con la que cae de los taludes justo a la salida de la trinchera, donde el fondo se estrecha entre la roca y la tierra | Igual que en el §8.1 |
| **Derrumbe** (solo con corte, memoria ≥ 850) | Talud sur, X 176–190: bloques sobre la vía | La roca es la que se desprende, y la malla está ahí por eso | Hace falta el tren de obras. La obra es la batalla del H5 §3 |
| **Puesto de obra** (v2 HESCO, yaw 180) | X 176–191, Z 88–103, sobre el camino de servicio | Lo monta el jugador para proteger a los obreros | Ve el derrumbe desde arriba. Es un frente del mundo persistente mientras dura la obra |
| **Postes de comunicaciones** (sin catenaria) | Lado sur, cada 50 m | La línea Sagunto–Teruel es de vía única y sin electrificar (SIN VERIFICAR con Paula) | Siluetas verticales que marcan la vía de noche |

## 4. Entradas de la horda
- **D1**: el olivar del norte, de X 90 a 200, entra por Z 128 y baja rodando por el talud de tierra.
- **D2**: el matorral del sur, de X 80 a 180, entra por Z 0 y se despeña por la roca.
- **D3**: por la vía, de frente, de X 230 a 256 (igual que en el §8.1).
- **D4**: por el camino del Mas, desde los dos extremos. Se amontona en el puente y cae al tren.
- **Detrás (X 0–40)**: nada. Es la salida de emergencia.

## 5. Luz (noche, luna 0,45)
No hay luz eléctrica: solo la luna, los focos del tren y los de los vehículos. La lectura depende del valor del talud (el perfil aprobado de la D-N42: arriba 65–69, taludes 48–51 y fondo 38–42), de la línea del vallado y de la cuneta de coronación. La roca con malla tiene que quedar más clara que la tierra, para que se lean las dos caídas. Eso lo valida Lucía con muestra.

## 6. Piezas y fotos que harían falta (para Teo y Paula, cuando toque)
- **Teo** (5 variantes cada una): paso superior (vigas de hormigón, arco de fábrica, tablero metálico, losa con pretil de malla y losa con barrera de hormigón), pontón, vallado de Adif, malla de triple torsión como decal sobre el talud, bancal de piedra seca, poste de comunicaciones, hito kilométrico y bloques de derrumbe.
- **Paula**: desmontes de Adif con malla de triple torsión, un paso superior de camino sobre trinchera, el vallado de Adif y la línea Sagunto–Teruel por el Alto Palancia (para confirmar que es de vía única y sin catenaria).
- **FPS**: unas 260 piezas (≈140 árboles, ≈110 matas, el puente, el pontón y la valla en tramos). Hay que medirlo antes de darlo por bueno (D-N70).

## 7. Pendiente
- Nacho: un talud distinto a cada lado en la física de caídas, y el sitio «obra» en el dato.
- Lucía: el valor de la roca frente a la tierra de noche, con muestra.
- Mak: si el desmonte v0 vale como plantilla para el puente y Nules.

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
