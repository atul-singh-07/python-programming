# Difference between string and list.

# List: List are mutable which means u can make update or can have changes in list where 
# u can access the element of list using index values for printing and updation of list.
student=["karan",95.4,17,"Delhi"]
print(student)
print(student[0])

student[0]="Atul"
student[1]="99"
print(student[0])
print(student[1])

# String: String are immutable which means u cannot make changes to str using index values 
# whereas u can access the string element using index values.

a="AtulOs"
print(a[0])# --> u can access the element of str using index
print(a[4])

a[0]="T" #---> but in python updation is not allowed in string making it immutable[ERROR]
