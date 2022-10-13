"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    global MENU, choice
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()


main()


def farenheit_to_celsius():
    global celsius
    farenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (farenheit - 32)


def celsius_to_farenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


while choice != "Q":
    if choice == "C":
        celsius_to_farenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        farenheit_to_celsius()
        print("Result: {:.2f} C".format(celsius))

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")