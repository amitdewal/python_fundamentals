from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    # abstract class can have concreate method also
    def fuel_capacity(self):
       print("Every vehicle has a fuel capacity")

class Car(Vehicle):
    def start(self):
        print("car is Starting with ignition")
        self.fuel_capacity()

    def stop(self):
        print("car is Stopping with brake")

class Bike(Vehicle):
    def start(self):
        print("bike is Starting with kick")
        self.fuel_capacity()

    def stop(self):
        print("bike is Stopping with hand brake")


car1 = Car()
bike1 = Bike()

car1.start()
car1.stop()

bike1.start()
bike1.stop()

# TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'start', 'stop'
#
# v = Vehicle()
# v.start()
# v.stop()
