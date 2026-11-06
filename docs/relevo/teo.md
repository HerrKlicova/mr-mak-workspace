# Relevo · Teo (Modelado 3D)

Última actualización: 6-nov-2026, 17:35 (Madrid). Si eres el nuevo Teo, sigue desde aquí y desde lo que se enlaza. No des nada por sabido fuera de este documento.

## 1. Quién eres y cómo trabajas

- **Teo**, modelador 3D de «Vía Muerta» (el RTS zombi ferroviario de Eugenio). Tu trabajo: modelos 3D con bloques por código (y Hunyuan3D-2mv con 4 vistas cuando hace falta), el repaso en Blender, la verificación y la entrega a Unity. Siempre en español.
- **Firma** en cada mensaje: «— Teo · [retrato](/mnt/project-files/equipo/retrato_teo_64_x4.png)».
- **Lucía** (Diseño) revisa y aprueba cada modelo: es la jueza de cohesión. **Bruno** (pixel art) da consejo de píxel. **Paula** busca las fotos reales. **Marcos** importa los modelos en Unity, pero **no recibe mensajes de hilos**: todo lo que es para él va por el coordinador (Mak).
- **Límites**: nada de pagos ni credenciales, nada irreversible, ni Tripo ni Higgsfield. Lee el código descargado antes de ejecutarlo. Lo que tenga que ejecutarse en el PC de Eugenio se pide. No inventes medidas: marca **SIN VERIFICAR** lo que no tenga fuente.
- Eugenio aprueba por defecto lo que recomienda el equipo. Le llegan las capturas por la **galería** (hilo «Enseñar capturas de la noche y el tren»): se le pasan allí las rutas y Mak le avisa con un enlace.

## 2. Herramienta (skill `modelado-3d`)

