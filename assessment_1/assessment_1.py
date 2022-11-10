movies = []
FILENAME = "movie_list.txt"
CATEGORIES = ["ACTION", "COMEDY", "DOCUMENTRY", "DRAMA", "THRILLER", "OTHER"]
MENU = print("MENU: \n(D)isplay movies\n(A)dd new movie\n(W)atch a movie\n(Q)uit")

def menu():
    print(MENU)
    choice = (input(">>>")).upper()
    while choice != "Q":
        if choice == "D":
            display_movies()
        elif choice == "A":
            new_movie()
        elif choice == "W":
            watch_movie()
    quit()



def read_movies_to_list():
    in_file = open(FILENAME, "r")
    for line in in_file:
        line = line.replace("\n", "")
        movie = line.split(",")
        movies.append(movie)
        for i in range(len(movies)):
            movies[i][2] = movies[i][2].upper()
    in_file.close()


def new_movie():
    new_movie_title = input("Movie Title: ")
    while new_movie_title == "":
        print("Invalid Movie Title")
        new_movie_title = input("Movie Title: ")
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
    print(CATEGORIES)
    new_movie_genre = input("Movie Genre: ")
    new_movie_genre = new_movie_genre.upper()
    print(new_movie_genre)
    if new_movie_genre not in CATEGORIES:
        print("Invalid movie genre, please enter one from list.")
        print(CATEGORIES)
        new_movie_genre = input("Movie Genre: ")
        new_movie_genre.upper()

    print(f"{new_movie_title} from {new_movie_year} added to movies list")
    new_movie = [new_movie_title, new_movie_year, new_movie_genre, "u"]
    movies.append(new_movie)


def display_movies():
    ##from operator import itemgetter """NOT WORKING ASK LINDSAY"""
    ##movies.sort(key=itemgetter(1, 0))
    number_of_movies = len(movies)

    for i in range(number_of_movies):
        print(f"{i}. {movies[i][3]} {movies[i][0]} - {movies[i][1]} ({movies[i][2]})")


def watch_movie():
    display_movies()
    number_of_movies = len(movies)
    movie_number = int(input("Select Number for movie to watch: "))
    if movies[movie_number][3] == 'w':
        print(f"You have already watched {movies[movie_number][0]}")
    else:
        print(f"You watched {movies[movie_number][0]} from {movies[movie_number][1]}")
        movies[movie_number][3].replace("u", "w")  # ASK LINDSAY


def quit():
    number_of_movies = len(movies)
    out_file = open(FILENAME, "w")
    for i in range(number_of_movies):
        print(f"{movies[i][0]},{movies[i][1]},{movies[i][2]},{movies[i][3]}", file=out_file)
    out_file.close()
    print("Have a good day")

menu()
