# Línea base verificada, 2026-10-08/09

Origen: WPVibe en lectura: WordPress, API REST WooCommerce y HTML de Elementor.
- WordPress con **Woodmart Child 1.0.0**, Elementor 4.3.4, WooCommerce 11.2.0 y Composite Products 11.1.3.
- Home: página 10625 «Home Mega-electronics», con widgets enumerados en `data/home-grid-map.json`.
- 18 páginas publicadas; 58 categorías de producto (7 principales); 19 productos; 6 menús; 5 posts de demo.
- 44 categorías con 0 productos directamente asignados (pueden tener descendientes).
- WooCommerce en COP; importes y productos son presumiblemente demo, no inventario comercial validado.
- 0 productos composite publicados en la consulta.
- Pasarelas consultadas: transferencia, cheque y contra reembolso; todas deshabilitadas.
- `/tienda/` y `/finalizar-compra/` devolvieron mensaje de próximo lanzamiento en inspección previa.
- Los primeros botones Compra, Solicita tu visita y Pre ordenar apuntan a `#`.
- Menús apuntan «Nosotros» a `/outlet/` y «Tienda» a `/stores/`, páginas de demo.
- Contactos/footer contienen direcciones estadounidenses y correo demo de WoodMart.
- Lighthouse móvil anterior: Rendimiento 93, Accesibilidad 93, Buenas prácticas 100, SEO 92 (medición de laboratorio).

**Pendiente:** archivos reales del tema hijo, staging, backup restaurable, catálogo, contacto real, autorización comercial Redragon, documentación/API BuildCores, prueba de pago E2E. Snapshot no equivale a monitoreo continuo.
