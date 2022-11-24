from prac_09.unreliable_car import UnreliableCar
import random


def main():
    RELIABILITY = random.uniform(0, 100)
    my_unreliable_car = UnreliableCar("Batmobile", 100, RELIABILITY)
    my_unreliable_car.drive(60)
    print(my_unreliable_car)



main()
