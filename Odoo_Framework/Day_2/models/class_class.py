# __author__ = 'ITPLUS'

from odoo import models, fields, api


class ClassClass(models.Model):
    _name = 'lop'

    name = fields.Char(string='Name')
    state = fields.Selection(selection=[('open', 'Open'), ('close', 'Close')],
                             string='State', default='open')
    student_ids = fields.One2many(comodel_name='student',
                                  inverse_name='class_id', string='Students')
    teacher_id = fields.Many2many(comodel_name='teacher', string='Teachers', relation='lop_teacher_rel')
    student_count = fields.Integer(compute='_get_student_count', string='Student Count', store=True)
    leader = fields.Many2one('student', string='Leader')

    @api.depends('student_ids')
    def _get_student_count(self):
        for c in self:
            c.student_count = len(c.student_ids)


