#-*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c)  
# All Right Reserved
#
##############################################################################

{
    'name': 'Atul | Shipping label',
    'version': '1.0',
    'category': 'Tools',
    'description': """This module add objects to add checkbox in sales order line for delivered item""",
    'summary': 'customisation',
    'author': 'Atul',
    'website': 'http://www.boffinhub.in',
    'depends': ['base','sale','stock'],
    'data': [
            'label_status.xml',
            'stock_views.xml'
    #      'security/ir.model.access.csv',
         ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
