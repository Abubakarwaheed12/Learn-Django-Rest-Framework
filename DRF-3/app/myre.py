# test our first api

import requests 
import json 

URL='http://127.0.0.1:8000/students/'

data={
    'name':'hamza',
    'age':18,
}

json_data = json.dumps(data)

# get request  
# r=requests.get(url = URL)

# post request

r = requests.post(url=URL , data=json_data)

data=r.json()

print(data)

