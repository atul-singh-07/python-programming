# Take three numbers and print the largest one.

a=int(input("ENTER A:"))
b=int(input("ENTER B:"))
c=int(input("ENTER C:"))

if a>=b and a>=c:# note: here in pyhton this (and) works as && in c
    print("A is greatest:",a)
elif b>=c and b>=a:
    print("B is greatest:",b)
else:
    print("C is greatest:",c)