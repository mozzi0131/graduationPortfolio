import sqlite3 as s
import datetime

data = 2

if __name__ == "__main__":
#def insertData(data):
    with s.connect(r"database.db") as conn:
        cur = conn.cursor()
        insert_sql = "insert into classifiedsound (soundIndex,time) values (?,?)"
        select_sql = "select soundIndex,time from classifiedsound order by time desc limit 1"
 
    # 1건씩 추가하기
    #여기서 이전 데이터와 비교해서?? 최근 것과 큰 시간차없이 같은 data 들어가면 pass하기
    #가장 최신인 데이터에 어떻게 입력하는가? << ascend/descend order로 접근?

    #SELECT * FROM clients ORDER BY id LIMIT 1 < 이러ㅓㄴ식으로
        cur.execute(select_sql)
        row = cur.fetchall()

        for i in row:
            #여기서 i에 접근해서 데이터값 받아오고.. 
            latest_data = i

        if latest_data[0] == data :
            latest_time = latest_data[1]
            latest_hour = latest_time.split(':')[0]
            latest_minute = latest_time.split(':')[1]
            latest_second = latest_time.split(':')[2]

            latest_cal = latest_hour*3600 + latest_minute*60 + latest_second

            dateInfo = str(datetime.datetime.now()).split('.')[0]
            print(dateInfo)
            now_time = dateInfo.split(' ')[1]
            now_hour = now_time.split(':')[0]
            now_minute = now_time.split(':')[1]
            now_second = now_time.split(':')[2]

            now_cal = now_hour*3600 + now_minute*60 + now_second

            if latest_cal - now_cal <= 300:
                break;
            else :
                cur.execute(insert_sql, (data,dateInfo)
                conn.commit()
                cur.close()

        else :
            cur.execute(insert_sql, (data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            cur.close()
