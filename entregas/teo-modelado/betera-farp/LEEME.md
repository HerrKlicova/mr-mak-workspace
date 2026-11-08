# FARP de Bétera · Teo, 8-nov

Para Álvaro (colocación) e Iker (Bétera). Es un encargo de Lucía (decisiones-noche.md, 08-11 21:15) a partir del informe de Paula betera_rearme_y_nules_viveres_v1.md, y está **aprobado por Lucía (21:25)**. Hoja: /mnt/project-files/docs/arte/modelado-3d/betera-rearme/hoja_farp_betera.png.

5 piezas × 5 variantes, en LOD0 y LOD1: `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas usan la misma `T_Paleta32.png`. Ejes como el resto del kit: origen en el suelo, en el centro; lo largo va a lo largo de X; −Y de Blender es +Z de Unity con yaw 0. Ninguna pieza lleva colisión y nada debe pisar el claro de 25 × 25 m.

| Carpeta | Variantes | Medidas (X × Y × alto) |
|---|---|---|
| CisternaFlexible | Llena, Media, Vacia, SinBorde, Doble | Berma de 7,2 × 5,45 m (Doble: 9,0); con la manguera de salida, que va hacia +X, 11,3 × 5,9 × 1,4 m |
| Manguera | Recta (10,4 m), Curva, EseLarga, Enrollada, Boquerel | 0,18 m de grosor |
| Carrete | Patin, Lleno, Vacio, Tumbado, Bomba | 2,1 × 1,8 × 1,5 m |
| Sacos | Sueltos, Hilera3 (1,9 m), Hilera6 (3,9 m), Pila, **EnU** | U de 3,85 × 2,3 m abierta hacia +Y, de una hilada (0,26 m) |
| CajasMunicion | Cerrada, Abierta, Pila4, Pale (1,2 × 0,8 × 0,8), Vacias | Caja de 0,5 × 0,3 × 0,35 m, lisa (sin rótulo ni calibre) |

Colores: vejiga 6c7874, berma 847c34 (el amarillo de RA2, apagado), manguera 605c48, sacos d4d0cc/b8b8b8 y cajas 70784c/50541c. Sin rojo, sin ámbar y sin el color de selección. Banda de la horda: 0 %. Auditoría OK en las 50 piezas (25 × 2 LOD). Medidas SIN VERIFICAR.

Código: TBD `claude/modelado-3d-skill`, `bloques/farp_betera.py` (3ff4557).
