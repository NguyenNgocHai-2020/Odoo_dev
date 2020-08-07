{
    'name': 'Odoo Day 2',
    'version': '1.0',
    'category': 'Demo',
    'sequence': 1,
    'summary': 'Demo create odoo module',
    'description': "",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/group_security.xml',
        'security/ir.model.access.csv',
        'views/students_view.xml',
        'views/class_view.xml',
        'views/teacher_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
