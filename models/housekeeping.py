# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class HouseKeeping(models.Model):
    _name = "pms.housekeeping"

    room_status = fields.Selection(
        [('reservation', 'Reservation'), ('vacant', 'Vacant'), ('occupied', 'Occupied'), ('clean', 'Clean'),
         ('maintenance', 'Maintenance'),
         ('dirty', 'Dirty')], string='Room Status', required=True, default='vacant')
    room_no = fields.Integer(string='Room No#', required="True")
    room_type = fields.Selection([('nk', 'Non-smoking King size bed'),
                                  ('njk', 'Non-smoking King size jacuzzi bed'),
                                  ('nhk', 'Non-smoking King size handicapped bed'),
                                  ('nqq', 'Non-smoking Queen size double bed')], string='Room Type', default='nk')
    checkin_date = fields.Date(string='CheckIN Date', default=datetime.today())
    checkout_date = fields.Date(string='CheckOut Date')

    color = fields.Integer('Color', compute='_get_color')

    def _get_color(self):
        """Computing Color value according to the conditions"""
        for rec in self:
            if rec.room_status == 'clean':
                rec.color = 1
            if rec.room_status == 'dirty':
                rec.color = 2
            else:
                rec.color = 3
