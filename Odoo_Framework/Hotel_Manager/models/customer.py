from odoo import models, fields, api


class Customer(models.Model):
    _name = 'customer'
    _rec_name = 'customer_name'

    customer_name = fields.Char(string='Name', required=True)
    customer_phone = fields.Char(string='Phone Number')
    customer_ID = fields.Char(string='ID No')
    customer_amount = fields.Integer(string='Amount')
    booking_ids = fields.Many2one(comodel_name='booking', string='Booking')