# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import fields, models, api

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    delegacion_id = fields.Many2one('res.partner', string='Delegación')
    provincia_id = fields.Many2one('res.country.state', string='Provincia',
                                   related='delegacion_id.state_id', store=True)
    facturar_a = fields.Many2one('res.partner', string='Facturar a', store=True)
