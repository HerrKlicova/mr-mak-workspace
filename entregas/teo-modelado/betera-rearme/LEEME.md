# Zona de rearme de Bétera: camión cisterna y remolque de munición (Teo, 8-nov). Aprobado por Lucía (18:26).

`T_Paleta32.png` (URP/Lit, `_BaseMap` = paleta). Banda de la horda: 0 % en las 10 variantes. Sin rojo ni ámbar (la placa
naranja de mercancías peligrosas de la foto BT3 va lisa en gris claro). Medidas SIN VERIFICAR.

| Pieza | Variantes | Origen y medidas |
|---|---|---|
| `SM_CamionCisterna_v<n>_<Variante>` | Aparcado, Repostando (manguera de 7 m tendida hacia +X, boquilla y extintor de carro), Protegido (sacos terreros en +X y detrás), Averiado (cabina basculada, una rueda fuera), Quemado | 8,0 × 2,45 m, 3,4 m de alto. Largo a lo largo de Y con la cabina hacia −Y (como el VAMTAC). Origen en el suelo, en el centro |
| `SM_RemolqueMunicion_v<n>_<Variante>` | Cargado (cajas de munición), Cohetes, Descargando (lateral de +X abatido y cajas en el suelo hacia +X), Tapado (lona), Vacio (desenganchado, apoyado en la pata) | Remolque de un eje, 3,6 × 2,3 m con las ruedas; la lanza hacia −Y. Origen en el suelo, bajo el eje. Las cajas son las del `rearme_set` |

## Colocación (Lucía)
- **P1** (rearme en (172; 0; 104)): `Repostando` y `Descargando` (los v1 del camión y el v2 del remolque, o el v1 Cohetes), con
  el lado +X mirando al helicóptero, a unos 7 m de su centro: la manguera llega hasta él.
- **P2 y P3**: `Aparcado` y `Tapado` (v0 y v3).
- Mejora opcional para Iker, si sale barato: con un NH90 rearmando en P1, mostrar `Repostando` y `Descargando`; en reposo,
  `Aparcado` y `Cargado`. Las variantes comparten origen y huella, así que el cambio es solo de malla.
