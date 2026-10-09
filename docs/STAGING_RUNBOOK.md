# Runbook — Activación Hostinger WordPress Staging

**Estado inicial (2026-10-08):** instrucción de activación entregada; **no se ha comprobado creación del subdominio**.

## Propósito
Aislar trabajo de la **fase 1 de JB Tecnología MED** (Header Builder, megamenús, landing Elementor, estilos) de producción. No hay CD ni push automático a Hostinger. GitHub sigue siendo registro de decisiones, código propio y revisiones; Elementor/WooCommerce permanecen en su base de datos.

## Crear copia en hPanel (acción del titular)
1. hPanel → Sitios web → `jbtecnologiamed.com.co` → Panel de control.
2. WordPress → Staging → Crear staging.
3. Nombre propuesto: `staging`; **la URL resultante se debe confirmar** antes de usarla en herramientas.
4. Esperar duplicación; guardar URL definitiva y fecha en la sección «Evidencia».
5. Si no aparece Staging, comprobar plan (Business o superior) y detección de WordPress; no instalar plugins ni clonar bases de datos por improvisación.

Documentación: https://www.hostinger.com/support/5720286-how-to-create-a-wordpress-staging-environment-in-hostinger/

## Aislamiento / seguridad antes de trabajar
- Verificar que URL staging carga, tiene HTTPS y apunta a otro WordPress/base de datos; nunca probar cambios destructivos en producción.
- Restringir acceso a staging mediante autenticación a nivel servidor o equivalente. Marcar como **no indexable** en WordPress y evitar exposición de datos copiados.
- Comprobar que la copia no envía correos reales, no procesa pedidos ni cobros reales, ni llama a pasarelas o webhooks de producción. Preferir pagos deshabilitados / sandbox y notificaciones deshabilitadas en staging.
- No publicar capturas de contactos, clientes, pedidos, llaves, registros o ajustes sensibles en el repo público.
- Comprobar disponibilidad de backup restaurable antes de cualquier posterior despliegue.
- Validar licencias de WoodMart, Composite Products y otros plugins premium para staging.
- **NO usar el botón «Publicar» de Hostinger sin evaluación de diferencias en DB.** Hostinger avisa que reemplaza archivos y base de producción, perdiendo compras/cambios posteriores.

## Conectar la copia
1. Una vez confirmada la URL, ejecutar WPVibe `connect_site({site_url: URL_CONFIRMADA})`.
2. Completar autorización de WordPress desde el enlace de un solo clic.
3. Verificar `site_info` del staging y compararlo con producción (tema, plugins, versión).
4. Solo tras confirmar aislamiento, inspeccionar header real y contenedores padres Elementor. No editar aún producción.

## Estrategia de publicación futura
Evitar la sustitución completa de la DB si han entrado pedidos o cambió catálogo desde la creación del staging. Transferir exclusivamente cambios de theme/plugin y páginas/configuraciones identificadas con mecanismo apropiado, respaldos, pruebas y autorización explícita.

## Evidencia pendiente
- URL real de staging: **pendiente**
- Fecha de creación: **pendiente**
- Aislamiento confirmado: **pendiente**
- WPVibe staging verificado: **pendiente**
- Backup restaurable: **pendiente**
- Compras y pagos deshabilitados: **pendiente**
- Capturas responsive y aceptación: **pendiente**
