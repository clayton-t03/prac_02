FILENAME = "guitars.csv"
guitars = []
print(
    "in myguitars.py, there is no error checking, please only input numbers for year and cost and whatever for the name \nplease follow menu prompts")


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.compare < other.compare


def read_guitars():
    in_file = open(FILENAME, "r")
    for line in in_file:
        guitar = line.strip().split(",")
        guitars.append(guitar)
        for i in range(len(guitars)):
            guitars[i][1] = int(guitars[i][1])
            guitars[i][2] = float(guitars[i][2])
    in_file.close()


def print_guitars():
    from operator import itemgetter
    guitars.sort(key=itemgetter(1))
    guitar_objects = {Guitar(*guitar) for guitar in guitars}
    for obj in guitar_objects:
        print(obj.name, "from", obj.year, "costs", obj.cost)


def quit():
    out_file = open(FILENAME, "w")
    for i in range(len(guitars)):
        print(f"{guitars[i][0]},{guitars[i][1]},{guitars[i][2]}", file=out_file)
    out_file.close()
    print("Thank you")


def add_guitars():
    choice = input("what would you like to: \n (A)dd a guitar \n (D)isplay guitars \n (Q) to quit \n >>>>")
    while choice != "Q":
        if choice == "A":
            new_name = input("name: ")
            new_year = int(input("year: "))
            new_cost = float(input("cost: "))
            new_guitar = [new_name, new_year, new_cost]
            guitars.append(new_guitar)
        elif choice == "D":
            print_guitars()
        choice = input("would you like to: \n (A)dd a guitar \n (D)isplay guitars \n (Q) to quit \n >>>>")
    quit()


read_guitars()
add_guitars()
