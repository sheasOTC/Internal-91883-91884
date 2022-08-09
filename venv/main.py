import json
import random
from datetime import datetime


def prompt():
    selection = input("Welcome to Passgen!\n "
                      "To generate a password enter: Generate\n "
                      "To store a password enter: Store\n "
                      "To list all passwords enter: List\n "
                      "To see details of a password enter: Inspect\n "
                      "To delete a password enter: Delete\n"
                      "To exit the program enter: Exit")
    if selection.lower() == "generate":
        use = input("What is usage for this password?\n")
        login = input("What is the login for this password\n")
        generate()
        print(f"A password for {use}")
    elif selection.lower() == "store":

    elif selection.lower() == "list":

    elif selection.lower() == "inspect":

    elif selection.lower() == "remove":

def generate(use, login):
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    if use in password:
        print(f"There is already a password for {use}.\n Please enter another use.")
    else:
        now = datetime.now()  # Gets the date and time
        dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        chars = list(
            '~!@#$%^&*()_+`1234567890-=qwertyuiop[]QWERTYUIOP{}|asdfghjkl;ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?')  # List of characters used for password generation
        generated = []
        for char in range(random.randint(8, 20)):  # Randomly generates length of password
            generated.append(chars[random.randint(0, 92)])  # Adds one random character to list
            joint = ''.join(generated)
        password[use] = {}
        password[use]["Email/Username"] = login
        password[use]["Password"] = joint
        password[use]["Date/Time"] = dateTime
    with open('passwords.json', 'w') as f:  # Gets the JSON file
        json.dump(password, f)  # Gets the JSON file to dump information


def store(use, login, key):
    with open('passwords.json', 'r') as f:
        password = json.load(f)
    if use in password:
        print(f"There is already a password for {use}.\n Please enter another use.")
    else:
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        password[use] = {}
        password[use]["Email/Username"] = login
        password[use]["Password"] = key
        password[use]["Date/Time"] = dateTime
    with open('passwords.json', 'w') as f:  # Stores user inputted information such as email and password
        json.dump(password, f)


def inspect(use):  # When user types a usage for a password that is valid it will print each detail about it
    with open("passwords.json", 'r') as f:
        password = json.load(f)
    if use in password:
        print(f"The details for {use} are " + "Email/Username:" + password[use]['Email/Username'] + " Password:" +
              password[use]["Password"] + " Date and Time:" + password[use]["Date/Time"])
    else:
        print(f"{use} does not exist.")


def list_usages():  # Lists every single usage for passwords
    with open('passwords.json', 'r') as f:
        password = json.load(f)
    for i in password:
        print(i)
    if len(password) == 0:  # Prints out statement if there are no passwords
        print("You have no passwords stored.")


def delete(use):
    with open("passwords.json", 'r') as f:
        password = json.load(f)
    if use in password:
        del password[use]  # Deletes user inputed
        with open("passwords.json", 'w') as f:
            json.dump(password, f)
        print(f"Deleted {use}")
    else:
        print(f"{use} does not exist.")


