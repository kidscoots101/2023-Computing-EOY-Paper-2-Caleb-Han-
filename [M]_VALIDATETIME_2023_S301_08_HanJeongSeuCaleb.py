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

print(validateTime("45:20"))

# Length check of 5 is missing
# Your colon check assume to input only have 1 colon.
# Forced casting into int can crash your program, use isdigit() 1st

# Q12 2/4
    
















