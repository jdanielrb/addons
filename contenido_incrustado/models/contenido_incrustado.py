from odoo import models, fields

class ContenidoIncrustado(models.Model):
    _name = 'contenido.incrustado'
    _description = 'Vista para contenido incrustado'

    name = fields.Char(string='Nombre', default='Iframe Content')
