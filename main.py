from backend import app
from Scrapingnew import main
import sqlite3

if __name__ == '__main__':
    main()

    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute('SELECT * FROM games')
    data = c.fetchall()
    conn.close()

    app.run(port=5000, host="0.0.0.0", debug=True)
