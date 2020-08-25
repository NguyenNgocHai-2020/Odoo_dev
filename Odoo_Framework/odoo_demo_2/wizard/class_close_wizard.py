# __author__ = "ITPLUS"

from odoo import models, fields, api


class ClassCloseWizard(models.TransientModel):
    _name = 'class.close.wizard'

    # student_ids = fields.Many2many('student', string='Student')
    #
    # @api.model
    # def default_get(self, default_fields):
    #     res = super(ClassCloseWizard, self).default_get(default_fields)
    #     if self.env.context.get('active_id', False):
    #         class_record = self.env['class.class'].browse(self.env.context.get('active_id'))
    #         res['student_ids'] = [(6, 0, class_record.student_ids.ids)]
    #     return res
    #
    # @api.multi
    # def close_class(self):
    #     if self.env.context.get('active_id', False):
    #         class_record = self.env['class.class'].browse(self.env.context.get('active_id'))
    #         class_record.graduate_class_action()

    def close_class(self):
        if self.env.context.get('active_id', False):
            class_record = self.env['class.class'].browse(self.env.context.get('active_id'))
            class_record.graduate_class_action()
