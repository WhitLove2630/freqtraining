import sqlite3
def login() :
    while True :
        username = input('Enter Username:\n')
        with sqlite3.connect('freqtest.db') as db:
            c = db.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        results = c.fetchall()

        if results:
            for i in results:
                print(f'Welcome {i[0]}')
            return (username)
        else:
            newprompt = input("Username not recognized. Create new user?(y/n):\n")
            if newprompt.lower() == 'y' :
                return new_user(username)
            else: continue
def new_user(_username) :
    email = input("Enter email:\n")
    with sqlite3.connect('freqtest.db') as db:
        c = db.cursor()
    c.execute("INSERT INTO users VALUES(?, ? , DATETIME('NOW', 'LOCALTIME'), 0)", (_username, email))
    db.commit()
