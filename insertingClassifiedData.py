import sqlite3 as s
import datetime

data = 1

#if __name__ == "__main__":
def insertData(data):
    with s.connect(r"database.db") as conn:
        cur = conn.cursor()
        insert_sql = "insert into classifiedsound (soundIndex,time) values (?,?)"
        select_sql = "select * from classifiedsound where soundIndex = ? order by time desc limit 1"

        test_sql = "select * from classifiedsound order by time"
 
    # 1건씩 추가하기
    #여기서 이전 데이터와 비교해서?? 최근 것과 큰 시간차없이 같은 data 들어가면 pass하기
    #가장 최신인 데이터에 어떻게 입력하는가? << ascend/descend order로 접근?

    #SELECT * FROM clients ORDER BY id LIMIT 1 < 이러ㅓㄴ식으로
        cur.execute(select_sql,(data,))
        row = cur.fetchall()

        #list가 empty면 걍 데이터 넣으면 된다는 말임
        if len(row) == 0 :
            cur.execute(insert_sql, (data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()

            cur.execute(test_sql)
            t_result = cur.fetchall()

            for j in t_result:
                print(j)
                    
            cur.close()


        else :
            for i in row:
                print(i)
                latest_data = i

            latest_time = latest_data[1].split(' ')[1].split(':')
            print(latest_time)

            latest_hour = (int)(latest_time[0])
            latest_minute = (int)(latest_time[1])
            latest_second = (int)(latest_time[2])

            latest_cal = latest_hour*3600 + latest_minute*60 + latest_second

            nowDate = str(datetime.datetime.now()).split('.')[0]
            dateInfo = nowDate.split(' ')[1].split(':')

            now_hour = (int)(dateInfo[0])
            now_minute = (int)(dateInfo[1])
            now_second = (int) (dateInfo[2])

            now_cal = now_hour*3600 + now_minute*60 + now_second

            if latest_cal - now_cal > 300:
                cur.execute(insert_sql, (data,nowDate))
                conn.commit()

                cur.execute(test_sql)
                t_result = cur.fetchall()

                for j in t_result:
                    print(j)
                
               
                cur.close()
            else:
                print("같은 소리가 반복적으로 입력되고 있습니다.")
