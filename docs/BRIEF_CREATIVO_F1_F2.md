# JB Tecnología MED — Brief creativo y plan de imágenes F1–F2

**Versión:** 1.0 · **Fecha:** 2026-10-09 · **Estado:** propuesta para revisión, no implementada en Elementor · **Sitio:** staging.jbtecnologiamed.com.co · **Portada:** WordPress/Elementor ID `10625`

**Fuentes trazables:** [landing-spec.json](../data/landing-spec.json), [elementor-structure.json](../data/elementor-structure.json), [brand-provisional.json](../data/brand-provisional.json). La lista maestra, con fichas y prompts completos, está en [image-asset-plan.json](../data/image-asset-plan.json).

## 1. Dirección de arte, fase 1

**Concepto:** «Tecnología que impulsa cada mundo». Tres ambientes narrativos conectados (Hogar cálido, Empresa confiable, Gaming potente), una sola firma visual de grafito mate, plata, cian controlado y reflejos de fotografía editorial. Para Redragon, acento rojo únicamente cuando el producto/permiso sea auténtico.

- **Marca:** dos logos originales JB aportados por el propietario, *sin regenerar ni deformar*; códigos cromáticos temporales `#0C141B`, `#43CED0`, `#EDF2F4`; manual oficial pendiente.
- **Fotografía:** materiales físicos creíbles, escala real, dispositivos no deformados, iluminación volumétrica sobria, sin luces artificiales excesivas. Composición con espacio negativo para títulos editables.
- **Copy:** español de Colombia, directo, legible, sin inventar precios, garantía, convenios, plazo de atención, ventas históricas ni direcciones.
- **Diseño:** textos y botones HTML de Elementor/WoodMart; NO insertar tipografía dentro del archivo de imagen. Tamaño táctil >=44px; contraste WCAG AA objetivo.
- **Visuales de catálogo:** SKU auténticos con fuente/licencia acreditada; generación IA solo para imágenes conceptuales donde no se anuncia referencia concreta. No usar personajes identificables ni fotografías falsas de instalaciones JB.
- **Edición conservadora:** respetar `wd_slider`, widgets de `wd_products`, imágenes de variaciones, carruseles y fondos Elementor; no reconstruir su JSON.

## 2. Matriz de los 19 bloques comerciales

El inventario real de Elementor contiene menos de 19 bloques autónomos. Las referencias «por identificar» representan componentes comerciales solicitados, no contenedores que ya existan.

| # | Bloque | Referencia técnica | Imágenes | Titular propuesto | CTA propuesto | Issue | Estado |
|---|---|---|---|---|---|---|---|
| 01 | Computadoras para tu Hogar | `wd_slider 92fe419` | JB-IMG-001 | Tecnología que acompaña tu día | Explorar equipos | HOME-02 | Pendiente |
| 02 | Soluciones Empresariales | `wd_slider 92fe419` | JB-IMG-002 | Soluciones que impulsan tu empresa | Solicitar asesoría | HOME-02 | Pendiente |
| 03 | Gaming | `wd_slider 92fe419` | JB-IMG-003 | Potencia para cada partida | Explorar gaming | HOME-02 | Pendiente |
| 04 | Tienda Oficial Redragon | `a594443` | JB-IMG-004 | Universo Redragon | Ver Redragon | HOME-03 | Pendiente |
| 05 | Arma tu PC | `358b342` | JB-IMG-005 | Construye tu próxima PC | Solicitar cotización | HOME-04 | Pendiente |
| 06 | Servicio Técnico | `0edf505` | JB-IMG-006 | Servicio técnico especializado | Solicitar diagnóstico | HOME-04 | Pendiente |
| 07 | Categorías | `a4f058a` | JB-IMG-007, JB-IMG-008, JB-IMG-009, JB-IMG-010, JB-IMG-011, JB-IMG-012 | Explora nuestras categorías | Ver categorías | HOME-05 | Pendiente |
| 08 | Lo más Vendido | `f39b027` | JB-IMG-013 | Productos destacados | Explorar productos | HOME-05 | Pendiente |
| 09 | Promociones especiales y más productos | `add2d95` | JB-IMG-014 | Oportunidades para actualizarte | Ver promociones | HOME-05 | Pendiente |
| 10 | Redragon más fuerte | `9d5db0c` | JB-IMG-015 | Tu zona Redragon | Descubrir colección | HOME-03 | Pendiente |
| 11 | Productos Redragon | contenedor `9b34239` | JB-IMG-016 | Productos Redragon | Ver productos | HOME-03 | Pendiente |
| 12 | Más productos variables | contenedor `0589a74` | JB-IMG-017 | Opciones que se adaptan a ti | Ver opciones | CAT-02 | Pendiente |
| 13 | JB Tecnología Soluciones Empresariales y Digitales | Por identificar/crear | JB-IMG-018 | Tecnología para tu operación | Conocer soluciones | HOME-06 | Pendiente |
| 14 | 1A · 2B · 3C | Por identificar/crear | JB-IMG-019 | Tres razones para elegirnos | Conocer ventajas | HOME-06 | Pendiente |
| 15 | Sector empresarial | Por identificar/crear | JB-IMG-020, JB-IMG-021, JB-IMG-022 | Soluciones para distintos negocios | Solicitar propuesta | HOME-06 | Pendiente |
| 16 | Blog | `3a1cee8` | JB-IMG-023, JB-IMG-024, JB-IMG-025 | Ideas para decidir mejor | Leer artículos | LEGAL-01 | Pendiente |
| 17 | Términos y Condiciones | Por identificar/crear | Sin imagen nueva | Información clara para comprar | Consultar términos | LEGAL-01 | Pendiente |
| 18 | Lugares / Dirección / Empresa | Por identificar/crear | JB-IMG-026 | Hablemos de tu próximo proyecto | Contactar | HOME-06 | Pendiente |
| 19 | Footer | contenedor `34936cb` | JB-IMG-027 | JB Tecnología MED | Ver información | HOME-06 | Pendiente |

