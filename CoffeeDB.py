import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM sqlite_master")
con.close()

#To add data to database: Add Farm, ProcessingMethod, User. Then add Bean, add Batch, add BeanInBatch. Then add Coffee, then add Post

def postNote():
    print("Post New Note to CoffeeDB")
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    points = input("Points Score: ")
    if 0 <= points <= 10:
        print("asdasd")
    else:
        print("asdasd")
    notes = input("Notes: ")

    print(f"New Post posted!\n\n")

def printTopUsers():
    print("Printing Top Coffee Drinkers This Year")
    for row in cursor.execute("SELECT U.UserID, U.FullName, COUNT(P.UserID) AS CoffeesDrunk FROM User AS U LEFT JOIN Post AS P"
                    "WHERE P.UserID = U.UserID AND P.tastingdate LIKE '%2022%'"
                    "GROUP BY U.UserID"
                    "ORDER BY COUNT(P.UserID) DESC"):
                    print(row)

def valueForMoney():
    print("Printing Highest Average Score to Price Ratio")
    for row in cursor.execute("SELECT C.name, C.priceperkilo, C.roastery, AVG(P.points)/C.priceperkilo AS AvgScoreToPriceRatio"
                                "FROM Coffee AS C LEFT JOIN Post AS P"
                                "WHERE C.CoffeeID = P.CoffeeID ORDER BY AvgScoreToPriceRatio DESC"):
                    print(row)

def searchKeyword():
    keyword = input("\nEnter a keyword to search for: ").lower()
    for row in cursor.execute("Select C.name, C.roastery"
                                "FROM Coffee AS C LEFT JOIN Post AS P ON P.CoffeeID = C.CoffeeID"
                                "WHERE P.tastingnotes LIKE keyword=:keyword OR C.description LIKE keyword=:keyword", {"keyword": keyword}):
                    print(row)
        
def includeCountriesExcludeMethod():
    countryInput = (input("Enter up to three countries to search for: ").lower()).split()
    countries = [countryInput.append(None) for i in range(3-len(countryInput))]
    method = input("Enter a method to exclude.").lower()
    for row in cursor.execute("SELECT Coffee.CoffeeName, Coffee.Roastery FROM Coffee"
                                "INNER JOIN Batch ON Coffee.BatchID = Batch.BatchID"

                                "WHERE (method=:method IS NULL OR LOWER(ProcessingMethod.Name) <> method=:method)"
                                "AND (country1=:country1 IS NULL OR LOWER(Farm.Country) = country1=:country1"
                                "AND (country2=:country2 IS NULL OR LOWER(Farm.Country) = country2=:country2"
                                "AND (country3=:country3 IS NULL OR LOWER(Farm.Country) = country3=:country3", {"method": method, "country1": countries[0], "country2": countries[1], "country3": countries[3]}):
        print("row")

while True: #Login check
    print("Welcome to CoffeeDB.")
    email = input("Please enter email: ")
    password = input("Please enter password: ")
    try:
        login = cursor.execute("SELECT User.Email, User.Password"
                                "WHERE User.Email IS email=:email"
                                "AND User.Password IS password=:password", {"email": email, "password": password})
    except ValueError:
        print("Could not find user. Try again: ")
        continue

functionList = [postNote, printTopUsers, valueForMoney, searchKeyword, includeCountriesExcludeMethod]

while True: #Main program loop
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
