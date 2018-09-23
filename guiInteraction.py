import sqlite3
import pymysql
import recordingSnd

userID = input()
userPW = input()

awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
select_sql = "select userPassword from users_record where userID = %s"
cur = awsConn.cursor()
cur.execute(select_sql,(userID,))
row = cur.fetchall()

if len(row) != 0:
    for i in row :
        print(i[0])
        if userPW == i[0]:
            localConn = sqlite3.connect('database.db')
            localConn.execute("CREATE TABLE if not exists classifiedSound (userID VARCHAR(16) DEFAULT " + userID +", soundIndex INT, time TIMESTAMP)")
            localConn.close()
            recordingSnd.recording(userID)
        else:
            print("맞는 pw가 아닙니다")
else :
    print("존재하지 않는 id입니다")


awsConn.close()




