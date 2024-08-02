# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Documents(models.Model):
    _name = "pms.documents"

    document_no = fields.Char(string='Document No')
    document_type = fields.Selection(
        [('cc', 'Credit Card'), ('dl', 'Driving License'), ('sid', 'State ID'), ('pp', 'Passport')],
        string='Document Type', required=True, default='dl')
    issue_date = fields.Date(string='Issue Date')
    issue_place = fields.Char(string='Issue Place')
    expiry_date = fields.Date(string='Expiry Date')
    valid_till = fields.Date(string='Valid Till')
    card_type = fields.Selection(
        [('visa', 'Visa'), ('master', 'Mastercard'), ('discover', 'Discover'), ('amex', 'American Express')],
        string='Document Type')
    guest_id = fields.Many2one('pms.guest', string='Guest')
