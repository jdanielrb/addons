# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.asterisk_plus.models.user import USER_PERMITTED_FIELDS

USER_PERMITTED_FIELDS.append('phone_ring_volume')


class User(models.Model):
    _inherit = 'asterisk_plus.user'

    phone_ring_volume = fields.Integer(string='Phone Ring Volume, %', required=True, default=100)

    @api.constrains('phone_ring_volume')
    def _check_phone_ring_volume(self):
        for rec in self:
            if rec.phone_ring_volume < 0 or rec.phone_ring_volume > 100:
                raise ValidationError('Volume must be in a range from 0 to 100%!')

    @api.model
    def search_pbx_users(self, search_query):
        if not self.env.user.has_group('asterisk_plus.group_asterisk_user'):
            raise ValidationError('Only PBX users can search other PBX users!')
        domain = ['|', ['exten', '=ilike', f'%{search_query}%'], ['user', '=ilike', f'%{search_query}%']]
        search_fields = ['id', 'name', 'exten', 'user']
        users = self.sudo().search_read(domain, search_fields, limit=10, order='exten asc')
        return users

    @api.model
    def get_user_by_number(self, search_query):
        if not self.env.user.has_group('asterisk_plus.group_asterisk_user'):
            raise ValidationError('Only PBX users can search other PBX users!')
        domain = [['exten', '=', search_query]]
        search_fields = ['id', 'name', 'exten', 'user']
        user = self.sudo().search_read(domain, search_fields, limit=1, order='exten asc')
        return user[0] if user else False
