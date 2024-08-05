{
    "name": "Herramientas WTECH Ciudad Segura",
    "author": "WTECH Ciudad Segura",
    "version": "1.0",
    "category": "tools",
    # "depends": ["base"],
    "data": [
        "views/01_graficos_views.xml",  # Primero la vista
        "views/02_pdf_views.xml",  # Primero la vista
        "views/herramientas_actions.xml",  # Luego la acción
        "views/herramientas_menu.xml",  # Y al final el menú
    ],
    "assets": {
        "web.assets_backend": [
            "contenido_incrustado/static/src/css/styles.css",
        ],
    },
    "installable": True,
    "application": True,
}
