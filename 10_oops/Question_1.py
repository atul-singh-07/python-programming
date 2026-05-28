# Create student class that takes name and marks of three subjects as arguments in constructor .
# Then create a method to print the average. 

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self): #method
        sum=0
        for i in self.marks:
            sum=sum+i
        print("hi",self.name,"ypur average score is:",sum/3)
        
s1=Student("Atul",[99,98,97])
s1.get_avg()