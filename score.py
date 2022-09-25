"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()

from random import randint
random_score = randint(0, 100)
print("The random score is: ", random_score)


