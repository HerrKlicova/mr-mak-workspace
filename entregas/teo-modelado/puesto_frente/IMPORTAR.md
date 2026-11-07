# Puesto de frente: nota de importación para Marcos

Teo, 7-nov-2026. Aprobado por Lucía; la variante por defecto es la v2. Código en `bloques/puesto_frente.py`, commit eda9825 de la rama `claude/modelado-3d-skill`.

## Archivos
- En el PC: `C:\Dev\mr-mak-workspace\herramientas\modelado-3d\puesto_frente\`
- En el proyecto: `/mnt/project-files/docs/arte/modelado-3d/puesto_frente/`
- `SM_PuestoFrente_vN_LOD0.fbx` y `SM_PuestoFrente_vN_LOD1.fbx`, con N de 0 a 4.
- `T_Paleta32.png`: los colores van por UV a esta paleta, como en el resto de bloques.

## Variante por defecto
**La v2** (Lucía, 7-nov): un recinto cuadrado de HESCO con la entrada estrecha al sur y unos sacos delante en chicane, una tienda y un mástil con antena y foco. Repite el lenguaje de la puerta de vehículos y es la que más destaca de noche. Bruno ha hecho el icono del mapa por defecto a partir de esta planta.

Las otras cuatro sirven para que cada sitio del mapa tenga su propio aspecto:

| Variante | Qué es |
|---|---|
| v0 | Anillo octogonal de sacos, tienda y mástil con foco |
| v1 | Parapeto de sacos en U, tienda grande y torre de luz en remolque (4 focos) |
| v2 | **Por defecto.** Recinto de HESCO con tienda y mástil de antena con foco |
| v3 | Sacos y tienda bajo una red de camuflaje, con un foco en trípode |
| v4 | Dos tiendas pequeñas, un nido de ametralladora con techo y un mástil con foco |

## Escala y ejes
- 1 unidad = 1 m (exportador `exportar_unity`, `FBX_SCALE_ALL`). Al importar, deja Scale Factor en 1 y Convert Units activado, igual que con los demás bloques.
- Medidas de la v2: unos 14,3 × 16,4 m en planta (16,4 m incluyen la chicane) y 9 m de alto hasta la punta de la antena. Las demás variantes también ocupan unos 15 × 15 m.
- Ejes: la entrada mira a −Y en Blender, así que en Unity mira a **+Z** (`transform.forward`), con la misma convención que el resto de modelos.
- Sombreado plano (normales por cara) con las normales inclinadas hacia arriba (1,0), para que la sombra no caiga en la banda de la horda. No recalcules las normales al importar: deja Normals en Import.

## Origen
En el **suelo**, en el **centro del puesto** (no en el centro de la caja envolvente). Se coloca con y = 0 sobre el terreno, en el punto del mapa que ocupa el pelotón.

## Jerarquía y el hijo «Luces»
```
SM_PuestoFrente_vN_LODn   todo lo apagado (sacos, HESCO, tienda, mástil, cajas…)
└─ Luces                  los cristales de los focos; transformación identidad
```
- `Luces` tiene la posición, el giro y la escala en identidad: está colgado del padre en el origen, y su malla ya está en su sitio.
- **Emisión:** dale a `Luces` un material emisivo en crema **f0dc9c** (el mismo que las balizas del helipuerto y de las carreteras: nada de rojo ni ámbar). Enciéndelo de noche y apágalo (albedo f0dc9c sin emisión) de día. Si añades una luz puntual real, ponla en el cristal del foco:
  - v0, v2 y v4: un foco en el mástil que mira hacia la entrada (−Y de Blender, es decir, +Z de Unity) y algo hacia abajo, a unos 5,9 m de alto en v0 y v2 y a unos 4,9 m en v4.
  - v1: una barra de 4 focos a 7,4 m, en la torre del remolque.
  - v3: un foco en el trípode a 2,4 m.
- Triángulos de Luces: 12 (48 en la v1).

## Triángulos (v2)
LOD0: 1416 + 12 · LOD1: 1212 + 12. Las demás variantes tienen entre 2200 y 2500 en el LOD0 y entre 590 y 720 en el LOD1.

## Facción y contorno
El FBX lleva las propiedades de usuario `tbd_faccion = propio` y `tbd_rim = 1`, como las unidades propias, para tu AssetPostprocessor.

## Colores (por si los tocas en Unity)
- Sacos: 88885c.
- HESCO: 70784c, con el relleno de arriba en b4a080.
- Tienda: paredes en 70784c y techo en 847c34. La puerta va en 605c48 (lona recogida).
- Mástil y remolque: 6c7874. Cabezas de los focos: 48403c.
- Cajas: 605c48 sobre palés b4a080. Banderín: 70784c.

## Sin verificar
- **Forma:** la tienda está confirmada con las fotos de Paula K6_tienda_2 (tiendas modulares de pared baja y cumbrera) y la torre de luz con K7_foco_2 (torre Magnum en remolque).
- **Color de la tienda:** en las fotos la lona es beige, pero se queda en verde porque así se lee mejor; en beige desaparecería sobre el relleno de los HESCO y la explanada (Lucía, 7-nov). El color y las cotas de la tienda siguen SIN VERIFICAR para un despliegue concreto.
