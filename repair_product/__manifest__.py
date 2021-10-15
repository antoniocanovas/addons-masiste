# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Repair Product",
    "summary": "Repair products not sold by us,"
               " these ones can be always different and must not be included in product.product.",
    "version": "14.0.1.0.0",
    "category": "Repair",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ["repair"],
    "data": [
        "security/ir.model.access.csv",
        "views/repair_view.xml",
        "views/menu_views.xml",
        "views/company_view.xml",
        "views/report_repairorder_extended.xml"
    ],
    "installable": True,
}
