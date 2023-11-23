total = neg_count = 0 # changed == to = #+1m
month_values = [] # changed to list #+1m
filename = "September.csv"

with open(filename, "r") as infile:
    temp = infile.readline().split(",")          

for value in temp: # changed to for loop #+1m
    month_values.append(int(value)) #+1m

for x in month_values: #removed range and changed to loop through list #+1m
    if x > 0: # checks if the individual item in list is > 0 #+1m
        total += x
    else: # changed syntax #+1m
        neg_count = neg_count + 1

total_count = len(month_values) - neg_count # put as a variable #+1m
avg_rainfall = total / total_count

print("The average rainfall for the month of {} is {}.".format(filename[:-4],avg_rainfall)) #rearranged formatting #+1m

'''
Task 3
Total: 9/10
'''
