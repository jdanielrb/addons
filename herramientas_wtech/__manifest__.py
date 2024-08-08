# -*- coding: utf-8 -*-
{
    "name": "Herramientas WTECH Ciudad Segura",
    "author": "WTECH Ciudad Segura",
    "version": "1.0",
    "category": "tools",
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/css/styles.css",
        ],
    },
    "installable": True,
    "application": True,
}
