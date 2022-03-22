# -*- coding: utf-8 -*-
# from odoo import http


# class AdvancedSale(http.Controller):
#     @http.route('/advanced_sale/advanced_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advanced_sale/advanced_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advanced_sale.listing', {
#             'root': '/advanced_sale/advanced_sale',
#             'objects': http.request.env['advanced_sale.advanced_sale'].search([]),
#         })

#     @http.route('/advanced_sale/advanced_sale/objects/<model("advanced_sale.advanced_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advanced_sale.object', {
#             'object': obj
#         })
