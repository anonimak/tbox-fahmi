import requests
import json

TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOjEsIm5lZWRWZXJpZmljYXRpb24iOmZhbHNlLCJfaWQiOiI1ZGNmODE2NThmZDQzMjdkYjVlN2E2MjQiLCJuYW1lIjoiREZMQUJTIiwidXNlcm5hbWUiOiJkZmxhYnMiLCJlbWFpbCI6InRlY2hAZGZsYWJzLmNvbSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNTc0MTYyMDk2fQ.jUfTIinCwE8d3WJi-dtP1hGNnt_zX-k8rIJ-zEysik4'
BASE  = 'https://api.ztoh.id/'
URL   = BASE+'users?search=email%3Dtest%2540test.com'
head  = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + TOKEN
}

response = requests.get(URL, headers=head)
data     = response.json()
print(data)