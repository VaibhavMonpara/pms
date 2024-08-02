from odoo import models, fields, api
import requests


class PmsItinerary(models.Model):
    _name = 'pms.itinerary'
    _description = 'Places Itinerary'

    query = fields.Char('Search for places')
    location = fields.Char('Location')
    radius = fields.Char('Radius')

    data = fields.Text('Data')

    itinerary_line_ids = fields.One2many('pms.itinerary.lines', 'itinerary_id')

    def fetch_places_data(self):
        if self.query:
            if self.location or self.radius:
                records = self.search_places(self.query, self.location, self.radius)
            else:
                records = self.search_places(self.query)
            if records:
                self.itinerary_line_ids = [(5, 0, 0)]
                counter = 0
                for place in records:
                    if place.get('photos'):
                        data = place.get('photos')[0]
                        image_data = data.get('reference')
                    else:
                        image_data = ''
                    line = self.env['pms.itinerary.lines'].create({
                        'itinerary_id': self.id,
                        'name': place.get("name", "N/A"),
                        'address': place.get("formatted_address", "N/A"),
                        'rating': place.get("rating", "N/A"),
                        'types': place.get("types", []),
                        'image': image_data
                    })
                    self.itinerary_line_ids += line
                    counter += 1
                    if counter < 8:
                        continue
                    else:
                        break

    def get_google_api_key(self):
        config = self.env['pms.google.places.config'].search([], limit=1)
        return config.api_key if config else None

    def search_places(self, query, location=None, radius=None, language=None):
        base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        params = {
            'query': query,
            'key': self.get_google_api_key()
        }
        if location:
            params['location'] = location
        if radius:
            params['radius'] = radius
        if language:
            params['language'] = language

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()['results']
        else:
            return []

    # Function to retrieve place details
    def get_place_details(self, place_id, language=None):
        base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
        params = {
            'place_id': place_id,
            'key': self.get_google_api_key()
        }
        if language:
            params['language'] = language

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()['result']
        else:
            return {}


class PmsItineraryLines(models.Model):
    _name = 'pms.itinerary.lines'
    _description = 'Places Itinerary Lines'

    itinerary_id = fields.Many2one('pms.itinerary', string='Itinerary')
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    rating = fields.Char(string='Rating')
    types = fields.Char(string='Types')
    image = fields.Binary(string='Image')
