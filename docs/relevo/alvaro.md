# Relevo · Álvaro (Diseño de niveles)

Última actualización: 8-nov-2026, ~10:00 UTC, escrito por el hilo «Álvaro · Diseño de niveles (2)» (cmsg_014mgaTqwTDTmezhB3g3Rs8BM5EpVTHfG6CbN79pLL7PE4) para el hilo (3). Si eres el nuevo Álvaro, empieza aquí. Este archivo sustituye al de 6/7-nov (copia del anterior en el registro de abajo) y a `docs/relevos/alvaro-2026-11-07.md`, que ya no se mantiene.

## 1. Personaje
- **Álvaro**, diseñador de niveles, 44 años, ex urbanista de ADIF. Fichado el 6-nov porque Eugenio preguntó «¿es normal que la vía esté cortada?» y pidió un nivel que «tenga sentido, sea realista y se sienta vivo».
- Regla de la casa: **cada vía, calle y muro tiene que tener una razón de existir.** Si no sabes contar por qué algo está ahí, sobra o está mal puesto. El espacio cuenta la historia (el atasco tiene una cabeza, el corte se ve, el carril abierto lo abrió alguien).
- Firma: «— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)».

## 2. Tono
- Español, frases completas. Coordenadas (X; Y; Z) o (X; Z) en metros, yaw en grados, archivo:línea para código.
- Conclusión primero y luego el porqué; se recomienda una opción, sin listas de preguntas.
- Lo no verificado se marca **SIN VERIFICAR**; lo que no se ve sin Unity, con ❓. ETA y medidas calculadas se dicen como cuentas.
- Formato de actualización en el hilo: [HILO] [ESTADO] [qué cambió] [preguntas para Eugenio].

## 3. Normas vigentes
- Todo en español. Sin pagos, sin credenciales, nada irreversible. No inventar. Mak (coordinador) decide; el equipo no consulta a Eugenio.
- Lucía tiene la última palabra en cohesión y color, y es la única que asigna D-N (siguiente libre: **D-N164**). `docs/decisiones-noche.md` solo admite añadir al final; reléelo 10 s después de escribir.
- **Marcos e Iker no reciben mensajes de hilos**: todo lo suyo va por Mak o por push a mr-mak-workspace.
- A Eugenio solo con enlaces a la galería, nunca rutas. Cambios visuales grandes, primero como muestra, con al menos 5 variantes por estructura. Las muestras van a Galería marcadas «muestra, no build».
- Paleta de 32 colores. **Nada rojo ni ámbar** en el suelo ni en lo propio (982420/e08c30 solo en la interfaz de ataque o brecha). Luces crema f0dc9c, selección d4d0cc, línea central b8b8b8. Banda L* 9–13 reservada a la horda (D-N80).
- Ninguna pieza trae losa de suelo propia (salvo el helipuerto); el suelo lo pone el mapa de zonas.
- Mundo persistente (D-N91/D-N96): varios frentes, ETA (fórmula D-N120) y vehículos de tierra solo por carreteras del dato `mapa_*_carreteras*.json`. Lo que dice el dato tiene que verse en el suelo.
- Regla de 60 m (D-N44), medida desde el andén (punto más cercano), acordada con Hugo. Pila de cuerpos: StepUp = altura del obstáculo −0,6 m, 0,35 m por capa.
- Pieza nueva, medida en FPS antes de darla por buena (D-N70).
- Repos: mr-mak-workspace (rama main) con Co-Authored-By y Claude-Session en cada commit, y antes del push `git config lfs.https://github.com/HerrKlicova/mr-mak-workspace.git/info/lfs.locksverify false`; si el push falla por ir detrás, `git pull --rebase origin main`. HerrKlicova/TBD solo se lee.
- **Trampa**: nada de `grep -r` sobre `/mnt/project-files` (montaje de red). Busca en archivos concretos. Scripts con `python3 -I`.

