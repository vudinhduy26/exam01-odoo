from odoo import fields, api, models


class Custom(models.Model):
    _name = 'advanced.sale.db'
    _description = 'discount'
    _inherit = 'sale.order'

    transaction_ids = fields.Many2many(
          'sale.order.transaction', 'sale_transaction_ids',
          'trans_id', 'trans.sale_id',
          string='Tags')
    tag_ids = fields.Many2many(
          'sale.order.tag', 'sale_tag_ids',
          'tag_id', 'tag.sale_id',
          string='Tags')
    customer_discount_code = fields.Text(string='Customer discount')

