"""
This module contains all the app queries
"""
import mysql.connector
from mysql.connector import errorcode

def connect_to_db():
    """
    connects to the database, execute the query and return cnx.

    cnx is a connection object
    """

    # The Database login details
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': '127.0.0.1',                    #use 'localhost' or '127.0.0.1' if running from home
        'database': 'DbMysql08',
        'port': 3305,                           #use your forwarding port if running from home
        'raise_on_warnings': True,
    }

    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cur = cnx.cursor(buffered = True)
    return cnx,cur


def get_profiles_by_role_and_movie(role,movie_id):
    """
    return an iterator of profiles.

    keyword arguments:
    role -- the role we are looking
    movie -- the
    """
    cnx,cur = connect_to_db()
    cur.execute("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "
                "FROM profile, movie_crew "
                "WHERE movie_crew.profile_id = profile.profile_id AND "
                "movie_crew.movie_id = " + str(movie_id) + " AND "
                "movie_crew.role LIKE '%" + role + "%'")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_countries():
    """connect to db, return list of all countries in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT DISTINCT country FROM locations")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_all_movies():
    """connect to db, return list of all movies in our database"""

    cnx,cur = connect_to_db()       #get connection with db
    cur.execute("SELECT  movie_id, title FROM movies")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_movie(movie_id):
    """connect to db, return list of all movies in our database"""

    cnx,cur = connect_to_db()       #get connection with db
    cur.execute("SELECT  title, movie_id FROM movies WHERE movie_id =" + movie_id)
    lst = cur.fetchone()
    cur.close()
    cnx.close()
    return lst

def get_all_roles():
    """connect to db, return list of all roles in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT  DISTINCT role FROM movie_crew")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_movie_roles(movie_id):
    """connect to db, return list of all roles in specific movie"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT  DISTINCT role FROM movie_crew WHERE movie_id = " + movie_id )
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_genre():
    """connect to db, return list of all genres in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT DISTINCT genre FROM movies")   #sql query to return all genres
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_profile_names_and_photos():

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT name, photo_link, biography FROM profile limit 100")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_profile_by_search(role,gender,pop,orderby):

    cnx,cur = connect_to_db()             #get connection with db

    orderby = " ORDER BY " + orderby
    query = "popularity > " + pop

    if gender =="All" and not role == "All":
        values = (role, pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile, movie_crew, department WHERE profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role and department.role = %s and popularity > %s ORDER BY %s LIMIT 100" , values)

    if not gender == "All" and role =="All":
        values = (gender, pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile WHERE gender = %s and popularity > %s ORDER BY %s LIMIT 100" , values)

    if not gender =="All" and not role=="All":
        values = (gender, role, pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile, movie_crew, department WHERE profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role and gender = %s and department.role = %s and popularity > %s ORDER BY %s LIMIT 100" , values)

    if gender=="All" and role=="All":
        values = (pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile WHERE popularity > %s ORDER BY %s LIMIT 100" , values)

    #cur.execute("SELECT name, photo_link, biography FROM profile WHERE " + query + orderby + " limit 100 ")
    lst = cur.fetchall()
    size = len(lst)
    cur.close()
    cnx.close()
    return lst,size

def get_profile_by_name(name):

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT name, photo_link, biography FROM profile WHERE name LIKE '%"+name+"%' limit 100")
    lst = cur.fetchall()
    size = len(lst)
    cur.close()
    cnx.close()
    return lst,size


def get_country_roles(country):
    """
    retrun list all roles available in country names

    keyword arguments
    country -- the country we look at
    """
    cnx,cur = connect_to_db()
    cur.execute("SELECT  DISTINCT role FROM locations, movie_crew  "
    "WHERE locations.country LIKE '%" + country + "%' AND locations.movie_id = movie_crew.movie_id")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_profiles_by_role_and_counrty(role,country):
    """
    return an iterator of profiles.

    keyword arguments:
    role -- the role we are looking
    country -- the coutry we look roles at
    """
    cnx,cur = connect_to_db()
    cur.execute("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "+
                "FROM profile, movie_crew, locations "
                "WHERE movie_crew.profile_id = profile.profile_id AND "
                "movie_crew.movie_id = locations.movie_id AND "
                "locations.country LIKE '%" + country + "%' AND "
                "movie_crew.role LIKE '%" + role + "%'")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_main_department():
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT distinct main_department FROM profile WHERE main_department is not null")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_movies_by_words(words):
    """
    return a list of movies that includes the given words in their overview.

    keyword arguments:
    words -- list of words given by the user.
    """
    cnx,cur = connect_to_db()
    text = "'";
    for word in words:
        text += "+"+word+" "
    text += "'"
    cur.execute("SELECT * FROM movies "
                "Where match(overview) against("+text+" IN BOOLEAN MODE) LIMIT 100 ")
    lst = cur.fetchall()
    size = len(lst)
    cur.close()
    cnx.close()
    return lst,size

def get_movie_crew(movie_id):
    cnx,cur = connect_to_db()
    cur.execute("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "
                "FROM profile, movie_crew "
                "WHERE movie_crew.profile_id = profile.profile_id AND "
                'movie_crew.movie_id = ' + str(movie_id))
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_female_diversity_movies_lst():
    """
    returnd female ratio in movie crew for all movies  or NULL if data is missing.


    """
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT movies.movie_id, movies.title as title, COUNT(IF(profile.gender='1',1,NULL)) / NULLIF(COUNT(IF(profile.gender='1',1,NULL))+COUNT(IF(profile.gender='2',1,NULL)), 0) as ratio"
    + " FROM movie_crew, profile, movies WHERE profile.profile_id = movie_crew.profile_id AND movie_crew.movie_id = movies.movie_id "
    + " GROUP BY movies.movie_id HAVING ratio >= 0 ")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst
