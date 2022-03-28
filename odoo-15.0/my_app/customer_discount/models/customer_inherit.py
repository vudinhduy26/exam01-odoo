from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import re


class Customer(models.Model):
    _inherit = "res.partner"
    customer_discount_code = fields.Char('Discount Code')
    code_valid = fields.Boolean('Sale code Valid', default=False)
    sale_order_discount_estimated = fields.Float("Discount % ", compute='_calculator_discount_estimated')

    @api.model
    def _calculator_discount_estimated(self):
        pattern = re.compile(r"\d+")
        self.sale_order_discount_estimated = 0.0
        self.code_valid = False
        if self.customer_discount_code:
            first = self.customer_discount_code[0:4]
            last = self.customer_discount_code[4:]
            if first == "VIP_" and last.isdigit() and len(last) < 3:
                for record in self:
                    k = pattern.search(record.customer_discount_code)
                    record.sale_order_discount_estimated = float(k.group(0))
                self.code_valid = True
