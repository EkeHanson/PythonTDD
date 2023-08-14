from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get(self):
        pass


class Car(Vehicle):
    # def get(self):
    #     print('You drive the car')
    pass

class Motorcycle:
    def get(self):
        print('You drive the motorcyle')


car = Car()
