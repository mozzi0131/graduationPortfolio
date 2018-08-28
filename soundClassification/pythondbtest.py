import sqlite3 as s
import datetime


def insertData(data):
    with s.connect(r"database.db") as conn:
        cur = conn.cursor()
        sql = "insert into classifiedsound (soundIndex,time) values (?,?)"
 
    # 1건씩 추가하기
    #여기서 이전 데이터와 비교해서?? 최근 것과 큰 시간차없이 같은 data 들어가면 막
        cur.execute(sql, (data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        print("inserting success!!")
    
        conn.commit()
        cur.close()
