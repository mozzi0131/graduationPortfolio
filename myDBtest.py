from flask import Flask
import sqlite3 as lite
import json
from flask import jsonify

database_filename = 'database.db'

app = Flask(__name__)

@app.route("/getsqliteTest")
def getEmployeeList():
    
    try:
        #initiailize result set
        resultSet = []
        
        conn = lite.connect(database_filename)
        cs = conn.cursor()
        query = "SELECT * FROM classifiedsound"
        cs.execute(query)
        all_rows = cs.fetchall()

        # create a instances for filling up employee list
        for i in all_rows:
            content = {'index':i[0],'timestamp':i[1]}
            resultSet.append(content)
            content = {}

    except Exception as e:
        print(e)

    return jsonify(resultSet)

if __name__ == "__main__":
    app.run()



#출처: http://november11tech.tistory.com/75 [Mr.november11]
