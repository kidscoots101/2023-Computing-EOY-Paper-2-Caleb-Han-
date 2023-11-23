while True:
    check = input("Do you want to check for membership eligibility?(y/n): ")
    if check.lower() == "y":
        while True: #Q8
            age = int(input("Enter your age: "))
            if age < 0:
                print("Please enter a positive number!")
            elif age >= 0:
                if age <= 18:
                    print("You are eligible for a Junior membership.")
                    break
                else:
                    print("You are eligible for an Adult membership.")
                    freq = int(input("How many times a week do you swim? "))
                    if freq <= 2:
                        print("We recommend signing up for the Casual Category")
                    elif freq > 2:
                        print("We recommend signing up for the Premium Category")
                    break
    elif check.lower() == "n":
        print("Thank you for using this program")
        break
