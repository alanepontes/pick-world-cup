from ..commons.models import MetaModel

class User(db.Model, MetaModel):

	__metaclass__ = type('User', (type(db.Model), type(MetaModel)), {})
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.Text)

