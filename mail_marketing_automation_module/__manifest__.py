{
    'name' : 'Contact Sync Automation',
    'version':'16.0',
    'category' : 'Auotomation',
    'summary' : """Contact Sync Automation""",
    'sequence' : 4,
    'depends' : ['base','mass_mailing'],
    'data' : [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
                
    ],
    'images':['static/description/banner.jpg'],
    'application' : True,
    'installable' : True,
    'auto-install' : False,
}
