# -*- coding: utf-8 -*-
{
    'name': 'Product Material',
    'author': "Tony",
    'description': """
This module allow customization of product materials
    """,
    'version': '1.0',
    'category': 'Sales/Sales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_material_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
