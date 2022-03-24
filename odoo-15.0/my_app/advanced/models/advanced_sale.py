from odoo import fields, models, api, _
from datetime import datetime, timedelta


class advancedSale(models.Model):
    _inherit = 'res.partner'