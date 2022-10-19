def main():
    email_to_name = {} # creates empty dictioanry
    email = input("What is your email: ")

    while email != "":  # while email input is something
        name = get_name(email)
        confirm = input(f"is your name {name}? (Y/n)")
        if confirm != "" and confirm.upper() != "Y":  # if confirm is blank or a y/Y, proceed to enter name
            name = input("What is your name: ")  # renames name
        email_to_name[email] = name  # inputs name for correct email in email_to_name
        email = input("What is your email: ") # repeats loop

    for email, name in email_to_name.items():  # repeats the string below for all emails
        print(f"{name}'s email is {email}")


def get_name(email):
    before = email.split("@")[0]  # gets everything before @ symbol
    remove = before.split(".")  # removes . from before
    name = " ".join(remove).title()  # puts space where . was and adds capitals
    return name

main()
