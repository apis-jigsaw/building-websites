# application.py
import sqlite3
from flask import Flask, render_template, g
from player import Player
import os
import pdb

app = Flask(__name__, static_folder='public', template_folder='views')

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nhl.db'),
))

@app.route('/nhl/players/<player_id>')
def show_player(player_id):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('select * from players where id = ?;', player_id)
    player_details = cursor.fetchone()
    player = Player(*player_details)
    return render_template('player-1.html', player = player)

@app.route('/nhl/players')
def players():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('select * from players;')
    player_rows = cursor.fetchall()
    players = [Player(*player_row) for player_row in player_rows]
    return render_template('players.html', players = players)
app.run(debug = True)
