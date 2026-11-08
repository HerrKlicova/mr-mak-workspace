# Icono de víveres (D-N176, quinto recurso de la red). Bruno (Arte técnico), 8-nov

**Ya existía y está aprobado**: es el de la familia A1 (cargas), la misma que la munición, el combustible, los materiales y la población. Lucía lo aprobó el 6-nov (D-N47/D-N50).

- **Panel de carga (TrenPanel, Iker)**: las cuatro de ahora (Munición, Combustible, Materiales y Personas) son A1, y la de víveres **ya está en el proyecto**: `Assets/TBD/Resources/Icons/cargas/vm_cargas_viveres_32.png` y `_16.png`, con su .meta. Se carga con `Resources.Load<Texture2D>("Icons/cargas/vm_cargas_viveres_32")`. Las demás son `vm_cargas_{municion,combustible,materiales,poblacion}_{32,16}`. Es una caja de madera con hogaza y lata, 6–10 colores y contorno de 1 px.
- **HUD (fila de recursos de la interfaz v2)**: como los víveres pasan a ser un recurso de la red, añado aquí `ui_recurso_viveres_{32,16}` con su .meta, en `Assets/TBD/Resources/Icons/noche/`, junto a ui_recurso_{municion,materiales,combustible}. Tienen los mismos píxeles que el A1 (comprobado), como el resto de ui_recurso_*. El generador es build_recursos_hud.py, que ya los incluye.
