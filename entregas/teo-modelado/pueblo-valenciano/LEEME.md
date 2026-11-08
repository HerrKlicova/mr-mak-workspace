# Kit «Pueblo valenciano» y casa_pueblo r2 · Teo, 8-nov

Para Álvaro (colocación) y Marcos (zona de Sagunto). Sirve para que las dos hileras del pueblo, al norte del muro, dejen de ser 24 copias del mismo tipo de casa. **Aprobado por Lucía (8-nov, 19:14).** Hoja: /mnt/project-files/docs/arte/modelado-3d/pueblo-valenciano/hoja_pueblo_valenciano.png.

Cada pieza tiene 5 variantes en LOD0 y LOD1, con el nombre `<Pieza>/SM_<Pieza>_v<V>_<Nombre>_LODn.fbx`. Todas comparten la misma `T_Paleta32.png`. El origen está en el suelo, en el centro de la huella. La fachada mira a la calle en −Y de Blender (+Z en Unity con yaw 0) y las medianeras van lisas en ±X, como en casa_pueblo. El juego carga el LOD1.

## Casas (cambio de una en una)
Las cuatro tienen **la misma huella (6 × 10 m) y la misma colisión que casa_pueblo**, una caja de 6 × 10. Se pueden cambiar por una casa_pueblo cualquiera sin tocar las calles, el campo de tiro ni el balance. La casa de patio es más baja por delante, pero su colisión sigue siendo la caja.
| Carpeta | Variantes | Sugerencia |
|---|---|---|
| Esquina | DosPlantas, TresPlantas, BajoChaflan, CalAmarilla, Tapiada | En los extremos de cada hilera. El chaflán está en la esquina −X/−Y; para el extremo opuesto, gírala o usa la otra punta (sin escala negativa) |
| BajoComercial | Bar, Ultramarinos, Farmacia (sin cruz), Saqueada, Tapiada | 2 o 3 por hilera |
| TresAlturas | Cal, Ocre, Gris, Ropa, Ruina | Repartidas por las hileras |
| CasaPatio | Porton, Abierto, Parra, Naranjo, Derruida | En el borde del pueblo, hacia la huerta |

## Campanario (hito; NO colocar hasta que Álvaro diga dónde)
- Mide 25 m de alto, con una huella de 5 × 5 y zócalo de 5,6. Variantes: Ladrillo, Piedra, Reloj (reloj en −Y), Danado (remate caído al pie, en +X) y Andamio (en −Y).
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

Código: TBD `claude/modelado-3d-skill`, `bloques/pueblo_valenciano.py` (4a6040d) y `bloques/casa_pueblo.py`.
