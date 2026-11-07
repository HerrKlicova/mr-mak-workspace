# Piezas nuevas para montar Castellón: torreta de vigilancia y talud del depósito (Teo, 7-nov)

Para Iker, que lleva las estaciones. La lista se cerró con Álvaro y Lucía la aprobó (09:17, con retoques ya hechos). Colocación: `docs/niveles/estaciones/castellon.json` de Álvaro.

Todas usan la misma `T_Paleta32.png`: un material URP/Lit con `_BaseMap` = paleta, igual que los vehículos y el kit. En todas, el origen está en el suelo y el frente mira a +Z de Unity con yaw 0. Las medidas son SIN VERIFICAR, porque no hay foto de ninguna de las dos.

## Torreta de vigilancia (SM_Torreta_vN)
- Mide 3,3 x 4,1 m en planta y 6,7 m de alto.
- El foco mira al frente, hacia fuera del recinto. Tiene un hijo «Luces» con el cristal del foco, para la emisión de noche, como el puesto de frente; la v4 no lo tiene.

| Variante | Uso |
|---|---|
| v2 Improvisada | Heredada de los supervivientes: las 4 esquinas de Castellón al empezar y las estaciones pequeñas |
| v1 Hesco | Junto a las 2 puertas (ramal y vehículos), y como mejora |
| v0 Acero | Estación Segura, por defecto |
| v3 Reparacion | En liberación y Liberada, con andamio |
| v4 Caida | Caída: vacía, inclinada y con el techo arrancado |

Posiciones (Álvaro): NO (67; 87) yaw 315, NE (219; 87) yaw 45, SE (215; 10) yaw 135, SO (67; 7) yaw 225, puerta del ramal (219; 49) yaw 90 y puerta de vehículos (67; 36) yaw 270.

## Talud del depósito (SM_TaludDeposito_vN)
- Módulo de 10 m a lo largo de Z de Unity con yaw 0, con 6 m de base y 2 m de alto. Los extremos son verticales para que casen los módulos.
- Variantes: v0 Liso (por defecto), v1 Sacos (mejora), v2 Erosionado, v3 Esquina (8 x 8 m; Álvaro no la usa en Castellón) y v4 Reventado (ataque al depósito o estación caída).
- Posiciones (Álvaro): 7 módulos al norte centrados en X 149–209, Z 28, con yaw 90; 2 al este en (217; 17) y (217; 25), con yaw 0.

## Comprobado
- Presupuesto y auditoría OK en LOD0 y LOD1 de las 10 variantes. Nada bajo L* 28 en lo propio.
- La tierra no usa 845c28, para que no se funda con el llano. Las normales van hacia arriba en la tierra, los sacos y el HESCO.

Código: TBD `claude/modelado-3d-skill`, `bloques/torreta.py` y `bloques/talud_deposito.py`, e11336d. Hojas: /mnt/project-files/docs/arte/modelado-3d/castellon-piezas/.
