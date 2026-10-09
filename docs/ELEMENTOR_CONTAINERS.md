# Mapa de contenedores · Inspección real Elementor de staging

Fuente autenticada: WordPress Abilities API `hostinger-ai/elementor-get-page-structure`, post **10625**, 2026-10-09. Este informe corrige una hipótesis anterior: los IDs `7565dcd`, `b87a7ba`, `415d62f` observados en HTML del slider no están registrados como widgets individuales en el árbol principal de la página.

## Hero original
```text
7568552 contenedor hero
├─ 2d3e32a contenedor slider
│  └─ 92fe419 wd_slider — Hogar, Soluciones Empresariales, Gaming
└─ 2c204d2 contenedor banners
   ├─ a594443 wd_banner — Redragon
   └─ 632a8bd contenedor
      ├─ 358b342 wd_banner — Arma tu PC
      └─ 0edf505 wd_banner — Servicio técnico
```

Los tres slides internos de `wd_slider` podrían ser contenido de tipo slide propio de WoodMart: **antes de editarlos, inspeccionar el tipo de contenido, ID de cada slide y API guardado específica**. No usar los IDs renderizados de slide como `elementor_widget_id`.

## Otras secciones
| Root container | Widgets comprobados | Función |
|---|---|---|
| `8c17414` | `a4f058a` título · `0a8805a` categorías | Grid de categorías |
| `83672e3` | `f39b027` título · `b06b2e1` botón · `02967c8` productos | Ofertas |
| `ccf832f` | `add2d95` banner · `24979cf` título · `6d5ed1b` productos | Oferta + New Goods |
| `9b34239` | `9d5db0c` título · `c641c25` temporizador · `361c1c4` productos | Redragon, **con fondo de imagen** |
| `0589a74` | `9a9fd19` título · `8f79708` productos | Más productos |
| `3f0349b` | `ae86de8` título · `a34aa36`, `8370220`, `1a971bc` banners · `bac3fab` productos | Bloques secundarios |
| `e15b1f2` | `2873ffc` productos | Vistos recientemente |
| `a8d67dc` | `3a1cee8` título · `1bb77de` blog | Blog |
| `34936cb` | `1e52912` título · `fdc69ab` texto · `261f538` botón | Cierre corporativo |

La estructura exhaustiva está en [`data/elementor-structure.json`](../data/elementor-structure.json). Los bloques empresariales adicionales de la narración comercial no tienen todos contenedores independientes observados: se diseñarán sin forzar equivalencias falsas.

## Política de implementación
1. Proteger staging (`blog_public=0` y bloqueo de acceso/automatizaciones).
2. Identificar fuente del `wd_slider` y menú Header Builder, distinguir WordPress Menu ID y Template ID.
3. Diseñar CSS aislado antes de alterar widgets.
4. Implementar y comparar screenshots; registrar before/after con evidencia no sensible.
5. Nunca sobrescribir contenido de Elementor con JSON reconstruido ni fondos de video/imagen por error.
