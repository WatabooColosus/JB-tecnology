# JB Tecnología MED · Desarrollo web

Repositorio público de especificación, diseño y desarrollo incremental de [JB Tecnología MED](https://jbtecnologiamed.com.co/), coordinado por Agencia Digital Wataboo.

> **Estado:** fase 1 · navegación, identidad y landing. **No está conectado a despliegue automático.** El WordPress en Hostinger continúa siendo la fuente del contenido en producción.

## Stack observado
WordPress · WoodMart Child · Elementor · WooCommerce · Composite Products. La landing de origen es la página Elementor **10625**, “Home Mega-electronics”. Los datos de referencia fueron obtenidos con consultas de lectura de WPVibe (2026-10-08/09).

## Orden de trabajo
1. **1A — Navegación e identidad:** cabecera, menús/megamenús, móvil, logo y sistema visual provisional.
2. **1B — Landing:** conservar los 19 bloques de la portada, transformar contenido y enlaces, validar responsive/accesibilidad.
3. **2 — Catálogo:** categorías, atributos, variantes, galerías dinámicas y AJAX, con datos comerciales validados.
4. **3 — Arma tu PC:** Composite Products y futura integración con BuildCores (sin API contratada o comprobada aún).
5. **4 — Resto de páginas:** empresas, soporte, blog, contacto, legales, pagos, envíos y SEO.

## Documentación
- `AGENTS.md`: instrucciones de seguridad y trabajo para Codex.
- `data/home-grid-map.json`: orden real y IDs de elementos Elementor.
- `data/navigation-proposal.json`: propuesta de navegación.
- `docs/BASELINE.md`: hallazgos comprobados y pendientes.
- `docs/FASES.md`: hitos y criterios de aceptación.
- `docs/DEPLOYMENT.md`: GitHub, staging y WordPress.
- `wordpress/design/jb-tokens.css`: tokens CSS de marca **provisionales**, no desplegados.

## Protección
- No subir credenciales, `wp-config.php`, bases SQL, datos de compradores, backups, temas/plugins premium ni material privado.
- No editar producción automáticamente: trabajar mediante rama → pruebas → staging → aprobación → despliegue manual.
- No afirmar ser “Tienda Oficial Redragon” hasta comprobar la autorización comercial.
- Los precios y productos importados de demo **no equivalen** al inventario empresarial.

La apertura del código no implica que el contenido de WordPress ni las credenciales deban ser públicos.

## Centro de operación y diseño (2026-10-09)
- [Mapa maestro de las 19 secciones de la landing](docs/LANDING_MAESTRA.md)
- [Especificaciones por sección (JSON)](data/landing-spec.json)
- [Dimensiones responsive, tokens visuales y animaciones](docs/SISTEMA_VISUAL_DIMENSIONES.md)
- [Menús y megamenús WoodMart](docs/ARQUITECTURA_MENUS.md)
- [Decisiones, ideas y bloqueos](docs/DECISIONES_IDEAS.md)
- [Staging y puerta de seguridad P0](docs/STAGING_SECURITY.md)
- [Issues y dependencias](docs/TAREAS_GITHUB.md)
- [Backlog de trabajo verificable](data/backlog.json)
- [Proceso para Codex + WPVibe](docs/PROCESO_CODEX_WPVIBE.md)

**Staging:** https://staging.jbtecnologiamed.com.co (conexión WPVibe verificada; seguridad y noindex pendientes de confirmar). La producción NO es destino de despliegues automáticos.

**Actualización de staging:** `blog_public=0` y `noindex` confirmados. WPVibe avanzado activado solo en staging. Draft de Woodmart Child creado y escrito, aún sin publicar; preview pendiente por HTTP 429. Ver [Estado de seguridad](docs/STAGING_SECURITY.md) y [Registro del borrador](docs/STAGING_DRAFT.md).
