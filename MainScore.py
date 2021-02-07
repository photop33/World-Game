from flask import Flask

import Utils
from Score import get
app = Flask(__name__)

@app.route('/')
def score_server():
    ss=get()
    print(ss)
    try:
        score = open("C:\\Users\\l1313\\Desktop\\New folder\\HEllo.txt", "r")

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
                <h1>The score is <div id="score">""" + str(ss) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=8777)


