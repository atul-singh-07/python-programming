a=int(input("Enter A:"))
b=int(input("Enter B:"))

def product(a,b): # here if a=1 and b=1 and they are known as default parameter
    return a*b

print("Product is:",product(a,b))