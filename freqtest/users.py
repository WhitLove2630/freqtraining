import sqlite3
import datetime

conn = sqlite3.connect('freqtest.db')
# conn.execute('PRAGMA foreign_keys = ON')
c = conn.cursor()

def create_users_table() :
    c.execute('''CREATE TABLE IF NOT EXISTS users
    (username TEXT PRIMARY KEY,
    email TEXT,
    date_created TEXT,
    times_played INTEGER)''')

def user_entry(username, email) :
    user = username
    mail = email
    c.execute('INSERT INTO users VALUES(?, ?, DATETIME("NOW", "LOCALTIME"), 0)',(user, mail))
    conn.commit()

def create_scores_table() :
    c.execute('''CREATE TABLE IF NOT EXISTS scores
    (datetime TEXT,
    id TEXT,
    frequency TEXT,
    score INTEGER)''')
def initial_score(username) :
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "50Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "63Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "80Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "100Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "125Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "160Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "200Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "250Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "315Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "400Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "500Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "630Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "800Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "1kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "1.25kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "1.6kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "2kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "3.15kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "4kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "5kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "6.3kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "8kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "10kHz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "12.5Hz", 0 , 0)', (username,))
    c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME") , ? , "16kHz", 0 , 0)', (username,))
    conn.commit()
    c.close()
    # conn.close()
u = 'TestUser'
em = 'TestUser@gmail.com'
create_users_table()
user_entry(u, em)
create_scores_table()
# initial_score(u)
