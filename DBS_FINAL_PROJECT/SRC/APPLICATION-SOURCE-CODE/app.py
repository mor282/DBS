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

@app.route("/search")
def search():
    lst = queries.get_department()
    languages = queries.get_languages()
    countries = queries.get_countries()
    genres = queries.get_genre()
    return render_template('regular_search.html',lst=lst, languages=languages, countries=countries,genres=genres)

@app.route("/search_results", methods=["POST"])
def search_results():
    members = request.form.get("number")
    depart = request.form.get("depart")
    agefrom = request.form.get("from")
    ageto = request.form.get("to")
    valid = ageto >= agefrom
    if ageto < '0':
        valid = False
    gender = request.form.get("gender")
    pop = request.form.get("pop")
    lang = request.form.getlist("lang")
    sizelang = len(lang)
    country = request.form.get("country")
    genre = request.form.getlist("genre")
    sizegenre = len(genre)
    orderby = request.form.get("orderby")
    results,length = queries.get_all(members,depart,agefrom,ageto,gender,pop,lang,country,genre,orderby)
    return render_template('search_res.html', members=members, lang=lang, sizelang=sizelang, valid=valid, genre=genre, sizegenre=sizegenre, results=results, length=length)

@app.route("/profiles")
def profiles():
    roles = queries.get_all_roles()
    lst = queries.get_profile_names_and_photos()
    return render_template('profiles.html', roles=roles, lst=lst)

@app.route("/profiles_results",methods=["POST"])
def profiles_results():
    role = request.form.get("role")
    gender = request.form.get("gender")
    pop = request.form.get("pop")
    orderby = request.form.get("orderby")
    lst2,size2 = queries.get_profile_by_search(role,gender,pop,orderby)
    return render_template('profiles_res.html', lst2=lst2, size2=size2)

@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = queries.get_all_movies()
    roles = queries.get_all_roles()
    return render_template('build_by_movie.html',movies_lst = movies_lst, roles= roles)

@app.route("/build_by_movie_role", methods = ["POST"])
def build_by_movie_role():
    movie_id = request.form.get("movie_id")
    movie = queries.get_movie(movie_id)
    roles = queries.get_movie_roles(movie_id)
    return render_template('build_by_movie_role.html',movie = movie, roles= roles)



@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():
    movies_lst = queries.get_all_movies()
    roles = queries.get_all_roles()
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    for r in res:
        print(r[1])
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst, roles= roles)

@app.route("/search_profile_by_name", methods=["POST"])
def search_profile_by_name():
    name = request.form.get("name")
    lst,size = queries.get_profile_by_name(name)
    return render_template("search_bu_name_results.html",lst=lst,size=size)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
