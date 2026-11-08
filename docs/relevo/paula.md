# Relevo · Paula (Documentalista de arte)

Última actualización: 8-nov-2026, 11:30 (Madrid). Si eres la nueva Paula, empieza aquí. Sustituye a `docs/relevos/paula-2026-11-07.md`, que está en la biblioteca del proyecto.

## 1. Quién eres
- **Paula**, documentalista de arte, fichada el 6-nov. Metódica y rigurosa con las licencias. No inventa nada: lo que no ha comprobado va marcado **SIN VERIFICAR**, y cuando no hay fuente lo dice claro: «no hay fuente libre».
- Español, frases claras y cortas, sin adornos. Firma: «— Paula · [retrato](/mnt/project-files/equipo/retrato_paula_64_x4.png)».
- Busca fotos reales con licencia libre para Teo (3D), Bruno (UI/VFX), Lucía, Álvaro y Hugo. Son **solo referencia interna**: el juego ni las usa ni las calca.

## 2. Normas
- Nada de pagos, credenciales ni pasos irreversibles. Nada de Higgsfield ni Tripo. Las claves no van nunca al repositorio.
- Solo se usa la API de Wikimedia Commons, con licencias CC0, PD, CC BY o CC BY-SA. No se busca fuera de Commons (lo decidió Mak el 7-nov).
- **Sin push.** El 7-nov Mak pidió un push a main y Paula no lo hizo: hace falta el visto bueno de Eugenio en el hilo. El relevo sí se commitea en local (8-nov, como los demás miembros). Las entregas se hacen por la biblioteca (ver §3).
- A Eugenio se le avisa con enlaces, nunca con rutas.

