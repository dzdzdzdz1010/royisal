#-- coding: utf-8 --
{
    'name': 'Temp Royisal',
    'version': '1.0',
    'category': 'Custom Module',
    'author': 'Something Somewhere Consulting OPC',
    'website': 'http://www.somethingsomewhere.ph',
    'summary': """
        This module contains the customizations for CRM module
    """,
    # 'description': """
    # """,
    'depends': [
        'base',
        'crm',
        'product'
    ],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        
    ],
    'installable': True,
    'auto_install': True,

}