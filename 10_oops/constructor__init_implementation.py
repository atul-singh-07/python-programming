class Student:

    # parameterized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("Adding new student in database....")

s1=Student("Atul",97)# object 1
print(s1.name, s1.marks)

s2=Student("Karan",100)# object 2
print(s2.name, s2.marks)