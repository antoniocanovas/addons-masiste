# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models, api


class RepairOrder(models.Model):
    _inherit = "repair.order"

    repair_line_ids = fields.One2many('repair.product.line', 'repair_id', string="Repair line")
    quotation_line_ids = fields.One2many('repair.quotation.line', 'repair_id', string="Quotation line")
    date_out = fields.Datetime('Date out')
    signature = fields.Binary('Signature')
    partner_credit = fields.Monetary(related='partner_id.credit', string='Credit')
    payment_term_id = fields.Many2one('account.payment.term', string='Payment term', store="False",
                                      related='partner_id.property_payment_term_id')

    @api.depends('partner_id')
    def get_pending_invoices(self):
        for record in self:
            invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'),
                                                        ('payment_state', '=', ['not_paid', 'in_payment'])])
            record['pending_invoice_ids'] = [(6, 0, invoices.ids)]
    pending_invoice_ids = fields.Many2many("account.move", string="Invoices", store=False, compute="get_pending_invoices")

    @api.depends('quotation_line_ids')
    def get_quotation_subtotal(self):
        for record in self:
            sub = 0
            for line in record.quotation_line_ids:
                sub += line.price_subtotal
            record.quotation_price_subtotal = sub
    quotation_price_subtotal = fields.Monetary(string="Subtotal", compute="get_quotation_subtotal", store=True)

    @api.depends('quotation_line_ids')
    def get_quotation_total(self):
        for record in self:
            tot = 0
            for line in record.quotation_line_ids:
                tot += line.price_total
            record.quotation_price_total = tot
    quotation_price_total = fields.Monetary(string="Total", compute="get_quotation_total", store=True)

    @api.depends('quotation_line_ids')
    def get_quotation_taxes(self):
        for record in self:
            tax = 0
            for line in record.quotation_line_ids:
                taxes = line.tax_ids.compute_all(line.price_unit, quantity=line.product_qty,
                                                   product=line.product_id,
                                                   partner=False)
                price_tax = sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
                tax += price_tax
            record.quotation_taxes = tax

    quotation_taxes = fields.Monetary(string="Tax", compute="get_quotation_taxes", store=True)

    print_quotation_lines = fields.Boolean(string="Print QL")
