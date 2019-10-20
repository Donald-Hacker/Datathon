import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from decimal import Decimal

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



# cost of tacos and burritos based on zip codes and city


# Names of Files
csv_file = open("just tacos and burritos.csv")
data = csv.reader(csv_file)
data.next();




#test and correct Data


restaurantList = []
hasMenu = True
previousId = "first"

# (Restaurant Data)
for line in data:

    # checks to see if there is a menu on the website
    if line[7]:
        hasMenu = "True"
    else:
        hasMenu = "False"

    id=line[0]
    name=line[11]
    category=line[2]
    province=line[13]
    city=line[3]
    address=line[1]
    postalcode=line[12]
    latitude=line[5]
    longitude=line[6]
    website=line[14]
    menuname = line[10]
    menudescription = line[9]
    cost = line[8]

    # checks to see if the same restaruant is repeated,
    # if it is, then append the menu o include a new food item
    if previousId != line[0]:
        # places an NULL for empty values

        if cost != '':
            cost = float(cost)

        if postalcode != '' and len(postalcode) <= 5:
            postalcode = float(postalcode)

        previousId = line[0]
        restaurantList.append(Restaurant(id,name,category,province,city,address,postalcode,latitude,longitude,website,hasMenu))
        restaurantList[len(restaurantList)-1].menu.append(Food(menuname,menudescription,cost))
    else:
        if cost != '':
            cost = float(cost)
        restaurantList[len(restaurantList)-1].menu.append(Food(menuname,menudescription,cost))

# (Yelp Data)
#



#raw data calculations
costTotal = 0
count = 0

costTotal2 = 0
count2 = 0


# mean of tacos and burrtiosc
for x in restaurantList:
    # remove empty data and null

    for y in range(len(x.menu)):
            # raw data
            # print(x.menu[y].cost)
        '''if(x.menu[y].cost != ''):
            costTotalRaw += x.menu[y].cost
            countRaw += 1
            '''
        #remove O's and empty values for cost
        if x.menu[y].cost and x.menu[y].cost < 200 and x.menu[y].cost != 0.0:

            # print(x.menu[y].cost)
            costTotal += x.menu[y].cost
            count += 1

        if x.menu[y].cost and x.menu[y].cost < 100 and x.menu[y].cost != 0.0:

            # print(x.menu[y].cost)
            costTotal2 += x.menu[y].cost
            count2 += 1

#meanRaw = costTotalRaw/countRaw
mean = costTotal/count
mean2 = costTotal2/count2

#print meanRaw,"\n"
print "Average: ", mean," count: ", count, "\n"
print "Average: ", mean2," count: ", count2, "\n"








#How to access The data
# Note: Do not index 0, its the name of the columns
# print "id: " + restaurantList[1].id + "\n"
# print "name: " + restaurantList[1].name + "\n"
# print "city: " + restaurantList[1].city + "\n"
# print "province: " + restaurantList[1].province + "\n"
# print "address: " + restaurantList[1].address + "\n"
# print "postalcode: " + restaurantList[1].postalcode + "\n"
# print "website: " + restaurantList[1].website + "\n"
# print "hasmenuUrl: " + restaurantList[1].menuUrl + "\n"
#
# print "menu name: " + restaurantList[1].menu[1].menuname + "\n"
# print "menudescription: " + restaurantList[1].menu[1].menudescription + "\n"
# print "cost" + restaurantList[1].menu[1].cost + "\n"
