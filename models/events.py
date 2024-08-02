from odoo import models, fields, api
import requests


class PmsEvents(models.Model):
    _name = 'pms.events'
    _description = 'Events'

    query = fields.Char('Search for events')
    location = fields.Char('Location')
    radius = fields.Char('Radius')

    data = fields.Text('Data')

    # itinerary_line_ids = fields.One2many('pms.itinerary.lines', 'itinerary_id')

    def get_eventbrite_api_key(self):
        config = self.env['pms.google.places.config'].search([('site_name', '=', 'Eventbrite')], limit=1)
        return config.api_key if config else None

    def fetch_events_data(self):

        if self.location or self.radius:
            records = self.search_events(self.query, self.location, self.radius)
        else:
            records = self.search_events(self.query)
        return records

    def search_events(self, query, location=None, radius=None, language=None, _logger=None):
        api_key = self.get_eventbrite_api_key()
        api_url = 'https://www.eventbriteapi.com/v3/events/search/'
        headers = {
            'Authorization': api_key,
        }
        params = {
            'location.address': self.location,
        }
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            events_data = response.json().get('events')
            self.data = events_data
        else:
            # Handle API errors
            _logger.error(f"Error fetching events: {response.text}")


class PmsEventsLines(models.Model):
    _name = 'pms.events.lines'
    _description = 'Event Lines'

    # itinerary_id = fields.Many2one('pms.itinerary', string='Itinerary')
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
