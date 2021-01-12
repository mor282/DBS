<<<<<<< Updated upstream
from flask import Flask, render_template, redirect, url_for, request,session
=======
from flask import Flask, render_template, redirect, url_for,json, jsonify, request,session
>>>>>>> Stashed changes
import queries
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')
<<<<<<< Updated upstream
    
@app.route("/profiles")
def profiles():
    roles = queries.get_all_roles()
    lst = queries.get_profile_names_and_photos()
    return render_template('profiles.html', roles=roles, lst=lst)
=======
>>>>>>> Stashed changes

@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = queries.get_all_movies()
<<<<<<< Updated upstream
    roles = queries.get_all_roles()
    return render_template('build_by_movie.html',movies_lst = movies_lst, roles= roles)

@app.route("/build_by_movie_role", methods = ["POST"])
def build_by_movie_role():
    movie_id = request.form.get("movie_id")
    movie = queries.get_movie(movie_id)
    roles = queries.get_movie_roles(movie_id)
    return render_template('build_by_movie_role.html',movie = movie, roles= roles)


=======
    return render_template('build_by_movie.html', movies_lst = movies_lst)


@app.route("/build_by_movie/<movie_id>")
def build_by_movie_role(movie_id):
    roles = queries.get_movie_roles(movie_id)
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({'movie_roles' : rolesArray })
>>>>>>> Stashed changes

@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():
    movies_lst = queries.get_all_movies()
<<<<<<< Updated upstream
    roles = queries.get_all_roles()
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    for r in res:
        print(r[1])
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst, roles= roles)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst)

if __name__ == '__main__':
    app.run(debug = True)
>>>>>>> Stashed changes
