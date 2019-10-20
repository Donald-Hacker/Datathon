import csv

# Class Declarations
class Restaurant(object):
    def __init__(self,id=None,name=None,category=None,province=None,city=None,address=None,postalcode=None,latitude=None,longitude=None,website=None,menuUrl=None):
        self.id  = id
        self.name = name
        self.category = category
        self.province = province
        self.city = city
        self.address = address
        self.postalcode = postalcode
        self.latitude = latitude
        self.longitude  = longitude
        self.website = website
        self.menuUrl = menuUrl
        self.menu = []

class Food(object):
    def __init__(self,menuname=None,menudescription=None,cost=None):
        self.menuname = menuname
        self.menudescription = menudescription
        self.cost = cost

    def __str__(self):
        return self.menuname





# Names of Files
csv_file = open("just tacos and burritos.csv")
data = csv.reader(csv_file)


restaurantList = []
hasMenu = True
previousId = "first"

# Loops through the csv file line by line
for line in data:

    # checks to see if there is a menu on the website
    if line[7]:
        hasMenu = "True"
    else:
        hasMenu = "False"

    # checks to see if the same restaruant is repeated,
    # if it is, then append the menu o include a new food item
    if previousId != line[0]:
        restaurantList.append(Restaurant(line[0],line[11],line[2],line[13],line[3],line[1],line[12],line[5],line[6],line[14],hasMenu))
        restaurantList[len(restaurantList)-1].menu.append(Food(line[10],line[9],line[8]))
        previousId = line[0]
    else:
        restaurantList[len(restaurantList)-1].menu.append(Food(line[10],line[9],line[8]))



#How to access The data
# Note: Do not index 0, its the name of the columns
print "id: " + restaurantList[1].id + "\n"
print "name: " + restaurantList[1].name + "\n"
print "city: " + restaurantList[1].city + "\n"
print "address: " + restaurantList[1].address + "\n"
print "postalcode: " + restaurantList[1].postalcode + "\n"
print "website: " + restaurantList[1].website + "\n"
print "hasmenuUrl: " + restaurantList[1].menuUrl + "\n"

print "menu name: " + restaurantList[1].menu[1].menuname + "\n"
print "menudescription: " + restaurantList[1].menu[1].menudescription + "\n"
print "(this item does not have a cost)" + restaurantList[1].menu[1].cost + "\n"
