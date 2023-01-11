from odoo import _, api, fields, models


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    line_ids = fields.One2many('hr.expense.line', 'expense_id', string="Detail", store=True)

    @api.depends('line_ids.amount', 'line_ids')
    def get_lines_amount(self):
        total = 0
        for li in self.line_ids:
            total += li.amount
        self.line_amount = total
    line_amount = fields.Float('Detail total', store=False, compute='get_lines_amount',
                               help='Gasto real del empleado según la suma de las líneas.')

    @api.depends('line_ids.amount', 'line_ids')
    def get_lines_amount_estimation(self):
        total = 0
        for li in self.line_ids:
            if li.type_id.amount > li.amount:
                total += li.type_id.amount
            else:
                total += li.amount
        self.market_amount = total
    market_amount = fields.Float('Market estimation', store=False, compute='get_lines_amount_estimation',
                                 help='Este campo es informativo para mostrar el importe resultante de pagar las dietas '
                                      'al precio pactado en convenio y si algún gasto es superior tenerlo en cuenta como '
                                      'si se abonara al precio real. Ej: si la dieta es 15 y el gasto 12 el '
                                      'resultado es 15. '
                                      'Si la dieta son dos líneas cada una de 15 pero el gasto es 7 + 30 el resultado será '
                                      '15 + 30 = 45.')
