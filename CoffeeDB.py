import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
#cursor.execute("SELECT * FROM sqlite_master")
#con.close()

while True:
    initInput = int(input("Choose function:;"))


def postNote(roastery, coffeeName, roastedDate, points, notes):


def printUsers():
    cursor.execute("SELECT User.UserID, User.FullName, COUNT(Post.UserID)"
                    "WHERE Post.UserID = User.UserID" 
                    "GROUP BY User.UserID" 
                    "ORDER BY COUNT(Post.UserID) DESC;")

def valueForMoney():
    cursor.execute("SELECT Coffee.CoffeeID, Coffee.CoffeeName, Coffee.Price, Post.CoffeeID, Post.Points"
                    ""
                    ";")

def searchKeyword(keyword):
    cursor.execute(f"SELECT Coffee.CoffeeNames, Coffee.Roastery"
                    "FROM Post INNER JOIN Coffee ON Post.CoffeeID = Coffee.CoffeeID" 
                    "WHERE Post.Notes CONTAINS {keyword} OR Coffee.Description CONTAINS {keyword}';")

def excludeKeyword(keyword):
    cursor.execute()

