print("Welcome to UG house managing system "+"\n","please select an option") 

def ViewAll(HouseName=None, HouseType=None): 
    houses ={1:{"Type":"Condo", "Name":"The Loft"},
        2:{"Type":"Villa", "Name":"Villa Peaceful"},
        3:{"Type":"Apartment", "Name":"Adoley Resident"},
        4:{"Type":"Bungalow", "Name":"Paddocks"},
        5:{"Type":"Villa", "Name":"Mensah Lodge"}}
    
    # function0
def ViewAll(HouseName=None, HouseType=None): 
    
    houses ={1:{"Type":"Condo", "Name":"The Loft"},
        2:{"Type":"Villa", "Name":"Villa Peaceful"},
        3:{"Type":"Apartment", "Name":"Adoley Resident"},
        4:{"Type":"Bungalow", "Name":"Paddocks"},
        5:{"Type":"Villa", "Name":"Mensah Lodge"}}
    
    for house_id, house_info in houses.items():print("\nHouse ID: ", house_id)
    for t in house_info:
        print(t,": ", house_info[t])
# functions
def addHouse(HouseName=None, HouseType=None): 
    HouseName = input("Enter a House name:") 
    HouseType = input("Set house type:") 
    db = open("database.txt", "r") 
    d = []
    f = [] 
    for i in d: 
        a,b, = i.split(",") 
        f = a,b
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
        print(data)
    if not len(HouseType)<=1: 
        db = open("database.txt", "r") 
        if not HouseName ==None: 
            if len(HouseName) <1: 
                print("Please provide a HouseName") 
                () 
            elif HouseName in d: 
                print("HouseName exists") 
                addHouse()   
            else: 
                if HouseType == HouseType: 
                    HouseType = HouseType.encode('utf-8') 
                    HouseType = (HouseType,()) 
                                        
                    db = open("database.txt", "a") 
                    db.write(HouseName+", "+str(HouseType)+"\n") 
                    print("House added successfully!")

#  functions1
def home1(option=None): print("Welcome, please select an option") 
option = input("View all | add house | modify a house:") 
if option == "View all":
    ViewAll()
elif option == "add house":
    addHouse()
else: 
    print("Please enter a valid parameter, this is case-sensitive") 
# function2
def home(option=None): print("Welcome, please select an option") 
option = input("View all | add house | modify a house:") 
if option == "View all":
    ViewAll()
elif option == "add house":
    addHouse()
else: 
    home1()

# function3
def addHouse(HouseName=None, HouseType=None): 
    HouseName = input("Enter a House name:") 
    HouseType = input("Set house type:") 
    db = open("database.txt", "r") 
    d = []
    f = [] 
    for i in d: 
        a,b, = i.split(",") 
        f = a,b
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
        print(data)
    if not len(HouseType)<=1: 
        db = open("database.txt", "r") 
        if not HouseName ==None: 
            if len(HouseName) <1: 
                print("Please provide a HouseName") 
                () 
            elif HouseName in d: 
                print("HouseName exists") 
                addHouse()   
            else: 
                if HouseType == HouseType: 
                    HouseType = HouseType.encode('utf-8') 
                    HouseType = (HouseType,()) 
                                        
                    db = open("database.txt", "a") 
                    db.write(HouseName+", "+str(HouseType)+"\n") 
                    print("House added successfully!")
