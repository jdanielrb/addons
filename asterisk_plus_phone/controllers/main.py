# -*- coding: utf-8 -*
# ©️ OdooPBX by Odooist, Odoo Proprietary License v1.0, 2020
import json
import logging
import uuid
from odoo import http, SUPERUSER_ID, registry, release
from odoo.api import Environment
from werkzeug.exceptions import BadRequest, NotFound

logger = logging.getLogger(__name__)

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import Dial, VoiceResponse


class Voice(http.Controller):
    @http.route('/voice', type='http', auth='none')
    def voice(self, **kw):
        resp = VoiceResponse()
        print(request.form)
        if request.form.get("To") == twilio_number:
            # Receiving an incoming call to our Twilio number
            dial = Dial()
            # Route to the most recently created client based on the identity stored in the session
            dial.client(IDENTITY["identity"])
            resp.append(dial)
        elif request.form.get("To"):
            # Placing an outbound call from the Twilio client
            dial = Dial(caller_id=twilio_number)
            # wrap the phone number or client name in the appropriate TwiML verb
            # by checking if the number given has only digits and format symbols
            if phone_pattern.match(request.form["To"]):
                dial.number(request.form["To"])
            else:
                dial.client(request.form["To"])
            resp.append(dial)
        else:
            resp.say("Thanks for calling!")

        return Response(str(resp), mimetype="text/xml")