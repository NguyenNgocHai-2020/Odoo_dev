# __author__ = "ITPLUS"

from odoo import models, fields, api


class Student(models.Model):
    _inherit = 'student'

    code = fields.Char(string='Student Code', default='New', readonly=1)

    @api.model
    def default_get(self, default_fields):
        res = super(Student, self).default_get(default_fields)

        return res

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('STUDENT_SEQUENCE')
        return super(Student, self).create(vals)