**Reglas de publicación:** los CTA apuntarán solo a páginas comprobadas, formularios operativos o categorías reales; jamás a `#`. El texto descriptivo propuesto para cada sección se conserva en `data/image-asset-plan.json`. La etiqueta «Tienda Oficial Redragon» se reemplaza provisionalmente por «Universo Redragon» hasta verificar autorización. «Lo más vendido» será «Productos destacados» salvo contar con datos reales. «1A · 2B · 3C» permanece sin significado asignado.

## 3. Inventario visual, fase 2 — 27 fichas

**Convención de archivo:** `JB-IMG-001-hero-hogar-v01.webp`, seguido de revisiones numeradas y sus variantes `-mobile`. Registrar el SHA-256 de cada archivo final. Ninguna de estas fichas implica que la imagen ya exista.

| Asset | Uso | Exportación objetivo (px) | Política de procedencia | Referencia | Estado |
|---|---|---|---|---|---|
| JB-IMG-001 | Hero hogar | 1920x800 + 1080x1350 | Generar | 92fe419 / slides WoodMart (relación pendiente) | Pendiente |
| JB-IMG-002 | Hero empresas | 1920x800 + 1080x1350 | Generar | 92fe419 / slides WoodMart (relación pendiente) | Pendiente |
| JB-IMG-003 | Hero gaming | 1920x800 + 1080x1350 | Generar | 92fe419 / slides WoodMart (relación pendiente) | Pendiente |
| JB-IMG-004 | Banner Redragon | 1200x480 + 800x1000 | Fuente oficial o fotografía propia | a594443 | Pendiente |
| JB-IMG-005 | Arma tu PC | 1200x740 + 800x1000 | Generar conceptual | 358b342 | Pendiente |
| JB-IMG-006 | Servicio técnico | 1200x740 + 800x1000 | Generar conceptual o foto propia | 0edf505 | Pendiente |
| JB-IMG-007 | Categoría portátiles | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-008 | Categoría computadores | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-009 | Categoría gaming | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-010 | Categoría componentes | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-011 | Categoría periféricos | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-012 | Categoría monitores | 800x800 | Foto comercial/SKU | 0a8805a | Pendiente |
| JB-IMG-013 | Tarjetas destacados | 1000x1000 | Solo fotografía real de SKU | 02967c8 | Pendiente |
| JB-IMG-014 | Campaña promociones | 1200x1440 + 1200x600 | Generar sin oferta | add2d95 | Pendiente |
| JB-IMG-015 | Redragon inmersivo | 1600x900 + 1080x1350 | Fuente oficial/SKU real | 9b34239 / imagen fondo a verificar | Pendiente |
| JB-IMG-016 | Colección productos Redragon | 1000x1000 | Solo catálogo real | 361c1c4 | Pendiente |
| JB-IMG-017 | Productos con variaciones | 1000x1000 por variación | Solo fotos reales por variación | 8f79708 | Pendiente |
| JB-IMG-018 | Panel soluciones empresariales | 1600x900 + 1080x1350 | Generar conceptual | Sección requerida, widget aún no asignado | Pendiente |
| JB-IMG-019 | 1A · 2B · 3C | 3 x 600x600 | No generar hasta definir significado | Sección requerida, significado pendiente | Pendiente |
| JB-IMG-020 | Sector salud/servicios | 1200x800 | Generar conceptual | Sector empresarial por definir | Pendiente |
| JB-IMG-021 | Sector comercio | 1200x800 | Generar conceptual | Sector empresarial por definir | Pendiente |
| JB-IMG-022 | Sector oficinas | 1200x800 | Generar conceptual | Sector empresarial por definir | Pendiente |
| JB-IMG-023 | Blog: elegir computador | 1200x675 | Generar editorial | 1bb77de / artículo nuevo | Pendiente |
| JB-IMG-024 | Blog: cuidado y mantenimiento | 1200x675 | Generar editorial | 1bb77de / artículo nuevo | Pendiente |
| JB-IMG-025 | Blog: gaming equilibrado | 1200x675 | Generar editorial | 1bb77de / artículo nuevo | Pendiente |
| JB-IMG-026 | Empresa y ubicación | 1600x900 | Solo fotografía real | Sección ubicación requerida | Pendiente |
| JB-IMG-027 | Textura footer | 1600x400 | Generar opcional | Footer / revisar estructura WoodMart | Pendiente |

