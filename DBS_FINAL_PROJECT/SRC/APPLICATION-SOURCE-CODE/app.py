from flask import Flask, render_template, redirect, url_for,json, jsonify, request,session
import queries
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/profiles")
def profiles():
    roles = queries.get_all_roles()
    lst = queries.get_profile_names_and_photos()
    return render_template('profiles.html', roles=roles, lst=lst)


@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = queries.get_all_movies()
    return render_template('build_by_movie.html',movies_lst = movies_lst)


@app.route("/build_by_movie/<movie_id>")
def build_by_movie_role(movie_id):
    roles = queries.get_movie_roles(movie_id)
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({'movie_roles' : rolesArray })

@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():
    movies_lst = queries.get_all_movies()
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst)

@app.route("/search_profile_by_name", methods=["POST"])
def search_profile_by_name():
    name = request.form.get("name")
    return render_template("search_bu_name_results.html")

@app.route("/find_movie_by_key_words")
def find_movie_by_key_words():
    return render_template("find_movie_by_key_words.html")

@app.route('/movies_by_words', methods=["post"])
def movies_by_words():
    text = request.form.get(words);
    words = text.split(",");
    n = len(words);

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
