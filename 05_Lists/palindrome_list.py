# Q: Write a programme to check if a list contains a palindrome element 
# hint:Use copy() method.

list_1=[1,"abc",3,"abc",1]
temp=list_1.copy()

list_1.reverse()

if (temp==list_1):
    print("Palindrome List")
else:
    print("Not a Palindrome List")
