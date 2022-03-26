# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerDiscount(http.Controller):
#     @http.route('/customer_discount/customer_discount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_discount/customer_discount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_discount.listing', {
#             'root': '/customer_discount/customer_discount',
#             'objects': http.request.env['customer_discount.customer_discount'].search([]),
#         })

#     @http.route('/customer_discount/customer_discount/objects/<model("customer_discount.customer_discount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_discount.object', {
#             'object': obj
#         })
