from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def page():
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute('SELECT * FROM games')
    answers = c.fetchall()
    conn.close()
    return render_template("index.html", answer=answers)

if __name__ == '__main__':
    app.run(debug=True)