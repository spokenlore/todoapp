import os

from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__, instance_relative_config=True)

app.config.update(dict(
    DATABASE='/tmp/flaskr.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

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

if __name__ == '__main__':
    init_db()
    app.run()
