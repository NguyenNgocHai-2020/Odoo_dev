from odoo import api, fields, models


class OrderLines(models.Model):
    _name = 'order.line'
    _rec_name = 'id'

    order_id = fields.Many2one(comodel_name='order', string='Order')
    product_id = fields.One2many(comodel_name='product', inverse_name='order_line', string='Product')
    qty = fields.Integer(string='Quantity')
    amount = fields.Float(string='Amount')
    sub_total = fields.Float(string='Total', compute='_get_total')

    # @api.onchange('product_id.price')
    # def onchange_amount(self):
    #     self.amount

    def _get_total(self):
        self.sub_total = self.qty * self.amount

