import sqlite3 as s
import datetime
 
with s.connect(r"database.db") as conn:
    cur = conn.cursor()
    sql = "insert into classifiedsound (soundIndex,time) values (?,?)"
 
    # 1건씩 추가하기
    cur.execute(sql, (5,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    print("inserting success!!")
    
    conn.commit()
    cur.close()
