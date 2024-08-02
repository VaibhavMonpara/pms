# -*- coding: utf-8 -*-
{
    'name': 'PMS Module',
    'author': 'Vaibhav',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/pms_view.xml',
        'views/guest_details_view.xml',
        'views/documents_view.xml',
        'views/housekeeping_view.xml',
        'views/itinerary_view.xml',
        'views/config_view.xml',
        'views/itinerary_line_view.xml',
        'views/events_view.xml',
        # 'views/assets.xml',
    ],
    'application': True,
    'auto_install': False,
}
