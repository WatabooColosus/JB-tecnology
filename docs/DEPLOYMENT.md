# GitHub ↔ Hostinger ↔ WordPress

**No existe despliegue automático ni sincronización en tiempo real.**
- GitHub: fuente de código propio, documentos, pruebas y PR.
- WordPress/Hostinger: fuente de contenido Elementor, menús, productos y pedidos.
- WPVibe: conexión autenticada de lectura verificada; no se probaron escrituras.

Procedimiento: respaldar archivos y DB → crear staging aislado → inspeccionar datos efectivos → PR y CI → importar cambios propios al tema hijo en staging → comprobar escritorio/móvil y WooCommerce → aprobación → deploy manual → auditoría posterior con SHA y fecha.

No incluir secretos, backups, pedidos, registros de compradores, plugins premium o temas comerciales en repositorios públicos.

## BuildCores
Integración **planeada, no activa**. Adaptador backend aislado para IDs/SKUs, reglas de compatibilidad y seguridad. Verificar API, credenciales, tarifas y contrato; no exponer llaves permanentes.
