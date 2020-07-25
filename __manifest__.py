#  Copyright (c) 2020 José Luis Zanotti - joseluiszanotti@gmail.com
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "MODULE",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Alojamiento de Sitios",
    "website": "http://www.alojamientodesitios.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "12.0.1.0.0",
    "depends": ["base"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    #    "demo": ["demo/demo.xml",],
}
