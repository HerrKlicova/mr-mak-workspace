# D-N80 · Shader de la horda (TBD/Horda): un material para todas las siluetas de Teo

Bruno (Arte técnico), 8-nov, 22:45. Esto está **SIN COMPILAR**: lo he escrito en la nube, sin Unity. Quien lo integre
(Marcos) tiene que abrirlo y mirar la consola. Me pasáis el error tal cual y lo corrijo.

## Qué resuelve

- **Antes**: un material URP Lit por camisa (`RenderAssets.Materials`), teñido con `ZombieBaseColor` hacia #303424.
  Con 5 siluetas × 3 camisas salen 15 combinaciones de material y malla, y toda la horda queda en un único tono.
- **Ahora**: **un solo material** `TBD/Horda` para las 5 (o más) mallas, así que son 5 lotes de Entities Graphics.
  El tono sale por instancia de `horda_paleta_lut.png` (8 camisas × 6 pantalones × 4 pieles, todos en L* 9–13),
  usando la máscara de color de vértice que ya escribe el `entregar.py` de Teo:
  - R = camisa, brazos y roto
  - G = pantalón y objetos (falda, mochila, gorra, casco, chaleco, bolsa, bastón, sombrero)
  - B = piel, pelo y nuca
  - negro = calzado, que sale en #1c200c (`_Resto`)
- No usa UV ni textura de albedo.
- Sangre acumulada opcional: el nivel 0–15 va en `_HordaPack.w`. Se pinta con `sangre_rampa.png` y Bayer 4×4 en espacio de mundo,
  sin alfa parcial. Las reglas son las de `horda_paleta.json`.
- Luz: Lambert del sol o la luna con sombras, más el ambiente SH. Sin especular. Pases ForwardLit, ShadowCaster y DepthOnly.
  Compatible con SRP Batcher y DOTS instancing (`#include_with_pragmas …/DOTS.hlsl`).

## Archivos (rutas como en el proyecto)

| Archivo | Qué es |
|---|---|
| `Assets/TBD/Shaders/Horda.shader` (+ .meta) | El shader |
| `Assets/TBD/Scripts/View/ZombiePaleta.cs` (+ .meta) | Componente `[MaterialProperty("_HordaPack")]` y `HordaPaleta.Elige(id)`, la regla de mezcla de build_horda_color.py portada tal cual, con los vectores de prueba en el comentario |
| `Assets/TBD/Resources/Icons/noche/sangre_rampa.png` (+ .meta) | Rampa de sangre 16×1, en Point y sin mipmaps. `horda_paleta_lut.png` ya está en el proyecto |

## ACTUALIZACIÓN 8-nov, 23:15: código ya conectado en TBD, rama `claude/horda-dn80` (896b197, sobre marcos/noche-prototipo ae93063)

El código ya está en esa rama. Con Unity abierto, a Marcos solo le queda copiar los binarios (desde la nube no se pueden subir por LFS):
1. Los 5 FBX LOD1 de `entregas/teo-modelado/zombis-dn80/` van en `Assets/TBD/Resources/Models/ZombiDN80/`, con el mismo nombre
   (`SM_Zombi_v3_Civil_LOD1.fbx`, etc.). En el import, *Vertex Colors* tiene que quedar en Import, que es lo normal, y *Mesh Compression* en Off.
2. `sangre_rampa.png` de esta entrega va en `Assets/TBD/Resources/Icons/noche/`, con su .meta.
3. Fusionar `claude/horda-dn80`. Al arrancar, la consola dice `[D-N80] horda con TBD/Horda: 5 siluetas, 1 material`.
   Si falta alguna malla, avisa con `[D-N80] falta …` y sigue con los zombis de antes, así que no rompe nada.
4. El shader ya está en *Always Included Shaders*, en GraphicsSettings.
5. Para cerrar la D-N80, Lucía pide una captura de noche con `-nightdense`.

## Cómo conectarlo a mano (referencia; la rama ya lo hace)

1. Crear el material `Horda.mat` con el shader `TBD/Horda`, poniendo `_HordaLut` = horda_paleta_lut y `_SangreRampa` = sangre_rampa.
   Tiene que estar marcado *Enable GPU Instancing*, aunque con Entities Graphics no hace falta.
2. En `PrototypeBootstrap`, donde hoy se llama a `RenderAssets.SetVariants(meshes, materials)`, pasar las mallas de Teo y
   **un único material**: `RenderAssets.SetVariants(meshes, new[] { hordaMat })`. Con `Variants = 1`, `teo` vale false
   en `RenderAttachSystem`. Por eso hay que cambiar la condición a `bool teo = RenderAssets.MeshVariants > 1;` y elegir la malla así:
   `mmi = MaterialMeshInfo.FromRenderMeshArrayIndices(0, (int)((hv >> 8) % (uint)RenderAssets.MeshVariants));`
3. En el mismo bucle, junto a `ZombieBaseColor` (o en su lugar), añadir:
   `em.AddComponentData(e, new ZombiePaleta { Value = HordaPaleta.Pack(zs[i].SimId) });`
   Si el material es TBD/Horda, `ZombieBaseColor` y `ZombieAtlasST` sobran (no dan error, pero gastan memoria por instancia).
4. Sangre, para más adelante: un sistema de presentación que sube `ZombiePaleta.Value.w` (+3 por impacto, +8 por muerte) y lo baja 1 cada 1,25 s.
   No va en la simulación.
5. El LOD de lejos sigue como está, con el sprite de masa de 8 px y su propio material en el índice 1 si `LodOn`.

Cosas que comprobar al abrirlo:
- Que el shader compila con DOTS_INSTANCING_ON. Si `UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_DEFAULT` no existe en esta versión,
  se cambia por `UNITY_ACCESS_DOTS_INSTANCED_PROP(float4, _HordaPack)`.
- Que `_HordaPack` llega distinto a cada zombi: con `-nightdense` tiene que verse variedad de matiz con el mismo valor.
- El .meta de `horda_paleta_lut.png` del proyecto tiene `textureCompression: 1` en una plataforma. Tiene que ir sin compresión,
  porque si no los 18 colores se mezclan.

## Siluetas (Teo)

Hay una herramienta nueva, `lamina_siluetas_horda.py` (TBD claude/sprites-importar, skill pixel-art-codigo/ejemplos).
Proyecta cada OBJ como la cámara del juego: ortográfica, 55°, ortho 26 y 1 px = 0,144 m. Saca la lámina de 8 orientaciones y la IoU entre cada par.
El criterio que propongo, a validar con Lucía, es que todos los pares tengan una IoU media de 0,70 o menos. `--prueba` la comprueba con 5 figuras de cajas.
