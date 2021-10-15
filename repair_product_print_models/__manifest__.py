# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Repair Product Print Models",
    "summary": "Repair products Print for client, for Count Product, and for labels pieces.",
    "version": "14.0.1.0.0",
    "category": "Repair",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ["repair","repair_product"],
    "data": [
        "views/report_repairorder_extended.xml",
        "views/templates.xml",
        "views/report_repairorder_products.xml",
    ],
    "installable": True,
}
