{
    'name': 'Hotel Manager',
    'version': '1.0',
    'category': 'Manager',
    'sequence': 2,
    'summary': '',
    'description': "This module provides tasks related to hotel management",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'views/menu_action.xml',
        'views/room_view.xml',
        'views/customer_view.xml',
        'views/booking_view.xml',
        # 'data/customer_data_default.xml',
        # 'data/room_data_default.xml',
        'security/group_security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
