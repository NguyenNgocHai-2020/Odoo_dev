from odoo import models, fields, api


# reqeired : được sửa
#     invisible : ẩn
#     readonly : chỉ đọc
#     attrs="{key:[(điều kiện),(),...]}"

class Students(models.Model):
    _name = 'student'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    address = fields.Char(string="Address", invisible=True)
    dob = fields.Date(string="Date of birth", default='2002-1-1')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                              string='Gender', default='male')
    class_id = fields.Many2one(comodel_name='lop', string='CLass')
    leader = fields.Many2one('student', string='Leader', related='class_id.leader', store=True)
    teacher_id = fields.Many2many('teacher', string='Teacher')

    @api.onchange('class_id')
    def onchange_class_id(self):
        if self.class_id:
            self.teacher_id = self.class_id.teacher_id

    @api.onchange('phone')
    def onchange_phone(self):
        result = {}
        if self.phone and len(self.phone) > 10:
            warning = {
                'title': 'Phone Warning!',
                'message': 'You must define phone number less than 10 character.',
            }
            result['warning'] = warning
        domain = {'teacher_ids': [('dob', '!=', False)]}
        result['domain'] = domain
        return result

    # @api.model
    # def create(self, vals):
    #     # self rỗng
    #     vals['name'] = vals['name'].title()
    #     res = super(Students, self).create(vals)
    #     return res
    

    def write(self, vals): 
        # self đại diện cho bản ghi cần sửa
        vals['name'] = vals['name'].title()
        res = super(Students, self).write(vals)
        return res
        
