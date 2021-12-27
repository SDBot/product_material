# -*- coding:utf-8 -*-
from odoo import models, fields


class ProductMaterial(models.Model):
    _name = "product.material"
    _description = "Product Material"

    code = fields.Char("Material Code", size=12, required=True)
    name = fields.Char("Material Name", required=True)
    type_id = fields.Many2one("product.material.type", "Material Type", required=True)
    price_buy = fields.Float("Buy Price", required=True)
    supplier_id = fields.Many2one("res.partner", "Related Supplier", required=True)

    _sql_constraints = [('price_buy_min', 'check(price_buy >= 100)', 'Buy price must be over 100')]


class ProductMaterialType(models.Model):
    _name = "product.material.type"
    _description = "Product Material Type"

    code = fields.Char("Type Code", size=12, required=True)
    name = fields.Char("Type Name", required=True)

    _sql_constraints = [('code_unique', 'unique (code)', 'Type code must be unique')]