**Formatos:** preferencia WebP o AVIF compatible; con JPEG/PNG como fuente cuando corresponda. Exportaciones del hero desktop y crop vertical independientes. No forzar imagen vertical mediante recorte del ancho original. Dimensiones *propuestas*, no medición final del widget. Optimizar por prueba real y presupuesto de bytes, evitando umbrales únicos sin conocer detalle/compresión. No hacer lazy-load del principal elemento LCP; usar `srcset`/`sizes` cuando WoodMart lo soporte.

## 4. Prompts de producción por ficha

**Prefijo creativo común (usar solo para recursos conceptuales):**

> Fotografía publicitaria editorial de tecnología premium, hiperrealista sin exceso de CGI, composición profesional, superficies grafito cepillado y acentos luminosos cian suaves, iluminación física creíble, materiales precisos, profundidad de campo controlada, colorimetría coherente con JB Tecnología MED, aspecto limpio, sin palabras, sin letras, sin precios, sin marcas añadidas, sin logotipos inventados, sin marcas de agua, sin personas con rostros protagonistas salvo necesidad comercial, espacio negativo para tipografía HTML. No modificar geometría de productos reales.

### JB-IMG-001 — Hero hogar

- **Destino:** 92fe419 / slides WoodMart (relación pendiente); **dimensión:** 1920x800 + 1080x1350; **espacio negativo:** izquierda 40%.
- **Origen permitido:** Generar.
- **Prompt/brief individual:** Escritorio doméstico contemporáneo con portátil y monitor de uso cotidiano, planta sutil, luz de mañana a través de ventana, ambiente acogedor y profesional; escena principal desplazada a la derecha; pantalla neutra sin interfaces ni marcas inventadas.
- **Issue:** HOME-02; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-002 — Hero empresas

- **Destino:** 92fe419 / slides WoodMart (relación pendiente); **dimensión:** 1920x800 + 1080x1350; **espacio negativo:** izquierda 45%.
- **Origen permitido:** Generar.
- **Prompt/brief individual:** Espacio empresarial colombiano contemporáneo, estaciones de trabajo ordenadas, portátiles empresariales, monitor y red cableada discretos, iluminación azul de amanecer, entorno realista sin personas identificables; producto a la derecha, zona limpia a la izquierda.
- **Issue:** HOME-02; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-003 — Hero gaming

