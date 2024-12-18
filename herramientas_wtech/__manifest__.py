# -*- coding: utf-8 -*-
{
    "name": "Herramientas WTECH Ciudad Segura",
    "author": "WTECH Ciudad Segura",
    "version": "2.0",
    "category": "tools",
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/views_asistencia.xml",
        "views/views_pdf.xml",
        "views/views_passgen.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "herramientas_wtech/static/src/css/styles.css",
        ],
    },
    "installable": True,
    "application": True,
}
