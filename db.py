import sqlite3

def Database():
    with sqlite3.connect("qqq.db") as connection:
        sql = '''CREATE TABLE games (name TEXT, views INTEGER, likes INTEGER, size TEXT, type TEXT)'''
        sql1 = 'SELECT * FROM games'
        cursor = connection.cursor()
        cursor.execute(sql1)
        results = cursor.fetchall()
        for i, row in enumerate(results, 1):
            print(row, i)

if __name__ == "__main__":
    Database()
