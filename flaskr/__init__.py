import os

from flask import Flask, render_template
import db

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
	SECRET_KEY='dev',
	DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

def init_db():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.cli.command('initdb')
def initdb_command():
	"""Initializes the database."""
	init_db()
	print('Initialized the database.')


def create_app(test_config=None):
	
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	@app.route('/register')
	def register():
		return render_template("register.html") 
	
	@app.route('/login')
	def login():
		return render_template("login.html")
	
	return app
