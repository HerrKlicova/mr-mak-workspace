# Vehículos con acabado de camuflaje en el albedo (Teo, 7-nov)

Encargo del coordinador (08:53): Eugenio vio el Dragón, el VAMTAC y el NH90 sin textura en la build.

## Por qué salían planos
- El FBX de la build está bien: tiene un material (MAT_Paleta32), la textura de la paleta (filtro de punto, sin mips) y la capa de UV en el centro de cada texel. `PrototypeBootstrap.Vehicles.cs` asigna bien `_BaseMap` = T_Paleta32 en URP/Lit.
- La primera causa es que el albedo del casco solo tenía dos valores (techo b4a080 y costados 50541c).
- La segunda causa es que la build lo aplana con el doble sRGB y el cuantizador al 65 % (D-N129 §0). **Eso está pendiente de tu lado:** hay que quitar el doble sRGB de `_lowRt` y poner el cuantizador del mundo a 0, sin tramado.

## Qué hay
- `dragon/`, `vamtac/` y `nh90/` llevan el acabado **0 boscoso**, que **va por defecto** (Lucía, 09:04).
  - Los archivos se llaman igual que en `Assets/TBD/Resources/Models/Vehiculos/<carpeta>/`, así que basta con sustituirlos.
  - T_Paleta32.png es idéntica, píxel a píxel, a la que ya hay.
- La jerarquía y los nombres de los hijos son los mismos: Rueda_*, Torre/Canon, Aro/Ametralladora, RotorPrincipal/RotorCola/DiscoRotor. La geometría no cambia; solo hay más caras en el casco por los cortes del camuflaje.
- `<carpeta>/acabados/` tiene los 5 acabados en LOD0 y LOD1: v0 Boscoso, v1 Liso (el de antes), v2 Árido, v3 Embarrado y v4 Urbano. Los otros cuatro se quedan en el paquete; Lucía decidirá más adelante para qué se usan.
- Nota: los pivotes del Dragón se mueven unos 11 cm a lo largo del vehículo respecto a la copia que tienes, y los del NH90 unos 6 cm. El acabado liso, que sale del mismo código, da lo mismo, así que la copia de la build es de una versión anterior. Los nombres y la jerarquía no cambian.

## Comprobado
- Presupuestos OK en los 15. El NH90 mantiene el aviso de las 16 aristas de borde del disco del rotor, como antes.
- Ningún albedo propio está bajo L* 28 (D-N80). Ningún costado usa colores de suelo ni de zombi.
- El costado pardo es 605c48. Bruno pidió cambiar el 6c4038 porque en sombra caía en la banda de la horda. Él proponía 845c28, pero ese no puede ir de costado porque es el llano; queda pendiente que confirme el 605c48.

Código: TBD `claude/modelado-3d-skill`, commits 64b8beb y de0f270 (`bloques/acabado.py`).
Hojas: /mnt/project-files/docs/arte/modelado-3d/vehiculos-acabados/.
