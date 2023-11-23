def validateTime(rt):
    isValidColon = False
    isValidss = False
    isValidmm = False
    for i in rt:
        if i == ":":
            isValidColon = True
            two_values = rt.split(":")
            mm = two_values[0]
            ss = two_values[1]
            if int(ss) > 59:
                isValidss = False
            elif int(ss) <= 59 and int(ss) > 0:
                isValidss = True
            if int(mm) > 0:
                isValidmm = True
            elif int(mm) < 0:
                isValidmm = False
    if isValidColon and isValidss and isValidmm:
        return True
    else:
        return False
while True:
    a12 = 0
    b = 0
    again = input("Do you want to enter more inputs? ") #how do user know what to enter?
    if again.lower() == 'n':                            #Asking for continue should come
        print("Thank you and have a nice day!")         # after the program run once
        break
    elif again.lower() == 'y':
        
        for _ in range(1,7):
            total_time_list = []
            while True:
                BAE = input("Enter the timings: ")
                list_bae = BAE.split(" ")
                value_valid = []
                for i in list_bae:
                    valid = validateTime(i)
                    value_valid.append(valid)
                if value_valid[0] and value_valid[1] and value_valid[2]:
                    break
                else:
                    print("Please enter a valid input")
            for i in list_bae:
                splitted = i.split(":")
                minute = int(splitted[0]) * 60
                seconds = int(splitted[1])
                total_time_list.append(minute+seconds)
            section_a1 = total_time_list[2] - total_time_list[1] - total_time_list[0]
            section_a2 = total_time_list[1]
            section_B = total_time_list[0]
            a12 += section_a1+section_a2
            b += section_B
        print("Summary of A1+A2 and B")
        print("Average of A1+A2: "+ " " + str(a12 /6) + " minutes") #See Line47
        print("Average of B: " + " "+ str(b/6) + " minutes")        #these are in seconds

# 1m : Loop statements for 6 iteration
# 1m : Variable(s) to store total timing for section a and B
# missing : Calculate average timing in mins
# missing : I/O statement to ask if user wants to continue
# 1m : Iterate program when 'Y' or 'y' is chosen

# Q14 /5















