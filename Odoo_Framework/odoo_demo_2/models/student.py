# __author__ = 'ITPLUS'

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Student(models.Model):
    _name = 'student'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    class_id = fields.Many2one(comodel_name='class.class', string='Class')
    leader = fields.Many2one('student', string='Leader', related='class_id.leader', store=True)
    teacher_ids = fields.Many2many('teacher', string='Teachers')
    state = fields.Selection(selection=[('study', 'Study'), ('graduate', 'Graduate')], default='study')
    point = fields.Float(string='Point', default=0)

    _sql_constraints = [
        ('check_phone', 'check(LENGTH(phone) = 10)',
         'Phone number need 10 character - sql constrains')
    ]

    @api.onchange('class_id')
    def onchange_class_id(self):
        if self.class_id:
            self.teacher_ids = self.class_id.teacher_ids

    @api.onchange('phone')
    def onchange_phone(self):
        result = {}
        # if self.phone and len(self.phone) > 10:
        #     warning = {
        #         'title': 'Phone Warning!',
        #         'message': 'You must define phone number less than 10 character.',
        #     }
        #     result['warning'] = warning
        domain = {'teacher_ids': [('dob', '!=', False)]}
        result['domain'] = domain
        return result

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Student, self).create(vals)
        return res

    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Student, self).write(vals)
        return res

    @api.constrains('phone')
    def validate_phone(self):
        if not self.phone or len(self.phone) > 10 or len(self.phone) < 10:
            raise ValidationError('Phone number need 10 character')

    def graduate_action(self):
        for student in self:
            if student.point > 5.0:
                student.state = 'graduate'
            # else:
            #     raise ValidationError('The point need greater than 5.0')

    def graduate_action_one(self):
        if self.point > 5.0:
            self.state = 'graduate'
