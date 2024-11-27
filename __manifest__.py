# -*- coding: utf-8 -*-
{
    'name': "job_posting",

    'summary': """
        This is simple Job Posting Module""",

    'description': """
        Job Posting Module
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','mail','web'],
    

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/job_action.xml',
        'views/templates.xml',
        'views/job_position_view.xml',
        'views/job_position_readonly_view.xml',
        'views/job_application_view.xml',
        'views/job_detail_view.xml',
        'views/job_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    
    'assets': {
        'web.assets_frontend': [
            'job_posting/static/src/scss/*.scss', 
            'job_posting/static/src/js/file_validation.js',   
        ],
        'web.assets_backend': [
            'job_posting/static/src/js/file_validation.js',
        ],
        
    },
}
