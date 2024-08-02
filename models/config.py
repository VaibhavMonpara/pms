from odoo import models, fields


class GooglePlacesConfig(models.Model):
    _name = 'pms.google.places.config'
    _description = 'Google Places API Configuration'

    site_name = fields.Char(string='Site Name')
    api_key = fields.Char(string='API Key')
    client_id = fields.Char(string='Client Id')
    private_token = fields.Char(string='Private Token')
    public_token = fields.Char(string='Public Token')

