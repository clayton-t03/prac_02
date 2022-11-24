from prac_09.car import Car
from random import randint

RELIABILITY = randint(1, 100)

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, current reliability {self.reliability:.2f}"

    def drive(self, distance):
        if RELIABILITY < distance:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
            print("Reliability more than distance")
        return distance_driven