# -*- coding: utf-8 -*-
# from odoo import http


# class Advanced(http.Controller):
#     @http.route('/advanced/advanced', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advanced/advanced/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advanced.listing', {
#             'root': '/advanced/advanced',
#             'objects': http.request.env['advanced.advanced'].search([]),
#         })

#     @http.route('/advanced/advanced/objects/<model("advanced.advanced"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advanced.object', {
#             'object': obj
#         })
