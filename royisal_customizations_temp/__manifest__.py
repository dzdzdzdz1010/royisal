#-- coding: utf-8 --
{
    'name': 'Royisal CRM Customizations',
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
        'product',
        'account'
    ],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/crm.xml',
        'views/partner.xml',
        'views/views.xml',
        
    ],
    'installable': True,
    'auto_install': True,

}