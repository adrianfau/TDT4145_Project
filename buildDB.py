import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM sqlite_master")
con.close()