"""
This module contains all the app queries
"""
import  query_utilities


def get_countries():
    """connect to db, return list of all countries in our database"""

    cnx = query_utilities.connect_to_db()             #get connection with db
    cur = cnx.cursor(buffered=True)                   #define a cursor
    query = ("SELECT DISTINCT country, location_id"   #sql query to return all countries
            "FROM locations")
    cur.execute(query)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_movies():
    """connect to db, return list of all movies in our database"""

    cnx,cur = query_utilities.connect_to_db()             #get connection with db
    query = ("SELECT  title, movie_id"   #sql query to return all movies
            "FROM movies")
    cur.execute(query)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_roles():
    """connect to db, return list of all roles in our database"""

    cnx,cur = query_utilities.connect_to_db()             #get connection with db
    query = ("SELECT  DISTINCT role"   #sql query to return all movies
            "FROM department")
    cur.execute(query)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


def get_genre():
    """connect to db, return list of all genres in our database"""

    cnx,cur = query_utilities.connect_to_db()             #get connection with db
    query = ("SELECT DISTINCT genre"   #sql query to return all movies
            "FROM movies")
    cur.execute(query)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst
