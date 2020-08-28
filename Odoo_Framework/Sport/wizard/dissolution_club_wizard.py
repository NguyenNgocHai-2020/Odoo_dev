from odoo import api, fields, models


class DissolutionClubWizard(models.Model):
    _name = 'dissolution.club.wizard'

    football_player_ids = fields.Many2many('football.player', string='Football Players')

    @api.model
    def default_get(self, default_fields):
        res = super(DissolutionClubWizard, self).default_get(default_fields)
        if self.env.context.get('active_id', False):
            club_record = self.env['club'].browse(self.env.context.get('active_id'))
            res['football_player_ids'] = [(6, 0, club_record.football_player_ids.ids)]
        return res

    def dissolution_club(self):
        if self.env.context.get('active_id', False):
            club_record = self.env['club'].browse(self.env.context.get('active_id'))
            club_record.dissolution_club()