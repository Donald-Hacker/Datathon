
import restaurant


# Names of Files
csv_file = "data.csv"

# opens files
data = open(csv_file,"r")

# Reads the first line of the csv file
properties = data.readline().rstrip("\n").split(',')

# Loops through the csv file line by line
for line in data:
    # turns the entire line into an array
    line = line.rstrip('\n').split(',')
    print(line)
print(properties)



#sort
