from odoo import api, fields, models


class Order(models.Model):
    _name = 'order'
    _rec_name = 'id'

    customer_id = fields.Many2one(comodel_name='customer', string='Customer')
    order_date = fields.Date(string='Date')
