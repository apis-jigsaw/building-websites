from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/players')
def whatever():
    return 'player 1, player 2'
