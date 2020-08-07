from odoo import models, fields, api


class Booking(models.Model):
    _name = 'booking'
    _rec_name = 'id'

    customer_id = fields.One2many(comodel_name='customer', inverse_name='booking_ids', string='Customer')
    check_in = fields.Datetime(string='Check-in')
    check_out = fields.Datetime(string='Check-out')
    cost = fields.Float(compute='_total_price', string='Cost')
    room_ids = fields.One2many(comodel_name='room', inverse_name='booking_ids', string='Room')

    def _total_price(self):
        total_price = 0
        for booking in self:
            for c in booking.room_ids:
                cost = c.price_room * 0.5
                total_price += cost
            booking.cost = total_price

