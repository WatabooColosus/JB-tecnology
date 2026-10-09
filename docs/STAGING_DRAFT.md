# Draft WoodMart Child editado mediante WPVibe

**Modificaciones realizadas exclusivamente en el borrador de tema `woodmart-child-wpvibe-draft`, en staging. No hay publicación.**

- `assets/jb-stage.css`: idéntico contenido al CSS versionado en `wordpress/jb-stage-design/assets/css/jb-stage.css` al commit de referencia (sin divergencia conocida).
- `functions.php`: fuente del tema hijo original (12 líneas), con filtro de host staging, clase `jb-stage-design` y carga encolada de CSS.
- El archivo `wordpress/staging-child/functions.php` es una **copia de la fuente escrita en el borrador**; se mantiene para auditoría de Codex. No reemplazar archivos del host automáticamente.
- WPVibe marcó ambas operaciones de escritura como exitosas; sin embargo tras esperar, se pudo generar el preview y verificar el CSS y la clase body en HTML.
- Falta verificar el enlace de preview, la presencia de clase en `body`, la carga real de estilos y las capturas responsive antes de declarar la tarea completada.

## Reversión
Descartar el draft no publicado (en WPVibe). No borrar el tema hijo activo ni usar Hostinger Publish/Replace Production. En GitHub, revertir commit de la rama únicamente bajo autorización si hay errores.

## Antes de volver a consultar el sitio
- Esperar por limitación HTTP 429, respetar intervalos y no saturar WordPress.
- Verificar seguridad de staging primero.

## Verificación técnica posterior
- Vista previa tokenizada generada por WPVibe (URL con token mantenida **fuera del repositorio público**).
- `<head>` de esa vista contiene hoja `jb-stage-brand-css` cargada desde `woodmart-child-wpvibe-draft/assets/jb-stage.css`.
- La etiqueta `<body>` de la vista tiene `jb-stage-design` y la clase `wp-child-theme-woodmart-child-wpvibe-draft`; `noindex` sigue presente.
- **Aún pendiente**: inspección visual real en varios tamaños y aprobación humana. Nada se ha publicado al staging activo.
