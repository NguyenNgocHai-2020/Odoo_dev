from odoo import api, fields, models


class Product(models.Model):
    _name = 'product'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    price = fields.Float(string='Price')
    order_line = fields.Many2one(comodel_name='order.line')