from plugins import db
from ..commons.models import MetaModel

secondary_soccer_competition_team = db.Table('secondary_soccer_competition_team',
    db.Column('soccer_competition_id', db.Integer, db.ForeignKey('soccer_competition.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)

class SoccerCompetition(db.Model, MetaModel):
    
    __metaclass__ = type('SoccerCompetitionMeta', (type(db.Model), type(MetaModel)), {})
    __tablename__ = 'soccer_competition'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    keys = db.relationship("Key", cascade="all, delete-orphan")
    teams = db.relationship("Team",
                    secondary=secondary_soccer_competition_team)
    games = db.relationship("Game", cascade="all, delete-orphan")  

    def __init__(self, name):
        self.name = name


secondary_key_team = db.Table('secondary_key_team',
    db.Column('key_id', db.Integer, db.ForeignKey('key.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)

class Key(db.Model, MetaModel):

    __metaclass__ = type('KeyMeta', (type(db.Model), type(MetaModel)), {})
    __tablename__ = 'key'

    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100), unique=True)
    soccer_competition_id = db.Column(db.Integer, db.ForeignKey('soccer_competition.id'))
    soccer_competition = db.relationship("SoccerCompetition", back_populates="keys")
    teams = db.relationship("Team",
                    secondary=secondary_key_team)
    games = db.relationship("Game", cascade="all, delete-orphan")

    def __init__(self, name, soccer_competition):
        self.name = name
        self.soccer_competition = soccer_competition


class Team(db.Model, MetaModel):

    __metaclass__ = type('TeamMeta', (type(db.Model), type(MetaModel)), {})
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name


class Game(db.Model, MetaModel):
    
    __metaclass__ = type('GameMeta', (type(db.Model), type(MetaModel)), {})
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100), unique=True)
    
    team_one_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_one = db.relationship("Team", foreign_keys='Game.team_one_id')

    team_two_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_two = db.relationship("Team", foreign_keys='Game.team_two_id')

    key_id = db.Column(db.Integer, db.ForeignKey('key.id'))
    key = db.relationship("Key", back_populates="games")
    
    soccer_competition_id = db.Column(db.Integer, db.ForeignKey('soccer_competition.id'))
    soccer_competition = db.relationship("SoccerCompetition", back_populates="games")

    def __init__(self, name, team_one, team_two, key, soccer_competition):
        self.name = name
        self.team_one = team_one
        self.team_two = team_two
        self.key = key
        self.soccer_competition = soccer_competition

