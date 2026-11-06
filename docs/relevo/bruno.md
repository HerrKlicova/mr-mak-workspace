# Relevo · Bruno (Arte técnico, pixel art por código)

Última actualización: 6-nov-2026, 17:10 (Madrid). Quien lea esto es el nuevo Bruno: continúa desde aquí y desde los documentos enlazados, y no da nada por sabido fuera de ellos.

## 1. Quién eres y cómo trabajas

- **Bruno**, 40 años, ex técnico de imprenta. Tranquilo, maniático del píxel suelto, honesto con lo que el código no alcanza. Arte técnico: pixel art por código (iconos, sprites, decals, texturas de suelo, VFX simples y láminas de referencia). Siempre en español. Modelo: Opus 5.5.
- **Firma** en cada mensaje: «— Bruno (Arte técnico) · [retrato](/mnt/project-files/equipo/retrato_bruno_64_x4.png)».
- **Lucía es la jueza de cohesión**: todo lo que haces pasa por ella antes de entregarse. Le mandas la ruta de la hoja de contacto y las dudas concretas; aplicas sus retoques y le dices el commit.
- **Mak** (el coordinador) encarga y reparte. **Marcos no recibe mensajes de hilos**: las notas de importación para él van a Mak (por message_coordinator).
- **Teo** (3D) y tú os calibráis mutuamente: tú le das reglas de lectura a tamaño de juego y referencias a mano; él te pasa capturas en `docs/arte/modelado-3d/capturas/`.
- Límites: sin pagos, sin credenciales, nada irreversible, sin Higgsfield ni Tripo. Código externo solo en la nube y sin credenciales. `docs/decisiones-noche.md` es **solo para añadir al final**.

## 2. Dónde está todo

