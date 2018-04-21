#-*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 
# All Right Reserved
#
##############################################################################

from osv import osv, fields

class stock_picking_out(osv.osv):
    
    
    _inherit = "stock.picking.out"

    ##############################################################################
    # 
    # Create a auto pack order for each delivery item lines  
    #
    ##############################################################################

    # _columns = {
        # 'label_status': fields.function(_get_status_of_delivery, type='boolean', string='Label Status', default=False),
        # 'label_status': fields.boolean('Label Status'),
    # }

    def auto_create_pack(self, cr, uid, ids, context={}):
        stock_mv = self.pool.get('stock.move')
        tracking_obj = self.pool.get('stock.tracking')
        pack = tracking_obj.create(cr, uid, {},context=context)
        pack_obj = tracking_obj.browse(cr, uid, int(pack), context=context)
        stock_move_ids =  stock_mv.search(cr, uid, [('picking_id', '=', ids[0])])
        for stock_id in stock_move_ids:
            stock_object = stock_mv.browse(cr, uid, stock_id, context=context)
            if stock_object.tracking_id.id == False:
                vals = {'tracking_id':pack_obj.id}
                stock_mv.write(cr, uid,[stock_id], vals)
            else:
                stock_mv.write(cr, uid,[stock_id], {})
stock_picking_out()

class stock_move(osv.osv):
    
    _inherit = "stock.move"

    def lebel_created_checkbox(self, cr, uid, ids, field_name, arg, order_id, context=None):
        result = {}
        for id in ids:
            stock = self.pool.get('stock.move')
            stk_id = stock.search(cr, uid,  [('id', '=', id)])
            if stk_id:
                stock_ob = stock.browse(cr, uid, stk_id[0], context=context)
                stock_pi = self.pool.get('stock.picking.out')
                stock_pi_id = stock_pi.search(cr, uid, [('id', '=', stock_ob.picking_id.id)])
                if len(stock_pi_id) == 0:
                    result[id] = False
                else:
                    stock_picking_obj = stock_pi.browse(cr, uid, stock_pi_id[0], context=context)
                    if stock_picking_obj.state == 'done' or stock_picking_obj.state == 'label-sent':
                        result[id] = True
                        # if stock_ob.state == 'done' or :
                        #     result[id] = True
                        # else:
                        #     result[id] = False
                    else:
                        result[id] = False
        return result

    def label_printed_checkbox(self, cr, uid, ids, field_name, arg, order_id, context=None):
        result = {}
        for id in ids:
            stock = self.pool.get('stock.move')
            
            stock_label = self.pool.get('stock.picking.out.label')
            stk_id = stock.search(cr, uid,  [('id', '=', id)])
            if stk_id:
                stock_ob = stock.browse(cr, uid, stk_id[0], context=context)
                # import pdb; pdb.set_trace()
                stock_label_print = self.get_label_print_ids(cr,stock_ob.picking_id.id,context)
                if len(stock_label_print) is 0:
                    result[id] = False
                else:
                    stock_label_search = stock_label.search(cr,uid, [('id','=',stock_label_print[0])])
                    stock_pi = self.pool.get('stock.picking.out')
                    stock_pi_id = stock_pi.search(cr, uid, [('id', '=', stock_ob.picking_id.id)])
                    if len(stock_pi_id) == 0:
                        result[id] = False
                    else:
                        if len(stock_label_search) == 0:
                            result[id] = False
                        else:
                            stock_picking_obj = stock_pi.browse(cr, uid, stock_pi_id[0], context=context)
                            stock_label_search_obj = stock_label.browse(cr, uid, stock_label_search[0], context=context)
                            if stock_label_search_obj.is_label_printed == True:
                                # if stock_ob.state == 'done':
                                result[id] = True
                                # else:
                                #     result[id] = False
                            else:
                                result[id] = False
        return result

    _columns = {
        'label_created': fields.function(lebel_created_checkbox, type='boolean', string='Label Created', default=False),
        'label_printed': fields.function(label_printed_checkbox, type='boolean', string='Label Printed', default=False),
    }

    def get_label_print_ids(self, cr, id, context):
        cr.execute("SELECT label_id, picking_id FROM stock_picking_label_ids WHERE picking_id=%d" %(id) )
        list_ids = cr.fetchall()
        return list_ids if len(list_ids) is 0 else list_ids[-1]