from flask import Flask, render_template, redirect,json,jsonify, url_for, request,session
import queries
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

# this section is associated to search profiles by Name, Gender, Profession and popularity
@app.route("/profiles")
def profiles():
    roles = queries.get_all_roles()
    lst = queries.get_profile_names_and_photos()
    return render_template('profiles.html', roles=roles, lst=lst)

@app.route("/search_profile_by_name", methods=["POST"])
def search_profile_by_name():
    name = request.form.get("name")
    lst,size = queries.get_profile_by_name(name)
    return render_template("search_bu_name_results.html",lst=lst,size=size)

@app.route("/profiles_res",methods=["POST"])
def profiles_res():
    role = request.form.get("role")
    gender = request.form.get("gender")
    pop = request.form.get("pop")
    orderby = request.form.get("orderby")
    lst2,size2 = queries.get_profile_by_search(role,gender,pop,orderby)
    return render_template('profiles_res.html', lst2=lst2, size2=size2)

# this section is associated to search profiles by movies
@app.route("/build_by_movie")
def build_by_movie():
    movies_lst = queries.get_all_movies()
    return render_template('build_by_movie.html', movies_lst = movies_lst)

@app.route("/build_by_movie/<movie_id>" , methods=["POST"])
def build_by_movie_role(movie_id):
    roles = queries.get_movie_roles(movie_id)
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({ 'movie_roles' : rolesArray })

@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():
    movies_lst = queries.get_all_movies()
    roles = queries.get_all_roles()
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst)

# this section is associated to search profiles by countries
@app.route("/build_by_country")
def build_by_country():
    country_lst = queries.get_countries()
    return render_template('build_by_country.html', country_lst = country_lst)

@app.route("/build_by_country/<country>", methods=["POST"])
def build_by_country_role(country):
    roles = queries.get_country_roles(country)
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({'country_roles' : rolesArray })

@app.route("/build_by_country_results", methods=["POST"])
def build_by_country_results():
    country_lst = queries.get_countries()
    country = request.form.get("country")
    role = request.form.get("role")
    res =  queries.get_profiles_by_role_and_counrty(role,country)
    return render_template('build_by_country_results.html',res = res,country_lst = country_lst)

# this section is associated to text-query to find movies by Key words in their overview
@app.route("/find_movie_by_key_words")
def find_movie_by_key_words():
    return render_template("find_movie_by_key_words.html")

@app.route('/movies_by_words', methods=["post"])
def movies_by_words():
    text = request.form.get('words');
    words = text.split(",");
    n = len(words);
    for word in words :
        if(not word.isalpha()):
            return render_template("movies_by_words_invalid.html")
    res,size = queries.get_movies_by_words(words)
    return render_template("movies_by_words.html", res = res, size=size)

@app.route('/movie_crew',methods=["POST"])
def movie_crew():
    movie_id = request.form.get('movie_id')
    movie = queries.get_movie(movie_id=movie_id)
    title = movie[0]
    res =  queries.get_movie_crew(movie_id)
    return render_template("movie_crew.html", res = res,title=title)


if __name__ == '__main__':
    app.run(debug = True)