| Qué | Dónde |
|---|---|
| Skill y documentación | repo TBD, `.claude/skills/modelado-3d/` (SKILL.md). PR #10, rama `claude/modelado-3d-skill`. |
| Copia de los scripts | `/mnt/project-files/docs/arte/modelado-3d/scripts/` (la nube) y `C:\Dev\mr-mak-workspace\herramientas\modelado-3d\` (el PC) |
| `malla3d.py` | importar, limpiar, vóxeles, diezmar, paleta de 32, `valor_partido`, `paleta_por_piezas`, auditar, legibilidad ΔL*, vistas y FBX |
| `entregar.py` | LOD0 + LOD1 + captura junto a la foto en un solo paso. Uso: `TBD_VARIANTE=n python3 entregar.py <bloque> <salida> --fotos <img[:recorte]>... --titulo ... --python_bpy /tmp/claude-0/bvenv/bin/python` |
| `bloques/taller.py` | primitivas: `caja` (rot_x/rot_y/rot_z, inclinar, cuña), `cilindro`, `esfera` (icosfera), `perfil_extruido`, `tejado` (1, 2 o 4 aguas), `costuras`; `t.fino(lod)` añade piezas solo al LOD0 |
| Bloques | `bloques/*.py`: dragon_v5, locomotora_r1, vagon_tropa_r2, vamtac_v2, zombi_cercano (grueso), zombi_fino, edificio_viajeros, marquesina, poste_catenaria, casa_baja, bloque_pisos, naranjo |

Atributos que `entregar.py` lee de un bloque: `PIEZAS`, `COLORES`, `COLORES_LOD1`, `VALOR_PIEZAS` (claro, costado[, abajo]), `FACCION`, `PRESUPUESTO` {lod: (mín, máx) triángulos}, `UMBRAL_CONTORNO`, `LEGIBILIDAD="cuerpo_medio"` (zombis). La variable `TBD_VARIANTE` elige la variante y nombra la salida `SM_<bloque>_vN_LODn`. `TBD_ZOMBI_CAMISA` fija la camisa del zombi.

## 3. Decisiones vigentes

- **Escala real** en metros para todo, también el tren (locomotora R1 de 24 m, R2 de 19,9 m, ancho ibérico de 1668 mm).
- **Ejes**: delante es −Y en Blender, que en Unity sale como **+Z** (lo midió Marcos). Z arriba.
- **Paleta de 32** (`referencias/paleta_32.hex`). Prohibidos en objetos: la familia roja y el ámbar e08c30 (solo la franja frontal del tren, D-N42, con `permitir=`). El 404460 es solo para el rim de las unidades propias.
- **D-N57, valor partido**: arriba claro (b4a080 por defecto) y costados oscuros (50541c militar, 605c48 civil), con contorno de 1 px. Se aprueba si ΔL* = máx(20 % más claro − suelo, contorno − suelo) ≥ 25. **Excepciones**: los zombis van todo oscuros (paleta de la Colmena 303424, 283440 y 442c0c; se mide el cuerpo medio contra el suelo); los pisos abiertos son interiores oscuros (R2: 605c48).
- **Reglas de color de Lucía**: nada de filos claros b8b8b8 en vehículos largos (se confunden con el contorno de selección). El decorado nunca va en los valores de la horda (1c200c, 303424): por eso la sombra de la copa del naranjo es 50541c.
- **LOD**: el juego carga **siempre el LOD1**. LOD1 solo con piezas de 0,4 m o más, contorno interior 0,25 y sin costuras. Las costuras y los detalles finos, solo en el LOD0 y en la familia de tono del panel.
- **Regla de píxel de Bruno**: 0,17 m/px; ningún detalle de menos de 2 px en el LOD1.
- **Norma de Eugenio (todos los modelos)**: detallar y texturizar desde las **fotos reales de Paula** (`C:\Dev\mr-mak-workspace\referencias-reales\`), con las ruedas de goma oscura separadas del casco, y entregar con la captura junto a la foto real. Sin foto, la columna dice «foto pendiente» y las medidas quedan SIN VERIFICAR.
- **Variedad (Eugenio, 16:58)**: cada estructura con al menos 5 variantes; los zombis son personas, con ropa y cosas. Para Lucía, a 20 px solo se nota la variedad de silueta, no la de color.
- **Suelos del banco**: trinchera, fondo de trinchera 6e6a5a, llano 845c28 y Sagunto c19e78.

## 4. Estado de las entregas (todo en el PC, en `herramientas\modelado-3d\`)

| Modelo | Estado |
|---|---|
| Dragón v5 (`dragon\v5\`, LOD1 v7) | Aprobado |
| R1 locomotora, R2 vagón de tropa v3 | Aprobados. Las cotas de la Rgs, SIN VERIFICAR (solo están comprobados el ancho de 1668 y la batalla de 2,0 m) |
| VAMTAC V2 | Enviado a Lucía |
| Zombi fino (`zombi_fino\camisa_*`) | Aprobado, sustituye al grueso |
| Zombi, variantes v1–v7 (`zombi_fino\variantes\`) | Aprobadas por Lucía (17:10): mochila, gorra, chaqueta abierta, falda, brazo caído, corpulento y bajo de 1,63 m. Marcos añade una escala de ±5 % por instancia. Nada de niños |
| Sagunto: edificio de viajeros, marquesina, poste de catenaria (`sagunto\<pieza>\`) | Aprobados con medidas típicas SIN VERIFICAR |
| Sagunto: casa baja y bloque de pisos, v1–v5 | Aprobados |
| Naranjo v2 (base y v1–v5) | Rehecho porque Eugenio veía «una piedra» y aprobado por Lucía (17:10). Las naranjas se quedan en a86c50: e08c30 en cientos de árboles parecerían avisos. Medidas SIN VERIFICAR: Paula prepara `E10_naranjo_*` |

Las capturas están en `/mnt/project-files/docs/arte/modelado-3d/capturas/` y los FBX de la nube en `/mnt/project-files/docs/arte/modelado-3d/<modelo>/`.

## 5. Pendiente

1. Las fotos de naranjos de Paula (`referencias-reales\ambientacion\E10_naranjo_*.jpg` y `E10_naranjo_medidas.md`): comparar el naranjo v2 con ellas y volver a entregarlo con `--fotos`.
2. Las fotos de Paula de la estación (E1–E3, en `referencias-reales\ambientacion\`): ajustar el edificio, la marquesina y el poste, y volver a pasar `entregar.py` con `--fotos`. También las de naranjos y casas, que ya están pedidas.
3. Las 5 variantes del edificio de viajeros, la marquesina y el poste de catenaria.
4. Las piezas 7 y 8 de Sagunto (aguada o almacén, y señales) si las piden. Las cotas de la Rgs, si Paula encuentra una fuente.

## 6. Trampas conocidas

- **Aristas no manifold**: dos cajas con esquinas o aristas que coinciden se funden en `limpiar` y dejan aristas sueltas. Acorta una de las dos o haz que se crucen; en cilindros apilados, solápalos con radios distintos. Las icosferas que se cruzan no dan problemas.
- **Sin PIL dentro de bpy** (`/tmp/claude-0/bvenv/bin/python`): las medidas de imagen (cuerpo medio, láminas) se hacen en el proceso principal con el `python3` del sistema.
- **El montaje de red** `/mnt/project-files`: copia a un nombre temporal y luego `mv -f`. Para borrar con `rm`, usa rutas literales (la comprobación de seguridad bloquea `rm` con variables).
- **No subas PNG al repo**: van por LFS y el proxy rechaza subir LFS. Los PNG van a `/mnt/project-files`.
- El proxy de la nube **no llega a Wikimedia** (403): las fotos las pone Paula.
- **MCP de Blender en el PC**: corta a los 60 s, así que haz una pieza por llamada. Sin `time.sleep`. Guarda y restaura `scene.img3d` (lo usa otro hilo). `*_for_cli` falla. Cuida la RAM del PC de Eugenio: si Mak pide pausa, nada local.
- **Hunyuan 2mv** con vistas lisas funde las ruedas, ondula la chapa y gira la malla 180°; por eso casi todo se hace por bloques. La licencia excluye la UE, pero Eugenio lo aceptó (`docs/herramientas-ia.md`). No vuelvas a preguntarlo.
- **`device_commit_files`**: admite como máximo 50 archivos por llamada.
- **El LOD0 no lo ve el jugador**: lo que tiene que leerse en el juego (naranjas, visor y similares) debe estar en el LOD1.
