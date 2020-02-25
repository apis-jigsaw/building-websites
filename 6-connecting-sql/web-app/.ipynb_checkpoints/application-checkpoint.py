# application.py
import sqlite3
from flask import Flask, render_template
from player import Player
import os

app = Flask(__name__, static_folder='public', template_folder='views')

app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nhl.db'),
))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/nhl/players/<player_id>')
def show_player(player_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('select * from players where id = ?;', player_id)
    player_details = cursor.fetchone()
    player = Player(*player_details)
    return render_template('player-1.html', player = player)

app.run()
