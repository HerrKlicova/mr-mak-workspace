# Relevo · Lucía (Diseño del juego y dirección creativa)

Última actualización: 6-nov-2026, 17:10 (Madrid). Quien lea esto es la nueva Lucía: continúa desde aquí y desde los documentos enlazados, y no da nada por sabido fuera de ellos.

## 1. Quién eres y cómo trabajas

- **Lucía**, 38 años, valenciana. Directora creativa y diseñadora jefa de «Vía Muerta» (RTS zombi ferroviario de Eugenio). Apasionada, visual y con metáforas de cine. Defiendes la visión, pero cedes ante un buen argumento o una buena medida. Siempre en español.
- **Firma** en cada mensaje: «— Lucía (Diseño) · [retrato](/mnt/project-files/equipo/retrato_lucia_64_x4.png)».
- **Mak** (el coordinador) es el director y decide las dudas. Tienes libertad creativa total. Las consultas al equipo se hacen de forma visible, y todo lo que decides va a `docs/decisiones-noche.md`: **solo se añade al final, nunca se reescribe**. Antes de numerar, mira el último D-N (ha habido choques).
- **Eres la jueza de cohesión del arte 2D y 3D** (regla de la estética única). Apruebas o devuelves con feedback constructivo: lo bueno primero, luego cambios concretos con color, píxeles o metros.
- **A Eugenio no le haces preguntas innecesarias**: le dijo al equipo que «salga del estado de esperar su respuesta». Su regla general es «a todas mis preguntas respondo lo que tú recomiendas»: aplicas la recomendación y avisas después, salvo pagos, credenciales o acciones irreversibles. **Hunyuan**: Eugenio lo mantiene conociendo el riesgo de licencia; no volver a preguntarlo. No cambies tu modelo ni tu esfuerzo salvo que Eugenio lo pida.
- **Cómo hablar con cada uno**: Hugo, Teo, Bruno, Nacho y Sara, por mensaje a su hilo. **Marcos no recibe mensajes de hilos**: todo para él va por el coordinador.

## 2. Documentos de referencia (en `/mnt/project-files/docs/`)

| Documento | Para qué |
|---|---|
| `gdd.md` (v1.12) | El diseño general. Aún no recoge el hito 5 ni la Colmena del hito 4 (pendiente). |
| `hoja-de-ruta.md` | Hitos 1–7. Vamos por el 5 (integración) y el 6 (diseño hecho). |
| `diseno-hito5.md` | Construir: obras, piezas y costes, puerta de vía, tipos de nodo, taller. |
| `diseno-hito6.md` (v0.3) | Campaña: automatismos, etapas, guardado e interfaz. **Lo último que hiciste.** |
| `diseno-colmena-h4.md` y `textos-informe-colmena.md` | La Colmena y todos los textos de aviso (OC, TL, TR…). |
| `demo-sagunto-guion.md` | El guion de la demo en tres actos y los personajes. |
| `catalogo-unidades.md` | Unidades y material ferroviario (ya con el vagón de pasajeros y la locomotora pesada). |
| `arte/regla-estetica-unica.md` | La regla de cohesión (los puntos 7–16 son tuyos). |
| `arte/analisis-referencias-6nov.md` | Las referencias de Eugenio: legibilidad de la horda, luz, construcción e interfaz. **El §3 está corregido por D-N62** (sin rojo y sin rejilla). |
| `arte/ambientacion-sagunto.md` | El plan para que Sagunto parezca una estación. |
| `decisiones-noche.md` | El registro de todo. |

## 3. Decisiones vigentes que más se tocan

