# __author__ = 'ITPLUS'

from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher'

    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of Birth')
    phone = fields.Char(string='Phone')
    class_ids = fields.Many2many(comodel_name='class.class',
                                 relation='teacher_class_rel',
                                 column1='teacher_id', column2='class_id',
                                 string='Class')
    # class_ids = fields.Many2many(comodel_name='class.class', string='Class')
