from flask import Flask, render_template, redirect,json,jsonify, url_for, request
import queries

app = Flask(__name__)

#first landing page.
@app.route("/")
def home():
    """return home page - home.html"""
    return render_template('home.html')

#application index.
@app.route("/index")
def index():
    """return a index page to select a searching Feature"""

    return render_template('index.html')

#_________________________________________________________________________________________
#this section is associated to search profiles by Name, Gender, Profession and popularity.

@app.route("/search")
def search():
    lst = queries.get_department()
    languages = queries.get_languages()
    countries = queries.get_countries()
    genres = queries.get_genre()
    return render_template('regular_search.html',lst=lst, languages=languages, countries=countries,genres=genres)


@app.route("/search_results", methods=["POST"])
def search_results():
    depart = request.form.get("depart")
    agefrom = request.form.get("from")
    ageto = request.form.get("to")
    valid = (ageto >= agefrom)
    gender = request.form.get("gender")
    pop = request.form.get("pop")
    lang = request.form.getlist("lang")
    sizelang = len(lang)
    country = request.form.get("country")
    genre = request.form.getlist("genre")
    sizegenre = len(genre)
    orderby = request.form.get("orderby")
    results,length = queries.get_all(depart,agefrom,ageto,gender,pop,lang,country,genre,orderby)
    return render_template('search_res.html', lang=lang, sizelang=sizelang, valid=valid, genre=genre, sizegenre=sizegenre, results=results, length=length, orderby=orderby)


#Search crew profiles by Name or by gender,Profession and popularity.
@app.route("/profiles")
def profiles():
    """return a profiles page with profile list and search options """

    #get list of all Professions in our db to use in select-dropdown-box.
    roles = queries.get_all_roles()

    #get the list of tuples of all profiles in our db, each tuple include all of the profiles data.
    lst = queries.get_profile_names_and_photos()

    #get a list of the roles existing in our db who have a description, return the role and the description
    lst2 = queries.get_roles_descriptions()
    return render_template('profiles.html', roles=roles, lst=lst, lst2=lst2)


#get the users input from @app.route("/profiles") when Choose to search by Name.
@app.route("/search_profile_by_name", methods=["POST"])
def search_profile_by_name():
    """return the profiles search results page"""

    #get the name from the form input @app.route("/profiles")
    name = request.form.get("name")

    #get list of tuples of relevant profiles with Name = name, And the length of the list.
    lst,size = queries.get_profile_by_name(name)

    return render_template("search_bu_name_results.html",lst=lst,size=size)


#get the users input from @app.route("/profiles") when Choose to search by gender,Profession and popularity.
@app.route("/profiles_res",methods=["POST"])
def profiles_res():
    """return the profiles search results page"""

    #get all users inputs from the form @app.route("/profiles")
    role = request.form.get("role")
    gender = request.form.get("gender")
    pop = request.form.get("pop")
    orderby = request.form.get("orderby")

    #get list of tuples of relevant profiles with Name = name, And the length of the list.
    lst2,size2 = queries.get_profile_by_search(role,gender,pop,orderby)
    return render_template('profiles_res.html', lst2=lst2, size2=size2)

#_________________________________________________________________________________________
# this section is associated to search profiles by movies

#Search crew profiles by The movies they worked at.
@app.route("/build_by_movie")
def build_by_movie():
    """return a Searching page"""

    #get list of tuples of all movies in our db to use in select-dropdown-box.
    movies_lst = queries.get_all_movies()
    return render_template('build_by_movie.html', movies_lst = movies_lst)


#fetched by @app.route("/build_by_movie") to provide Professions list to use in a second select-dropdown-box.
@app.route("/build_by_movie/<movie_id>" ,methods=["POST"])
def build_by_movie_role(movie_id):
    """return a json object contains all Professions associated with movie_id

        Keyword arguments:
        movie_id -- the movie_id of the selected movie from the form @app.route("/build_by_movie")
    """

    #get list of tuples of all roles in our db that associated with movie_id to use in select-dropdown-box.
    roles = queries.get_movie_roles(movie_id)

    #insert all roles in the role list into a list of tuples to adjust it to json object.
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({ 'movie_roles' : rolesArray })


