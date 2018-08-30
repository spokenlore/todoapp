import os

from flask import Flask, render_template

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)
	
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
