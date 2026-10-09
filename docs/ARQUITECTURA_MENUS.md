# Menús, megamenús y recorrido de compra — Fase 1A

El menú actual no equivale al propuesto. **Primero registrar la asignación real en Header Builder**; la REST API devuelve seis menús, pero sus `locations` están vacíos.

## Menús observados
| ID | Nombre WordPress | Misión tentativa |
|---:|---|---|
| 215 | Header menu Mega electronics | barra comercial |
| 216 | Header right menu | demo de países/divisas (USA, USD, GBP, EUR) |
| 217 | Main navigation | navegación principal (actual demo) |
| 218 | Mobile Categories Mega electronics | categorías móvil |
| 219 | Mobile navigation | navegación móvil |
| 220 | Sticky navigation Mega Electronics | barra sticky |

**Hallazgos:** «Tienda» apunta a `/stores/`; «Nosotros» a `/outlet/`; enlaces de países y monedas apuntan a `#`; «Computadores para Oficina» enlaza a periféricos; el header aún muestra el teléfono demo `+1 212-334-0212`.

## Navegación propuesta
**Principal:** Inicio · Equipos · Redragon · Arma tu PC · Empresas · Servicio técnico · Promociones · Blog · Contacto.
**Zona de utilidad:** buscar, cuenta, carrito, WhatsApp/asesoría (solo canal aprobado), categorías.
**Megamenú Equipos:** portátiles, PCs, componentes, monitores, periféricos, impresoras, soluciones de impresión.
**Megamenú Empresas:** equipos empresariales, software POS, servicios digitales, soporte técnico, solicitud de cotización.
**Megamenú Redragon:** periféricos, teclados, mouse, audífonos, accesorios (solo líneas realmente disponibles).
**Categorías**: nombres legibles en español y jerarquía comercial futura; no cambiar taxonomía hasta fase 2.

## Accesibilidad y estados
Foco visible, Tab/Enter/Escape, aria-expanded y gestión del foco; dropdown sin dependencia exclusiva de hover; menú táctil de ancho apropiado; sticky no bloquea contenido ni cart. Considerar búsqueda predictiva sin enviar datos del usuario a terceros no aprobados.

## Publicación
Solo modificar staging con backup, control de indexación y pagos/correos de prueba. No copiar la base de staging directamente a producción si hay pedidos nuevos.
