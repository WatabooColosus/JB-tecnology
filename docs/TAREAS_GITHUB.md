# Issues operativas · JB Tecnología MED

Fecha: 2026-10-09. El orden es jerárquico; no implica trabajos iniciados.

| Issue | Prioridad | Área | Trabajo | Depende |
|---|---|---|---|---|
| [#2](https://github.com/WatabooColosus/JB-tecnology/issues/2) (`SEC-01`) | P0 | staging | Preparar staging: aislamiento y noindex | — |
| [#3](https://github.com/WatabooColosus/JB-tecnology/issues/3) (`NAV-01`) | P1 | menu | Auditar WoodMart Header Builder y seis menús | `SEC-01` |
| [#4](https://github.com/WatabooColosus/JB-tecnology/issues/4) (`BRAND-01`) | P1 | brand | Aplicar identidad provisional JB a diseño base | `SEC-01` |
| [#5](https://github.com/WatabooColosus/JB-tecnology/issues/5) (`NAV-02`) | P1 | menu | Rediseñar navegación y megamenús de JB | `NAV-01`, `BRAND-01` |
| [#6](https://github.com/WatabooColosus/JB-tecnology/issues/6) (`HOME-01`) | P1 | landing | Mapear contenedores padres de 19 bloques Elementor | `SEC-01` |
| [#7](https://github.com/WatabooColosus/JB-tecnology/issues/7) (`HOME-02`) | P1 | landing | Renovar tríada Hogar / Empresas / Gaming | `HOME-01`, `BRAND-01` |
| [#8](https://github.com/WatabooColosus/JB-tecnology/issues/8) (`HOME-03`) | P1 | landing | Diseñar espacios destacados Redragon | `HOME-01`, `BRAND-01` |
| [#9](https://github.com/WatabooColosus/JB-tecnology/issues/9) (`HOME-04`) | P1 | landing | Arma tu PC y servicio técnico en landing | `HOME-01`, `BRAND-01` |
| [#10](https://github.com/WatabooColosus/JB-tecnology/issues/10) (`HOME-05`) | P1 | landing | Categorías, destacados y promociones sin demos | `HOME-01` |
| [#11](https://github.com/WatabooColosus/JB-tecnology/issues/11) (`HOME-06`) | P1 | landing | Grids empresariales, diferenciales y contacto | `HOME-01` |
| [#12](https://github.com/WatabooColosus/JB-tecnology/issues/12) (`RESP-01`) | P1 | quality | Verificar dimensiones y UX responsive | `NAV-02`, `HOME-02` |
| [#13](https://github.com/WatabooColosus/JB-tecnology/issues/13) (`CAT-01`) | P2 | catalog | Taxonomía y atributos reales de catálogo | `HOME-05` |
| [#14](https://github.com/WatabooColosus/JB-tecnology/issues/14) (`CAT-02`) | P2 | catalog | Productos variables e imágenes AJAX | `CAT-01` |
| [#15](https://github.com/WatabooColosus/JB-tecnology/issues/15) (`BUILD-01`) | P3 | integrations | Conectar Composite Products con BuildCores | `CAT-01`, `CAT-02` |
| [#16](https://github.com/WatabooColosus/JB-tecnology/issues/16) (`LEGAL-01`) | P3 | operations | Legal, blog, ubicaciones y checkout | `CAT-01` |
| [#17](https://github.com/WatabooColosus/JB-tecnology/issues/17) (`RELEASE-01`) | P3 | release | Publicación segura desde staging | `RESP-01`, `LEGAL-01` |

**Definición de done:** evidencia en staging; screenshots sin datos de clientes; enlaces funcionales; pruebas y CI; sin alteraciones accidentales en tienda real.

**Siguiente tarea que habilita el resto:** [SEC-01](https://github.com/WatabooColosus/JB-tecnology/issues/2) (seguridad del staging).
