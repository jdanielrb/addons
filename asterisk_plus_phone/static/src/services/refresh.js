/** @odoo-module **/
import {registry} from "@web/core/registry"

function Refresh(parent) {
    parent.bus.trigger("ROUTE_CHANGE")
}

registry.category("actions").add("refresh", Refresh);
