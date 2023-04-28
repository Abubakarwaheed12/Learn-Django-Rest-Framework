# test our first api

import requests 
import json 

URL='http://127.0.0.1:8000/students/'

r=requests.get(url = URL)

data=r.json()

print(r)
print(data)