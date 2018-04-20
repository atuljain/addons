#-*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 
# All Right Reserved
#
##############################################################################

from osv import osv, fields

class account_invoice_line(osv.osv):

    def _get_status_of_delivery(self, cr, uid, ids, field_name, arg, order_id, context=None):
        result = {}
        for id in ids:
            pass
            # invoice = self.pool.get('account.invoice.line')
            # invoice_id = invoice.search(cr, uid,  [('id', '=', id)])
            # if invoice_id:
            #     invoice_ob = invoice.browse(cr, uid, invoice_id[0], context=context)
            #     stock_pi = self.pool.get('stock.picking.out')
            #     stock_pi_id = stock_pi.search(cr, uid, [('invoice_id', '=', invoice_ob.invoice_id.id)])
            #     # import pdb; pdb.set_trace()
            #     if len(stock_pi_id) == 0:
            #         result[id] = False
            #     else:
            #         stock_picking_obj = stock_pi.browse(cr, uid, stock_pi_id[0], context=context)
            #         stock = self.pool.get('stock.move')
            #         stk_id = stock.search(cr, uid,  [('sale_line_id', '=', id)])
            #         stk_obj = stock.browse(cr, uid, stk_id[0], context=context)
            #         if stock_picking_obj.state == 'done' or stock_picking_obj.state == 'label-sent':
            #             if stk_obj.state == 'done':
            #                 result[id] = True
            #             else:
            #                 result[id] = False
            #         else:
            #             result[id] = False
            # else:
            #     result[id] = False
        return result

    _inherit="account.invoice.line"

    _columns = {
        'label_status': fields.function(_get_status_of_delivery, type='boolean', string='Label Status', default=False),
        # 'label_status': fields.boolean('Label Status'),
    }
account_invoice_line()

# def _get_status_of_delivery(self, cr, uid, ids, field_name, arg, order_id, context=None):
#         result = {}
#         for id in ids:
#             sales = self.pool.get('sale.order.line')
#             inoice line 
#             sales_id = sales.search(cr, uid,  [('id', '=', id)])
#             invoice line id 
#             if sales_id:
#                 sales_ob = sales.browse(cr, uid, sales_id[0], context=context)
#                 invoice line object
#                 stock_pi = self.pool.get('stock.picking.out')
#                 stock_pi_id = stock_pi.search(cr, uid, [('sale_id', '=', sales_ob.order_id.id)])
#                 if len(stock_pi_id) == 0:
#                     result[id] = False
#                 else:
#                     stock_picking_obj = stock_pi.browse(cr, uid, stock_pi_id[0], context=context)
#                     stock = self.pool.get('stock.move')
#                     stk_id = stock.search(cr, uid,  [('sale_line_id', '=', id)])
#                     stk_obj = stock.browse(cr, uid, stk_id[0], context=context)
#                     if stock_picking_obj.state == 'done' or stock_picking_obj.state == 'label-sent':
#                         if stk_obj.state == 'done':
#                             result[id] = True
#                         else:
#                             result[id] = False
#                     else:
#                         result[id] = False
#             else:
#                 result[id] = False
#         return result