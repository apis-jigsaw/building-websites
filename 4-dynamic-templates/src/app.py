from flask import Flask, render_template
app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def hello():
    return render_template('index.html')
  
@app.route('/nhl/players/<player_name>')
def nhl(player_name):
    return render_template('player.html', name=player_name)
  
app.run()