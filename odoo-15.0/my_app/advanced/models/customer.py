from odoo import fields , models ,api
import re

class customer(models.Model):
    _description = 'sales'
    _inherit = 'sale.order'

    customer_discount_code = fields.Text(string='Customer discount')
    Sale_order_discount_estimated = fields.Integer(string="Discount Total")

    def discount_customer(self):
        regex = re.compile(r'[0-9]+')
        result = regex.search(self.customer_discount_code)
        return result
