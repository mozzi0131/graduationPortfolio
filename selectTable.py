import sqlite3 as lite

database_filename = 'database.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

#select table
query = "SELECT * FROM classifiedsound"
cs.execute(query)
all_rows = cs.fetchall()
for i in all_rows:
    print (i)

cs.close()
conn.close()
