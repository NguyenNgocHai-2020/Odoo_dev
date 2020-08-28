# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo inherit demo',
    'version': '1.0',
    'category': '',
    'sequence': 1,
    'summary': 'Demo inherit',
    'description': "",
    'website': '',
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
