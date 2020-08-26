from odoo import api, fields, models


class Club(models.Model):
    _name = 'club'

    name = fields.Char(string='Name', required="1")
    date = fields.Integer(string='Year', required="1")
    address = fields.Char(string='Address', default='Ha Noi')
    football_player_ids = fields.One2many(comodel_name='football.player',
                                          inverse_name='clb_id',
                                          string='Football Player')
    football_player_count = fields.Integer(string='Football Player Count',
                                           compute='_get_player_count',
                                           store=True)
    state = fields.Selection(selection=[('active', 'Active'),
                                        ('dissolution', 'Dissolution')],
                             default='active')
    coach = fields.Char(string='Coach')

    def dissolution_club(self):
        self.state = 'dissolution'

    @api.onchange('football_player_ids')
    def onchange_state_player(self):
        if self.football_player_ids:
            for player in self.football_player_ids:
                player.write({'state': 'payroll'})

    @api.depends('football_player_ids')
    def _get_player_count(self):
        for club in self:
            club.football_player_count = len(club.football_player_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Club, self).create(vals)
        return res

    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        res = super(Club, self).write(vals)
        return res



