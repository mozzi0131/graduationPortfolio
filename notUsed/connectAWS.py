import pymysql

db = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')

cursor = db.cursor()

cursor.execute("select * from sound_record")

rows = cursor.fetchall()
for i in rows:
    print(i)
