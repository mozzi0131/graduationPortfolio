import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE classifiedSound (soundIndex INT, time TIMESTAMP)')
print ("Table created successfully");
conn.close()
