import sqlite3
con = sqlite3.connect("CoffeeDB.db")

#To add data to database: Add Farm, ProcessingMethod, User. Then add Bean, add Batch, add BeanInBatch. Then add Coffee, then add Post
# Example users:
# test | test | Test Testesen
# adrianfauske@gmail.com | banan | Adrian Nasir Fauske
# williarh@stud.ntnu.no | eple | William Strand Hassel
# kraemer@ntnu.no | 123 | Frank Alexander Kraemer

def postNote():
    print("Post New Note to CoffeeDB:")
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    while True:
        points = int(input("Points Score: "))
        if not 0 <= points <= 10:
            print("Please enter a valid score. ")
        break

    notes = input("Notes: ")
    cursor = con.cursor()
    print("List of roasteries: ")
    for row in cursor.execute("SELECT DISTINCT roastery FROM Coffee"):
        print(row)
    inRoastery = input("Select which roastery your coffee is from.")
    roasteryTest = cursor.execute("SELECT Roastery FROM Coffee INNER JOIN Post ON Coffee.CoffeeID = Post.coffeeID")
    # cursor.execute("INSERT INTO Post (tastingnotes, points) VALUES ({tastingnotes}, {points})")
    # val = (tastingnotes, points)
    # cursor.execute(sql, val)
    cursor.execute("SELECT UserID FROM User WHERE email=:email", {"email": email})
    myID = cursor.fetchone()
    myID = int(myID[0])
    cursor.execute("SELECT CoffeeID FROM Coffee WHERE name=:name", {"name": coffeeName})
    coffeeID = cursor.fetchone()
    coffeeID = int(coffeeID[0])

    cursor.execute("INSERT INTO Post (tastingnotes, tastingdate, UserID, CoffeeID, points) VALUES (?, CURRENT_DATE, ?, ?, ?)", (notes, myID, 1, points,))

    con.commit()
    print(f"\nNew Post posted!")

def printTopUsers():
    print("\n\nPrinting Top Coffee Drinkers This Year\nName | Cups of coffee drunk")
    cursor = con.cursor()
    for row in cursor.execute("SELECT U.FullName, COUNT(P.UserID) AS CoffeesDrunk FROM User AS U LEFT JOIN Post AS P WHERE P.UserID = U.UserID AND P.tastingdate LIKE '%2022%' GROUP BY U.UserID ORDER BY COUNT(P.UserID) DESC"):
                    print(row)
def valueForMoney():
    print("Printing Highest Average Score to Price Ratio")
    cursor = con.cursor()
    for row in cursor.execute("SELECT C.name, C.priceperkilo, C.roastery, AVG(P.points)/C.priceperkilo AS AvgScoreToPriceRatio FROM Coffee AS C LEFT JOIN Post AS P WHERE C.CoffeeID = P.CoffeeID ORDER BY AvgScoreToPriceRatio DESC"):
                    print(row)

def searchKeyword():
    keyword = input("Enter a keyword to search for: ").lower()
    cursor = con.cursor()
    print(f"\nPrinting coffees containing keyword {keyword}: ")
    for row in cursor.execute("SELECT C.name, C.roastery FROM Coffee AS C LEFT JOIN Post AS P ON P.CoffeeID = C.CoffeeID WHERE P.tastingnotes LIKE ? OR C.description LIKE ?", ['%'+keyword+'%', '%'+keyword+'%']):
                    print(row)
        
def includeCountriesExcludeMethod():
    print("List of available countries: ")
    cursor = con.cursor()
    for row in cursor.execute("SELECT country FROM Farm"):
        print(row)
    countryInput = (input("Enter up to two countries to search for, separated by a space: ").lower()).split()
    if len(countryInput) > 2:
        print("Please select MAX 2 countries.")
        includeCountriesExcludeMethod()
    countries = countryInput
    for i in range (2 - len(countryInput)):
        countries.append(None)
    #countries.append(None) = countryInput.append(None) for i in range(3-len(countryInput))

    print("\nList of all available processing methods: ")
    cursor = con.cursor()
    for row in cursor.execute("SELECT name from ProcessingMethod"):
        print(row)
    method = input("Enter a method to exclude: ").lower()
    print(countries)

    print(f"\nSearching for coffees that are not {method} from countries {countries}.")
    cursor = con.cursor()
    for row in cursor.execute("SELECT C.name, C.roastery FROM Coffee AS C INNER JOIN Batch AS B ON C.BatchID = B.BatchID INNER JOIN ProcessingMethod AS P on B.ProcessingMethodID = P.ProcessingMethodID INNER JOIN Farm AS F WHERE B.FarmID = F.FarmID AND P.name IS NOT :method AND ((:country1 IS NULL OR LOWER(F.country) =:country1) OR (:country2 IS NULL OR LOWER(F.country) =:country2))", {"method": method, "country1": countries[0], "country2": countries[1]}):
                    print(row)

while True: #Login check
    print("Welcome to CoffeeDB.")
    email = input("Please enter email: ")
    password = input("Please enter password: ")
    cursor = con.cursor()
    login = cursor.execute("SELECT email, password FROM User WHERE email =:email AND password =:password", {"email": email, "password": password})
    if login.fetchone() != None:
        cursor = con.cursor()
        name = cursor.execute("SELECT fullname FROM User WHERE email=:email", {"email": email})
        print(f"Logged in as {name.fetchone()}")
        break
    else:
        print("Error logging in. Try again.\n")
        continue

functionList = [postNote, printTopUsers, valueForMoney, searchKeyword, includeCountriesExcludeMethod]

while True: #Main program loop
    print("""\n\nFunctions:
    1 | Post Note
    2 | Print Top Coffee Tasters This Year
    3 | Print Highest Average Score to Price Ratio
    4 | Search for Keyword
    5 | Search For Countries and Exclude Methods
    6 | Exit Program""")
    try:
        initInput = int(input("Input Desired Function Number: "))
    except ValueError:
        print("Input an integer corresponding to a function.")
        continue
    if initInput == 6:
        print("Exiting Program.")
        break
    elif not 1 <= initInput <= (len(functionList) + 1) :
        print("Not a function! Try again.")
    else:
        functionList[initInput - 1]()

con.close()