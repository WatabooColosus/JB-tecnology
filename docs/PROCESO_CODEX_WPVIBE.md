# Procedimiento Codex + WPVibe · flujo auditable

1. Antes de cualquier cambio: leer `AGENTS.md`, `data/landing-spec.json`, `data/backlog.json`, `docs/STAGING_SECURITY.md`.
2. Escoger **una tarea** de GitHub Issues y verificar dependencias. Reflejar enlace de issue en PR.
3. Consultar estado de staging actual: tema, plugins, rutas, menú y padre real del widget Elementor. Guardar solo metadatos no sensibles.
4. Cambiar código propio en una rama; probar local; elaborar vista responsive 360,390,430,768,1024,1440,1920.
5. Tras aprobar seguridad, probar en staging mediante editor Elementor/WoodMart o integración autorizada; documentar método, copias de seguridad y reversión.
6. Hacer QA: contraste, tabulación, Escape, sticky/menú móvil, CTA funcionales, contenido sin datos demo, WooCommerce sin alteraciones.
7. Actualizar issue con evidencia mínima (sin pedidos/clientes). PR: diff, pruebas, capturas no sensibles, riesgos, rollback.
8. Fusionar solo cuando verificaciones estén en verde y la revisión haya aprobado el alcance. **No desplegar automáticamente a producción.**

## Semántica de estado
`pending` no es `done`. «CI verde» comprueba el código listado pero **no confirma** funcionamiento de WordPress ni pruebas de pagos.
