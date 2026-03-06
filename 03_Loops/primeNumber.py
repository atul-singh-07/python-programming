# Q: Write a programme to cheque whether the inputted number is a prime number or not.

n=int(input("Enter a number to check prime number:"))
a=0
for i in range(2,n-1):
    if(n%i==0):
        a=1
        break
if(n==0):
    print("Zero is Not a Prime number")
elif(a==0):
    print(n,"is a Prime Number")
else:
    print(n,"is not a prime number")