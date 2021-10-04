# Copyright 2021 Pedro Guirao - ingenieriacloud.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class RepairProductLine(models.Model):
    _name = "repair.product.line"
    _description = "Lines of repairs"

    name = fields.Char(string="Name")
    repair_id = fields.Many2one('repair.order', string='Repair Order')
    repair_product_id = fields.Many2one('repair.product', string='Product lot')
    repair_sn = fields.Many2one('repair.product.lot',
                                domain=[('repair_product_id', '=', repair_product_id)],
                                string='SN')

    partner_id = fields.Many2one('res.partner', related='repair_id.partner_id', string='Repairs')
    state_id = fields.Selection(string='State', related='repair_id.state')
    note = fields.Char(string='Note')
    scrap = fields.Binary(string='Scrap')
