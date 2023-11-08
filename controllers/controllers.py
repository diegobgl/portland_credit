# -*- coding: utf-8 -*-
# from odoo import http


# class PortlandCredit(http.Controller):
#     @http.route('/portland_credit/portland_credit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portland_credit/portland_credit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('portland_credit.listing', {
#             'root': '/portland_credit/portland_credit',
#             'objects': http.request.env['portland_credit.portland_credit'].search([]),
#         })

#     @http.route('/portland_credit/portland_credit/objects/<model("portland_credit.portland_credit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portland_credit.object', {
#             'object': obj
#         })
