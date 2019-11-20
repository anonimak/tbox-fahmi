import requests
import json

BASE  = 'https://api.ztoh.id/'
URL   = BASE+'users/sign-in'
body  = body = {
    "username": "dflabs",
    "password": "!@#QWEASDZXC"
}
head  = {'content-type': 'application/json'}
response = requests.post(URL, data=json.dumps(body), headers=head)
data  = response.json()
print(data)