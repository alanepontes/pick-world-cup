from plugins import db
from ..commons.models import MetaModel
from ..competitions.models import Team

class Bet(db.Model, MetaModel):
    
    __metaclass__ = type('BetMeta', (type(db.Model), type(MetaModel)), {})
    __tablename__ = 'bet'
    
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100))
    team_one_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_one = db.relationship("Team", foreign_keys='Bet.team_one_id')
    gols_team_one = db.Column(db.Integer)

    team_two_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_two = db.relationship("Team"foreign_keys='Bet.team_two_id', )
    gols_team_two = db.Column(db.Integer)

    def __init__(self, value, team_one, gols_team_one, team_two, gols_team_two):
        self.value = value
        self.team_one = team_one
        self.gols_team_one = gols_team_one
        self.team_two = gols_team_two
        self.gols_team_two = gols_team_two


