# Q: Write a programme to input a number and find its factorial.

n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1): # here used n+1 as the stop value is not itself included 
    fact=fact*i
print("The factorial of ",n,"is :",fact)