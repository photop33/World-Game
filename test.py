from flask import Flask, request
from test1 import get_idGame, bb
import pymysql
app = Flask(__name__)
@app.route('/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        get_idGame()
        print(bb)
        return "<H1 id='user'>" + bb + "</H1>"




    else:
        if request.method == 'GET':
            # return "<h1>The score is <div id="+ result +">{SCORE}</div></h1>", 200  # status code
            # get()
            return "<H1 id='user'>" + bb + "</H1>"


app.run(host='127.0.0.1', debug=True, port=3000)
