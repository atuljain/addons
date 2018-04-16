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
                stock_pi = self.pool.get('stock.picking.out')
                stock_pi_id = stock_pi.search(cr, uid, [('sale_id', '=', sales_ob.order_id.id)])
                if len(stock_pi_id) == 0:
                    result[id] = False
                else:
                    stock_picking_obj = stock_pi.browse(cr, uid, stock_pi_id[0], context=context)
                    stock = self.pool.get('stock.move')
                    stk_id = stock.search(cr, uid,  [('sale_line_id', '=', id)])
                    stk_obj = stock.browse(cr, uid, stk_id[0], context=context)
                    if stock_picking_obj.state == 'done' or stock_picking_obj.state == 'label-sent':
                        if stk_obj.state == 'done':
                            result[id] = True
                        else:
                            result[id] = False
                    else:
                        result[id] = False
            else:
                result[id] = False
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
# cr.execute('SELECT origin FROM stock_picking WHERE stock_picking.id = %s', tmp)
#         origin = cr.fetchone()
#         origin = origin[0] 
#         origin = int(origin[2:])
#         cr.execute('SELECT id FROM sale_order_line WHERE order_id = %s AND product_id=%s', (origin, vals['product_id']))                
#         zsli = cr.fetchone()    
#         zsli = zsli[0]    
#         vals['x_sale_line_id'] = zsli 
#         res_id = super(stock_pack_operation, self).create(cr, uid, vals, context=context)
#         return res_id