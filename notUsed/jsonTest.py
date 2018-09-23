from flask import Flask
import sqlite3 as lite
import json
from flask import jsonify

database_filename = 'database.db'
conn = lite.connect(database_filename)
cs = conn.cursor()
app = Flask(__name__)

@app.route("/getEmployeeList")
def getEmployeeList():
    
    try:

        # Initialize a employee list
        employeeList = []

        # create a instances for filling up employee list
        for i in range(0,2):
            empDict = {
            'firstName': 'Roy',
            'lastName': 'Augustine'}
            employeeList.append(empDict)
    
        # convert to json data
        jsonStr = json.dumps(employeeList)

    except Exception as e:
        print(e)

    return jsonify(Employees=jsonStr)

if __name__ == "__main__":
    app.run()



#출처: http://november11tech.tistory.com/75 [Mr.november11]
