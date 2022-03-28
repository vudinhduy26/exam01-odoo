from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import json


class OrderProduct(models.Model):
    _inherit = 'sale.order'
    sale_order_discount_estimated = fields.Float(string="Sale order discount estimated", default=0,
                                                 related='partner_id.sale_order_discount_estimated')
    customer_discount_code = fields.Char(string="Discount code", related="partner_id.customer_discount_code")
    discout_order_check = fields.Boolean('Order Valid', default=False, related="partner_id.code_valid")
    show_discount = fields.Monetary(string="Totals discount", compute='_amount_all')

    @api.depends('order_line.price_total', 'sale_order_discount_estimated')
    def _amount_all(self):
        super(OrderProduct, self)._amount_all()
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax - (amount_untaxed + amount_tax) * (
                    order.sale_order_discount_estimated) / 100.0,
            })

            order.show_discount = (amount_untaxed + amount_tax) * (
                order.sale_order_discount_estimated) / 100.0
