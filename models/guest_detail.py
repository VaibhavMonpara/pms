# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class GuestDetail(models.Model):
    _name = "pms.guest"
    _rec_name = "guest_name"

    # GUEST DETAILS
    guest_name = fields.Char(string='Guest Name')
    contact_no = fields.Integer(string='Contact', required=True)
    email = fields.Char(string='Email')
    street1 = fields.Char(string='Address1')
    street2 = fields.Char(string='Address2')
    zip = fields.Integer(string='Zip')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')

    document_ids = fields.One2many('pms.documents', 'guest_id')



