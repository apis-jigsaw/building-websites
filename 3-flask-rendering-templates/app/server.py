from flask import Flask, render_template
app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def hello():
    return render_template('index.html')
  
@app.route('/nhl/players/')
def nhl():
    return render_template('player.html')
  
  
app.run()