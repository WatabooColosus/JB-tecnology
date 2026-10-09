# Landing maestra · JB Tecnología MED · Fase 1

**Fuente:** secuencia expresada por el propietario, cotejada contra títulos visibles e IDs de widgets de Elementor en las páginas de producción y staging. La portada actual es **página 10625**, denominada internamente *Home Mega-electronics*.

**Principio:** no sustituir WoodMart ni destruir contenedores existentes. Adaptar cada grid en staging después de comprobar el elemento padre, las dependencias y los enlaces. Nada de contenido inventado ni productos ficticios.

## Orden obligatorio y finalidad

| # | Bloque declarado | Referencia identificada | ID de widget | Propósito y contenido |
|---|---|---|---|---|
| 01 | Computadoras para tu Hogar | observado | 7565dcd | Sección de hogar con imagen contextual y enlace válido |
| 02 | Soluciones Empresariales | observado | b87a7ba | Presentación B2B con oferta verificable |
| 03 | Gaming | observado | 415d62f | Identidad gamer premium sin saturación |
| 04 | Tienda Oficial Redragon | observado | a594443 | Solo usar palabra oficial con autorización de marca |
| 05 | Arma tu PC | observado | 358b342 | Sin fingir conexión BuildCores; formulario o ruta real |
| 06 | Servicio Técnico | observado | 0edf505 | Describir servicios y canal verificable |
| 07 | Categorías | observado | a4f058a | Mostrar categorías comerciales aprobadas, no demos |
| 08 | Lo más Vendido | observado | f39b027 | Solo ranking derivado de pedidos reales; si no, Productos destacados |
| 09 | Promociones especiales y más productos | parcial | add2d95 | Fechas precios y stock validados |
| 10 | Redragon más fuerte | observado | 9d5db0c | Visual distintivo condicionado a licencias |
| 11 | Productos Redragon | parcial | pendiente | No reemplazar demo por productos inventados |
| 12 | Más productos variables | parcial | pendiente | Swatches e imagen variante nativas primero; AJAX futuro |
| 13 | JB Tecnología Soluciones Empresariales y Digitales | solicitado | pendiente | Diferenciar área empresarial, software, hardware y soporte |
| 14 | 1A · 2B · 3C | solicitado | pendiente | Tres beneficios reales; significado pendiente de definición |
| 15 | Sector empresarial | solicitado | pendiente | Casos por sector y contacto comercial, sin cifras inventadas |
| 16 | Blog | observado | 3a1cee8 | Sustituir 5 blogs demo por contenidos propios |
| 17 | Términos y Condiciones | solicitado | pendiente | Textos legales validados; no encubrir páginas vacías |
| 18 | Lugares / Dirección / Empresa | solicitado | pendiente | Dirección y teléfonos reales; quitar ubicaciones demo USA |
| 19 | Footer | observado | pendiente | Menús footer y datos corporativos reales |

> La tabla NO implica que los 19 bloques existan como contenedores aislados. Las secciones de la parte baja son **requisitos comerciales** y deben localizarse o crearse con cuidado. Los IDs son solo referencia de widgets del snapshot.

## Especificación visual por familia
- **Hero principal:** tres mundos (hogar / soluciones empresariales / gaming) con cards gráficas diferenciadas, fondos creíbles, CTA verificables, tratamiento consistente de la marca JB.
- **Redragon:** espacio propio de alto impacto con banner, manifiesto, productos SOLO cuando marcas/autoridades/SKUs estén confirmados. Utilizar «Redragon» sin «Tienda Oficial» si la autorización no ha sido presentada.
- **Arma tu PC:** bloque conceptual preparado para Composite Products; experiencia de selección y futura vista 3D BuildCores. Por ahora, CTA de cotización/asesoría, no fingir funcionamiento.
- **Servicios:** servicio técnico, software y soluciones empresariales con contacto, diferenciación por segmento y credenciales verificables.
- **Catálogo editorial:** categorías, destacados, más vendidos solo con datos de pedidos reales, promociones vigentes con fechas, tarjetas variables cuando esté lista la base de producto.
- **Confianza corporativa:** 1A/2B/3C no tiene significado comercial confirmado; definir con cliente antes de titularlo. Blog propio, términos, contacto y footer sin direcciones ficticias.

## Jerarquía y CTA
Todos los CTA deberán describir la acción real (explorar, solicitar asesoría, cotizar, leer). **Cero enlaces `href="#"`** una vez aprobada la fase. Si una página no existe: usar ancla real válida, formulario real o desactivar el botón.

## Activos
- Logos nuevos aprobados sustituyen JB Pulse. Manual final **en desarrollo** por el cliente.
- Evitar introducir imágenes demo de WoodMart o logotipos Redragon no autorizados en productos.
- La publicación deberá incluir imágenes propias con textos alternativos, crops optimizados y derechos comprobados.

## Fuente estructurada
`data/landing-spec.json` aporta orden, objetivo, estado observado, CTA y tarea de cada bloque. Se versiona en Git; WooCommerce y Elementor siguen siendo la fuente de verdad del sitio.
