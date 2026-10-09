# P0 · Estado de staging y protección (lectura autenticada)

**Fecha de inspección:** 2026-10-09. URL: https://staging.jbtecnologiamed.com.co. WPVibe `site_info` respondió `verified`, alcance `Authenticated read only`. No se ha editado.

## Observado
- Sitio `JB Tecnologia MED`, activo `Woodmart Child 1.0.0`.
- WooCommerce, Composite Products y Elementor activos. Página inicial Elementor 10625.
- Cabecera renderizada aún contiene `+1 212-334-0212` y elementos demo.
- `<meta name="robots" content="max-image-preview:large">` en el HTML del staging: **no se observó `noindex` en head**. Es necesario comprobar también cabeceras HTTP/robots y la opción WordPress; no asumir que los buscadores ya la bloquearon.
- WPVibe Connect plugin no instalado en staging: lectura REST funciona, ediciones seguras de archivos/draft theme no están habilitadas.
- No se pudo confirmar desde esta lectura si la base SQL está realmente aislada ni si se desactivaron webhooks, correos y pasarelas.

## Puerta de entrada para cambios en staging
- [ ] Acceso restringido mediante autenticación/restricción del servidor.
- [ ] Confirmación de `noindex` y protección anti-indexación para staging.
- [ ] Confirmación técnica: BD de staging diferente a producción.
- [ ] Correos, procesadores de pago, webhooks y automatizaciones hacia externos bloqueados o modo sandbox.
- [ ] Backup completo probado/restaurable, fecha y propietario.
- [ ] Validación de URL, SSL, favicon y rutas de WordPress.
- [ ] Instalar WPVibe Connect solo tras decisión y autorización, si se necesita editar archivos desde el conector.

**Prohibido**: publicar staging mediante reemplazo total de DB sobre producción sin análisis de pedidos/cambios. No almacenar contraseñas ni datos personales en este repo público.
