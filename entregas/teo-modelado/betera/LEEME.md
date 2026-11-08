# Aeródromo de Bétera (D-N173): piezas nuevas · Teo, 8-nov

Para Iker. Siguen el §5 de `docs/niveles/betera-nivel.md` (Álvaro). **Aprobadas por Lucía (8-nov, 13:03)** con tres cambios, ya hechos:
- La torre y la garita tenían sombras en la banda de la horda (L* 9–13). Ahora la carpintería va en 6c7874 y el cristal en 605c48.
- La fachada de la torre pasa de d4d0cc a b8b8b8.
- El pino queda SIN VERIFICAR hasta que haya foto.

Además, el tronco del pino y el interior del hangar se han sacado de la banda. Medido sobre el LOD1 a tamaño de juego, ninguna pieza pasa del 1,7 % de píxeles en la banda. Las hojas están en /mnt/project-files/docs/arte/modelado-3d/betera/.

Cada carpeta tiene 5 variantes (`SM_<Pieza>_v0..v4_LOD0/LOD1.fbx`) y su `T_Paleta32.png`, que es la misma en todas: material URP/Lit con `_BaseMap` = paleta, como el kit. La variante la elige la semilla de cada instancia. Fuera es −Y de Blender, que en Unity es +Z con yaw 0. El origen está en el suelo.

| Carpeta | Pieza | Origen y orientación | Hijos animables |
|---|---|---|---|
| torre_control | Torre de control de 4 × 4 m, unos 12,7 m hasta la azotea (14,7 m en la v4). Sale de las fotos AE1. Variantes: foto, abandonada, fortificada, con caseta y radar, y alta | Centro del fuste. La escalera va en +X, la caseta de la v3 en −X | — |
| hangar | Hangar de 30 × 24 m, con bóveda de 10 m sobre muros de 6 m. Variantes: cerrado, entreabierto, a dos aguas, castigado y con red | Centro de la planta. El portón está en −Y (+Z en Unity): el nivel lo pone con yaw 0 | `Porton_O` y `Porton_E`: abrir = trasladar 12 m en X local hacia fuera (O a −X, E a +X) |
| tanque_combustible | Tanque horizontal de 12 × 3 m sobre cunas, con el eje a 2,1 m. Variantes: gris, verde, blanco, oxidado y con sacos | Centro, con el eje a lo largo de X | — |
| polvorin | Iglú semienterrado de 8 × 14 m y 4,2 m de alto, con las aletas hasta 14 m de ancho. Variantes: hierba, tierra, sacos, abierto con cajas, y red con venteos | Centro de la planta. La puerta está en −Y | `Puerta_O` y `Puerta_E` (bisagras en x = ∓1,5): abrir = girar −90° y +90° hacia fuera |
| valla_base | Tramo de valla de 10 m con malla de 2,5 m y el remate hacia fuera. Variantes: sana, combada, rota, con lona y con concertina suelta | Centro del tramo, a lo largo de X. Se repite cada 10 m: los postes van en ±1,25 y ±3,75, así que no se duplican | — |
| garita | Garita de 2,4 × 2,4 m con barrera de 6 m. Variantes: de obra, de chapa, con sacos, con marquesina y abandonada | Centro de la caseta. Ventana y barrera en −Y | `Barrera` (pivote en el poste): abrir = girar −80° sobre Y local |
| puerta_valla | Puerta principal de la foto AE1: hueco de 7 m, hojas de 2,2 m, pórtico de 5 m y placa del lema sin letras. Variantes: foto, sin pórtico, con chicane de sacos, con espino y forzada | Centro del hueco, a lo largo de X | `Hoja_O` y `Hoja_E` (bisagras en ∓3,5): abrir = girar +90° y −90° hacia dentro |
| pino | Pino carrasco, de 6 a 13 m, sin colisión. Variantes: típico, joven, inclinado, alto de dos pisos y medio seco | Pie del tronco | — |

- El helipuerto v4 (helipuerto/) es la toma P1. Las demás piezas del nivel son del kit (§5).
- Colores: nada rojo ni ámbar. SIN VERIFICAR: todas las medidas son estimadas, menos la forma de la torre, que sale de la foto. El pino está hecho de memoria.
- Auditoría y presupuesto OK en las 80 mallas.
- Pendiente de medir: los FPS con unos 200 pinos en instancing (betera-nivel.md §5).

Código: TBD `claude/modelado-3d-skill`, 2cd964c y c1f26dc (`bloques/torre_control.py`, `hangar.py`, `tanque_combustible.py`, `polvorin.py`, `valla_base.py`, `garita.py`, `puerta_valla.py` y `pino.py`).
