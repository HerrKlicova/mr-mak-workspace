# D-N160 · Pantalla del Informe de inteligencia y la Colmena en el mapa (Bruno, 9-nov). MUESTRA

Generado con build_informe.py (TBD claude/sprites-importar). Textos PROVISIONALES: el final lo escribe Lucía. Texto en Inter, marcos en múltiplos de 3 px y paleta de 32.

## 1) Informe: 5 composiciones a 1920×1080 (`hoja_informe.png`; cada una en `informe_V1..V5.png`)
Los 8 apartados aprobados: cabecera con el DTG «D41 · 2030A», resumen en una línea (con el glifo del estado), amenaza, fuerzas propias,
sin novedad en, valoración, necesidades y firma. Todas llevan el mapa APP-6 encajado.
Cada una usa la palabra de estilo de su variante del prefijo validado, así se ve cada marco montado.
| | Composición | Marco |
|---|---|---|
| V1 | Dos columnas: mapa grande a la izquierda y el parte entero a la derecha | remaches |
| V2 | Carpeta: mapa a todo el ancho y debajo el parte en 3 columnas | bisel |
| V3 | Teletipo: líneas numeradas en una columna central y el mapa en un recuadro | escuadras |
| V4 | Mesa de mapas: mapa a pantalla completa y el parte en tarjetas a los lados | marco doble |
| V5 | Pestañas: un apartado abierto cada vez y el mapa a la derecha | esquinas cortadas |

**Recomiendo la V1.** Se lee todo de una vez, sin pestañas; el mapa es lo bastante grande para los APP-6 a ×2; y el texto va a 19–21 px en una columna de 680 px.
La V4 es la más atmosférica, pero las tarjetas tapan la mitad del mapa. La V5 esconde la valoración detrás de una pestaña.

## 2) Avisos de la Colmena (`colmena_avisos.png`)
- El ámbar «La Colmena se agita…» va en el panel de avisos del mapa, junto al de zona sin tropa. Es ámbar porque es un aviso. El rojo es solo para ataques.
- CO-1 a CO-4 son entradas del informe con el glifo del estado. CO-2 va resaltada y lleva la causa con números (nodos abiertos y señal) y qué la calma.
- Al cambiar de estado sale una banda arriba al centro durante 2,5 s, en hueso y con el glifo.

## 3) La Colmena en el mapa sin ojos y sin texto (`colmena_mapa.png`, de cerca y de lejos a ½)
- La masa va siempre en #1c200c; lo que cambia es la **forma**.
  - **Dispersa:** punteado suelto y ancho, sin núcleo, con trébol y «~2.000?».
  - **Al acecho:** núcleo macizo con orla punteada, rombo discontinuo y flecha de eje.
  - **Enjambre:** masa maciza con contorno hueso, **columna de galones en V** con borde hueso hasta el nodo, y la cifra sin «~».
- De lejos, Dispersa y Al acecho se distinguen por el núcleo, y el Enjambre por la columna, que también se lee sobre la meseta oscura.
- Glifo del estado (16×16 u, en hueso): puntos sueltos, anillo cerrado y punta.
