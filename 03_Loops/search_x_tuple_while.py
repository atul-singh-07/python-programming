#tuple:(1,4,9,16,25,36,49,64,81,100)

tup=(1,4,9,16,25,36,49,64,81,100)
n=int(input("Enter the number to search:"))

i=0
while i<len(tup):
    if(n==tup[i]):
        print("Number found at:",i)
        break
    
    i=i+1
print("Searching Ended")