import json
import os.path
import random

if os.path.isfile(
        'passwords.json') == False:  # Checks if passwords.json file exists. Creates and writes a {} if file does not exist
    with open('passwords.json', 'w') as passwords:
        json.dump({}, passwords)
else:
    pass


def generate(use, id):
    with open('passwords.json', 'w') as passwords: #Gets the JSON file
        password = json.load(passwords)
    if use in password:
        print(f"There is already a password for {use}.\n Please enter another use.")
    else:
        chars = list('~!@#$%^&*()_+`1234567890-=qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?') #List of characters used for password generation
        generated = []
        for char in range(random.randint(8, 20)):
            generated.append(chars[random.randint(0, 92)])
            joint = ''.join(generated)
        passwords[use] = {}
        passwords[use]["Email/Username"] = id
        passwords[use]["Password"] = joint
    json.dump(password,passwords) #Dumps all entered content into the JSON file

generate("william's chin","scottw@stu.otc.school.nz")
