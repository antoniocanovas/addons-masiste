# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models, api


class RepairOrder(models.Model):
    _inherit = "repair.order"

    repair_line_ids = fields.One2many('repair.product.line', 'repair_id', string="Repair line")
    quotation_line_ids = fields.One2many('repair.quotation.line', 'repair_id', string="Quotation line")
    date_out = fields.Datetime('Date out')
    signature = fields.Binary('Signature')

    @api.depends('quotation_line_ids')
    def get_quotation_subtotal(self):
        for record in self:
            for line in record.quotation_line_ids:
                sub = line.price_subtotal
            record.quotation_price_subtotal = sub
    quotation_price_subtotal = fields.Monetary(string="Subtotal", compute="get_quotation_subtotal", store=True)

    @api.depends('quotation_line_ids')
    def get_quotation_total(self):
        for record in self:
            for line in record.quotation_line_ids:
                tot = line.price_total
            record.quotation_price_total = tot

    quotation_price_total = fields.Monetary(string="Total", compute="get_quotation_total", store=True)
    print_quotation_lines = fields.Boolean(string="Print QL")
