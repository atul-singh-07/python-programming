class Student:

    def __init__(self, name, marks):

        self.name = name          # Public variable
        self._course = "Python"   # Protected variable
        self.__marks = marks      # Private variable


    # Getter Method
    def get_marks(self):
        return self.__marks


    # Setter Method
    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")


obj = Student("Rahul", 85)

print("Name:", obj.name)

print("Course:", obj._course)

print("Marks:", obj.get_marks())


obj.set_marks(95)

print("Updated Marks:", obj.get_marks())