- **Destino:** 92fe419 / slides WoodMart (relación pendiente); **dimensión:** 1920x800 + 1080x1350; **espacio negativo:** izquierda 40%.
- **Origen permitido:** Generar.
- **Prompt/brief individual:** Setup gaming de alto desempeño con torre de panel transparente, refrigeración de aire creíble, doble monitor apagado o interfaz abstracta sin texto, teclado y mouse de aspecto realista, luces RGB cian y violeta discretas; sin estética juvenil excesiva.
- **Issue:** HOME-02; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-004 — Banner Redragon

- **Destino:** a594443; **dimensión:** 1200x480 + 800x1000; **espacio negativo:** izquierda 40%.
- **Origen permitido:** Fuente oficial o fotografía propia.
- **Prompt/brief individual:** Composición de periféricos Redragon auténticos procedentes de fotografías autorizadas de SKU verificados: teclado mecánico, ratón y auriculares, iluminación dramática neutra sobre superficie negra; acento rojo distintivo, sin redibujar el producto, ni alterar marca o referencia.
- **Issue:** HOME-03; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-005 — Arma tu PC

- **Destino:** 358b342; **dimensión:** 1200x740 + 800x1000; **espacio negativo:** izquierda 40%.
- **Origen permitido:** Generar conceptual.
- **Prompt/brief individual:** Gabinete de escritorio abierto con placa base, memoria, GPU y cableado técnicamente coherentes, proceso ordenado de montaje en estación profesional, brillo cian suave; sin piezas flotantes irreales ni etiqueta de configuración activa.
- **Issue:** HOME-04; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-006 — Servicio técnico

- **Destino:** 0edf505; **dimensión:** 1200x740 + 800x1000; **espacio negativo:** izquierda 40%.
- **Origen permitido:** Generar conceptual o foto propia.
- **Prompt/brief individual:** Manos de profesional revisando laptop abierta sobre tapete antiestático, herramientas de precisión, iluminación limpia de taller de informática, circuito y componentes verosímiles, sin indicar reparación específica no ofrecida.
- **Issue:** HOME-04; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-007 — Categoría portátiles

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** Portátil empresarial real fotografiado tres cuartos sobre fondo blanco roto con sombra delicada, producto completo sin recorte ni deformaciones; sustituir por fotografía de catálogo del SKU al activar comercio.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-008 — Categoría computadores

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** Torre de escritorio y monitor de oficina real en composición angular, iluminación suave, fondo neutro; la versión final debe corresponder a equipos efectivamente comercializados.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-009 — Categoría gaming

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** PC de escritorio gaming real con ventana lateral, iluminación cian y accesorios medidos, escena limpia sobre fondo neutro; no confundir con marcas/modelos no vendidos.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-010 — Categoría componentes

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** Placa base, memoria RAM y tarjeta gráfica como bodegón de componentes reales, empaque limpio sin texto fabricado, fondo neutro; cada componente final debe pertenecer al catálogo.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-011 — Categoría periféricos

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** Teclado, ratón y audífonos auténticos fotografiados sobre mesa grafito, luz lateral y sombra controlada; respetar colores y logotipos tal como aparecen en el producto.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-012 — Categoría monitores

- **Destino:** 0a8805a; **dimensión:** 800x800; **espacio negativo:** centro.
- **Origen permitido:** Foto comercial/SKU.
- **Prompt/brief individual:** Monitor real de escritorio, vista frontal tres cuartos con pantalla abstracta sin promesas de resolución; usar SKU propio antes de publicar.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-013 — Tarjetas destacados

- **Destino:** 02967c8; **dimensión:** 1000x1000; **espacio negativo:** centro.
- **Origen permitido:** Solo fotografía real de SKU.
- **Prompt/brief individual:** Fotografía de ficha de producto aprobada, fondo uniforme, resolución nítida, producto completo y colores exactos; prohibido inventar precios, modelos o distintivos de más vendidos.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-014 — Campaña promociones

- **Destino:** add2d95; **dimensión:** 1200x1440 + 1200x600; **espacio negativo:** derecha 60%.
- **Origen permitido:** Generar sin oferta.
- **Prompt/brief individual:** Composición aspiracional de tecnología doméstica y de oficina sin marcas, superficies metálicas, reflejos suaves cian, energía comercial elegante, espacio libre amplio para oferta validada que se compondrá en HTML; no incluir descuentos ni temporizadores.
- **Issue:** HOME-05; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-015 — Redragon inmersivo

