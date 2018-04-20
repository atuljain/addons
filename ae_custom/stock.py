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
