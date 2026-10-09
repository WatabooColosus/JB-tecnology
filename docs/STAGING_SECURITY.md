# P0 · Seguridad staging — Evidencia actualizada

Fecha de última actualización: 2026-10-09 · Conexión autenticada WPVibe sobre `https://staging.jbtecnologiamed.com.co`.

## Cambios confirmados
- [x] WPVibe Connect versión 1.20.3 instalado y activado **solo en staging** usando Hostinger Abilities API.
- [x] `wp option update blog_public 0` ejecutado en staging (respuesta OK, cache de LiteSpeed/Elementor purgada).
- [x] `wp option get blog_public` volvió **0** en staging; la lectura del `<head>` contiene `noindex`.
- [x] En producción `blog_public=1` y el HTML comprobado **no** contiene `noindex` tras el cambio.
- [x] `woodmart-child-wpvibe-draft` creado y editado en staging; **no se ha publicado** ni activado el borrador.
- [x] Estilos propuestos en el repositorio, y copia de `assets/jb-stage.css` escrita dentro de ese borrador.
- [x] Vista previa: se obtuvo después de una pausa y el HTML confirma CSS de borrador y clase de marca.
- [ ] QA visual: móvil, escritorio, accesibilidad y navegación no realizados todavía.

## Pendientes que mantienen SEC-01 abierto
- [ ] Proteger el subdominio con contraseña/HTTP Basic Auth o control de acceso en hPanel; `noindex` **NO equivale a privacidad**.
- [ ] Confirmar aislamiento de base SQL con Hostinger o comprobación segura del identificador DB (sin publicar el nombre ni claves). El comportamiento distinto de opciones y plugins es evidencia de separación lógica, pero no certifica el diseño de infraestructura.
- [ ] Copia de seguridad restaurable (archivos + BD) y plan de reversión.
- [ ] Deshabilitar/pasar a sandbox envío de correos, pagos, cron externos y webhooks en staging; no hacer transacciones reales de prueba.
- [ ] Verificar que ninguna URL/canonical del staging causa indexación involuntaria.

## Bloqueos y recuperación
Hostinger devolvió **HTTP 429** en intentos de usar una herramienta de staging. Respetar período de espera, no insistir ni realizar llamadas paralelas repetidas. Tras respetar un intervalo, la vista previa respondió y verificó carga de CSS y clase corporal. El 429 sigue siendo un riesgo operativo; no efectuar bucles de comprobación.

No pulsar **Publicar** staging de Hostinger para volcar DB a producción: podría sobrescribir ventas nuevas. Las ediciones del draft WordPress son privadas mientras no se publique el borrador.

## Origen y línea base
El tema activo sigue siendo Woodmart Child 1.0.0 en WPVibe `site_info` anterior a cambios. La homepage es Elementor #10625. Los cambios en staging NO implican que el código GitHub esté desplegado automáticamente.
