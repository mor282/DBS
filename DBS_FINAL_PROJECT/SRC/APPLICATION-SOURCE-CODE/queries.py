"""
This module contains all the app queries
"""

"""get all countries in our database"""
def get_countries():
    return ("SELECT DISTINCT country"
            "FROM locations")

"""get all genres in our database"""
def get_genre():
    return ("SELECT DISTINCT genre"
            "FROM movies")
