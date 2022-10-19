FILENAME = "wimbledon.txt"


def main():
    data = get_data(FILENAME)
    champion_to_titles, countries = analyze_data(data)
    display_data(champion_to_titles, countries)


def get_data(FILENAME):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() #skips first line
        for line in in_file:
            parts = line.strip().split(",") #remove commas
            data.append(parts) #puts parts into data (list)
        return data


def analyze_data(wimbledon):
    champion_to_titles = {} #creates new dictionary
    countries = [] #creates new list
    for data in wimbledon:
        countries.append(data[1]) #puts data into country lists
        countries = list(dict.fromkeys(countries)) #removes duplicates
        try:
            champion_to_titles[data[2]] += 1 #sums amount of titles each champion has
        except KeyError:
            champion_to_titles[data[2]] = 1
    return champion_to_titles, countries


def display_data(champion_to_titles, countries):
    print("Wimbledon Champions")
    for champion, titles in champion_to_titles.items():
        print(champion, titles)
    print(f"\nThese {len(countries)} countries have won wombledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
