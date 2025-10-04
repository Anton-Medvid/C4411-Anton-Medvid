import sqlite3

connection = sqlite3.connect('itstep_DB.sl3', 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Anton');")
cur.execute("INSERT INTO first_table (name) VALUES ('Medvid');")
connection.commit()
connection.close()