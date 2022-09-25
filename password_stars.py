print("Your password needs to be a minimum of 8 characters long")
password = input("ENTER PASSWORD: ")
res = any(ele.isupper() for ele in password)
count = 0

if len(password) < 8:
    password = input("Password invalid, Please enter Password: ")
if res == False:
    password = input("Password invalid, Please enter Password: ")

for i in range(0, len(password)):
    if(password[i] != ' '):
        count = count + 1

print('*' * count)
