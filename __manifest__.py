# -*- coding: utf-8 -*-
{
    'name': "portland_credit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Diego Gajardo",
    'website': "http://www.cleandev.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/credit_request_views.xml',
        'views/report_credit_request_template.xml',
        'reports/credit_request_report.xml',
        'views/customer_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
