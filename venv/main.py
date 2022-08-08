import json
import os.path
import random
from datetime import datetime

if not os.path.isfile(
        'passwords.json'):  # Checks if passwords.json file exists. Creates and writes a {} if file does not exist
    with open('passwords.json', 'w') as passwords:
        json.dump({}, passwords)
else:
    pass


def generate(use, id):
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    if use in password:
        print(f"There is already a password for {use}.\n Please enter another use.")
    else:
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        chars = list('~!@#$%^&*()_+`1234567890-=qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?')  # List of characters used for password generation
        generated = []
        for char in range(random.randint(8, 20)):
            generated.append(chars[random.randint(0, 92)])
            joint = ''.join(generated)
        password[use] = {}
        password[use]["Email/Username"] = id
        password[use]["Password"] = joint
        password[use]["Date/Time"] = dateTime
    with open('passwords.json', 'w') as f:  # Gets the JSON file
        json.dump(password, f)  # Dumps all entered content into the JSON file


def store(use, id, key):
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    if use in password:
        print(f"There is already a password for {use}.\n Please enter another use.")
    else:
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        password[use] = {}
        password[use]["Email/Username"] = id
        password[use]["Password"] = key
        password[use]["Date/Time"] = dateTime
    with open('passwords.json', 'w') as f:  # Gets the JSON file
        json.dump(password, f)



def inspect(use):
    with open("passwords.json", 'r') as f:
        password = json.load(f)
    print(f"The details for {use} are " + "Email/Username:" + password[use]['Email/Username'] + " Password:" + password[use]["Password"] + " Date and Time:" + password[use]["Date/Time"])

def listUsages():
    with open('passwords.json', 'r') as f:  # Gets the JSON file
        password = json.load(f)
    for i in password:
        print(i)


inspect('school')
