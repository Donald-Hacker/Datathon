
#This is a restaurant object

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
