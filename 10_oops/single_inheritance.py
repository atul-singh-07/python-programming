class Car:
    color="Black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Toyotacar(Car):# single inheritance
    def __init__(self,name):
        self.name=name
car1=Toyotacar("Fotuner")
car2=Toyotacar("Prius")
print(car1.start())