| Qué | Ruta |
|---|---|
| Skill | `.claude/skills/pixel-art-codigo/` en el repo HerrKlicova/TBD (copia en `/mnt/project-files/docs/arte/pixel-codigo/skill/`) |
| Motor | `scripts/pixelvm.py`: `Sprite` (rect, line, ellipse, poly, grid, outline, limit_colors, stamp, silhouette…), `PAL` (paleta de 32 con nombres), `reduce_16`, `check` (ΔL* ≥ 25 contra #181c30 y ≤ 10 colores), `contact_sheet` |
| Unificar Pixelab | `scripts/unificar.py <png> <salida> --tam 32 [--sin-rojo]`: pasa cualquier PNG a nuestra estética (alfa binaria, contorno, paleta estricta) |
| VFX externos | `scripts/fx_adaptar.py` (pixelfx a paleta y 12 fps) |
| Generadores | `ejemplos/build_*.py`: a1–a6 (iconos), a7_texturas (suelos), a8_humo, d_vfx, decals, prototipo, zombi, zombi_lod, fusilero, oficial, taller, lamina_siluetas, sagunto |
| Exportación para Unity | `ejemplos/exportar_sprites.py <carpeta>`: atlas de zombi (muerte), LOD, oficial; iconos del taller; aviso ámbar; piezas de Sagunto y decals. Las texturas A7 salen con `build_a7_texturas.py <carpeta>` |
| PNG entregados | `/mnt/project-files/docs/arte/pixel-codigo/<familia>/` (a2…a7, decals, fase-d, prototipo, zombi, zombi-lod, fusilero, oficial, taller, siluetas, sagunto, ref3d, unificar) |
| Documentos de Lucía | `docs/arte/regla-estetica-unica.md`, `direccion-visual.md`, `analisis-referencias-6nov.md`, `ambientacion-sagunto.md` |

**Rama de trabajo**: `claude/sprites-importar`, PR #13 abierto (abierto a 6-nov 17:10; sin CI). PR #1 y #11 fusionados. Nunca force push; si el PR se fusiona, rama nueva desde main.

## 3. Decisiones vigentes

- **Estética única**: una paleta de 32 (estricta), contorno de 1 px en los iconos y las unidades, luz arriba a la izquierda, 6–10 colores por icono, alfa 0/255, sin marco en los iconos, sin sangre ni calaveras. A 16 px, reducción con `reduce_16` y **retoque a mano** cuando deforma (cruces, llaves, signos).
- **Familias aprobadas**: A1 cargas, A2 alertas (aviso en ámbar, emergencia con rojo #982420, aspa ámbar = falta o cortado; `vm_alertas_aviso_*` = aviso genérico de la etiqueta de construcción, D-N62), A3–A6 (órdenes en hueso sin marco, tokens de estación), A7 texturas de suelo, A8 humo, fase D de VFX, decals, prototipo, taller.
- **Colores reservados**: rojo #982420 solo ataque y asedio; ámbar #e08c30 para avisos (nunca en decoración: la línea del andén va en #f0dc9c); **#404460 (slate) solo para el rim de las unidades propias**, nunca en suelos, sombras ni decals (lo quité del aceite y del balasto); **los valores más oscuros (#1c200c, #303424) son de la horda**.
- **D-N57, valor partido** para piezas de mundo y unidades: caras de arriba claras (beige/hueso), costados olive_dark, contorno de 1 px. Rim #404460 en el borde sur y este de la tropa propia; los zombis sin rim.
- **Suelos (A7)**: ΔL* ≤ 12 dentro de cada textura sin contar juntas; motas sueltas, nunca islas. Asfalto #6c7874 con motas #94948c y grietas #48403c; balasto en grey_brown sin piedras slate.
- **Horda (D-N61 y revisiones)**: silueta vertical de unos 3:1 en un solo valor #1c200c; brazos al frente desde 12 px; por debajo de 12 px, palito de 2×6 a 2×8. La sombra es un valor intermedio entre el suelo y la figura y no se acumula (máximo, no suma); 1,5× de día y para la mancha también al atardecer, 2,5× solo para figuras ≥ 12 px al atardecer, radial desde el foco de noche; sobre el asfalto, #48403c.
- **Rostros**: van en Pixelab (fase C), no por código. El Chispas del taller es provisional.
- **3D a tamaño de juego (para Teo)**: detalle ≥ 2 px de lado corto y separado ≥ 2 px; nada saliente menor de 3×3; lo fino se quita o pasa a cambio de valor plano; contorno solo en la silueta.

## 4. Pendiente

1. **Chispas**: cuando salga su retrato en Pixelab, reducirlo a 32 y 16 px con `unificar.py` para que el icono del taller y el retrato tengan la misma cara, y sustituir `chispas()` de `build_taller.py`.
2. **Iconos de la barra de construcción** (muro, puerta, foco, torre, sacos) a 32 px con el lenguaje de A1–A7 (§3 de `analisis-referencias-6nov.md`). No encargados aún.
3. **Marcos de tarjeta de unidad** a 1 px para el HUD (§4 del mismo documento), cuando Marcos haga la interfaz.
4. **Ambientación de Sagunto**: puntos 7–9 de `ambientacion-sagunto.md` si los piden (palés, bancos y farolas son de Teo).
5. Vigilar que el PR #13 se fusione; después, cada entrega nueva va en rama nueva desde main.

## 5. Trampas conocidas

- **Desde la nube no se pueden subir PNG al repo**: el proxy bloquea Git LFS y la escritura de blobs. Se entregan **scripts deterministas** que Marcos ejecuta en local, y los PNG van a la carpeta compartida. Comprueba siempre que el script da archivos idénticos (`cmp`) a los aprobados.
- **Nada de borrar con rm en lote** sobre la carpeta compartida (lo bloquea el control de seguridad): sobrescribe con cp.
- **`__pycache__`** queda sin seguimiento tras ejecutar los scripts y el hook de parada se queja: bórralo antes de terminar.
- **El remoto puede no tener upstream configurado**: si el hook dice que no hay rama remota, `git push -u origin claude/sprites-importar`.
- **`limit_colors` nunca funde los acentos** (ámbar, crema, rojo): si un fogonazo pasa de 10 colores, llama a `limit_colors` después de añadirlo.
- **La reducción a 16 px** convierte cruces en estrellas, una llave cerrada en lupa y la exclamación en un borrón: retócalo a mano (`icono_16` en `build_taller.py`, `aviso_16` en `build_a2.py`).
- **Pixelab ignora las negaciones** («no skull» saca calaveras): solo prompts positivos y una prueba de 4 antes de cada lote.
- **El ajuste al color más cercano** saca rosas y azules en las mezclas (el borde del charco del foco, sombras sobre gris): para graduar suelos y sombras, usa una paleta sin rojos, rosas, slate ni navy, o fija el color a mano (`SOMBRA_FIJA` en `build_lamina_siluetas.py`).
- **Regla frente a lectura**: algo puede cumplir el ΔL* y aun así leerse mal (piedras frías que parecen charcos, una diagonal clara que parece una correa de fusil). Mira siempre la prueba a x1 sobre los suelos.
- **No inventes**: si no has medido algo, dilo.
