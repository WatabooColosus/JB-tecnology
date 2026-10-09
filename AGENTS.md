# Instrucciones para Codex — JB Tecnología MED

1. Leer README y `data/home-grid-map.json`, `docs/BASELINE.md` antes de editar.
2. La web pública https://jbtecnologiamed.com.co está en **modo solo lectura** mientras no haya staging probado y aprobación expresa de publicación.
3. Preservar WordPress, WoodMart padre, tema hijo, Elementor, WooCommerce y Composite Products. Código propio aislado en child theme o plugin propio.
4. GitHub registra código, no sincroniza automáticamente el contenido guardado en la base de datos WordPress. No reemplazar el JSON Elementor ni la DB mediante scripts arbitrarios.
5. Nunca publicar credenciales, backups SQL, datos de compradores, pedidos, licencias premium o claves de servicio.
6. No editar precios, inventario, pagos, usuarios, impuestos ni envíos sin permiso explícito.
7. No afirmar distribución oficial Redragon ni integración BuildCores sin comprobar ambas.
8. Trabajar en ramas con PR; validar inventarios, diffs, responsive, accesibilidad y staging. No merge ni deploy por defecto.
9. Distinguir los estados `observado`, `parcial`, `solicitado` y `sin verificar`; no inventar datos.
10. Los IDs de Elementor incluidos representan widgets, no necesariamente el contenedor padre.

## Fuente de trabajo de Fase 1 (actualización)
Leer además `data/landing-spec.json`, `data/backlog.json`, `docs/SISTEMA_VISUAL_DIMENSIONES.md`, `docs/STAGING_SECURITY.md`.
- Los 19 bloques mantienen su orden y nivel de evidencia; `status: pending` no demuestra implementación.
- Las Issues GitHub enlazadas desde backlog son la fuente del progreso operativo. Nunca marcar finalizado sin evidencia.
- **Bloqueo SEC-01:** staging está conectado, pero no se ha verificado noindex, control de acceso, aislamiento DB ni bloqueo de envíos reales. No hacer modificaciones hasta verificar estos puntos.
- Priorizar menús/landing; catálogo y BuildCores después. Respetar logos nuevos y manual futuro, Redragon oficial solo si hay autorización.
