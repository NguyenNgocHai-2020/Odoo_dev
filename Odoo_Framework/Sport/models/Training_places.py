from odoo import api, fields, models


class Training_places(models.Model):
    _name = 'training.places'

    name = fields.Char(string='Name', required='1')
    address = fields.Char(string='Address', required='1')
    football_player_ids = fields.Many2many('football.player',
                                           string='Football Players')

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Training_places, self).create(vals)
        return res

    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Training_places, self).write(vals)
        return res