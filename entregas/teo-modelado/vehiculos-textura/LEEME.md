# Vehículos con textura horneada a partir de fotos reales (Teo, 7-nov)

Para Marcos. **Sustituye a `vehiculos-acabados/` (cf2f07a), que queda anulado.** Eugenio vio que el camuflaje por caras parecía tener parches, así que ahora cada vehículo lleva pintura lisa verde OTAN con una textura horneada de 768 x 512. La textura tiene juntas de chapa, remaches, el sol en el techo, polvo, suciedad baja con el borde irregular, barro y desgaste de aristas. Las referencias son fotos de Paula en `referencias-reales/` (vehiculos, aereo y superficies). Lucía lo aprobó a las 09:33.

## Qué hay
- `dragon/`, `vamtac/` y `nh90/` llevan el uso **1 de campaña, que va por defecto**. Los nombres coinciden con `Resources/Models/Vehiculos/<carpeta>/`, así que basta con sustituir los dos FBX y `T_Paleta32.png`.
  - **Ojo:** `T_Paleta32.png` ya no es la paleta, sino la textura del vehículo. El nombre se mantiene para que `MakeVeh` no cambie: sigue siendo un material por carpeta, con `_BaseMap` = esa textura.
  - El LOD0 ocupa la mitad izquierda y el LOD1 el cuadrado de abajo a la derecha, así que comparten un solo archivo.
  - Importa la textura con filtro Point, sin mipmaps, sin compresión y en sRGB, igual que antes.
- `<carpeta>/usos/` tiene los 5 grados de uso, cada uno con sus FBX y su textura: v0 Parque, v1 Campaña, v2 Árido, v3 Embarrado y v4 Castigado. La UV de cada carpeta va con su propia textura, así que no mezcles archivos de carpetas distintas.

## Corregido: cañón y ametralladora bajo el suelo
El exportador FBX de Blender, con bake_space_transform, escribía mal el segundo nivel de la jerarquía. **El `Canon` (bajo `Torre`) y la `Ametralladora` (bajo `Aro`) salían girados 90° y metidos bajo el suelo.** Les pasaba también a las entregas anteriores, y seguramente por eso en la captura de Eugenio no se ve el cañón.
- Ahora están en su sitio, con la rotación local a cero. Lo he comprobado reimportando: el Canon queda a 2,7–3,0 m de alto, delante de la torre.
- Los nombres y la jerarquía son los mismos: Rueda_*, Torre/Canon, Aro/Ametralladora, RotorPrincipal/RotorCola/DiscoRotor.

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de los 15. Quedan los mismos avisos de antes: el VAMTAC LOD0 tiene 1202 triángulos y el disco del rotor del NH90 tiene 16 aristas de borde.
- Los colores de la textura están cuantizados a la paleta, sin tramado, sin violetas de la horda y sin el llano 845c28. Nada queda por debajo de L* 28.
- Los cristales son 48403c, de la familia oscura 303424: el 60546c salía de noche como una raya azul viva (Lucía, 09:40).
- Hay una prueba de noche con la luz v3 a la escala de la captura (hoja_noche_escala_captura.png). **SIN VERIFICAR:** es una aproximación con mi render, no la build, y lo que vale es la captura de la Noche24 con el color de D-N129 ya corregido.

Código: TBD `claude/modelado-3d-skill`, `textura_real.py` y el arreglo del FBX en `malla3d.py` (924a82c y a8fe988).
Hojas: /mnt/project-files/docs/arte/modelado-3d/vehiculos-textura/.
