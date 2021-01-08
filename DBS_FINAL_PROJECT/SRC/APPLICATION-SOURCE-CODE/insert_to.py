import mysql.connector
from mysql.connector import errorcode
import requests

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
        print(errorcode)
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
        print(x)  #change to something else
    return


def init_lang_dict():
    lang_api = requests.get(
        "https://api.themoviedb.org/3/configuration/languages?api_key=a48ba1f202cb5cd5e619e2f5e041b34a")
    txt = lang_api.text
    txt = txt.split('{')  # get a string of all the rows in that page
    entry_amt = len(txt)  # count the rows in this page
    for i in range(2, entry_amt):
        curr_row = txt[i][:-2]
        l_iso = (curr_row.replace('"', '').split("iso_639_1:")[1].split(',')[0])
        l_english = (curr_row.replace('"', '').split(",english_name:")[1].split(',')[0])
        # l_english=l_english.encode('utf-8')
        lang_dict[l_iso] = l_english
    return

def get_table_full_name(table_name):
    return name_dict.get(table_name)

def get_table_values_tup(table_name):
    return values_tup_dict.get(table_name)

def get_genre_name(m_genre):
    y=m_genre.split(",")
    s=len(y)
    for i in range(s):
        y[i]=genre_dict.get(y[i])
    y=tuple(y)
    return y

# payload = "client_id%0A=###################&redirect_uri=#################%2F&client_secret=##############&code={}&grant_type=authorization_code&undefined=".format(code)
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache"
#     }

#==========================global dictionaries===================================================
name_dict = {
    "department": "department(role, department)",
    "locations": "locations(location_id, movie_id, country)",
    "movie_crew": "movie_crew(crew_id, profile_id, role, movie_id)",
    "movies": "movies(movie_id, title, budget, revenue, runtime, language,"
              " poster_link, release_year, genre, overview)",
    "profile": "profile(profile_id, name, gender, age, main_department, popularity, biography, photo_link)",
    "quotes": "quotes(quote_id, title, quote)"
}

values_tup_dict = {
    "department": "(%s, %s)",
    "locations": "(%s, %s, %s)",
    "movie_crew": "(%s, %s, %s, %s)",
    "movies": "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "profile": "(%s, %s, %s, %s, %s, %s, %s, %s)",
    "quotes": "(%s, %s, %s)"
}

genre_dict = {"28": "Action", "12": "Adventure", "16": "Animation", "35": "Comedy",
              "80": "Crime", "99": "Documentary", "18": "Drama", "10751": "Family",
              "14": "Fantasy", "36": "History", "27": "Horror", "10402": "Music",
              "9648": "Mystery", "10749": "Romance", "878": "Science Fiction",
              "10770": "TV Movie", "53": "Thriller", "10752": "War", "37": "Western"}

lang_dict = {}
#================================end of global dictionaries============================================


def init_movies(cnx, cur):

    m_first_page_url = "https://api.themoviedb.org/3/discover/movie?api_key=a48ba1f202cb5cd5e619e2" \
          "f5e041b34a&sort_by=popularity.desc&page=1&release_date.lte=2020-12-31"
    m_first_page_response = requests.get(m_first_page_url)
    m_first_page_txt = m_first_page_response.text

    m_page_amt = int(m_first_page_txt.replace('"', '').split("total_pages:")[1].split(",")[0])

    for k in range(1, m_page_amt + 1):

        m_curr_url = "https://api.themoviedb.org/3/discover/movie?api_key=a48ba1f202cb5cd5e619e2" \
              "f5e041b34a&sort_by=revenue.desc&page={}&release_date.lte=2020-12-31".format(str(k))
        m_response = requests.get(m_curr_url)
        m_txt = m_response.text  # get a string of all the rows in that page
        m_entry_amt = len(m_txt.split('{'))  # count the rows in this page
        for i in range(2, m_entry_amt):
            m_curr_row = m_txt.split('{')[i][:-2].replace('"', '')

            m_id = (m_curr_row.split(",id:")[1].split(',')[0])

            # movies related data

            # getting the rest of data from another place
            m_url2 = "https://api.themoviedb.org/3/movie/{}?api_key=a48ba1f202cb5cd5e619e2f5e041b34a".format(m_id)
            m_response2 = requests.get(m_url2)
            m_txt2 = m_response2.text

            m_title = (m_curr_row.split(",title:")[1].split(',')[0])

            m_revenue = (m_txt2.replace('"', '').split(",revenue:")[1].split(',')[0])

            m_budget = (m_txt2.replace('"', '').split(",budget:")[1].split(',')[0])

            m_runtime = (m_txt2.replace('"', '').split(",runtime:")[1].split(',')[0])

            m_language = (m_curr_row.split(",original_language:")[1].split(',')[0])
            m_language = lang_dict.get(m_language)

            m_poster_link = "https://image.tmdb.org/t/p/original/" + (m_curr_row.split(",poster_path:")[1].split(',')[0])

            m_release_year = (m_curr_row.split(",release_date:")[1].split('-')[0])

            m_genre = (m_curr_row.split(",genre_ids:[")[1].split(']')[0])
            m_genre = get_genre_name(m_genre)

            m_overview = (m_curr_row.split(",overview:")[1]).split(',popularity:')[0]

            # will be changed to movie insert
            print(("id {} , tit {} , bud {} , rev {} , run {} , "
                   "lan {} , pos {} , rel {} , gen {} , ove {}").format(
                                                m_id, m_title, m_budget, m_revenue, m_runtime, m_language,
                                                m_poster_link, m_release_year, m_genre, m_overview))
            insert_query(cnx, cur, "movies", (m_id, m_title, m_budget, m_revenue, m_runtime, m_language,
                                                m_poster_link, m_release_year, m_genre, m_overview))
            # locations related data
            l_url = "https://api.themoviedb.org/3/movie/{}?api_key=a48ba1f202cb5cd5e619e2f5e041b34a".format(m_id)
            l_response = requests.get(l_url)
            l_txt = l_response.text
            l_curr_row = l_txt.replace('"', '')

            l_countries = l_curr_row.split(",production_countries:[")[1].split(']')[0]
            l_country_amt = len(l_countries.split('{')) - 1
            for j in range(1, l_country_amt + 1):
                l_curr_country = l_countries.split("{")[j].split(",name:")[1].split("}")[0]
                # will be changed to locations insert
                print(m_id, l_curr_country)


        m_response.close()

def main():
    cnx = connect_to_db()
    cur = cnx.cursor(buffered=True)

    init_lang_dict()
    init_movies(cnx, cur)

    cur.close()
    cnx.close()

main()


