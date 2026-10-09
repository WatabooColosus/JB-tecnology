<?php
/**
 * Enqueue script and styles for child theme
 */
function woodmart_child_enqueue_styles() {
	wp_register_style( 'child-style', get_stylesheet_directory_uri() . '/style.css', array( 'woodmart-style' ), woodmart_get_theme_info( 'Version' ) );
	wp_style_add_data( 'child-style', 'path', get_stylesheet_directory() . '/style.css' );

	wp_enqueue_style( 'child-style' );
}
add_action( 'wp_enqueue_scripts', 'woodmart_child_enqueue_styles', 10010 );

/**
 * JB Tecnología MED — integración de estilos aprobables en staging.
 * Solo se ejecuta en el subdominio staging; nunca modifica producción.
 */
function jb_child_is_staging_host(): bool {
    $host = wp_parse_url( home_url( '/' ), PHP_URL_HOST );
    return is_string( $host ) && strtolower( $host ) === 'staging.jbtecnologiamed.com.co';
}

function jb_child_stage_body_class( array $classes ): array {
    if ( jb_child_is_staging_host() ) {
        $classes[] = 'jb-stage-design';
    }
    return $classes;
}
add_filter( 'body_class', 'jb_child_stage_body_class' );

function jb_child_enqueue_staging_design(): void {
    if ( ! jb_child_is_staging_host() ) {
        return;
    }
    $file = get_stylesheet_directory() . '/assets/jb-stage.css';
    if ( ! file_exists( $file ) ) {
        return;
    }
    wp_enqueue_style(
        'jb-stage-brand',
        get_stylesheet_directory_uri() . '/assets/jb-stage.css',
        array( 'child-style' ),
        (string) filemtime( $file )
    );
}
add_action( 'wp_enqueue_scripts', 'jb_child_enqueue_staging_design', 10020 );
