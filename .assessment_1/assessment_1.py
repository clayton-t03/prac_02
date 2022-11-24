"""https://github.com/cp1404-students/a1-movies-clayton-t03"""

movies = []
FILENAME = "movie_list.txt"
CATEGORIES = ["ACTION", "COMEDY", "DOCUMENTRY", "DRAMA", "THRILLER", "OTHER"]
MENU_STRING = "MENU: \n(D)isplay movies\n(A)dd new movie\n(W)atch a movie\n(Q)uit"


def menu():
    """Menu function generates menu and assigns functions for key inputs"""
    print(MENU_STRING)
    choice = (input(">>>")).upper()
    while choice != "Q":
        if choice == "D":
            display_movies()
        elif choice == "A":
            new_movie()
        elif choice == "W":
            watch_movie()
        else:
            print("Invalid choice")
        print(MENU_STRING)
        choice = (input(">>>")).upper()
    quit()
    print("Thank You")


def read_movies_to_list():
    """reads from file and converts to list"""
    in_file = open(FILENAME, "r")
    for line in in_file:
        line = line.replace("\n", "")
        movie = line.split(",")
        movies.append(movie)
        for i in range(len(movies)):
            movies[i][0] = movies[i][0].title()
            movies[i][2] = movies[i][2].upper()
            movies[i][1] = int(movies[i][1])
    in_file.close()


def new_movie():
    """generates a new movie"""
    new_movie_title = input("Movie Title: ").title()
    while new_movie_title == "":
        print("Invalid Movie Title")
        new_movie_title = input("Movie Title: ").title()
    while True:
        try:
            new_movie_year = int(input('Movie Release Year: '))
            if new_movie_year <= 0:
                print("Movie Release date must be greater than 0")
                new_movie_year = int(input('Movie Release Year: '))
            break
        except ValueError:
            print('Incorrect input, please input valid year: ')
            continue

    print("Please select genre from following categories:")
    print(f"{CATEGORIES[0]}, {CATEGORIES[1]}, {CATEGORIES[2]}, {CATEGORIES[3]}, {CATEGORIES[4]}, {CATEGORIES[5]}")
    new_movie_genre = input("Movie Genre: ")
    new_movie_genre = new_movie_genre.upper()
    if new_movie_genre not in CATEGORIES:
        print("Invalid movie genre, please enter one from list.")
        print(f"{CATEGORIES[0]}, {CATEGORIES[1]}, {CATEGORIES[2]}, {CATEGORIES[3]}, {CATEGORIES[4]}, {CATEGORIES[5]}")
        new_movie_genre = input("Movie Genre: ")
        new_movie_genre.upper()

    print(f"{new_movie_title} from {new_movie_year} added to movies list")
    new_movie = [new_movie_title, new_movie_year, new_movie_genre, "u"]
    movies.append(new_movie)


def display_movies():
    """displays movies"""
    count = 0
    number_of_movies = len(movies)
    for i in range(number_of_movies):
        if movies[i][3] == "w":
            count = count + 1
    number_of_movies = len(movies)
    from operator import itemgetter
    movies.sort(key=itemgetter(1, 0))
    for movie in movies:
        max_length = max(len(movie[0]) for movie in movies)
    for i in range(number_of_movies):
        if movies[i][3] == "u":
            movies[i][3] = "*"
        else:
            movies[i][3] = " "
        dash = "-"
        length = max_length + 2 - int(len(movies[i][0]))
        print(f"{i:>3}. {movies[i][3]} {movies[i][0]} {dash:>{length}} {movies[i][1]:>{3}} ({movies[i][2]})")

        if movies[i][3] == "*":
            movies[i][3] = "u"
        else:
            movies[i][3] = "w"
    print(f"{count} movies watched, {len(movies) - count} movies still to watch")


def watch_movie():
    """changes u to w"""
    count = 0
    number_of_movies = len(movies)
    for i in range(number_of_movies):
        if movies[i][3] == "w":
            count = count + 1
    if count == number_of_movies:
        print("All movies have been watched")
    else:
        display_movies()

        while True:
            try:
                movie_number = int(input("Select Number for movie to watch: "))
                if movie_number < 0:
                    print("Invalid input")
                    movie_number = int(input("Select Number for movie to watch: "))
                break
            except ValueError:
                print("Incorrect input")
                continue

        if movies[movie_number][3] == 'w':
            print(f"You have already watched {movies[movie_number][0]}")
        else:
            print(f"You watched {movies[movie_number][0]} from {movies[movie_number][1]}")
            movies[movie_number][3] = "w"


def quit():
    """saves list to file"""
    number_of_movies = len(movies)
    out_file = open(FILENAME, "w")
    for i in range(number_of_movies):
        print(f"{movies[i][0]},{movies[i][1]},{movies[i][2]},{movies[i][3]}", file=out_file)
    out_file.close()
    print("Have a good day")


def main():
    """starts program"""
    print("Assessment - 1; Movies to watch by Clayton Tozer")
    read_movies_to_list()
    number_of_movies = len(movies)
    print(f"{number_of_movies} loaded from {FILENAME}.")
    menu()


main()
