# H1 exigente · Mundo8 (marcos/mundo-zum, con nacho/hito1 dd639af8: recarga desde Red.Sacar) · Marcos, 12-11
- A: `TBD.exe -mundo -guion -grabar -turbo 4 -salir-en 18300 -hashlog hash_H1_A.txt` (con ventana).
- B: `TBD.exe -mundo -reproducir mundo_grabacion.txt -turbo 4 -salir-en 18300 -hashlog hash_H1_B.txt` (con ventana), con `mundo_hash_ref.txt` = hash_H1_A.
- Comparador de Sara: `desync=False · ticks comunes: 18301 (del 0 al 18300)`. Los dos ficheros son idénticos byte a byte.
- Log de B: `desync=False · 18301 ticks comparados`, final `tick 18300, abatidos 50, bajas 8, hash 6ca6db91ab959091` (el mismo que A).
- Grabación: 25 órdenes de 10 tipos (Mover 5, AtacarMoviendo 2, Parar, Formación, FuegoLibre 2, PuntoVia 6, TrazarVia 2, NuevaLinea, AsignarTren 3, NuevoTren 2).
- La red: «vía trazada: tramo 0, 108 piezas, 1233 m, 1 paso a nivel; 28 curvas»; el trazado inválido, rechazado («Cruce demasiado sesgado, 29°»); «A y B unidas… el tren sale».
- Valores distintos de cada sistema en 18.301 ticks: reloj 18301, unidades 18301, zombis 18301, red.trenes 18206, red.almacen 20, red.cargas 16, red.trazos 6, **red.via 2** (cambia una vez: al trazar).
- Lo que NO entra: borrar un tramo con el tren en marcha (no hay orden de borrar vía en la red de Iker) y añadir el depósito a la línea (sin orden). La recarga de Nacho: no hay línea de log que la confirme; en el hash, red.almacen cambia 20 veces.
