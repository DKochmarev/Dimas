from flask import Flask, render_template
import dbnew

app = Flask(__name__)

@app.route("/")
def page():
    answers = dbnew.Database()
    return render_template("index.html", answer=answers)

if __name__ == '__main__':
    app.run(debug=True)