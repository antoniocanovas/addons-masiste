from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class HrExpeseLine(models.Model):
    _name = 'hr.expense.line'
    _description = 'Hr expense detail line'

    type_id = fields.Many2one('hr.expense.type', string="Type")
    amount = fields.Float('Amount')
    expense_id = fields.Many2one('hr.expense', string='Expense', store=True, required=True)
    date = fields.Date('Expense date', store=True, related='expense_id.date')
    employee_id = fields.Many2one('hr.employee', store=True, related='expense_id.employee_id')

    @api.depends('type_id')
    def get_name_from_type(self):
        for record in self:
            record.name = record.type_id.name
#    name = fields.Char('Description', compute='get_name_from_type', readonly=False)
    name = fields.Char('Description', default='type_id.name', readonly=False)

    @api.depends('type_id')
    def get_standard_amount(self):
        for record in self:
            record.standard_amount = record.type_id.amount
    standard_amount = fields.Float('Estimated', store=True, readonly=True, compute='get_standard_amount')