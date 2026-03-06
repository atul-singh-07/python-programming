# Palindrome Number
# Example: 121 → palindrome as reverse of 121 is: 121

n=int(input("Enter a number:"))
temp=n
r=0
while(n!=0):
    ld=n%10
    r=r*10
    r=r+ld
    n=n//10
if(temp==r):
    print("Entered Number:",temp,"is an Palindrome number")
else:
    print("The Number Entered is not a Palindrome Number")