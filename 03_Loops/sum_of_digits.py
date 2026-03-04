# Q: Write a programme to input a number and sum all the digits contained in that number.

n=int(input("Enter a number:"))
sum=0
while(n!=0):
    ld=n%10 # here ld:lastdigit
    sum=sum+ld
    n=n//10 # performing integer division
print("Sum:",sum)
