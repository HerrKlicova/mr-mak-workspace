# Audio

**Estado:** todavía no se ha generado ningún sonido. Esta pestaña se rellenará cuando el GDD fije la lista de
voces, efectos, ambientes y música.

## Herramienta
- ElevenLabs, plan **Pro** (desde el 5-nov-2026): 814.102 créditos al mes, reinicio el 5-dic-2026. El mismo saldo sirve para audio, imagen y vídeo.
- La clave vive solo en la variable de entorno de usuario `ELEVENLABS_API_KEY`; nunca en archivos del repositorio.
- Salida en bruto (candidatos sin elegir): `Assets/Audio/_raw/` del proyecto Unity, ignorada por Git.

## Uso comercial de la música (verificado 5-nov-2026)
Según «Eleven Music model specific terms» (actualizado el 9-oct-2026), el plan **Pro** permite uso comercial online y offline
**salvo cine, TV, radio y «Studio Games»** (juegos comercializados que no sean «Indie Game»). Un **Indie Game** es el que ha
generado menos de **500.000 USD** en total y lo desarrolla o publica una entidad con menos de **1.000.000 USD** de ingresos por
juegos. Si el juego deja de cumplirlo, hay **60 días** para pasar a un plan que lo permita. Hay que **declarar el uso de IA**
según las normas de cada plataforma. Sin verificar: términos de voces y efectos de sonido. Detalle en la guía, apartado 8.

## Banco de sonidos (plantilla)

| ID | Tipo | Evento | Prompt | Herramienta | Versión | Estado | Archivo | Cambio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *(vacío)* | | | | | | | | |

Tipos: voz, efecto, ambiente, música. Estados: candidato, elegido, sustituido. Cada sonido elegido lleva el
identificador del cambio `C-xxx` que lo introdujo. La skill `game-audio-workflow` del repositorio define cómo
escuchar, elegir e integrar los sonidos con identificadores estables.
