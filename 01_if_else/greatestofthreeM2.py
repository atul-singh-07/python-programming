# method:02
# by nested if and else statements
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if(a>b):
    if(a>c):
        print("A is greatest:",a)
    else:
        print("C is greatest:",c)
else:
    if(b>c):
        print("B is greatest:",b)
    else:
        print("C is greatest:",c)