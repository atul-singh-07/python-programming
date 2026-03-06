# Armstrong Number 
# Example: 153 → 1³ + 5³ + 3³ = 153

n=int(input("Enter a  number:"))
countDigit=0
temp=n
temp2=n
sum=0
armstrong=0
# counting the number of digit on entered number
while(temp2!=0):
    countDigit=countDigit+1
    temp2=temp2//10
    
while(n!=0):
    ld=n%10
    sum=ld**countDigit
    armstrong=armstrong+sum
    n=n//10
if(temp==armstrong):
    print("Entered number:",temp,"is an Armstrong number")
else:
    print("The number is not a Armstrong Number")

# Note: this is ultimate armstrong code working on any digits of number