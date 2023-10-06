from flask import Flask
# from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# app.app_context().push()
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(100), unique=True)
	# date_joined = db.Column(db.Date, default=timedelta.utcnow)

	def __repr__(self):
		return f'<User: {self.email}>'
	