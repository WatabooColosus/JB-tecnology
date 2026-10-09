<?php
/**
 * Plugin Name: JB Tecnologia MED - Staging Design
 * Description: Capa visual aislada para probar la nueva identidad en staging WoodMart, sin cambiar productos ni Elementor.
 * Version: 0.1.0
 * Requires PHP: 8.0
 * Text Domain: jb-tecnologia-med
 *
 * IMPORTANTE: código de desarrollo; no copiar a producción automáticamente.
 */
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Cortafuegos de producción: aplicación deliberadamente limitada al
 * subdominio staging confirmado por el propietario.
 */
function jb_stage_design_is_staging(): bool {
    $site_host = wp_parse_url(home_url('/'), PHP_URL_HOST);
    return is_string($site_host)
        && strtolower($site_host) === 'staging.jbtecnologiamed.com.co';
}

add_filter('body_class', static function (array $classes): array {
    if (jb_stage_design_is_staging()) {
        $classes[] = 'jb-stage-design';
    }
    return $classes;
});

add_action('wp_enqueue_scripts', static function (): void {
    if (!jb_stage_design_is_staging()) {
        return;
    }
    $css_file = plugin_dir_path(__FILE__) . 'assets/css/jb-stage.css';
    wp_enqueue_style(
        'jb-stage-design',
        plugins_url('assets/css/jb-stage.css', __FILE__),
        [],
        file_exists($css_file) ? (string) filemtime($css_file) : '0.1.0'
    );
}, 50);
