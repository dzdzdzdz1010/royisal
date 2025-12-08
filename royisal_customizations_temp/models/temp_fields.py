from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError

class CRMTemp(models.Model):
    _inherit = 'crm.lead'

    product_category_id = fields.Many2one('product.category',string="Product Category")
    material_id = fields.Many2one('royisal.material',string="Material")
    stone_type_id = fields.Many2one('royisal.stone.type',string="Stone Type")
    plating_id = fields.Many2one('royisal.plating',string="Plating")
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