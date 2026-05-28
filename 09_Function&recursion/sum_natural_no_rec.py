n=int(input("Enter a number:"))

def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1) 

print("Sum of first n natural number is:",sum(n))