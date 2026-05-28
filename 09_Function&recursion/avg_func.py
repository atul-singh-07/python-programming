a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

def avg(a,b,c):# funtion definition
    sum=a+b+c
    avg=sum/3
    return avg

print("Average of A B C is:",avg(a,b,c))# function call