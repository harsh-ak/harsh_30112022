# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "harsh_30112022",
    "version": "1.0",
    "summary": "Contact Edit",
    "sequence": 10,
    "description": """
This Module will able to allow To view the contact details and edit it""",
    "depends": ["contacts", "website"],
    "data": [
        "views/menu.xml",
        "views/contact_template.xml",
        "views/contact_detail_template.xml",
        "views/thankyou_page.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
