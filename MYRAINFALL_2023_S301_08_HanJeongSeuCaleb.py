total = neg_count = 0 # changed == to =
month_values = [] # changed to list
filename = "September.csv"

with open(filename, "r") as infile:
    temp = infile.readline().split(",")          

for value in temp: # changed to for loop
    month_values.append(int(value))

for x in month_values: #removed range and changed to loop through list
    if x > 0: # checks if the individual item in list is > 0
        total += x
    else: # changed syntax
        neg_count = neg_count + 1

total_count = len(month_values) - neg_count # put as a variable
avg_rainfall = total / total_count

print("The average rainfall for the month of {} is {}.".format(filename[:-4],avg_rainfall)) #rearranged formatting