- **Destino:** 9b34239 / imagen fondo a verificar; **dimensión:** 1600x900 + 1080x1350; **espacio negativo:** derecha 60%.
- **Origen permitido:** Fuente oficial/SKU real.
- **Prompt/brief individual:** Fotografía de producto Redragon auténtico en escenario gaming nocturno, contraste grafito/rojo, ángulo heroico, atmósfera controlada, halo de iluminación cian secundario; sin simulación de acuerdos oficiales ni fotografías de productos ficticios.
- **Issue:** HOME-03; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-016 — Colección productos Redragon

- **Destino:** 361c1c4; **dimensión:** 1000x1000; **espacio negativo:** centro.
- **Origen permitido:** Solo catálogo real.
- **Prompt/brief individual:** Fotografía individual de cada SKU Redragon autorizado para comercialización, fondo limpio, color y accesorios exactos, incluir variante real y detalles técnicos comprobados.
- **Issue:** HOME-03; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-017 — Productos con variaciones

- **Destino:** 8f79708; **dimensión:** 1000x1000 por variación; **espacio negativo:** centro.
- **Origen permitido:** Solo fotos reales por variación.
- **Prompt/brief individual:** Conjunto de tomas reproducibles del mismo SKU para cada color, capacidad o configuración realmente disponible; misma cámara e iluminación, sin editar o inventar características.
- **Issue:** CAT-02; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-018 — Panel soluciones empresariales

- **Destino:** Sección requerida, widget aún no asignado; **dimensión:** 1600x900 + 1080x1350; **espacio negativo:** izquierda 45%.
- **Origen permitido:** Generar conceptual.
- **Prompt/brief individual:** Interior de pyme tecnológica con estación de trabajo, impresora de oficina, pantalla de soporte y equipo de red, ambiente funcional moderno, luz natural equilibrada; productos genuinos genéricos sin marcas inventadas.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-019 — 1A · 2B · 3C

- **Destino:** Sección requerida, significado pendiente; **dimensión:** 3 x 600x600; **espacio negativo:** centro.
- **Origen permitido:** No generar hasta definir significado.
- **Prompt/brief individual:** Reservar tres iconos vectoriales de trazo consistente solo tras recibir significado y pruebas de los tres beneficios: no inferir 1A/2B/3C.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-020 — Sector salud/servicios

- **Destino:** Sector empresarial por definir; **dimensión:** 1200x800; **espacio negativo:** derecha 60%.
- **Origen permitido:** Generar conceptual.
- **Prompt/brief individual:** Oficina de servicios profesionales con estaciones de trabajo y soporte informático, sin inventar contratos, clientes ni instalaciones hospitalarias atribuidas a JB.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-021 — Sector comercio

- **Destino:** Sector empresarial por definir; **dimensión:** 1200x800; **espacio negativo:** derecha 60%.
- **Origen permitido:** Generar conceptual.
- **Prompt/brief individual:** Pequeño comercio con computador de punto de venta genérico y escáner de código de barras sin logotipo, iluminación de entorno comercial realista, sin simular software propio ya integrado.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-022 — Sector oficinas

- **Destino:** Sector empresarial por definir; **dimensión:** 1200x800; **espacio negativo:** derecha 60%.
- **Origen permitido:** Generar conceptual.
- **Prompt/brief individual:** Oficina de equipo pequeño colaborando con portátiles y monitores discretos, escena ordenada y profesional, sin personas identificables ni marcas ficticias.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-023 — Blog: elegir computador

- **Destino:** 1bb77de / artículo nuevo; **dimensión:** 1200x675; **espacio negativo:** centro derecha.
- **Origen permitido:** Generar editorial.
- **Prompt/brief individual:** Escritorio de trabajo con portátil y pantalla adicional, libreta, luz natural, perspectiva informativa tipo revista de tecnología, sin texto integrado.
- **Issue:** LEGAL-01; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-024 — Blog: cuidado y mantenimiento

