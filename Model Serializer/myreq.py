import json 
import requests 



URL="http://127.0.0.1:8000/" 


# Get Data
def get_data( id = None):
    data={}
    
    if id is not None:
        data={'id':id}
        
    json_data=json.dumps(data)
    
    r=requests.get(url = URL , data = json_data)
     
    res_data=r.json()
    
    print(res_data)


# get_data()   



# Insert Data 
def post_data():
    data={
        'name':'Rohit',
        'age':12,
        'father_name':'rohit',
        'class_name':'5th',
        'grade':'4+',
    }
    
        
    json_data=json.dumps(data)
    
    r=requests.post(url = URL , data = json_data)
    
    res_data=r.json()
    
    print(res_data)

# post_data()


# Update Data 

def update_data():
    data={
        'id':1,
        'name':'abu bakar',
        'age':'18',
        'father_name':'Waheed Ahmad',
        'class_name':'5th',
        'grade':'4+',
    }
    
        
    json_data=json.dumps(data)
    
    r=requests.put(url = URL , data = json_data)
     
    res_data=r.json()
    
    print(res_data)

# update_data()




# Delete Data 
def delete_data(id):
    data={'id':id,}
    json_data=json.dumps(data)
    
    r=requests.delete(url = URL , data = json_data)
     
    res_data=r.json()
    
    print(res_data)

delete_data(4)