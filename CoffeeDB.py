print("banana")
import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM sqlite_master")
con.close()

#To add data to database: Add Farm, Add ProcessingMethod, Add User, Add Bean, Add Batch, Add BeanInBatch, add Coffee, Add Post

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
    keyword = lower(input("\nEnter a keyword to search for: "))
    for row in cursor.execute("SELECT Coffee.CoffeeNames, Coffee.Roastery"
                    "FROM Post INNER JOIN Coffee ON Post.CoffeeID = Coffee.CoffeeID" 
                    "WHERE CONTAINS(LOWER(Post.Notes), keyword=:keyword) OR CONTAINS(LOWER(Coffee.Description), keyword=:keyword)", {"keyword": keyword}):
                    print(row)
        

def includeCountriesExcludeMethod():
    countryInput = split(lower(input("Enter up to three countries to search for: ")))
    countries = [countryInput.append(None) for i in range(3-len(x))]
    method = lower(input("Enter a method to exclude."))
    for row in cursor.execute("SELECT Coffee.CoffeeName, Coffee.Roastery FROM Coffee"
                                "INNER JOIN Batch ON Coffee.BatchID = Batch.BatchID"

                                "WHERE (method=:method IS NULL OR LOWER(ProcessingMethod.Name) <> method=:method)"
                                "AND (country1=:country1 IS NULL OR LOWER(Farm.Country) = country1=:country1"
                                "AND (country2=:country2 IS NULL OR LOWER(Farm.Country) = country2=:country2"
                                "AND (country3=:country3 IS NULL OR LOWER(Farm.Country) = country3=:country3", {"method": method, "country1": countries[0], "country2": countries[1], "country3": countries[3]}):
        print("row")

while True:
    print("Welcome to CoffeeDB.")
    email = input("Please enter email: ")
    password = input("Please enter password: ")
    try:
        login = cursor.execute("SELECT User.Email, User.Password"
                                "WHERE User.Email IS email=:email"
                                "AND User.Password IS password=:password", {"email": email, "password": password})
    except ValueError

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
