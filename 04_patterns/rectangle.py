# Q: Write a programme to enter two digits to control row and column of a rectangle.

# *****
# *****
# *****
# *****

n=int(input("Enter Row:"))
m=int(input("Enter Column:"))

for i in range(1,n+1):
    for j in range(1,m+1):
        print("*",end="") # end=" " → prevents newline after each star
    print() # working as a next line