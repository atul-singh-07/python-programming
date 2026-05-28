class Student:
    college_name="ABC college" # class attributes
    def __init__(self,name,marks):
        self.name=name # object attributes
        self.marks=marks

    def welcome(self): #method 1
        print("Wlcome Student",self.name)

    def get_marks(self):# method 2
        return self.marks
    
s1=Student("Atul",97)
s1.welcome()
print(s1.get_marks())