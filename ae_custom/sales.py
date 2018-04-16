#-*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 
# All Right Reserved
#
##############################################################################

from osv import osv, fields

class sale_order_line(osv.osv):

    def _get_status_of_delivery(self, cr, uid, ids, field_name, arg, order_id, context=None):
        result = {}
        for id in ids:
            sales = self.pool.get('sale.order.line')
            sales_id = sales.search(cr, uid,  [('id', '=', id)])
            if sales_id:
                sales_ob = sales.browse(cr, uid, sales_id[0], context=context)
                if sales_ob.order_id.shipped == True:
                    result[id] = True
                    print "----false"
                else:
                    result[id] = False
                    print "-----true"
            else:
                result[id] = False
                print "----true"
        return result

    _inherit="sale.order.line"

    _columns = {
        'label_status': fields.function(_get_status_of_delivery, type='boolean', string='Label Status', default=False),
        # 'label_status': fields.boolean('Label Status'),
    }
sale_order_line()

# shipped
# stock.picking.out
# state
# origin
# move_lines
# stock.move
# state
# origin
# sale_line_id