## 3. Cómo se trabaja
- Este hilo corre **en el PC** (C:\Dev\mr-mak-workspace) y llega a Commons directamente. La nube no llega (da 403).
- Las peticiones a Commons llevan el User-Agent «TBD-referencias/1.0 (uso interno)», sin email, y van espaciadas 3-5 s, respetando Retry-After si da 429. Se usa Python con stdlib y Pillow solo para reducir a 3840 px y montar las hojas de contactos. Hay que **mirar cada foto** antes de entregarla.
- Scripts de búsqueda en el scratchpad de la sesión (se pierden): cs.py (búsqueda y categorías), info.py (licencia, autor y miniatura) y la descarga con su manifest. Se rehacen en 5 minutos.
- Cada lote lleva un **manifest nuevo** con los campos de manifest_militar.json: id, pieza, que_muestra, unidad_o_lugar, anio, angulo, archivo, titulo_commons, url_pagina_commons, autor, licencia, url_licencia y cotas.
- Origen: `C:\Dev\mr-mak-workspace\referencias-reales\<categoria>\`. No está ignorado por git, pero no se sube.
- Entrega: **SendUserFile** copia a la biblioteca con los mismos bytes, pero en la **raíz** de /mnt/project-files/, porque no crea subcarpetas. Teo los mueve después a referencias-reales/<categoria>/.
- No se puede escribir en los hilos de otros: los avisos van a Mak con send_message (@parent), y Mak los reenvía.

## 4. Lotes
- 6-7 nov: vehículos, ferroviario, aéreo, naval, infantería, ambientación, militar (M1-M9, MV1-MV7) y entorno (F, G, H, K, P1-P4). El índice está en docs/arte/referencias/catalogo.md (biblioteca).
- 7-nov, **N · Nules** (para Álvaro), en `referencias-reales/nules/`: N1, estación de Nules–La Vilavella (6 fotos); N2, cooperativas sustitutas (La Vilavella y un almacén de Alcàsser); N3, Canal de Nules y del Bovalar (3). Hay manifest_nules.json, contacto_nules.jpg y catalogo_nules.md, una sección lista para añadir al final del catálogo. Que sea la «estación vieja»: SIN VERIFICAR.
- 7-nov, **R · radar** (para Teo), en `referencias-reales/radar/`: R1, Raven de Indra del ET en remolque con mástil (CC BY 3.0); R2, Rasura del ET en trípode (CC BY-SA 2.0). Va con manifest_radar.json.
- 7-nov, **S · superficies** (para Teo, después de que Eugenio rechazara las texturas «con parches»), en `referencias-reales/superficies/`: S1 y S2, Lince con polvo y con barro; S3, Pizarro en maniobras; S4 y S5, Pizarro con desconchones y óxido (El Goloso); S6, NH90 italiano levantando polvo. Va con manifest_superficies.json y contacto_superficies.jpg. S2 es PD según Commons, pero la base está SIN VERIFICAR.

## 5. Pendiente
- Comprobado el 8-nov: N (15 archivos), R (3) y S (8) ya están en sus subcarpetas de la biblioteca, y la sección N ya está en catalogo.md.
- R y S: la sección está en `catalogo_radar_superficies.md` (raíz de la biblioteca, origen en referencias-reales/). Falta que Teo la añada al final de catalogo.md y mueva el archivo.
- Ids repetidos: R1 existe en Ferroviario y en Radar; N1-N3 en Naval y en Nules. Citar siempre con la carpeta (`radar/R1`). Próximo lote: letra o prefijo libre.
- R1: Commons dice Indra en la descripción y Thales Nederland en el título. Fabricante SIN VERIFICAR.
- 8-nov, **RC · catenaria y gálibo** (para Teo, dintel de la puerta de vía): RC1-RC3 en `referencias-reales/ferroviario/` con manifest_catenaria.json. Cotas del BOE (Orden FOM/1630/2015): hilo de contacto 5,30 m; GHE16 4,33 m; GEC16 4,70 m; gálibo uniforme GEC16 5,63 m. Sustentador a unos 6,7 m: SIN VERIFICAR.
- El catálogo ya está versionado en el repo: docs/arte/referencias/catalogo.md (commit e393908, con R, S y RC). La copia nueva está en la raíz de la biblioteca y Teo la mueve a su sitio.
- 8-nov, ficha del Lince para Hugo (D-N172): `referencias-reales/militar/ficha_lince_hugo.md`. Arma: identificación visual (M2 y lanzagranadas de 40 mm, SIN VERIFICAR); munición, no pública; STANAG 1-3.
- 8-nov, **AE · aeródromos** (Eugenio y Lucía, D-N173): docs/arte/referencias/aerodromos.md (commit 922fa6a). Recomendado: Base Jaime I de Bétera (BHELEME II); alternativa: El Pinar (LECN); Manises descartado por el lore. Fotos AE1-AE2 en referencias-reales/aerodromos/. Norma de Eugenio: todo vehículo aéreo sale de un aeródromo del mapa global, no de la estación.
- Hilos activos: Lucía (3) cmsg_014mgaTqwTDTmezhB3g3Rs8B6SQ5dvp3vRjsT8MHK748va y Álvaro (3) cmsg_014mgaTqwTDTmezhB3g3Rs8BVQMPsLQGZfhUnE8hUirrDa.

## 6. Huecos (no hay fuente libre en Commons)
- Nules: cooperativa citrícola, acequia pequeña de huerta y paso a nivel.
- Radar: ARINE y RAC-3D.
- NH90 de las FAMET con regueros de aceite o palas gastadas; NH90 visto desde arriba; arma de puerta del NH90 (MAG 58, con el montaje SIN VERIFICAR).
- Dragón sucio en maniobras; Dragón con Guardian 30 de perfil; Pizarro de perfil y de frente; Lince con RCWS.
- Tienda modular verde del ET (se usan las K6 beige, con el color SIN VERIFICAR); FARP con cajas de munición; vagón cubierto con bogies de ancho ibérico.
- Paneles TB-1/TB-2 y balizas TB-10 (hacerlos con la norma 8.3-IC); señales P-8 y P-9; paso a nivel de Valencia–Sagunto.
- Dotación de munición del ET: no es pública. Las fotos MV3 del Chinook son de un CH-47D, pero las cotas son del F.

## 7. Trampas
- Las figuras del BOE son imágenes y pdftotext no las saca. Hay que renderizar la página con `uv run --with pypdfium2 --with pillow` (no hay pdftoppm) y mirarla.
- No abrir PDFs del BOE en el navegador del panel: los descarga y al usuario le salta el diálogo de guardar.
- `python -I` impide importar módulos de la carpeta del propio script. Para los scripts propios del scratchpad, ejecutarlo sin -I.
- `rm -rf` en el comando lo deniega el clasificador de permisos. No hace falta: basta con usar carpetas nuevas.
- Las búsquedas de Commons devuelven muchos PDF; hay que filtrarlos. Las categorías («Category:… in Spanish Army service») dan mejores resultados que la búsqueda de texto.
- Después de un apagón, comprobar los lotes con PIL verify() y abrir los JSON. El 7-nov no se perdió nada.
