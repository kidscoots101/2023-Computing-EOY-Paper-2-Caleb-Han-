while True: #Q9: +1m
    check = input("Do you want to check for membership eligibility?(y/n): ") #Q9: +1m
    if check.lower() == "y": 
        while True: 
            age = int(input("Enter your age: ")) #Q8: +0m; how do you know that input is int?
            if age < 0: #Q8: +0m; is 0 positive?
                print("Please enter a positive number!") #Q8: +1m
            elif age >= 0:
                if age <= 18:
                    print("You are eligible for a Junior membership.")
                    break
                else:
                    print("You are eligible for an Adult membership.")
                    #Q10: +1m (addition of code at the correct point)
                    freq = int(input("How many times a week do you swim? ")) #Q10: +1m
                    if freq <= 2: #Q10: +1m
                        print("We recommend signing up for the Casual Category")
                    elif freq > 2:
                        print("We recommend signing up for the Premium Category") #Q10: +1m
                    break
    elif check.lower() == "n":
        print("Thank you for using this program")
        break #Q9: +1m

'''
Task 2
Q8 : 1/3 marks
Q9 : 3/3 marks
Q10: 4/4 marks
Total: 8/10 marks
'''