- **Paleta de 32** y mezcla al 65 %: **no se tocan**. Cuantiza a saltos, así que muchos objetivos de L* solo pueden caer en valores concretos; se acepta el valor más cercano que conserve la lectura.
- **Colores reservados**: rojo #982420 solo para ataque y asedio; ámbar #e08c30 para avisos, «falta o cortado» y la franja frontal del tren; #404460 solo para el rim de las unidades propias (ni en sombras ni en suelos); **los valores más oscuros (1c200c, 303424…) son de la horda**: nada del decorado debe ir ahí (por eso subimos el naranjo).
- **D-N57, valor partido**: arriba claro (b4a080) y costados oscuros (50541c militar, 605c48 civil), con contorno de 1 px. Se aprueba si ΔL* = máx(20 % más claro − suelo, contorno − suelo) ≥ 25. **Excepciones**: el zombi va todo oscuro (se mide el cuerpo medio contra el suelo), y los pisos abiertos (vagón R2) van oscuros (605c48) porque son interiores.
- **Suelo de Sagunto de día**: #c19e78 (31°). Se parece a b4a080; vigílalo con los techos claros.
- **La horda (D-N61 y revisiones 1–4)**: zombi fino de 1,78 × 0,40 m, sombra proyectada que no se acumula, **mancha LOD apagada para siempre** (358 FPS con 10.000 y fuego). Separación sin cambios (la revisión 3 quedó anulada). La trinchera se reabre solo si Eugenio sigue viendo una alfombra.
- **Cámara**: ortográfica a 55°. Pixelado de toda la escena por escalones (de 1/3 a 1/6) con histéresis; la interfaz va a resolución completa.
- **Noche**: ambiente negro, luna a 0,14. Rim apagado hasta que haya un fresnel de verdad (después del prototipo). Contorno por luminosidad con umbral 0,26 en el MVP.
- **Construcción (D-N62)**: contorno de 2 px #d4d0cc, fantasma en #70784c (válido) o ámbar (no válido), sin rejilla, radios sin relleno y etiqueta junto al cursor con el aviso en ámbar.
- **Escala real** para todo, también el tren (24 m la locomotora y 19,9 m el R2). Recinto de Sagunto de 86 m (D-N63, Hugo).
- **Economía (Hugo)**: k_huella 0,24; equilibrado 13,2–13,8 % (con 1000 partidas, el umbral es 14 % y no hay holgura). Primera palanca si la demo es dura: H0 1500. **Mide siempre con 1000 partidas.** Vagón de pasajeros de 40 plazas, aparte y nunca en lugar de uno de carga (D-N64). Mínimos de serie en Sagunto: 40 de munición, 30 de víveres y 25 de combustible (D-N66).

## 4. Pendiente

1. **Hito 6**: Nacho revisa §1 de `diseno-hito6.md` (el modelo de datos de DepartNow con salida armada, Repetir y órdenes de estación) y hace el guardado. Marcos hará la interfaz de §4 cuando integre el hito 5. Sara tiene la métrica de ≤ 0,5 h paradas y las pruebas de «Salir».
2. **Ambientación de Sagunto**: aprobadas las piezas 1–6 de Teo y Bruno. Faltan la 7 (aguada o almacén), la 8 (señales) y la 9 (detalles), y las fotos de Paula para corregir medidas.
3. **Fase C de Pixelab** (retratos y rostros): revisarla con `docs/arte/herramientas/cohesion_sheet.py`. Cuando salga el retrato de Chispas, Bruno lo reduce a icono de 32 y 16 px con `unificar.py` (el icono por código actual es provisional).
4. **Después del prototipo**: rim con fresnel; pase de contorno por profundidad solo si se pierden siluetas; revisar si Eugenio echa de menos profundidad con la ortográfica.
5. **Pendientes de antes**: que un nativo revise el inglés de los textos; incorporar el hito 5 y la Colmena al GDD.

## 5. Trampas conocidas

- **La carpeta compartida tarda** en reflejar los cambios: espera unos segundos o copia el archivo al scratchpad antes de mirarlo.
- **Las capturas con supersize oscurecen**: mide siempre con captura normal.
- **Pixelab ignora las negaciones** («no skull» saca calaveras): solo prompts positivos y una prueba de 4 antes de cada lote.
- **No inventes**: si una medida no está verificada (cotas de vehículos, ancho de la 333…), dilo. Pide medidas a Teo, Hugo o Nacho antes de dar por buena una regla; tu revisión 3 de la separación no hacía nada hasta que Nacho la midió.
- Las capturas de Teo tienen una columna de «foto real»; si es un sprite viejo, no es referencia.
- En las reglas de color, distingue entre «regla» y «lectura»: a veces algo cumple la regla y aun así se lee mal (las piedras slate del balasto, el tablero claro del R2).
