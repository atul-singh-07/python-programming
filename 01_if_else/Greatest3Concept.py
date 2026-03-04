# Take three numbers and print the largest one.

a=int(input("ENTER A:"))
b=int(input("ENTER B:"))
c=int(input("ENTER C:"))
if a>b & a>c: # if both are true then 1 & 1 then it will print
    print("A is greatest")
elif b>a & b>c:
    print("B is greatest")
else:
    print("C is greatest")

# Note: here in this code we have used single & which is a logical operator here it's seem's
#       to work like && in c but its not that 

# here in python we use (and) instead of &&

# IMP: python reads the condition as if a > (b & a) > c:
# thats why the logic of this code may look right but its not