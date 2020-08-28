from odoo import api, fields, models


class Customer(models.Model):
    _name = 'customer'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')],
                              default='male')

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
            vals['name'] = vals['name'] + 'PYA0520E'
        res = super(Customer, self).create(vals)
        return res

    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
            vals['name'] = vals['name'] + 'PYA0520E'
        res = super(Customer, self).write(vals)
        return res
