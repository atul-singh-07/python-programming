class Car:

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")


class Engine:

    @staticmethod
    def fuel():
        print("Diesel Engine")


class Fortuner(Car, Engine):

    def __init__(self, brand):
        self.brand = brand


car1 = Fortuner("Toyota")

print("Brand:", car1.brand)

car1.start()
car1.fuel()
car1.stop()