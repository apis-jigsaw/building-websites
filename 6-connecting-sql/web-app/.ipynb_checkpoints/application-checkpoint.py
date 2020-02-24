# application.py
import sqlite3
from flask import Flask, render_template
from player import Player

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/nhl/players/<player_id>')
def show_player(player_id):
    conn = sqlite3.connect('nhl.db')
    cursor = conn.cursor()
    cursor.execute('select * from players where id = ?;', player_id)
    player_details = cursor.fetchone()
    player = Player(*player_details)
    return str(player.__dict__)

app.run()