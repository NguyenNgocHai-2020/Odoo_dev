# __author__ = 'ITPLUS'

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    present_person = fields.Char(string='Present Person')

    @api.model
    def create(self, vals):
        if vals.get('present_person', ''):
            vals['present_person'] = self.convert_name_to_standard(vals.get('present_person', ''))
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        if vals.get('present_person', ''):
            vals['present_person'] = self.convert_name_to_standard(vals.get('present_person', ''))
        return super(SaleOrder, self).write(vals)

    def convert_name_to_standard(self, name_str):
        if name_str:
            return name_str.title()
