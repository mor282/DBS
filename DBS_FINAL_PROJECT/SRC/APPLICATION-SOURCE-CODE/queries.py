"""
This module contains all the app queries
"""
import  query_utilities

"""get all countries in our database"""
def get_countries():
    """connect to db, return list of all countries in our database"""
    cnx = query_utilities.connect_to_db()
    cur = cnx.cursor(buffered=True)
    query = ("SELECT DISTINCT country, location_id"
            "FROM locations") 


"""get all genres in our database"""
def get_genre():
    return ("SELECT DISTINCT genre"
            "FROM movies")
