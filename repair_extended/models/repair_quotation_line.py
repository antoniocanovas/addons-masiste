# Copyright 2021 Pedro Guirao - Ingenieriacloud.com


from odoo import fields, models, api
from odoo.exceptions import ValidationError


class RepairQuotationLine(models.Model):
    _name = "repair.quotation.line"
    _description = "New quotation unalterable by pieces or services changes"

    repair_id = fields.Many2one('repair.order', string='Repair Order')
    product_id = fields.Many2one("product.product", string="Product")
    product_uom_id = fields.Many2one("uom.uom", string="Uom")

    product_qty = fields.Float(string="Product qty", default="1")
    currency_id = fields.Many2one('res.currency', string='Currency', readonly=1, related=False)

    @api.depends('product_qty','product_uom_id','product_id')
    def get_unit_price(self):
        for p in self:
            if p.product_id:
                    if p.repair_id.pricelist_id:
                        pricelist = p.repair_id.pricelist_id
                        if p.product_qty:
                              p['price_unit'] = pricelist.get_product_price(p.product_id, p.product_qty, False)
                        else:   p['price_unit'] = pricelist.get_product_price(p.product_id, 1, False)
                    else:
                        p['price_unit'] = p.product_id.lst_price

    price_unit = fields.Monetary(string="Unit price", compute="get_unit_price", store=True)

    tax_ids = fields.Many2many("account.tax", string="Taxes", related="product_id.taxes_id", readonly=1)

    @api.depends('product_qty', 'product_uom_id', 'product_id')
    def get_subtotal_price(self):
        self.price_subtotal = self.price_unit * self.product_qty
    price_subtotal = fields.Monetary(string="Subtotal", compute="get_subtotal_price", store=True)

    @api.depends('product_qty', 'product_uom_id', 'product_id')
    def get_total_price(self):
        taxes = self.tax_ids.compute_all(self.price_unit, quantity=self.product_qty, product=self.product_id,
                                        partner=False)
        price_tax = sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
        self.price_total = self.price_unit + price_tax

    price_total = fields.Monetary(string="Total", compute="get_total_price", store=True)

