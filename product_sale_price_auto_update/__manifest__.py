# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Product Sale Price AutoUpdate",
    "summary": "Update sale price automatically "
               "when cost is changed in order to fetch pricelist,",
    "version": "14.0.1.0.0",
    "category": "Sales",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ['sale',
                'base_automation',
                ],
    "data": [
        "data/action_server.xml",
        "views/company_view.xml"
    ],
    "installable": True,
}
