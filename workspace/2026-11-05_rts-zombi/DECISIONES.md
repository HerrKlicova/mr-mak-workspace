# Decisiones

Registro de decisiones del proyecto. Cada entrada tiene un identificador `D-xxx`, un estado
(**aceptada**, **propuesta**, **abierta**, **sustituida por D-yyy**) y su origen. Una decisión nunca
se borra: si cambia, se crea otra que la sustituye y se anota el cambio en [CAMBIOS.md](CAMBIOS.md).

| ID | Fecha | Decisión | Estado | Origen |
| --- | --- | --- | --- | --- |
| D-001 | 2026-11-05 | Motor: **Unity 6.3 LTS (6000.3.x)** con URP y Entities 1.5.0 / Entities Graphics 1.5.0. Razones: es la LTS vigente (soporte hasta dic-2027), Entities cambia de API desde la 6.4 y la 6.3 es la línea verificada. | aceptada | Eugenio autorizó la versión el 5-nov; Unity 6.6 (Update release, no LTS) descartada en D-006 |
| D-002 | 2026-11-05 | El **3D se genera con Hunyuan** (addon «Image to 3D» de Blender). Solo para vehículos y edificios clave; las hordas no usan modelos generados. | aceptada, **en revisión por licencia** (ver D-011) | Eugenio, 5-nov |
| D-003 | 2026-11-05 | **Imágenes de referencia y concepto** por la API de ElevenLabs (plan Pro). Candidatos: GPT Image 2.5 (Sunburst o Flare) y Nano Banana Pro (`gemini-3-pro-image`). Seedream queda fuera hasta confirmar su acceso. Se compararán los dos con el mismo prompt cuando el concepto esté cerrado (recomendación del hilo B, aceptada). | aceptada | Eugenio mencionó ambos modelos el 5-nov; prueba hecha con `gpt-image-2.5-flare` |
| D-004 | 2026-11-05 | **Pixelab solo para la capa 2D** (iconos, interfaz, mapa, retratos, impostores, VFX, decals). El plan se reinicia el 17-nov y probablemente no se renueve: el lote se genera antes del 12-nov. | aceptada | Eugenio, respuesta «p2: si» del 5-nov; documento del piloto |
| D-005 | 2026-11-05 | **mr.mak es la fuente viva del proyecto**: GDD, ideas, assets y sonidos, con el historial de cambios respecto a la idea original. | aceptada | Eugenio, 5-nov |
| D-006 | 2026-11-05 | **No usar Unity 6.6** para este proyecto. Es una Update release (sin soporte largo) y Entities cambia de API entre versiones. | aceptada (Eugenio: «a todas mis preguntas respondo lo que tú recomiendas», 5-nov) | Hilo B |
| D-007 | 2026-11-05 | **Repositorio del juego separado** del de mr.mak: `C:\Dev\TBD` con origen `https://github.com/HerrKlicova/TBD.git`. mr.mak irá a `https://github.com/HerrKlicova/mr-mak-workspace.git`; hasta cambiar su `origin` (hoy es la plantilla del autor), no se hace push desde mr-mak-workspace. | aceptada (repositorios creados por Eugenio); cambio del `origin` de mr.mak pendiente | Eugenio creó los repositorios el 5-nov; Hilo B |
| D-008 | 2026-11-05 | **Proyecto Unity creado a partir de la plantilla «3D URP» del editor 6000.3.28f1**, sin `Library/`: URP 17.3.0, Entities 1.5.0, Entities Graphics 1.5.0 y MCP for Unity 10.3.0 por manifest; `.gitignore` oficial de Unity, Git LFS para binarios y `.mcp.json` sin claves. Primer commit `0726f9f`, subido a `TBD`. **Aún sin abrir en Unity** (falta activar la licencia Personal). | aceptada | Eugenio: «guía completada» y «te autorizo a todo» (5-nov) |
| D-009 | 2026-11-05 | **Primero el juego, después los assets.** El lote de Pixelab queda parado (167 generaciones gastadas hoy; 18 VFX gratis hechos) y se empieza el prototipo de zona en `C:\Dev\TBD` con primitivas y sin arte: fuerte con puerta, vía con tren, horda en DOTS que se amontona y cae, y shader de pixelado con la paleta de 32 colores. Commit `df5f7cf`. | aceptada | Eugenio, 5-nov («¿no es mejor empezar primero a desarrollar el juego?») |
| D-010 | 2026-11-05 | **Base del zombi 3D: Kenney «Animated Characters 3» (CC0)**, con aspectos de zombi y animaciones idle y correr; animaciones adicionales por resolver (Mixamo exige cuenta de Adobe de Eugenio). Pendiente de que Eugenio descargue el zip a mano (kenney.nl bloquea la descarga por script). | aceptada (descarga pendiente) | Eugenio, 5-nov («Vale pues adelante», «respondo lo que tú recomiendas») |
| D-012 | 2026-11-05 | **Sin sensación de rejilla y cámara libre** (GDD §9c, v1.10). Agentes con posición, velocidad y orientación continuas; el flujo solo da la dirección deseada, interpolada bilinealmente; rejilla interna de 0,5 m con datos agregados; muros como sólidos con grosor y altura con colisión cápsula; construcción libre por polilíneas; cámara con rotación, inclinación y zoom continuos y snapping a píxel solo visual. Implementado en el prototipo (commit `353a881` de `TBD`), sin compilar ni probar. | aceptada | Eugenio, 5-nov («que no se sienta como un juego 2D que limita el movimiento y la construcción»); Hilo A |

## Cómo añadir una decisión

1. Siguiente `D-xxx` libre.
2. Una frase de decisión, una de motivo y el origen (quién la tomó y cuándo).
3. Si sustituye a otra, cambiar el estado de la anterior a «sustituida por D-yyy» y añadir la entrada correspondiente en `CAMBIOS.md`.
