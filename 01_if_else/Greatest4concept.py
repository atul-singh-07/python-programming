a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
d=int(input("Enter D:"))

if(a>=b and a>=c and a>=d):
    print("A is greatest")

elif(b>=a and b>=c and b>=d):
    print("B is greatest")

elif(c>=a and c>=b and c>=d):
    print("C is greatest")

else:
    print("D is greatest")