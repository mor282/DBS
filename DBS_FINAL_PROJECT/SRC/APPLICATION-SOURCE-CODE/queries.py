"""
This module contains all the app queries
"""
import mysql.connector
from mysql.connector import errorcode


#db connection--------------------------------------------------------------------------------------------

def connect_to_db():
    """
    connects to the database, execute the query and return cnx.

    cnx is a connection object
    """

    # The Database login details
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': '127.0.0.1',                    #use 'host' :'mysqlsrv1.cs.tau.ac.il'
        'database': 'DbMysql08',
        'port': 3305,                           #'port': 3306
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

#-------------------------------------------------------------------------------------------------------------
#getters______________________________________________________________________________________________________

def get_countries():
    """connect to db, return list of all countries in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT DISTINCT country FROM locations order by country")
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


def get_all_movies():
    """connect to db, return list of all movies in our database"""

    cnx,cur = connect_to_db()       #get connection with db
    cur.execute("SELECT  movie_id, title FROM movies")
    lst = cur.fetchall()
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

def get_roles_descriptions():
    """connect to db, return list of all roles in our database"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("select distinct role, job_description from department where job_description is not null ")
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
    return lst,len(lst)


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


def get_languages():
    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT distinct language FROM movies")
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

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#profiles by country-------------------------------------------------------------------------------------------

#q1
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

#q2
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
                "WHERE locations.country LIKE '%" + country + "%' AND movie_crew.role LIKE '%" + role + "%' AND "
                "movie_crew.profile_id = profile.profile_id AND "
                "movie_crew.movie_id = locations.movie_id")

    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#profiles by movies-----------------------------------------------------------------------------------------

def get_movie_roles(movie_id):
    """connect to db, return list of all roles in specific movie"""

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT  DISTINCT role FROM movie_crew WHERE movie_id = " + movie_id )
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst


#q3
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
                "WHERE movie_crew.movie_id = " + str(movie_id) + " AND "+
                "movie_crew.role LIKE '%" + role + "%' AND "
                "movie_crew.profile_id = profile.profile_id"
                )
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

#-------------------------------------------------------------------------------------------------------------------------------------------------
#gender diversity---------------------------------------------------------------------------------------------------------------------------------

#q4
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


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#profiles by search-----------------------------------------------------------------------------------------

def get_profile_by_name(name):

    cnx,cur = connect_to_db()             #get connection with db
    cur.execute("SELECT name, photo_link, biography, age, popularity, main_department FROM profile WHERE name LIKE '%"+name+"%' limit 100")
    lst = cur.fetchall()
    size = len(lst)
    cur.close()
    cnx.close()
    return lst,size


def get_roles_of_department(depart):
    cnx,cur = connect_to_db()             #get connection with db
    values = (depart,)
    cur.execute("SELECT role FROM department WHERE department = %s ", values)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

#q5
def get_profile_by_search(role,gender,pop,orderby):

    cnx,cur = connect_to_db()             #get connection with db

    query = ""

    if gender =="All" and not role == "All":
        values = (role, pop)
        query = "SELECT DISTINCT name, photo_link, biography, age, popularity, main_department FROM profile, movie_crew, department WHERE department.role = %s and popularity >= %s and profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role"


    if not gender == "All" and role =="All":
        values = (gender, pop)
        query = "SELECT DISTINCT name, photo_link, biography, age, popularity, main_department FROM profile WHERE gender = %s and popularity >= %s"

    if not gender =="All" and not role=="All":
        values = (gender, role, pop)
        query = "SELECT DISTINCT name, photo_link, biography, age, popularity, main_department FROM profile, movie_crew, department WHERE gender = %s and department.role = %s and popularity >= %s and profile.profile_id = movie_crew.profile_id and movie_crew.role = department.role"

    if gender=="All" and role=="All":
        values = (pop,)
        query = "SELECT DISTINCT name, photo_link, biography, age, popularity, main_department FROM profile WHERE popularity >= %s"

    query = query + " and (age is null or age < 99 or age = 99)"
    if (orderby == '1'):
        query = query + " ORDER by popularity DESC LIMIT 100"
    if (orderby == '2'):
         query = query + " ORDER by name LIMIT 100"
    if (orderby == '3'):
         query = query + " ORDER by age DESC LIMIT 100"

    cur.execute(query,values)
    lst = cur.fetchall()
    size = len(lst)
    cur.close()
    cnx.close()
    return lst,size


#text-query - find movie by keywords------------------------------------------------------------------
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
#q6
def get_movie_crew(movie_id):
    cnx,cur = connect_to_db()
    cur.execute("SELECT DISTINCT profile.profile_id, name, gender, age, main_department, popularity, biography, photo_link "
                "FROM profile, movie_crew "
                "WHERE movie_crew.movie_id =" + str(movie_id) + " AND "
                "movie_crew.profile_id = profile.profile_id"
                )
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst

#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------

#search profile by all parameters--------------------------------------------------------------------------------------------------------

#q7
def get_all(depart,agefrom,ageto,gender,pop,lang,country,genre,orderby):

    cnx,cur = connect_to_db()             #get connection with db
    lst=""
    if (agefrom > ageto or len(genre) == 0 or len(lang) == 0):
        cur.close()
        cnx.close()
        return lst,-1

    list = []
    query = "SELECT DISTINCT profile.name, profile.biography, profile.popularity, profile.age, profile.photo_link, profile.main_department FROM profile, movie_crew, department, movies, locations, genres WHERE"

    if agefrom > '1' or ageto < '99':
        query = query + " age > %s and age < %s and"
        list.append(agefrom)
        list.append(ageto)

    else:
         query = query + " (age is null or age < 99 or age = 99) and"

    if depart != 'all':
        query = query + " department = %s and "
        list.append(depart)

    if gender != 'both':
        query = query + " gender = %s and"
        list.append(gender)

    if lang[0] != 'all' and len(lang) < 14:
        query = query + " ("
        for l in lang[:-1]:
            query = query + "language = %s or "
            list.append(l)
        query = query + "language = %s ) and"
        list.append(lang[-1])

    if country != 'all':
        query = query + " country = %s and"
        list.append(country)

    if genre[0] != 'all' and len(genre) < 19:
        query = query + " ("
        for g in genre[:-1]:
            query = query + "genre = %s or "
            list.append(g)
        query = query + "genre = %s ) and"
        list.append(genre[-1])

    query = query + " popularity >= %s AND profile.profile_id = movie_crew.profile_id AND department.role = movie_crew.role AND movies.movie_id = movie_crew.movie_id AND movies.movie_id = locations.movie_id AND movies.movie_id = genres.movie_id"

    list.append(pop)

    if (orderby == '1'):
        query = query + " ORDER by popularity DESC LIMIT 100"
    if (orderby == '2'):
        query = query + " ORDER by name LIMIT 100"
    if (orderby == '3'):
        query = query + " ORDER by age DESC LIMIT 100"

    values = tuple(list)
    cur.execute(query,values)
    lst = cur.fetchall()
    cur.close()
    cnx.close()
    return lst,len(lst)
