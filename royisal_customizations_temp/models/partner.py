from odoo import fields,api,models

class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    whatsapp_number = fields.Char(string="WhatsApp Number")
    number_of_employees = fields.Selection([
        ('1-10', '1-10'),
        ('11-50', '11-50'),
        ('51-200', '51-200'),
        ('201-500', '201-500'),
        ('500_up', '500+'),
    ], string='Number of Employees')
    credit_term_id = fields.Many2one('account.payment.term',string="Credit Terms")
    shipping_address = fields.Char(string="Shipping Address")
    buying_role = fields.Char(string="Buying Role")