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
`MapaTactico.Mancha(...)` pinta la mancha de horda **oscura y tramada en 1c200c**, el valor de la horda, como el minimapa de la D-N147. **Solo pasa a rojo 982420 donde ataca un nodo o un tren** (Lucía, 8-nov: si siempre es roja, el rojo deja de avisar). `MapaTactico.EnAtaque(...)` dice si un téxel está en ataque: a menos del casco más 1,5 km de un nodo Asediada, o a menos de 2 km de un tren atacado.

## Cambios en `OperationsMap3D.cs` (iker/red-estaciones, 760 líneas)
1. **BuildTerrain**: sustituir el doble bucle que rellena `_baseColors` con `Hypso(...)` por
   `_baseColors = MapaTactico.Pintar(_relief, _a.Graph, MinX, (MaxX - MinX) / (TexW - 1.0), MaxY, -(MaxY - MinY) / (TexH - 1.0), TexW, TexH, false);`
   Crear `_tex` sin mipmaps y con Point: `new Texture2D(TexW, TexH, TextureFormat.RGBA32, false) { wrapMode = TextureWrapMode.Clamp, filterMode = FilterMode.Point };`
   Cambiar el material del terreno a `Shader.Find("Universal Render Pipeline/Unlit")` (el sombreado ya va cocido en la textura; con Lit, la paleta se oscurece y cambia de tono). La línea `_Smoothness` sobra.
2. **UpdateTexture**: al principio, la lista de trenes atacados en unidades de mapa (se usa también en el parche de detalle):
   ```
   var atac = TrenesAtacados();
   ```
   y la línea del Lerp pasa a `_px[y * TexW + x] = MapaTactico.Mancha(c, d, x, y, false, d > 0.08f && MapaTactico.EnAtaque(_a.Graph, mx, my, atac));` (las variables `a` y `float a = ...` sobran).
   Método nuevo en OperationsMap3D (copia la lógica de posición de UpdateNetwork):
   ```
   List<Vector2> TrenesAtacados()
   {
       var l = new List<Vector2>(); var g = _a.Graph;
       for (int i = 0; i < _a.Services.Count; i++)
       {
           var s = _a.Services[i]; if (!(s.Ambushed || (_a.Encounter.Active && _a.Encounter.Service == i))) continue;
           var t = s.Train; var e = s.AtStop ? null : t.CurrentEdge(g);
           if (e == null) { var n = g.Nodes[s.AtStop || t.Route.Count == 0 ? s.Stops[s.StopIndex].Node : t.Route[t.Route.Count - 1]]; l.Add(new Vector2(n.XMeters, n.YMeters)); }
           else { var f = g.Nodes[t.Route[t.Leg]]; var to = g.Nodes[t.Route[t.Leg + 1]]; float kt = e.LengthMm > 0 ? (float)t.OffsetMm / e.LengthMm : 0f; l.Add(Vector2.Lerp(new Vector2(f.XMeters, f.YMeters), new Vector2(to.XMeters, to.YMeters), kt)); }
       }
       return l;
   }
   ```
3. **Parche de detalle**: `const int TW = 256;` pasa a `512` en BuildDetail y en UpdateDetailTexture (23 m por téxel en lugar de 47). En BuildDetail, el bucle que rellena `cols` con `Hypso(...)` pasa a
   `double dmx = DetailSizeKm / MapGeo.KmPerUnit / (TW - 1); cols = MapaTactico.Pintar(_relief, _a.Graph, MinX + (center.x - half) / MapGeo.KmPerUnit, dmx, MaxY - (center.z - half) / MapGeo.KmPerUnit, -dmx, TW, TW, true);`
   `_detailTex`: `new Texture2D(TW, TW, TextureFormat.RGBA32, false) { wrapMode = TextureWrapMode.Clamp, filterMode = FilterMode.Point };`
   En UpdateDetailTexture, `var atac = TrenesAtacados();` antes del bucle, y la línea del Lerp pasa a `_detailPx[y * TW + x] = MapaTactico.Mancha(c, d, x, y, dot && d > 0.08f, d > 0.08f && MapaTactico.EnAtaque(_a.Graph, mx, my, atac));`
4. `Hypso` se puede quedar (ya no la llama nadie) o borrarse.

## Por comprobar (no tengo Unity)
- Que compile. Las firmas usadas son IElevationSource.HeightM, RailGraph.Nodes/Edges, RailNode.XMeters/YMeters/Name/Id y MapGeo.CoastX/KmPerUnit.
- Coste: el parche de detalle pide 514² alturas (antes, 256²) cada vez que se rehace, al moverse unos 3 km. En Python tarda unos 8 s; en C# debería quedarse por debajo de 0,2 s. Si da tirón, bajar TW a 384.
- **El paso entre la zona y el mapa (Lucía, 8-nov)**: nada de negro. Un fundido corto, de 0,3 s como mucho, a navy 181c30, atado al umbral de la rueda (al cruzar EnterKm hacia dentro y ExitKm hacia fuera), para que el zoom se sienta continuo y no como un corte de escena; es lo que Eugenio pidió comparándolo con Ebbtide. El suelo ocre b4a080 de la zona se queda. Es de Iker o de Marcos, en el sitio de NetSession.DrawFade.
- Las estaciones: los iconos y los nombres ya los dibuja OnGUI. En la captura, el icono de Nules queda debajo del panel del tren; eso es de TrenPanel, no del terreno.
