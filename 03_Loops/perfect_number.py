# Q: Check if a number is perfect.
#    Example: 6 → 1+2+3 = 6
# A perfect number is a positive integer that equals the sum of its proper divisors, 
# excluding the number itself. For example, 6 is a perfect number because its divisors 
# (1, 2, 3) add up to 6. Other examples include 28, 496, and 8128. All known perfect numbers are even.

n=int(input("Enter a number:"))
sum=0
for i in range (2,n-1): # here 
    divisor=n//i
    sum=sum+divisor
    print(divisor)
if(n==sum):
    print("The number:",n,"is an perfect number")
else:
    print("The number is not a Perfect number")



    ################################### Hold ################################