# Q: Write a programme to input a number and count the digit of that number.

n=int(input("Enter a number:"))
temp=n
count=0
while(n!=0):
    n=n//10 # performing integer division to reduce the number by eliminating lastdigit 1 by 1 
    count=count+1
print("Count of ",temp,"is:",count)