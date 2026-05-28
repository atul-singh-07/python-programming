try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)


except ZeroDivisionError:
    print("Cannot divide by zero")


except ValueError:
    print("Invalid Input")


else:
    print("Division Successful")


finally:
    print("Program Ended")