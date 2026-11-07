# QA13–QA20: diferencias entre la build y las maquetas

Bruno (Arte técnico), 07-11 ~07:50. Para Marcos. He comparado las capturas de la Galería (7) con las maquetas (`uidemo-referencia/`, `contraste/final_D/` y la D-N118). Los colores están medidos en las PNG de `mr-mak-workspace/docs/capturas/qa13…15`.

**Resumen.** QA13 y QA14 todavía llevan el HUD de depuración y el parte antiguo, y el kit UiNoche no aparece. La QA15 es la primera con el kit, y la composición coincide con las maquetas. Fallan sobre todo **los colores (un problema de espacio de color)**, la letra y las piezas que se entregaron después (contraste D, D-N118 y D-N122).

## 1. Colores: el más importante, y explica lo que vio Sara
El proyecto está en espacio de color Linear (`m_ActiveColorSpace: 1`) y los PNG del kit tienen sRGB activado (eso está bien). Lo medido:

| Dónde | Debería ser | Sale en la build | Lectura |
|---|---|---|---|
| Menú: texto de los botones (Hueso) | d4d0cc | **a7a099** | Al texto se le aplica sRGB→lineal: sale oscurecido |
| Menú: título de Opciones (Crema) | f0dc9c | **deb654** | Igual |
| Menú: números de los deslizadores (Beige) | b4a080 | **745937** | Igual |
| Menú: «Continuar» inactivo (OlivaGris 605c48) | 605c48 | ≈ navy | Por eso casi no se ve |
| Menú: placa de los botones (textura) | 181c30 | 181c30 | Correcto |
| Partida: placas del HUD y del parte (textura) | 181c30 | **565d78** | A la textura se le aplica lineal→sRGB de más: sale lavada |
| Partida: título del parte (Crema) | f0dc9c | f0dc9b | Sale bien, porque los dos errores se compensan |

**Hipótesis (sin verificar en Unity):**
- (a) IMGUI pasa a lineal los `Color` que recibe. Corrección: en `UiNocheKit.Texto` (y en cualquier `GUI.color` o `textColor`), usar `QualitySettings.activeColorSpace == ColorSpace.Linear ? c.gamma : c`.
- (b) En la escena de partida, el OnGUI acaba en un búfer intermedio que luego se vuelve a codificar a sRGB, quizá por la cámara URP con HDR o posproceso. En el menú no pasa.
- Si solo corriges (a), en la partida el texto saldrá lavado como las placas, así que hacen falta las dos.
- Prueba rápida para (b): en la partida, desactivar el posproceso o HDR de la cámara y comprobar que la placa del reloj vuelve a 181c30.

## 2. Menú (QA15, `qa15_menu_build_vs_maqueta.png`)
- Las placas son las antiguas de la D-N115. Falta el **retoque D** (`contraste/final_D/`): borde concrete_light, texto inactivo concrete y candado.
- Letra: sale la de sistema, fina y sin sombra; la maqueta usa la de píxel con sombra. Ya lo sabíamos, pero además el texto queda **pegado arriba** dentro del botón. Propuesta: `Texto` con `TextAnchor.MiddleLeft` y el alto del botón, en lugar de y + 4.
- Opciones (`qa15_opciones_build_vs_maqueta.png`): la composición coincide al píxel. Las diferencias son solo los colores del punto 1. En la maqueta, la casilla de pantalla completa está marcada; en la build no, pero eso es un dato, no un error.

## 3. HUD de partida (QA15)
- La disposición coincide con -uidemo: recursos, reloj y barra de la noche, avisos, fila de frentes, tarjetas y órdenes.
- **Tarjetas de vehículo** (`qa15_tarjetas_vehiculo_x3.png`): siguen siendo las de antes de la D-N118.
  - Llevan texto encima del marco («alto», «tierra»).
  - No tienen la placa del número ni las tres barras.
  - **El VAMTAC sale con el fotograma de caja abierta y lanzador**, que Nacho mandó quitar. Ya está corregido en la tira (todas las variantes son ahora el blindado), pero aun así usad el fotograma 0.
  - Las tres llevan el mismo número táctico «94», porque todas usan el mismo índice de fotograma.
  - Integrar `entregas/bruno-vehiculos/final/` (LEEME y JSON).
- Falta la fila del muro (D-N122, `entregas/bruno-muro/final/`). Es lógico, porque se entregó después.
- Las capturas de partida salen a 960x540. Si la ventana era de ese tamaño, la base de 640x360 queda a x1,5, que no es entero, y los píxeles salen desiguales. Usad ventana o escala entera (x2 = 1280x720, x3 = 1920x1080), o decidme si es solo cosa de cómo se guardó la captura.

