# Copyright 2021 Pedro Guirao - ingenieriacloud.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, api


class RepairProductLine(models.Model):
    _name = "repair.product.line"
    _description = "Lines of repairs"


    repair_id = fields.Many2one('repair.order', string='Repair Order')
    repair_product_id = fields.Many2one('repair.product', string='Product')
    repair_sn = fields.Many2one('repair.product.lot',
                                string='SN')

    partner_id = fields.Many2one('res.partner', related='repair_id.partner_id', string='Repairs')
    state = fields.Selection(string='State', related='repair_id.state')
    date_out = fields.Datetime(string='Date out', related='repair_id.date_out')
    note = fields.Char(string='Note')
    scrap = fields.Boolean(string='Scrap')

    @api.depends('repair_product_id')
    def get_default_description(self):
        self.name = self.repair_product_id.name

    name = fields.Char(string="Description",
                       compute=get_default_description,
                       readonly=False,
                       store=True)
