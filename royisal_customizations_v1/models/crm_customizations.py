from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError

class CRMLeadCustomizations(models.Model):
    _inherit = 'crm.lead'

    interested_id = fields.Many2one(
        'crm.tag',
        string='What you are interested in?',
        context={'type': 'interest'},
        domain=[('type', '=', 'interest')],
    )

    business_status = fields.Selection([
        ('In the business', 'In the business'),
        ('Start Up', 'Start Up'),
        ('N/A', 'N/A'),
    ])

    business_type_id = fields.Many2one(
        'crm.tag',
        string="Business Type",
        context={'type': 'business_type'},
        domain=[('type', '=', 'business_type')],
    )

    employee_count = fields.Selection([
        ('1-10', '1-10'),
        ('11-50', '11-50'),
        ('51-200', '51-200'),
        ('201-500', '201-500'),
        ('500_up', '500+'),
    ], string='Employee Count',related="partner_id.employee_count",store=True,readonly=False)

    deal_pipeline = fields.Selection([
        ('Ecommerce Pipeline', 'Ecommerce Pipeline'),
        ('Sales Pipeline', 'Sales Pipeline'),
        ('Events and Exhibitions','Events and Exhibitions'),
    ])

    last_contact_date = fields.Datetime(
        string="Last Contacted On",related="partner_id.last_contact_date",
        store=True,readonly=False,tracking=True)
    
    whatsapp_number = fields.Char(
        string="WhatsApp Number",
    )
    contact_email = fields.Char(string="Email",related="partner_id.email",store=True)
    deal_line_ids = fields.One2many(
        'royisal.deal.order.line',
        'deal_id',
        string="Deal Order Lines")
    contact_owner_id = fields.Many2one('res.partner',string="Contact Owner")
    ip_country = fields.Many2one('res.country',string="IP Country")

class ResPartnerCustomization(models.Model):
    _inherit = 'res.partner'

    employee_count = fields.Selection([
        ('1-10', '1-10'),
        ('11-50', '11-50'),
        ('51-200', '51-200'),
        ('201-500', '201-500'),
        ('500_up', '500+'),
    ], string='Employee Count')

    whatsapp_number = fields.Char(
        string="WhatsApp Number"
    )
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    last_contact_date = fields.Datetime(string="Last Contact Date",tracking=True)
    ip_country = fields.Many2one('res.country',string="IP Country")
    contact_owner_id = fields.Many2one('res.partner',string="Contact Owner")
    
class CRMTagType(models.Model):
    _inherit = 'crm.tag'

    type = fields.Selection([
        ('None', 'None'),
        ('interest', 'Interest'),
        ('business_type', 'Business Type'),
    ])

    @api.model
    def create(self, vals):
        res = super(CRMTagType, self).create(vals)
        type = self.env.context.get('type', False)
        if type:
            if type == 'interest':
                res.type = 'interest'
            elif type == 'business_type':
                res.type = 'business_type'
        return res
 
class DealOrderLine(models.Model):
    _name = 'royisal.deal.order.line'

    _rec_name = 'description'
    deal_id = fields.Many2one('crm.lead',string="Deal")
    product_id = fields.Many2one('product.template',string="Product")
    attribute_line_ids = fields.One2many(
        'royisal.deal.product.attribute',
        'deal_line_id',
        string="Product Attributes")
    description = fields.Text(string="Description",compute="_compute_description",store=True)
    product_price = fields.Float(string="Product Price")
    quantity = fields.Integer(string="Quantity",default=1)
    reference = fields.Char(string="Reference")
    subtotal = fields.Float(string="Subtotal",compute="_compute_subtotal",store=True)

    @api.onchange('product_price','quantity')
    def _onchange_subtotal(self):
        self.subtotal = self.product_price * self.quantity

    @api.depends('product_price','quantity')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.product_price * rec.quantity
    

    @api.depends('product_id','attribute_line_ids','attribute_line_ids.value_ids')
    def _compute_description(self):
        for rec in self:
            desc = ""
            for attribute in rec.attribute_line_ids:
                values = ", ".join(attribute.value_ids.mapped('name'))
                desc += f"- {attribute.attribute_id.name}: {values};\n"
            rec.description = f"{rec.product_id.name or ""}\n{desc}"

class DealProductAttribute(models.Model):
    _name = 'royisal.deal.product.attribute'

    deal_line_id = fields.Many2one('royisal.deal.order.line',string="Deal Order Line")
    attribute_id = fields.Many2one('product.attribute',string="Attribute")
    value_ids = fields.Many2many('product.attribute.value',string="Attribute Values")


    