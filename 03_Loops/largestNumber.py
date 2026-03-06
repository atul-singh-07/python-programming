# 5️⃣ Find Largest Digit in a Number
# Input:
# Enter number: 52964
# Output:
# Largest digit = 9
# Hint:
# Compare every digit while extracting.

n=int(input("Enter a number:"))
max=-1
while(n!=0):
    ld=n%10
    if(ld>max):
        max=ld
    n=n//10
print("Max number:",max)