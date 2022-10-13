MINIMUM = 1
MAXIMUM = 45
NUMBERS_IN_LINE = 6

number_of_picks = int(input("how many quick picks: "))

from random import randint

for i in range(number_of_picks):
    quick_pick = []
    for j in range(NUMBERS_IN_LINE):
        number = randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick)) ## prints with spaces inbetween numbers
