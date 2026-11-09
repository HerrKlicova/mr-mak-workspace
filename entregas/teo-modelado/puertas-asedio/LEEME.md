# Puertas para el asedio (D-N151) · Teo, 9-nov

Para Marcos, Iker y Nacho. Encargo de Lucía (8-nov, 23:48). Durante el asedio, las puertas del tren y de vehículos se cierran del todo y funcionan como un tramo de muro más. Hoja: /mnt/project-files/docs/arte/modelado-3d/puerta-via/hoja_puertas_asedio.png.

**Aprobado por Lucía (9-nov, 26:05)**, con el cambio de que la puerta de vehículos abre hacia dentro.

**Resumen.** Los tres modelos de puerta ya traían 5 variantes × 4 estados de daño y pivotes en las bisagras. Ahora añado:
- la tabla de ángulos de abierta, a medio cerrar y cerrada;
- **una colisión por modelo** que gira con las hojas;
- la colocación de la pila de zombis delante de la puerta cerrada.

**No hay portillo.** Álvaro lo ha confirmado (8-nov, 23:50): con la estación sitiada, la tropa aparece ya dentro y fuera y no sale a pie. Ha corregido la línea antigua de nules-nivel.md.

## Qué puerta va en cada sitio (Álvaro)
| Estación | Puerta | Modelo | Hueco | Dónde |
|---|---|---|---|---|
| Sagunto | Vía oeste | `SM_PuertaVia` (puerta-via/) | 5 m | Z 62,9–66,1, yaw 270 |
| Sagunto | Vía este (solo visual en el MVP) | `SM_PuertaVia` | 5 m | muro este, yaw 90 |
| Sagunto | Vehículos sur E4 | `SM_PuertaVehiculos` (muro-estados/puerta_vehiculos/) | 8 m | X 95–103, yaw 180 |
| Sagunto | Vehículos oeste-sur | `SM_PuertaVehiculos` | 8 m | (70; 0; 53), yaw 270, hueco Z 49–57 |
| Nules | Vía doble oeste | `SM_PuertaViaDoble` (nules/puerta_via_doble/) | 7,4 m | Z 60,8–68,2, yaw 270 |
| Nules | Vía del apartado oeste | `SM_PuertaVia` | 5 m | Z 46,5–51,5, yaw 270 |
| Nules | Vía doble este | `SM_PuertaViaDoble` | 7,4 m | yaw 90 |
| Nules | Vehículos sur | `SM_PuertaVehiculos` | 8 m | X 177,22–185,22, yaw 180 |

Fuera es +Z de Unity con yaw 0. El origen está en el suelo, en el centro del hueco.

## Abrir y cerrar: pivotes y ángulos
La jerarquía no cambia: la raíz (jambas) tiene dos hijos, `Hoja_O` y `Hoja_E`, y cada uno tiene el origen en su bisagra. Se giran sobre la vertical local.

| Modelo | Bisagra de Hoja_O / Hoja_E (Unity, x) | Abre hacia | Cerrada | A medio cerrar | Abierta |
|---|---|---|---|---|---|
| SM_PuertaVia (5 m) | +2,49 / −2,49 | dentro | 0° | O +45°, E −45° | O +90°, E −90° |
| SM_PuertaViaDoble (7,4 m) | +3,69 / −3,69 | dentro | 0° | O +45°, E −45° | O +90°, E −90° |
| SM_PuertaVehiculos (8 m) | +3,99 / −3,99 | **dentro** | 0° | O +45°, E −45° | O +90°, E −90° |

- **Las tres abren hacia dentro** (Lucía, 9-nov 26:05). Hacia fuera, la puerta de vehículos chocaba con la horda y con la pila justo cuando los vehículos salen a atacar (señal `vehiculos_fuera` del tutorial). **Cambia respecto al LEEME de muro-estados: la de vehículos ya no gira O −90° y E +90°, sino O +90° y E −90°.** Signos comprobados en Blender. La hoja tiene que barrer hacia dentro del recinto. Si en Unity sale al revés, se cambia el signo de las dos hojas. **SIN VERIFICAR en Unity.**
- La x de la bisagra va en ejes de Unity (Hoja_O está en −X de Blender, que es +X de Unity con yaw 0). Lo más sencillo es girar el `localRotation` del hijo y no hacer la cuenta.
- A medio cerrar es un paso del giro. Con 0,25 s de animación (como el paso de reposo a apuntando) no hace falta malla propia.

## Colisión (`colision/`)
`SM_PuertaVia_Col.fbx`, `SM_PuertaViaDoble_Col.fbx` y `SM_PuertaVehiculos_Col.fbx` tienen **la misma jerarquía y los mismos pivotes que la puerta visible**:
- la raíz son las dos jambas (cajas de 0,9 × 1,2 m);
- `Hoja_O` y `Hoja_E` son una caja cada una, de la bisagra al centro.

Todas miden 2,1 m de alto, como el muro y la pila. Son cajas de 6 caras, sin material.
- **Cerrada (0°):** bloquea de jamba a jamba, sin rendijas (las dos cajas de las hojas se tocan en x = ±0,01).
- **Abierta (±90°):** deja libre el hueco. Para eso hay que girar las hojas de colisión con los mismos ángulos que las visibles: lo más fácil es meter el FBX de colisión como hijo de la puerta y girar a la vez los `Hoja_*` de los dos.
- **Estados:** en Sano, Dañado y Muy dañado (e0–e2), las hojas de colisión están activas: una puerta dañada sigue cerrando. En Brecha (e3) se desactivan las dos hojas y quedan solo las jambas.
- En la simulación (NightSim), el sólido de la puerta cerrada es el tramo de muro de la D-N151, con su vida. Las cotas son estas cajas. Es lo que falló en qa20: la puerta cerrada no tenía sólido.

## La pila de zombis delante de una puerta cerrada
- La cara de fuera de las hojas (y de la caja de colisión) está en **y = −0,16** de Blender, es decir, 0,16 m hacia fuera del centro del muro. La del HESCO está en −0,55. **Delante de una puerta, las celdas de la pila van con el origen en y = −0,16, 0,39 m más adentro que delante del muro.** Las alturas (2,1 m de muro) son las mismas.
- **Arreglo en la pila (pila-zombis/, ya sustituida):** las celdas y los remates entregados tenían el origen en el centro de su caja y no al pie del muro, como decía el LEEME. Así quedaban metidos 1,3–1,9 m en el muro. Ya están corregidos: el origen está al pie de la cara de fuera (y = 0), y la pila baja hacia fuera. Las colisiones de la pila ya estaban bien.

## Otros cambios
- Puerta de vehículos (muro-estados/puerta_vehiculos/, las 5 variantes): como ahora abre hacia dentro, en Muy dañado (e2) la hoja que cuelga y en Brecha (e3) los trozos caen hacia dentro, igual que en las puertas de vía. Se han sustituido las e2 y las e3; las e0 y las e1 no cambian (comprobado).
- La placa del pórtico de la v4 (Blindada) estaba en #d4d0cc, el hueso reservado para la interfaz (Bruno, 8-nov). Pasa a #b8b8b8. Se han sustituido las v4 de las tres puertas (12 FBX por LOD, con mallas idénticas; solo cambian las UV de la placa). En las puertas de vía, la placa son los aisladores del LOD0, así que su LOD1 no cambia.

Código: TBD `claude/modelado-3d-skill` 0c44aad y fd10748 (`colision_puertas.py`, `bloques/puerta_estados.py`, `bloques/pila_zombis.py`).
