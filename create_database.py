import sqlite3 as db


def create_dbs():
    conn = db.connect("main.db")
    conn2 = db.connect("recv_img/users_list.db")
    c = conn.cursor()
    c2 = conn2.cursor()

    c.execute(''' CREATE TABLE login (userid TEXT, userpwd TEXT) ''')
    c2.execute(''' CREATE TABLE users (userid TEXT) ''')

    users_list = [
        ["krishna", "krishna132"],
        ["kalyani", "kalyani132"],
        ["gopi", "gopi139"],
        ["sai", "sai267"],
        ["manoj", "manoj142"],
        ["mano", "mano138"],
        ["dushyanth", "dushyanth133"],
        ["ashok", "ashok123"],
        ["rrk", "rrk124"]
    ]

    for user in users_list:
        c.execute("INSERT INTO login VALUES (?,?)", [user[0], user[1]])
        c2.execute("INSERT INTO users VALUES (?)", [user[0]])

    conn.commit()
    conn2.commit()

    conn.close()
    conn2.close()


def creater_user():
    conn        = db.connect("main.db")
    conn2       = db.connect("recv_img/users_list.db")
    c           = conn.cursor()
    c2          = conn2.cursor()

    username    = str(input("Enter user name : "))
    while True:
        c.execute("SELECT * FROM login WHERE userid = ?", [username])
        if len(c.fetchall()):
            username = str(input("User is already there, Pick another user Name : "))
        else:
            break
    userpwd = str(input("Enter your Password : "))

    c.execute("INSERT INTO login VALUES (?,?)", [username, userpwd])
    c2.execute("INSERT INTO users VALUES (?)", [username])

    conn.commit()
    conn2.commit()

    print("User Created Successfully!!")

    conn.close()
    conn2.close()


if __name__ == "__main__":
    create_dbs()
