#Delete Pymysql
import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
cursor = conn.cursor()
conn.autocommit(True)
for i in range (0,24):
    x=str(i)
    print(x)
    (cursor.execute("DELETE FROM Game WHERE idGame = "+ x +" "))