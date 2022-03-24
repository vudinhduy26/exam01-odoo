from odoo import fields, models, api
import re
import json


class customer(models.Model):
    _description = 'sales'
    _inherit = 'sale.order'

    customer_discount_code = fields.Text(string='Customer discount')
    Sale_order_discount_estimated = fields.Monetary(string="Money Discount Total Last")
    discounttat = fields.Float(string="Discount % ", compute="_discount_customer")

    # check = fields.Text(compute="check_discount_customer")

    @api.onchange('discounttat', 'customer_discount_code')
    def _discount_customer(self):
        z = 0
        pattern = re.compile(r"\d+")
        if self.customer_discount_code:
            for record in self:
                k = pattern.search(record.customer_discount_code)
                record.discounttat = float(k.group(0))
                z = float(k.group(0))
        return z

    show_discount_total = fields.Monetary(string=f"Discount Total", )


    @api.model
    def action_confirm(self):
        self.Sale_order_discount_estimated = 100


    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed','discounttat')
    def _compute_tax_totals_json(self):
        super(customer, self)._compute_tax_totals_json()
        def compute_taxes(order_line):
            price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
            order = order_line.order_id
            return order_line.tax_id._origin.compute_all(price, order.currency_id, order_line.product_uom_qty, product=order_line.product_id, partner=order.partner_shipping_id)

        account_move = self.env['account.move']
        for order in self:
            order.Sale_order_discount_estimated = order.amount_total - order.amount_total*(order.discounttat)/100.0
            tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line, compute_taxes)
            tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, order.Sale_order_discount_estimated, order.amount_untaxed, order.currency_id)
            order.tax_totals_json = json.dumps(tax_totals)
        self.show_discount_total = self.amount_total*(self.discounttat)/100.0
