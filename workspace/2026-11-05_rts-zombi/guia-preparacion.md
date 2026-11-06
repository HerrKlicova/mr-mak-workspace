# Guía de preparación del entorno — RTS zombi en Unity 6

**Para:** Eugenio · **Redactada:** 2026-11-05 (Hilo B) · **Actualizada:** 2026-11-05, ~15:50 hora de Madrid · **Estado:** verificada; falta que Eugenio diga «guía completada»

Esta guía está pensada para alguien que nunca ha usado Unity. Cada paso dice **qué hacer**, **cómo comprobar que ha funcionado** y **si cuesta dinero**. Todavía no se ha creado ningún proyecto de Unity ni se ha escrito código del juego: eso espera a que tú confirmes que la guía está completada.

## Cómo leer las marcas de verificación

| Marca | Significado |
| --- | --- |
| ✔ | Comprobado en documentación oficial actual, o en tu PC durante esta sesión. |
| ◐ | Comprobado en parte (fuente secundaria, o la página oficial no lo detalla). Hay que confirmarlo en pantalla. |
| ✘ | No he podido verificarlo. No lo doy por cierto. |

Las fuentes están al final, en el apartado 14.

---

## 0. Resumen en 10 líneas

1. **Versión de Unity: 6.3 LTS (6000.3.x).** La 6.0 LTS tenía soporte «hasta octubre de 2026», es decir, ya terminado (salvo suscripciones Enterprise/Industry). ✔
2. **Unity Personal es gratis** mientras ingresos y financiación de los últimos 12 meses sean inferiores a 200.000 USD. ✔
3. **Nada de lo esencial es de pago** para empezar: Unity Personal, Unity Hub, Entities, MCP for Unity (licencia MIT) y Git son gratuitos. ✔
4. **MCP for Unity** (v10.3.0, 4-oct-2026) funciona con Claude y se instala desde Unity sin terminal. ✔ Su botón de configuración registra el servidor en Claude. ◐ (no lo he podido probar: Unity aún no está instalado)
5. **ElevenLabs: actualizado.** Al empezar la sesión tu plan era «Creator» y la API de Imagen y Vídeo exige «Pro o superior». El 5-nov (hacia las 14:23 UTC, las 15:23 en Madrid) subiste a **Pro** (comprobado: `tier: pro`, 814.102 créditos al mes) y las consultas de solo lectura a la API de imagen y de vídeo responden **200**, sin haber generado nada. Falta una prueba de generación real para confirmarlo del todo. ✔/◐ Detalles en el apartado 8.
6. **mr.mak funciona desde la app de escritorio de Claude** (esta misma sesión corre ahí y lee el CLAUDE.md y las skills del repositorio). ✔
7. **El addon de Blender se puede controlar con Python** (`bpy.context.scene.img3d` y `bpy.ops.img3d.generate()`). TRELLIS, Hunyuan y «More Views» están listos; Pixal3D y Hi3D todavía no. **Decisión del 5-nov: se usará Hunyuan.** Probado de punta a punta: una imagen en 3 min 01 s y con vistas múltiples en 1 min 33 s (40.000 caras). ✔
8. **Pixelab:** 8.825 generaciones restantes, el ciclo se reinicia el 17-nov-2026. ✔
9. **Dato del Hilo A sobre URP:** Forward+ es una *opción* seleccionable, no un requisito; Forward es el valor por defecto. Ver apartado 4. ✔/◐
10. **Tu PC ya tiene** Git, Git LFS, uv, Python, Node y la CLI de Claude. **Falta** Unity Hub y el Editor. ✔

---

## 1. Qué hay ya en tu PC (comprobado el 2026-11-05)

| Elemento | Estado |
| --- | --- |
| Windows 11 Pro 10.0.26100 | ✔ cumple el requisito del Editor (Windows 10 21H1 o superior, x64) |
| GPU NVIDIA RTX 5080, 16 GB de VRAM, controlador 616.64 | ✔ el Editor pide una GPU compatible con DX10/11/12 o Vulkan |
| Disco C: 267 GB libres · Disco D: 322 GB libres | ✔ |
| Git 2.55.0 · Git LFS 3.7.1 | ✔ instalados |
| uv 0.13.0 · `uvx` 0.13.0 | ✔ instalados (MCP for Unity los necesita) |
| Python 3.14.7 (alias de WindowsApps) | ◐ MCP for Unity pide Python 3.10 o superior; ver la nota del apartado 7 |
| Node 24.21.0 · .NET 10.0.401 · GitHub CLI 2.102.0 | ✔ |
| Claude Code (CLI) 2.1.318 | ✔ |
| Blender 4.4 y Blender 5.2 (5.2.1 LTS en ejecución) | ✔ |
| Unity Hub / Unity Editor | **No instalados** |
| Variables de entorno de usuario `ELEVENLABS_API_KEY`, `PIXELLAB_API_TOKEN`, `GODOT_PATH` | ✔ existen (no he leído sus valores) |
| `GEMINI_API_KEY`, `FAL_KEY` | No existen |

Tamaño de la descarga del Editor y de los módulos: ✘ no verificado; calcula varios GB y deja margen en C: o D:.

---

## 2. Unity Hub y cuenta (gratis)

