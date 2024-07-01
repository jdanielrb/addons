/** @odoo-module **/
"use strict"

import {CharField} from "@web/views/fields/char/char_field"
import {registry} from "@web/core/registry"
import {Component} from "@odoo/owl"

export class OriginateCallField extends CharField {
    static template = 'phone.OriginateCall'

    setup() {
        super.setup()
        this.messaging = null
        Component.env.services.messaging.get().then((messaging) => {
            this.messaging = messaging
        });
    }

    _onClickOriginateCall(e) {
        e.stopPropagation()
        let props = {phone: this.props.value}
        if (this.props.record.resModel === "crm.lead") {
            Object.assign(props, {lead_id: this.props.record.data.id})
        }
        this.messaging.messagingBus.trigger('make_call', props)
    }
}

registry.category("fields").add("originate_call", OriginateCallField)
