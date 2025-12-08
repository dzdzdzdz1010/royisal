from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError

class CRMTemp(models.Model):
    _inherit = 'crm.lead'

    product_category_id = fields.Many2many('product.category','category_lead_rel','lead_id','categ_id',string="Product Category")
    material_id = fields.Many2many('royisal.material','material_lead_rel','lead_id','material_id',string="Material")
    stone_type_id = fields.Many2many('royisal.stone.type','stone_lead_rel','lead_id','stone_id',string="Stone Type")
    plating_id = fields.Many2many('royisal.plating','plating_lead_rel','lead_id','plating_id',string="Plating")
    product_type_custom = fields.Char(string="Product Type")

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