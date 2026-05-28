from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started with Key")


class Bike(Vehicle):

    def start(self):
        print("Bike Started with Button")


c = Car()
b = Bike()

c.start()
b.start()