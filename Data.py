import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json
import math
#!/usr/bin/expect
#general description of raw data
Rest_data = pd.read_csv("just tacos and burritos.csv")
#print Rest_data.describe(), "\n"
data_cost = Rest_data["menus.amountMin"]
Rest_data["menus.amountMin"].fillna(data_cost.mean(), inplace = True)
# print Rest_data.describe()
#print descriptive_stats_costs

# # Number of restauarnat
# data_id = data["id"]
# data_id_unique = data_id.unique()
# number_of_rest = len(data_id_unique)
# #print "\nNumber of Restaurants: ",number_of_rest
mean_state = []
abbr = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
abbr2 = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
cost_v_state = Rest_data[["menus.amountMin","province"]]
for x in range(50):
    value = cost_v_state.query("province == '" + abbr[x] +"'" or "province == '" + abbr2[x] +"'")
    z = float(value["menus.amountMin"].mean())
    if not math.isnan(z):
        mean_state.append(value["menus.amountMin"].mean())
    else:
        mean_state.append(0)
print min(mean_state),"\n",max(mean_state)

# y_pos = np.arange(50)
# plt.bar(y_pos,mean_state,align = 'center')
# plt.xticks(y_pos,abbr)
# plt.show()
