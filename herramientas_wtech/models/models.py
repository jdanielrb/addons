from odoo import models, fields, api

class herramientas_wtech(models.Model):
    _name = "herramientas_wtech.herramientas_wtech"
    _description = "Herramientas Wtech"

    # name = fields.Char(
    #     string="Nombre", required=True, help="Nombre del registro o gráfico."
    # )
    # url_iframe = fields.Char(
    #     string="URL del Iframe",
    #     default="http://localhost:8501",
    #     help="URL para mostrar en el iframe.",
    # )
    # show_options = fields.Boolean(
    #     string="Mostrar Opciones", default=True, help="Mostrar el panel de opciones."
    # )
    # description = fields.Text(
    #     string="Descripción", help="Descripción o información adicional."
    # )

    # # Un campo que podrías usar para obtener información específica de alguna API o fuente de datos
    # user_count = fields.Integer(
    #     string="Conteo de Usuarios",
    #     compute="_compute_user_count",
    #     store=True,
    #     help="Cantidad de usuarios registrada.",
    # )

    # @api.depends("url_iframe")
    # def _compute_user_count(self):
    #     # Supongamos que haces algún cálculo o traes información de una API externa
    #     self.user_count = 42  # Solo un ejemplo, aquí iría la lógica real
