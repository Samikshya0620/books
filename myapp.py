import requests
import json
URL ="http://127.0.0.1:8000/ucreate"

data = {
    'username':'Ram',
    'password' : 'abcde',
    'firstname' : 'Ram',
    'middlename' : 'Prasad',
    'lastname' : 'gyawali',
    'email' : 'ram2@gmail.com'
}

json_data = json.dumps(data)

r = requests.post(url =URL, data = json_data)
data = r.json()
print(data)