odoo.define('contenido_incrustado.ocultar_barra_herramientas', function (require) {
    "use strict";
    var ControlPanel = require('web.ControlPanel');

    ControlPanel.include({
        _renderContent: function () {
            // Puedes eliminar completamente la barra de herramientas:
            return $();
            // O personalizar su contenido:
            // return this._super.apply(this, arguments).find('.o_control_panel_main_buttons').hide(); 
        }
    });
});
