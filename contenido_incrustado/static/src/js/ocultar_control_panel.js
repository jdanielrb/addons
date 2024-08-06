/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListView } from "@web/views/list/list_view";

function removeControlPanel(env) {
    const components = registry.category("views").get("list");
    if (components) {
        components.forEach((component) => {
            const originalSetup = component.prototype.setup;
            component.prototype.setup = function () {
                const res = originalSetup.call(this);
                this.props.controlPanelProps.hidden = true;  // Ocultar el control panel
                return res;
            };
        });
    }
}

removeControlPanel();
