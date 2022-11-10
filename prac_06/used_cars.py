"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from pracs.prac_06 import car  ##doesn't work due to the way my folders are set up


def main():
    """Demo test code to show how to use car class."""
    my_car = car("hilux", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo_car = car("limo", 100)
    limo_car = add.fuel(20)
    print(f"{limo_car.name} has {limo_car.fuel} units of fuel")
    limo_car.drive(115)
    print(limo_car)


main()