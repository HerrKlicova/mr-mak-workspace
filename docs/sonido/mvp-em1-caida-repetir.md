# Sonidos del MVP: EM-1, «{Estación} ha caído» y «Repetir la noche» (para Iker)

Encargo de Lucía, 9-nov. Solo usa sonidos que ya están en `Assets/TBD/Resources/Audio`, así que no hay que generar nada nuevo. Lo he comprobado en `marcos/rodeo-edificio` (0d6469b).

| Momento | Sonido (ya en el juego) | Llamada | Vol. | 2D/3D | Cuándo | Ducking |
|---|---|---|---|---|---|---|
| **EM-1, aviso de emboscada** (mapa y zona) | `sfx_aviso_horda_1..6` (6 variantes; ahora no lo usa nadie) | `Sfx.Play("aviso_horda", Vector3.zero, 0.7f, 0.05f); Sfx.Duck(1.5f);` | 0,7 | 2D | Una vez cuando aparece el aviso EM-1 de ese tren. Como mucho uno por tren y día (como D-N39) | `Sfx.Duck(1.5f)`: el ambiente del mapa baja −6 dB, como con los demás avisos |
| **«{Estación} ha caído»** (cartel de derrota) | `sfx_estacion_caida_1..6` | Ya está: `PrototypeBootstrap.Night.cs:449`, `Sfx.Play("estacion_caida", Vector3.zero, 0.9f, 1f)` | 0,9 | 2D | Al salir el cartel. Vale para las tres causas (estación, tren o las dos) | Grupo «alerta»: baja el resto a 0,55 durante 1,5 s |
| **Botón «Repetir la noche»** | `sfx_ui_clic_1..9` | `Sfx.Play("sfx_ui_clic");` (igual que «Empezar» en `MainMenu.cs:61`) | 1,0 (GlobalGain 0,45) | 2D | Al pulsar, antes de `NetSession.Reset()` | No baja nada (grupo «ui») |

## Notas

- **EM-1:** no uso `sfx_ui_aviso_ambar`, porque ya es «Sin escolta / sin defensa» y se confundirían. Tampoco uso `sfx_alarma_ataque`, porque es la alarma de la noche en la zona. `sfx_aviso_horda` todavía no está medido en LUFS: si al oírlo tapa a los CO, bájalo a 0,5. Si no te da tiempo, la alternativa es `ui_aviso_ambar` a 0,6.
- **Prefijos:** `Sfx.Play(evento, pos, …)` pone `sfx_` delante, así que va sin el prefijo. `Sfx.Play(nombre)` usa el nombre exacto, así que va con el prefijo.
- **Pausa:** los tres respetan `AudioListener.pause`. Si el cartel de derrota pausa el juego antes de sonar, el sonido de caída tiene que ir antes de la pausa (ahora va así en `NightEnded`).
- **Mapa de mezcla completo:** `docs/sonido/mezcla-mvp.md` (en la carpeta del proyecto).

— Nuria (Sonido)
