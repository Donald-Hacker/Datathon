import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json


#general description of raw data
Rest_data = pd.read_csv("just tacos and burritos.csv")
data_cost = Rest_data["menus.amountMin"]
Rest_data["menus.amountMin"].fillna(data_cost.mean(), inplace = True)
#print descriptive_stats_costs

# # Number of restauarnat
# data_id = data["id"]
# data_id_unique = data_id.unique()
# number_of_rest = len(data_id_unique)
# #print "\nNumber of Restaurants: ",number_of_rest
business_data = pd.read_json("business.json",lines=True)
business_data = business_data[["stars","address"]]
RestData = RestData.join(business_data,how="inner",on="address")
Rest_data = user[["address","stars"]]
print Rest_data.describe()
