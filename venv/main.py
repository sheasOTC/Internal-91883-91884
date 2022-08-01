import json
import os

if os.path.isdir('passwords.json') == False:
    with open('passwords.json','w') as passwords:
        json.dump({},passwords)
    else
    
