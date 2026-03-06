# Q: Write a programme to print the pattern of a square.

# ****
# ****
# ****
# ****

n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="") # end=" " → prevents newline after each star
    print()# working as a next line
    