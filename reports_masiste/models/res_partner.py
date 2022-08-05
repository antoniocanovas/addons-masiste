# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name_printed = fields.Char(string='Empresa', compute='get_name_printed', store=False)

    def get_name_printed(self):
        for record in self:
            name = record.name
            if (record.company_type != 'company') and (record.parent_id.id):
                name = record.parent_id.name
            record['name_printed'] = name
