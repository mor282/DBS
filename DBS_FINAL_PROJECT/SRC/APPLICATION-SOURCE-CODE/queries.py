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
    query = ("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "
            "FROM profile, movie_crew "
            "WHERE movie_crew.profile_id = profile.profile_id AND "
            "movie_crew.movie_id = %s AND "
            "movie_crew.role = %s " )
    cur.execute(query,(movie_id,role))
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_countries():
    """connect to db, return list of all countries in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT DISTINCT country FROM locations order by country")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_all_movies():
    """connect to db, return list of all movies in our database"""

    cnx,cur = connect_to_db()       #get connection with db
    cur.execute("SELECT  title, movie_id FROM movies")
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
    cur.execute("SELECT DISTINCT genre FROM genres")   #sql query to return all genres
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
        cur.execute("SELECT name, photo_link, biography FROM profile, movie_crew, department WHERE profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role and department.role = %s and popularity >= %s ORDER BY %s LIMIT 100" , values)

    if not gender == "All" and role =="All":
        values = (gender, pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile WHERE gender = %s and popularity >= %s ORDER BY %s LIMIT 100" , values)

    if not gender =="All" and not role=="All":
        values = (gender, role, pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile, movie_crew, department WHERE profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role and gender = %s and department.role = %s and popularity >= %s ORDER BY %s LIMIT 100" , values)

    if gender=="All" and role=="All":
        values = (pop, orderby)
        cur.execute("SELECT name, photo_link, biography FROM profile WHERE popularity >= %s ORDER BY %s LIMIT 100" , values)

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

def get_main_department():
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT distinct main_department FROM profile")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_department():
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT distinct department FROM department")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_roles_of_department(depart):
    cnx,cur = connect_to_db()             #get connection with db
    values = (depart,)
    cur.execute("SELECT role FROM department WHERE department = %s ", values)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_languages():
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT distinct language FROM movies")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

def get_all(members,depart,agefrom,ageto,gender,pop,lang,country,genre,orderby):

    cnx,cur = connect_to_db()             #get connection with db
    lst=""
    if (members < '1' or agefrom > ageto or ageto < '0' or len(genre) == 0 or len(lang) == 0):
        cur.close()
        cnx.close()
        return lst,0

    list = []
    query = "SELECT DISTINCT profile.name, department.role, profile.biography, profile.popularity, profile.age, profile.photo_link, movies.title, genres.genre FROM profile, movie_crew, department, movies, locations, genres WHERE"

   # if (agefrom < '2' and ageto > '99') == False:
    #    query = query + " age > %s and age < %s and"
     #   list.append(int(agefrom))
      #  list.append(int(ageto))



    query = query + " popularity >= %s AND profile.profile_id = movie_crew.profile_id AND department.role = movie_crew.role AND movies.movie_id = movie_crew.movie_id AND movies.movie_id = locations.movie_id AND movies.movie_id = genres.movie_id ORDER BY %s LIMIT 10000"

    list.append(pop) #should be append(pop)
    list.append(orderby) #should be append(orderby)
    values = tuple(list)
    cur.execute(query,values)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst,len(lst)+1
