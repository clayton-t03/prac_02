score = int(input("What was your score? "))
if score < 0 or score > 100:
    print("Invalid score, please input number between 0 and 100")
    score = int(input("What was your score? "))


def main():
    MENU = "Present Results (1)\nPresent Stars (2)\nQuit (3)"
    print(MENU)
    choice = int(input(">>> "))
    if choice == 1:
        if score >= 90:
            print("Excellent")
            main()
        elif score >= 50:
            print("Passable")
            main()
        else:
            print("Bad")
            main()
    if choice == 2:
        print("*" * score)
        main()
    elif choice == 3:
        print("Thanks")
    elif choice <= 0 or choice > 3:
        print("Please make valid choice:")
        main()


main()





