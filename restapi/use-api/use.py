import requests
import json
BASE_URL="http://127.0.0.1:8000/"
ENDPOINT='api/updates/'

def get_list():
    req=requests.get(BASE_URL+ENDPOINT)
    print(json.dumps(req.json(),indent=1))
    print("Status code",req.status_code)
    data=req.json()
    #for obj in data:
    #    if obj['pk'] == 1:
    #        req2=requests.get(BASE_URL+ENDPOINT+str(obj['pk']))
    #        print(json.dumps(req2.json(),indent=2))

def create_list():
    new_data={
        'user':1,
        'content':'Another new cool update'
    }
    r=requests.post(BASE_URL+ENDPOINT,data=new_data)
    print(r.status_code)
    print(r.headers)
    print(json.dumps(r.json(),indent=1))

def delete_list():
    r=requests.delete(BASE_URL+ENDPOINT)
    print(r.headers)
    print(r.json())
    print(r.text)



get_list()
#create_list()
#delete_list()

