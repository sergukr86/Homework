import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"


@app.route("/tracks")
def tracks():
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM tracks")
    cnt_lines = cur.fetchone()
    con.close()
    return render_template("music.html", cnt_lines=cnt_lines)


@app.route("/names")
def customers():
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("SELECT DISTINCT first_name FROM customers")
    f_name = cur.fetchall()
    con.close()
    return render_template("customers.html", f_name=f_name)


@app.route("/tracks-sec")
def duration():
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tracks")
    tracks_info = cur.fetchall()
    con.close()
    return render_template("tracks.html", tracks_info=tracks_info)


if __name__ == "__main__":
    app.run(debug=True)
