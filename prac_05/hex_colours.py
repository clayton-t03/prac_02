COLOUR_TO_CODE = {"Alice Blue": "#f0f8ff", "Bulgarian Rose": "#480607", "Cameo Pink": "#efbbcc",
                  "Dark Sky Blue": "#8cbed6", "Eggshell": "#f0ead6", "Fire Opal": "#e95c4b",
                  "Generic Viridian": "#007f66", "Hollywood Cerise": "#f400a1", "Iceberg": "#71a6d2", "Jade": "#00a86b"}

colour_name = input("Colour: ").title()  # doesn't make it case dependant

while colour_name != "":  # While colour_name is an input and not a blank
    try:
        print(f"The code for colour {colour_name} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:  # if colour_name isn't apart of COLOUR_TO_CODE
        print("Invalid colour name")
    colour_name = input("Colour: ").title()
