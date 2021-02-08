import datetime
import pymysql

def get():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    cursor = conn.cursor()
    conn.autocommit(True)
    (cursor.execute("SELECT * FROM Q2PbjAC1nT.Game;"))
    result = cursor.fetchall()
    a=len(result)
    b=result[a - 1]
    print(b[1])
    score = str(b[1])
    return score
    cursor.close()
    conn.close()


def add_score(difficulty):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    cursor = conn.cursor()
    conn.autocommit(True)
    (cursor.execute("SELECT idGame FROM Q2PbjAC1nT.Game;"))
    result = cursor.fetchall()
    ten=len(result)
    if ten != 0:
        for i in result[ten-1]:
            print(i)
            point=i +difficulty
        id = (cursor.execute("SELECT id FROM Q2PbjAC1nT.Game;"))
        id = id + 1
    else:
        id=1
        point = difficulty
    cursor.close()
    conn.close()



    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    conn.autocommit(True)
    cursor = conn.cursor()
    now = datetime.datetime.utcnow()
    str_now = now.date().isoformat()
    print("Point-",point)
    cursor.execute('INSERT INTO Q2PbjAC1nT.Game (id,idGame,Gamecol) VALUES (%s,%s,%s)',(id,point,str_now))
    cursor.close()
    conn.close()



