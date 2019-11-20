import requests
import json

TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOjEsIm5lZWRWZXJpZmljYXRpb24iOmZhbHNlLCJfaWQiOiI1ZGNmODE2NThmZDQzMjdkYjVlN2E2MjQiLCJuYW1lIjoiREZMQUJTIiwidXNlcm5hbWUiOiJkZmxhYnMiLCJlbWFpbCI6InRlY2hAZGZsYWJzLmNvbSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNTc0MTYyMDk2fQ.jUfTIinCwE8d3WJi-dtP1hGNnt_zX-k8rIJ-zEysik4'
BASE  = 'https://api.ztoh.id/'
URL   = BASE+'collaboration/chat/create'
head  = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + TOKEN
}
body  = {
    "sender": "5dcf81658fd4327db5e7a624",
	"message": "salam kenal, namaku tibo",
	"channel": "5dd36f20d685684288351d14",
	"type": "chat"
}

response = requests.post(URL, data=json.dumps(body), headers=head)
data     = response.json()
print(data)