# Draft WoodMart Child editado mediante WPVibe

**Modificaciones realizadas exclusivamente en el borrador de tema `woodmart-child-wpvibe-draft`, en staging. No hay publicación.**

- `assets/jb-stage.css`: idéntico contenido al CSS versionado en `wordpress/jb-stage-design/assets/css/jb-stage.css` al commit de referencia (sin divergencia conocida).
- `functions.php`: fuente del tema hijo original (12 líneas), con filtro de host staging, clase `jb-stage-design` y carga encolada de CSS.
- El archivo `wordpress/staging-child/functions.php` es una **copia de la fuente escrita en el borrador**; se mantiene para auditoría de Codex. No reemplazar archivos del host automáticamente.
- WPVibe marcó ambas operaciones de escritura como exitosas; sin embargo no se pudo completar la verificación del preview por HTTP 429.
- Falta verificar el enlace de preview, la presencia de clase en `body`, la carga real de estilos y las capturas responsive antes de declarar la tarea completada.

## Reversión
Descartar el draft no publicado (en WPVibe). No borrar el tema hijo activo ni usar Hostinger Publish/Replace Production. En GitHub, revertir commit de la rama únicamente bajo autorización si hay errores.

## Antes de volver a consultar el sitio
- Esperar por limitación HTTP 429, respetar intervalos y no saturar WordPress.
- Verificar seguridad de staging primero.
