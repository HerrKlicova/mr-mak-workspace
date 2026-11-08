# D-N80 · Cinco siluetas de zombi · Teo, 8-nov

Para Bruno (shader TBD/Horda, entregas/bruno-horda-shader/) y Marcos (integración en la horda). **Aprobado por Lucía (8-nov, 23:55).** La hoja está en /mnt/project-files/docs/arte/modelado-3d/zombis-dn80/hoja_zombis_dn80.png.

| Archivo | Silueta | LOD1 (tris) | Qué la distingue |
|---|---|---|---|
| SM_Zombi_v3_Civil | civil | 192 | chaqueta abierta, brazos al frente desparejos (la base) |
| SM_Zombi_v18_Huerta | obrero de la huerta | 248 | sombrero de 0,40 de ala y azada al hombro que sobresale por detrás |
| SM_Zombi_v19_Uniformado | uniformado | 200 | erguido, casco y chaleco anchos, brazos colgando; sin armas |
| SM_Zombi_v17_Gordo | gordo y lento | 176 | barriga y piernas abiertas: ancho y bajo (12 px frente a 16) |
| SM_Zombi_v16_Rapido | descarnado y rápido | 144 | inclinado 38° a la carrera: el único en diagonal |

## Contrato con el shader de Bruno
- Una malla por silueta, un solo material (TBD/Horda). Sin UV y sin huesos: el andar va en el vértice.
- Máscara en el color de vértice «Col»: R = camisa y brazos; G = pantalón y objetos (sombrero, azada, casco, chaleco); B = piel, pelo y nuca; negro = calzado (#1c200c). El tono de cada instancia sale de horda_paleta_lut.png, toda en L* 9–13.
- El pivote está en los pies. Delante es −Y en Blender, que en Unity es +Z con yaw 0. El juego carga el LOD1.

## Comprobado
- **Forma:** medida con lamina_siluetas_horda.py de Bruno (TBD claude/sprites-importar) a ortho 26 y 55°, en 8 orientaciones y en 4 poses (base, andar1, andar2 y trepar). Los 10 pares son aptos: media ≤ 0,70 y máximo ≤ 0,80 (pares.csv). El más justo es civil/uniformado, con 0,68 de media y 0,79 de máximo. Lucía dice que si en la build se confunden, se exagera más el uniformado y no se toca el civil.
- **Banda:** en la horda de noche con el tinte de Bruno, el 68 % de los píxeles de zombi queda en L* 9–13. El resto es el sombreado del render (L* de 7,8 a 14,3). Sin rojo ni ámbar.
- Auditoría OK en LOD0 y LOD1, sin aristas no-manifold. Las variantes 0–15 de zombi_fino no cambian.
- Las poses de medida están en OBJ en /mnt/project-files/entregas/teo-horda-obj/ (TBD_POSE en el bloque).

Código: TBD `claude/modelado-3d-skill`, `bloques/zombi_fino.py` (7cef8b8).
