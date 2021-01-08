from flask import Flask, render_template, redirect, url_for, request, json
import queries
import datetime

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = get_movies()
    roles = get_roles()
    return render_template('build_by_movie.html',movies_lst = movies_lst, roles= roles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
