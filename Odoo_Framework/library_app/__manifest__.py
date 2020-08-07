# {
#     'name': 'Library Management',
#     'description': 'Manage library book catalogue and lending.',
#     'author': 'Harvey',
#     'depends': ['base'],
#     'data': [
#         'views/library_menu.xml'
#     ],
#     'application': True,
# }
{
    'name': 'Library Management',
    'version': '1.0',
    'sequence': 1,
    'description': "Manage library book catalogue and lending.",
    'author': 'Harvey',
    'depends': [
        'base',
    ],
    'data': [
        # 'security/library_security.xml',
        'views/library_menu.xml',
        'views/book_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}