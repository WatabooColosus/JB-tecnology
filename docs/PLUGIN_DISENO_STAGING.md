# Plugin de diseño de staging — `JB Stage Design`

**Estado: código desarrollado en GitHub, NO instalado ni ejecutado en WordPress.**

Objetivo: aplicar en staging una primera capa visual sobria basada en la nueva identidad de JB Tecnología MED sobre las clases de WoodMart y la estructura real Elementor, sin reemplazar archivos premium ni reescribir la base de datos.

## Características
- Filtro estricto por hostname `staging.jbtecnologiamed.com.co` antes de adjuntar estilos.
- CSS aislado por clase `body.jb-stage-design`, con cabecera oscura y acentos turquesa provisionales, dropdowns premium y focus visible.
- Decoración ligera de banners existentes (IDs del Elementor inspeccionado), compatible con prefers-reduced-motion.
- Sin Javascript inyectado, sin AJAX, sin cuentas de usuario ni alteraciones a precios/pedidos.
- Si se instala en producción por accidente, el CSS del plugin no se carga porque falla el filtro por hostname. Esto **no sustituye revisión ni autorización de despliegue**.

## Instalación SOLO después de cerrar SEC-01
1. Asegurar staging noindex y restringido con contraseña de Hostinger.
2. Confirmar base de datos separada, backups restaurables y envíos externos deshabilitados.
3. Verificar los IDs de Elementor en el WordPress de staging actual.
4. Instalar plugin propio desde una distribución ZIP creada del directorio `wordpress/jb-stage-design`, no usar Plugins → Instalar de WordPress.org para este código privado.
5. Activar solo en staging, comparar header + menú + landing en 360,390,430,768,1024,1440 y 1920 px.
6. Anotar en GitHub Issue NAV-02 el antes/después con capturas, sin datos personales.

## Reversión
Desactivar el plugin `JB Tecnologia MED - Staging Design`; no genera tablas ni opciones. La cabecera vuelve a estilo del tema. No borra productos ni reescribe Elementor.

## Limitaciones
No reemplaza menú WordPress ni Header Builder. No incluye logo original definitivo ni afirma rediseño completado. Los colores son candidatos, no valores oficiales del manual.
