import mysql.connector
from mysql.connector import errorcode
import requests

"""
connects to the database, execute the query and return an iterator.
keyword arguments:
query -- the query we want to execute
args -- additional arguments
"""


# set connection and return a cursor
def connect_to_db():
    # The Database login details
    config = {
        'user': 'DbMysql08',
        'password': 'DbMysql08',
        'host': 'localhost',  # needed for running from home
        'database': 'DbMysql08',
        'port': 3305,  # needed for running from home (the tunnel port)
        'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    return cnx


# given connection, cursor, the name of the table and the values- inserts this line to this table
def insert_query(cnx, cur, table_name, values):
    try:
        cur.execute("INSERT INTO " + name_dict.get(table_name) + " VALUES" +
                    values_tup_dict.get(table_name), values)
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
        print(x)  # change to something else
    return


def init_role_dict():
    prod = "https://thefilmproduction.wordpress.com/production-department/"
    camera = "https://thefilmproduction.wordpress.com/camera-department/"
    sound = "https://thefilmproduction.wordpress.com/production-sound-department/"

    # build the dict
    get_crew()
    get_g2(prod)
    get_g2(camera)
    get_g2(sound)
    get_light()
    get_dir()
    get_art()
    get_style()


def rid_of_signs(desc):
    desc1 = desc.replace('&#8221;', '"')
    desc1 = desc1.replace('&#8220;', '"')
    desc1 = desc1.replace('&#8212;', '--')
    desc1 = desc1.replace('&#8217;', '`')
    desc1 = desc1.replace('<strong>', '"')
    desc1 = desc1.replace('</strong>', '"')
    return desc1


def get_crew():
    crew = "https://thefilmproduction.wordpress.com/"
    resposeSecond = requests.get(crew)
    s2txt = resposeSecond.text
    cat = s2txt.split("</h2>")
    for j in range(3, 5):
        row = cat[j].split("<p style=")
        for i in range(1, len(row)):
            key = row[i].split("<strong>")[1].split("</strong>")[0]
            desc = str(row[i].split('&#8211;')[1].split("</p>")[0])
            desc = rid_of_signs(desc)
            role_dict[key] = desc
    resposeSecond.close()


def get_art():
    key = "Production Designer"
    desc = "Production Designers are major heads of department on film crews, and are responsible for the entire Art Department. They play a crucial role in helping Directors to achieve the film’s visual requirements, and in providing Producers with carefully calculated schedules which offer viable ways of making films within agreed budgets and specified periods of time. Filming locations may range from an orderly Victorian parlour, to a late-night café, to the interior of an alien space ship. The look of a set or location is vital in drawing the audience into the story, and is an essential element in making a film convincing and evocative. A great deal of work and imagination goes into constructing an appropriate backdrop to any story, and into selecting or constructing appropriate locations and/or sets."
    role_dict[key] = desc
    key = "Art Director"
    desc = "Art Directors act as project managers for the biggest department on any film – the Art Department. They facilitate the Production Designer’s creative vision for all the locations and sets that eventually give the film its unique visual identity. Art Directors are responsible for the Art Department budget and schedule of work, and help the Production Designer to maximise the money allocated to the department. Art Directors are usually requested by the Production Designer, and are responsible for the Assistant Art Director, the Draughtsman* (as many as 20 Draughtsmen may be employed on big budget films), the Art Department Assistant(s) and all Construction personnel. As Art Directors must find practical solutions to creative problems while simultaneously monitoring the budget, this is highly skilled work. Many Art Directors work on television drama and commercials, as well as on films. The hours are long and the job can involve long periods working away from home. Art Directors work on a freelance basis."
    role_dict[key] = desc
    key = "Carpenter"
    desc = "Carpenters on film productions are key members of the construction team, and they must be very skilled at their craft.  Reporting to the Chargehand Carpenter, they build, install and remove wooden structures on film sets and locations, and also make wooden props, furniture and scenic equipment.  The role requires extensive carpentry experience and creative skills, as well as the ability to work to deadlines, and under pressure."
    role_dict[key] = desc
    key = "Set Decorator"
    desc = "Set Decorators provide anything that furnishes a film set, excluding structural elements. They may have to provide a range of items, from lumps of sugar and tea spoons, to newspapers, furniture and drapes, to cars, carriages, or even cats and dogs. There are two types of props: action props, or all props that are described in the shooting script; and dressing props, or items that help to bring characters to life or to give a certain atmosphere and sense of period to a place."
    role_dict[key] = desc


def get_g2(link):
    resposeSecond = requests.get(link)
    s2txt = resposeSecond.text
    s2txt = s2txt.replace('"', '')
    rows = s2txt.split("<h2 style=text-align:justify;><span style=color:#ff0000;")
    for i in range(1, len(rows)):
        key = rows[i].split("</span></h2>")[0][4:]
        desc = rows[i].split("<p style=text-align:justify;>")[1].split(".</p>")[0]
        desc = rid_of_signs(desc)
        role_dict[key] = desc
    resposeSecond.close()


def get_dir():
    dir = "https://thefilmproduction.wordpress.com/direction-department/"
    resposeSecond = requests.get(dir)
    s2txt = resposeSecond.text
    s2txt = s2txt.replace('"', '')
    rows = s2txt.split("<h2 style=text-align:justify;><span style=color:#ff0000;")
    for i in range(1, len(rows)):
        key = rows[i].split("</span></h2>")[0][4:]
        if (i == 1) or (i == 5):
            desc = desc = rows[i].split("<p style=text-align:justify;>")[1].split("</p>")[0]
        else:
            desc = desc = rows[i].split("<p style=text-align:justify;>")[2].split("</p>")[0]
        desc = rid_of_signs(desc)
        role_dict[key] = desc
    resposeSecond.close()


def get_light():
    light = "https://thefilmproduction.wordpress.com/light-department/"
    resposeSecond = requests.get(light)
    s2txt = resposeSecond.text
    s2txt = s2txt.replace('"', '')
    rows = s2txt.split("<h2 style=text-align:justify;><span style=color:#ff0000;")
    for i in range(1, len(rows)):
        key = rows[i].split("</span></h2>")[0][4:]
        desc = desc = rows[i].split("<p style=text-align:justify;>")[2].split("</p>")[0]
        desc = rid_of_signs(desc)
        role_dict[key] = desc
    resposeSecond.close()


def get_style():
    style = "https://thefilmproduction.wordpress.com/style-department/"
    resposeSecond = requests.get(style)
    s2txt = resposeSecond.text
    s2txt = s2txt.replace('"', '')
    rows = s2txt.split("<h2>")
    for i in range(1, len(rows)):
        key = rows[i].split("</h2>")[0][3:]
        desc = rows[i].split("</h2>")[1].split("<p><strong>")[0]
        desc = desc.replace('<p>', '')
        desc = rid_of_signs(desc)
        role_dict[key] = desc
    resposeSecond.close()


def init_lang_dict(lang_dict):
    lang_api = requests.get(
        "https://api.themoviedb.org/3/configuration/languages?api_key=a48ba1f202cb5cd5e619e2f5e041b34a")
    txt = lang_api.text
    txt = txt.split('{')  # get a string of all the rows in that page
    entry_amt = len(txt)  # count the rows in this page
    for i in range(2, entry_amt):
        curr_row = txt[i][:-2]
        l_iso = (curr_row.replace('"', '').split("iso_639_1:")[1].split(',')[0])
        l_english = (curr_row.replace('"', '').split(",english_name:")[1].split(',')[0])
        lang_dict[l_iso] = l_english
    return


# ==========================global dictionaries===================================================
name_dict = {
    "department": "department(role, department, job_description)",
    "department_null": "department(role, department)",
    "locations": "locations(movie_id, country)",
    "movie_crew": "movie_crew(profile_id, role, movie_id)",
    "movies": "movies(movie_id, title, budget, revenue, runtime, language,"
              " poster_link, release_year, overview)",
    "movies_poster_link_null": "movies(movie_id, title, budget, revenue, runtime, language,"
                               " release_year, overview)",
    "profile": "profile(profile_id, name, gender, age, main_department, popularity, biography, photo_link)",
    "profile_age_null": "profile(profile_id, name, gender, main_department, popularity, biography, photo_link)",
    "profile_bio_null": "profile(profile_id, name, gender, age, main_department, popularity, photo_link)",
    "profile_bio_age_null": "profile(profile_id, name, gender, main_department, popularity, photo_link)",
    "genres": "genres(movie_id, genre)"
}

values_tup_dict = {
    "department": "(%s, %s, %s)",
    "department_null": "(%s, %s)",
    "locations": "(%s, %s)",
    "movie_crew": "(%s, %s, %s)",
    "movies": "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "movies_poster_link_null": "(%s, %s, %s, %s, %s, %s, %s, %s)",
    "profile": "(%s, %s, %s, %s, %s, %s, %s, %s)",
    "profile_age_null": "(%s, %s, %s, %s,%s, %s, %s)",
    "profile_bio_null": "(%s, %s, %s, %s,%s, %s, %s)",
    "profile_bio_age_null": "(%s, %s, %s, %s,%s, %s)",
    "genres": "(%s, %s)"
}

genre_dict = {"28": "Action", "12": "Adventure", "16": "Animation", "35": "Comedy",
              "80": "Crime", "99": "Documentary", "18": "Drama", "10751": "Family",
              "14": "Fantasy", "36": "History", "27": "Horror", "10402": "Music",
              "9648": "Mystery", "10749": "Romance", "878": "Science Fiction",
              "10770": "TV Movie", "53": "Thriller", "10752": "War", "37": "Western"}

lang_dict = {}
role_dict = {}


# ================================end of global dictionaries============================================


def init_database(cnx, cur):
    m_first_page_url = "https://api.themoviedb.org/3/discover/movie?api_key=a48ba1f202cb5cd5e619e2" \
                       "f5e041b34a&sort_by=revenue.desc&page=1&release_date.lte=2020-12-31"
    m_first_page_response = requests.get(m_first_page_url)
    m_first_page_txt = m_first_page_response.text

    m_page_amt = int(m_first_page_txt.replace('"', '').split("total_pages:")[1].split(",")[0])

    for k in range(86,91):

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
            m_temp_poster_link = m_curr_row.split(",poster_path:")[1].split(',')[0]
            if m_temp_poster_link == "null":
                m_poster_link = "null"
            else:
                m_poster_link = "https://image.tmdb.org/t/p/original/" + m_temp_poster_link
            m_release_year = (m_curr_row.split(",release_date:")[1].split('-')[0])
            m_overview = (m_curr_row.split(",overview:")[1]).split(',popularity:')[0]

            if m_poster_link == "null":
                insert_query(cnx, cur, "movies_poster_link_null", (m_id, m_title, m_budget, m_revenue, m_runtime,
                                                                   m_language, m_release_year, m_overview))
            else:
                insert_query(cnx, cur, "movies", (m_id, m_title, m_budget, m_revenue, m_runtime, m_language,
                                                  m_poster_link, m_release_year, m_overview))

            # genre related data
            m_genre = (m_curr_row.split(",genre_ids:[")[1].split(']')[0])
            m_gen_amt = len(m_genre.split(","))
            for j in range(m_gen_amt):
                m_curr_gen = genre_dict.get(m_genre.split(",")[j])
                # print(m_id, m_curr_gen)
                insert_query(cnx, cur, "genres", (m_id, m_curr_gen))

            # locations related data
            l_curr_row = m_txt2.replace('"', '')
            l_countries = l_curr_row.split(",production_countries:[")[1].split(']')[0]
            l_country_amt = len(l_countries.split('{')) - 1
            for j in range(1, l_country_amt + 1):
                l_curr_country = l_countries.split("{")[j].split(",name:")[1].split("}")[0]
                insert_query(cnx, cur, "locations", (m_id, l_curr_country))

            # profile related data
            p_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=a48ba1f202cb5cd5e619e2f5e041b34a".format(
                m_id)
            p_response = requests.get(p_url)
            p_txt = p_response.text
            p_txt = p_txt.replace('"', '')
            p_txt = p_txt.split(",crew:")[1]
            p_txt = p_txt.split('{')
            leng_crew = len(p_txt)
            for j in range(1, leng_crew):
                p_curr_row = p_txt[j]
                c_name = p_curr_row.split(",name:")[1].split(',')[0]
                c_gender = p_curr_row.split(",gender:")[1].split(',')[0]
                c_id = p_curr_row.split(",id:")[1].split(',')[0]
                c_known_for = p_curr_row.split(",known_for_department:")[1].split(',')[0]
                c_pop = p_curr_row.split(",popularity:")[1].split(',')[0]
                c_dep = p_curr_row.split(",department:")[1].split(',')[0]
                c_role = p_curr_row.split(",job:")[1].split('}')[0]
                urlbirth = "https://api.themoviedb.org/3/person/{}?api_key=a48ba1f202cb5cd5e619e2f5e041b34a".format(
                    c_id)
                p_response2 = requests.get(urlbirth)
                p_txt2 = p_response2.text
                p_txt2 = p_txt2.replace('"', '')
                c_bio = p_txt2.split(",biography:")[1].split(",")[0]
                c_age = p_txt2.split(",birthday:")[1].split(",")[0]
                c_photo_link = p_txt2.split(",profile_path:")[1].split("}")[0]
                c_photo_link = "https://image.tmdb.org/t/p/original/" + c_photo_link
                if c_age == "null" and c_bio == "":
                    insert_query(cnx, cur, "profile_bio_age_null",
                                 (c_id, c_name, c_gender, c_known_for, c_pop, c_photo_link))
                elif c_age == "null":
                    insert_query(cnx, cur, "profile_age_null",
                                 (c_id, c_name, c_gender, c_known_for, c_pop, c_bio, c_photo_link))
                elif c_bio == "":
                    c_age = str(2020 - int(c_age[:4]))
                    insert_query(cnx, cur, "profile_bio_null",
                                 (c_id, c_name, c_gender, c_age, c_known_for, c_pop, c_photo_link))
                else:
                    c_age = str(2020 - int(c_age[:4]))
                    insert_query(cnx, cur, "profile",
                                 (c_id, c_name, c_gender, c_age, c_known_for, c_pop, c_bio, c_photo_link))
                # department related data
                d_role_description = role_dict.get(c_role, "null")
                if d_role_description == "null":
                    insert_query(cnx, cur, "department_null", (c_role, c_dep))
                else:
                    insert_query(cnx, cur, "department", (c_role, c_dep, d_role_description))
                insert_query(cnx, cur, "movie_crew", (c_id, c_role, m_id))
                p_response2.close()

            m_response.close()
            p_response.close()
        print(k)


def main():
    cnx = connect_to_db()
    cur = cnx.cursor(buffered=True)
    init_role_dict()
    init_lang_dict(lang_dict)
    init_database(cnx, cur)
    cur.close()
    cnx.close()
    print("done!")

main()
