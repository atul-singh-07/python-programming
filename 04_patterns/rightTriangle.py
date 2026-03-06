# *
# **
# ***
# ****
# *****

n=int(input("Enter a number:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*",end="") # end=" " → prevents newline after each star
    print()