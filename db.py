import sqlite3

connection = sqlite3.connect("my_database.db")
sql = '''CREATE TABLE games (name TEXT, views INTEGER, likes INTEGER, size TEXT, type TEXT)'''
sql1 = 'SELECT * FROM games'
cursor = connection.cursor()
cursor.execute(sql1)
#
res = cursor.fetchall()
i = 0
for r in res:
    print(r)
connection.commit()
connection.close()
