from odoo import fields, models, api
import re


class customer(models.Model):
    _description = 'sales'
    _inherit = 'sale.order'

    customer_discount_code = fields.Text(string='Customer discount')
    Sale_order_discount_estimated = fields.Integer(string="Discount Total")
    discount = fields.Float(string="Discount % ", compute="_discount_customer")
    #check = fields.Text(compute="check_discount_customer")

    @api.onchange('discount', 'customer_discount_code')
    def _discount_customer(self):
        pattern = re.compile(r"\d+")
        if self.customer_discount_code:
            for record in self:
                k = pattern.search(record.customer_discount_code)
                record.discount = float(k.group(0))


