from odoo import models, api, fields


class productProduct(models.Model):
    _name = 'product.product.db'
    _description = 'product'

    name = fields.Char(string="Name Product")
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
    unit_price = fields.Monetary(string='Unit Price',
                                currency_field='currency_id', )
