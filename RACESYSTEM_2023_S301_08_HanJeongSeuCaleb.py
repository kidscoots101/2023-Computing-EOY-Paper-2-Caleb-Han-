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
total_time_list = []
for i in list_bae:
    splitted = i.split(":")
    minute = int(splitted[0]) * 60
    seconds = int(splitted[1])
    total_time_list.append(minute+seconds)
section_a1 = total_time_list[2] - total_time_list[1] - total_time_list[0]
section_a2 = total_time_list[1]
section_B = total_time_list[0]
if section_a1 + section_a2 < section_B:
    print("Section A1 + A2 is faster than Section B.")
elif section_a1 + section_a2 > section_B:
    print("Section A1 + A2 is slower than Section B.")
elif section_a1 + section_a2 == section_B:
    print("Section A1 + A2 is equally as fast as Section B.")
    
    
















