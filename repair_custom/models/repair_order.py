# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    repair_line_ids = fields.One2many('repair.product.line', 'repair_id', string="Name")
    date_out = fields.Datetime('Date out')
    signature = fields.Binary('Signature')
