from flask import Flask
import Utils
from Score import get
app = Flask(__name__)
from MainGame import MainGame
from  Live import load_game

@app.route('/')
def score_server():
    ss=get()
    print(ss)
    try:
        score = ss

    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
                <h1>The score is  <div id="score">""" + str(ss) + """</div></h1>
        </body>
    </html>"""

@app.route('/gamepicker')
def game_picker():
    res=MainGame()

@app.route('/guessgame')
def gussgame():
    load_game(2)
    print ("finish guessgame")

@app.route('/memorygame')
def memorygame():
    load_game(1)
    print ("finish memorygame")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=8777)


