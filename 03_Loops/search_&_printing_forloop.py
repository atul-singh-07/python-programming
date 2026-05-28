n=int(input("Enter a number:"))

a=[1,4,9,16,25,36,49,64,81,100]
# traversing
for i in a:
    print(i)

# searching
index=0
for i in a:
    if(n==i):
        print(i,"Founded at index",index)
    index=index+1