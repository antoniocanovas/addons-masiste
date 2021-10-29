# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    default_product_id = fields.Many2one('product.product', string="Default Product")
