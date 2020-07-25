from odoo import api, fields, models

# class odoo-module-scaffold(models.Model):
#     _name = 'odoo-module-scaffold.odoo-module-scaffold'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
