# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api, _


class PMS(models.Model):
    _name = "pms"
    _rec_name = 'room_no'

    # GUEST DETAILS
    guest_id = fields.Many2one('pms.guest', string='Guest Name', required=True)
    contact_no = fields.Char(string='Phone')
    company = fields.Char(string='Company')
    email = fields.Char(string='Email')
    street1 = fields.Char(string='Address1')
    street2 = fields.Char(string='Address2')
    zip = fields.Integer(string='Zip')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    no_of_guest = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], string='Guests', default='2')

    # Date and time details
    date = fields.Date(string='Date', default=datetime.today())
    checkin_date = fields.Date(string='CheckIN Date', default=datetime.today())
    checkout_date = fields.Date(string='CheckOut Date')
    checkin_time = fields.Float(string='CheckIn Time')
    checkout_time = fields.Float(string='CheckOut Time')
    length_of_stay = fields.Integer(string='Days', default=1)

    # ROOM DETAILS
    room_status = fields.Selection(
        [('reservation', 'Reservation'), ('vacant', 'Vacant'), ('occupied', 'Occupied'), ('clean', 'Clean'),
         ('maintenance', 'Maintenance'),
         ('dirty', 'Dirty')], string='Room Status', required=True, default='vacant')
    room_no = fields.Integer(string='Room No#', required="True")
    room_rate = fields.Float(string='Room Rate', default=100.00)
    deposit = fields.Float(string='Deposit')
    room_type = fields.Selection([('nk', 'Non-smoking King size bed'),
                                  ('njk', 'Non-smoking King size jacuzzi bed'),
                                  ('nhk', 'Non-smoking King size handicapped bed'),
                                  ('nqq', 'Non-smoking Queen size double bed')], string='Room Type', default='nk')

    # PAYMENT DETAILS
    payment_type = fields.Selection([('card', 'Card'), ('cash', 'Cash')], string='Payment Type', default='card')

    color = fields.Integer('Color', compute='_get_color')

    image = fields.Image('Identity Card', help="Select image here")

    def _get_color(self):
        """Computing Color value according to the conditions"""
        for rec in self:

            if rec.room_status == 'occupied':
                rec.color = 1
            if rec.room_status == 'vacant':
                rec.color = 2
            if rec.room_status == 'clean':
                rec.color = 3
            else:
                rec.color = 4

    @api.onchange('checkout_date')
    def onchange_checkout_date(self):
        if self.checkout_date and self.checkin_date:
            delta = self.checkout_date - self.checkin_date
            number_of_days = delta.days
            self.length_of_stay = number_of_days
        else:
            pass

    def checkin_process(self):
        """
        going to add and update the checkin details and data
        """
        self.room_status = "occupied"

    def reservation_process(self):
        """
        TO DO : make a reservation with the data inside the tables
        """
        self.room_status = "reservation"

    def checkout_process(self):
        """
        TO DO : changes to do for check out process
        """
        self.room_status = "dirty"
