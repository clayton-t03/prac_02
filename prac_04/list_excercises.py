numbers = []
for i in range(5):
    number = int(input(f"What is your {i + 1} number: "))
    numbers.append(number)

print(f"the first number is {numbers[0]}")
print(f"the last number is {numbers[4]}")
print(f"the smallest number is {min(numbers)}")
print(f"the largest number is {max(numbers)}")
average = sum(numbers) / 5
print(f"the sum of numbers is {sum(numbers)}, the average number is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access Granted")
    print(f"Welcome {username} ")
else:
    print("Access Denied")