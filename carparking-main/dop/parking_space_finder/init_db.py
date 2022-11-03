import sqlite3

connection = sqlite3.connect('database.db')


with open('D:\SEMESTER\FIFTH_SEMESTER\CSE3001\project\carparking-main\carparking-main\dop\parking_space_finder\schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO todo (user_name, user_pass) VALUES (?, ?)",
            ('mayank', '123')
            )

cur.execute("INSERT INTO todo (user_name, user_pass) VALUES (?, ?)",
            ('aman', '321')
            )

connection.commit()
connection.close()