# abstraction: Hiding the implementation detail of a class and only showing the essential
#              feature to the user.

class Car:

    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def starts(self):
        self.acc=True
        self.clutch=True
        print("Car Started.....")

car1=Car()
car1.starts()

# output=car started ... we dont get to know that acc got true and clutch get true