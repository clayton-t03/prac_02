name = input("What is your name? ")

NAME_FILE = "name.txt"
out_file = open(NAME_FILE, 'w')
print(name, file=out_file)
out_file.close()

in_file = open("name.txt")
for line in in_file:
    print("Your name is:",line)
in_file.close()


sum_of_numbers = 0
in_file = open("numbers.txt")
for i in range(2):
    line = in_file.readline()
    number = int(line)
    sum_of_numbers = sum_of_numbers + number
print(sum_of_numbers)
in_file.close()

#would need more numbers

sum_of_numbers = 0
how_many_numbers = int(input("How many numbers would you like to add? "))
in_file = open("numbers.txt")
for i in range(how_many_numbers):
    line = in_file.readline()
    number = int(line)
    sum_of_numbers = sum_of_numbers + number
print(sum_of_numbers)
in_file.close()



