FILENAME = "guitars.csv"

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
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        guitar = line.strip().split(",")
        guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    in_file.close()
    return guitars


def print_guitars(guitars):
    for obj in guitars:
        print(obj.name, "from", obj.year, "costs", obj.cost)


def quit(guitars):
    out_file = open(FILENAME, "w")
    for i in range(len(guitars)):
        print(f"{guitars[i].name},{guitars[i].year},{guitars[i].cost}", file=out_file)
    out_file.close()
    print("Thank you")


def main():
    guitars = read_guitars()
    choice = input("what would you like to: \n (A)dd a guitar \n (D)isplay guitars \n (Q) to quit \n >>>>")
    while choice != "Q":
        if choice == "A":
            guitars.append(add_guitar())
        elif choice == "D":
            print_guitars(guitars)
        choice = input("would you like to: \n (A)dd a guitar \n (D)isplay guitars \n (Q) to quit \n >>>>")
    quit(guitars)


def add_guitar():
    new_name = input("name: ")
    new_year = int(input("year: "))
    new_cost = float(input("cost: "))
    new_guitar = Guitar(new_name, new_year, new_cost)
    return new_guitar


main()
