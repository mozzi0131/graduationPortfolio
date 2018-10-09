import requests
import json
import sys
import pymysql
import datetime

def sendPushAlarm(data,userID):
    awsPW_sql = "select userToken from users_record where userID = %s"
    awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
    cur = awsConn.cursor()
    
    if data == 0:
        title = "사이렌 소리"
    elif data == 1:
        #fire alarm
         title = "화재경보기 소리"
    elif data == 2:
        #boiling water
         title = "물 끓는 소리"
    elif data == 3:
        #dog
         title = "개 짖는 소리"

    cur.execute(awsPW_sql,userID)

    result = cur.fetchone()

    print("token is",result[0])

    url = 'https://fcm.googleapis.com/fcm/send'

    body = {
        "data": { 
        "title": title+"가 발생했습니다",
        "body":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"에"+title+"가 발생했습니다."
        },
        "to": result[0]
    }

    headers = {
        'Content-Type': 'application/json; UTF-8',
        'Authorization': 'key=AAAA4JNgslk:APA91bE9n-dVOrQWSgQnCLT3qaigpxWQoLc0KEdJJM1RrYqq4qVZ4j9lb32UwahJJqYF-bedwNxqcM6iIzJ-a2P-10UyidyMKkR9QOuxSP9hep_jNGOwMVWmRZwPq7FQer2L5wiU_Kmq'
    }

    req = requests.post(url, headers=headers, data=json.dumps(body))
    print("data pushed!!")

    cur.close()
