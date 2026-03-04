# Q: Write a programme to tell whether an inputed number is a strong number or not.

#    strong number:A number is strong if sum of factorial of its digits equals the number.
#                  Example: 145 → 1! + 4! + 5! = 145

n=int(input("Enter a number:"))
temp=n
sum=0
while(n!=0):
    ld=n%10
    n=n//10 # /:floating division and //:integer division
    
    fact=1
    for i in range(1,ld+1):# if n=123 than ld=3 then i--> 1 2 3 
        fact=fact*i
    
    sum=sum+fact
if(temp==sum):
    print("The number:",temp,"is a strong number")
else:
    print("Not a strong number")