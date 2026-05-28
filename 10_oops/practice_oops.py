class Student:

    def __init__(self,name,marks):
        print("Adding new student in database.....")
        self.name=name
        self.marks=marks

s1=Student("Atul",98)
print(s1.name,s1.marks)

s2=Student("Karan",100)
print(s2.name,s2.marks)
