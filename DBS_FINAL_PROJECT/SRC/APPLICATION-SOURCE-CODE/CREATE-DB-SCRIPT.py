import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime
import queries


def connect_to_db():
    """
    connects to the database, execute the query and return cnx.

    cnx is a connection object
    """

    # The Database login details
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': '127.0.0.1',       #use 'localhost' or '127.0.0.1' if running from home
        'database': 'DbMysql08',
        'port': 3305,                           #use your forward if running from home
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

    return cnx.cursor(buffered=True)



def Insert_Query(query,values):
    """
    make a connection to the db, execute an insert query return success

    keyword arguments:
        query -- the query to execute
        values -- values for the query

"""
    cnx = connect_to_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute(query)
    except :
        cnx.rollback()
        print("Error")

    cnx.commit()
    cur.close()
    cnx.close()
    return
