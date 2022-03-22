from odoo import fields, models, api


class subject(models.Model):
    _name = 'subject.m.m'
    _description = 'Subject school'
    _order = 'date_create desc, name'
    name = fields.Char(string="Name subject ", required=True)
    date_create = fields.Date(string="Date create ")
    author_ids = fields.Many2many(comodel_name='res.partner', string='Creator')
    image_sub = fields.Binary(string="Image subject")
    description = fields.Html(string="Description subject", sanitize=True, strip_style=False)
    state = fields.Selection(
        [('not_available', 'Not Available'),
         ('available', 'Available')]
    )
    student_register_subject = fields.Many2many(comodel_name='student.m.m')
    numbers_student = fields.Integer(string='Number student', compute="_count_number_student_school")
    currency_id = fields.Many2many(comodel_name="res.currency", string="Currency")
    money = fields.Monetary(string="Money of subject",
                            currency_field='currency_id')

    @api.depends('numbers_student')
    def _count_number_student_school(self):
        for record in self:
            record.numbers_student = len(record.student_register_subject)
