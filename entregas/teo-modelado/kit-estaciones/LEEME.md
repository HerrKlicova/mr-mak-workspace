# Kit modular de estaciones (Teo, 7-nov; aprobado por Lucía a las 08:35)

Encargo de Eugenio: que todas las estaciones reutilicen los assets de Sagunto, combinados de otra manera, y que todas se puedan visitar y atacar. Los módulos comparten la misma lista de materiales y la misma `T_Paleta32.png`, así que puedes instanciarlos juntos sin rehacer la paleta. Medidas SIN VERIFICAR (no hay planos).

## Módulos (`modulos/`, LOD0 y LOD1)
El origen es el centro de la planta, en el suelo, y el frente mira a la vía (+Z en Unity).
- **SM_KitAnden_v0–v5**: tramo de 10 m (9,98 m) y 4 m de fondo, a 0,68 m. Variantes: 0 lateral con banda; 1 bajo (0,38 m); 2 roto; 3 rampa; 4 bordillo y juntas; 5 isla central.
- **SM_KitMarquesina_v0–v5**: tramo de 6 m. El origen está en la cara de arriba del andén, así que súbelo 0,68 m. Variantes: 0 celosía de Sagunto; 1 voladizo; 2 a dos aguas (isla); 3 sin chapa; 4 hundida; 5 hormigón.
- **SM_KitCuerpo_v0–v6**: módulo de edificio de 4 m (3,98 m) que se encadena en X. Los FBX tienen fondo 9 m. Variantes: 0 Sagunto 2 plantas; 1 Nules 2 plantas; 2 Nules 1 planta; 3 Sagunto 1 planta; 4 tapiado; 5 taquilla; 6 tres plantas.
- **SM_KitRemate_v0–v5**: frontón, hastial escalonado de Nules, torreta, ala terraza, pórtico y testero con chimenea.
- **SM_KitSueltas_v0–v7**: banco, farola, cartel (banda para el decal), papelera, carro, caseta de enclavamiento, **escombro** (estado Caída) y **andamio** (estado Liberada).

**Ojo con el fondo:** Nules usa cuerpos y remates de 8 m de fondo y Castellón de 13 m, y los FBX sueltos tienen 9 m. Para esos dos, o escalas el módulo en Z de Unity (fondo/9) o usas el FBX del montaje. Si prefieres FBX por fondo, te los saco.

## Montajes de prueba (`montajes/`, una sola malla por estado)
Estados de la D-N124:
- **Nules** (apeadero): v0 abandonada (estado inicial), v1 Segura, v2 En liberación, v3 Caída, v4 Liberada.
- **Castellón** (principal): v0 Segura, v1 Asediada, v2 Caída, v3 Liberada.

El origen es el centro del edificio en la línea de su fachada (Nules X 130 / Z 74 y Castellón X 130 / Z 75 de los niveles de Álvaro), con la vía hacia -Z de Unity.

## Instancias (`instancias/estacion_<e>_v<n>.json`)
Es la lista de módulos de cada montaje: prefab, posición y giro, con `parametros` cuando el fondo no es 9 m. Para el juego lo bueno es instanciar módulo a módulo. La conversión a Unity (`pos_unity` = (-x, z, -y) de Blender y `giro_y_unity` = -giro) sale de la convención que mediste (Blender -Y → Unity +Z) y está **SIN VERIFICAR en Unity**: compárala la primera vez con el FBX del montaje de la misma variante.

Colores: el granate 642030 sube a 8c5048 en el LOD1 (Lucía) y las fachadas d4d0cc quedan como mucho en L* 75 en la vista de juego. Scripts en TBD (bloques/kit_*.py, estacion_*.py), commit f8eb0d3.
