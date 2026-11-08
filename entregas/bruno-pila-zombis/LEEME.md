# Pila de zombis: colocación en la zona (Bruno, 8-nov). Para Marcos

Las piezas son de Teo (`entregas/teo-modelado/pila-zombis/`, 0dd8b6a, aprobadas por Lucía) y el código de colocación es mío.
**SIN COMPILAR**: lo he escrito en la nube, sin Unity. Si no compila, pásame el error de la consola tal cual.

## Rama de TBD
`claude/pila-zombis` (f87f86c), **encima de** `claude/horda-dn80`: hay que fusionar primero la D-N80 o fusionar esta, que la incluye.
Solo añade `Assets/TBD/Scripts/View/PilaZombisSystem.cs` (+ .meta). No toca la simulación.

## Pasos del Editor (no se pueden hacer desde la nube por LFS)
1. Lo de la D-N80 primero (ver `entregas/bruno-horda-shader/LEEME.md`): los 5 FBX de los zombis y `sangre_rampa.png`.
2. Copiar las tres carpetas de Teo dentro de `Assets/TBD/Resources/Models/PilaZombis/`, con los mismos nombres:
   `celda/` (SM_PilaZombi_Altura<1-5>_s<0-2>_LOD<0|1>.fbx), `remate/` y `colision/`.
3. En el import de todos esos FBX: *Mesh Compression* en Off. El color de vértice se deja tal cual, **sin forzar el alfa a 1**,
   porque lleva la semilla de tono por cuerpo (241–255). Sin materiales importados (el código pone TBD/Horda). Sin colliders generados.
4. Al arrancar, la consola dice `[Pila] mallas de la pila cargadas…`. Si falta una celda, avisa con `[Pila] falta …` y no pinta pila,
   así que no rompe nada.

## Qué hace (PilaZombisSystem, PresentationSystemGroup, cada 0,1 s)
- Tramos: cada `Solid` de Kind 0 cerrado, quitando el tren. Se parte en celdas de 0,5 m por la cara de FUERA, que es la contraria al centro del fuerte.
- Cuenta por celda los zombis vivos que están a ≤ 1,5 m de la cara (PileRadiusMm). **Nota de Nacho:** si están subidos (y > 0,25 m),
  siguen contando hasta 4 m, así que el que trepa por la rampa no se sale de su celda.
- Altura según los umbrales de Nacho: 3 → Altura1, 4 → 2, 5 → 3, 6 → 4 y 7 o más → 5. Para que no parpadee, vuelve a sueltos solo por debajo de 2
  y cambia como mucho una vez por segundo.
- Semilla = índice de celda % 3. Tono por celda con `_HordaPack` (MaterialPropertyBlock); los cuerpos varían además con el alfa.
- Remates: RemateIzq en el borde −X de la primera celda de cada tramo seguido y RemateDer en el +X de la última, con su altura y semilla.
- Colisión: si están los `_COL`, se les pone un MeshCollider convexo, que solo sirve para clics y rayos de la vista. La simulación no usa
  la física de Unity: la pila de NightSim y la de la zona van por su cuenta (CellPile). No se ha convertido nada de UCX_, porque
  esa convención es de Unreal y Unity no la reconoce.
- Los zombis de una celda con pila dejan de dibujarse (`DisableRendering`) y vuelven a verse cuando la pila se deshace.
- Si cambian los tramos (una obra nueva o una brecha), se rehace toda la pila.

## Banderas
- `-sinpila` la apaga (para comparar en una captura).
- `-pilaalto 1.3` iguala el alto de las piezas a los zombis sueltos, que se dibujan a ×1,3 (D-N73). Por defecto va a escala real (1,0),
  así que si la pila se ve baja al lado de los sueltos, se prueba con 1.3. A lo largo siempre mide 0,5 m.

## Coste
El recuento recorre todos los zombis contra todos los tramos cada 0,1 s, en C# gestionado. Con -nightdense (10.000) puede
costar unos pocos ms: hay que mirarlo en el Profiler. Si pesa, lo paso a un job de Burst.
