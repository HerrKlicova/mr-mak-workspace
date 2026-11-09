# Mapa de zonas del suelo de Nules a 1 m por píxel, con los mismos ids que sagunto_zonas.json (Álvaro, 9-nov). python3 -I zonas_nules.py <carpeta>
import numpy as np, json, os, sys
from PIL import Image
D = sys.argv[1] if len(sys.argv) > 1 else '.'
X0, X1, Z0, Z1 = -80, 336, -80, 208          # zona 256 x 128 más 80 m de faldón por lado
W, H = X1 - X0, Z1 - Z0
xs = np.arange(W) + X0 + 0.5; zs = Z1 - np.arange(H) - 0.5
X, Z = np.meshgrid(xs, zs)
def box(x0, x1, z0, z1): return (X >= x0) & (X < x1) & (Z >= z0) & (Z < z1)
z = np.full((H, W), 5, np.uint8)               # base: huerta (la Plana)
z[box(X0, 26, 40, 98)] = 6                     # oeste: descampado pisado por donde entra Na
z[box(231, X1, 58, 98)] = 6                    # este: descampado junto a la vía (Nb)
z[Z >= 98] = 7                                 # el pueblo al norte (y su faldón)
z[box(10, 104.5, 92, 128)] = 6                 # plaza con jardín (palmeras sin colisión): por aquí entra Nc
z[box(85, 210, 96, 111)] = 2                   # explanada norte (§15)
z[box(X0, 104.5, 80, 92)] = 4; z[box(125.5, X1, 80, 92)] = 4   # aparcamiento y calle de la Estación
z[box(X0, X1, 31.5, 38.5)] = 4                 # calle del polígono
z[box(4, 64, 2, 29)] = 10; z[box(74, 164, 2, 29)] = 10; z[box(191.5, 252.1, 2, 29)] = 10   # naves (suelo bajo los modelos)
z[box(164, 191.5, 2, 29)] = 6                  # patio de carga (claro del NH90)
z[box(26, 85, 40, 80)] = 6; z[box(188, 231, 40, 80)] = 6   # alrededores de la estación, fuera del recinto (andenes de X 26 a 231)
z[box(85, 188, 40, 96)] = 1                    # recinto
for zc in (62.6, 66.4): z[box(X0, X1, zc - 2, zc + 2)] = 3     # generales
z[box(X0, 184, 47, 51)] = 3                    # apartado (topera en X 184)
z[box(200, 262, 40, 58)] = 5                   # huerto de víveres (§13)
z[(z == 5) & box(X0, X1, 8, 10)] = 9           # acequia madre al sur de las naves
Image.fromarray(z, 'L').save(os.path.join(D, 'nules_zonas_1m.png'))
meta = {"origen_px00": "esquina noroeste: X=-80, Z=208", "px_m": 1, "ancho": W, "alto": H, "X": [X0, X1], "Z": [Z0, Z1],
        "uv_unity": "u=(X+80)/416, v=(Z+80)/288 (fila 0 del PNG arriba, como v=1)",
        "zonas": "los mismos ids y colores que sagunto_zonas.json (0–11); aquí no hay cauce (8) ni cerro (11)",
        "fuente": "nules-nivel.md §2, §13 y §15; generador herramientas/zonas_nules.py"}
json.dump(meta, open(os.path.join(D, 'nules_zonas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# vista en color para comprobar
pal = {0: (138, 122, 92), 1: (96, 92, 72), 2: (148, 140, 110), 3: (90, 84, 76), 4: (108, 120, 116), 5: (80, 84, 28), 6: (128, 116, 90), 7: (180, 160, 128), 9: (108, 120, 116), 10: (96, 92, 72)}
rgb = np.zeros((H, W, 3), np.uint8)
for k, c in pal.items(): rgb[z == k] = c
Image.fromarray(rgb).resize((W * 2, H * 2), Image.NEAREST).save(os.path.join(D, 'nules_zonas_vista.png'))
print('ok', W, H, {int(k): int((z == k).sum()) for k in np.unique(z)})
