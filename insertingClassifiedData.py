import sqlite3 as s
import pymysql
import datetime
import postPush

#if __name__ == "__main__":
def insertData(data,userID):
    print("insertData")
    AWSinsert_sql = "insert into sound_record(recordNum, userID, soundType, recordDate) values (NULL,%s,%s,%s)"
    AWStest_sql = "select * from sound_record order by recordDate"
    
    sqliteSelect_sql = "select * from classifiedsound where soundIndex = ? order by time desc limit 1"
    sqliteInsert_sql = "insert into classifiedsound (soundIndex,time) values (?,?)"
    
    with s.connect(r"database.db") as sqliteConn:
        localcur = sqliteConn.cursor()

        localcur.execute(sqliteSelect_sql,(data,))
        row = localcur.fetchall()

        if len(row) == 0 :
            print("넣습니다~~~")
            print(userID)
            localcur.execute(sqliteInsert_sql,(data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
            cur = awsConn.cursor()
            cur.execute(AWSinsert_sql, (userID,data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            awsConn.commit()

            postPush.sendPushAlarm(data,userID)
            print("postPush called")

            cur.execute(AWStest_sql)
            t_result = cur.fetchall()

            for j in t_result:
                print(j)

                
                    
            cur.close()

#여기서부터 다시 수정하면됨
            
        else :
            for i in row:
                print(i)
                latest_data = i

            latestDate = latest_data[2]
            latest_YMD= latestDate.split(' ')[0]
            latest_Y = latest_YMD.split('-')[0]
            latest_M = latest_YMD.split('-')[1]
            latest_D = latest_YMD.split('-')[2]
            
            nowDate = str(datetime.datetime.now()).split('.')[0]
            now_YMD = nowDate.split(' ')[0]
            now_Y = now_YMD.split('-')[0]
            now_M = now_YMD.split('-')[1]
            now_D = now_YMD.split('-')[2]

            if latest_Y == now_Y and latest_M == now_M and latest_D == now_D :
                #비교
                latest_time = latestDate.split(' ')[1].split(':')
                print(latest_time)
                latest_hour = (int)(latest_time[0])
                latest_minute = (int)(latest_time[1])
                latest_second = (int)(latest_time[2])
    
                latest_cal = latest_hour*3600 + latest_minute*60 + latest_second
    
                nowDate = str(datetime.datetime.now()).split('.')[0]
                dateInfo = nowDate.split(' ')[1].split(':')
                print(dateInfo)
    
                now_hour = (int)(dateInfo[0])
                now_minute = (int)(dateInfo[1])
                now_second = (int) (dateInfo[2])

                now_cal = now_hour*3600 + now_minute*60 + now_second

                print(now_cal - latest_cal)

                if abs(now_cal - latest_cal) > 300:
                    print("시간차 확인하고 데이터 삽입함")
                    localcur.execute(sqliteInsert_sql,(data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
                    cur = awsConn.cursor()
                    cur.execute(AWSinsert_sql, (userID,data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    awsConn.commit()
                    postPush.sendPushAlarm(data,userID)
                    print("postPush called")
               
                    cur.close()
                else:
                    print("같은 소리가 반복적으로 입력되고 있습니다.")
            else:
                print("ok")
                localcur.execute(sqliteInsert_sql,(data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
                cur = awsConn.cursor()
                cur.execute(AWSinsert_sql, (userID, data,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                awsConn.commit()
                postPush.sendPushAlarm(data,userID)
                print("postPush called")

                cur.close()

    
