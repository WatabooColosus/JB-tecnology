#!/usr/bin/env python3
"""Source-contract tests for a staging-only WordPress presentation plugin."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
php=(root/"wordpress/jb-stage-design/jb-stage-design.php").read_text(encoding="utf-8")
css=(root/"wordpress/jb-stage-design/assets/css/jb-stage.css").read_text(encoding="utf-8")

assert "staging.jbtecnologiamed.com.co" in php
assert "wp_parse_url(home_url('/'), PHP_URL_HOST)" in php
assert "if (!jb_stage_design_is_staging())" in php
assert "body_class" in php
assert "wp_enqueue_style" in php
assert "body.jb-stage-design" in css
assert "focus-visible" in css
assert "prefers-reduced-motion" in css
assert "elementor-element-7568552" in css
assert "elementor-element-9b34239" in css
assert "wp_remote_post" not in php and "file_put_contents" not in php
assert "wc_create_order" not in php
print("OK: plugin de diseño restringido a staging, estilos aislados y sin escrituras de WooCommerce")