1. Entra en la página oficial **Download Unity** (https://unity.com/download), inicia sesión o crea tu cuenta de Unity, y pulsa **Download** para Windows. ✔
2. Abre el instalador `.exe` y sigue el asistente. ✔ Si el Hub te pide acceso al sistema de archivos o al firewall, es normal: lo usa para tus proyectos y para descargar recursos. ✔
3. Abre Unity Hub e inicia sesión con tu Unity ID. ✔
4. **Licencia:** elige **Unity Personal** (gratuita). Se puede usar si ingresos o financiación de los últimos 12 meses son inferiores a 200.000 USD; tú eres dueño de lo que creas. ✔ Los pasos exactos de activación dentro del Hub los guía el propio Hub. ✘ (la página oficial «Manage licenses» no pude abrirla)
5. Instala el Hub en una ruta normal (no unidad de red ni enlaces simbólicos, que el Hub no admite). ✔

**Comprobación:** el Hub abre sin errores, aparece tu cuenta arriba a la derecha y en la sección de licencias consta una licencia Personal activa.

**¿De pago?** No. Unity Pro solo haría falta si superaras el umbral de 200.000 USD o quisieras publicar en consolas. ✔

---

## 3. Instalar Unity 6.3 LTS con sus módulos

1. En el Hub: **Installs → Install Editor**. Elige **Unity 6.3 LTS (6000.3.x)**. ✔ El Hub te ofrecerá la versión de parche vigente; yo no puedo fijarla por ti. Un blog de terceros fechado el 17-oct-2026 cita 6000.3.26f1 como última; es ◐ y puede haber una más nueva.
2. En la pantalla de módulos marca:
   - **Windows Build Support (IL2CPP)** (identificador interno `windows-il2cpp`). ✔
   - Un editor de código si no tienes uno (el Hub suele ofrecer Visual Studio). Para Entities se necesita **Visual Studio 2022 o posterior, o Rider 2021.3.3 o posterior**. ✔ Si ya usas VS Code, no he verificado qué extensión oficial hace falta. ✘
   - Documentación local: opcional.
3. Pulsa **Install** y espera.

Si olvidas un módulo: Hub → **Installs → Manage → Add Modules**. ✔

**Comprobación:** en **Installs** aparece «6000.3.x» con el módulo de Windows IL2CPP listado.

**Por qué no la 6.0:** su soporte LTS de dos años terminaba en octubre de 2026 (hoy es noviembre). La 6.3 LTS tiene soporte hasta diciembre de 2027. ✔

### Estado real tras la instalación (5-nov, comprobado en el disco)
- **Instalada: Unity 6000.3.28f1** en `C:\Program Files\Unity\Hub\Editor\6000.3.28f1`. ✔ Es la línea 6.3 LTS. (Eugenio escribió «6.2 ltd», pero la carpeta instalada es la 6000.3.)
- El Hub instaló primero **6000.6.8f1 (Unity 6.6)** por defecto y se canceló. Unity 6.6 es una Update release (la página oficial de soporte solo marca como LTS la 6.0 y la 6.3), y desde la 6.4 Entities es un paquete del editor con la versión del editor: la 6.5 eliminó `Entities.ForEach`, `Job.WithCode` y los Aspects, y la 6.6 deja obsoletos los componentes gestionados y `PlaybackPolicy`. Que la 6.6 no sea LTS lo leo en un rastreador de terceros; lo demás es de la guía de actualización de Unity. ✔/◐ Se anota como decisión D-006 (pendiente de que Eugenio confirme).
- **Aviso «Unity CLI ya está disponible»:** la CLI de Unity es un ejecutable para gestionar editores, módulos y proyectos sin el Hub; con el paquete `com.unity.pipeline` permite a un agente observar y manejar un editor abierto, incluso ejecutar C# en vivo. La documentación oficial la califica de **experimental**, y el paquete también. ✔ No la necesitas ahora; el plan es MCP for Unity. Volver a mirarla cuando sea estable.

**¿De pago?** No.

---

## 4. Crear el proyecto (solo cuando tú lo confirmes)

> Reglas del proyecto: **no se crea el proyecto hasta que digas que esta guía está completada.** Estos pasos son los que se seguirán entonces.

1. Hub → **New project** → editor 6.3 LTS.
2. Plantilla: la 3D con URP. En el disco la plantilla se llama **«3D URP»** (ver más abajo); el nombre que muestra el Hub puede ser «Universal 3D», pero eso no lo he podido comprobar en pantalla. ◐ **Evita** la de alta gama (`3d-high-end`, HDRP).
3. Ubicación: **una carpeta propia fuera de mr-mak-workspace**, por ejemplo `C:\Dev\<nombre-del-juego>\`. Es un repositorio Git distinto (apartado 6). El nombre del juego está pendiente (provisional: TBD).
4. Desmarca «Connect to Unity Cloud» / «Use Unity Version Control» si el asistente lo ofrece: usaremos Git. ◐ (opciones exactas del asistente no verificadas)

**Comprobación de que URP está activo:** en el Editor, *Edit → Project Settings → Graphics*: el campo de configuración de la tubería (Scriptable Render Pipeline Settings) debe apuntar a un asset de tipo `UniversalRenderPipelineAsset`. ◐ (ruta habitual; la página oficial dio la comprobación pero no era taxativa)

### Proyecto creado (5-nov, tras «guía completada»)
Eugenio dio la guía por completada y autorizó el resto. El proyecto está en **`C:\Dev\TBD`** (repositorio `https://github.com/HerrKlicova/TBD.git`, primer commit `0726f9f`). ✔
- **Cómo se creó:** el editor tiene el argumento `-createProject` con `-cloneFromTemplate` (documentación oficial), pero **se negó a arrancar: «No valid Unity Editor license found»** (0 licencias; además el Hub de la Tienda de Windows no pasó la validación del cliente de licencias). ✔ Por eso copié a mano los archivos de la plantilla «3D URP» (solo `Assets`, `Packages` y `ProjectSettings`, sin `Library/`), que es lo que hace esa opción. No se abrió el proyecto en Unity.
- **Manifest de paquetes:** URP 17.3.0, Entities 1.5.0, Entities Graphics 1.5.0, MCP for Unity por Git en la etiqueta `v10.3.0`, y el resto de la plantilla; sin `packages-lock.json` (Unity lo regenera). Burst no se fijó: lo resuelve Entities. **No se ha verificado que ese conjunto resuelva sin errores** hasta abrirlo en Unity. ◐
- **Ajustes comprobados en `ProjectSettings`:** Visible Meta Files, serialización de recursos en texto (Force Text), asset de URP asignado. ✔ El nombre del producto se puso a «TBD». Domain Reload no se tocó.
- **Archivos añadidos:** `.gitignore` oficial de Unity, `.gitattributes` con Git LFS (el único PNG de la plantilla ya sube por LFS), `.env.example` sin valores, `.mcp.json` (MCP for Unity en `http://localhost:8080/mcp`, ElevenLabs y Pixelab con variables de entorno), `CLAUDE.md` y `README.md`. Búsqueda de claves en los archivos versionados: sin resultados. ✔
- **Lo que falta y solo puede hacer Eugenio:** activar la licencia **Unity Personal** (Hub → icono de cuenta → *Manage licenses* → *Add* → licencia Personal gratuita; los nombres exactos de los botones no los he podido comprobar) y abrir `C:\Dev\TBD` con el editor 6000.3.28f1 (Hub → *Add → Add project from disk*). Aunque la active, queda la duda de si el editor ve la licencia del Hub de la Tienda de Windows; si sigue diciendo «No valid license», habrá que mirar ese punto. ◐
- Después: comprobar en *Window → Package Manager* que no hay errores y que **Burst es 1.8.25 o superior**; *Window → MCP for Unity* → iniciar el servidor y ver «Connected».

### Qué contiene la plantilla instalada (comprobado en el disco, solo lectura)
El editor 6000.3.28f1 incluye tres plantillas en `Editor\Data\Resources\PackageManager\ProjectTemplates`: `3d-cross-platform` (17.0.14), `3d-high-end` (17.0.7) y `2d-cross-platform` (6.1.6). La que usa URP es la primera: su `package.json` se llama **«3D URP»** (`com.unity.template.urp-blank`). Su manifest fija versiones de la época de Unity 6.0 (por ejemplo `com.unity.render-pipelines.universal` 17.0.1), así que al crear el proyecto habrá que actualizar URP y comprobar los paquetes. ✔ (Esto sustituye lo que decía arriba sobre «Universal 3D», que era una suposición.)

### Forward+ (dato del Hilo A)

- **Forward** es la ruta por defecto de URP. **Forward+** es una opción: no hay límite de luces que afectan a cada objeto (sí hay un límite de luces visibles por cámara). ✔
- Con Forward+ se ignoran los ajustes de URP *Additional Lights*, *Main Light* y *Per Object Limit*. ✔
- Para elegirla: en el asset *Universal Renderer* (el «Renderer Data» al que apunta el URP Asset), campo **Rendering Path**. ◐ (la página oficial lo remite a otra que no pude abrir)
- **No he podido confirmar que ECS/Entities Graphics exija Forward+.** Una búsqueda sugiere que Forward+ ayuda con muchas luces en ECS, pero ninguna fuente oficial lo declara obligatorio. ✘ Se deja como decisión de arte/rendimiento del Hilo A, a probar con un prototipo.

---

## 5. Paquetes (Entities / DOTS)

Para Unity 6.3 (6000.3) la documentación oficial indica estas versiones **released** (no preliminares): ✔

| Paquete | ID | Versión para 6000.3 |
| --- | --- | --- |
| Entities | `com.unity.entities` | **1.5.0** |
| Entities Graphics | `com.unity.entities.graphics` | **1.5.0** |

(Una búsqueda mostró también la línea 1.4.x para 6.3; la página oficial de 6.3 solo lista 1.5.0, así que usa esa.)

**Cómo instalar:** *Window → Package Manager*, selecciona **Unity Registry**, busca «Entities» y pulsa **Install**; repite con «Entities Graphics». También se puede añadir por nombre del paquete. ✔ Las dependencias (Burst, Collections, Mathematics, Jobs) normalmente se instalan solas, pero no está declarado en las páginas que leí. ◐

**Ajuste recomendado por la documentación de Entities:** desactivar **Domain Reload** al entrar en modo Play (mejora el rendimiento del editor). Ruta habitual: *Edit → Project Settings → Editor → Enter Play Mode Settings*. ✔ (la recomendación) / ◐ (la ruta)

**Comprobación:** en el Package Manager, *In Project* lista «Entities 1.5.0» y «Entities Graphics 1.5.0», sin iconos de error. En la ventana *Console* no debe haber errores rojos tras instalar.

**Burst:** el Hilo A pide que sea la **1.8.25 o superior** (lo necesita para su plan de simulación determinista). La versión que viene con 6.3 no he podido leerla en la documentación (la página dio 404); se comprobará en el Package Manager al crear el proyecto. ✘ No hace falta instalar paquetes de red: el cooperativo irá con lockstep determinista (hito 7, tras el MVP).

**Cosas que no he verificado y que importan:**
- Requisitos concretos de Entities Graphics (versión de API gráfica, SRP Batcher, etc.) ✘
- Compatibilidad con Forward+ ✘ (ver apartado 4)
- Dificultad real: Entities exige C# y un modo de pensar distinto (datos y sistemas, no objetos). No es de pago, pero sí una curva de aprendizaje importante. Es una recomendación mía, no un dato de la documentación.

**¿De pago?** No.

---

## 6. Git: repositorio, .gitignore y buenas prácticas

### Dos repositorios, no uno

| Repositorio | Contenido | Ruta |
| --- | --- | --- |
| **Juego** | Proyecto Unity (`Assets/`, `Packages/`, `ProjectSettings/`, código) | `C:\Dev\<juego>\` (nuevo) |
| **mr.mak** | Tarjeta del reportaje visual (documentos vivos, imágenes, manifiestos) | `C:\Dev\mr-mak-workspace\workspace\...` |

Es el mismo patrón que ya usas: el `.gitignore` de mr-mak-workspace ya ignora `projects/incremental-godot/`, `projects/roblox-study/` y `projects/roll-a-town/` como «proyecto local con su propio Git». ✔

> ⚠ **Aviso sobre mr-mak-workspace:** su `origin` apunta a `https://github.com/witnesstodark/mr-mak-workspace.git` (el repositorio plantilla del autor), no a una copia tuya, y hay mucho trabajo sin confirmar (tarjetas RPG Caravaca, Kenshi, etc., ver `git status`). **No hagas `git push` ahí.**
>
> **Estado (5-nov):** Eugenio ya ha creado dos repositorios privados vacíos: `https://github.com/HerrKlicova/TBD.git` (el juego) y `https://github.com/HerrKlicova/mr-mak-workspace.git` (mr.mak). Ambos se pueden leer desde este PC con el gestor de credenciales de Git (consulta de solo lectura; el push no se ha probado). El cambio del `origin` de mr.mak lo bloqueó el sistema de permisos; se hace con estos dos comandos, desde `C:\Dev\mr-mak-workspace`:
>
> ```bash
> git remote rename origin upstream
> git remote add origin https://github.com/HerrKlicova/mr-mak-workspace.git
> ```
>
> Así la plantilla queda como `upstream` (para traer novedades) y `origin` pasa a ser tuyo.

### Pasos para el repositorio del juego (cuando exista el proyecto)

1. Copia `docs/unity.gitignore` de esta carpeta a la **raíz del proyecto Unity** como `.gitignore`. Es la plantilla oficial de GitHub (dominio público, CC0) más unas líneas mías para secretos y audio en bruto. ✔
2. En Unity: *Edit → Project Settings → Editor*: **Version Control Mode = Visible Meta Files** y **Asset Serialization Mode = Force Text**. Son los valores por defecto en proyectos nuevos; confírmalos. ◐ (fuentes secundarias)
3. `git init`, añade `.gitignore`, haz el primer commit **antes** de importar nada pesado.
4. **Commitea siempre los archivos `.meta`** junto a cada recurso. ◐
5. Mueve, renombra y borra recursos **desde el panel Project de Unity**, no desde el Explorador de Windows (rompe los `.meta`). Es práctica habitual de Unity; no la he contrastado en una página oficial concreta. ◐
6. Git LFS ya está instalado (3.7.1). Recomiendo seguir con LFS texturas, audio, modelos 3D y `.blend`. Mi propuesta de `.gitattributes` (no verificada contra documentación de Unity):

```gitattributes
*.png  filter=lfs diff=lfs merge=lfs -text
*.jpg  filter=lfs diff=lfs merge=lfs -text
*.psd  filter=lfs diff=lfs merge=lfs -text
*.wav  filter=lfs diff=lfs merge=lfs -text
*.mp3  filter=lfs diff=lfs merge=lfs -text
*.ogg  filter=lfs diff=lfs merge=lfs -text
*.fbx  filter=lfs diff=lfs merge=lfs -text
*.glb  filter=lfs diff=lfs merge=lfs -text
*.blend filter=lfs diff=lfs merge=lfs -text
```

7. GitHub Free admite archivos de hasta 2 GB con LFS. ✔ Las cuotas gratuitas de almacenamiento y ancho de banda de LFS **no las pude verificar** ✘: miralas en tu cuenta antes de subir mucho contenido pesado.
8. Hábitos: commits pequeños y frecuentes; una rama por función; etiqueta (`git tag`) cada hito; no cambies de modo de serialización a mitad de proyecto (hazlo en un commit aislado). ◐

**Comprobación:** `git status` en el proyecto no muestra `Library/`, `Temp/`, `Logs/`, `UserSettings/` ni `.env`; `git check-ignore -v .env` responde con la regla.

**¿De pago?** No. Un repositorio privado en GitHub sí es posible en plan Free, pero los límites de LFS son lo que debes mirar.

---

## 7. MCP for Unity + Claude (sin depender de la terminal)

### Qué es y qué versión
MCP for Unity, de CoplayDev. Versión actual **v10.3.0 (4-oct-2026)**, licencia **MIT (gratis)**. Soporta Unity 2021.3 LTS y posteriores, incluido 6.x. Requiere Python 3.10 o superior (instalado vía `uv`). ✔ «Aura for Unity» es otro producto premium del mismo patrocinador; **no lo necesitas**. ✔

### Instalar el paquete en Unity (un clic de menú, sin terminal)
1. En Unity: *Window → Package Manager → «+» → Add package from git URL…* ✔
2. Pega: `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main` ✔ (rama estable). La documentación sugiere poder fijar una versión con `#v10.0.0`, pero la última publicada es v10.3.0; si quieres fijarla, `#v10.3.0` corresponde a la etiqueta de la última release. ◐
3. Esto necesita **Git en el PATH** (lo tienes). ✔ Alternativas: OpenUPM o Asset Store. ✔
4. Al importar se abre un **asistente de configuración**: confirma Python y `uv` (te ayuda a instalarlos si faltan) → **Done** → lista de clientes detectados → **Configure Selected**. ✔
5. Más tarde: *Window → MCP for Unity* para arrancar o parar el servidor, cambiar entre HTTP y stdio, o reconfigurar. El panel muestra «Connected» cuando todo está unido. ✔

### Python y uv en tu PC
`uv` 0.13.0 está instalado. Tu `python` es un alias de la Tienda de Windows (3.14.7). La versión 10.3.0 incluye una corrección de «detección de Python detrás de los alias de la Tienda de Windows». ✔ Si el asistente se queja, que instale su propio Python con `uv`; no hace falta que toques el tuyo. ◐

### Conectarlo a Claude en la app de escritorio
La app de escritorio de Claude tiene **dos superficies distintas**, y MCP for Unity las trata distinto:

| Superficie | Cómo la configura MCP for Unity | Transporte |
| --- | --- | --- |
| **Pestaña Code** (donde estás trabajando ahora, y donde corre mr.mak) | Botón **Configure** del asistente. Claude Code «conecta automáticamente tras configurar». ✔ | HTTP (`http://localhost:8080/mcp`), por defecto ✔ |
| **Pestaña de chat** de Claude Desktop | Escribe `claude_desktop_config.json`. «Claude Desktop solo admite stdio» ✔ | stdio vía `uvx --from mcpforunityserver mcp-for-unity --transport stdio` ✔ |

**Recomendación: usa la pestaña Code** abriendo la sesión **con la carpeta del proyecto Unity como carpeta de trabajo**. Así el servidor aparece también en el `.mcp.json` de ese proyecto y convive con ElevenLabs.

Hechos de tu equipo: existe `~/.claude.json` y la CLI de Claude Code 2.1.318. No existe aún `claude_desktop_config.json` en `%APPDATA%\Claude` ni en la ruta del paquete MSIX. ✔ (Si algún día lo editas a mano y no se carga, hay un informe aislado de que la app lee una ruta virtualizada de `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\...`. ◐)

**Conexión manual (si el botón no funcionara).** Un `.mcp.json` en la raíz del proyecto Unity:

```json
{
  "mcpServers": {
    "unityMCP": { "type": "http", "url": "http://localhost:8080/mcp" }
  }
}
```

⚠ La documentación de MCP for Unity muestra este bloque **sin** `"type"`, pero la documentación de Claude Code dice que una entrada con `url` y sin `type` **se rechaza**. Por eso incluyo `"type": "http"`. ✔

La primera vez, Claude Code pide **aprobar** los servidores definidos en `.mcp.json`. ✔

### Seguridad
El servidor HTTP escucha solo en loopback (`127.0.0.1`) por defecto; abrirlo a la red local exige activar «Allow LAN Bind (HTTP Local)». **Déjalo desactivado.** ✔

### Cómo verificar (de menos a más)
1. Unity: *Window → MCP for Unity* → estado **Connected**.
2. Claude (pestaña Code, sesión con la carpeta del proyecto): el servidor `unityMCP` figura como conectado. En la CLI el comando es `/mcp`; en la app de escritorio no he verificado el equivalente exacto. ◐
3. Prueba de humo oficial: pide *«Crea un cubo en el origen y añade un Rigidbody»*. Debe aparecer el cubo en la escena en segundos. ✔

### Lo que **no** he podido comprobar
- No lo instalé ni lo probé: Unity no está instalado y no debo crear el proyecto todavía. ✘
- Qué hace exactamente el botón *Configure* con Claude Code (si invoca `claude mcp add` y necesita la CLI en el PATH o escribe archivos). ✘ Tu CLI está en `~/.local/bin`; si falla, usa el `.mcp.json` manual de arriba.
- El número de versión exacto de cada «herramienta» disponible: ver la referencia en https://coplaydev.github.io/unity-mcp/reference/tools. ✘

**¿De pago?** No.

---

## 8. ElevenLabs: conexión segura

### Estado actual (hechos)
- Tu plan: **Pro** (suscripción activa, mensual), actualizado el 5-nov-2026. Antes era Creator, con 26.003 de 229.088 créditos usados. Ahora: **814.102 créditos al mes, 0 usados**, con el próximo reinicio el **5-dic-2026**. 160 plazas de voz (antes 30). La próxima factura aparece como 99,00 USD más impuestos (119,79 USD en total). ✔ (datos de la consulta de suscripción del 5-nov, tras la subida)
- La clave está en la **variable de entorno de usuario** `ELEVENLABS_API_KEY` (no he leído su valor). ✔
- El `.mcp.json` de mr-mak-workspace la referencia como `${ELEVENLABS_API_KEY}` y arranca el servidor con `uvx elevenlabs-mcp`; el MCP funciona (la consulta de suscripción respondió). ✔

### Cómo mantenerla segura
1. **Nunca** pegues la clave en `.mcp.json`, en el código, ni en un `.md`. Solo el nombre `${ELEVENLABS_API_KEY}`. ✔ (La expansión de variables `${VAR}` funciona en `.mcp.json`.)
2. En el repositorio del juego, el `.gitignore` ya excluye `.env`, `.env.*` (salvo `.env.example`). Crea `.env.example` con **solo los nombres vacíos** (`ELEVENLABS_API_KEY=`).
3. Para el proyecto nuevo, el `.mcp.json` del juego repetirá el bloque de `elevenlabs`, cambiando `ELEVENLABS_MCP_BASE_PATH` a una carpeta del juego **ignorada por Git** (`Assets/Audio/_raw`, ya incluida en `unity.gitignore`). El actual apunta al proyecto `incremental-godot`. ✔

**Comprobación:** `git grep -n "sk_"` (o el prefijo de tu clave) en el repositorio no devuelve nada; el MCP de ElevenLabs responde sin que la clave aparezca en ningún archivo versionado.

### Uso comercial de la música de ElevenLabs en el juego (pendiente que dejó el GDD)
Verificado en las condiciones oficiales **«Eleven Music model specific terms»** (última actualización indicada: 9-oct-2026). ✔
- **Plan Pro:** música para **uso individual**; descarga de alta calidad (WAV sin pérdida o mp3 de 192 kbps); hasta **500 minutos de descarga** y 304 de generación al mes; uso por API permitido; sin atribución obligatoria. Eugenio es una persona individual, así que cumple la restricción de elegibilidad.
- **Derechos de medios en los planes de autoservicio, Pro incluido:** «todo uso comercial online y offline, **excepto cine, TV, radio y *Studio Games***».
- **«Studio Game»** = un videojuego comercializado (venta, publicidad u otra monetización) que **no sea un «Indie Game»**.
- **«Indie Game»** = un juego que, sumadas todas sus versiones y DLC, ha generado **menos de 500.000 USD** desde su primera salida comercial, y está desarrollado o publicado por una entidad cuyos ingresos por todos sus juegos son **menos de 1.000.000 USD**.
- **Consecuencia:** un juego en solitario por debajo de esos umbrales **sí puede usar música de Eleven Music con el plan Pro**. Si deja de ser Indie Game, hay **60 días** para pasar a un plan que permita Studio Games (en la tabla, solo «Enterprise Music»); pasado ese plazo hay que dejar de usar la música en el juego, salvo en copias ya distribuidas. La responsabilidad de saber si el juego es Indie Game es de quien lo publica.
- **Plataformas:** el documento no menciona Steam por nombre, pero incluye los juegos publicados en plataformas de terceros y obliga a **cumplir las normas de cada plataforma sobre contenido generado por IA** (en Steam hay que declararlo).
- **Lo que no he verificado:** las condiciones de **voces y efectos de sonido** (son otros términos), las de **imagen y vídeo** generados por la API y el estado actual de una versión anterior de las condiciones de la música que parecía más restrictiva (la versión vigente es la que he leído). ✘ Vuelve a leer las condiciones antes de publicar, porque pueden cambiar en cualquier momento («surten efecto al publicarse»).

### ¿Tu plan incluye la API de Imagen y Vídeo?
**Con el plan Pro, sí en principio.** La documentación oficial dice que la API de Imagen y Vídeo requiere plan **Pro o superior**; por debajo, la llamada falla con `402 paid_plan_required`. Además, la clave necesita el permiso *Image & Video* o *Flows*. ✔

**Lo que he comprobado tras tu subida a Pro (5-nov, ~14:30 UTC):**
- La consulta de suscripción devuelve `tier: pro`. ✔
- Dos peticiones de **solo lectura** con tu clave: `GET /v1/flows/image` y `GET /v1/flows/video` (listar generaciones) responden **HTTP 200** con lista vacía. No se generó nada ni se gastó ningún crédito. ✔
- **Lo que esto no prueba del todo:** la documentación sitúa el error 402 en las llamadas de *creación*, y un listado podría estar permitido aunque la creación no lo estuviera. Tampoco prueba qué modelos concretos están habilitados (Seedream sigue requiriendo aprobación). Por eso la prueba definitiva es **una generación real pequeña**, que gasta créditos y no he hecho. ◐
- La cabecera `xi-api-key` es la habitual de ElevenLabs; la página que consulté no la nombraba, pero la petición se aceptó. ✔

Matices:
- **Modelos soportados por la API** (cuando se tiene Pro): `gpt-image-1`, `gpt-image-1.5`, `gpt-image-2` y dos variantes 2.5; `gemini-2.5-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-image`, `gemini-3.1-flash-lite-image`; `bytedance-seedream-5-lite` y `-5-pro`; y para vídeo Veo 3.1 y Seedance. ✔ (los tres que mencionaste existen)
- **Seedream (ByteDance)** está **desactivado por defecto incluso en la API** y requiere aprobación explícita (error `model_access_denied`); la documentación menciona a clientes Enterprise que contactan con soporte, así que **no está claro que Pro baste**. ✔/✘ Cuenta con que gpt-image y gemini-image sí funcionen y con que Seedream pueda seguir bloqueado hasta confirmarlo con una prueba.
- **Créditos compartidos:** las generaciones se cobran en créditos, igual que en la app, y el coste depende del modelo, la resolución, la duración y las entradas; las fallidas no se cobran. El mismo saldo (814.102 al mes) sirve para voces, efectos y música. ✔
- **Cómo ver el coste antes de gastar:** la app web de ElevenLabs muestra el coste antes de enviar. No hay un endpoint documentado de presupuesto en la API. ✔ Por eso la prueba la haría desde la app web o con una sola imagen de tamaño mínimo.
- Precio del plan Pro: la próxima factura aparece como 99,00 USD más impuestos. ✔ (datos de tu cuenta)

### Opciones para las imágenes de referencia (actualizado con Pro)
| Opción | Hechos | Coste |
| --- | --- | --- |
| **API de ElevenLabs con Pro** (gpt-image, gemini-image; Seedream a confirmar) | Acceso de lectura confirmado (HTTP 200); creación sin probar ◐ | Créditos del plan (sin coste extra de suscripción) |
| **Pixelab** (ya lo tienes, MCP conectado) | 8.825 generaciones restantes; reinicio 17-nov. Útil para sprites e iconos en pixel art | Incluido hasta el reinicio |
| **API de Gemini** (Google AI Studio) | **Ningún modelo de imagen es gratuito.** Precios estándar: Nano Banana Pro 0,134 USD por imagen 1K/2K; Gemini 3.1 Flash Image 0,067 USD en 1K ✔ | Pago por uso; ya no hace falta si ElevenLabs funciona |
| **fal.ai** (skill incluida en mr.mak) | Pago por uso; `FAL_KEY` no existe | Opcional |

**Los dos modelos que mencionó Eugenio existen en la API (comprobado):**
- **«GPT 2.5»** = `gpt-image-2.5-sunburst` («producción», detalle y edición precisa, 5 niveles de calidad) y `gpt-image-2.5-flare` (variante rápida con los mismos controles, para alto volumen). Admiten hasta 10 imágenes de referencia, máscara de edición, 1K/2K/4K y calidad `low` a `max`. La documentación no describe otra diferencia. ✔
- **«Nano Banana Pro»** = `gemini-3-pro-image` (la página de precios de Google lo nombra «Gemini 3 Pro Image (Nano Banana Pro)»): modelo de razonamiento, buen texto legible, hasta 10 imágenes de referencia en la API, 1K/2K/4K. Sin parámetro de calidad ni máscara. ✔
- **Prueba hecha:** una imagen con `gpt-image-2.5-flare` (1K, calidad baja, 16:9) se creó correctamente en unos 15 s y el resultado es utilizable (ver tarjeta, pestaña Arte). El coste en créditos no se pudo medir por la API. **Nano Banana Pro y GPT 2.5 Sunburst no se han probado.**
- **Recomendación:** GPT Image 2.5 Flare para iterar rápido y barato (conceptos), Sunburst o Nano Banana Pro para las imágenes finales de referencia; comparar los dos con el mismo prompt cuando el concepto esté cerrado.

**Mi recomendación actualizada:** usar la API de ElevenLabs (ya pagada con Pro) para imágenes de referencia y de concepto, con gpt-image o gemini-image según resultado, y Pixelab para el pixel art final. Antes de lanzar un lote, una **prueba única de una imagen** para confirmar que la creación funciona y cuánto cuesta en créditos. Descarto abrir una cuenta de Gemini por ahora.

**Recordatorio:** el vídeo se cobra por duración y es mucho más caro en créditos que una imagen; no lo usaría hasta tener el concepto cerrado. (Es una recomendación mía; no he medido costes.)

---

## 9. mr.mak: qué es, que funciona desde la app de escritorio y cómo montar el reportaje

### Hechos
- README y estructura leídos: dos ventanas conectadas, **Chats** (CLI reales de Claude Code, Codex u OpenCode en terminales con pestañas e historial) y **Workspace** (tarjetas con informes, imágenes, prompts, archivos, skills y conexiones MCP). Hay una versión móvil por Tailscale. ✔
- **Funciona desde la app de escritorio, no solo desde terminal:** esta misma sesión corre en la pestaña Code de la app de escritorio, con `C:\Dev\mr-mak-workspace` como carpeta de trabajo, y ha leído el `CLAUDE.md`, el `AGENTS.md`, las skills del proyecto y el MCP de ElevenLabs y Pixelab. Además, el servicio de mr.mak está en marcha ahora mismo (proceso Node 41160, `http://127.0.0.1:56251/` responde 200). ✔
- mr.mak ejecuta **la CLI real** que ya tienes (Claude Code 2.1.318) con su inicio de sesión; **no necesita clave de API** para los chats. ✔ (las funciones de voz/dictado sí usan claves aparte y de pago, y están desactivadas)
- Reglas del repositorio relevantes (AGENTS.md): registrar entregables en `workspace/workspace.json`; una tarjeta por proyecto con las revisiones dentro; conservar fuentes editables; no reiniciar la app sin permiso; contenido en inglés por defecto salvo petición explícita. Tus tarjetas actuales están en español, y la instrucción del proyecto dice «español siempre»: **usaré español** y lo dejo anotado. ✔
- Tarjeta de referencia ya existente: **RPG Caravaca** (`workspace/2026-10-14_rpg-caravaca/`), con `index.html`, `modelo.json`, `tarjeta.js/css` y subcarpetas `assets/` (criaturas, enemigos, música, niveles…). Es el patrón a imitar. ✔
- Hay 20 skills útiles ya incluidas (planificación, audio, UI, VFX, diseño de niveles, imagen de referencia, materiales, revisión visual…). **Ninguna menciona Unity en sus textos** (0 coincidencias); las de audio, niveles, UI y revisión visual no mencionan ningún motor concreto, y dos contienen la palabra «three» (posiblemente Three.js). Hay que probarlas con el flujo de Unity. ◐

### Propuesta: mr.mak como fuente viva del proyecto
Tu indicación (5-nov): *todo* —ideas, diseño, assets, sonidos— documentado y ordenado en mr.mak; el GDD se traduce a mr.mak y se trabaja sobre él, con historial de qué era la idea original y cómo ha cambiado.

**Una tarjeta fijada** (`pinned: true`), `workspace/2026-11-05_<juego>/`, con estas pestañas (en `steps` de `workspace.json`):

| Pestaña | Contenido | Archivo |
| --- | --- | --- |
| **Resumen** | Estado, cifras, «ahora / siguiente», enlaces al resto | `index.html` (generado desde `modelo.json`, como Caravaca) |
| **GDD** | Documento vivo, una sección por sistema | `GDD.md` |
| **Idea original** | Copia **congelada** del primer GDD (nunca se edita) | `GDD-v0.1-original.md` |
| **Cambios** | Historial: qué cambió respecto a la idea original, por qué y cuándo | `CAMBIOS.md` |
| **Decisiones** | Registro de decisiones (propuesta/aceptada/sustituida) | `DECISIONES.md` |
| **Investigación** | Fuentes, juegos de referencia, **imágenes de referencia** con su origen | `INVESTIGACION.md` + `assets/referencias/` |
| **Arte** | Conceptos, sprites, modelos 3D, versiones y prompts | `ARTE.md` + `assets/arte/` |
| **Audio** | Banco de sonidos: voces, efectos, ambientes y música, con prompt y versión | `AUDIO.md` + `assets/audio/` |
| **Herramientas** | Esta guía y el estado de cada herramienta | `guia-preparacion.md` |

**Cómo versionar los cambios (tres capas complementarias):**

1. **Instantánea congelada.** `GDD-v0.1-original.md` se guarda tal cual al cerrar el borrador y no se vuelve a tocar. Cada hito grande (`v0.2`, `v1.0`) genera una copia nueva con su etiqueta Git (`git tag gdd-v0.2`).
2. **Registro de cambios con formato fijo** (`CAMBIOS.md`), una entrada por cambio:

   ```
   ### C-014 · 2026-11-20 · Sistema: Hordas
   - Antes: 1.000 zombis simulados en detalle.
   - Ahora: simulación por niveles de detalle (detallada cerca, abstracta lejos).
   - Motivo: viabilidad técnica (D-007).
   - Origen: hilo «Diseño», decisión de Eugenio el 2026-11-20.
   - Commit: <hash>
   ```

   Cada sección del GDD lleva una línea «Idea original / Estado actual» con los identificadores `C-xxx` que la afectan, de modo que se ve la evolución sin abrir otro archivo.
3. **Historial de Git** como red de seguridad: `git log -p workspace/2026-11-05_<juego>/` muestra el texto exacto de cada cambio. Para que valga, el repositorio de mr.mak necesita un `origin` tuyo (ver aviso del apartado 6).

**Assets (imágenes, sprites, modelos, sonidos):** un **manifiesto** `assets/manifiesto.json` con una entrada por asset: `id`, tipo, herramienta y modelo, **prompt completo**, fecha, archivo, estado (`candidato / elegido / sustituido`), `sustituye_a` / `sustituido_por`, coste en créditos y enlace al cambio `C-xxx`. mr.mak ya incluye una herramienta offline que registra entradas y salidas con huella SHA-256 (`scripts/asset-delivery/`); es útil para la integridad de los archivos, no sustituye la aprobación visual. ✔ Las fuentes editables (diagramas en Mermaid o DOT, prompts) se guardan junto al resultado.

**Estado de esta propuesta:** es solo un diseño. **No he creado la tarjeta** ni tocado `workspace.json`; espero tu visto bueno (pregunta 2).

---

## 10. Blender: addon «Image to 3D» (solo inspección)

### Hechos
- Addon **«Image to 3D», 3DRedbox Studio, v1.0.3** (autor: Milad Kambari), instalado en `%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\image_to_3d`. Está en **Blender 5.2 (5.2.1 LTS)**; en Blender 4.4 no está. Junto a él hay otro addon, `Tripo3d_Blender_Bridge`, que no usas. ✔
- El motor está en `D:\3D ENGINES\` (TRELLIS.2, Hunyuan, Pixal3D, Hi3D) y la salida se guarda en `D:\3D ENGINES\output\<nombre>_<fecha>.glb`. ✔
- **¿Se puede controlar con Python? Sí.** Lo comprobé con el MCP de Blender, que está conectado, solo con consultas de lectura:
  - Propiedades en `bpy.context.scene.img3d`: `engine` (`TRELLIS` / `HUNYUAN` / `PIXAL3D` / `HI3D`), `image_path`, `quality` (`FAST` / `HIGH` / `ULTRA`), `faces` (TRELLIS, por defecto 200.000), `faces_hy` (Hunyuan, por defecto 40.000), `use_texture`, `texture` (1024/2048/4096), `seed`, `view_1`–`view_3` (vistas extra), `auto_detail`, `auto_enhance`, `creativity` y otras. ✔
  - Operadores: `bpy.ops.img3d.generate()`, `enhance`, `enhance_detail`, `paint_detail`, `cancel`, `undo_texture`, `undo_detail`, etc. ✔
  - `generate` solo funciona si hay una imagen válida en `image_path` y no hay otro trabajo en curso; trabaja en un subproceso (no bloquea Blender) y deja el `.glb` en la carpeta de salida. ✔ (leído en el código; **no lo ejecuté**)
- **Estado de los motores (actualizado a las ~15:45 hora local):** TRELLIS ✔ listo · Hunyuan ✔ listo · **Hunyuan «More Views» ✔ listo (instalado por Eugenio)** · **Pixal3D ✘ no listo · Hi3D ✘ no listo**. Existe la marca `INSTALLED_HI3D` pero el motor aún no responde como listo; suele deberse a una descarga o preparación en curso (◐, no confirmado). ✔
- **Mínimo de polígonos:** tú indicas 5.000; en las propiedades del addon el mínimo configurable es **1.000** caras (tanto `faces` como `faces_hy`). La cifra de 5.000 puede venir de otra cosa (la calidad real del resultado); no la verifiqué. ✘
- Llevar el modelo a Unity: Unity no necesita Blender instalado si exportas **FBX** desde Blender. Para `.glb` existe el paquete oficial glTFast en la documentación de Unity, pero esa página no confirma el nombre de instalación ni las versiones. ◐ Dejaré esto para la fase de arte, junto con la limpieza (retopología, texturas, LODs).

### Decisión (5-nov): el 3D se generará con Hunyuan

Hunyuan es el motor elegido. Lo que sé de él en tu instalación:
- **Está listo** (`engine_ready("HUNYUAN")` devuelve verdadero) ✔
- En el código, Hunyuan se selecciona con `scene.img3d.engine = "HUNYUAN"` y usa su propio número de caras, `faces_hy` (por defecto **40.000**, mínimo configurable 1.000), no `faces`, que es el de TRELLIS. La textura se pinta siempre con Hunyuan (`use_texture`, `texture` 1K/2K/4K). ✔
- Las **vistas extra** (`view_1`–`view_3`, atrás/izquierda/derecha) requieren «Hunyuan More Views», que **todavía no está listo**; si se rellenan sin él, el addon se detiene con un aviso. ✔ Para empezar, se usa una sola imagen frontal.
- **«Enhance Detail» (Hi3D)** necesita el motor Hi3D, que tampoco está listo. La opción `auto_detail` debe quedarse en `OFF` hasta entonces. ✔ «Enhance Texture» depende de Hunyuan; el operador existe y su comprobación previa responde bien, pero no la he ejecutado. ◐
- Mi aviso de siempre: los resultados de este tipo de motores necesitan limpieza (retopología, textura, LODs) antes de entrar en Unity; sirven para vehículos y edificios clave, no para hordas. Es tu criterio y lo mantengo.

**Aviso de licencia (5-nov):** el archivo `D:D ENGINES\models	encent\Hunyuan3D-2.1\LICENSE` dice: «THIS LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA» y su apartado 4(c) prohíbe usar el modelo **o su resultado** fuera del territorio (el mundo salvo esos tres). ✔ (leído en tu disco). **En España, el uso comercial de modelos generados con Hunyuan no está cubierto.** La carpeta de «More Views» (Hunyuan3D-2mv) no incluye archivo de licencia ✘. **El addon usa los pesos en local, no una API:** la carga se hizo desde `D:D ENGINES\models	encent\...` y el motor avisa de que trabaja sin conexión. ✔ Alternativa del mismo addon: **TRELLIS.2** (README local del modelo: licencia MIT ✔; las licencias de sus dependencias, como DINOv3 o BiRefNet, no las he revisado ✘). Pendiente de decisión de Eugenio.

### Pruebas hechas (5-nov, autorizadas por Eugenio)

**Prueba 1: una sola imagen frontal.** Imagen `docs/assets/mr-mak.png` (peluche del cerdito de mr.mak), `engine = HUNYUAN`, `quality = FAST`, 40.000 caras, textura 1K. Resultado: **3 min 01 s**, 1 objeto, 40.000 caras, 1 material, 1 mapa UV, `.glb` de 3,3 MB. Se pintó la textura y el resultado es reconocible (con sombrero de copa y morro incluidos). Antes de pintar la textura, torch usaba 4,88 GB y quedaban 10,62 GB libres de 17,07 GB; **el pico de VRAM no se midió**. ✔

**Prueba 2: Hunyuan «More Views» (vistas múltiples).** Eugenio instaló «More Views» y `hy_mv_ready()` pasó a verdadero. ✔ Cómo funciona (leído en el código y confirmado al ejecutar):
- Las vistas extra son tres propiedades de `bpy.context.scene.img3d`: `view_1` = **atrás**, `view_2` = **izquierda**, `view_3` = **derecha**, además de la imagen principal `image_path`, que es el **frente**. Se pueden rellenar una, dos o las tres; todas son opcionales. ✔
- Con ellas, el motor carga el modelo de forma multivista (**Hunyuan3D-2mv**) en lugar del normal. En el registro aparece «VIEWS 4 (Hunyuan multi-view: front, back, left, right)». ✔
- **Cómo hay que hacer las fotos** (texto del propio addon): es *el mismo objeto*, con *la misma luz*, **entero en el encuadre**. La vista izquierda es la del objeto visto desde *su* mano izquierda (en la imagen mira hacia la izquierda) y la derecha, desde *su* mano derecha (mira hacia la derecha). ✔
- Sin «More Views» instalado, si se rellenan las vistas el addon se detiene con el aviso «Hunyuan multi-view files are not installed». ✔
- **Mi prueba:** usé la imagen original como frente y, como vistas atrás, izquierda y derecha, tres renders del modelo de la prueba 1 (ortográficos, con fondo gris claro). Resultado: **1 min 33 s**, 40.000 caras, 3,1 MB. El modelo salió **más limpio y más fiel por detrás y por los lados** (la pata, el sombrero y el hocico se ven más definidos). ✔
- **Qué no demuestra:** las tres vistas salieron del propio modelo, así que la comparación es circular; sirve para validar que el flujo funciona, no para medir cuánto mejora con vistas reales. El tiempo menor (1:33 frente a 3:01) **no es una mejora del método**: la segunda ejecución ya tenía los modelos cargados en memoria. ✘ No he comparado con vistas hechas a mano ni con una hoja de personaje.
- **Flujo recomendado para el juego** (propuesta mía): partir de una imagen de concepto del vehículo o edificio en vista frontal limpia, generar sus vistas atrás, izquierda y derecha con el mismo modelo de imagen (misma luz y encuadre), y pasarlas a `view_1`–`view_3`. La skill `character-sheet-pipeline` del repositorio prepara hojas de personaje con vistas múltiples; **no la he probado con este addon**. ◐

Resultados e imágenes: tarjeta del proyecto en mr.mak, pestaña Arte.

**Cómo repetir una prueba por Python** (con Blender abierto y el addon activo):

```python
s = bpy.context.scene.img3d
s.engine = "HUNYUAN"; s.quality = "FAST"; s.faces_hy = 40000
s.use_texture = "ON"; s.texture = "1024"
s.image_path = r"C:\ruta\frente.png"
s.view_1 = r"C:\ruta\atras.png"; s.view_2 = r"C:\ruta\izquierda.png"; s.view_3 = r"C:\ruta\derecha.png"  # opcionales
bpy.ops.img3d.generate('INVOKE_DEFAULT')   # asíncrono; el estado queda en s.status
```

El resultado se guarda en `D:\3D ENGINES\output\<nombre>_<fecha>.glb` y se importa a la escena abierta. El estado («Done in 1:33  -  40,000 faces») se lee en `s.status`.

**Incidencia (mía) con Blender en segundo plano:** para renderizar los resultados lancé Blender sin interfaz con el ajuste de fábrica. Eso hizo que Blender limpiara las librerías de Python que las extensiones guardan en `%APPDATA%\Blender Foundation\Blender\5.2\extensions\.local\lib\python3.13\site-packages` (quedaron archivos `.~stale~…`). La instancia abierta sigue funcionando, pero **al reiniciar Blender pueden fallar extensiones que dependan de esas librerías** (por ejemplo el MCP). Según la documentación y fuentes de la comunidad, Blender solo vuelve a sincronizar esas librerías al instalar, activar o desactivar una extensión. **Solución:** *Edit → Preferences → Get Extensions*, desactivar y volver a activar la extensión afectada. ◐ (no lo he podido probar sin reiniciar el Blender de Eugenio). Las ejecuciones siguientes usaron una carpeta de usuario aislada y no tocaron nada más.

**Comprobación de la guía:** con una imagen asignada y el motor en Hunyuan, `bpy.ops.img3d.generate.poll()` debe devolver `True`; y el `.glb` aparece en `D:\3D ENGINES\output`. ✔ (comprobado)

### Hallazgo extra
MCP for Unity 10.3.0 añade un **«Blender Bridge»** para manejar BlenderMCP desde el Editor de Unity. ✔ Hoy ya tienes el MCP de Blender conectado; sería una forma de cerrar el circuito Blender → Unity. No lo he probado. ✘

---

## 11. Pixelab: lote antes del 12 de noviembre

- Saldo verificado el 2026-11-05: **8.825 generaciones restantes** de 20.000, plan Tier 3 «Pixel Architect 2x» activo, **reinicio el 17-nov-2026**, 6,87 USD de crédito. ✔
- **Piloto ejecutado el 5-nov** (autorizado por Eugenio, «p2: si»; plan de `docs/pixelab-piloto.md` del Hilo A): **78 generaciones** gastadas, saldo final **8.747,05**, 42 elementos. Cada coste coincide con el anunciado por la herramienta (medido con `get_balance` antes y después). ✔
- **Costes medidos:** `create_image_pixen` **1** generación por imagen (16×16 hasta 512×288); personaje v3 de 64 px con 8 direcciones **2**; animación de plantilla (8 fotogramas) **1 por dirección**; hoja de interfaz de 256×256 **10**; `create_image_pro` de 320×180 **10** (1 candidato). ✔
- **Qué salió bien:** retratos, iconos de recursos, personaje de 8 direcciones y la ilustración de evento (la de `pixen` a 512×288 por 1 generación es la mejor relación calidad/coste).
- **Qué hay que corregir en el lote:** fichas del mapa (vistas inconsistentes), VFX (salió un soldado en el fogonazo, y son fotogramas sueltos), un icono con fondo opaco, decal de sangre con suelo de fondo, texto («START») en el botón pese a pedir «no text». Detalle y hojas de contacto en la pestaña Arte de la tarjeta de mr.mak.
- **Pendiente:** aprobación del estilo por Eugenio y recálculo del lote por el Hilo A. El lote debe lanzarse antes del 12-nov.

---

## 12. Otras herramientas que merecen la pena

| Herramienta | Por qué | Coste | Verificado |
| --- | --- | --- | --- |
| **Skills de mr.mak** (`game-audio-workflow`, `game-ui-workflow`, `game-vfx-workflow`, `game-level-design`, `image-reference-workflow`, `materials-to-game`, `plan`, `gameplay-visual-review`) | Ya incluidas; estructuran el trabajo de audio, interfaz, efectos, niveles y revisión visual. **Recomiendo** empezar por `plan` y `game-audio-workflow`. | Gratis | ◐ existen; no probadas con Unity |
| **MCP de Blender** (ya conectado) | Control de Blender por Claude (escena, capturas, Python). | Gratis | ✔ |
| **Blender Bridge de MCP for Unity** | Une Blender y Unity. | Gratis (MIT) | ✔ existe; ✘ sin probar |
| **MCP de Pixelab** (ya conectado) | Sprites, tiles, animaciones de pixel art. | Plan existente | ✔ |
| **ElevenLabs MCP** (ya conectado) | Voz, efectos de sonido y música. | Créditos de Creator | ✔ |
| **Unity Profiler y Test Framework** | Medir el rendimiento de las hordas y probar sistemas. Son parte de Unity. | Gratis | ✘ no verificado en esta sesión |
| **GitHub CLI** (instalado) | Crear el repositorio privado desde terminal. | Gratis | ✔ instalado |

Descartadas por tus reglas: Higgsfield y Tripo. No he recomendado assets de terceros (por ejemplo bibliotecas gratuitas) porque no he verificado sus licencias en esta sesión.

---

## 13. Lista de comprobación final (para marcar «guía completada»)

- [ ] Unity Hub instalado, sesión iniciada, licencia **Personal** activa
- [ ] Unity **6.3 LTS** instalado con **Windows Build Support (IL2CPP)** y un IDE compatible
- [ ] Repositorio privado creado para el juego; `unity.gitignore` listo para copiar; Git LFS decidido
- [ ] Decidido el `origin` de mr-mak-workspace (el actual es el de la plantilla)
- [ ] ElevenLabs: clave solo en variable de entorno; `.env.example` sin valores
- [ ] Plan Pro activo (hecho el 5-nov) y probada **una** generación de imagen por API para confirmar la creación y su coste en créditos
- [ ] Aprobada la estructura del reportaje en mr.mak (apartado 9)
- [ ] Probado, con tu permiso, un modelo de punta a punta con Hunyuan en el addon de Blender (apartado 10)
- [ ] Tras crear el proyecto: URP activo, Entities 1.5.0 y Entities Graphics 1.5.0 sin errores, MCP for Unity «Connected» y el cubo de prueba creado desde Claude

**Cuando hayas marcado todo y me lo digas, se podrá crear el proyecto de Unity.**

---

## 14. Fuentes consultadas (2026-11-05)

- Unity 6 y soporte LTS: https://unity.com/releases/unity-6 · versión 6000.3.0f1 (3-dic-2025): https://unity.com/releases/editor/whats-new/6000.3.0
- Requisitos del Editor 6.3: https://docs.unity.com/en-us/engine/6000.3/manual/get-started/install-and-upgrade/getting-started-installing-unity/system-requirements
- Instalar Unity Hub: https://docs.unity.com/en-us/hub/install-hub-win-mac · CLI y módulos: https://docs.unity.com/en-us/hub/hub-cli-reference
- Unity Personal: https://unity.com/products/unity-personal
- Entities 6000.3: https://docs.unity.com/en-us/engine/6000.3/manual/packages-list/packages-all/pack-safe/com-unity-entities · Entities Graphics: https://docs.unity.com/en-us/engine/6000.3/manual/packages-list/packages-all/pack-safe/com-unity-entities-graphics · Instalación: https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/getting-started-installation.html
- URP: https://docs.unity.com/en-us/engine/6000.3/manual/render-pipelines/universal-render-pipeline/urp-introduction · Forward y Forward+: https://docs.unity.com/en-us/engine/6000.3/manual/render-pipelines/universal-render-pipeline/introduction/urp-concepts/rendering-paths/forward-rendering-paths
- MCP for Unity: https://github.com/CoplayDev/unity-mcp · instalación https://coplaydev.github.io/unity-mcp/getting-started/install · transportes https://coplaydev.github.io/unity-mcp/architecture/transports · release v10.3.0 https://github.com/CoplayDev/unity-mcp/releases/tag/v10.3.0 · PyPI https://pypi.org/project/mcpforunityserver/
- Claude Code y MCP: https://code.claude.com/docs/en/mcp · app de escritorio: https://code.claude.com/docs/en/desktop
- ElevenLabs imagen y vídeo (API): https://elevenlabs.io/docs/eleven-api/guides/cookbooks/image-and-video · capacidades: https://elevenlabs.io/docs/overview/capabilities/image-video
- Precios de Gemini: https://aistudio.google.com/docs/pricing
- Plantilla `.gitignore` de Unity: https://github.com/github/gitignore/blob/main/Unity.gitignore · Git LFS en GitHub: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- glTFast: https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.0/manual/index.html
- Comprobaciones locales: PC de Eugenio (DESKTOP-1BLD8V4), 2026-11-05: herramientas, variables de entorno (solo si existen), mr-mak-workspace, addon de Blender (solo lectura), Pixelab `get_balance`, ElevenLabs `check_subscription`.

## 15. Preguntas abiertas para Eugenio

1. **Versión de Unity:** ¿Unity 6.3 LTS? *Recomiendo que sí* (la 6.0 LTS ya terminó su soporte).
2. **Estructura de mr.mak (apartado 9):** ¿te vale la tarjeta fijada con las pestañas y el registro de cambios? *Recomiendo que sí*; en cuanto lo confirmes puedo crear el esqueleto vacío.
3. **Repositorio de mr.mak (resuelto salvo un paso):** los repositorios existen. Falta cambiar el `origin` de mr.mak con los dos comandos del apartado 6 (el sistema de permisos bloqueó al hilo B).
4. **Prueba del addon de Blender (hecha):** ver apartado 10. Una imagen en 3 min 01 s y con More Views en 1 min 33 s.
5. **Imágenes de referencia (hecha, con matiz):** la creación por API funciona con `gpt-image-2.5-flare`. Falta decidir si se prueba también Nano Banana Pro (`gemini-3-pro-image`) y GPT 2.5 Sunburst cuando el concepto esté cerrado. *Recomiendo comparar los dos con el mismo prompt.*
6. **Versión de Unity:** ¿confirmas no usar Unity 6.6 y quedarte con la 6.3 LTS (6000.3.28f1 instalada)? *Recomiendo que sí.*
7. **Estilo del piloto de Pixelab:** ¿lo apruebas o ajustamos las fichas del mapa y los VFX antes del lote? *Recomiendo aprobar retratos y personaje, y repetir mapa y VFX.*
