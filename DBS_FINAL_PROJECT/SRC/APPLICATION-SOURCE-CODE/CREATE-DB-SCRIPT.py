import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime
import queries

def connect_to_db():
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': 'mysqlsrv1.cs.tau.ac.il',
        'database': 'DbMysql08',
        'port': 3306,
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

    cur = cnx.cursor(buffered=True)
    try:
        cur.execute()
        cnx.commit()
    except:
        cnx.rollback()


    cursor.close()
    cnx.close()