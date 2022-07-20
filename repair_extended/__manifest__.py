# Copyright 2021 IC - Serincloud SL
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Repair Extended",
    "summary": "Repair products not sold by us,"
               " these ones can be always different and must not be included in product.product.",
    "version": "14.0.1.0.0",
    "category": "Repair",
    "author": "Pedro Guirao, ",
    "website": "",
    "license": "AGPL-3",
    "depends": ["repair", "base_automation", "partner_expired_debt"],
    "data": [
        "security/ir.model.access.csv",
        "views/repair_view.xml",
        "views/menu_views.xml",
        "views/company_view.xml",
        "views/invoice_view.xml",
    ],
    "installable": True,
}
