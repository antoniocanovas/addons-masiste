# Copyright 2021 Pedro Guirao - ingenieriacloud.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class RepairProductLot(models.Model):
    _name = "repair.product.lot"
    _description = "Lines of repairs"

    name = fields.Char(string="Lot", required=True)
    repair_product_id = fields.Many2one('repair.product', string='Product', required=True)
    repair_ids = fields.One2many('repair.product.line', 'repair_id', string='Repairs')
