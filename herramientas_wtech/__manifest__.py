{
    "name": "Herramientas WTECH Ciudad Segura",
    "author": "WTECH Ciudad Segura",
    "version": "1.0",
    "category": "tools",
    "depends": ["base"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "herramientas_wtech/static/src/css/styles.css",
        ],
    },
    "installable": True,
    "application": True,
}
