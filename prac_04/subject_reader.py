"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  #
        parts[2] = int(parts[2])  #makes number integer
        print(parts)  # See if that worked
        data.append(parts)
    input_file.close()
    return data


def display(data):
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]:12} and has {subject_data[2]:3} students.")


main()
