# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    # here, key has to be full xmlID(including the module name) of all the
    # new report actions that you have defined for check layout
    account_check_printing_layout = fields.Selection(selection_add=[
        ('account_check_report_masiste.action_print_check_sabadell', 'Check Sabadell'),
    ], ondelete={
        'account_check_report_masiste.action_print_check_sabadell': 'set default',
    })