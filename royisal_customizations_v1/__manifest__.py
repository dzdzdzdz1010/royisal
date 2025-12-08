#-- coding: utf-8 --
{
    'name': 'Royisal Customizations V1',
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
        'views/crm_customizations.xml',
        'views/partner.xml',
    ],
    'installable': True,
    'auto_install': True,

}