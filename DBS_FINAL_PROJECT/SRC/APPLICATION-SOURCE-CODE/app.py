from flask import Flask, render_template, redirect, url_for, request,session
from flask_session import session
import queries
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/index")
def index():
    if session.get("crew") is None:
        session["crew"] = []
    return render_template('index.html')

@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = get_movies()
    roles = get_roles()
    return render_template('build_by_movie.html',movies_lst = movies_lst, roles= roles)

@app.route("/build_by_movie_results", methods=["POST"])
    def build_by_movie_results():
        movie_id = request.form.get("movie_id")
        role = request.form.get("role")
        res =  get_profiles_by_roles_and_movie(role,movie_id)
        return render_template('build_by_movie_results.html')

@app.route("/crew_lst")
    def show_crew():
        return render_template('crew_list.html', crew_lst = session.get("crew"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
