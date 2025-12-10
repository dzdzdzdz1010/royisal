from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError


class CRMCustomFields(models.Model):
    _inherit = 'crm.lead'

    last_contacted_date = fields.Datetime(string="Last Contacted Date")
    first_name = fields.Char(string="First Name",related="partner_id.first_name",store=True,readonly=False)
    last_name = fields.Char(string="Last Name",related="partner_id.last_name",store=True,readonly=False)
    whatsapp_number = fields.Char(string="WhatsApp Number")

    source_online_id = fields.Many2many('royisal.lead.source.online','lead_source_online_rel','lead_id','source_id', string="Lead Source (Online)")
    source_offline_id = fields.Many2one('royisal.lead.source.offline',string="Lead Source (Offline)")
    lead_status = fields.Selection([
        ('Hot Leads', 'Hot Leads'),
        ('Warm Leads', 'Warm Leads'),
        ('Cold Leads', 'Cold Leads'),
        ('Vendor/Supplier', 'Vendor/Supplier'),
        ('Spammer/Invalid', 'Spammer/Invalid'),
    ])
    lifecycle_stage = fields.Selection([
        ('Subscriber', 'Subscriber'),
        ('Lead', 'Lead'),
        ('Marketing Qualified Leads', 'Marketing Qualified Leads'),
        ('Sales Qualified Leads', 'Sales Qualified Leads'),
        ('Opportunity', 'Opportunity'),
        ('Customer', 'Customer'),
        ('Evangelist', 'Evangelist'),
        ('Other', 'Other'),
    ])
    interested_in = fields.Selection([
        ('ODM','ODM (Your brand, our designs)'),
        ('OEM','OEM (You design, we create)'),
        ('Other','Other')
    ])
    customer_status = fields.Selection([
        ('vip', 'V.I.P. (Above 5M)'),
        ('regular', 'Regular (1-5M)'),
        ('small', 'Small (Below 1M)'),
        ('sleeping', 'Sleeping (No order over 1 year)'),
    ])
    buying_role = fields.Char(string="Buying Role",related="partner_id.buying_role",store=True,readonly=False)
    tax_id_number = fields.Char(string="Tax ID/EORI Number",related="partner_id.vat",store=True,readonly=False)
    product_ids = fields.Many2many('product.template','lead_product_rel','lead_id','product_id',string="In house Product Collection")
    business_status = fields.Selection([
        ('In the business','In the business'),
        ('Start Up','Start Up'),
        ('N/A','N/A')
    ])
    business_type_id = fields.Many2one('royisal.business.type',string="Business Type")

    # Deals
    deal_pipeline = fields.Selection([
        ('Ecommerce Pipeline', 'Ecommerce Pipeline'),
        ('Sales Pipeline', 'Sales Pipeline'),
        ('Events and exhibitions', 'Events and Exhibitions'),
    ])
    
    product_category_id = fields.Many2many('product.category','category_lead_rel','lead_id','categ_id',string="Product Category")
    material_id = fields.Many2many('royisal.material','material_lead_rel','lead_id','material_id',string="Material")
    stone_type_id = fields.Many2many('royisal.stone.type','stone_lead_rel','lead_id','stone_id',string="Stone Type")
    plating_id = fields.Many2many('royisal.plating','plating_lead_rel','lead_id','plating_id',string="Plating")
    design_reference = fields.Char(string="Design Reference")
    deal_amount = fields.Float(string="Deal Amount")
    recent_deal_amount = fields.Float(string="Recent Deal Amount")
    interested_quantity = fields.Integer(string="Interested Quantity")

class RoyisalBusinessType(models.Model):
    _name = 'royisal.business.type'

    name = fields.Char(string="Name",required=True)
class RoyisalCustomerStatus(models.Model):
    _name = 'royisal.customer.status'

    name = fields.Char(string="Name",required=True)

class LeadSourceOnline(models.Model):
    _name = 'royisal.lead.source.online'

    name = fields.Char(string="Name",required=True)

class LeadSourceOffline(models.Model):
    _name = 'royisal.lead.source.offline'

    name = fields.Char(string="Name",required=True)

class RoyisalPlating(models.Model):
    _name = 'royisal.plating'
    _description = 'Royisal Plating'

    name = fields.Char(string="Plating Name",required=True)

class RoyisalMaterial(models.Model):
    _name = 'royisal.material'
    _description = 'Royisal Material'

    name = fields.Char(string="Material Name",required=True)

class RoyisalStoneType(models.Model): 
    _name = 'royisal.stone.type'
    _description = 'Royisal Stone Type'

    name = fields.Char(string="Stone Type Name",required=True)