#get the users input from @app.route("/build_by_movie") and render the search results page.
@app.route("/build_by_movie_results", methods=["POST"])
def build_by_movie_results():

    #get list of tuples of all movies in our db to use in select-dropdown-box.
    movies_lst = queries.get_all_movies()

    #get all users inputs from the form @app.route("/build_by_movie").
    movie_id = request.form.get("movie_id")
    role = request.form.get("role")

    #get list of tuples of relevant profiles associated to the selected movie and Profession.
    res =  queries.get_profiles_by_role_and_movie(role,movie_id)
    return render_template('build_by_movie_results.html',res = res,movies_lst = movies_lst)

#__________________________________________________________________________________________________
# this section is associated to search profiles by countries

#Search crew profiles by The countries they worked at.
@app.route("/build_by_country")
def build_by_country():
    """return a Searching page"""

    #get list of tuples of all countries in our db to use in select-dropdown-box.
    country_lst = queries.get_countries()
    return render_template('build_by_country.html', country_lst = country_lst)


#fetched by @app.route("/build_by_movie") to provide Professions list to use in a second select-dropdown-box.
@app.route("/build_by_country/<country>", methods=["POST"])
def build_by_country_role(country):
    """return a json object contains all Professions associated with country

        Keyword arguments:
        country -- the selected country from the form @app.route("/build_by_country")
    """
    #get list of tuples of all roles in our db that associated with country to use in select-dropdown-box.
    roles = queries.get_country_roles(country)

    #insert all roles in the role list into a list of tuples to adjust it to json object.
    rolesArray=[]
    for row in roles:
        roleObj ={'id':row[0], 'name': row[0] }
        rolesArray.append(roleObj)
    return jsonify({'country_roles' : rolesArray })


#get the users input from @app.route("/build_by_movie") and render the search results page.
@app.route("/build_by_country_results", methods=["POST"])
def build_by_country_results():

    #get list of tuples of all movies in our db to use in select-dropdown-box.
    country_lst = queries.get_countries()

    #get all users inputs from the form @app.route("/build_by_country").
    country = request.form.get("country")
    role = request.form.get("role")

    #get list of tuples of relevant profiles associated to the selected country and Profession.
    res =  queries.get_profiles_by_role_and_counrty(role,country)
    return render_template('build_by_country_results.html',res = res,country_lst = country_lst)


#__________________________________________________________________________________________________
# this section is associated to text-query to find movies by Key words contained in their overview

#renders a search page with input form to search movies by key words.
@app.route("/find_movie_by_key_words")
def find_movie_by_key_words():
    """return a search page"""
    return render_template("find_movie_by_key_words.html")

#get the user's input from @app.route("/find_movie_by_key_words") and render the search results page.
@app.route('/movies_by_words', methods=["post"])
def movies_by_words():

    #get user's input from @app.route("/find_movie_by_key_words")
    text = request.form.get('words');

    #process the users input to a more comfortable object
    words = text.split(",");

    #validate user's input.
    for word in words :
        if(not word.isalpha()):
             #if the user's input is invalid open new search page with alert message.
            return render_template("movies_by_words_invalid.html")
    #if the user's input is valid, get list of tuples of relevant movies.
    res,size = queries.get_movies_by_words(words)
    return render_template("movies_by_words.html", res = res, size=size)


#get called from @app.route('/movies_by_words') to show the crew of certain movie.
@app.route('/movie_crew',methods=["POST"])
def movie_crew():
    """render a page with a list of a Choosen movie crew memberes """

    #get the choosen movie's movie_id and title from the form button @app.route('/movies_by_words')
    movie_id = request.form.get('movie_id')
    title = request.form.get('movie_title')

    #get list of tuples of relevant all profiles.
    res =  queries.get_movie_crew(movie_id)
    return render_template("movie_crew.html", res = res,title=title)

#show the percentage of male and female crew members in films
@app.route("/diversity_by_movie")
def build_diversity():
    movies_lst = queries.get_female_diversity_movies_lst()
    return render_template('diversity_by_movie.html', movies_lst = movies_lst)


if __name__ == '__main__':
    app.run(debug = True) #host = '0.0.0.0', port = 40042, debug =False
