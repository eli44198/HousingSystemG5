import database
from database import *

print("Welcome to UG house managing system " + "\n", "please select an option")


def home():
    option = int(input(
        "\n"
        "Press 1: View all house \n"
        "press 2: Add your house \n"
        "Press 3: Modify house details \n"
        "\n********************************************************************\n"
    ))

    #For Option 1: view all houses
    if option == 1:
        def ViewAll():
            print(*view_all)
        ViewAll()
        home()

    #For option 2: add a house function
    elif option == 2:

        def addHouse():
            print("Use underscore _ inplace of space")
            HouseName = input(str("Enter a the name of the house: \n"))
            HouseId = input("Enter the house Id: \n")
            HouseType = input("Enter the type of house: \n")

            db = open("database.py", "a")

            if HouseName not in database.view_all:
                add = "\n%s = {'House_Id': \'%s\',  'Type': \'%s\', 'Name': \'%s\'} \n\n" \
             % (HouseName, HouseId, HouseType, HouseName)
                db.write(add)
                db.write("view_all.append('%s')" % HouseName)
                db.close()
            else:
                print("Please try again")
                home()
        addHouse()

    #For option 3: Modify house details
    elif option == 3:
        def modify():
            print(*view_all)
            try:
                House = input("\nWhich house do you wish to modify? \n")
                attributes = input("\nWhat do you wish to modify? \n")
                features = ["House_Id", "Name", "Type"]
                print(*features)
                
            except:
                print("Failed. Please try again")
        modify()
    else:
        print("Please try again")
home()




