# Count Even and Odd Digits
# Input:
# n = 52846

# Output:
# Even digits = 4
# Odd digits = 1

# Hint:
# Use %10 to extract digits.
n=int(input("Enter a number:"))
CountEven=0
CountOdd=0
while(n!=0):
    ld=n%10
    if(ld%2==0):
        CountEven=CountEven+1
    else:
        CountOdd=CountOdd+1
    n=n//10
print("Even Digit =",CountEven)
print("Odd Digit:",CountOdd)