## 4. Parte (QA15)
- La composición coincide con `uidemo_3_parte`. «Seguir» casi no se lee: el texto sale gris sobre el oliva claro, por el punto 1.
- La derrota lleva el velo y el borde rojo, como en la maqueta.

## 5. QA13 y QA14
- HUD de depuración, texto plano y parte antiguo («Sagunto ha caído.» sin el kit). La QA15 los sustituye, así que no apunto nada más de ellos.
- Las capturas «victoria_*» de QA13 y QA14 muestran derrotas («Sagunto ha caído», integridad 0 %). Es del guion de la prueba, no del arte. Se lo comento a Sara.
- Mapa de red (QA13, `vista_mapa_tras_vista`): las unidades en tránsito no llevan las piezas del ETA (D-N113: ficha de 13 con muesca, placa ETA y barra). Están en `entregas/bruno-mapa/final/`. Ahora solo se ven el icono y el nombre.
- Vista del tren (QA13): no se ven el humo diésel ni el destello del faro (D-N84, `noche-prototipo/tren/`). Comprobad si estaban apagados en esa prueba.

## 6. QA20 (07-11, de 04:33 a 05:41; corridas normal, difícil, fácil y vehículos)
Mismo estado que la QA15. No he visto ninguna pieza nueva integrada ni ningún cambio de color:
- El reloj y las placas siguen en **565d78** en las cuatro corridas (deberían ser 181c30). El texto del parte sale gris claro sobre el azul lavado. Es el punto 1.
- Las tarjetas de vehículo siguen siendo las de antes de la D-N118: el VAMTAC con lanzador, el «94» repetido y las etiquetas «alto» y «tierra» encima.
- Sin la fila del muro (D-N122) ni el retoque D del menú.
- La derrota tiene el botón **«Volver a empezar» casi ilegible**: el texto (≈ c1c1a2) sobre la placa clara (b1b694) da menos de 1,2:1. Al corregir el punto 1 debería mejorar; si no, ese botón tiene que usar la placa normal y no la de encima.
- Las capturas siguen saliendo a 960x540 (x1,5).
- Lo bueno: la composición del HUD, del parte y del velo de derrota sigue coincidiendo con las maquetas, y la horda se lee como masa oscura en la corrida difícil.

## §7 QA22 (normal, 08:35; Bruno, 7-nov 08:30 UTC)
Capturas: `docs/capturas/qa22/normal_captura_*.png` (960x540, solo partida; no hay menú ni parte).

**Color (comprobar_color.py hud sobre normal_captura_20261107_083627):**
- Tal cual: placa del reloj y panel de órdenes en `565d78` (debe dar `181c30`: MAL). El texto Hueso sí da `d4d0cc`.
- Si se deshace una codificación sRGB: placas en `181c30` exacto (OK), y el texto pasa a `a7a099`, el mismo oscurecimiento del menú.
- Lectura: en la escena de partida, la imagen entera (mundo y HUD) lleva **una codificación sRGB de más**. La foto de la pantalla de Eugenio (08:20) coincide con la captura tal cual, así que no es cosa de la captura. Por eso la noche sale beige, plana y «sepia». Debajo de eso, el texto IMGUI sigue saliendo oscuro (falta el `c.gamma` de f6c4785 compilado).
- Sospechoso principal (sin verificar): `_lowRt` creada como `new RenderTexture(w, h, 24, RenderTextureFormat.ARGB32)`. Prueba: descriptor con `sRGB = true` o `GraphicsFormat.R8G8B8A8_SRGB`. Lo que debería verse: `/mnt/project-files/docs/arte/pixel-codigo/noche-prototipo/color-noche/qa22_ahora_vs_sin_doble_srgb.png`.

**Integración:**
- D-N118: **sigue sin integrar**. Las tarjetas de vehículo son las de antes: llevan las etiquetas «alto» y «tierra» encima y el «94» repetido, igual que en el §6.
- D-N122 (muro en el HUD), retoque D del menú y botón C del parte: **no se pueden comprobar**, porque no salen en estas capturas. Hacen falta capturas del menú, del parte y del HUD con el muro dañado.
- Trazadoras: salen como líneas largas de arma a blanco (los «láseres» de Eugenio). Ver §4 de docs/encargo-control-disparos-noche.md.
