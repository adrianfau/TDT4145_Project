print("banana")
import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM sqlite_master")
con.close()

def postNote():
    print("Post New Note to CoffeeDB")
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    points = input("Points Score: ")
    notes = input("Notes: ")

    print(f"New Post posted!\n\n")


def printTopUsers():
    print("Printing Top Coffee Drinkers This Year")
    for row in cursor.execute("SELECT User.UserID, User.FullName, COUNT(Post.UserID)"
                    "WHERE Post.UserID = User.UserID AND Post.TastingDate = '2022'" 
                    "GROUP BY User.UserID" 
                    "ORDER BY COUNT(Post.UserID) DESC"):
                    print(row)


def valueForMoney():
    print("Printing Highest Average Score to Price Ratio")
    for row in cursor.execute("SELECT Coffee.CoffeeID, Coffee.CoffeeName, Coffee.Price, Post.CoffeeID, Post.Points"
                    ""
                    ""):
                    print(row)


def searchKeyword():
    keyword = input("\nEnter a keyword to search for: ")
    for row in cursor.execute("SELECT Coffee.CoffeeNames, Coffee.Roastery"
                    "FROM Post INNER JOIN Coffee ON Post.CoffeeID = Coffee.CoffeeID" 
                    "WHERE CONTAINS(Post.Notes, keyword=:keyword) OR CONTAINS(Coffee.Description, keyword=:keyword)", {"keyword": lower(keyword)}):
                    print(row)
        

def includeCountriesExcludeMethod():
    countries = input("Enter up to three countries to search for: ")
    method = input("Enter a method to exclude.")
    for row in cursor.execute("SELECT"):
        print("row")

functionList = [postNote, printTopUsers, valueForMoney, searchKeyword, includeCountriesExcludeMethod]

while True:
    print("""Functions:
    1 | Post Note
    2 | Print Top Coffee Tasters This Year
    3 | Print Highest Average Score to Price Ratio
    4 | Search for Keyword
    5 | Search For Countries and Exclude Methods
    6 | Exit Program\n""")
    try:
        initInput = int(input("Input Desired Function Number: "))
    except ValueError:
        print("Input an integer. ")
        continue
    if initInput == 6:
        print("Exiting Program.\n\n")
        break
    elif not 1 <= initInput <= (len(functionList) + 1) :
        print("Not a function! Try again.\n\n")
    else:
        functionList[initInput - 1]()
