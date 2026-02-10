ask = "y"

while ask.lower() == "y":

    a = int(input("Enter Date: "))
    b = input("Enter Name of Month: ").lower()# for handling both upper case and lower case
                                              # input we use lower()
    if a == 7 and b == "october":
        print("Atul")
    elif a == 22 and b == "june":
        print("Nancy")
    elif a == 20 and b == "june":
        print("Sameer")
    elif a == 11 and b == "september":
        print("Aayush")
    else:
        print("Not in Database")

    ask = input("Enter y to continue or n to exit: ")
print("Program Ended")