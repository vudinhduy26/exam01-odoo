from odoo import fields, models, api, _
from datetime import datetime, timedelta


class advancedSale(models.Model):
    _name = 'advanced.sale'
    _description = 'sale'

    def _default_validity_date(self):
        if self.env['ir.config_parameter'].sudo().get_param('sale.use_quotation_validity_days'):
            days = self.env.company.quotation_validity_days
            if days > 0:
                return fields.Date.to_string(datetime.now() + timedelta(days))
        return False

    customer = fields.Many2one(comodel_name='res.partner', string='Customer')

    name = fields.Char(string='Order Reference', required=True, copy=False,
                       states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    date_order = fields.Datetime(string='Order Date', required=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")

    validity_date = fields.Date(string='Expiration', copy=False,
                                states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                default=_default_validity_date)
    order_line = fields.Many2one(comodel_name='product.product', string='Order Lines', states={'cancel': [('readonly', False)], 'done': [('readonly', False)]}, copy=True, auto_join=True)

    customer_discount_code = fields.Text(string="Customer Discount")
    Sale_order_discount_estimated = fields.Integer()

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')