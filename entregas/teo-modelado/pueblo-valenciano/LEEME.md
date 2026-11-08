# Kit «Pueblo valenciano» y casa_pueblo r2 · Teo, 8-nov

Para Álvaro (colocación) y Marcos (zona de Sagunto). Sirve para que las dos hileras del pueblo, al norte del muro, dejen de ser 24 copias del mismo tipo de casa. **Aprobado por Lucía (8-nov, 19:14).** Hoja: /mnt/project-files/docs/arte/modelado-3d/pueblo-valenciano/hoja_pueblo_valenciano.png.

Cada pieza tiene 5 variantes en LOD0 y LOD1, con el nombre `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas comparten la misma `T_Paleta32.png`. El origen está en el suelo, en el centro de la huella. La fachada mira a la calle en −Y de Blender (+Z en Unity con yaw 0) y las medianeras van lisas en ±X, como en casa_pueblo. El juego carga el LOD1.

## r2 (8-nov, 23:15): fachadas según las fotos de Sagunt
**Aprobada por Lucía (8-nov, 23:15).** Hoja: /mnt/project-files/docs/arte/modelado-3d/pueblo-valenciano/hoja_pueblo_valenciano_r2.png. Las fotos de Paula (referencias-reales/sagunt_calles) se han usado solo como guía: no se ha calcado ninguna fachada.
- Mismos nombres de archivo, medidas, pivotes y colisión que la r1. Marcos solo tiene que sustituir los FBX. **Única excepción:** `Campanario/SM_Campanario_v1_Piedra_*` desaparece y su sitio lo ocupa `SM_Campanario_v1_Silleria_*`.
- Zócalo de 1,2 m que cambia según la casa: 605c48, gris 94948c o verde azulado 6c7874 (L* 49, lejos del d4d0cc de selección). En tres casas la cal es crema b4a080 (Esquina TresPlantas, BajoComercial Farmacia y CasaPatio Porton).
- La forja de los balcones (pasamanos, pletina y barrotes) y las rejas de barrotes de la planta baja solo están en LOD0. Las persianas enrollables con su cajón están en LOD0 y en LOD1.
- **Balcones, rejas y persianas son solo fachada:** no añaden colisión y no cambian la línea de visión (D-N174).
- **Campanario v1 Silleria**: torre de sillería b4a080 al estilo de El Salvador. Tiene un vano de medio punto por cara, terraza plana con pretil y ningún chapitel, y mide unos 24 m. Es decorado. Su sitio lo decide Álvaro. La v2 Reloj, que ya está colocada, no cambia de forma.
- Auditoría OK en LOD0 y LOD1 de las 25 piezas, sin aristas no-manifold. Banda de la horda: 0 %. El LOD0 tiene como máximo 1508 triángulos.

## Casas (cambio de una en una)
Las cuatro tienen **la misma huella (6 × 10 m) y la misma colisión que casa_pueblo**, una caja de 6 × 10. Se pueden cambiar por una casa_pueblo cualquiera sin tocar las calles, el campo de tiro ni el balance. La casa de patio es más baja por delante, pero su colisión sigue siendo la caja.
| Carpeta | Variantes | Sugerencia |
|---|---|---|
| Esquina | DosPlantas, TresPlantas, BajoChaflan, CalAmarilla, Tapiada | En los extremos de cada hilera. El chaflán está en la esquina −X/−Y; para el extremo opuesto, gírala o usa la otra punta (sin escala negativa) |
| BajoComercial | Bar, Ultramarinos, Farmacia (sin cruz), Saqueada, Tapiada | 2 o 3 por hilera |
| TresAlturas | Cal, Ocre, Gris, Ropa, Ruina | Repartidas por las hileras |
| CasaPatio | Porton, Abierto, Parra, Naranjo, Derruida | En el borde del pueblo, hacia la huerta |

## Campanario (hito)
- **Colocado por Álvaro (19:16): (118; 0; 128), v2 Reloj, yaw 180** (mira al fuerte). Queda detrás de la hilera trasera, que es continua en X 96,5–143,5, así que no cruza ninguna línea de tiro hacia los accesos. Las instancias de las casas están en docs/niveles/sagunto_pueblo_instancias_v1.csv (§10.19).
- Mide 25 m de alto, con una huella de 5 × 5 y zócalo de 5,6. Variantes: Ladrillo, Silleria (r2, antes Piedra), Reloj (reloj en −Y), Danado (remate caído al pie, en +X) y Andamio (en −Y).
- Condiciones de Lucía:
  - Álvaro lo coloca fuera de las líneas de tiro hacia los accesos del muro (D-N174). Si se cruza con alguna, Nacho mide antes de que entre.
  - **Es decorado**: no es un puesto de tirador ni se puede usar.

## casa_pueblo r2 (sustituye a la del PC, mismos nombres)
- `casa_pueblo/SM_casa_pueblo_v0–v5_LODn.fbx`, con los mismos nombres y la misma geometría que la entrega del 6-nov (C:\Dev\mr-mak-workspace\sagunto\casa_pueblo).
- Solo cambian los colores. La carpintería pasa de 543820 a 605c48: en sombra, el 543820 caía al 9 % en la banda de la horda (L* 9–13), y Lucía lo da por fallo de la build actual. La reja pasa de 48403c a 6c7874, y el zócalo de las v2 y v5, de 283440 (valor de la horda) a 6c7874.
- Marcos: basta con sustituir los FBX.

## Comprobado
- Auditoría OK en LOD0 y LOD1 de las 31 piezas (25 + 6). Banda de la horda: 0 % en todas.
- SIN VERIFICAR: las medidas son de memoria, porque Paula no tiene fotos de calles del pueblo.

Código: TBD `claude/modelado-3d-skill`, `bloques/pueblo_valenciano.py` (r1 4a6040d, r2 7be10a8) y `bloques/casa_pueblo.py`.
