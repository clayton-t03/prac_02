name = str(input("What is your name? "))
menu_string = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu_string)
choice = ""
while choice != "Q":
    choice = input("What would you like to do? ")
    if choice == "H":
        print("Hello", name)
        print(menu_string)
    elif choice == "G":
        print("Goodbye", name)
        print(menu_string)
    elif choice == "Q":
        print("Finished")
    else:
        print("INVALID CHOICE")
        print(menu_string)
