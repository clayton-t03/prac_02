import wikipedia


def search_and_suggest():
    user_input = input("What would you like to search: ")
    while user_input != "":
        print(wikipedia.search(user_input, results=3))
        user_choice = input("What one to summarise: ")
        try:
            print(wikipedia.summary(user_choice))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            return print("Please try another more specific query")
        print("Information gathered from:")
        user_choice = wikipedia.page(user_choice)
        print("Wikipedia title: ", user_choice.title)
        print(user_choice.url)
        user_input = input("What would you like to search: ")
    print("Thanks")


search_and_suggest()
