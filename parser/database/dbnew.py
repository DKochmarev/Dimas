import sqlite3
# conn = sqlite3.connect("qqq.db")
# sql = '''CREATE TABLE games (name TEXT, views INTEGER, likes INTEGER, size TEXT, type TEXT)'''
# cursor = conn.cursor()
# cursor.execute(sql)

def Database():
    with sqlite3.connect("qqq.db") as connection:
        sql1 = 'SELECT * FROM games'
        cursor = connection.cursor()
        cursor.execute(sql1)
        results = cursor.fetchall()
        return results

if __name__ == "__main__":
    Database()