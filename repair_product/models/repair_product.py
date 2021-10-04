# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models


class RepairProduct(models.Model):
    _name = "repair.product"
    _description = "Products not sold by us"

    name = fields.Char(string="Name")
    lot_ids = fields.One2many('repair.product.lot', 'repair_product_id')
