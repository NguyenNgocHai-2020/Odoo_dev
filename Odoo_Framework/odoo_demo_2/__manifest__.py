# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo demo 2',
    'version': '1.0',
    'category': '',
    'sequence': 1,
    'summary': 'Demo create odoo module and security',
    'description': "",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/odoo_demo_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/class_view.xml',
        'views/teacher_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
