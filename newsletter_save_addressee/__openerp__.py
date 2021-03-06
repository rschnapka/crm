# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Save addressees of newsletters",
    "version": "1.0",
    "author": "Therp BV",
    "license": "AGPL-3",
    "complexity": "normal",
    "description": """
This addons saves a link between a newsletter being sent and the partner the
newsletter is sent to.
    """,
    "category": "Newsletter",
    "depends": [
        'newsletter',
    ],
    "data": [
        "view/newsletter_newsletter.xml",
        "view/res_partner.xml",
        'security/ir.model.access.csv',
    ],
    "js": [
    ],
    "css": [
    ],
    "qweb": [
    ],
    "test": [
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
