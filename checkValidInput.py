import pymysql

def checkValidData(data,userID):
    awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')

    cur = awsConn.cursor()

    if data == 0:
        #siren
        cur.execute("select sirenOn from user_settings where userID = %s", userID)
    elif data == 1:
        #fire alarm
        cur.execute("select fireOn from user_settings where userID = %s", userID)
    elif data == 2:
        #boiling water
        cur.execute("select waterOn from user_settings where userID = %s", userID)
    elif data == 3:
        #dog
        cur.execute("select dogOn from user_settings where userID = %s", userID)

    result = cur.fetchone()

    print("data is",data,"and result is",result[0])

    cur.close()

    print("cur is closed")
    if result[0] == 0:
        print("return False")
        return False
    elif result[0] == 1:
        print("return True")
        return True
