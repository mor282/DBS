import mysql.connector
from mysql.connector import errorcode

"""
connects to the database, execute the query and return an iterator.
keyword arguments:
query -- the query we want to execute
args -- additional arguments
"""

#set connection and return a cursor
def connect_to_db():

    # The Database login details
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': 'localhost',       #needed for running from home
        'database': 'DbMysql08',
        'port': 3305,              #needed for running from home (the tunnel port)
        'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    return cnx

#given connection, cursor, the name of the table and the values- inserts this line to this table
def insert_query(cnx, cur, table_name, values):
    try:
        cur.execute("INSERT INTO " + get_table_full_name(table_name) + " VALUES" +
                    get_table_values_tup(table_name), values)
        cnx.commit()
    except:
        cnx.rollback()
    return

#
def get_query(cur, query):
    try:
        cur.execute(query)
    except:
        print("error- couldn't get result of" + str(query))

    res = cur.fetchall()
    for x in res:
        print(x) #change to
    return

def get_table_full_name(table_name):
    name_dict = {
        "department": "department(role, department)",
        "locations": "locations(location_id, movie_id, country)",
        "movie_crew": "movie_crew(crew_id, profile_id, role, movie_id)",
        "movies": "movies(movie_id, title, budget, revenue, runtime, language,"
                  " poster_link, release_year, genre)",
        "profile": "profile(profile_id, name, gender, age, main_department, popularity, biography, photo_link)",
        "quotes": "quotes(quote_id, title, quote)"
    }
    return name_dict.get(table_name)

def get_table_values_tup(table_name):
    name_dict = {
        "department": "(%s, %s)",
        "locations": "(%s, %s, %s)",
        "movie_crew": "(%s, %s, %s, %s)",
        "movies": "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        "profile": "(%s, %s, %s, %s, %s, %s, %s, %s)",
        "quotes": "(%s, %s, %s)"
    }
    return name_dict.get(table_name)



def mf(cnx):
    cur = cnx.cursor(buffered=True)

    v1 = ("water boi", "money eaters")
    insert_query(cnx, cur, "department", v1)
    q2 = "select * from department"
    get_query(cur, q2)
    cur.close()
    cnx.close()

def tst():
    print(get_table_values_tup("profile"))

cnx = connect_to_db()
mf(cnx)
#tst()
