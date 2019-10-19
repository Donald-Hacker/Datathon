import csv

#import restaurant as File
class Restaurant:
    def __init__(self,id,category,province,city,address,postalcode,latitude,longitude,website,menuUrl):
        self.id  = id
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

class Food:
    def __init__(self,id,menuname,menudescription,cost):
        self.id = id
        self.menuname = menuname
        self.menudescription = menudescription
        self.cost = cost



# Names of Files
csv_file = open("just tacos and burritos.csv")
data = csv.reader(csv_file)


restaurantList = []
hasMenu = True
previousId = "0";

# Loops through the csv file line by line
for line in data:
    # turns the entire line into an array


    #previous id is derived from the Restaurant class
    if previousId != "0":
        previousId = restaurantList[len(restaurantList)-2]


    # checks to see if there is a menu on the website
    if line[7]:
        hasMenu = True
    else:
        hasMenu = False


    # checks to see if the its the same restaurant
    if previousId == line[0] or previousId == '0':
        restaurantList.append(Restaurant(previousId,line[2],line[13],line[3],line[1],line[12],line[5],line[6],line[14],hasMenu))
    else:
        restaurantList.append(Restaurant(line[0],line[2],line[13],line[3],line[1],line[12],line[5],line[6],line[14],hasMenu))


print(restaurantList)
