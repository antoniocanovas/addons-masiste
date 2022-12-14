# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Helpdesk report Masiste",
    "summary": "Adds ticket print option",
    "version": "14.0.2.1.0",
    "category": "Reports",
    "author": "Pedro Guirao, ",
    "website": '',
    "license": "AGPL-3",
    "depends": ['helpdesk_mgmt', 'helpdesk_mgmt_project', 'helpdesk_type', 'custom_masiste'],
    "data": [
        "report/ticket_report_templates.xml",
        "report/report.xml",
    ],
    "installable": True,
}
