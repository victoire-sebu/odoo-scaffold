# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleName(http.Controller):
#     @http.route('/module_name/module_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_name/module_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_name.listing', {
#             'root': '/module_name/module_name',
#             'objects': http.request.env['module_name.module_name'].search([]),
#         })

#     @http.route('/module_name/module_name/objects/<model("module_name.module_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_name.object', {
#             'object': obj
#         })
