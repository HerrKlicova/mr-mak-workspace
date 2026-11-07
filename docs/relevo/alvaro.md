# Relevo · Álvaro (Diseño de niveles)

Última actualización: 6-nov-2026, 18:35 (Madrid). Si eres el nuevo Álvaro, empieza aquí.

## 1. Quién eres
- **Álvaro**, diseñador de niveles, 44 años, ex urbanista de ADIF. Cada vía, calle y muro tiene que tener una razón de existir; cuentas historias con el espacio. Fichado el 6-nov a petición de Eugenio. Siempre en español.
- Firma: «— Álvaro (Niveles) · [retrato](/mnt/project-files/equipo/retrato_alvaro_64_x4.png)».
- **Lucía** (Diseño) tiene la última palabra en cohesión. **Teo** hace los modelos. **Paula**, las fotos. **Bruno**, los decales. **Marcos** integra en Unity pero **no recibe mensajes de hilos**: lo suyo va por Mak (coordinador).

## 2. Estado
- Hilo: «Álvaro · Diseño de niveles» (cmsg_014mgaTqwTDTmezhB3g3Rs8B7enPzJo8dEESiziswpJAm1).
- Entregado: `docs/niveles/sagunto-nivel.md` (v1.1, APROBADO por Lucía 18:27 con correcciones de color: asfalto 6c7874, hollín 303424/48403c, pintadas d4d0cc, humo lejano sobre Valencia, ambulancia sin cruz roja) y `docs/niveles/sagunto_plano_v1.png`. Pendiente de que Marcos haga P1-P3 y de los modelos de Teo.
- Build 8e567cc de Marcos revisada: correcciones C1-C9 en §7 del documento. Remates de Teo (paso superior y puente) movidos al faldón (X = −20 y X = 280, §7b). Pendiente: siguiente build de Marcos.

## 3. Hallazgos y decisiones vigentes
- **La vía cortada es un fallo**: `PrototypeBootstrap.cs:1624-1628` dibuja los raíles de X 10 a 100 (resto del fuerte de 31 m). El fuerte va de 70 a 156. Arreglo P1: todo el ancho, como el desmonte.
- **El bloque de pisos (172; 70) está encima de la vía** (Z 63-77, vía en 64,5). P2: moverlo a (174; 82).
- **El muro este está cerrado**; propuesta: puerta de vía este solo visual en el MVP.
- Suelo de 256 × 128 m: al alejar se ve el vacío. P3: faldón decorativo.
- Convención de ficción: oeste de la zona = Valencia; este = Castellón y la bifurcación de Teruel; norte = pueblo y castillo; sur = huerta, Puerto y mar. Es convención de juego, no cartografía verificada.

## 4. Rutas
- Código del juego: repo HerrKlicova/TBD (público; se puede clonar en la nube). `Assets/TBD/Scripts/View/PrototypeBootstrap.cs` (`BuildSaguntoAmbience`, construcción del nivel), `Assets/TBD/Scripts/Sim/SimTypes.cs` (`Level`, `CuttingLevel`), `Sim/SimWorldSetup.cs` (aparición de la horda).
- Fotos de ambientación de Paula: catálogo en `docs/arte/referencias/catalogo.md` (E1-E10); las 32 imágenes ya están copiadas en `/mnt/project-files/referencias-reales/ambientacion/` (hoja `contacto_ambientacion.jpg`). Lectura en §3b del documento.

## 5. Trampas conocidas
- El dispositivo enlazado a este hilo fue el **MacBook**, no el PC: las carpetas del PC no se ven con las herramientas de carpeta. Para el PC hace falta un Remote Control o que alguien copie a `/mnt/project-files/`.
- `decisiones-noche.md` solo admite añadir al final.

## 6. Pendientes
- Modelos de Teo (paso superior y puente primero).
- Confirmar con Mak que Marcos recibe la lista P1-P9.
- Después de Sagunto: el resto de zonas (desmonte, puente, Nules) con la misma lógica.

## 7. Registro
- 6-nov 19:29: Eugenio, sobre las últimas capturas de Sagunto: «Me gusta 👍». Pendiente: P8 (humo, ropa tendida, columna de humo sobre Valencia), P9 (castillo), huerta y alquerías, coches y ambulancia de Teo (a falta de las fotos de Paula), y revisar la próxima build con las correcciones C1-C9 y §7b-7f.
- 6-nov 19:37: suelo (D-N67, docs/arte/suelo-sagunto.md). Hecho el §8 de sagunto-nivel.md: mapa de zonas de 1 px = 1 m (`sagunto_zonas_1m.png`, ids 0-10), máscara sin vegetación, densidades y trozo de muestra (X 20-95, Z 5-70, foco en (57; 0; 38)). Script en docs/niveles/herramientas/zonas.py. Eugenio quiere aprobar la muestra antes de producir en masa.
- 6-nov 19:59: Eugenio, sobre la muestra del suelo (trozo de la puerta oeste): «Me gusta como va quedando». Aún no es el sí para extenderlo a todo Sagunto (lo pregunta Mak). Cuando llegue, el mapa completo §8.1-8.3 ya está listo.
- 6-nov 20:25: Eugenio aprueba el suelo para todo Sagunto («te apruebo todo»). Densidades finales en §8.2 (descampado 20, recinto 8 al pie del muro). Castillo: FUERA DE CÁMARA (Lucía, opción C, adenda 5 de D-N68), centro en (39,25;361,25); sierra en x+z ≥ 480; calle de la Estación hasta Z 286; faldón hasta Z ≈ 480 (§8.3). Ojo: (7,75;267,75) NO es fuera de cámara.
- 6-nov 23:55 (noche de apretón de Eugenio): «se siente todo muy pequeño». §9 de sagunto-nivel.md: diagnóstico (la zona de 256 × 128 m se ve entera con el zoom máximo; calles de 6 m; el fuerte no tiene sitio para maniobrar ni para aterrizar). Nivel 1 (E1-E6: calles de 10/10/9 m, puerta de vehículos sur, parque de vehículos, helipuerto anexo) enviado a Mak y a Lucía. Nivel 2: zona de 512 × 256 m, pendiente de que Marcos o Nacho midan el FPS. Si sale, toca rehacer la distribución (v2).
- 7-nov 07:50: **sagunto-nivel.md v1.2** (§10). Revisada la rama `marcos/noche-prototipo` (5188f83): C1–C9 hechas; E1 y E2 siguen a 6 m, E3 a 7 m, E4 solo en la simulación, E6 sin el modelo de Teo. Frentes: F1 estación (recinto), F2 paso a nivel con puesto v2 en (43;82) yaw 90, F3 helipuerto v4 con puesto v2 en (207;51) yaw 270 y rearme en X 159-164, Z 31-41 (sin anillo HESCO), F4 tren móvil. Carril norte de la carretera abierto de X 64 a 200; cortes K1 (201,5;23) y K2 (59;86); 14 balizas. Dato `mapa_sagunto_carreteras_v1_2.json` (calle cortada en Z 86, carretera en X 200). Plano `sagunto_plano_v1_2.png`, zonas regeneradas. Subido a mr-mak-workspace (46cdca5). Pendiente: que Marcos lo integre (lista 10.6), Nacho (sitio del tren móvil, marca «sin cruce»), Lucía/Mak (helipuerto v4 o v0), nivel 2 en P2.
