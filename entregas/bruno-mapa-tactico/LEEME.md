# Plano táctico oscuro en el mapa de operaciones (estilo de la D-N113). Bruno (Arte técnico), 8-nov

Encargo de Lucía: a 2500 m, la vista de mapa salía como «un plano beige con dos líneas» (Teo, captura 4_nules_descargar.png). Causa: el terreno se pintaba con `Hypso`, un degradado de altura beige (el llano en b4a080), con luz de URP Lit y filtro bilineal. Además, el parche de detalle de 12 km solo tenía 256 téxeles. No había costa, pueblos, curvas ni sombreado.

**Previas** (sin Unity, mismo cálculo pasado a Python; `previa_mapa_tactico.py`):
- `mapa_tactico_nules_2500m.png`: el parche de cerca sobre Nules, en vista cenital (en el juego se verá con perspectiva). Se ven el casco con manzanas, la huerta con lindes, la carretera y las curvas de nivel.
- `mapa_tactico_costa_lejos.png`: el terreno grueso de la costa, de Valencia a Castellón, con el sombreado, las curvas cada 200 m, el mar y la línea de costa.

## Qué hace `MapaTactico.cs` (archivo nuevo, `Assets/TBD/Scripts/View/`)
`MapaTactico.Pintar(relieve, grafo, mx0, dmx, my0, dmy, w, h, detalle)` devuelve los téxeles en la paleta de 32:
- suelo por bandas de altura (303424, 48403c, 605c48, 6c7874 y 94948c) con fundido tramado; sombreado cocido con la luz del noroeste; curvas de nivel (de cerca, cada 50 m, y cada 250 m más marcadas; de lejos, cada 200 m y cada 1000 m más marcadas);
- mar en navy 181c30 con la costa en 94948c;
- pueblos alrededor de cada nodo (radio por nombre, PROTOTIPO): manzanas, calles y filo claro;
- huerta del llano litoral (solo de cerca) y carreteras paralelas a la vía, también PROTOTIPO, como el relieve.
`MapaTactico.Mancha(...)` pinta la mancha de horda tramada en 982420, con los puntos de cerca en 642030, en lugar del Lerp hacia (150, 22, 26).

## Cambios en `OperationsMap3D.cs` (iker/red-estaciones, 760 líneas)
1. **BuildTerrain**: sustituir el doble bucle que rellena `_baseColors` con `Hypso(...)` por
   `_baseColors = MapaTactico.Pintar(_relief, _a.Graph, MinX, (MaxX - MinX) / (TexW - 1.0), MaxY, -(MaxY - MinY) / (TexH - 1.0), TexW, TexH, false);`
   Crear `_tex` sin mipmaps y con Point: `new Texture2D(TexW, TexH, TextureFormat.RGBA32, false) { wrapMode = TextureWrapMode.Clamp, filterMode = FilterMode.Point };`
   Cambiar el material del terreno a `Shader.Find("Universal Render Pipeline/Unlit")` (el sombreado ya va cocido en la textura; con Lit, la paleta se oscurece y cambia de tono). La línea `_Smoothness` sobra.
2. **UpdateTexture**: sustituir la línea del Lerp por `_px[y * TexW + x] = MapaTactico.Mancha(c, d, x, y, false);` (las variables `a` y `float a = ...` sobran).
3. **Parche de detalle**: `const int TW = 256;` pasa a `512` en BuildDetail y en UpdateDetailTexture (23 m por téxel en lugar de 47). En BuildDetail, el bucle que rellena `cols` con `Hypso(...)` pasa a
   `double dmx = DetailSizeKm / MapGeo.KmPerUnit / (TW - 1); cols = MapaTactico.Pintar(_relief, _a.Graph, MinX + (center.x - half) / MapGeo.KmPerUnit, dmx, MaxY - (center.z - half) / MapGeo.KmPerUnit, -dmx, TW, TW, true);`
   `_detailTex`: `new Texture2D(TW, TW, TextureFormat.RGBA32, false) { wrapMode = TextureWrapMode.Clamp, filterMode = FilterMode.Point };`
   En UpdateDetailTexture, sustituir la línea del Lerp por `_detailPx[y * TW + x] = MapaTactico.Mancha(c, d, x, y, dot && d > 0.08f);`
4. `Hypso` se puede quedar (ya no la llama nadie) o borrarse.

## Por comprobar (no tengo Unity)
- Que compile. Las firmas usadas son IElevationSource.HeightM, RailGraph.Nodes/Edges, RailNode.XMeters/YMeters/Name/Id y MapGeo.CoastX/KmPerUnit.
- Coste: el parche de detalle pide 514² alturas (antes, 256²) cada vez que se rehace, al moverse unos 3 km. En Python tarda unos 8 s; en C# debería quedarse por debajo de 0,2 s. Si da tirón, bajar TW a 384.
- **El paso a la zona**: el suelo de la zona sigue en el ocre b4a080 (Lucía, 6-nov, para que el fundido no saltara). Con el plano oscuro, el paso a menos de 2 km cambia de color. Si se nota feo, que el fundido de entrada a la zona pase por negro (NetSession.DrawFade), o lo hablamos con Lucía.
- Las estaciones: los iconos y los nombres ya los dibuja OnGUI. En la captura, el icono de Nules queda debajo del panel del tren; eso es de TrenPanel, no del terreno.
