# Check whether a given year is a leap year.

a=int(input("Enter the year:"))
if a%4==0:
    print(a,":is a leap year")
else:
    print(a,":is not a leap year")

# concept: leap year always come after four year then if a year is divided by four and its
#          remainder is equal to zero then its a leap year