## 4. Estado (8-nov, 10:00)
### Sagunto
- `docs/niveles/sagunto-nivel.md` v1.3 aprobada por Mak (7-nov). §10.8: F4 sigue al tren (Nacho lo mete en Transporte.cs), puerta oeste-sur en (69; 0; 53) yaw 90, VAMTAC en X 110 y 118, accesos oeste y sur en `mapa_sagunto_carreteras_v1_3.json` (acceso_oeste [[99,53],[59,53]], acceso_sur [[99,53],[99,23]]), caseta del paso a nivel cambiada por armario de Adif. ETA de Nacho: F2 25 s (a pie 37 s), F3 30 s, su puesto 32 s. Plano `sagunto_plano_v1_3.png` (script `herramientas/plano_v1_3.py`).
- Frentes: F1 estación (112; 78), F2 paso a nivel (59; 62) con puesto v2 en (43; 0; 82) yaw 90, F3 helipuerto v4 (180; 0; 44) con puesto v2 en (207; 0; 51) yaw 270 y rearme X 159-164 × Z 31-41, F4 tren móvil. Cortes K1 (201,5; 23) y K2 (59; 86), 14 balizas.
- **Siguiente tarea de Mak**: revisar el §10.6 (y §10.7/10.8) contra la **Noche57**, que sale hacia las 13:30 del 8-nov, **a partir de sus capturas en la galería** (https://claude.ai/artifact/XctYKKrtjAkKe57N7grxre). La Noche23 queda obsoleta, no la revises.

### Otras estaciones (petición de Eugenio del 7-nov: entrar en cada estación reclamada, llevar trenes, reutilizar el kit de Sagunto de otra manera)
- Desmonte v0 (`desmonte-nivel.md`, plano y `mapa_desmonte_carreteras_v0.json`): aprobado por Mak como plantilla. Fondo de 12 m a 7 m de profundidad, talud sur de roca 45° (borde Z 51) y norte de tierra 35° (borde Z 80), paso superior en X 120.
- Puente del Palancia v0 (`palancia-nivel.md`): tipo «puente bajo sobre rambla», con estribos macizos en X 262–265,6 y 340,8–344,4 (§0b).
- Nules v0 (`nules-nivel.md`): recinto §2b X 108–152 × Z 56–87, 150 m (132 de HESCO + 18 de puertas), 127,2 u; caseta de compuertas en (200; 0; 17,5).
- Castellón v0 (`castellon-nivel.md`, plano, `mapa_castellon_carreteras_v0.json` y `docs/estaciones/castellon.json` con piezas, paradas de asalto y orden de liberación). Elegida porque es día 1, única fuente de combustible y objetivo de la Colmena el día 7. Recinto [[64,4],[212,4],[222,14],[222,90],[64,90]]; naves en X 68–136, Z 6–22; vías muertas en Z 12/17/22; módulos del kit en yaw 180 a Z 81,5. Una sola vía dentro de los recintos (precedente de Sagunto).
- Importador de Iker: puntos [x,z] o [x,y,z]; la variante explícita solo se respeta en kit_cuerpo, kit_remate y torreta; la cisterna la gira 90° en código.
- Ninguna de estas tiene todavía build revisada; las aprobaciones de Lucía de Palancia, Nules y Castellón: SIN VERIFICAR, compruébalo en su hilo o en decisiones-noche.md.

### Estados del muro (D-N163 §1, Lucía (3), 8-nov)
- Muestra entregada el 8-nov ~09:50: `docs/niveles/muestras/muestra_estados_muro.png` (script `herramientas/muestra_estados_muro.py`, commit e0bf2f9). Alzado a 1 m = 14 px. Sacos (tramo de 8 m, 1,2 m de alto), HESCO (módulo de 10 m, 2,1 m, D-N59) y puerta de vehículos (8 m, dos hojas, D-N111), cada uno con 5 variantes × 4 estados: sano ≥70 %, dañado 30–70 %, muy dañado 1–30 %, brecha 0 (escombro, no bloquea).
  - Sacos: v0 hiladas rectas, v1 en talud, v2 mezclados, v3 con tablón, v4 con red.
  - HESCO: v0 malla limpia, v1 geotextil a la vista, v2 doble escalonado, v3 remate de sacos, v4 red de camuflaje.
  - Puerta: v0 tubo y chapa, v1 chapa ondulada, v2 tablones y flejes, v3 malla con espino, v4 blindada con pórtico.
  - Paleta: saco 88885c, relleno b4a080, HESCO 70784c/50541c, malla b8b8b8, suelo c4ac84, chapa 94948c, madera a86c50.
- **Pendiente de Lucía**: aprobarla y decidir si el tramo de sacos es de 8 m (dos módulos de 4 m de Teo, lo que yo propongo) o de 10 m como dice D-N163. Los muro_sacos v0–v4 de Teo (aprobados 04:45) son estados de la variante v0; las otras 4 variantes son nuevas. Teo modela solo tras la aprobación. Avisados Lucía, Teo, Galería y Mak.

## 5. Pendientes, por orden
1. Noche57 (~13:30): capturas en la galería contra §10.6–10.8 de sagunto-nivel.md. Informe a Mak con lo hecho, lo que falta y lo que no se ve en captura (❓).
2. Respuesta de Lucía a la muestra del muro; si cambia el tramo a 10 m, regenerar la muestra.
3. Nivel 2 de Sagunto (512 × 256 m, §9.4, `sagunto_plano_v2_boceto.png`): en P2, pendiente de FPS.
4. Siguientes estaciones con la misma plantilla cuando Mak lo pida.

## 6. Hilos útiles
- Lucía (Diseño): cmsg_014mgaTqwTDTmezhB3g3Rs8BSZDYcz7acLVfZhyx8TSa9Z
- Teo (modelado): cmsg_014mgaTqwTDTmezhB3g3Rs8BQBMQ2t9Dd6zTKHvAJDPgmp
- Galería: cmsg_014mgaTqwTDTmezhB3g3Rs8BF41b4Axbvz2cmCkE5RzXUu
- Hugo (economía): cmsg_014mgaTqwTDTmezhB3g3Rs8BWGk2rnnayJGk4VrTFCj9Y2 (ojo: la puerta de vía cuesta 8 u, no 6)
- Nacho (simulación): cmsg_014mgaTqwTDTmezhB3g3Rs8BC2ZTPxQjU4PPAPBWqWE7Qa
- Un hilo no puede mandarse mensajes a sí mismo; los ids de los demás salen de list_threads.

## 7. Rutas
- Documentos, planos y datos: `/mnt/project-files/docs/niveles/` (copia en mr-mak-workspace `docs/niveles/`). Scripts en `docs/niveles/herramientas/`.
- Zonas de Sagunto: `sagunto_zonas_1m.png` (1 m/px, X −250..506, Z −200..480, ids 0–11), `sagunto_sin_vegetacion_1m.png`, `zonas.py`.
- Juego (TBD, solo lectura): `Assets/TBD/Scripts/View/PrototypeBootstrap.cs`, `View/PrototypeBootstrap.Vehicles.cs`, `Sim/SimTypes.cs`, `Units/Transporte.cs` (RoadMap, ETA), `StreamingAssets/Noche/mapa_sagunto_carreteras.json`.
- Modelos de Teo: `/mnt/project-files/docs/arte/modelado-3d/`. Para medir un FBX binario, rehacer un lector de unas 40 líneas de los nodos «Vertices».
- Fotos de Paula: `/mnt/project-files/referencias-reales/`.

## 8. Registro antiguo (resumen del 6–7 nov)
- 6-nov: v1.1 de Sagunto aprobada por Lucía; correcciones C1–C9 a Marcos; vía cortada (`PrototypeBootstrap.cs:1624-1628`) arreglada en P1. Suelo por zonas aprobado por Eugenio para todo Sagunto (20:25), castillo fuera de cámara en (39,25; 361,25). 23:55: «se siente todo muy pequeño» → §9 (nivel 1 E1–E6, nivel 2 en P2).
- 7-nov 07:44: v1.2 aprobada por Mak con helipuerto v4 (§10). 7-nov ~09:00: v1.3 aprobada (§10.8). Después, desmonte, Palancia, Nules y Castellón v0.
- 8-nov: muestra de estados del muro (D-N163 §1).

— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)
