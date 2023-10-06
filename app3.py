from flask import config, db
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)
app.app_context().push()

@app.route('/')
def index(): 
	return render_template('index.html')
	
if __name__ == "__main__":
	app.run(debug=True )