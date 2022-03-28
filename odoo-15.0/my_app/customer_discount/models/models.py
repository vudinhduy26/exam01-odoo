from odoo import api, fields, tools, models


class test(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        print("u", self.env.user)
        print("u1", self.env.company)
        print("u2", self.env.companies)
        print("u3", self.env.context)
        print('data', vals)
        
        return super(test, self).create(vals)