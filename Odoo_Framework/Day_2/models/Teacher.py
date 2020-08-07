from odoo import models, fields, api


class Teacher(models.Model):
    _name = "teacher"

    image = fields.Binary(string='Image', attachment=True)
    name = fields.Char(string='Name', required=True)
    age_teacher = fields.Integer(string='Age', default=25)
    address_teacher = fields.Char(string='Address', invisible=True)
    gender_teacher = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender',
                                      default='male')
    # class_id = fields.Many2many(comodel_name='class', relation='teacher_class_rel', column1='teacher_id',
    #                             column2='class_id', string='class_id')
    class_ids = fields.Many2many(comodel_name='lop', string='Class')
