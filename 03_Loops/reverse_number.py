# Q: Write a programme to input a number and and print the reverse of that number.

n=int(input("Enter a number:"))
r=0
while(n!=0):
    ld=n%10
    r=r*10
    r=r+ld
    n=n//10 # performing integer division
print("The reversed Number is:",r)