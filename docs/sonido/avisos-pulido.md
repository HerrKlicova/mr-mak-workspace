# Sonidos de los avisos del pulido (Nuria, 11-nov, para Iker)

Encargo de Lucía (`docs/pulido-hasta-19.md`). He medido los niveles en el repo (`git lfs pull` y ebur128). Nivel efectivo = LUFS del archivo + 20·log10(vol). Referencia: la alarma de ataque da −19,3 LUFS (−14,9 a 0,6).

Rama de tbd: **`nuria/avisos-pulido`**, sobre main 16:47. Sin compilar. Solo vista.

| Aviso | Archivo (ya en el repo) | Llamada | Vol. | Efectivo | Estado |
|---|---|---|---|---|---|
| **EM-1, emboscada** (mapa) | `sfx_aviso_horda_1..6` (−14,4 a −17,3 LUFS) | `OperationsMap3D` (ya estaba) | **0,7 → 0,45** | −21,8 | ✅ en la rama. A 0,7 sonaba más fuerte que la alarma (−18,0) |
| **EM-1, emboscada** (zona) | igual | `PrototypeBootstrap.Emboscada.cs`, junto al `HintMsg` de EM-1: `Sfx.Play("aviso_horda", Vector3.zero, 0.45f, 5f); Sfx.Duck(1.5f);` | 0,45 | −21,8 | ✅ en la rama. Una vez por emboscada (D-N199) |
| **«{Estación} ha caído»** (zona) | `sfx_estacion_caida_1..6` (−15,1 a −16,7) | `NightEnded` (ya estaba) | 0,9 | −16,8 | ✅ sin cambios. Es el momento más fuerte, a propósito |
| **«{Estación} ha caído»** (mapa o registro, si la noche termina fuera de la zona) | igual | **Iker**, donde salga ese aviso: `Sfx.Play("estacion_caida", Vector3.zero, 0.6f, 5f); Sfx.Duck(3f);` | 0,6 | −20,3 | ⏳ falta el sitio. Solo cuando ocurre, nunca al volver a entrar (D-N199) |
| **Llega el socorro al cerco** (D-N196) | `sfx_tren_bocina_1..6` (−14,4 a −18,0; no se usaba) | `TrenPanel.Vigilar()`, donde la tropa baja sola | mapa 0,3 / zona 0,5 | −26,8 / −22,3 | ✅ en la rama. Bocina del tren que llega y, después, el combate de siempre |
| **Reserva por debajo de 47 u** | `sfx_municion_baja_1..5` (**normalizados a −24 LUFS**: antes iban de −21,4 a −28,7; la 6 queda fuera porque no daba nivel) | **Iker**, donde salga el aviso: `Sfx.Play("municion_baja", Vector3.zero, 0.6f, 10f);` | 0,6 | −28,4 | ⏳ falta el aviso. Suena al bajar de 47 y no vuelve a sonar hasta que pase otra vez de 47. Es del grupo «alerta», así que baja el resto 1,5 s |
| **Puerta E4, se abre** (D-N198) | `sfx_puerta_e4_abrir_1..5` (**nuevo**) | **Iker**, al cambiar el estado: `Sfx.PlayAt("puerta_e4_abrir", new Vector3(99f, 0f, yMuroSur), 1f, 2f);` | 1,0 | −24 a pie de puerta | ⛔ falta generar (créditos) |
| **Puerta E4, se cierra** (al anunciarse el asedio) | `sfx_puerta_e4_cerrar_1..5` (**nuevo**) | igual, con `puerta_e4_cerrar` | 1,0 | −24 | ⛔ falta generar |

Mientras no existan los archivos de la puerta, `Sfx` no encuentra el clip y no suena nada (no da error). Iker puede dejar puestas ya las dos llamadas.

## Puerta E4: lo que falta

Script: `herramientas/sonido/puerta_e4.py`. Pide 6 tomas de 5 s de cada sonido y se queda con las 5 mejores (descarta las mudas o las que no tienen golpe final). Las deja a −24 LUFS en mono, en `entregas/sonido-puerta-e4/`. Gasta unos **720 créditos** (tope de 900) y no reintenta ninguna llamada. **Lo tiene que lanzar Eugenio en el PC**, porque desde la sesión el control de permisos bloquea las llamadas de pago:

```
cd C:\Dev\mr-mak-workspace
git pull
python herramientas\sonido\puerta_e4.py
```

Después, copiar los 10 OGG a `Assets/TBD/Resources/Audio` (o decírmelo y los subo yo a la rama).

— Nuria (Sonido)
