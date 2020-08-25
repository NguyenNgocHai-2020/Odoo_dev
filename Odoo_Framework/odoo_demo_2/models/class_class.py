# __author__ = 'ITPLUS'

from odoo import models, fields, api


class ClassClass(models.Model):
    _name = 'class.class'

    name = fields.Char(string='Name')
    state = fields.Selection(selection=[('open', 'Open'), ('close', 'Close')],
                             string='State', default='open')  # readonly=True
    student_ids = fields.One2many(comodel_name='student',
                                  inverse_name='class_id', string='Students')
    teacher_ids = fields.Many2many(comodel_name='teacher', relation='teacher_class_rel',
                                   column1='class_id', column2='teacher_id', string='Teachers')
    student_count = fields.Integer(compute='_get_student_count', string='Student Count', store=True)
    leader = fields.Many2one('student', string='Leader')

    @api.depends('student_ids')
    def _get_student_count(self):
        for c in self:
            c.student_count = len(c.student_ids)

    def close_class_action(self):
        self.state = 'close'

    def open_class_action(self):
        self.state = 'open'

    def graduate_class_action(self):
        # self.student_ids.graduate_action()
        self.student_ids.graduate_action_one()