- **Destino:** 1bb77de / artículo nuevo; **dimensión:** 1200x675; **espacio negativo:** centro derecha.
- **Origen permitido:** Generar editorial.
- **Prompt/brief individual:** Kit técnico profesional con laptop abierta, brocha antiestática y herramientas pequeñas, composición editorial informativa, componentes coherentes, sin instrucciones peligrosas.
- **Issue:** LEGAL-01; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-025 — Blog: gaming equilibrado

- **Destino:** 1bb77de / artículo nuevo; **dimensión:** 1200x675; **espacio negativo:** centro derecha.
- **Origen permitido:** Generar editorial.
- **Prompt/brief individual:** Espacio gaming ordenado con monitor, teclado y torre bien ventilada; estética editorial premium y neutra, iluminación cian discreta, sin logos falsos.
- **Issue:** LEGAL-01; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-026 — Empresa y ubicación

- **Destino:** Sección ubicación requerida; **dimensión:** 1600x900; **espacio negativo:** centro.
- **Origen permitido:** Solo fotografía real.
- **Prompt/brief individual:** Fotografía verificable del local, fachada o equipo JB Tecnología MED con consentimiento y localización validadas; no generar un local ficticio ni mostrar direcciones supuestas.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.

### JB-IMG-027 — Textura footer

- **Destino:** Footer / revisar estructura WoodMart; **dimensión:** 1600x400; **espacio negativo:** sin foco.
- **Origen permitido:** Generar opcional.
- **Prompt/brief individual:** Trama abstracta de líneas tecnológicas geométricas mínimas sobre grafito mate, acento cian casi imperceptible, contraste bajo para mantener legibilidad de enlaces legales.
- **Issue:** HOME-06; **estado:** diseño de referencia pendiente de aprobación y generación.


## 5. Flujo auditable y compuertas de aprobación

1. Guardar brief y cotejar orden + IDs de la landing y slide post types.
2. Aprobar titular/CTA/escena por bloque y verificar páginas destino reales.
3. Comprobar licencia para Redragon, fotografías de productos e instalaciones.
4. Producir imágenes conceptuales sin marcas falseadas; fotografiar/catalogar SKUs concretos.
5. Exportar variaciones desktop/mobile, realizar revisión de recorte, nitidez, peso y alt text.
6. **Antes de editar contenido o publicar:** crear backup posterior a la creación del staging, incluyendo BD independiente + carpeta `staging`; comprobar restauración selectiva.
7. Subir imágenes a Medios de **staging** únicamente; registrar `attachment_id`, URL y checksum local.
8. Cambiar widget correcto con herramientas nativas, conservar configuración completa y cachés; registrar `elementor_widget_id`/slide ID.
9. Verificar desktop 1440, tablet 768, mobile 390 y 360; comprobar CTA, foco, contraste, scroll y WooCommerce.
10. Guardar antes/después, resultados, enlaces a GitHub Issue/PR, fecha, aprobador, rollback y hash.
11. Solo tras la aprobación del titular publicar el tema/landing en staging. **Nunca activar sincronización staging→producción automáticamente**.

## 6. Registro mínimo de evidencia por recurso

`asset_id | issue | revision | source_license | generated_or_original | sha256 | wp_attachment_id | Elementor widget/slide | before_url | after_url | mobile_qa | desktop_qa | approved_by | approval_date | rollback | status`

Estados: `brief_preparado` → `aprobado_para_producir` → `asset_disponible` → `validado_en_staging` → `aprobado_para_publicar`. Ningún elemento sin pruebas puede figurar como realizado.

## 7. Bloqueadores conocidos y decisiones pendientes

- Falta un **respaldo posterior a la creación del staging**; el de 2026-10-08 17:59 (Bogotá) no contiene ese entorno.
- Aislamiento de BD staging/producción informado por Hostinger; evitar plugins conectados a servicios externos compartidos.
- Manual definitivo, archivos finales de los dos logos y autorizaciones para marcas/productos aún por aportar al sitio.
- 19 bloques comerciales no equivalen a 19 widgets independientes, y los tres slides requieren identificación propia en WoodMart.
- SKU reales, precios, promociones, tienda oficial Redragon, BuildCores, páginas destino y significado «1A · 2B · 3C» requieren verificación.
- CSS Fase 1.1/1.2 está en el tema **borrador WPVibe staging**, pero las últimas ampliaciones deben versionarse en el repositorio. No afirmar que todos los cambios están en GitHub.
