# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports without taxes ",
    "summary": "Reports from sale.order and account wihtout taxes.",
    "version": "14.0.2.0.0",
    "category": "Reports",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ['sale', 'stock', 'account_payment_mode',
                'purchase', 'base_comment_template',
                'sale_comment_template', 'custom_masiste', 'account_invoice_report_due_list'],
    "data": [
        "views/report_account_move_without_taxes.xml",
        "views/report_purchaseorder_without_taxes_date_req.xml",
        "views/report_account_move_changes.xml",
        "views/report_sale_order_without_taxes.xml",
        "views/report_delivery_document_custom.xml",
    ],
    "installable": True,
}
