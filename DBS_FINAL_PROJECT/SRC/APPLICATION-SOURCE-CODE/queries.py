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

    cur.execute("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "+
                "FROM profile, movie_crew "
                "WHERE movie_crew.profile_id = profile.profile_id AND "
                "movie_crew.movie_id = " + movie_id + " AND "
                "movie_crew.role LIKE '%" + role + "%'")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_countries():
    """connect to db, return list of all countries in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT DISTINCT country, location_id FROM locations")
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
    cur.execute("SELECT movie_id, title FROM movies WHERE movie_id =" + movie_id)
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
    """
    connect to db, return list of all roles in specific movie

    keywords arguments:
    movie_id -- the uniqe id of the movie we want
    """

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT  DISTINCT role FROM movie_crew WHERE movie_id = " + str(movie_id) )
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
    cur.execute("SELECT name, photo_link FROM profile limit 100")
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst
