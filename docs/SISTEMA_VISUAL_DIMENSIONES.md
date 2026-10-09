# Sistema visual y dimensiones · versión provisional 0.1

**Carácter:** experiencia tecnológica premium; oscuro/grafito + plata, acento turquesa/cian acorde con los dos nuevos logotipos. **No son códigos oficiales de marca**: se actualizarán al recibir el manual definitivo.

## Tokens provisionales
| Token | Propuesta | Uso |
|---|---|---|
| fondo | `#0C141B` | cabecera, hero, footer |
| superficie | `#132631` | cards, dropdowns |
| superficie elevada | `#1A3540` | megamenús |
| cian | `#43CED0` | botones, foco, estados |
| plata | `#EDF2F4` | texto principal |
| texto secundario | `#A5BEC6` | descripciones |
| borde | `#2A404B` | separadores |

Usar gradientes, líneas de circuito y destellos con moderación. Mantener presencia empresarial y gaming sin efectos que dificulten lectura. No introducir logo dibujado por CSS como si fuera el oficial. Usar logo oficial cuando se proporcione PNG/SVG apto.

## Dimensiones de diseño (objetivos, no tamaños verificados de la plantilla)
| Vista objetivo | Ancho viewport | Retícula | Container máximo | Gutter |
|---|---:|---|---:|---:|
| móvil pequeño | 360 px | 4 columnas | 100% − 32 px | 16 px |
| móvil estándar | 390 / 430 px | 4 columnas | 100% − 32 px | 16 px |
| tablet | 768 px | 8 columnas | 100% − 40 px | 20 px |
| portátil | 1024 px | 12 columnas | 100% − 48 px | 20 px |
| escritorio | 1440 px | 12 columnas | 1280 px | 24 px |
| ultrawide | 1920 px | 12 columnas | 1280 px | 24 px |

**Breakpoints candidatos:** 640px, 768px, 1024px y 1280px. Ajustar después de leer breakpoints de WoodMart/Elementor activos; no duplicar media queries sin necesidad.

## Especificación por elemento
| Elemento | Desktop propuesto | Tablet | Móvil |
|---|---|---|---|
| Header | 76–88 px + barra superior opcional | 72–80 px | 60–72 px, menú off-canvas |
| Hero/slider | área ~520–660 px alto | ~420–560 px | altura por contenido (sin recorte de textos) |
| Trio hogar/empresa/gaming | 3 tarjetas (4 columnas c/u) | 2+1 según imagen | 1 por fila o carrusel accesible |
| Megamenú | 3–5 columnas, navegación teclado | lista compacta | acordeones |
| Producto | 4 columnas | 2–3 columnas | 1–2 columnas, anchura legible |
| Blog | 3 cards | 2 cards | 1 card |
| Footer | 4–5 columnas | 2–3 columnas | 1 columna con grupos |
| Botones táctiles | ≥ 44 × 44 px | ≥ 44 × 44 px | ≥ 44 × 44 px |

**Recursos gráficos orientativos:** slider amplio 16:9 o 21:9 según fotografía y responsive; banner intermedio 2:1; cards 4:5/3:4; categorías 1:1; fotos de producto preferentemente 1:1 con `object-fit:contain` para no cortar componentes. Exportar WebP/AVIF cuando compatible, `srcset`, `sizes`, lazy load bajo el primer viewport y LCP hero prioritario.

## Animaciones e interacción
- Microinteracciones hover/focus 120–240 ms; desplazamiento 2–4 px, no parallax pesado por defecto.
- Menús tipo megamenú WoodMart; carga AJAX nativa donde aporte y se confirme su compatibilidad.
- Variaciones de productos con WooCommerce + WoodMart swatches antes de AJAX personalizado.
- Respeto `prefers-reduced-motion`; sin animaciones de scroll que oculten información.
- No depender de hover para descubrir categorías en móvil.
- Navegación por teclado, estado focus visible, contraste WCAG AA y etiquetas accesibles.

## Objetivos de pruebas (no resultados actuales)
- Mobile sin scroll horizontal ni textos desbordados.
- Lighthouse performance y accessibility ≥90 como objetivo, revisar datos reales.
- LCP ideal ≤2.5s, CLS ≤0.1, INP ≤200ms en usuarios reales cuando haya datos; no prometer estas cifras antes de medir.
