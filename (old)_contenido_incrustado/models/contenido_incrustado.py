from odoo import models, fields

class ContenidoIncrustado(models.Model):
    _name = 'contenido_incrustado.contenido_incrustado'  # Nombre técnico del modelo
    _description = 'Contenido Incrustado'  # Descripción del modelo

    name = fields.Char(string='Nombre', required=True)  # Campo de nombre (obligatorio)
    # Agrega aquí otros campos que necesites para tu modelo
