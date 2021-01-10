from flask import Flask, render_template, redirect, url_for, request,session
import queries
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/build_by_movie", methods = ["GET","POST"])
def build_by_movie():
    movies_lst = queries.get_movies()
    roles = queries.get_roles()
    return render_template('build_by_movie.html',movies_lst = movies_lst, roles= roles)

@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  get_profiles_by_role_and_movie(role,movie_id)
    return render_template('build_by_movie_results.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
