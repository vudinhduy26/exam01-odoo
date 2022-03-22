from odoo import fields, api, models
from datetime import timedelta
from odoo.exceptions import ValidationError
import re


class student(models.Model):
    _name = 'student.m.m'
    _description = 'This is model students'
    _order = 'name desc'
    name = fields.Char(string='Full Name', required=True)
    age = fields.Integer(string='Age')
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Sex')
    address = fields.Char(string='Address', required=True)
    date_birth = fields.Date(string='Date of birth')
    number_phone = fields.Char(string='Number phone')
    face_student = fields.Binary(string="Face Image", help="Select image here")
    level = fields.Selection([
        ('c1', 'Primary School.'),
        ('c2', 'Junior high school.'),
        ('c3', 'High school.'),
    ])
    subjects_were_register = fields.Many2many(comodel_name='subject.m.m', string="Subject")

    @api.onchange('level', 'age')
    def _check_level(self):
        for record in self:
            # onchange
            # if record.level == 'c1':
            #     if int(record.age) >= 6 or int(record.age) <= 10:
            #         raise models.ValidationError('Date must be in the past')
            if 6 <= int(record.age) <= 10:
                if record.level == 'c2' or record.level == 'c3':
                    raise models.ValidationError("Can't choose Junior high school , High school.")
            elif 11 <= int(record.age) <= 14:
                if record.level == 'c1' or record.level == 'c3':
                    raise models.ValidationError("Can't choose Primary School , High school.")
            elif 15 <= int(record.age) <= 18:
                if record.level == 'c1' or record.level == 'c2':
                    raise models.ValidationError("Can't choose Primary School , Junior high school.")

    @api.constrains('age')
    def _check_age(self):
        rere = re.compile(r'[0-9]{1,2}$')
        for record in self:
            if not rere.search(str(record.age)):
                raise ValidationError('This is not Age')
            elif int(record.age) <= 5 or int(record.age) >= 18:
                raise ValidationError("You can't join")

    @api.constrains('number_phone')
    def _check_phone(self):
        rere = re.compile(r'[0-9]{10,14}$')
        for record in self:
            if not rere.search(record.number_phone):
                raise ValidationError('This not number phone')

    @api.constrains('date_birth')
    def _check_birth(self):
        for record in self:
            if record.date_birth and record.date_birth > fields.Date.today():
                raise models.ValidationError('Date must be in the past')
