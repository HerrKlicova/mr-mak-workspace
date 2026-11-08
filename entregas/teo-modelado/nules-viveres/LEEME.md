# Víveres de Nules: la huerta de naranjos · Teo, 8-nov

Para Álvaro (colocación, nules-nivel.md §13) y Marcos. Es un encargo de Lucía (decisiones-noche.md, 08-11 21:15) a partir del informe de Paula betera_rearme_y_nules_viveres_v1.md, y está **aprobado por Lucía (21:25)**. Hoja: /mnt/project-files/docs/arte/modelado-3d/nules-viveres/hoja_viveres_nules.png.

5 piezas × 5 variantes, en LOD0 y LOD1: `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas usan la misma `T_Paleta32.png`. Los ejes son los mismos que en el resto del kit:
- El origen está en el suelo, en el centro.
- Lo largo va a lo largo de X.
- La cara que da a la calle mira a −Y de Blender, que es +Z en Unity con yaw 0.

## Colisión y visión (D-N178)
- **Tapia: colisión de muro y corta la línea de visión.**
- Naranjos: **no** cortan la visión.
- La casa de labor es sólida, como las casas.
- Balsa y palots: lo que decida Álvaro.

| Carpeta | Variantes | Medidas (X × Y × alto) |
|---|---|---|
| Naranjos | Plantones, Jovenes, HileraJoven (4 en 15 m), HileraAdulta (3 en 10 m, marco de 5 m), Calva | Hilera de 16 × 3,9 × 3,8 m; adulto de ~3,6 m de copa |
| Tapia | Recto, Esquina (brazos de 5 m hacia −X y +Y), Porton (2,4 m), Roto, Contrafuertes (hacia −Y) | Módulo de 10 × 0,4 m y 2,2 m de alto (2,3 m con la albardilla) |
| CasaLabor | Encalada, Ocre, Porche (emparrado de 3 m en −Y), Abandonada, Cipreses (4) | Casa de 10 × 8 m y 9,4 m de alto; los cipreses van en +X, hasta 12,5 m de ancho total |
| Balsa | Llena, Media, Vacia, Vallada, Rota (talud caído hacia +X) | Ø 16,4 m con el talud (vaso de Ø 14) y 1,45 m de alto |
| Palots | Pila2, Bloque (3 × 2 × 3), Fila (5), Volcados, ConFruta | Palot de 1,2 × 1,0 × 0,75 m, genérico gris |

Cantidades de Álvaro: unos 51 naranjos, 4 tapias (una Roto y otra Porton), 1 casa de labor y 1 balsa.

La fruta es pequeña y va en a86c50 (sin ámbar). Las fotos de Paula no son de Nules, así que son guía y no calco. Banda de la horda: 0 %. Auditoría OK en las 50 piezas. Medidas SIN VERIFICAR.

Código: TBD `claude/modelado-3d-skill`, `bloques/viveres_nules.py` (3ff4557).
