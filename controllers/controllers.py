from odoo import http

# class Odoo-module-scaffold(http.Controller):
#     @http.route('/odoo-module-scaffold/odoo-module-scaffold/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-module-scaffold/odoo-module-scaffold/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-module-scaffold.listing', {
#             'root': '/odoo-module-scaffold/odoo-module-scaffold',
#             'objects': http.request.env['odoo-module-scaffold.odoo-module-scaffold'].search([]),
#         })

#     @http.route('/odoo-module-scaffold/odoo-module-scaffold/objects/<model("odoo-module-scaffold.odoo-module-scaffold"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-module-scaffold.object', {
#             'object': obj
#         })
