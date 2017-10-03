# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Springboard Consolidated Sales Report',
    'category': 'Sales',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Consolidated Sales report
        """,
    'depends': ['base','sale','point_of_sale'],
    'data': [
        'data/ir_models.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_views.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/ir_actions_server.xml',
        'data/ir_cron.xml'
    ],
    'installable': True,
    'application': False,
}
