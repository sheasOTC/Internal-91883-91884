import json
import time
from cryptography.fernet import Fernet
import random
from datetime import datetime
import os.path
import atexit

if not os.path.exists('key.key'):  # Checks if file exist; ensures that key file is not replaced.
    with open('key.key', 'wb') as f:
        key = Fernet.generate_key()
        f.write(key)  # Creates and stores key for encryption/decryption

try:
    with open('passwords.json', 'w') as f:
        json.dump({}, f)
except:
    pass


def prompt():
    decode()
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    selection = input("Welcome to Passgen!\n "
                      "To generate a password enter: Generate\n "
                      "To store a password enter: Store\n "
                      "To list all uses for passwords enter: List\n "
                      "To see details of a password enter: Inspect\n "
                      "To delete a password enter: Delete\n "
                      "To stop during a command enter: Stop\n "
                      "To exit the program enter: Exit\n "
                      "Note: Stop cannot be used for any usage/login/password. (Not Caps Sensitive)\n")

    if selection.lower() == "generate":
        use = input("What is usage for this password?\n")
        if use.lower() == "stop": prompt()  # Checks if "stop" is typed during any points during the prompts
        while use in password:  # Continuously checks if variable use is in the passwords.json file asking to enter a new one until user enters non-taken usage
            if use.lower() == "stop": prompt()
            use = input(f"{use} is already being used for a password. Please enter another\n")
        login = input("What is the login for this password\n")
        if login.lower() == "stop": prompt()
        generate(use, login)
        prompt()  # Re-runs the selection text

    elif selection.lower() == "store":
        use = input("What is usage for this password?\n")
        if use.lower() == "stop": prompt()
        while use in password:
            if use.lower() == "stop": prompt()
            use = input(f"{use} is already being used for a password. Please enter another\n")
        login = input("What is the login for this password\n")
        if login.lower() == "stop": prompt()
        keyword = input(f"What is the password for {use}?\n")
        if keyword.lower() == "stop": prompt()
        store(use, login, keyword)
        print(f"Password for {use} has successfully been stored\n")
        prompt()

    elif selection.lower() == "list":
        list_usages()
        prompt()

    elif selection.lower() == "inspect":
        if len(password) == 0:  # Checks if any passwords are stored in passwords.json file
            print("You have no passwords stored.")
            prompt()
        else:
            use = input("What is usage for this password?\n")
            if use.lower() == "stop": prompt()
            while use not in password:
                if use.lower() == "stop": prompt()
                use = input(f"Please enter a valid usage.\n")
            inspect(use)
            prompt()

    elif selection.lower() == "delete":
        if len(password) == 0:
            print("You have no passwords stored.")
            prompt()
        else:
            use = input("What is the use of the password you want to delete? (Caps Sensitive)\n")
            if use.lower() == "stop": prompt()
            while use not in password:  # Checks if there is a name that exist
                if use.lower() == "stop": prompt()
                use = input(f"{use} is not a password. Please enter correctly. (Caps Sensitive)\n")
            delete(use)
            print(f"Successfully deleted {use}\n")
            prompt()

    elif selection.lower() == "exit":
        print("Exiting Passgen")
        encode()
        time.sleep(0.5)
        quit()
    else:
        print(f"{selection} is not valid.")
        prompt()
    encode()


def generate(use, login):
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    decode()
    now = datetime.now()  # Gets the date and time
    dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    chars = list(
        '~!@#$%^&*()_+`1234567890-=qwertyuiop[]QWERTYUIOP{}|asdfghjkl;ASDFGHJKL:zxcvbnm,./ZXCVBNM<>?')  # List of characters used for password generation
    generated = []
    numchars = len(chars)
    for char in range(random.randint(8, 20)):  # Randomly generates length of password
        generated.append(chars[random.randint(0, numchars)])  # Adds one random character to list
        joint = ''.join(generated)
    password[use] = {}  # Gets data ready to be dumped into JSON file
    password[use]["Email/Username"] = login
    password[use]["Password"] = joint
    password[use]["Date/Time"] = dateTime
    print(f"The password for {use} is {joint}\n")
    with open('passwords.json', 'w') as f:  # Gets the JSON file
        json.dump(password, f)  # Gets the JSON file to dump information
    encode()


def store(use, login, keyword):
    decode()
    with open('passwords.json', 'r') as f:
        password = json.load(f)
    now = datetime.now()
    dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    password[use] = {}
    password[use]["Email/Username"] = login
    password[use]["Password"] = keyword
    password[use]["Date/Time"] = dateTime
    with open('passwords.json', 'w') as f:  # Stores user inputted information such as email and password
        json.dump(password, f)
    encode()


def inspect(use):  # When user types a usage for a password that is valid it will print each detail about it
    decode()
    with open("passwords.json", 'r') as f:
        password = json.load(f)
    if use in password:
        print(f"The details for {use}: \n" + "Email/Username:" + password[use]['Email/Username'] + " \nPassword:" +
              password[use]["Password"] + " \nDate and time of creation:" + password[use]["Date/Time"] + "\n")
    else:
        print(f"{use} does not exist.")
    encode()


def list_usages():  # Lists every single usage for passwords
    decode()
    with open('passwords.json', 'r') as f:
        password = json.load(f)
    for i in password:
        print(i)
    if len(password) == 0:  # Prints out statement if there are no passwords
        print("You have no passwords stored.")
    encode()


def delete(use):
    decode()
    with open("passwords.json", 'r') as f:
        password = json.load(f)
    if use in password:
        del password[use]  # Deletes user inputted
        with open("passwords.json", 'w') as f:
            json.dump(password, f)
    else:
        print(f"{use} does not exist.")


def encode():
    with open('passwords.json', 'rb') as f:
        data = f.read()
    encrypted = getkey().encrypt(data)
    if os.path.isfile('passwords.json'):
        os.remove('passwords.json')
    with open('encrypted.json', 'wb') as e:
        e.write(encrypted)


def decode():
    with open('encrypted.json', 'rb') as e:
        encrypted = e.read()
    decrypted = getkey().decrypt(encrypted)
    with open('passwords.json', 'w') as f:
        f.write(decrypted.decode())


def getkey():
    with open('key.key', 'rb') as k:
        key = k.read()
    return Fernet(key)


prompt()
atexit.register(encode())  # Used to run encoding while program is shutdown
