# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sport PYA0520E',
    'version': '1.0',
    'category': '',
    'sequence': 1,
    'summary': 'About sport of PYA0520E',
    'description': "",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'wizard/dissolution_club_wizard_view.xml',
        'security/group_user.xml',
        'security/ir.model.access.csv',
        'views/menu_action.xml',
        'views/training_view.xml',
        'views/club.xml',
        'views/football_player.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
